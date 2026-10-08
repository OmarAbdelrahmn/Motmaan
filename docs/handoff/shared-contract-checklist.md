# Shared web, Flutter and backend contract checklist

Updated: 8 October 2026. **Proposed handoff criteria, not an approved API or implementation authorization.** Read the [readiness review](../planning/20-development-readiness-review.md) and [decision register](../planning/06-decisions-and-open-questions.md) first.

## Current detailed workflow

[Authentication and authorization](../planning/21-authentication-and-authorization-workflows.md) now supplies a draft state/contract outline and proposed matrix. Patient login uses SMS with six-digit codes, five-minute validity, a 60-second resend interval and five failed attempts per challenge. The owner delegated imported linking to the recommended hybrid: documented verified links prepared during migration, with reception reviewing ambiguous/unverified exceptions before record access. Staff roles provide baseline permissions with per-person management customization; clinical-record and recording grants remain separate and assignable only by administrators explicitly authorized by the owner. Reception verifies patient identity when both recovery channels are lost; an authorized account administrator approves recovery. A deactivated doctor may finish/save only the already-active consultation; new work is blocked immediately. Session limits are confirmed; detailed proof, unresolved multi-role conflict precedence and engineering mechanisms still need contracts; within-role additions/removals are confirmed (AUD-09). [Provider setup](../planning/16-external-provider-guide.md) records owner responsibility and the reported ready MyFatoorah account. This is progress on R02–R04/R09, not completion of their gates.

Detailed identity-review/recovery states, adult-consent execution and an operation-contract table are now supplied as proposals in workflow 21. Provider guide 16 supplies proposed acceptance/outage evidence by connection. These improve reviewability; final payloads, evidence rules and provider tests are not complete.

## How to use this checklist

Complete this for each workflow before its implementation starts. Backend, web and Flutter developers agree one behavior contract; operational/clinical/financial owners resolve business choices. Mock data must match the contract and use synthetic identities. A mock is not evidence of working authorization or integration.

An **API contract** is the developer-written agreement for what the frontend sends to the backend, what the backend returns, and what happens on denial, expiry or conflict. For example, a staff screen needs a defined way to receive that user's effective permissions and a defined denial response if a permission is removed before an action is submitted. The owner settles business rules and reviews outcomes; endpoint names, JSON fields and status codes are developer design work, not an additional owner decision.

All entries below are outstanding planning artifacts unless already supplied by a linked topic. Existing narratives explain intent but do not complete field-level contracts. Do not invent final endpoints or silently accept proposed defaults.

**Confirmed documentation/testing approach, 8 October:** Swagger UI with OpenAPI contracts, SQL Server integration tests using Testcontainers, Playwright web tests and Flutter integration tests. [Engineering tools and messaging notes](../planning/24-approved-engineering-tools-and-realtime.md) distinguish approved backend tools from the still-proposed SignalR/FCM/APNs choice. Approval of tooling does not finalize fields, statuses or event contracts. Detailed SignalR event contract is deferred (AUD-20); prior proposals are not final taxonomy/ordering/delivery/scaling. Preserve existing live/unread requirements and proposed transport status.

## Confirmed changes for the shared implementation contract

| Area | Confirmed behavior / approved direction | Owning detail and design boundary |
|---|---|---|
| Effective permissions | Role defaults with explicit individual allowed/removed overrides during creation and later edits; a 90-permission role minus 5 gives that user 85 while another keeps 90. Show default/added/removed/effective; backend enforces actual permission and scope, audits changes and safely revokes | [05](../planning/05-identity-and-access.md#individual-permission-customization--aud-09); only global multi-role conflict policy/delegation/catalog details remain open |
| Privileged access | Mandatory stronger verification/MFA and sensitive-action step-up; ordinary staff toggle cannot bypass it; patient OTP unchanged | [21 lifecycle](../planning/21-authentication-and-authorization-workflows.md#privileged-verification-lifecycle--aud-08); enrollment, recovery/lost device and audit; mechanism design pending |
| Language display | Appropriate selected-language representation of suitable dynamic data beyond clinical text; preserve original, transliterate names, permit approved corrected derivations, avoid repeated requests and blind identifier translation | [03](../planning/03-integrations-and-storage.md#multilingual-display-data--aud-16); reusable consistent Web/Flutter contract, sensitive provider approval and clinical controls remain |
| Extensions and closure | Block extension if later booking exists for doctor or room; no booking shifts. Reception may perform authorized operational closure when doctor forgets, with finalizer audit and actual-end/closure timestamps separate; no clinical signing | [10](../planning/10-customer-mobile-appointments.md), [14](../planning/14-patient-session-feedback.md); actual overruns still recorded; feedback deadlines and other extension rules unchanged |
| Clinical versions | Preserve original and every meaningful edited version, modifying practitioner/time, PDF/export version and signature lineage; authorized history/audit, approved direct-edit experience | [05](../planning/05-identity-and-access.md#clinical-document-version-history--aud-15); no schema or history UI assumed |
| Files and media | Supported uploads resume from server-confirmed parts after 48% interruption and restart; expose progress/integrity/failure/processing. Recording readiness gates clinical start; adaptive available-quality streaming with private restricted playback | [04 authoritative media](../planning/04-online-sessions.md), [03 ordinary files](../planning/03-integrations-and-storage.md#secure-file-lifecycle--aud-23); do not infer patient playback access or provider-controlled recovery; PDFs/images need no video transcoding |
| Public discovery/cache | Efficient measured SQL first, later beneficial Redis caching for public mobile doctor/availability/profile/service/category endpoints; client uses HTTPS API only | [09](../planning/09-performance-security-and-responsive-websites.md), [22](../planning/22-azure-hosting-and-deployment.md); SQL revalidates booking capacity, finances/payment and sensitive authorization; no early Redis provision |
| Reliable finance/jobs | Approved ledger/correction/reconciliation direction and atomic outbox/Hangfire dispatch, idempotency, crash recovery and urgent/bulk separation; truthful pending/failure/recovery state | [02](../planning/02-booking-and-finance.md), [23](../planning/23-outbox-and-background-jobs.md); approved direction, no new financial policy or final payloads |
| Hosting and reports | Qatar Central interim subject to production data suitability; Saudi migration after checks/approval. Operational reports use target/actual/period/compliance/trend/incidents separately from business KPIs | [22](../planning/22-azure-hosting-and-deployment.md), [09 baselines](../planning/09-performance-security-and-responsive-websites.md#initial-operational-targets-and-reporting--aud-26); unmeasured initial targets, no deployed resources |

Future-only recurring patient-task edits remain unchanged (AUD-18). Existing Figma, responsive/RTL and platform functionality are preserved; no new broad parity redesign (AUD-24). Salary-paid priority is unchanged; a future salaried-group recommendation idea is only a note (AUD-27). All deferred policy/contracts remain deferred; compensation boundaries are addressed during affected development with finance/owner decisions, not invented defaults.

## Minimum workflow handoff

| Item | Required contents |
|---|---|
| Requirement and status | Stable feature ID, topic/source links, confirmed versus proposed rules, scope and explicit deferrals |
| Actors and access | Authenticated account, beneficiary patient, payer, branch, practitioner assignment, role-selected staff dashboard, role baseline plus individual customization, endpoint-specific effective permission, visible fields, revocation behavior and denied examples |
| Permission coverage | Map every protected endpoint to its specific action permission; separate create/read/update/delete and non-CRUD actions; state required resource scope and negative test cases. Confirm exact catalog/defaults, unresolved multi-role precedence/delegation and sensitive-grant authority before the affected endpoint is implemented |
| Development role fixtures | One confirmed/active nonproduction account per staff role, full role baseline, synthetic scoped records and safe test authentication. Verify newly assigned service permissions appear automatically through role membership; ensure fixtures cannot be provisioned in production |
| Screens | Entry points, navigation, fields/validation, actions, success, empty, loading, pending, error, denied, expired, interrupted and retry states |
| State transitions | Current state → actor/action → eligibility → next state; distinguish booking/payment/attendance/clinical completion/recording/accounting |
| API operations | Request/response fields, types/nullability, IDs, supported filters, bounded pagination, stable sort and safe error codes |
| Time | UTC instants, Asia/Riyadh presentation, server time/deadline, exact cutoff boundary, policy version and client refresh behavior |
| Money and entitlements | Currency/precision, price snapshot, beneficiary/payer/owner, quoted versus final totals, tax/discount allocation and refund/consumption states |
| Retry and conflict | Duplicate action key scope, timeout with unknown outcome, conflict response, stale edit detection and recovery; whether a new attempt is permitted |
| Background operations | Confirmed outbox/Hangfire direction; define application operation identity, authorized status/progress/result, acceptance versus completion, refresh/resume, safe errors, retry/replay/cancel eligibility and artifact expiry/access. Keep accounting sync separate from payment/booking state; agree deduplication and provider unknown-outcome handling. See [detailed design](../planning/23-outbox-and-background-jobs.md) |
| Files and notifications | Authorized upload/download, types/size limits, scanning status, notification recipient/channel, deep-link target and inaccessible-target behavior |
| Integration evidence | Provider/account flow, safe public client configuration, callbacks verified by backend, errors, retry/reconciliation and test evidence |
| Compatibility | Contract version/change policy, older installed mobile app behavior, web deployment coordination and safe refresh/logout |
| Acceptance | Success and denial examples, concurrency/failure cases, representative data, named reviewer and completion evidence |

API-returned allowed actions are a useful UI contract, but the server must recheck eligibility and access when an action executes. No client flag is authorization.

## First workflow: identity through booked appointment

Recommended first development slice, subject to the owner selecting it and authorizing implementation:

| Contract | Web and Flutter need to agree | Unresolved dependency |
|---|---|---|
| Patient challenge and session | Challenge identifier, expiry/resend/attempt states, session/recovery outcomes, account/patient links and logout | Detailed first-access evidence, duplicate contacts and session mechanisms; patient SMS/defaults and hybrid linking approach confirmed |
| Patient context | Current beneficiary, authorized family actions, branch context and payer identity | Family consent/minor rules; use an agreed self-patient flow first without claiming family completion |
| Discovery | Public fields, approved expertise IDs, date range, available salary-paid priority, fallback and separate next-available suggestions | Public field schema, mixed-date ranking and bounded search horizon |
| Quote and hold | Service/mode/practitioner/beneficiary, amount/currency, eligibility, server deadline and expired state | Deferred discussion: room capacity timing, price/tax contract, which booking paths require a hold; resolve before booking implementation |
| Payment | Attempt identity, MyFatoorah checkout entry/return, verified pending/success/failure states and reconciliation across any direct BNPL route | Owner reports account ready; technical enabled-method evidence, Tabby/Tamara connection path, method-specific capture/refund lifecycle and deferred late-payment rule remain |
| Appointment | Booked time/duration, mode, permitted actions, cancellation eligibility and detail refresh | Canonical statuses, staff exceptions, capacity and cash workflow |
| Staff operational view | Authorized appointment list/detail, room assignment, payment state and reception arrival | Remaining permission defaults and room constraints; base staff sign-in confirmed |

Mandatory examples: slot lost; seven-minute unpaid expiry; payment pending after app return; payment succeeds after expiry; duplicate tap; app killed/reopened; user switches account; inaccessible patient; unauthorized branch; exactly 24 hours versus just under 24 hours; room conflict. Expected outcomes must come from agreed rules, not screen-level guesses.

## Other workflow contracts to prepare

- **Clinical:** encounter fields, draft/save/issue/edit behavior, actual start/end versus Finished, report/prescription formats, qualifications and assignment scope. Direct editing and mandatory clinical report versions/author/time/export/signature lineage are confirmed (AUD-15); exact storage/presentation/access mechanics remain design work.
- **Packages and wallet:** separate discounted allocation from refund repricing; show server-calculated terms, balances, payout eligibility and failure states. Never calculate withdrawal rights from a single displayed balance.
- **Video:** authorized join, consent, recording readiness/failure indication, reconnect/end, independent playback authorization and management replacement review.
- **Patient tasks:** definition versus occurrence, timezone/cutoffs, future-only changes, missed reason, summary period/recipients and duplicate completion handling.
- **Tickets and reviews:** response visibility, reopening, one ticket survey, session review deadline/edit eligibility, popup suppression across devices and expired review presentation.
- **Recruitment:** exact field/conditional validation, safe uploads, management states, duplicate acceptance, provisioning/invitation status and approved public profile mapping.
- **Staff tasks:** per-action permissions and notifications; multi-assignee completion remains deferred and must not receive an assumed rule.
- **Assessments — deferred contract (AUD-17):** platform contract, SSO, account/patient mapping, access purchase, result ownership and correction. Document 18 is a question list, not an integration specification.
- **Management reporting:** metric definition, period/timezone, permitted drill-down, exclusions, reconciliation and export scope.
- **Account lifecycle:** creation, recovery, contact changes, deletion request/status, retained-data explanation, active bookings/wallet handling and revocation. Family exit is a separate action.

## Shared interface baseline

Agree Arabic/English text ownership, RTL/LTR component behavior, Arabic/Latin input, phone formatting, date/currency display, calendar behavior, responsive tables, accessible labels/focus, and phone/tablet/desktop checks. Define patient web/mobile parity explicitly: mobile review editing and rating popup are confirmed; web editing/popup parity must not be inferred.

Define what remains visible offline, whether edits can be saved as drafts, and how a failed or ambiguous write is recovered. Do not add offline booking/payment or persistent clinical caching by default. Notification links and provider returns must fetch current authorized API state; old screen state is not proof of payment or ongoing access.

## Completion record template

For each workflow record: feature ID; business reviewer; API/web/Flutter owners; contract revision; screen/design links; outstanding blockers; acceptance examples; provider evidence where applicable; review date. Mark **ready for implementation** only for the covered workflow, and separately record implementation/test/release status later. No part of this checklist currently certifies the complete application ready.
