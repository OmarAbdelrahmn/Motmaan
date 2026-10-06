# Shared web, Flutter and backend contract checklist

Updated: 4 October 2026. **Proposed handoff criteria, not an approved API or implementation authorization.** Read the [readiness review](../planning/20-development-readiness-review.md) and [decision register](../planning/06-decisions-and-open-questions.md) first.

## Current detailed workflow

[Authentication and authorization](../planning/21-authentication-and-authorization-workflows.md) now supplies a draft state/contract outline and proposed matrix. Patient login uses SMS with six-digit codes, five-minute validity, a 60-second resend interval and five failed attempts per challenge. The owner delegated imported linking to the recommended hybrid: documented verified links prepared during migration, with reception reviewing ambiguous/unverified exceptions before record access. Clinical-record and recording grants are separate and assigned only by administrators explicitly authorized by the owner for access management. Reception verifies patient identity when both recovery channels are lost; an authorized account administrator approves recovery. A deactivated doctor may finish/save only the already-active consultation; new work is blocked immediately. Session limits are confirmed; detailed proof, remaining role grants and engineering mechanisms still need contracts. [Provider setup](../planning/16-external-provider-guide.md) records no accounts yet and owner responsibility. This is progress on R02–R04/R09, not completion of their gates.

Detailed identity-review/recovery states, adult-consent execution and an operation-contract table are now supplied as proposals in workflow 21. Provider guide 16 supplies proposed acceptance/outage evidence by connection. These improve reviewability; final payloads, evidence rules and provider tests are not complete.

## How to use this checklist

Complete this for each workflow before its implementation starts. Backend, web and Flutter developers agree one behavior contract; operational/clinical/financial owners resolve business choices. Mock data must match the contract and use synthetic identities. A mock is not evidence of working authorization or integration.

All entries below are outstanding planning artifacts unless already supplied by a linked topic. Existing narratives explain intent but do not complete field-level contracts. Do not invent final endpoints or silently accept proposed defaults.

## Minimum workflow handoff

| Item | Required contents |
|---|---|
| Requirement and status | Stable feature ID, topic/source links, confirmed versus proposed rules, scope and explicit deferrals |
| Actors and access | Authenticated account, beneficiary patient, payer, branch, practitioner assignment, action permission, visible fields, revocation behavior and denied examples |
| Screens | Entry points, navigation, fields/validation, actions, success, empty, loading, pending, error, denied, expired, interrupted and retry states |
| State transitions | Current state → actor/action → eligibility → next state; distinguish booking/payment/attendance/clinical completion/recording/accounting |
| API operations | Request/response fields, types/nullability, IDs, supported filters, bounded pagination, stable sort and safe error codes |
| Time | UTC instants, Asia/Riyadh presentation, server time/deadline, exact cutoff boundary, policy version and client refresh behavior |
| Money and entitlements | Currency/precision, price snapshot, beneficiary/payer/owner, quoted versus final totals, tax/discount allocation and refund/consumption states |
| Retry and conflict | Duplicate action key scope, timeout with unknown outcome, conflict response, stale edit detection and recovery; whether a new attempt is permitted |
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
| Quote and hold | Service/mode/practitioner/beneficiary, amount/currency, eligibility, server deadline and expired state | Room capacity timing, price/tax contract, which booking paths require a hold |
| Payment | Attempt identity, approved checkout entry/return, verified pending/success/failure states and reconciliation | Gateway approval, method-specific lifecycle, late-payment resolution |
| Appointment | Booked time/duration, mode, permitted actions, cancellation eligibility and detail refresh | Canonical statuses, staff exceptions, capacity and cash workflow |
| Staff operational view | Authorized appointment list/detail, room assignment, payment state and reception arrival | Remaining permission defaults and room constraints; base staff sign-in confirmed |

Mandatory examples: slot lost; seven-minute unpaid expiry; payment pending after app return; payment succeeds after expiry; duplicate tap; app killed/reopened; user switches account; inaccessible patient; unauthorized branch; exactly 24 hours versus just under 24 hours; room conflict. Expected outcomes must come from agreed rules, not screen-level guesses.

## Other workflow contracts to prepare

- **Clinical:** encounter fields, draft/save/issue/edit behavior, actual start/end versus Finished, report/prescription formats, qualifications and assignment scope. Protected history is proposed; direct report editing remains confirmed.
- **Packages and wallet:** separate discounted allocation from refund repricing; show server-calculated terms, balances, payout eligibility and failure states. Never calculate withdrawal rights from a single displayed balance.
- **Video:** authorized join, consent, recording readiness/failure indication, reconnect/end, independent playback authorization and management replacement review.
- **Patient tasks:** definition versus occurrence, timezone/cutoffs, future-only changes, missed reason, summary period/recipients and duplicate completion handling.
- **Tickets and reviews:** response visibility, reopening, one ticket survey, session review deadline/edit eligibility, popup suppression across devices and expired review presentation.
- **Recruitment:** exact field/conditional validation, safe uploads, management states, duplicate acceptance, provisioning/invitation status and approved public profile mapping.
- **Staff tasks:** per-action permissions and notifications; multi-assignee completion remains deferred and must not receive an assumed rule.
- **Assessments:** platform contract, SSO, account/patient mapping, access purchase, result ownership and correction. Document 18 is a question list, not an integration specification.
- **Management reporting:** metric definition, period/timezone, permitted drill-down, exclusions, reconciliation and export scope.
- **Account lifecycle:** creation, recovery, contact changes, deletion request/status, retained-data explanation, active bookings/wallet handling and revocation. Family exit is a separate action.

## Shared interface baseline

Agree Arabic/English text ownership, RTL/LTR component behavior, Arabic/Latin input, phone formatting, date/currency display, calendar behavior, responsive tables, accessible labels/focus, and phone/tablet/desktop checks. Define patient web/mobile parity explicitly: mobile review editing and rating popup are confirmed; web editing/popup parity must not be inferred.

Define what remains visible offline, whether edits can be saved as drafts, and how a failed or ambiguous write is recovered. Do not add offline booking/payment or persistent clinical caching by default. Notification links and provider returns must fetch current authorized API state; old screen state is not proof of payment or ongoing access.

## Completion record template

For each workflow record: feature ID; business reviewer; API/web/Flutter owners; contract revision; screen/design links; outstanding blockers; acceptance examples; provider evidence where applicable; review date. Mark **ready for implementation** only for the covered workflow, and separately record implementation/test/release status later. No part of this checklist currently certifies the complete application ready.
