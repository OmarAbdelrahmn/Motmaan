# Performance security and responsive websites

Updated: 8 October 2026. Performance/security and mobile/desktop websites are confirmed priorities. The user approved the engineering tools listed below; remaining detailed configuration is proposed/open, not tested behavior.

## Implementation approach

Use the api-pattern skill at `C:/Users/omarf/.codex/skills/api-pattern/SKILL.md` when implementation is requested. Follow controller, service/use-case, Result/Error, DTO validation, and EF Core patterns. Load the relevant module-boundary, data/performance, reliability, and verification references for each change. Historical example packages and project names in the skill are not automatic project decisions.

No scaffolding, endpoints, migrations, or deployment have been created. Azure SQL Database and Azure Managed Redis are selected; OpenTelemetry with Application Insights and HybridCache are now approved. App Service, private Blob Storage and Key Vault remain proposals. Transactional outbox with Hangfire is confirmed. The .NET/package versions, contracts, worker configuration, regional service access/tiers and final topology remain open; Qatar Central is the interim preference subject to production data review (AUD-05). See [Azure deployment preparation](22-azure-hosting-and-deployment.md) and [background workflow design](23-outbox-and-background-jobs.md).

**Confirmed engineering choices, 8 October:** modular monolith, ASP.NET Core policy/resource authorization, FluentValidation, Swagger UI with OpenAPI contracts, typed HttpClient with .NET HTTP resilience, OpenTelemetry/Application Insights, HybridCache/Redis, SQL Server integration tests with Testcontainers, Playwright and Flutter integration tests. Protected audit/edit history, incoming-webhook deduplication and SQL concurrency protection are also approved. [Detailed responsibilities](24-approved-engineering-tools-and-realtime.md) retain unresolved versions/contracts/limits and the still-proposed SignalR/FCM/APNs messaging design.

## Performance design

- Apply trusted authorization scope, filtering, ordering, and bounded pagination in SQL before loading results.
- Project only fields needed by the caller. Use AsNoTracking for read-only entity queries and avoid unnecessary navigation graphs and N+1 access.
- Add indexes for measured filter/order patterns; inspect generated SQL and representative execution plans. Index every column is not a strategy.
- Avoid a single patient-page response containing all clinical history, financial history, files, and messages. Load authorized sections through bounded queries.
- Evaluate availability over a bounded date range, with efficient schedule and overlap lookups. Revalidate capacity transactionally when reserving; cached availability cannot authorize a booking.
- Use short transactions and bounded concurrency. Never run simultaneous EF operations on the same DbContext.
- Keep external provider calls out of database transactions. Move report generation, imports, large exports, recording post-processing, and durable notifications into appropriate background workflows.
- Use the confirmed outbox/Hangfire design: atomically persist required follow-up work with business changes, dispatch bounded batches, make retries idempotent and checkpoint large operations. Separate time-sensitive work from bulk processing; monitor backlog and oldest due work. Scheduled checks must revalidate current state and deadlines; delayed execution cannot extend booking eligibility. Detailed recovery and verification requirements are in [background workflow design](23-outbox-and-background-jobs.md).
- Cache public catalog and brand content where useful, with invalidation rules. Do not share patient or staff data across users through cache keys or public caching.
- **AUD-21:** optimize/measure SQL first; use confirmed HybridCache and later Azure Managed Redis selectively for public mobile API doctor listings/available-doctor discovery, profiles and service/category catalogs when measured use cases and hosting are ready. SQL stays authoritative for bookings, payments, wallet and packages. Define multi-instance invalidation, permission revocation and cache-outage behavior; security controls must not disappear during a Redis outage. Capacity and provisioning timing remain open.
- Use managed private storage for large files and direct supported recorder delivery; do not route all video bytes through normal API requests.
- Measure response latency, query cost, memory, resource utilization, job backlog, and provider failures under representative data before adding infrastructure.

AUD-26 below supplies approved initial operational planning baselines, not demonstrated production SLAs. Refine endpoint/frontend payload, concurrency and workload budgets through representative testing. Use the expected 10,000-plus patient histories and growth assumptions for planning, not just empty-database demonstrations.

## Security design

Enforce identity, role-selected staff dashboard eligibility, endpoint-specific action permission, and resource scope on every applicable workflow. Separate create/read/update/delete and other protected endpoint actions where they exist; a UI-hidden control never substitutes for an API check. Protect exports and file access as well as screen data. Keep staff authentication distinct from patient OTP and recovery. Promptly invalidate permission changes and revoked sessions.

The confirmed one-account-per-staff-role fixture belongs only in development/test environments. Keep accounts active/verified for functional testing, let role-baseline changes update their effective permissions automatically, and use synthetic scoped records. Do not ship fixture identities or default credentials to production. Test both allowed and denied actions; a role's full baseline still does not bypass separate clinical/recording grants or branch/patient scope.

Validate requests and database constraints. Use transaction/concurrency protection for overlapping bookings, wallet spending, package consumption, and compensation updates. Authenticate provider callbacks, deduplicate retryable effects, and reconcile ambiguous outcomes.

Keep files private by default, scope upload and download grants, validate content, and scan untrusted uploads before access. Candidate attachments do not inherit medical-record visibility. Keep secrets in approved server-side configuration and exclude secrets, OTPs, and unnecessary health data from logs.

Rate-limit expensive public, login, recovery, recruitment, upload, and payment operations based on their risks and deployment topology. Per-instance limits must not be described as global limits without shared enforcement. Protect cookie-based actions against CSRF where applicable; finalize browser session design before choosing controls.

Protect audit integrity, backups, retention jobs, and recovery procedures. Use safe errors with trace references and production diagnostics that do not leak private information. A Saudi storage region is an infrastructure choice, not by itself a complete assurance of regulatory compliance.

## Initial operational targets and reporting — AUD-26

**Approved Direction:** normal initial planning baselines, subject to testing, hosting/contract validation and adjustment. These are not achieved targets or production SLAs.

| Metric | Initial planning target | Measurement qualification |
|---|---|---|
| Monthly application/API availability | 99.5% | Define eligible service monitoring and measurement boundaries |
| API read latency | P95 ≤ 800 ms | Exclude waiting on external payment, SMS or video providers; measure dependencies separately |
| Normal API write latency | P95 ≤ 1,500 ms | Same external-wait exclusion; distinguish long asynchronous work |
| Unexpected server error rate | < 1% of eligible requests | Define eligible requests and unexpected server failures consistently |
| Recovery Time Objective (RTO) | 4 hours | Validate through incident/restore exercises and operator responsibilities |
| Recovery Point Objective (RPO) | 1 hour | Requires suitable log/backup recovery; daily backup alone does not guarantee this |
| Backup frequency | At least daily | Add recovery mechanisms needed for RPO; verify database/file consistency and restore |

Operational reports display metric name, target, actual value, measurement period, compliance, historical trend and relevant failures/incidents. Include applicable API latency, availability/errors, background-job failures, upload/processing failures, backup/restore status and resource utilization. Keep infrastructure metrics separate from appointments, occupancy, revenue and satisfaction business KPIs, while allowing both in appropriate authorized management dashboards. Do not invent clinical/financial formulas. Unknown actual values must be shown as unmeasured, not compliant.

Before launch validate hosting capabilities, contractual obligations and representative workloads, assign measurement/recovery owners and retain evidence. [Azure planning](22-azure-hosting-and-deployment.md) must supply compatible recovery mechanisms.

## Responsive public and authenticated websites

The mobile/desktop requirement applies to the main branded website, Join us forms, patient booking and account pages, management dashboard, specialist dashboard, and video-session screens. Tablet support from the source remains included.

Plan layouts and interactions for narrow and wide screens, Arabic RTL and English LTR, touch and keyboard use, clear labels, readable type, and accessible focus behavior. Adapt dense tables and calendars without making permissions or important actions disappear. Keep upload, verification, booking/payment, and session flows usable on a phone.

Serve appropriately sized images, load recordings on demand, keep JavaScript and large dependencies bounded, and measure page behavior on representative mobile networks/devices. Public brand assets may use public caching; authenticated medical and financial responses need appropriate private cache policies.

Branding interpretation: display the center's name, logo, and identity consistently on public pages. Exact design, content management permissions, assets, and frontend stack remain open.

## Confirmed production-readiness checks

All proposed checks are required: security, user acceptance, payment/accounting reconciliation, successful backup restoration, representative performance verification, and monitoring. The two-month target does not prove readiness. Initial numeric baselines are defined below; workload-specific thresholds and named sign-off owners remain open. Preserve the existing delivery plan and two-month target (AUD-03).

Proposed acceptance coverage includes branch restrictions on queries, reports, exports, files, and background workflows; no clinical or financial privilege gained from internal task assignment; salary-paid availability priority and external-doctor fallback. These are future checks, not verified implementation behavior.

**Review follow-ups R12–R14:** Name owners and measurable thresholds for the required checks. Add a supported browser/device matrix, clinical draft/cache/logout behavior, API compatibility for older installed mobile clients, app distribution/signing ownership, store/privacy declarations and account deletion/request handling. Prepare trial migration and cutover/rollback evidence alongside restore tests; export discussion retains its user-deferred status. See the [readiness review](20-development-readiness-review.md) for current gaps and official mobile-policy references, and the [shared contract checklist](../handoff/shared-contract-checklist.md) for client acceptance criteria. These are proposed delivery artifacts, not completed checks or approved policy defaults.

## Verification when implementation starts

Use meaningful authorization, ownership, concurrency, retry, and business-rule tests for affected workflows. Use the real database provider for provider-specific transaction and query behavior. Check performance with representative histories and peak usage. Verify critical flows on mobile and desktop with RTL/LTR and keyboard/touch use. Repeat checks when changes justify it rather than adding boilerplate tests that mirror the implementation.

Acceptance should include denied direct API access, cross-patient identifier substitution, stale permission revocation, duplicate webhook processing, contested booking, safe recruitment uploads, repeated candidate acceptance without duplicate doctor accounts, SMS delivery retries, monthly incentive threshold crossing and refund corrections, contact recovery boundaries, and measurable booking/search/report performance. Define exact acceptance thresholds before claiming completion.

## References

- [EF Core efficient querying](https://learn.microsoft.com/en-us/ef/core/performance/efficient-querying)
- [OWASP authorization guidance](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html)
- [OWASP file upload guidance](https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html)
