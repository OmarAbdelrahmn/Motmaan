# System scope and backend direction

Updated: 4 October 2026. Status: planning.

The API will support the center's operational, clinical, and financial workflows across staff dashboards, the patient website, and mobile apps. Our first focus is defining booking and payment behavior, alongside patient identity and authorization, before choosing tables and endpoints.

## Branch rollout

- **Confirmed:** The first release serves one branch. The system should support adding more branches later.
- **Confirmed:** Patients, doctors, schedules, and reporting are restricted by branch. Backend resource scope enforces this restriction. Cross-branch exceptions remain open; assignment/transfer details remain deferred.

## Launch approach

- **Latest confirmed direction:** Include all currently enumerated project modules/features in the first stage. This supersedes the earlier direction to split features between stages. The user also expects production to start after two months from development start.
- **Open:** Reconcile exact source-document subfeatures and explicit exceptions before final scope lock. More job types remain later because Join us starts with doctors only. Current insurance is excluded with future NPHIES/Waseel readiness; bank-transfer bookings are prohibited, checkout holds are seven minutes and patient changes within 24 hours are blocked. Remaining family/access, assignment and financial edge cases stay open/deferred.
- **Confirmed timing/quality direction:** Replace Emdaad when Motmaan enters production, after two months of development, at production-level quality. Security, user acceptance, payment/accounting reconciliation, backup restore, performance, and monitoring checks are all required. Exact thresholds, sign-off owners, and schedule remain open.

## Organization and practitioner model

- **Confirmed:** The system serves Motmaan only; it is not currently a platform for multiple independent clinics.
- **Confirmed:** It must manage Motmaan's own doctors and external doctors who provide services for Motmaan under a percentage-based arrangement.
- **Confirmed:** Employed and external doctors use the same operational behavior and access rules within permissions, assigned-patient scope, and branch scope. Prioritize available salary-paid practitioners in patient discovery/booking; preserve external fallback when prioritized practitioners are full over the selected dates and matching filters. Compensation arrangements stay distinct. Search uses start/end dates; equal dates mean one day. Evaluate fallback over the selected date range and matching filters; mixed-date presentation remains open.

## Requirements recorded from the document

The center currently has about 10 specialists, growing to 25, about 30 appointments daily, growing to 60, 6,000 to 10,000 existing patient records, and four shared rooms. The first release includes management web functionality, a patient booking website, and iOS and Android apps.

| Module | Responsibilities |
|---|---|
| Identity and access | Patient phone OTP, optional username and verified email recovery, staff authentication, configurable roles, action permissions, portal access |
| Patients and families | Identity documents, duplicate prevention, family relationships, independent medical histories, consent, configurable fields |
| Catalog and specialists | Departments, services, specialist-specific pricing, qualifications, licenses, public profiles, offers |
| Doctor expertise | Editable catalog of concerns/areas treated, linked to doctor profiles and used in patient search filters; details in [practitioner expertise](13-practitioner-expertise.md) |
| Practitioner recruitment | Public Join us applications, management review, contact tracking, and acceptance with automatic doctor account/role provisioning and SMS invitation |
| Scheduling | Center and specialist working hours, Ramadan overrides, leave, breaks, closures, rooms, availability |
| Appointments | Holds, booking, payment deadlines, attendance, completion, cancellations, rescheduling, follow-ups, waiting lists |
| Packages | Purchase, session entitlements, reservations, consumption, expiry, transfers, refunds |
| Finance | Payments, invoices, receipts, refunds, wallet entries, staff cashboxes, practitioner salary and percentage arrangements, commissions, discounts, loyalty |
| Clinical records | Session records, diagnoses, medication catalog, prescriptions, attachments, approved reports |
| Treatment follow-up | Plans, recurring task occurrences, completion, missed-task reasons, reminders, weekly summaries |
| Support tickets | Patient support requests, management queue, responses, status tracking, and notifications; detailed workflow is open |
| Patient feedback | Optional session/doctor review within 48 hours from session end, with comments; visible to management, author, and session doctor. Closed-ticket satisfaction rating with optional comments, once per ticket, tied to resolver; see [patient feedback](14-patient-session-feedback.md) |
| Assessments | Specialist requests, payment, SSO, completion, result import, revenue attribution |
| Remote sessions | Participant authorization, Agora access, recording, restricted playback, retention |
| Operations | Notifications, internal staff tasks (reception/accountant assignment, priority, details), audit history, settings, reports, initial setup progress |
| Public website | Center identity and content, practitioner/service presentation, and Join us entry; branding interpretation is recorded below |

## User additions after the source document

- **Confirmed:** Future implementation must use the api-pattern skill. Performance and security are explicit priorities.
- **Confirmed:** Practitioner compensation supports a percentage arrangement and a salary arrangement with an incentive on monthly eligible revenue above a configurable target. Monthly target/incentive revenue uses completed, fully paid sessions after discounts, excluding VAT and adjusted for refunds. SAR 10,000 and 20% are examples; allocation and period-correction details remain open.
- **Confirmed:** Candidates submit information through Join us on the main website. Management can review/contact them, and authorized acceptance automatically provisions the doctor account, assigns the doctor role, and schedules an SMS invitation. Secure first-access and retry details are proposed in the recruitment note.
- **Confirmed:** Every website must work well on mobile and desktop, including public pages and both staff dashboards.
- **Confirmed:** Patient treatment tasks have two types: repeatable self-care actions and Motmaan program recommendations. Doctors control tasks and their reminder schedule; patients report completion or a missed reason. The backend sends push notifications according to the doctor-defined schedule and recurrence. Doctor controls include reminder time, weekdays, start/end dates, and reminders per day; Changes to recurring patient tasks apply only to future occurrences and preserve earlier completion history. Weekly summaries go to both patient and assigned doctor; numeric task limits and summary content, timing and channels remain open.
- **Confirmed:** Patients can book and pay through both the mobile app and the responsive patient website, including from a recommended Motmaan program.
- **Confirmed payment options:** mada, Apple Pay, credit/debit cards, Tabby, and Tamara are required together. Tap Payments is preferred for evaluation and PayTabs is a comparison; merchant approval and final provider selection remain open.
- **Confirmed booking/payment rule:** An online booking becomes confirmed only after the provider confirms successful payment. The API must rely on trusted provider confirmation rather than a client-only checkout return.
- **Confirmed cancellation consequence for Motmaan/doctor cancellations:** Credit the patient in the Motmaan internal wallet. The patient requests bank payout inside the wallet for service-refund-origin funds only; a system administrator or accountant approves. Coupon credit is not withdrawable; execution/verification details remain open.
- **Confirmed package direction:** Administrators create package offers and control their availability, end/expiry, and package settings. Exact fields and limits remain to be specified.
- **Confirmed patient case visibility:** Patients can view all information about their own case in the patient experience. Exact presentation and any internal-only administrative metadata remain open.
- **Confirmed treatment-task interaction:** Patients can mark self-care tasks complete or missed and provide a reason; support recurrence-based push notifications and weekly progress summaries. Exact send time and summary behavior remain open.
- **Confirmed:** Patients submit support tickets; administrators resolve them using Open, In progress, Waiting for patient, Resolved, and Closed statuses. Send push updates and show a new-message indicator. On Closed, email a survey rated out of 10 with optional comments and one submission per ticket, linked to the resolver. Management sees all results; patients see their own response.
- **Confirmed:** Initial staff role groups are manager, reception, administrator, and doctor; accountant participation is now required for internal staff tasks. The detailed permission matrix remains deferred.
- **Confirmed:** Access is role- and permission-based. The frontend should show or hide actions according to granted permissions, while the backend must enforce them regardless of interface state.
- **Confirmed:** Management controls whether a doctor is active. Only active doctors can log in to the doctor dashboard; deactivation effects on existing sessions and reactivation flow remain open.
- **Confirmed doctor clinical scope:** Doctors are expected to handle all listed clinical work (diagnoses, treatment plans, prescriptions, reports, session records, and tasks), within their permissions, assigned-patient scope, and applicable qualification rules.
- **Confirmed doctor search filters:** Expertise/concern, specialty, language, appointment mode, and availability.
- **Confirmed recruitment information:** Applications capture usual personal information, expertise, and degrees. Management verifies degrees and applicant data before activation. Baseline fields/documents follow the reviewed existing website, plus therapeutic expertise multi-select; see [recruitment reference](19-recruitment-current-website-reference.md). Verification, upload constraints and additional evidence remain open.
- **Confirmed compensation configuration:** Percentage rates are changeable through the system. Rates vary by practitioner and use net revenue after tax/discounts. Further deductions, optional service-specific rates, edit ownership and refund reversals remain open.
- **Confirmed timezone:** Use Saudi Arabia time (`Asia/Riyadh`) throughout the project. Persist event timestamps as UTC instants and convert for display, date boundaries, schedules, and recurrence calculations using the named zone.
- **Confirmed translation need:** When users import Arabic-language data, support translation into English through a suitable translation API. Google Cloud Translation is a candidate to evaluate, not a finalized vendor. Preserve the Arabic original and treat machine translations as such; confirm privacy, residency, cost, and clinical review requirements before handling health records externally.
- **Confirmed post-session feedback:** Patients may optionally review the session and doctor within 48 hours from session end, rated out of 10 with written comments (recommended as optional). Management sees all reviews; the author and session doctor see that review; other users do not. Mobile review edits are allowed within the original 48-hour window; web editing remains unspecified.
- **Confirmed ticket satisfaction:** On closure, email a survey rated out of 10 with optional comments and one submission per ticket. Associate the response with the resolver; management sees all results and the patient sees their own.
- **Confirmed:** Public Join us starts with doctor applications; administrators control openings/applications. Other job types may be added later.
- **Confirmed cash scope:** Cash is accepted only for in-person sessions when the patient attends; no general cash-at-booking flow is approved.
- **Confirmed user direction superseding broader source wording:** Each doctor can view only records for their own assigned patients. The source document's wider specialist access must not be used as the default for this project.
- **Confirmed:** A patient no-show retains the paid fee or consumes one package session for both in-person and online appointments. Automatic assignment uses scheduled start plus an admin-configured grace period, with attendance/active-consultation safeguards; correction rules remain open.
- **Confirmed mobile direction:** Show a countdown to an in-person appointment and deliver advance reminders using an administration-configured lead time. The countdown interpretation and related mobile behavior are documented in [customer mobile appointments](10-customer-mobile-appointments.md).
- **Interpretation:** The user's reference to clinic identity means the center's name, logo, and branding on public pages; detailed brand assets are not yet supplied.

Public employment applications are a current user addition. They are distinct from the later external-practitioner marketplace in the source document; do not defer recruitment simply because that marketplace is later work.

## Cross-scope clarifications — 4 October 2026

- **Confirmed clinical reports:** When a finalized clinical report needs correction, the authorized doctor edits that report directly; a separate revised-report issuance workflow is not required. Keep granted permissions, assigned-patient/branch scope, and qualifications in force. This answer concerns clinical reports, not accounting invoices, prescriptions, or unrestricted deletion. Proposed: preserve protected edit history/audit without making the doctor create another report; exact audit and patient-update presentation remain open.
- **Confirmed management dashboard:** Include all four figures offered in the question: revenue, bookings, unpaid amounts, and patient satisfaction. Definitions, period filters, layout/order, and drill-downs remain open; "all" does not select every unspecified metric. Enforce authorized branch/reporting scope.
- **Confirmed weekly treatment summaries:** Both the patient and their assigned doctor receive the weekly progress summary; content, timing, and channels remain open.
- **Latest clarification:** Current packages repeat sessions for a chosen practitioner, with family usage and practitioner-change/difference payment; future treatment pathways are deferred. The existing assessment platform will be integrated, with [programmer questions](18-assessment-platform-integration-questions.md) pending. Multi-assignee staff-task completion and Emdaad export discussion remain deferred; full migration at launch remains in scope.

## Release boundaries

The user's latest direction is to include all currently enumerated project requirements/features in the first stage, including features the source document labels later or separately approved. This supersedes earlier staged-scope answers and source-document phasing. Preserve explicit user exceptions: Join us starts with doctor jobs only, and deferred workflows remain deferred. Confirm detailed source-only subfeatures before implementation if they conflict with a later specific user decision.

- **Requirement:** Core booking, clinical records, finance, packages, remote sessions, treatment follow-up, provider integrations, and migration belong to the initial scope.
- **Historical source phasing:** The source describes insurance classifications, coverage, prior approvals and claims structures, with NPHIES/Waseel connectivity separately approved. The later specific user direction is no current insurance and future integration readiness; do not build live insurance operations from the broad first-stage statement.
- **Historical source phasing, superseded by broad first-stage direction:** Wasfaty, Nafath, the external-doctor marketplace and training courses were described as later or separately approved. They must remain visible in the first-stage scope inventory unless a specific user exception applies. Their exact use cases, access and acceptance criteria are incomplete. The marketplace must be reconciled with the confirmed Motmaan-only organization boundary; do not infer independent clinic businesses. Internal prescription PDFs remain in scope.
- **Historical source phasing, superseded:** Section 20 placed dashboards/analytics in a second phase. Current first-stage direction includes them; the four named management figures are confirmed, while the remaining detailed reports still need definitions.
- **Open:** Loyalty is described as a configurable unit disabled by default, while later prioritization places it last. Disabled functionality is not automatically excluded scope.
- **Confirmed addition:** Internal administrative tasks include reception/accountant assignments to several staff, Low/Normal/High/Urgent priority, details, optional due dates/overdue indicators, comments, and files. Status derives from actions; event notifications appear live in the website. Management sees full branch-authorized details; staff see full created/assigned details. Exact mappings and multi-assignee completion remain open. Separate from patient tasks; see [internal staff tasks](15-internal-staff-tasks.md).

The source document specifies a two-to-three-month overall delivery target and prioritizes mobile apps, Qoyod, assessment integration, then analytics and loyalty when time is constrained. The user separately directed that production starts after two months from development start. Neither statement is a validated delivery estimate; detailed milestones and acceptance gates remain to be planned.

## Proposed architecture

Use a modular monolith: one backend with clear feature ownership and one initial relational database. The database engine, .NET version, deployment topology, and job platform are still open.

Future implementation follows the api-pattern skill at `C:/Users/omarf/.codex/skills/api-pattern/SKILL.md`. See [performance security and responsive websites](09-performance-security-and-responsive-websites.md) for the user's quality priorities.

- Keep controllers focused on HTTP inputs and outputs.
- Put workflows in application services or use cases, with explicit Result and Error outcomes.
- Use EF Core as the default unit of work. The owning workflow controls the commit.
- Define module contracts for cross-module writes and avoid circular service dependencies.
- Use transactions and concurrency protection for slot reservation, money, and entitlements.
- Use durable jobs and an outbox where reliable delivery to external providers matters.
- Propagate cancellation, bound collection queries, and provide predictable errors.
- Use `Asia/Riyadh` as the single project time zone for user-facing times, working schedules, policy boundaries, reports, and recurring jobs. Persist event instants in UTC; perform local calendar/recurrence logic in `Asia/Riyadh` and convert at boundaries.
- Keep integrations behind explicit adapters so provider changes are localized. Adapters reduce backend coupling; replacing a video SDK may still require client changes.
- Design for external practitioners with distinct practitioner identities and permissions inside Motmaan. The confirmed product is for Motmaan only, not multiple independent clinic organizations.

## Operational capabilities

Plan private object storage, strong staff authentication, protected audit logs, versioned policy acceptance, backups with tested restoration, and monitoring of API and job failures. Define measurable availability, response-time, recovery-time, and recovery-point targets rather than leaving them as "fast" or "high availability".

**Confirmed:** Replace Emdaad at production launch and migrate all its data and referenced files. Proposed migration checks include export samples, mapping, duplicate review, financial reconciliation, trial import, and cutover validation. Actual export coverage and file retrieval remain to validate.

**Confirmed latest owner clarification:** Seed/import existing data before the system starts operating. This is a launch prerequisite; exact seeded account-to-patient links and first-access identity matching remain open. Reception assigns rooms per appointment with suggestions of available rooms. Online recording is mandatory for safety and performance review. Additional staff/doctor verification can be enabled or disabled and uses SMS when enabled. See the relevant booking, recording and identity notes for remaining details; implementation is not authorized.

## Before implementation

Prepare the confirmed scope, workflow and state diagrams, permission matrix, data ownership model, API contracts, and acceptance scenarios. Obtain provider sandbox access and migration samples early. Figma and operational review requirements remain part of the source project scope; this planning task does not execute them.

**Review follow-up R01/R10/R14, 4 October 2026:** Build a source-to-feature acceptance inventory before claiming all source requirements are covered. Explicitly include thinly specified catalog/pricing administration, Ramadan/overnight schedules, waitlist offers (distinct from the unselected waiting-room queue), free follow-ups, cashboxes, discounts/loyalty, clinical forms/catalogs, reports/exports, training and the source marketplace capabilities. Preserve existing exclusions/deferrals and the Motmaan-only boundary. Clinical form definitions and a dedicated patient-task behavior specification remain missing. See the [readiness review](20-development-readiness-review.md); these are planning gaps, not new approved features or a change to the two-month target.

Reference: [Microsoft web application architecture guidance](https://learn.microsoft.com/en-us/dotnet/architecture/modern-web-apps-azure/common-web-application-architectures).

## Confirmed clarification - 4 October 2026

- Doctors may issue finalized clinical reports and prescriptions directly, without a separate management approval step, within granted permissions, assigned-patient scope, and applicable qualifications.

## Latest scope boundaries — 4 October 2026

- No current insurance; prepare for future NPHIES/Waseel. No current treatment pathways mixing services/practitioners; repeated-session packages are practitioner-specific with the confirmed transfer/family rules.
- Checkout holds last seven minutes with countdown/expiry message; booking by bank transfer is not allowed. Patient cancellation/modification is blocked with less than 24 hours remaining.
- Refund-origin wallet withdrawals are requested inside the wallet, approved by system administrator/accountant, and exclude coupons. Bank execution remains open.
- Parents add members; own clinical/session access, payer invoices and self-exit with family-head notice/independent patient capabilities are confirmed. Minor/guardian eligibility, cross-member access and post-exit bookings/entitlements remain open.
