# Development readiness review

Reviewed: 4 October 2026. **Reviewer assessment and recommendations; no new user decisions or implementation authorization.**

## Planning progress after this review

The user selected [authentication/authorization and providers](21-authentication-and-authorization-workflows.md) as the next detailed workflow. Patient login uses SMS with six-digit codes, five-minute validity, a 60-second resend interval and five failed attempts per challenge. The owner delegated imported linking to the recommended hybrid: documented verified links prepared during migration, with reception reviewing ambiguous/unverified exceptions before record access. Clinical-record and recording grants are separate and assigned only by administrators explicitly authorized by the owner for access management. Reception verifies patient identity when both recovery channels are lost; an authorized account administrator approves recovery. A deactivated doctor may finish/save only the already-active consultation; new work is blocked immediately. Staff credentials, default-on self/admin SMS control, web/mobile session limits and provider account ownership/availability are also answered. Detailed flows and a proposed permission matrix now exist; unresolved identity/access questions, contracts and provider evidence keep R02–R04/R09 open. On 5 October, proposed evidence/recovery/consent procedures, operation contracts and provider outage/acceptance tables were added; these are untested review artifacts. The original review below is a dated assessment, not a statement that later planning has made no progress.

## Verdict

Motmaan has enough product direction to begin UX design, screen inventories, workflow review, and API contract planning. It is **not yet ready for an unrestricted handoff to build the complete web and mobile applications against production behavior**. Many core rules are known, but authorization, workflow transitions, data contracts, and integration evidence are unfinished.

After explicit implementation authorization, isolated presentation work can start once its design and technical baseline are agreed. Developers do not need every future detail resolved, but each implemented workflow needs its own complete contract. Unresolved clinical, access, scheduling, or financial behavior must not be invented independently by the web and Flutter teams.

The two-month production target is a user requirement, not a validated estimate. With broad first-stage scope, full Emdaad replacement, and multiple unverified integrations, it is high risk. The documents do not establish team capacity, estimates, accountable owners, or a dependency-based schedule. There is insufficient evidence to promise that date; this review neither changes it nor reduces scope.

## Review coverage and limits

Reviewed the project instructions, root overview/context, all 19 existing planning documents, and both developer handoffs. Assessed consistency, missing workflow decisions, client dependencies, and acceptance readiness. No application or provider was tested. The original DOCX was not re-audited in this pass; complete source traceability remains a gap. Existing PDF exports were not revalidated or regenerated.

The provider research in documents 16–17 remains dated research, not a new account validation. Official OpenAPI and mobile-store guidance was checked for the additional contract/release recommendations below. This is a product and engineering planning review, not a certification of security or legal compliance.

## What is already sufficiently clear

- One Motmaan organization, one initial branch, future branch support; patient mobile app and four web surfaces; Arabic/English and RTL/LTR.
- Patient phone OTP and established-email recovery, assigned-patient doctor access, and server-enforced branch/resource scope.
- Seven-minute checkout hold, trusted provider payment confirmation, less-than-24-hour patient change restriction, and no-show consumption without doctor incentive.
- Practitioner-specific repeated-session packages, family usage, the confirmed base-price refund example, and both practitioner-change modes.
- Distinct actual consultation end and later doctor confirmation; optional reviews within 48 hours of actual end.
- Mandatory recording, management-reviewed replacement sessions, doctor-controlled recurring tasks, support tickets, and doctor recruitment with automatic account provisioning.

These decisions support meaningful design work. The issue is completing the connections between them and specifying behavior under failure, concurrency, and changing access.

## Readiness by workstream

| Workstream | Current assessment | Evidence needed before affected implementation |
|---|---|---|
| Public site and Join us | Ready for design; conditional for UI build | Brand/content inventory, web stack, field validation, upload rules, application states and submission contract |
| Shared web/mobile presentation | Ready for design | Bilingual component rules, navigation, responsive layouts, loading/empty/error/denied states, target devices |
| Patient login and records | Blocked for real patient integration | Verified import-to-account mapping, session/recovery contracts, patient-visible fields and access boundaries |
| Discovery and booking | Partly specified | Capacity/room timing, canonical transitions, hold/payment conflict handling and response contracts |
| Checkout, wallet and packages | Blocked for complete production flow | Provider lifecycle, refund/payout states, mixed-credit handling and remaining financial rules |
| Family and practitioner transfer | Blocked for access-sensitive flows | Consent, relationship evidence, minor rules, who can act, temporary access and revocation; existing deferrals retained |
| Reception and management | Partly specified | Minimum action/resource permission matrix, cash flow, room assignment, metrics and exception handling |
| Doctor clinical workspace | Partly specified | Clinical forms, prescribing eligibility by practitioner type, save/edit conflicts, assignment duration and session transitions |
| Online sessions | Blocked for production integration | Consent/refusal/failure policy and verified web/mobile recording/storage flow |
| Tasks, tickets, feedback | Suitable for design; incomplete for all actions | Task occurrence rules, reopen mappings, notification matrix, review expiry presentation; shared-task completion remains deferred |
| Assessments | Integration blocked | Response to document 18, identity/SSO/payment/result contracts and test environment |
| Launch and Emdaad cutover | Not ready | Migration rehearsal, reconciled balances/files/access, operational targets, release evidence and owners |

“Blocked” is local to that workflow. It is not a reason to halt unrelated design or contract preparation.

## Priority findings

**Build gate** means resolve before implementing the affected behavior. **Launch gate** means evidence is needed before production. Ownership below is proposed, not a staff permission grant.

| ID / gate | Evidence and possible problem | Recommended next artifact / proposed owner |
|---|---|---|
| R01 — Build | [Scope](01-system-scope.md) includes all enumerated features, but source phasing still described some as later. Training, marketplace behavior, Nafath/Wasfaty, loyalty, waitlists, cashboxes and free follow-ups have less detail than booking. A marketplace must not silently become independent-clinic SaaS. | Feature inventory mapping source section → current user decision → web/mobile/staff surface → acceptance criteria → dependency. Owner + product lead; retain current scope and explicit exceptions. |
| R02 — Build | [Handoffs](../handoff/shared-contract-checklist.md) repeatedly require “API-authoritative” state but no field-level API contracts exist. Web and mobile could invent incompatible enums, validation and retry behavior. | Agreed contract for each selected workflow, including errors, authorization, examples and concurrency outcomes. Backend + web + Flutter leads. |
| R03 — Build | [Identity](05-identity-and-access.md) still defers detailed staff grants, family access and assignment duration. “Manager,” “parent,” or “assigned doctor” alone cannot decide every record/action. | Minimum matrix for the first implemented workflow, including negative cases and revocation. Owner + clinical/operations lead. Deferred policies stay deferred; dependent implementation waits. |
| R04 — Build | [Login](07-patient-login-and-recovery.md) has preseeded data but no confirmed first-access matching; staff base credentials and session mechanics are open. Shared/recycled phone numbers could attach the wrong medical file. | Identity/account/patient mapping flow, duplicate review, required registration fields, recovery/session outcomes. Owner + backend lead; do not reopen export-format discussion by assumption. |
| R05 — Build | [Booking](02-booking-and-finance.md) requires payment before online confirmation and reception-selected rooms. Cash is allowed only on attendance, but the preceding staff-booked/walk-in lifecycle is unspecified. A doctor slot may exist while all four source-described rooms are occupied. | Transition table for self-service, staff-created, package and free visits; specify room-capacity reservation versus named-room selection, cash/unpaid states, and late-payment resolution. Operations + finance + backend. |
| R06 — Build | [Finance](02-booking-and-finance.md) confirms refund intent, but negative package refund remainder, paid differences, rounding, mixed coupon/refund funds, payout failure and closed-period corrections remain open. | Finance-reviewed examples and event/state table, including who paid versus who received care and Qoyod reconciliation. Finance + backend. Package detail discussion remains outside the next owner batch. |
| R07 — Build | [Session timing](10-customer-mobile-appointments.md) separates actual end from Finished but uses “unfinished” for overrun alerts. Doctor confirmation after 48 hours could trigger an invitation after eligibility has expired. Actual-start capture and late attendance correction are unresolved. | Timestamp/actor/state map; define clinical versus documentation warnings, delayed confirmation presentation, and correction effects. Clinical + reception leads. Do not extend the confirmed review window or require notes before departure. |
| R08 — Build + launch | [Recording](04-online-sessions.md) is mandatory, while consent refusal, failed recorder start, mid-call recording failure and storage/fallback acceptance remain open. Call join success does not prove recording. | Approved consent/failure decision table and later synthetic end-to-end proof on web/iOS/Android and exact private storage. Owner + clinical + integration leads. |
| R09 — Build + launch | [Providers](16-external-provider-guide.md) have preferences and public research but not all required account/API evidence. Assessment display/payment contract is unknown; payment and SMS availability cannot be inferred from a provider name. | Dependency register with accountable contact, required artifact, current status, due date and evidence. Validate payment, SMS/email, Qoyod, assessments, recording and storage for each release slice. Owner + integration lead. |
| R10 — Build | Clinical fields are largely module descriptions in [scope](01-system-scope.md) and [access](05-identity-and-access.md). Direct report edits are confirmed, but form fields, draft/save semantics, protected history and prescription correction are incomplete. | Clinician-reviewed form dictionary and sample reports/prescriptions, required/optional fields, correction/conflict behavior and patient visibility. Clinical lead + backend/web leads. Do not infer that every specialist can prescribe. |
| R11 — Build | Patient-task rules are spread across scope/appointment notes. Summary recipients are confirmed, but occurrence boundaries, backdating/missed actions, edit cutoffs and summary calculations are incomplete. Notifications and dashboard metrics also lack unified definitions. | Dedicated task behavior section/spec, notification event matrix and metric dictionary. Define revenue versus cash collected and keep session satisfaction separate from ticket satisfaction. Product + clinical + finance leads. |
| R12 — Build + launch | [Quality](09-performance-security-and-responsive-websites.md) asks for RTL, responsiveness and weak-network behavior but has no agreed screen/state inventory, design baseline, device matrix, web stack or client compatibility plan. | Shared UX/state inventory and technical decisions; define drafts/cache/logout behavior, pagination, stale-data handling and old-mobile-client compatibility. Web + Flutter + backend leads. |
| R13 — Build + launch | No account deletion/request flow or mobile release checklist is described. Account deletion is distinct from leaving a family; app release also needs store ownership, privacy declarations, recording indication and purchase-type review. | Account lifecycle/retention decision and release checklist with owner and evidence. Owner + mobile/web/backend leads. See external evidence below; no medical-record purge rule is selected. |
| R14 — Launch | Full Emdaad replacement and all-module delivery are required, but export coverage, trial migration, rollback, measurable quality targets, team capacity and sign-off owners are absent. | Resourced dependency-based delivery plan, migration/cutover rehearsal and release acceptance record. Owner + delivery/QA/operations leads. Export discussion stays deferred; launch remains blocked without eventual evidence. |

## Concrete scenarios that must have agreed outcomes

These are acceptance questions, not invented policies:

1. Two patients request the same slot; a payment succeeds after seven minutes and the slot has been reassigned. The payment must remain visible and be resolved without double-booking or charging twice; the exact resolution policy is open.
2. Reception assigns the last suitable room while another patient is checking out. Decide when capacity is guaranteed and which client sees a conflict.
3. A cash-paying patient arrives without a prepaid online booking. Define whether this is a staff reservation or walk-in, when capacity is taken, and who may record cash/unpaid amounts.
4. A parent pays for another adult's session, then that adult leaves the family. Clinical access, existing appointment control, payer invoice visibility, package entitlement and wallet ownership need separate outcomes.
5. A doctor records actual end on Monday but confirms Finished after the 48-hour review deadline. The deadline stays anchored to actual end; email/popup/expired-screen behavior needs a decision.
6. The patient has left but the doctor is still writing notes. Decide whether the overrun warning and reception escalation remain active; do not confuse documentation with an occupied room or active consultation.
7. Recording fails while the call continues. Define what the participants see and do, preserve restricted playback, and keep management replacement review separate from automatic entitlement.
8. Two family members reserve the last package session, or a wallet payout and purchase use the same refundable credit. Define the conflict response and refresh behavior; no duplicate consumption/spending.
9. A finalized report is edited on two staff devices, or assignment is revoked while a patient page/file is open. Define conflict and revocation responses without losing audit history or serving stale unauthorized data.
10. Staff confirms payment while Qoyod is unavailable. Distinguish paid booking from accounting-sync failure, reconcile once, and avoid asking the patient to pay again.

## Recommended work order

1. **Planning now:** agree the source-to-feature inventory, choose the first complete workflow for development, prepare bilingual wireframes and fill the shared contract checklist. Gather non-sensitive provider documentation and identify owners. This does not reopen deferred questions automatically.
2. **Before a workflow is coded:** resolve its specific business/access questions, approve its states and examples, select required technical mechanisms, and obtain explicit implementation authorization. Start with patient identity + discovery + booking + verified payment + staff appointment view, once its gates pass.
3. **After authorization:** build one complete workflow across backend, patient web, Flutter and the required staff actions, then verify its failure paths. Build other independent slices concurrently where their contracts are ready. This is sequencing within the confirmed first release, not permission to drop modules.
4. **Before committing to the production date:** estimate all remaining slices with the actual team, provider lead times, testing, store submission and migration effort. If the forecast misses two months, present explicit scope/date/staffing options to the owner; do not silently remove required checks.
5. **Before launch:** complete security/access checks, finance reconciliation, provider failure recovery, real-device Arabic/English testing, migration rehearsal, backup restore, monitoring and operational handover with named sign-offs.

Can wait until the affected slice: exact card arrangement, cosmetic copy, catalog labels during wireframing, noncritical report layout and unselected numeric defaults. They still need owners before release. Cannot be guessed: identity proof, financial ownership, permissions, privacy/recording consent, capacity guarantees or irreversible state transitions.

## Shared client contract recommendation

Use [the shared contract checklist](../handoff/shared-contract-checklist.md) for both clients. API definitions should include types, allowed actions, timestamps/deadlines, field visibility, errors and examples before either team depends on them. OpenAPI provides a standard description of HTTP API capabilities; choose a version supported by the selected tooling rather than adopting a version solely because it is newest. [OpenAPI specification](https://spec.openapis.org/oas/latest.html).

Recommended acceptance evidence is one agreed contract plus successful and failed examples implemented consistently in both clients. A clickable prototype or mocked successful payment is design evidence, not evidence that authorization, payment or recording works.

## Additional mobile-release evidence

For apps supporting account creation, Apple requires an in-app way to initiate account deletion. Google Play requires an in-app deletion request path and an external web path. Add a clear request/status flow; define retained-data categories with the responsible owner instead of treating logout, family exit or account disablement as deletion. [Apple account deletion](https://developer.apple.com/support/offering-account-deletion-in-your-app/), [Google Play account deletion](https://support.google.com/googleplay/android-developer/answer/13327111?hl=en-EN).

Apple's recording guideline requires explicit consent and a clear visual and/or audible recording indication. Its person-to-person service exception permits external payment for real-time one-to-one services such as consultations. This does not establish that separately sold assessments, courses or digital content have the same treatment. Review each purchasable product and the applicable store policies before fixing its checkout design. [Apple review guidelines, 2.5.14 and 3.1.3(d)](https://developer.apple.com/app-store/review/guidelines/).

Proposed release evidence: center-owned store accounts/signing, app identifiers, privacy/data disclosures including SDK behavior, support and deletion URLs, recording/camera/microphone permission UX, reviewer access, test distribution, real devices, and a compatible-backend/version rollout plan. None has been verified by this review.

## Documentation repairs made in this review

- Replaced the long root summary with a starting guide and grouped document map; reduced the new-chat context to an entry guide.
- Separated active owner questions, resolved answers and discussion history; kept explicit deferrals and source requirements.
- Corrected stale “weekly summaries open” wording: recipients are confirmed, details remain open. Corrected stale profile-approval and doctor-priority summaries.
- Labeled source release phasing as historical rather than current exclusions; retained broad stage-one scope and flagged thinly specified capabilities.
- Moved patient-private translation/review guidance out of the public-site section and integrated handoff updates into their relevant subject sections.
- Added shared contract and readiness gates to both developer handoffs. Existing numbered topic paths and previous PDF exports are preserved.

Track owner answers in [the living tracker](12-user-notes-and-open-questions.md). Keep this review's recommendations distinct from [confirmed decisions](06-decisions-and-open-questions.md).
