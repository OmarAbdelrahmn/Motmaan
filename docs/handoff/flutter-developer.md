# Flutter developer handoff

Updated: 4 October 2026. Status: planning handoff. The project is not in implementation; this file captures current product direction and should be updated as decisions are confirmed.

**Confirmed recovery and adult-family consent:** Confirmed role baseline: reception handles scoped branch bookings/contact details, accountants handle scoped finance, doctors handle assigned patients, and managers receive only owner-assigned operational/reporting permissions. Separate clinical/recording grants remain required; the full granular action matrix is not approved by this baseline. Confirmed self-service safeguard: turning staff SMS verification off or changing its phone requires password confirmation and an SMS code to the existing verified phone. A lost phone uses the approved administrator recovery process. Detailed audit, conflict handling and administrator-change safeguards remain proposals.

Staff lost-phone recovery is approved through an authorized account administrator after identity verification; recovery of the last available administrator requires owner verification. An adult family member must explicitly consent before a parent or another authorized family member can view their clinical records. Family membership, package sharing and payment rights do not establish clinical consent; detailed consent/proof/revocation and minor rules remain open.

**Confirmed session limits:** Staff web expires after 30 minutes inactive or eight hours total; patient web after 30 minutes inactive or 24 hours total; patient app after 30 inactive days or 90 days total. Reauthentication must support active consultations and unsaved forms safely. The 15-minute mobile access-token lifetime, storage/revocation mechanism and meaningful-activity details remain engineering proposals.

**Detailed contract planning, 5 October 2026:** Workflow 21 now describes proposed identity-review/recovery states, adult consent execution and an operation-contract table. Design pending/rejected/conflict/reauthentication states without exposing candidate records. Phone delivery, verified identity linking and clinical permission are distinct outcomes. Evidence rules, final API payloads, consent/minor mechanics and remaining provider choices are still open.

## Readiness and shared contracts

**Current selected workflow:** [Authentication/authorization draft](../planning/21-authentication-and-authorization-workflows.md) defines proposed transitions, challenge/session contracts, access matrix and acceptance scenarios. Patient login uses SMS with six-digit codes, five-minute validity, a 60-second resend interval and five failed attempts per challenge. The owner delegated imported linking to the recommended hybrid: documented verified links prepared during migration, with reception reviewing ambiguous/unverified exceptions before record access. Clinical-record and recording grants are separate and assigned only by administrators explicitly authorized by the owner for access management. Reception verifies patient identity when both recovery channels are lost; an authorized account administrator approves recovery. A deactivated doctor may finish/save only the already-active consultation; new work is blocked immediately. Detailed evidence, remaining role defaults, transfer scope and exception termination still need contracts. [Provider setup](../planning/16-external-provider-guide.md) now records no accounts currently available and owner responsibility for all accounts. Technical delegation/provider selections remain open.

**Confirmed staff clarification:** Username/verified email/phone plus password and default-on, self-managed SMS additional verification concern staff web sign-in. They do not add patient passwords or make patient OTP optional. Patient SMS transport/defaults and the hybrid imported-linking approach are confirmed; detailed identity evidence remains open. Use proposed states from document 21 for design; do not implement its unapproved numeric/token defaults.


**Reviewer assessment, 4 October 2026:** Ready for UX/design and workflow contract preparation; not a complete implementation handoff. Read the [readiness review](../planning/20-development-readiness-review.md) and [shared contract checklist](shared-contract-checklist.md). Implementation still needs explicit user authorization and completion of the gates for the affected workflow. API-authoritative behavior requires an agreed field/state/error contract; this file is not that contract.

Prioritize patient identity/first access, shared booking/payment states, family eligibility, recording consent/failure, weak-network/resume behavior and assessment integration contracts. Prepare account deletion/request and release planning, center-owned store/signing setup, SDK disclosures, deep links, real-device checks and older-client compatibility (R02–R09, R12–R13). Account deletion and family exit are different operations; retained records need a separate policy. These are review follow-ups, not approved screen/API designs.

## Product and technical context

- Build the patient mobile application for iOS and Android using Flutter.
- Motmaan is the only organization in scope. The first release serves one branch; additional branches may be added later.
- The backend is planned with ASP.NET Core and EF Core. API contracts, endpoints, and mobile authentication/session implementation have not been finalized.
- Do not start scaffolding or implementation until the user explicitly moves the project into implementation.
- Performance and security are priorities. Patient authorization is enforced by the API; client-side hiding is not access control.

- Patients, doctors, schedules, and reporting are branch-restricted; display only API-authorized branch data.

## Confirmed mobile app responsibilities

### Patient identity and profile

- Sign in with phone number and a one-time code sent to that number.
- Patients may add a username or email after sign-in. Email must be verified before it can be used for recovery. A username is an identifier, not proof of ownership.
- The same patient identity and backend rules apply to the mobile app and patient website.

- Established verified-email proof is sufficient for lost-phone recovery without administration review. Use backend recovery challenges sent to the previously verified email and verify the replacement phone; never treat a newly entered email/phone as proof of the old account. Maintain the same account/patient identity and existing recovery safeguards.

### Appointments, booking, and checkout

- Patients can browse Motmaan services/doctors, book appointments, and pay in the app. The responsive patient website offers the same booking and payment capability.
- Patient doctor discovery should support filtering by expertise/concern, specialty, language, appointment mode, and availability. Use API-returned public data; see [practitioner expertise](../planning/13-practitioner-expertise.md).
- Combine selected filter categories with AND and values within a category with OR; availability is checked by the API.
- Patients can book and pay for a recommended Motmaan program from the app.
- Required online payment options are mada, Apple Pay, credit/debit cards, Tabby, and Tamara, available together. Tap Payments is the preferred gateway candidate to evaluate; PayTabs is a comparison. This is not a final contract selection, and merchant/provider approval remains pending.
- An online appointment is not confirmed merely because checkout returned to the app. Display confirmation only after the API reports successful payment confirmed by the provider.
- Do not put provider secrets in the Flutter app or collect/store raw card data. The backend will create and reconcile payment attempts; the exact hosted checkout/native SDK flow depends on provider selection and API contracts.
- Cash is accepted only at an attended in-person session; do not present cash as an online checkout option. Bank transfer for bookings is not allowed.
- Block patient cancellation and appointment modification with less than 24 hours remaining, using API-authoritative eligibility. At/above the cutoff preserve refund-to-original-method or wallet choice and reserved package-session restoration. This replaces the earlier unspecified admin cutoff; staff exceptions and other change details remain open.
- If Motmaan/doctor cancels, credit the wallet. Provide an in-wallet bank-payout request for service-refund-origin funds only; system administrator or accountant approves. Coupons are not withdrawable. Bank details/verification, execution, rejection and timings remain open; submitted or approved does not mean paid.

- Prioritize available salary-paid practitioners in discovery/booking; preserve external fallback when prioritized practitioners are full over the selected start/end date range and matching filters. Equal dates mean one day. Backend availability/fallback eligibility is authoritative; mixed-date presentation remains open.
- Checkout holds the appointment for seven minutes and shows a payment countdown distinct from the existing appointment-start countdown. At unpaid expiry show «انتهى وقت الدفع، يرجى المحاولة مرة أخرى» and refresh availability; server releases the hold. Reopening/resuming the app must recover the original server deadline, not restart seven minutes. Provider confirmation and late-payment handling remain backend responsibilities; an elapsed local timer must not overwrite a verified paid booking.
- Wallet should show API-provided withdrawable service-refund balance separately from nonwithdrawable coupon credit, with request history/status. Family membership does not grant access to someone else's withdrawable balance.

### Packages, case information, and treatment tasks

- Administrators create and control package offers, including their sale period/end or expiry and package settings. The app displays the package terms and balances supplied by the API; exact configuration fields are open.
- Patients can view all information about their own case in the patient experience. The boundary for internal administrative metadata has not been defined.
- Patient-imported Arabic data may have an English machine translation from the backend. Preserve/display the Arabic original and mark translated text as machine-generated; do not call translation APIs directly from Flutter. Clinical translation behavior is in [integration planning](../planning/03-integrations-and-storage.md).
- Within 48 hours from session end, patients may optionally review the session and doctor, with a rating out of 10. Management sees all reviews; the patient author sees their own, and the session doctor sees that review. Other users do not see it; see [patient feedback](../planning/14-patient-session-feedback.md).
- A patient's tasks include repeatable self-care actions (for example, three actions daily/weekly) and recommendations to join a Motmaan program related to their needs.
- Doctors assign patient tasks. Doctors control patient-task reminder scheduling; the backend sends push notifications according to the doctor-defined schedule and task recurrence, and the app displays them. Patients can mark task occurrences complete or missed and provide a reason; doctors can review progress. Doctor controls include time of day, selected weekdays, start/end dates, and reminders per day. Changes to recurring patient tasks apply only to future occurrences and preserve earlier completion history. Weekly summaries go to both patient and assigned doctor; numeric task limits and summary content, timing and channels remain open.
- Father or mother adds family members. Each member views their own reports/sessions/diagnoses and invoices if they paid. Provide «الخروج من العائلة» for API-authorized eligible members; notify family head and allow independent booking/ordinary patient powers after exit. Cross-member permissions, relationship verification, minors/guardian interaction and post-exit package/booking effects remain open; do not infer them from family package sharing.

- Doctors can edit finalized clinical reports directly. Patient report views should refresh the current authorized report; do not require a separately issued revised report. Exact edit-history/patient-update presentation is unresolved. This does not select prescription or invoice correction rules.
- Weekly treatment-task progress summaries are for both patient and assigned doctor. Patient app renders the patient's own summary; contents, timing, and delivery channels remain open. Public biography/expertise changes require management approval before publication; render approved profile data.
- Session reviews support written comments (recommended as optional) and mobile editing of the patient's existing review within the original 48-hour window from session end. Fetch API-authoritative ownership, eligibility, deadline, and saved state; edits do not extend the window. Rating stays out of 10; visibility stays management/author/session doctor.
- Doctors control patient-task times, weekdays, start/end dates, and reminder count per day; the backend sends recurrence-based push and the app displays it. Administration still controls appointment reminder lead time. Internal reception/accountant tasks and their live website notifications belong to the staff web workspace; no patient-mobile staff-task screens have been requested.
- Doctors may issue finalized clinical reports and prescriptions directly, without a separate management approval step, within granted permissions, assigned-patient scope, and applicable qualifications.
- Changes to recurring patient tasks apply only to future occurrences and preserve earlier completion history. Display API-provided task versions and preserve historical progress.
- Practitioner changes support both «جلسة فقط» (existing practitioner retains follow-up) and «نقل مسؤولية المتابعة» (new practitioner takes ongoing responsibility). Display the API-provided assignment mode/current follow-up practitioner and eligibility. Who may choose/approve and where the choice is presented remain open; do not assume a patient-selectable control or default from this answer. Buying another practitioner's session alone does not transfer follow-up. Existing price-difference and package rules remain in force.
- Current packages repeat sessions for a specified practitioner chosen by the patient; show that practitioner's packages. Family members can consume sessions and switch practitioner with a price difference if applicable. Beneficiary, purchaser and practitioner remain distinct; show only API-authorized members/slots and server-calculated difference. A cheaper-practitioner switch does not refund the difference; show the API-calculated amount. Entitlement after family exit remains open. Future treatment pathways across practitioners are deferred.
- Before refund submission, display an API-calculated explanation of base-price repricing: the confirmed example is SAR 1,000 paid, two used × SAR 300, refund SAR 400. Do not compute refunds/commissions locally from remaining discounted sessions. Consumed no-show sessions also use standalone/base price outside the package for refund repricing; no doctor incentive is earned. Tax, original-versus-performing practitioner base-price attribution after transfer, paid differences and commission reversals remain open.
- Existing assessment platform will be integrated rather than rebuilt. Name/API/SSO/results/payment and launch status are not technically verified. See [questions for its programmer](../planning/18-assessment-platform-integration-questions.md). UI method (SDK, WebView, browser/deep link) is still open; secrets and result validation belong on the backend.

### Appointment status, countdown, reminders, and video

- Reception records in-person Arrived status. Actual consultation end is patient departure; notes are written afterward and a prescription may precede departure. The doctor's later Finished confirmation triggers an emailed session/doctor rating request. If unanswered, show a rating popup on the next app opening from API-authoritative submission/eligibility/deadline state; email/web submissions suppress the unanswered popup. Rating remains optional, out of 10, with the existing 48-hour-from-session-end/mobile-edit rules. The 48-hour deadline runs from actual consultation end even if confirmation is delayed; reception records actual in-person end if the doctor forgets. Detailed recording/correction permissions, popup repetition, multiple pending reviews and missing-email behavior remain open. Do not provide patient-operated attendance/completion actions; online join evidence remains separate.
- Doctor overrun warnings, reception escalation, and session extension are staff workflows. Overrun duration runs from actual consultation start; reception is alerted after a system-configured delay if still unfinished. Delay value/default/owner and actual-start capture remain open. The doctor may extend an active session by a period configurable by doctor or management. No new patient duration countdown/end action or automatic booking shift is approved; display only API-provided state. Keep booked duration distinct from active extension and preserve attendance/ongoing-consultation no-show protection. No-show still uses scheduled start plus its separate grace period. Extension into a later booking is allowed with a doctor warning that another patient is waiting; existing bookings do not shift automatically. Extension limits and exact waiting/conflict detection remain open.
- Booking shows scheduled free doctor slots and next-available date/time. If the search returns no available appointments at all, show separate next-available suggestions, potentially outside the selected range, while retaining matching non-date filters, branch scope, and salary-paid availability priority/external fallback. Do not silently widen the range. Suggestion count/horizon remain open. Doctor/management settings include daily session count, configurable duration, weekday working hours, breaks, and days off; five sessions/day and X minutes are examples only.
- Session count/duration setting changes affect only unbooked slots. Existing bookings keep their booked date/time and duration; display the appointment's API-provided values rather than applying the doctor's latest duration setting. Exact duration configuration scope (such as per service) remains open.
- Doctor-ready notifications to patient and reception are triggered by the doctor's Ready for patient button. Channels remain open; advance reminders stay separate. Waiting-room queue position and estimated wait were not selected.

- Show an appointment countdown and advance reminders using lead times set by administration. No numeric default is approved.
- The mobile app may show the time until an upcoming in-person appointment; server/API time and appointment state are authoritative. A countdown never proves attendance or marks an appointment complete/no-show.
- Patient no-shows retain the paid fee or consume one package session for both in-person and online appointments. The API evaluates no-show at appointment start plus its configurable grace period, unless attendance or an active consultation is recorded.
- Agora is the provisional online-session provider. The API will authorize appointment participants and provide session access. Storage credentials and provider secrets never belong in the app.
- Every online consultation must be recorded for safety and performance review. Show recording/consent/readiness state from the API and do not offer an unrecorded-consultation toggle. Consent/refusal and recorder-failure behavior remain open; a successful call join is not recording readiness. Mandatory recording does not grant recording-playback access.
- If connection failure prevents completion, the patient can open a support ticket and management may grant a free replacement after review. Display API-authorized review/grant status; do not create a free session automatically on disconnect or ticket submission. Replacement eligibility/expiry and partial-session accounting remain open.
- Recording playback is restricted by management-selected permissions. Patient access to a recording has not been approved; do not assume recordings are patient-visible.
- Reception selects rooms per appointment with available-room suggestions in the staff website. The patient app books against API-authorized capacity; it does not assign rooms or treat a room suggestion as a reservation. Selection timing during self-service confirmation remains open.
- Existing data is seeded/imported before operation. First-login access still requires the backend's verified account-to-patient mapping; preseeded data does not authorize access based solely on a shared/matching phone number. Prepare documented verified links during migration; reception reviews ambiguous/unverified links before access. Evidence requirements and duplicate/shared-contact reconciliation remain open.

### Support tickets

- Patients submit support tickets from the signed-in app; administrators resolve them. Statuses are Open, In progress, Waiting for patient, Resolved, and Closed. Send push notifications and show an in-ticket new-message indicator. Email the patient a satisfaction survey rated out of 10 with optional comments and one submission per ticket when the ticket is Closed; link it to the resolving administrator. Management sees all responses; the patient sees their own.
- Keep ticket history and status visible to the requester once the backend contract is ready. Do not put sensitive case content in push-notification text.
- Ticket reopening has no time limit; resulting status mapping, attachments, notification channels and service targets remain open in [support ticket planning](../planning/11-support-tickets.md).

- Patients may reopen their resolved/closed support tickets without a time limit. Render API-authoritative ownership and reopening eligibility; resulting status mapping remains open. Keep one satisfaction response per ticket, including after reopening.
- Ticket satisfaction comments are optional; one submission per ticket. Show submitted state from the API across devices; expiry remains open.

## App-wide experience requirements

- Arabic and English; correct RTL/LTR layouts and content direction.
- Use `Asia/Riyadh` for all patient-facing schedule/time display and task recurrence. The API supplies authoritative timestamps; persisted event instants are UTC.
- Responsive behavior across phone and tablet form factors, accessible labels/focus, clear loading/empty/error states, and usable touch targets.
- Handle weak/intermittent mobile networks, app resume, duplicate taps, and provider redirects without duplicating bookings or payments.
- Refresh appointment/payment state from the API after returning from checkout, reopening the app, or restoring connectivity.
- Register/unregister push devices through the API according to the eventual notification design. FCM/APNs are proposed, not selected.

## Provider documentation findings for later development

Read the [4 October provider review](../planning/17-provider-documentation-development-notes.md) alongside the provider guide. These are research findings and proposed verification tasks; no SDK or provider account is selected by this update.

- With the chosen checkout flow, register required app identifiers and use only approved public configuration. Keep payment-pending and refund-pending views distinct; recover API state on return/resume before allowing another attempt. BNPL approval and capture mapping belongs to the agreed backend/gateway contract.
- If FCM is selected, complete APNs capabilities/key setup, handle token availability and refresh, and update API device binding on login/logout/account changes. Verify permission denial and foreground/background/terminated/force-stop behavior on real devices. Push is supplementary to persisted appointment/task/ticket state.
- For calls, use appointment-authorized tokens and handle expiry, reconnection, and recorder readiness through the eventual API contract. A successful join or checkout SDK callback does not establish recording readiness or paid booking state.
- Keep clinical text out of lock-screen previews and provider telemetry; fetch authorized details after a notification tap. Translation display and clinical-review procedure remain open/deferred as recorded in planning.
- Wati is now a named WhatsApp/SMS evaluation candidate; see [Wati delivery notes](../planning/17-provider-documentation-development-notes.md#whatsapp-and-sms-handling-wati). OTP transport/fallback is backend-managed. Display API challenge expiry and resend state; never infer verification from delivery or restart expiry after a channel change. A WhatsApp-first login flow is not selected. No Wati/Twilio secret belongs in Flutter.

- See [external provider guide](../planning/16-external-provider-guide.md) for client configuration responsibilities.

## Open or deferred items affecting Flutter

- Doctor order is API-authoritative: prioritize available salary-paid practitioners over percentage-paid practitioners, retaining existing filters/branch/date/external fallback rules. Tie-breaks and mixed-date presentation remain open; do not expose compensation rates.
- Gateway selection and Motmaan merchant approvals for mada, Apple Pay, cards, Tabby, and Tamara.
- Exact checkout UI: hosted page, provider SDK, or native wallet buttons per platform.
- Staff change exceptions, practitioner-change selection/approval and detailed access, and branch assignment remain open; patient changes within 24 hours are blocked. Session-only and ongoing-follow-up transfer modes are confirmed.
- Remaining cross-member family consent/access, minor/self-exit eligibility and post-exit shared entitlement remain open.
- Bank payout request fields, verification, execution/status/rejection and timing remain open; in-wallet request and approval actors are confirmed.
- Patient-visible internal-only case metadata and recording access.
- Expertise filter taxonomy and public profile fields; patient-facing filters should use approved API catalog entries.
- Support-ticket attachments, reopening status mapping, survey format and service targets. Patient reopening without a time limit is confirmed.
- Numeric patient-task schedule limits and weekly-summary behavior; doctor timing/weekday/date/reminder-count controls are confirmed.
- Detailed reconciliation of source-only feature details and role/permission matrix. All project requirements/features are in stage one except explicit deferred items.
- Notification channels and lead-time values; staff authentication does not apply to the patient app.

- Multi-assignee staff-task completion and Emdaad export discussion remain deferred; full migration at launch remains in scope. Current packages repeat practitioner sessions; future treatment pathways are deferred. Assessment-platform integration questions are now prepared, with technical answers pending.
- No insurance in the current release; system readiness for future NPHIES/Waseel is requested. Do not add current insurance checkout/claims screens from the broader source scope.

## Keep this handoff current

When the user confirms a rule that changes the Flutter app's screens, behavior, API needs, or permissions, update this file and the central decision register. Keep unresolved items marked open/deferred. Do not invent final API endpoints or bypass API authorization.

## Related notes

- [Project overview](../../README.md)
- [System scope](../planning/01-system-scope.md)
- [Booking and finance](../planning/02-booking-and-finance.md)
- [Integrations and storage](../planning/03-integrations-and-storage.md)
- [Identity and access](../planning/05-identity-and-access.md)
- [Decisions and open questions](../planning/06-decisions-and-open-questions.md)
- [Customer mobile appointments](../planning/10-customer-mobile-appointments.md)
- [Support tickets](../planning/11-support-tickets.md)
