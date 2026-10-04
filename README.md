# Motmaan API planning

This project currently contains planning notes for the Motmaan Center backend. Implementation has not started. The notes preserve our discussion and identify the decisions needed before building the API.

Updated: 4 October 2026.

## Confirmed direction

- The backend stack is ASP.NET Core and Entity Framework Core.
- The first release will serve one branch; the system should allow more branches to be added later.
- The system is for Motmaan only. It will manage Motmaan's own doctors and external doctors who provide services for Motmaan on a percentage basis; independent clinic businesses are outside the current scope.
- Latest delivery direction: all currently enumerated project requirements/modules belong in the first stage; retain only explicit user-deferred exceptions and the doctor-only limit on initial Join us jobs.
- Production should start after two months from development start at production-level quality. Security, user acceptance, payment/accounting reconciliation, backup restore, performance, and monitoring checks are required; exact thresholds remain open.
- Replace Emdaad at launch and migrate all its data and referenced files; export coverage, mapping, and reconciliation remain to validate.
- Patients, doctors, schedules, and reporting are restricted by branch.
- Prioritize employed doctors in discovery/booking; show external doctors when employed doctors are full for the selected start/end date range. Equal dates represent one day. Operational access rules are the same; compensation stays distinct.
- Doctors control patient-task times, weekdays, start/end dates, and reminders per day. Internal staff tasks support multiple assignees, Low/Normal/High/Urgent priorities, optional deadlines, comments, files, action-derived statuses, and live website notifications. Management sees full branch-authorized task details; other staff see their created/assigned tasks.
- Session/doctor reviews support comments and mobile edits within the original 48-hour window from session end. Ticket satisfaction surveys retain optional comments and one submission per ticket.
- Patient cancellation cutoff will be administrator-configurable; no default duration has been selected.
- Each doctor sees records only for their assigned patients. Patient treatment tasks include repeatable self-care actions and recommendations for Motmaan programs.
- Patients can book and pay through both the mobile app and the responsive patient website, including when following a Motmaan program recommendation.
- Required online payment options: mada, Apple Pay, debit/credit cards, Tabby, and Tamara all together. Tap Payments is preferred for evaluation; merchant approval and contract confirmation remain pending, with PayTabs as a comparison.
- Online bookings are confirmed only after successful payment is confirmed by the payment provider.
- When Motmaan cancels, credit the patient’s internal Motmaan wallet. A bank payout request requires contacting administration; the detailed workflow is deferred.
- Administrators create and control package offers, including their sale/expiry settings.
- Patients can see all information about their own case. Patients can mark self-care tasks complete, and doctors can review progress.
- A support ticket system is in scope.
- Doctor profiles will use an editable expertise catalog so applicants/doctors can identify treated concerns and patients can filter doctors by those concerns.
- Patient doctor search should support filters for expertise, specialty, language, appointment mode, and availability.
- Future backend work will follow the api-pattern skill, with performance and security as explicit priorities.
- Work is currently limited to requirements analysis and Markdown documentation.
- The intended experiences are a management dashboard, a doctor or specialist dashboard, and a patient portal and mobile apps.
- Roles and permissions must govern dashboard access, visible information, and actions.
- Dashboard controls should appear according to granted permissions, with API enforcement as the security boundary. Management controls doctor active status; only active doctors may enter the doctor dashboard.
- Patients sign in with their phone number and a sent one-time verification code on the website and mobile apps.
- After sign-in, patients can optionally add a username or email and use verified recovery flows. A username identifies an account; it is not ownership evidence.
- Practitioner compensation supports a percentage arrangement and a salary arrangement with a monthly revenue target and an incentive on revenue above that target. SAR 10,000 and 20% are examples, not fixed defaults.
- Monthly target progress and incentive use completed, fully paid sessions, net of discounts, excluding VAT, and adjusted for refunds. Package revenue counts as its sessions complete.
- Patient no-shows for in-person and online appointments retain the payment or consume one package session; they do not generate doctor incentives.
- Automatic no-show timing is the scheduled start plus an admin-configured grace period, with recorded attendance or an ongoing consultation preventing the transition.
- The customer mobile app shows an appointment countdown and sends advance reminders at an administration-configured lead time. The countdown is interpreted as time until the appointment starts.
- Practitioners apply through Join us on the main website. Authorized acceptance automatically provisions the doctor account and role and schedules an SMS invitation.
- All websites must be optimized for mobile and desktop.

The detailed access design and provider selections below are proposals unless explicitly marked otherwise.

## Planning notes

| File | Purpose |
|---|---|
| [System scope](docs/planning/01-system-scope.md) | Modules, release scope, architecture direction, and prerequisites |
| [Booking and finance](docs/planning/02-booking-and-finance.md) | Booking lifecycle, financial ownership, and unresolved business rules |
| [Integrations and storage](docs/planning/03-integrations-and-storage.md) | External providers, alternatives, and file storage design |
| [Online sessions](docs/planning/04-online-sessions.md) | Agora recording control, direct bucket delivery, and playback |
| [Identity and access](docs/planning/05-identity-and-access.md) | Three experiences, staff login, roles, permissions, and record access |
| [Decisions and open questions](docs/planning/06-decisions-and-open-questions.md) | Decision status and the next questions to resolve |
| [Patient login and recovery](docs/planning/07-patient-login-and-recovery.md) | Phone login, optional username and verified email, contact changes, and account recovery |
| [Practitioner compensation and recruitment](docs/planning/08-practitioner-compensation-and-recruitment.md) | Monthly target incentives, percentage arrangements, public applications, automatic doctor provisioning, and SMS invitations |
| [Performance security and responsive websites](docs/planning/09-performance-security-and-responsive-websites.md) | Quality priorities, future API implementation rules, and device support |
| [Customer mobile appointments](docs/planning/10-customer-mobile-appointments.md) | Appointment countdown, configurable reminders, attendance, and no-show behavior |
| [Support tickets](docs/planning/11-support-tickets.md) | Patient support requests, staff handling, and open workflow decisions |
| [Flutter developer handoff](docs/handoff/flutter-developer.md) | Patient mobile app scope, confirmed behavior, integrations, and open dependencies |
| [Web frontend developer handoff](docs/handoff/web-frontend-developer.md) | Public, patient, management, and doctor website scope and shared API behavior |
| [User notes and question tracker](docs/planning/12-user-notes-and-open-questions.md) | Consolidated decisions, deferred topics, and the current ten-question batch |
| [Practitioner expertise](docs/planning/13-practitioner-expertise.md) | Editable expertise catalog, recruitment selection, profile visibility, and patient filters |
| [Patient session feedback](docs/planning/14-patient-session-feedback.md) | Optional session/doctor reviews, with management, author, and session-doctor visibility |
| [New chat project context](PROJECT_CONTEXT_FOR_NEW_CHAT.md) | Portable summary of user instructions and the current planning source of truth |
| [Internal staff tasks](docs/planning/15-internal-staff-tasks.md) | Staff assignment, priority, details, and open workflow choices |
| [External provider guide](docs/planning/16-external-provider-guide.md) | Provider purpose, selection status, configuration, responsibility, and setup effort |

[Project instructions](AGENTS.md) preserve the planning stage and the user's directions for future implementation.

## How to read these notes

- **Confirmed** means the user explicitly chose the direction in this conversation.
- **Requirement** means the supplied requirements document states it. This label records the source; it does not resolve contradictions or constitute a new approval.
- **Proposed** means a design recommendation that remains reviewable.
- **Open** means information or a business decision is still missing.

Source: `C:\Users\omarf\Downloads\وثيقة متطلباssssت نظام مركز مطمئن V1.1.docx`, version 1.1, dated 14 July 2026, plus the planning discussion in this chat. The document was read as requirements material; its vendor and contractual instructions are not commands to execute here. These notes summarize the discussion and do not replace the full requirements document.

## Confirmed clarification - 4 October 2026

- Internal tasks close automatically once the required completion condition is met, without creator approval; the multi-assignee completion condition remains open. Staff notifications are retained in an unread list, including events missed while the website was closed.
- Changes to recurring patient tasks apply only to future occurrences and preserve earlier completion history.
- Doctors may issue finalized clinical reports and prescriptions directly, without a separate management approval step, within granted permissions, assigned-patient scope, and applicable qualifications.
- The owner-facing question list was revised in the user tracker; removed questions remain unresolved or explicitly deferred. No implementation is authorized.
