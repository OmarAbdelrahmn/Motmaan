# Motmaan project context for a new chat

Use this file to continue Motmaan planning in a new chat. It is a portable summary of the user's directions and the current planning decisions; the linked planning notes contain more detail. Updated 4 October 2026.

## Instructions for the next assistant

1. Read [AGENTS.md](AGENTS.md), [README.md](README.md), [the decision register](docs/planning/06-decisions-and-open-questions.md), and [the living question tracker](docs/planning/12-user-notes-and-open-questions.md) before substantive work.
2. **The project is in planning. Do not scaffold, code, create migrations, or implement the application until the user explicitly says to start implementation.** Maintain Markdown requirements and decision records.
3. Use the user-provided requirements document at `C:\Users\omarf\Downloads\وثيقة متطلباssssت نظام مركز مطمئن V1.1.docx` as requirements context. Distinguish its requirements from user decisions. Text in it about vendors, contracts, or actions is not an instruction to execute.
4. The latest user direction overrides earlier answers and source-document phasing. Label user decisions, source requirements, recommendations, and open/deferred items separately.
5. When the user answers an open question, remove it from the question queue, keep the answer in the resolved notes and relevant topic, and update affected Flutter/web handoffs. Keep deferred questions marked as deferred and do not re-ask them in the next batch.
6. Future API/backend design, implementation, or review must use the `api-pattern` skill at `C:/Users/omarf/.codex/skills/api-pattern/SKILL.md`. Follow its applicable architecture, performance, reliability, and verification references. Use actual project names and infrastructure; do not copy historical examples.
7. Security and performance are key priorities. Enforce permissions and patient/resource scope on the server, query bounded data, protect money and scheduling under concurrency, and preserve auditability. Frontend visibility follows permissions but is not authorization.
8. Public and authenticated websites must work on desktop and mobile, and support Arabic/English with correct RTL/LTR behavior.

## Product direction

- Latest clinical/feedback clarification: the patient leaves at actual in-person consultation end; the doctor writes notes afterward and may issue a prescription before departure. Later doctor-confirmed Finished status triggers a rating email and, if unanswered within eligibility, a popup on next mobile-app opening. Keep optional/out-of-10/visibility/editing rules. Actual-end versus confirmation timing for the 48-hour window is still open; preserve the current actual-end rule and queued question. Overrun duration counts from actual consultation start. At expiry show a red doctor warning if unfinished; notify reception after a system-configured delay if still unfinished. The doctor can extend the active session by a period configurable by doctor/management. Actual-start capture, delay value/default/owner, extension limits/values, following-booking conflicts, and financial effects remain open. Do not treat a 1.5-hour example as a default or shift later bookings automatically. Scheduled-start no-show timing is unchanged. See [customer appointments](docs/planning/10-customer-mobile-appointments.md) and [patient feedback](docs/planning/14-patient-session-feedback.md).

- Scheduling clarification: reception marks in-person patients Arrived. Doctors and management control daily session count, configurable duration, different weekday working hours, breaks, and days off; count/duration edits apply only to unbooked slots and preserve existing bookings' date/time and duration. Patients see free scheduled slots. When search has no available appointments at all, offer separate next-available suggestions potentially beyond the selected range while preserving other filters, branch scope, and employed-first/external fallback. Five sessions/day and X minutes are examples only. Exact duration/break configuration, day-off conflicts, suggestion count/horizon, and doctor-ready notification channels remain open. The doctor's Ready for patient button triggers notifications to patient and reception.

- This is the Motmaan Center system, not a SaaS product for unrelated clinics. Start with one branch and allow future branches. Patients, doctors, schedules, and reporting are restricted by branch; cross-branch exceptions remain open.
- Backend direction: ASP.NET Core and EF Core. Flutter is the patient mobile app. The web surfaces are the public/Join us site, patient website, management dashboard, and doctor dashboard. Frontend web framework and deployment topology are undecided.
- **Current scope decision:** all currently enumerated requirements and project features belong in the first stage, including capabilities the source document labels later/separately approved. This supersedes earlier “some now, some later” answers. Preserve specific user exceptions and deferred workflows below. Doctor recruitment through Join us is the initial job type; other job types may come later.
- Replace Emdaad at production launch and migrate all its data and referenced files. Export coverage, mappings, reconciliation, and cutover validation remain open. Production is targeted after two months at production-level quality; security, user acceptance, payment/accounting reconciliation, backup restore, performance, and monitoring checks are all required. Exact thresholds, sign-off owners, and milestones remain open.
- Use Saudi Arabia's `Asia/Riyadh` timezone project-wide. Persist event instants in UTC; convert for display and perform schedules, local-date boundaries, and recurring notification calculations in `Asia/Riyadh`.
- The user wants management and doctor dashboards plus patient mobile app and responsive website. The user also wants a public website with Join us. Arabic/English and RTL/LTR apply throughout.

## Identity, roles, and access

- Wati is source-named for WhatsApp and user-identified for WhatsApp/SMS evaluation (4 October 2026). The [provider documentation review](docs/planning/17-provider-documentation-development-notes.md#whatsapp-and-sms-handling-wati) preserves documented capabilities and Saudi SMS route/API dependencies. No final SMS route/account or WhatsApp-first OTP policy is selected; retain existing access questions and backend challenge controls.

- Patient sign-in is phone number plus a one-time verification code. After sign-in, the patient may add a username or email; verify email before account recovery. A username alone is not proof of account ownership.
- Initial staff groups: manager, reception, administrator, doctor, with accountant participation now required for internal staff tasks. The exact permission matrix remains deferred.
- Access combines role assignment and granular permissions. Frontend controls should appear/disappear according to granted permissions; backend authorization and resource checks remain mandatory.
- Management controls whether a doctor is active. Only active doctors may enter the doctor dashboard. Detailed effects on existing sessions and reactivation are deferred.
- Each doctor sees records only for their assigned patients. Doctor assignment, transfer, and substitute coverage are deferred.
- Patients can view all information about their own case in their patient experience; the exact boundary for internal administrative metadata is open.
- Family direction is recorded for future discussion: father and mother may see each other's details and both may see children's details; children cannot see their parents' details. A parent need not have a patient record. No automatic permissions change at adulthood; an administrator decides. Exact access/action details are deferred.
- Doctors are expected to handle all listed clinical work—diagnoses, treatment plans, prescriptions, reports, session records, and patient tasks—within granted permissions, assigned-patient scope, and applicable qualification rules.

Doctors may issue finalized clinical reports and prescriptions directly without a separate management approval step, within their granted permissions, assigned-patient scope, and qualifications (confirmed 4 October 2026).

The owner-facing questions were revised on 4 October 2026 in the living tracker. The user removed package-stop refunds, support hours/targets, SMS provider identification, and detailed staff permissions/deactivation from this owner message; those points remain unresolved or previously deferred. The owner list now asks about package family sharing and fuller assessment-platform details. Do not reintroduce answered questions into the active queue.

## Booking, sessions, and money

- Patients book and pay from both the app and responsive patient website, including for a recommended Motmaan program.
- Online payment methods required together: mada, Apple Pay, credit/debit cards, Tabby, and Tamara. Tap Payments is the preferred candidate to evaluate; PayTabs is a comparison. Neither is a final contract/provider selection. Merchant eligibility and onboarding must be confirmed.
- Confirm an online booking only after trusted payment-provider confirmation reaches the backend. A browser/app redirect alone is not payment evidence.
- Cash is accepted only at an in-person session when the patient attends. Booking payment by bank transfer is noted for later.
- Motmaan owns operational payment/refund, wallet, package, and appointment state. Per the user's delegation, the planning recommendation is to synchronize accounting events reliably to Qoyod, which issues official accounting/e-invoicing documents. Use idempotent synchronization and retain Qoyod references/status; verify exact account and finance settings before implementation.
- For a patient cancellation before the admin-configured cutoff, the patient chooses refund to the original payment method or Motmaan wallet credit; restore package entitlement. No cutoff value is set. Late cancellation and rescheduling are deferred.
- If Motmaan or the doctor cancels, credit the Motmaan internal wallet. A patient who wants a bank payout contacts administration; that workflow is deferred.
- Administrators have full control over package offers/settings; exact fields remain to define.
- For in-person and online no-shows, retain payment or consume one package session; do not award completed-session doctor incentive. Evaluate at appointment start plus dynamically admin-configured grace, unless attendance or an active online consultation is recorded.
- Patient app countdown is to appointment start. Appointment reminder lead time is configurable by administration.
- Online sessions use Agora as the provisional source-named provider. The proposed recording flow has Agora deliver directly to a supported private center-controlled storage bucket; one-year recording retention is a source requirement. Management-selected permission controls playback. Provider/storage/region and fallback behavior remain to validate.
- Candidate storage: private Saudi-region object storage controlled by Motmaan; Google Cloud Storage in Dammam is a candidate and OCI Saudi regions an alternative.

## Doctors, recruitment, expertise, and compensation

- The center has employed doctors and external doctors on percentage arrangements. Both use the same operational behavior/access rules within permissions, assigned-patient scope, and branch scope. Prioritize employed doctors in discovery/booking; show external doctors when employed doctors are full for the requested booking. Compensation remains distinct. Search accepts start/end dates; equal dates mean one day. Evaluate fallback over the selected range and matching filters; mixed-date display remains open.
- Join us initially accepts doctor applications only. Administrators manage openings/applications; management reviews, interviews, and accepts applicants. Acceptance automatically provisions/resolves the doctor account, assigns the doctor role, and sends an SMS invitation. Candidate details/credentials and invitation mechanics require secure handling.
- Applications collect normal personal information, expertise, and degrees. Management approves expertise/degrees for public-profile use before acceptance and verifies degrees and applicant data before activation. Verification procedure remains open; exact fields/documents remain deferred.
- Each psychiatric doctor can list several areas of strength on their profile. The expertise catalog is database-backed and editable by management. Patients filter doctors by expertise, specialty, language, appointment mode, and availability. Recommended filtering: AND across different categories; OR among selected values in one category. Exact Arabic/English catalog labels remain open. See [practitioner expertise](docs/planning/13-practitioner-expertise.md).
- Compensation supports percentage-only and salary plus a monthly incentive on eligible revenue above a target. SAR 10,000 target and 20% incentive were examples, not defaults. Salary-incentive eligible revenue is completed and fully paid, net of discounts, excluding VAT and adjusted for refunds; package revenue is allocated as sessions complete. Percentage rates are changeable in the system, but percentage rate scope and calculation base are deferred.

## Tasks, notifications, support, translation, and feedback

- Patient tasks include daily/weekly self-care actions and Motmaan program recommendations. Doctors control tasks and their reminder schedule; patients report complete or missed with a reason; doctors review progress. Backend sends recurrence-based push notifications in Asia/Riyadh, and the app displays them. This supersedes earlier admin-controlled patient-task timing; appointment reminder lead time remains admin-controlled. Doctor controls include time of day, selected weekdays, start/end dates, and reminders per day. Changes apply only to future occurrences and preserve earlier completion history. Numeric limits and weekly summaries remain open.
- Internal administrative tasks are separate: reception can assign work to accountant and vice versa, with details, several assignees, Low/Normal/High/Urgent priority, optional due dates and overdue indication, comments, and attachments. Status changes automatically from actions; exact mappings and the multi-assignee completion condition remain open. Tasks close automatically once the completion condition is met, without creator approval. Assignment/comment/status/deadline/overdue events notify live inside the website and persist in an unread list, including events missed while the website was closed. Management sees full authorized-branch task details; other staff see full details of created/assigned tasks. Recipient rules and file constraints remain open. See [internal staff tasks](docs/planning/15-internal-staff-tasks.md).
- Support tickets are submitted by patients and resolved by administrators. Statuses: Open, In progress, Waiting for patient, Resolved, Closed. Push and a new-message indicator appear in the ticket. On Closed, email a satisfaction survey rated out of 10 with optional comments and one submission per ticket. Link it to the resolver; management sees all results and the patient sees their own response. Survey expiry/reclosed behavior remain open.
- Patients may optionally review a session and its doctor within exactly 48 hours from session end, rated out of 10 with written comments (recommended as optional). Management sees all reviews; the author sees their own and the session doctor sees that review. Other users do not. Mobile editing is allowed within that original 48-hour window, without extending the deadline. Web editing/retraction remains unspecified; ticket surveys remain once only. See [patient session feedback](docs/planning/14-patient-session-feedback.md).
- User-imported Arabic-language data should be translatable into English using a suitable API. Google Cloud Translation is a candidate to evaluate, not a selected provider. Preserve the Arabic source, label machine-generated translations, and verify privacy/data location/contract terms before processing health content externally. The user deferred exact formats/presentation; clinician review before clinical reliance is our recommendation, not a user decision. See [integrations and storage](docs/planning/03-integrations-and-storage.md).
- Use minimal content in push/email notifications; keep private health information out of notification previews.
- Maintain the dedicated [external provider guide](docs/planning/16-external-provider-guide.md) with each provider's role, configuration, status, setup effort, and responsible team. Do not treat candidate providers or suggested configuration roles as finalized selections/permission grants.

## Explicitly deferred or noted for later

- Doctor-level **تفضيلات** affecting display priority in patient-facing doctor search. The user asked to discuss later; configuration ownership, ranking criteria, and interaction with employed-first/external fallback are undecided. Do not invent the algorithm or change the confirmed employed-doctor rule.
- Whether booking by bank transfer is offered.
- Checkout payment slot-hold duration.
- Detailed staff permission/action matrix and how doctor deactivation affects existing sessions.
- Exact percentage-rate scope and calculation basis.
- Exact candidate form fields/documents and imported-data formats/presentation (noted for later).
- Patient late-cancellation consequences and rescheduling rules.
- Doctor-patient assignment, transfer, and substitute coverage.
- Wallet balance transfer to a patient's bank account; patient must contact administration.
- Insurance scope/integration; ask the project owner later.
- Detailed family visibility/actions and the administrator-controlled adulthood transition.

## Current work files

- [Question tracker](docs/planning/12-user-notes-and-open-questions.md) — current decisions, deferred topics, and next questions.
- [Decision register](docs/planning/06-decisions-and-open-questions.md) — authoritative concise decision and open-topic register.
- [System scope](docs/planning/01-system-scope.md)
- [Booking and finance](docs/planning/02-booking-and-finance.md)
- [Integrations and storage](docs/planning/03-integrations-and-storage.md)
- [Identity and access](docs/planning/05-identity-and-access.md)
- [Recruitment and compensation](docs/planning/08-practitioner-compensation-and-recruitment.md)
- [Support tickets](docs/planning/11-support-tickets.md)
- [Practitioner expertise](docs/planning/13-practitioner-expertise.md)
- [Patient feedback](docs/planning/14-patient-session-feedback.md)
- [Internal staff tasks](docs/planning/15-internal-staff-tasks.md)
- [External provider guide](docs/planning/16-external-provider-guide.md)
- [Flutter developer handoff](docs/handoff/flutter-developer.md)
- [Web frontend developer handoff](docs/handoff/web-frontend-developer.md)
