# Transactional outbox and Hangfire background jobs

Updated: 8 October 2026. Planning design; no application code, database schema or worker deployment has been created.

## Confirmed direction and remaining design work

**Confirmed by the user on 8 October 2026:** Use the **transactional outbox pattern with Hangfire** for reliable external effects and appropriate lengthy or scheduled workflows. This includes reliable accounting synchronization and notifications, along with imports, exports, reports and scheduled checks where needed. Apply it selectively according to durability and execution needs; a service's size alone does not determine whether it runs in the background.

**AUD-22: Approved Direction.** Atomic outbox persistence, durable integration events where needed, reliable dispatch/retries, idempotent external operations, crash recovery, clear failure states and separation of urgent/bulk work are approved requirements. The detailed mechanisms below are engineering design for that direction. Exact schemas, states, job contracts, package versions, hosting topology, batch sizes, concurrency limits, polling intervals, retry limits, retention and alert thresholds remain developer design work. Business rules recorded as open or deferred in other documents remain unresolved. This decision does not authorize application implementation or Azure provisioning.

Use the `api-pattern` skill and its reliability, module-boundary, data/performance and verification references for future backend work. Motmaan currently has no existing Hangfire infrastructure; historical examples in that skill are not evidence of installed packages here.

## Responsibilities and workflow selection

| Responsibility | Planned approach |
|---|---|
| Authorization, validation and critical local state | The owning application use case enforces action permission and branch/patient/resource scope and commits related SQL changes with concurrency protection |
| Work that must follow a successful commit | Persist its outbox record in the same SQL transaction as the business changes |
| Durable execution, delayed/recurring work and retries | Hangfire executes jobs with their own dependency scope and cancellation lifetime |
| Large workflows with several committed steps | Persist operation/step state, checkpoints and external references; Hangfire invokes the next eligible step |
| Client progress and results | An authorized application API exposes durable operation state, separate from internal Hangfire job state |

Recommended uses in Motmaan:

- **Payments and Qoyod:** After authenticated, backend-verified payment/refund handling, commit the valid Motmaan state transition and required accounting outbox work together. Synchronize Qoyod afterward and retain its references and reconciliation status. An accounting outage must be visible separately from verified payment and appointment state. Official invoice availability depends on successful Qoyod issuance.
- **Notifications:** Persist required delivery work for booking changes, doctor readiness, approved recruitment invitations, ticket updates, rating invitations and weekly summaries. Recheck recipient access, eligibility and expiry before delivery; provider acceptance does not prove that a person received or read a message.
- **Scheduled work:** Use Hangfire for appointment/task reminders, hold-expiry checks, no-show checks and approved retention work. Store the authoritative due time and relevant version/state in SQL. Patient-task recurrence follows `Asia/Riyadh`; event instants are persisted in UTC.
- **Large processing:** Use durable job execution for approved imports, exports, report generation and recording post-processing. Store files in approved private storage and process bounded batches. Emdaad migration and assessment contracts remain deferred; display-language behavior is confirmed in document 03 while vendor/format/privacy details remain open.

Reservation capacity, wallet spending, package consumption and compensation invariants require SQL transaction/concurrency protection wherever the work executes. Keep external HTTP calls and lengthy processing outside database transactions. OTP delivery requires its own timely, expiry-aware path; do not place it behind bulk jobs or assume all messaging has the same latency needs.

## Transaction and dispatch flow

1. Authenticate and authorize the request or provider callback, validate its input, and resolve the trusted resource scope. For incoming provider events, record a deduplication identity and enforce legal state transitions; an incoming-event record is distinct from an outgoing outbox record.
2. The owning use case stages the business changes and required outbox entries on the same unit of work. Commit them atomically in Azure SQL. A single EF save covers its writes; protect earlier reads and competing writes explicitly where an invariant requires it.
3. Return the committed business outcome. For a genuinely asynchronous operation, return an application operation reference and pending state under an agreed API contract; acceptance is not completion of the remote effect.
4. A continuously available dispatcher scans bounded batches of due outbox work and claims entries atomically using an expiring lease or equivalent concurrency control. It enqueues Hangfire jobs using durable identifiers.
5. A job loads the identified work, checks whether it is already complete or obsolete, verifies the applicable scope and eligibility, and executes its effect. It persists progress, provider references and the final result. Only successful completion of the agreed effect marks that delivery complete; permanent failure remains visible for authorized recovery.

**The SQL commit and Hangfire enqueue are separate durability boundaries**, even if both use the same database. Ordinary EF saving followed by `BackgroundJob.Enqueue` is not assumed atomic. If enqueue fails, the committed outbox entry stays recoverable. If enqueue succeeds but recording that enqueue fails, recovery may enqueue it again. The job therefore tolerates duplicate execution. Persist dispatch/job references and recover expired claims or stalled work deliberately rather than enqueueing every pending entry on every scan. Record enqueue status separately from delivery completion.

Proposed outbox data includes event/delivery ID, event type and schema version, source entity/operation ID, branch/resource references, created/due UTC instants, minimal payload or immutable data reference, dispatch/execution state, attempt count, next attempt, lease owner/expiry, Hangfire reference, safe failure code, provider reference and completion instant. Final names and fields are open. Where one event triggers several effects, track each destination independently so a successful notification is not repeated solely because Qoyod failed.

## Retry, deduplication and external outcomes

- Design for **at-least-once execution**. Neither an outbox nor Hangfire supplies exactly-once business effects automatically. Use unique operation/delivery keys and database constraints; concurrent duplicate jobs must not duplicate local financial entries or entitlement changes.
- Use provider idempotency keys or unique external references where supported. A crash after a provider succeeds but before Motmaan saves that success creates an unknown outcome. Query/reconcile using the persisted operation identity before repeating a charge, refund or invoice creation. If a provider cannot safely deduplicate or reveal the result, route the ambiguity to review rather than blindly retrying. Provider guarantees remain to verify.
- Retry transient failures with bounded backoff and rate limits. Do not retry invalid requests, permanent permission denial, obsolete reminders or rejected business transitions as technical failures. Coordinate Hangfire retry behavior with outbox scheduling so two independent retry loops do not multiply calls.
- Preserve required ordering for an individual booking/payment/accounting operation using persisted versions or sequence checks. Multiple workers do not automatically preserve event order. Unrelated operations may run concurrently within measured limits.
- When retries are exhausted, retain actionable failure state and alert the responsible operator. Authorized replay uses the same business identity and rechecks current eligibility. Audit recovery actions.

## Large workflows and time-sensitive checks

Split a growing service into clear use cases and workflow steps when their responsibilities diverge. Persist which step is pending, running, completed, failed or awaiting review, with input references, completed checkpoints and safe errors. Each step owns a short local transaction; retry resumes from verified checkpoints. An import that commits batches must report partial progress and row errors rather than promise whole-file atomicity.

Hangfire sequences or continuations can help schedule steps, but the persisted business workflow state determines eligibility and recovery. A remote payment, delivered message or issued document cannot be undone by rolling back a later SQL transaction. Define correction/compensation and manual review for each affected workflow before implementation; this decision does not select automatic refund or cancellation rules.

Jobs that expire a hold, classify a no-show or send a reminder must atomically recheck the current appointment/task version, authoritative deadline and attendance/payment state. Rescheduling, cancellation, completion or a task-schedule edit makes stale jobs harmless. Server eligibility must use the stored deadline even if the cleanup job runs late; a delayed worker must not extend a seven-minute payment hold. Exact late-payment treatment remains deferred in [booking and finance](02-booking-and-finance.md).

Hangfire execution may be delayed by polling, load or downtime; it is not a guarantee of execution at an exact instant. Its recurring scheduler checks on a minute interval. Choose dispatcher and delayed-job polling behavior from agreed latency targets; reminders, doctor-ready messages and hold/no-show processing have different needs. Persist due work and define recovery after downtime, including suppressing expired or obsolete messages.

## Hosting, security and operation

- **Proposed starting storage:** Use Hangfire SQL Server storage with the selected Azure SQL Database, in a dedicated Hangfire schema. Business and outbox tables share the transaction boundary; Hangfire persistence remains separate. A separate job database/worker host is an option after measuring contention and identifying isolation needs. Redis remains the selected cache service, not the only durable store for this work.
- Run dispatch and job processing in a host that stays available independently of browser requests. Hosting alongside the API requires validated always-on behavior and restart recovery; a separate worker process can isolate bulk work and be scaled when justified. The final host and resources remain open.
- Separate latency-sensitive notification/integration work from bulk imports/reports using queues and bounded worker allocation. Bound provider calls and SQL concurrency; never run concurrent EF operations on one DbContext. Measure the workload before setting worker counts or adding infrastructure.
- Jobs receive identifiers and resolve their own scoped dependencies. Persist durable inputs first; do not serialize HttpContext, request streams, access tokens, OTPs, full clinical records or request-scoped service instances into job arguments. Preserve required financial/policy snapshots without unnecessary sensitive payloads.
- Recheck current resource scope and recipient consent/access when generating exports or delivering protected information. System integration jobs use explicit service authority and the scope of the committed operation; they do not impersonate a requester with a saved session token. Define the effect of revocation on each job without silently abandoning required financial reconciliation.
- Restrict the Hangfire dashboard and replay controls to specifically authorized operators. Use least-privilege runtime database access and a separate reviewed schema-deployment identity. Protect job/outbox data, logs, artifacts and backups; apply a defined retention policy.
- Monitor oldest due work, pending/failed counts, execution latency, retries, stalled leases, provider errors, accounting mismatches and worker health. Set alert thresholds and recovery ownership before production. Hangfire success means the job ran successfully; payment, message delivery and official invoicing need their own domain/provider evidence.

## Client handoff

Web and Flutter use application API state. Where a workflow is asynchronous, agree operation references, safe status/progress, refresh or bounded polling, resume after connection loss, denial, failure and retry behavior. Queued work is pending; a push message or checkout redirect does not establish success. Keep accounting-sync status separate from appointment/payment state. Downloads require a fresh authorization check. Clients receive neither outbox payloads nor Hangfire administrative access.

Exact endpoint names, response fields, status codes, polling limits and permitted retry/cancel actions are still contract work in the [shared checklist](../handoff/shared-contract-checklist.md).

## Verification required when implementation starts

Verify with Azure SQL/SQL Server behavior and representative workloads:

- Business transaction rollback leaves neither its changes nor its outbox work committed; a crash immediately after commit leaves recoverable work.
- Crashes before/after enqueue and before/after an external effect recover without losing work or duplicating financial effects; ambiguous provider outcomes enter reconciliation/review.
- Duplicate and out-of-order provider events, overlapping workers and lease expiry preserve state/concurrency invariants and required ordering.
- Provider outage, exhausted retries and authorized replay produce truthful progress and actionable failures; bulk jobs do not starve time-sensitive work.
- Reschedule/cancel/attendance/payment changes make stale deadline and reminder jobs harmless; recovery after downtime respects expiry and existing deferred business decisions.
- Scope/consent revocation blocks unauthorized exports or delivery; operation polling and result files reject cross-patient/cross-branch identifiers. Dashboard access and replay require explicit permission.
- Imports resume from checkpoints with correct counts; app/web return or reconnect displays API-authoritative state. Logs and job arguments exclude sensitive payloads and credentials.

These are acceptance requirements for future work, not executed tests. Final numeric thresholds, provider guarantees and named recovery owners remain open.

## Official technical references

Checked for this planning discussion on 8 October 2026:

- [Microsoft: atomic state/event persistence and idempotent consumers](https://learn.microsoft.com/en-us/azure/architecture/patterns/cqrs).
- [Hangfire: persistent enqueue and restart recovery](https://docs.hangfire.io/en/latest/background-methods/calling-methods-in-background.html).
- [Hangfire: SQL Server storage and polling](https://docs.hangfire.io/en/latest/configuration/using-sql-server.html).
- [Hangfire: recurring scheduler behavior](https://docs.hangfire.io/en/latest/background-methods/performing-recurrent-tasks.html).
- [Hangfire: exception handling and retries](https://docs.hangfire.io/en/latest/background-processing/dealing-with-exceptions.html).

The documented mechanisms inform the approved architecture direction; Motmaan's provider accounts, packages and deployed behavior have not been verified by these references.
