# Web frontend developer handoff

Updated: 4 October 2026. Status: planning handoff. The project is not in implementation; this file captures current product direction and should be updated as decisions are confirmed.

## Product and technical context

- This handoff covers the public Motmaan website and its Join us form, the patient website, management dashboard, and doctor/specialist dashboard.
- Motmaan is the only organization in scope. The first release serves one branch, with more branches possible later.
- Backend: ASP.NET Core and EF Core are selected. Frontend framework, repository structure, and API contracts remain open. Do not assume a framework or implement against invented endpoints.
- Do not start scaffolding or implementation until the user explicitly moves the project into implementation.
- Performance and security matter. The API is the authority for identity, permissions, record scope, prices, booking state, and provider payment confirmation.

## Required web surfaces

### Public center website and Join us

- Present Motmaan's public identity, services, specialist profiles, and other approved content. Brand assets and final content ownership are not yet defined.
- The public Join us form collects candidate information. Submission does not create a doctor account or grant dashboard access.
- The first stage accepts doctor applications only; administrators control openings and applications. Candidate expertise should be collected from the database-backed expertise catalog (exact selection/review rules are open).
- After an authorized management acceptance, the backend automatically provisions/resolves the doctor account, assigns the approved doctor role, and sends/schedules an SMS invitation. Show truthful application status without exposing internal notes or credentials.
- Public and authenticated sites must support Arabic/English, RTL/LTR, and mobile, tablet, and desktop layouts.
- Patient doctor discovery should filter by expertise/concern, specialty, language, appointment mode, and availability from the API. Render approved public profile data only; taxonomy and candidate review rules remain open. See [practitioner expertise](../planning/13-practitioner-expertise.md).
- Combine selected filter categories with AND and values within one category with OR; availability is checked by the API.
- The candidate form collects normal personal information, expertise, and degrees/academic qualifications. Exact fields, required documents, verification, and public-profile mapping remain open.
- Management interviews candidates and approves their expertise/degrees for public-profile use before accepting them.
- Display patient-imported Arabic data alongside its backend-generated English translation, preserve the source, and label machine translation. Do not send private clinical content to a translation vendor from the browser.
- Patients may optionally review the session and doctor within 48 hours from session end, using a rating out of 10. Management sees all reviews; the patient author sees their own and the session doctor sees that review. Do not show it to other patients or unrelated doctors.

### Patient website

- The patient website and Flutter app both support patient sign-in, booking, and payment.
- Patient sign-in is phone plus a one-time code. Optional username/email setup and verified recovery follow backend rules.
- Patients can view all information about their own case in the patient experience; the definition of internal administrative metadata remains open.
- Patients can book and pay for a recommended Motmaan program from the patient website.
- Required online checkout options: mada, Apple Pay, credit/debit cards, Tabby, and Tamara. Tap Payments is the preferred provider candidate to evaluate and PayTabs is a comparison; gateway and merchant approvals are not final.
- An online booking becomes confirmed only after the backend reports provider-confirmed successful payment. Never trust the browser redirect or a frontend-supplied success state by itself.
- Do not store provider secrets or raw payment card data in frontend code. Use backend-created payment attempts and the chosen provider's approved checkout integration.
- Cash is accepted only at an attended in-person session; it is not an online checkout method. Booking by bank transfer is deferred for later discussion.
- Administrators create and control package offers, sale/expiry, and settings. Render current API-provided package terms and entitlements; do not hardcode pricing or expiry rules.
- On-time patient cancellation can offer a refund to the original payment method or Motmaan wallet credit; package entitlement is restored. The admin-configured deadline has no default. Late-cancellation and rescheduling rules are deferred.
- If Motmaan or the assigned doctor cancels, credit the patient in the internal Motmaan wallet. Bank withdrawal requires the patient to contact administration; detailed payout flow is deferred.
- Doctors assign self-care tasks and program recommendations. Doctors control patient-task reminder scheduling; the backend sends task push notifications according to the doctor-defined schedule and recurrence, and the patient app displays them. Patients can mark occurrences complete or missed and give a reason; doctors can review progress. Doctor controls include time of day, selected weekdays, start/end dates, and reminders per day. Changes to recurring patient tasks apply only to future occurrences and preserve earlier completion history. Numeric limits and weekly summaries remain open.
- Patients submit support tickets; administrators resolve them. Statuses are Open, In progress, Waiting for patient, Resolved, and Closed. Send push updates and show an in-ticket new-message indicator. Email the patient a satisfaction survey rated out of 10 with optional comments and one submission per ticket when the ticket is Closed; link the response to the resolving administrator. Management sees all responses; the patient sees their own.

### Management dashboard

- Permission-driven management workspace for operations, finance, configuration, providers, reporting, packages, support tickets, recruitment, and other approved modules.
- Administrators create and control package offers and configure relevant policy settings, including cancellation cutoff, no-show grace, and reminder lead time; no numeric defaults are approved.
- Initial staff groups are manager, reception, administrator, and doctor, with accountant participation required for internal tasks. The detailed permission matrix is still being defined.
- Show or hide dashboard actions based on granted permissions. The API still enforces each permission and resource scope independently.
- Management controls doctor active status; only active doctors may enter the doctor dashboard. The UI should reflect the backend's authoritative status.
- Management sees all patient session/doctor reviews and ticket-satisfaction responses. The session-review author and session doctor can see that session's review; unrelated users cannot.
- Percentage compensation rates are configurable in the system; exact rate scope and calculation basis remain open.
- Motmaan/doctor-initiated appointment cancellation credits the Motmaan wallet. Wallet-to-bank transfer requires contacting administration and remains a future workflow decision.
- Management needs an administrator support queue to assign, reply, resolve, and close patient tickets within the eventual permissions. Reopen rules, attachment constraints, notification channels, and response targets remain open.
- Candidate acceptance triggers automatic backend doctor account/role provisioning and SMS invitation; do not add a second manual account-creation step.
- A role grants only its configured capabilities. The API enforces all sensitive permissions and row/resource access.

### Doctor/specialist dashboard

- Each doctor, including external doctors, can view only records for their own assigned patients. This user decision is narrower than the broad specialist-access line in the supplied requirements document.
- Assignment, transfer, substitute coverage, and emergency access are deferred. Do not infer access by changing a patient identifier or relying only on UI filters.
- Doctors can access their schedule and assigned case information, and handle diagnoses, treatment plans, prescriptions, reports, session records, and tasks within granted permissions, assigned-patient scope, and applicable qualification rules. They assign repeatable self-care tasks or Motmaan program recommendations and review patient task progress.
- Practitioner compensation varies by arrangement. This dashboard should show only the doctor’s authorized own compensation details; finance/configuration rules remain backend-owned.

## Attendance, doctor capacity, and readiness — clarified 4 October 2026

- Reception marks an in-person patient Arrived. Actual consultation end is patient departure; the doctor writes notes afterward and may write a prescription before departure. Keep clinical end distinct from later Finished confirmation, which triggers an emailed rating request. Do not require notes before departure or invent a mandatory note-save gate; exact confirmation validation remains open. Show a clear confirmation step and authoritative states. Rating remains optional, out of 10, within the existing 48-hour-from-session-end rule; delayed-confirmation timing and web editing remain open. The unanswered-rating popup is confirmed for the patient mobile app, not newly required for the website. Refresh saved review state across email/web/app submissions.
- Count allocated duration from actual consultation start. At expiry show a red doctor warning if unfinished; notify reception after a system-configured delay if still unfinished. Display API-authoritative timing/status; actual-start capture and delay value/default/configuration owner remain open. Provide the doctor's Extend session action using a period configurable by doctor or management; values/limits/repeat-extension rules remain open. Keep booked duration, active extension, actual consultation end, notes, and Finished confirmation distinct. Proposed: refresh warnings after extension/completion and avoid stale/duplicate escalation. Do not auto-complete, end an attended consultation, apply no-show, shift later bookings, or add charges. No-show still uses scheduled start plus separate attendance grace. Later-booking conflicts, pending-documentation warnings, and online applicability remain open.
- Doctor and management dashboards need controls for daily session count, configurable session duration, different working hours per weekday, breaks between sessions, and days off, within granted permissions and branch scope. Five daily sessions and X minutes are examples only. Count/duration setting edits affect only unbooked slots; existing bookings keep their booked date/time and duration. Exact duration/break configuration and day-off conflicts remain open. Do not infer a complete permission matrix or automatic rescheduling authority. Show booked appointment values from the API rather than applying current doctor settings.
- Patient booking uses scheduled free slots and next-available date/time. When there are no available appointments at all in search results, show separate next-available suggestions, potentially outside the selected range. Keep matching non-date filters, branch scope, and employed-first/external fallback; do not silently widen the range. Suggestion count/horizon remain open. Waiting-room queue/estimated-wait display was not selected.
- Include the doctor's Ready for patient button; its confirmed action notifies both patient and reception. Channels remain open; advance reminders remain separate. Keep attendance, readiness, completion, feedback, and payment distinct.

## Shared interaction and quality requirements

- All public and authenticated web pages work well on mobile, tablet, and desktop; support Arabic RTL and English LTR, keyboard/touch access, readable forms, and responsive tables/calendars.
- Use `Asia/Riyadh` for schedule, date-boundary, recurrence, and display behavior; API event instants are persisted as UTC.
- Handle loading, empty, validation, permission-denied, payment-pending, provider-failure, and retry states explicitly.
- Query only bounded data and render only fields returned for the current authorization context. Do not download all clinical or finance data and hide it in the browser.
- Keep all medical files private; use backend-authorized upload/download flows. Avoid clinical details in URLs, analytics, logs, or third-party error tools.
- Avoid duplicating actions during refresh, repeated submission, provider return, or uncertain network responses. Backend idempotency and authoritative state must drive the interface.

## Provider documentation findings for later development

Read the [4 October provider review](../planning/17-provider-documentation-development-notes.md) alongside the provider guide. These are research findings and proposed verification tasks; selections and deferred business policies are unchanged.

- Register checkout domains where required; choose a provider-supported responsive checkout after account approval. Preserve API-authoritative pending/confirmed/refund states after returns, refresh, duplicate submissions, or a lost redirect. Server callback verification differs across providers and belongs on the backend.
- Video access and recording readiness require authorized API state. Private playback may include multiple HLS assets; do not assume a single public video URL or infer playback permission from doctor/patient identity.
- Show accounting-sync failures separately from operational payment/booking state in permitted management views. Provider settings expose masked references/status only under a specific permission.
- Wati acceptance is distinct from delivery; management delivery histories should reflect the eventual API states. Staff unread notifications remain persisted Motmaan records independent of live transport availability. Translation location and clinical-review approval remain unresolved.
- Wati is now a named WhatsApp/SMS evaluation candidate; see [Wati delivery notes](../planning/17-provider-documentation-development-notes.md#whatsapp-and-sms-handling-wati). Management should show API-authorized per-channel attempts and fallback/receipt state, with secrets masked. Patient OTP expiry/resend state comes from the backend; delivery is not verification. Doctor acceptance still requires SMS, whose route and invitation support must be validated.

## Open or deferred items affecting web frontend

- Doctor-level **تفضيلات** influencing patient-facing doctor display priority are explicitly deferred. Configuration ownership, management/doctor UI, ranking rules, and interaction with employed-first/external fallback remain unspecified; use the eventual API-authoritative order.
- Payment gateway selection, merchant onboarding, and exact web checkout flow.
- Booking by bank transfer is deferred; cash is limited to attended in-person sessions.
- Late-cancellation and rescheduling behavior; explicitly deferred.
- Doctor-patient assignment and substitute access; explicitly deferred.
- Insurance integration (capture readiness vs live claims); explicitly deferred for the project owner.
- Qoyod API/account validation and correction/reconciliation workflow; planning direction assigns official accounting/e-invoicing documents to Qoyod.
- Support-ticket reopen rules, attachments, notification channels, and service targets.
- Support-ticket survey rating labels, comment length, expiry, and reopened/reclosed behavior; optional comments and one submission per ticket are confirmed.
- Patient session-review rating labels, comment length/requiredness, web editing/retraction, and management reports; mobile edits within the original 48-hour window are confirmed.
- Translation vendor approval, data location/privacy, and clinical review workflow.
- Expertise catalog labels, candidate approval, public profile fields, and patient filter scope.
- Reconcile source-only feature details and staff role permissions; all project requirements/features are stage one except explicit deferred items.
- Doctor deactivation behavior for existing sessions and reactivation flow; clinical qualification rules; direct report/prescription issuance is confirmed.
- Exact recruitment form fields/documents, credential verification, and public doctor profile fields.
- Percentage rate scope and calculation basis.
- Patient-task schedule limits, weekly summaries, and exact support-ticket push/email triggers.
- Package offer configuration fields; patient-facing case-data boundary for internal admin metadata.
- Exact analytics/reports, notification channels, brand assets/content workflow, and performance budgets.

## Keep this handoff current

When the user confirms a rule that changes a web page, interaction, permission, or API dependency, update this file and the central decision register. Keep recommendations and deferred items labeled. Do not invent final API endpoints or weaken authorization for frontend convenience.

## Related notes

- [Project overview](../../README.md)
- [System scope](../planning/01-system-scope.md)
- [Booking and finance](../planning/02-booking-and-finance.md)
- [Integrations and storage](../planning/03-integrations-and-storage.md)
- [Identity and access](../planning/05-identity-and-access.md)
- [Decisions and open questions](../planning/06-decisions-and-open-questions.md)
- [Practitioner compensation and recruitment](../planning/08-practitioner-compensation-and-recruitment.md)
- [Support tickets](../planning/11-support-tickets.md)

## Latest clarified behavior

- Patients, doctors, schedules, and reporting are branch-restricted. Respect API-authorized branch scope on lists, details, reports, and exports; cross-branch exceptions remain open.
- Prioritize employed doctors in discovery/booking; show external doctors when employed doctors are full over the selected start/end date range and matching filters. Equal dates mean one day. Backend fallback eligibility is authoritative; mixed-date presentation remains open. Operational access rules are the same; compensation stays distinct.
- Management verifies candidate degrees and applicant data before activation. Verification procedure remains open; exact applicant fields/documents remain deferred.
- Session reviews support comments (recommended as optional) and exactly 48 hours from session end; mobile edits are allowed within that original window. Web editing remains unspecified; render API-authoritative saved feedback and eligibility. Ticket satisfaction comments are optional and submission remains once per ticket.
- Doctor dashboard controls patient tasks and reminder times, selected weekdays, start/end dates, and reminders per day. Backend schedules/sends push; administration still controls appointment reminder lead time. Changes to recurring patient tasks apply only to future occurrences and preserve earlier completion history. Numeric schedule limits remain open.
- Internal staff-task workspace: reception/accountant assignment with several assignees, details, Low/Normal/High/Urgent priority, optional deadlines/overdue indication, comments, and attachments. Status updates automatically from actions; mappings and multi-assignee completion remain open. Assignment/comment/status/deadline/overdue events notify live in the website. Management sees full authorized-branch task details; staff see full created/assigned task details. Live events and files must obey API scope. Exact staff grants stay deferred; assignment does not grant clinical/finance authority. See [internal staff tasks](../planning/15-internal-staff-tasks.md).
- See [external provider guide](../planning/16-external-provider-guide.md) for browser configuration responsibilities.

## Confirmed clarification - 4 October 2026

- Doctors may issue finalized clinical reports and prescriptions directly, without a separate management approval step, within granted permissions, assigned-patient scope, and applicable qualifications.
- Internal tasks close automatically once the required completion condition is met, without creator approval; the multi-assignee completion condition remains open. Staff notifications are retained in an unread list, including events missed while the website was closed. Transport and detailed recipient rules remain open.
