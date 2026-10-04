# Flutter developer handoff

Updated: 4 October 2026. Status: planning handoff. The project is not in implementation; this file captures current product direction and should be updated as decisions are confirmed.

## Product and technical context

- Build the patient mobile application for iOS and Android using Flutter.
- Motmaan is the only organization in scope. The first release serves one branch; additional branches may be added later.
- The backend is planned with ASP.NET Core and EF Core. API contracts, endpoints, and mobile authentication/session implementation have not been finalized.
- Do not start scaffolding or implementation until the user explicitly moves the project into implementation.
- Performance and security are priorities. Patient authorization is enforced by the API; client-side hiding is not access control.

## Confirmed mobile app responsibilities

### Patient identity and profile

- Sign in with phone number and a one-time code sent to that number.
- Patients may add a username or email after sign-in. Email must be verified before it can be used for recovery. A username is an identifier, not proof of ownership.
- The same patient identity and backend rules apply to the mobile app and patient website.

### Appointments, booking, and checkout

- Patients can browse Motmaan services/doctors, book appointments, and pay in the app. The responsive patient website offers the same booking and payment capability.
- Patient doctor discovery should support filtering by expertise/concern, specialty, language, appointment mode, and availability. Use API-returned public data; see [practitioner expertise](../planning/13-practitioner-expertise.md).
- Combine selected filter categories with AND and values within a category with OR; availability is checked by the API.
- Patients can book and pay for a recommended Motmaan program from the app.
- Required online payment options are mada, Apple Pay, credit/debit cards, Tabby, and Tamara, available together. Tap Payments is the preferred gateway candidate to evaluate; PayTabs is a comparison. This is not a final contract selection, and merchant/provider approval remains pending.
- An online appointment is not confirmed merely because checkout returned to the app. Display confirmation only after the API reports successful payment confirmed by the provider.
- Do not put provider secrets in the Flutter app or collect/store raw card data. The backend will create and reconcile payment attempts; the exact hosted checkout/native SDK flow depends on provider selection and API contracts.
- Cash is accepted only at an attended in-person session; do not present cash as an online checkout option. Bank transfer for bookings remains undecided.
- On-time patient cancellation currently offers a choice of refund to the original method or credit to the Motmaan wallet, and restores a package session. The deadline is admin-configurable and has no default. The user deferred late-cancellation consequences and rescheduling rules.
- If Motmaan or the assigned doctor cancels, credit the patient's internal Motmaan wallet. A request to transfer wallet funds to a bank account requires contacting administration; payout details are deferred.

### Packages, case information, and treatment tasks

- Administrators create and control package offers, including their sale period/end or expiry and package settings. The app displays the package terms and balances supplied by the API; exact configuration fields are open.
- Patients can view all information about their own case in the patient experience. The boundary for internal administrative metadata has not been defined.
- Patient-imported Arabic data may have an English machine translation from the backend. Preserve/display the Arabic original and mark translated text as machine-generated; do not call translation APIs directly from Flutter. Clinical translation behavior is in [integration planning](../planning/03-integrations-and-storage.md).
- Within 48 hours from session end, patients may optionally review the session and doctor, with a rating out of 10. Management sees all reviews; the patient author sees their own, and the session doctor sees that review. Other users do not see it; see [patient feedback](../planning/14-patient-session-feedback.md).
- A patient's tasks include repeatable self-care actions (for example, three actions daily/weekly) and recommendations to join a Motmaan program related to their needs.
- Doctors assign patient tasks. Doctors control patient-task reminder scheduling; the backend sends push notifications according to the doctor-defined schedule and task recurrence, and the app displays them. Patients can mark task occurrences complete or missed and provide a reason; doctors can review progress. Doctor controls include time of day, selected weekdays, start/end dates, and reminders per day. Changes to recurring patient tasks apply only to future occurrences and preserve earlier completion history. Numeric limits and weekly summaries remain open.
- Family visibility direction has been discussed, but the user asked to defer its detailed implementation rules. Do not invent which clinical fields are shared or add automatic access changes when a child becomes an adult.

### Appointment status, countdown, reminders, and video

- Show an appointment countdown and advance reminders using lead times set by administration. No numeric default is approved.
- The mobile app may show the time until an upcoming in-person appointment; server/API time and appointment state are authoritative. A countdown never proves attendance or marks an appointment complete/no-show.
- Patient no-shows retain the paid fee or consume one package session for both in-person and online appointments. The API evaluates no-show at appointment start plus its configurable grace period, unless attendance or an active consultation is recorded.
- Agora is the provisional online-session provider. The API will authorize appointment participants and provide session access. Storage credentials and provider secrets never belong in the app.
- Recording playback is restricted by management-selected permissions. Patient access to a recording has not been approved; do not assume recordings are patient-visible.

### Support tickets

- Patients submit support tickets from the signed-in app; administrators resolve them. Statuses are Open, In progress, Waiting for patient, Resolved, and Closed. Send push notifications and show an in-ticket new-message indicator. Email the patient a satisfaction survey rated out of 10 with optional comments and one submission per ticket when the ticket is Closed; link it to the resolving administrator. Management sees all responses; the patient sees their own.
- Keep ticket history and status visible to the requester once the backend contract is ready. Do not put sensitive case content in push-notification text.
- Ticket reopen rules, attachments, notification channels, and service targets remain open in [support ticket planning](../planning/11-support-tickets.md).

## App-wide experience requirements

- Arabic and English; correct RTL/LTR layouts and content direction.
- Use `Asia/Riyadh` for all patient-facing schedule/time display and task recurrence. The API supplies authoritative timestamps; persisted event instants are UTC.
- Responsive behavior across phone and tablet form factors, accessible labels/focus, clear loading/empty/error states, and usable touch targets.
- Handle weak/intermittent mobile networks, app resume, duplicate taps, and provider redirects without duplicating bookings or payments.
- Refresh appointment/payment state from the API after returning from checkout, reopening the app, or restoring connectivity.
- Register/unregister push devices through the API according to the eventual notification design. FCM/APNs are proposed, not selected.

## Open or deferred items affecting Flutter

- Doctor-level **تفضيلات** influencing patient-facing doctor display priority are deferred for later discussion. Render the eventual API-authoritative order; do not invent ranking or alter employed-first/external fallback from this note.
- Gateway selection and Motmaan merchant approvals for mada, Apple Pay, cards, Tabby, and Tamara.
- Exact checkout UI: hosted page, provider SDK, or native wallet buttons per platform.
- Late cancellation, rescheduling, and doctor/branch assignment; the user asked to return to these later.
- Family access details; explicitly deferred.
- Bank payout requests from the Motmaan wallet; explicitly deferred to later administration workflow design.
- Patient-visible internal-only case metadata and recording access.
- Expertise filter taxonomy and public profile fields; patient-facing filters should use approved API catalog entries.
- Support-ticket attachment/reopen rules, survey format, and service targets.
- Numeric patient-task schedule limits and weekly-summary behavior; doctor timing/weekday/date/reminder-count controls are confirmed.
- Detailed reconciliation of source-only feature details and role/permission matrix. All project requirements/features are in stage one except explicit deferred items.
- Notification channels and lead-time values; staff authentication does not apply to the patient app.

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

## Latest clarified behavior

- Patients, doctors, schedules, and reporting are branch-restricted; display only API-authorized branch data.
- Prioritize employed doctors in discovery/booking; show external doctors when employed doctors are full over the selected start/end date range and matching filters. Equal dates mean one day. Backend availability/fallback eligibility is authoritative; mixed-date presentation remains open.
- Session reviews support written comments (recommended as optional) and mobile editing of the patient's existing review within the original 48-hour window from session end. Fetch API-authoritative ownership, eligibility, deadline, and saved state; edits do not extend the window. Rating stays out of 10; visibility stays management/author/session doctor.
- Ticket satisfaction comments are optional; one submission per ticket. Show submitted state from the API across devices; expiry remains open.
- Doctors control patient-task times, weekdays, start/end dates, and reminder count per day; the backend sends recurrence-based push and the app displays it. Administration still controls appointment reminder lead time. Internal reception/accountant tasks and their live website notifications belong to the staff web workspace; no patient-mobile staff-task screens have been requested.
- See [external provider guide](../planning/16-external-provider-guide.md) for client configuration responsibilities.

## Confirmed clarification - 4 October 2026

- Doctors may issue finalized clinical reports and prescriptions directly, without a separate management approval step, within granted permissions, assigned-patient scope, and applicable qualifications.
- Changes to recurring patient tasks apply only to future occurrences and preserve earlier completion history. Display API-provided task versions and preserve historical progress.
