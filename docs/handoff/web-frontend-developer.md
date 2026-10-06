# Web frontend developer handoff

Updated: 4 October 2026. Status: planning handoff. The project is not in implementation; this file captures current product direction and should be updated as decisions are confirmed.

**Confirmed recovery and adult-family consent:** Confirmed role baseline: reception handles scoped branch bookings/contact details, accountants handle scoped finance, doctors handle assigned patients, and managers receive only owner-assigned operational/reporting permissions. Separate clinical/recording grants remain required; the full granular action matrix is not approved by this baseline. Confirmed self-service safeguard: turning staff SMS verification off or changing its phone requires password confirmation and an SMS code to the existing verified phone. A lost phone uses the approved administrator recovery process. Detailed audit, conflict handling and administrator-change safeguards remain proposals.

Staff lost-phone recovery is approved through an authorized account administrator after identity verification; recovery of the last available administrator requires owner verification. An adult family member must explicitly consent before a parent or another authorized family member can view their clinical records. Family membership, package sharing and payment rights do not establish clinical consent; detailed consent/proof/revocation and minor rules remain open.

**Confirmed session limits:** Staff web expires after 30 minutes inactive or eight hours total; patient web after 30 minutes inactive or 24 hours total; patient app after 30 inactive days or 90 days total. Reauthentication must support active consultations and unsaved forms safely. The 15-minute mobile access-token lifetime, storage/revocation mechanism and meaningful-activity details remain engineering proposals.

**Detailed contract planning, 5 October 2026:** Workflow 21 now describes proposed identity-review/recovery states, adult consent execution and an operation-contract table. Design pending/rejected/conflict/reauthentication states without exposing candidate records. Phone delivery, verified identity linking and clinical permission are distinct outcomes. Evidence rules, final API payloads, consent/minor mechanics and remaining provider choices are still open.

## Readiness and shared contracts

**Current selected workflow:** [Authentication/authorization draft](../planning/21-authentication-and-authorization-workflows.md) defines proposed transitions, challenge/session contracts, access matrix and acceptance scenarios. Patient login uses SMS with six-digit codes, five-minute validity, a 60-second resend interval and five failed attempts per challenge. The owner delegated imported linking to the recommended hybrid: documented verified links prepared during migration, with reception reviewing ambiguous/unverified exceptions before record access. Clinical-record and recording grants are separate and assigned only by administrators explicitly authorized by the owner for access management. Reception verifies patient identity when both recovery channels are lost; an authorized account administrator approves recovery. A deactivated doctor may finish/save only the already-active consultation; new work is blocked immediately. Detailed evidence, remaining role defaults, transfer scope and exception termination still need contracts. [Provider setup](../planning/16-external-provider-guide.md) now records no accounts currently available and owner responsibility for all accounts. Technical delegation/provider selections remain open.

**Confirmed staff login:** Accept username, verified email or phone number plus password. SMS additional verification is enabled by default; each staff user/doctor controls their own setting, while an administrator with the relevant permission can control it for all accounts. Render the setting and challenge from the backend. Self-change verification, administrative audit/recovery and concurrent setting-change safeguards are proposed in document 21; patient OTP remains separate and required.


**Reviewer assessment, 4 October 2026:** Ready for UX/design and workflow contract preparation; not a complete implementation handoff. Read the [readiness review](../planning/20-development-readiness-review.md) and [shared contract checklist](shared-contract-checklist.md). Implementation still needs explicit user authorization and completion of the gates for the affected workflow. API-authoritative behavior requires an agreed field/state/error contract; this file is not that contract.

Prioritize minimum staff permissions, staff sign-in, cash/room workflows, clinical form definitions, appointment transitions and metric definitions (R02–R07, R10–R12). Prepare the shared patient account lifecycle/deletion path and mobile-return/deep-link support (R13). Keep patient-private data in authenticated patient views; public profiles expose only approved public fields. These are review follow-ups, not approved screen/API designs.

## Product and technical context

- This handoff covers the public Motmaan website and its Join us form, the patient website, management dashboard, and doctor/specialist dashboard.
- Motmaan is the only organization in scope. The first release serves one branch, with more branches possible later.
- Backend: ASP.NET Core and EF Core are selected. Frontend framework, repository structure, and API contracts remain open. Do not assume a framework or implement against invented endpoints.
- Do not start scaffolding or implementation until the user explicitly moves the project into implementation.
- Performance and security matter. The API is the authority for identity, permissions, record scope, prices, booking state, and provider payment confirmation.

- Patients, doctors, schedules, and reporting are branch-restricted. Respect API-authorized branch scope on lists, details, reports, and exports; cross-branch exceptions remain open.

## Required web surfaces

### Public center website and Join us

- Present Motmaan's public identity, services, specialist profiles, and other approved content. Brand assets and final content ownership are not yet defined.
- The public Join us form collects candidate information. Submission does not create a doctor account or grant dashboard access.
- The first stage accepts doctor applications only; administrators control openings and applications. Candidate therapeutic expertise is a confirmed multi-select from the database-backed catalog; labels/selection limits and review details remain open.
- After an authorized management acceptance, the backend automatically provisions/resolves the doctor account, assigns the approved doctor role, and sends/schedules an SMS invitation. Show truthful application status without exposing internal notes or credentials.
- Public and authenticated sites must support Arabic/English, RTL/LTR, and mobile, tablet, and desktop layouts.
- Patient doctor discovery should filter by expertise/concern, specialty, language, appointment mode, and availability from the API. Render approved public profile data only; taxonomy and candidate review rules remain open. See [practitioner expertise](../planning/13-practitioner-expertise.md).
- Combine selected filter categories with AND and values within one category with OR; availability is checked by the API.
- Use [the current website field/document reference](../planning/19-recruitment-current-website-reference.md), plus therapeutic expertise multi-select. Specialist required uploads are CV and health-specialties certificate, with conditional current-job license question. The administrative reference includes CV and conditional portfolio. Credential verification/public-profile mapping stay open; initial doctor-only recruitment scope is not expanded without a user decision.
- Management interviews candidates and approves their expertise/degrees for public-profile use before accepting them.

- Post-hiring public biography/expertise changes require management approval before publication. Doctor submission and management review/rejection details remain open. Proposed: keep last approved public values while updates await review; public discovery only renders approved data.
- Management verifies candidate degrees and applicant data before activation. Current-site applicant fields/documents are recorded; verification procedure, extra credential evidence and upload limits remain open.

### Patient website

- The patient website and Flutter app both support patient sign-in, booking, and payment.
- Patient sign-in is phone plus a one-time code. Optional username/email setup and verified recovery follow backend rules.
- Patients can view all information about their own case in the patient experience; the definition of internal administrative metadata remains open.
- Patients can book and pay for a recommended Motmaan program from the patient website.
- Required online checkout options: mada, Apple Pay, credit/debit cards, Tabby, and Tamara. Tap Payments is the preferred provider candidate to evaluate and PayTabs is a comparison; gateway and merchant approvals are not final.
- An online booking becomes confirmed only after the backend reports provider-confirmed successful payment. Never trust the browser redirect or a frontend-supplied success state by itself.
- Do not store provider secrets or raw payment card data in frontend code. Use backend-created payment attempts and the chosen provider's approved checkout integration.
- Cash is accepted only at an attended in-person session; it is not an online checkout method. Booking by bank transfer is not allowed.
- Administrators create and control package offers, sale/expiry, and settings. Render current API-provided package terms and entitlements; do not hardcode pricing or expiry rules.
- Block patient cancellation and appointment modification with less than 24 hours remaining, using API-authoritative eligibility. At/above the cutoff preserve original-method refund/wallet choice and package-session restoration. Staff exceptions and other modification details remain open.
- Motmaan/doctor cancellation credits the wallet. The patient requests payout inside the wallet; only service-refund-origin funds are withdrawable and system administrator or accountant approves. Coupon credit is not withdrawable. Execution/verification and detailed statuses remain open.
- Doctors assign self-care tasks and program recommendations. Doctors control patient-task reminder scheduling; the backend sends task push notifications according to the doctor-defined schedule and recurrence, and the patient app displays them. Patients can mark occurrences complete or missed and give a reason; doctors can review progress. Doctor controls include time of day, selected weekdays, start/end dates, and reminders per day. Changes to recurring patient tasks apply only to future occurrences and preserve earlier completion history. Weekly summaries go to both patient and assigned doctor; numeric task limits and summary content, timing and channels remain open.
- Patients submit support tickets; administrators resolve them. Statuses are Open, In progress, Waiting for patient, Resolved, and Closed. Send push updates and show an in-ticket new-message indicator. Email the patient a satisfaction survey rated out of 10 with optional comments and one submission per ticket when the ticket is Closed; link the response to the resolving administrator. Management sees all responses; the patient sees their own.

- Patients may reopen their resolved/closed tickets without a time limit, within API-authoritative ownership and eligibility. Resulting status mapping remains open; reopening does not grant a second satisfaction-survey response.
- Established verified-email proof is sufficient for lost-phone replacement without administration review. Use the backend challenge to the previously verified address and verify the replacement phone; maintain account identity and recovery safeguards. Newly supplied contacts are not proof of old-account ownership.
- Prioritize available salary-paid practitioners in discovery/booking; preserve external fallback when prioritized practitioners are full over the selected start/end date range and matching filters. Equal dates mean one day. Backend fallback eligibility is authoritative; mixed-date presentation remains open. Operational access rules are the same; compensation stays distinct.
- Session reviews support comments (recommended as optional) and exactly 48 hours from session end; mobile edits are allowed within that original window. Web editing remains unspecified; render API-authoritative saved feedback and eligibility. Ticket satisfaction comments are optional and submission remains once per ticket.
- Patient selects practitioner then a defined repeated-session package. Family members may consume sessions and change practitioner with a price difference if applicable. Show server-calculated eligibility, remaining sessions, difference and payment state; a cheaper-practitioner switch does not refund the difference. Package sharing does not grant shared clinical access. Management controls package offers/settings. Future treatment pathways across different practitioners/services are deferred.
- Package-stop refund preview uses base prices for used sessions. Confirmed example: SAR 1,000 paid for four originally SAR 1,200 sessions, two used at SAR 300 each, refund SAR 400. Discounted per-session allocation SAR 250 is a separate revenue concept. Consumed no-show sessions also use standalone/base price outside the package for refund repricing; no doctor incentive is earned. Tax, original-versus-performing practitioner base-price attribution after transfer, paid differences and commission reversals remain open.
- Show a seven-minute checkout countdown from the server hold deadline; do not reset it after reload. At unpaid expiry display «انتهى وقت الدفع، يرجى المحاولة مرة أخرى» and refresh availability. The appointment-start countdown is separate. Provider return/elapsed local timer does not establish or erase verified payment; late-payment resolution remains backend-owned.
- Father or mother adds members. Each member sees own reports/sessions/diagnoses and invoices if they paid. Provide API-eligible «الخروج من العائلة», notify family head and enable independent booking/ordinary patient powers. Proof/consent, cross-member permissions, minor/guardian interaction, existing appointments and entitlement after exit remain open. UI must refresh/revoke family data according to current API access.
- Wallet shows withdrawable refund-origin balance and nonwithdrawable coupon credit separately. Patient submits request inside wallet; system administrator or accountant approves within granted financial scope. Execution/rejection/timing and bank verification remain open; approval is not success of transfer.
- Assessment platform already exists per user; integrate rather than recreate it. See [programmer questions](../planning/18-assessment-platform-integration-questions.md). Patient/practitioner result views and management connection health depend on verified API contracts and access; UI embedding/redirect/SSO are not selected. No insurance now; prepare for future NPHIES/Waseel without current live claims or insurer checkout.
- Display patient-imported Arabic data alongside its backend-generated English translation, preserve the source, and label machine translation. Do not send private clinical content to a translation vendor from the browser.
- Patients may optionally review the session and doctor within 48 hours from session end, using a rating out of 10. Management sees all reviews; the patient author sees their own and the session doctor sees that review. Do not show it to other patients or unrelated doctors.

### Management dashboard

- Permission-driven management workspace for operations, finance, configuration, providers, reporting, packages, support tickets, recruitment, and other approved modules.
- Administrators create and control package offers and configure relevant policy settings, including no-show grace and reminder lead time; no numeric defaults for those are approved. Patient cancellation/modification cutoff is now confirmed as 24 hours.
- Initial staff groups are manager, reception, administrator, and doctor, with accountant participation required for internal tasks. The detailed permission matrix is under active clarification.
- Staff/doctors use username, verified email or phone number plus password. SMS additional verification is enabled by default and each person manages their own setting; an administrator with the relevant permission can control it for all accounts. Render the API-required challenge/configuration; the browser cannot skip an enabled challenge. Change/recovery safeguards remain proposed. Patient phone OTP is a separate authentication context; no SMS vendor is selected by this decision.
- Show or hide dashboard actions based on granted permissions. The API still enforces each permission and resource scope independently.
- Management controls doctor active status; only active doctors may enter the doctor dashboard. The UI should reflect the backend's authoritative status.
- Management sees all patient session/doctor reviews and ticket-satisfaction responses. The session-review author and session doctor can see that session's review; unrelated users cannot.
- Percentage rates vary by practitioner and use net revenue after tax and discounts; further deductions, service overrides, edit authority and refund reversals remain open. Above-target commission applies only to additional eligible revenue over the target.
- Provide a scoped wallet-payout review queue for system administrator/accountant approval of service-refund funds. Motmaan/doctor cancellation still credits the wallet; no coupon withdrawal. Separate request/approval from bank execution and reflect API-provided status.
- Management needs an administrator support queue to assign, reply, resolve, and close patient tickets within the eventual permissions. Patients may reopen their resolved/closed tickets without a time limit; resulting status mapping, attachment constraints, notification channels and response targets remain open.
- Candidate acceptance triggers automatic backend doctor account/role provisioning and SMS invitation; do not add a second manual account-creation step.
- A role grants only its configured capabilities. The API enforces all sensitive permissions and row/resource access.

- Management dashboard includes revenue, bookings, unpaid amounts, and patient satisfaction within authorized branch/reporting scope. "All" selects these four offered examples; definitions, period filters, layout/order, and drill-downs remain open. Do not invent formulas or grants from the dashboard requirement.
- Internal staff-task workspace: reception/accountant assignment with several assignees, details, Low/Normal/High/Urgent priority, optional deadlines/overdue indication, comments, and attachments. Status updates automatically from actions; mappings and multi-assignee completion remain open. Assignment/comment/status/deadline/overdue events notify live in the website. Management sees full authorized-branch task details; staff see full created/assigned task details. Live events and files must obey API scope. Exact staff grants are under active clarification; assignment does not grant clinical/finance authority. See [internal staff tasks](../planning/15-internal-staff-tasks.md).
- Internal tasks close automatically once the required completion condition is met, without creator approval; the multi-assignee completion condition remains open. Staff notifications are retained in an unread list, including events missed while the website was closed. Transport and detailed recipient rules remain open.

### Doctor/specialist dashboard

- Each doctor, including external doctors, can view only records for their own assigned patients. This user decision is narrower than the broad specialist-access line in the supplied requirements document.
- Practitioner changes support session-only assignment and transfer of ongoing follow-up. Selection/approval authority, effective time, detailed access, substitute coverage and emergency access remain open. Do not infer access by changing a patient identifier or relying only on UI filters.
- Doctors can access their schedule and assigned case information, and handle diagnoses, treatment plans, prescriptions, reports, session records, and tasks within granted permissions, assigned-patient scope, and applicable qualification rules. They assign repeatable self-care tasks or Motmaan program recommendations and review patient task progress.
- Practitioner compensation varies by arrangement. This dashboard should show only the doctor’s authorized own compensation details; finance/configuration rules remain backend-owned.

- The doctor can edit a finalized clinical report directly within permissions and assigned-patient/branch scope. Do not require a separate revised-report issuance workflow. Protected edit history is proposed; audit and patient-update presentation remain open. This does not select prescription or accounting correction rules.
- Weekly treatment-task summaries go to both patient and assigned doctor; contents, timing, and channels remain open. The doctor view remains restricted to assigned patients.
- Doctor dashboard controls patient tasks and reminder times, selected weekdays, start/end dates, and reminders per day. Backend schedules/sends push; administration still controls appointment reminder lead time. Changes to recurring patient tasks apply only to future occurrences and preserve earlier completion history. Numeric schedule limits remain open.
- Doctors may issue finalized clinical reports and prescriptions directly, without a separate management approval step, within granted permissions, assigned-patient scope, and applicable qualifications.
- Support both practitioner-change modes: «جلسة فقط» retains the existing follow-up practitioner, while «نقل مسؤولية المتابعة» assigns ongoing responsibility to the new practitioner. Show API-authoritative mode, responsibility and allowed actions in relevant patient/staff views. Selection/approval actors, placement of controls and effective timing remain open. The patient's choice of practitioner alone does not approve an automatic transfer or grant broader record access. Former-practitioner access and existing tasks/bookings/assessments after transfer still need rules.

## Attendance, doctor capacity, and readiness — clarified 4 October 2026

- Reception marks an in-person patient Arrived. Actual consultation end is patient departure; the doctor writes notes afterward and may write a prescription before departure. Keep clinical end distinct from later Finished confirmation, which triggers an emailed rating request. Do not require notes before departure or invent a mandatory note-save gate; exact confirmation validation remains open. Show a clear confirmation step and authoritative states. Rating remains optional, out of 10, within the existing 48-hour-from-session-end rule; the deadline starts at actual consultation end even if confirmation is delayed. Reception records actual in-person end if the doctor forgets; detailed recording/correction permissions and web editing remain open. The unanswered-rating popup is confirmed for the patient mobile app, not newly required for the website. Refresh saved review state across email/web/app submissions.
- Count allocated duration from actual consultation start. At expiry show a red doctor warning if unfinished; notify reception after a system-configured delay if still unfinished. Display API-authoritative timing/status; actual-start capture and delay value/default/configuration owner remain open. Provide the doctor's Extend session action using a period configurable by doctor or management; values/limits/repeat-extension rules remain open. Keep booked duration, active extension, actual consultation end, notes, and Finished confirmation distinct. Proposed: refresh warnings after extension/completion and avoid stale/duplicate escalation. Do not auto-complete, end an attended consultation, apply no-show, shift later bookings, or add charges. No-show still uses scheduled start plus separate attendance grace. Allow extension into a later booked appointment with a warning to the doctor that another patient is waiting; exact waiting/conflict detection, pending-documentation warnings and online applicability remain open.
- Doctor and management dashboards need controls for daily session count, configurable session duration, different working hours per weekday, breaks between sessions, and days off, within granted permissions and branch scope. Five daily sessions and X minutes are examples only. Count/duration setting edits affect only unbooked slots; existing bookings keep their booked date/time and duration. Exact duration/break configuration and day-off conflicts remain open. Do not infer a complete permission matrix or automatic rescheduling authority. Show booked appointment values from the API rather than applying current doctor settings.
- Patient booking uses scheduled free slots and next-available date/time. When there are no available appointments at all in search results, show separate next-available suggestions, potentially outside the selected range. Keep matching non-date filters, branch scope, and salary-paid availability priority/external fallback; do not silently widen the range. Suggestion count/horizon remain open. Waiting-room queue/estimated-wait display was not selected.
- Include the doctor's Ready for patient button; its confirmed action notifies both patient and reception. Channels remain open; advance reminders remain separate. Keep attendance, readiness, completion, feedback, and payment distinct.
- Reception assigns a room per appointment. Show available-room suggestions for the selected appointment, then let reception choose; do not automatically dedicate a room to a doctor's whole shift. Use API-authorized branch/availability state and recheck the selection when saving. Self-service confirmation timing, suggestion ranking, room constraints and later room changes remain open.

## Online recording, interruption review and seeded-data access — 4 October 2026

- Every online consultation must be recorded for safety and performance review. Show consent and API-authoritative recorder readiness/status; do not offer an unrecorded-session toggle. Consent/refusal and recorder-failure handling remain open, and recording remains separate from permission-controlled playback.
- If connection failure prevents completion, management may review the case and grant a free replacement session; the patient may open a support ticket for review. Provide patient ticket access and management review/grant presentation within API-authorized scope. A disconnect or ticket submission does not automatically grant a session or mark the original Finished. Detailed grant controls/conditions and partial-session accounting remain open.
- Existing data is seeded/imported before operation begins. Display only data authorized through verified account-to-patient links. The adopted approach prepares documented verified links during migration and routes ambiguous/unverified links to reception before access. Seeded identifiers, shared/duplicate-phone reconciliation and evidence requirements remain open; seeding alone does not authorize phone-only medical-file access. Emdaad export formats remain deferred.

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

- See [external provider guide](../planning/16-external-provider-guide.md) for browser configuration responsibilities.

## Open or deferred items affecting web frontend

- Prioritize available salary-paid practitioners in the API-provided order, retaining branch/date/filter/external fallback rules. Ranking configuration ownership, tie-breaks and mixed-date display remain open; salary/rate details are private.
- Payment gateway selection, merchant onboarding, and exact web checkout flow.
- Booking by bank transfer is not allowed; cash is limited to attended in-person sessions.
- Staff cancellation/modification exceptions and further change details remain open; patient changes within 24 hours are blocked.
- Practitioner-change selection/approval, timing and detailed access, plus substitute coverage, remain open/deferred; both session-only and ongoing-follow-up transfer modes are confirmed.
- No insurance currently; future NPHIES/Waseel operations/contracts are deferred, with integration readiness requested.
- Qoyod API/account validation and correction/reconciliation workflow; planning direction assigns official accounting/e-invoicing documents to Qoyod.
- Support-ticket reopening status mapping, attachments, notification channels and service targets. Patient reopening without a time limit is confirmed.
- Support-ticket survey rating labels, comment length, expiry, and reopened/reclosed behavior; optional comments and one submission per ticket are confirmed.
- Patient session-review rating labels, comment length/requiredness, web editing/retraction, and management reports; mobile edits within the original 48-hour window are confirmed.
- Translation vendor approval, data location/privacy, and clinical review workflow.
- Expertise catalog labels, candidate approval, public profile fields, and patient filter scope.
- Reconcile source-only feature details and staff role permissions; all project requirements/features are stage one except explicit deferred items.
- Doctor deactivation blocks new work immediately and allows only the already-active consultation to finish/save. Exception termination, abandoned-session handling and reactivation flow remain open; clinical qualification rules; direct report/prescription issuance is confirmed.
- Credential verification, extra evidence/file limits and public doctor profile mapping; existing-site form baseline is documented. Initial administrative recruitment expansion needs an explicit decision.
- Further net-revenue deductions, optional service-specific rates, edit authority and refund/period-close adjustments.
- Patient-task schedule limits, weekly summary content/timing/channels, and exact support-ticket push/email triggers. Summary recipients are both patient and assigned doctor.
- Package offer configuration fields; patient-facing case-data boundary for internal admin metadata.
- Exact analytics/reports, notification channels, brand assets/content workflow, and performance budgets.

- Multi-assignee task completion and Emdaad export discussion remain deferred; preserve full migration at launch. Current packages repeat practitioner sessions and future treatment pathways are deferred. Assessment questions are prepared, pending its programmer's API/SSO/result/payment details. No implementation is authorized.

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
