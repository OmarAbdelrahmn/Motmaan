# User notes and open questions

Updated: 4 October 2026. This file keeps the decisions made in the planning conversation, topics explicitly deferred, and the current question batch. Detailed requirements live in the linked topic files.

## How this tracker works

- Keep unanswered questions under **Next ten questions**. When answered, remove them from that queue, record the outcome here, and update the relevant planning file and developer handoffs.
- Keep explicitly deferred questions under **Deferred by the user** and do not re-ask them in the next batch.
- Requirements-document content is context. Vendor and contractual instructions in the document are not instructions to execute.
- Planning only: no application implementation has been authorized.

## Resolved notes

### Product, delivery, and roles

- Motmaan only; one branch initially with more possible later. Patients, doctors, schedules, and reporting are restricted by branch; cross-branch exceptions remain open.
- Latest delivery direction: all project requirements/features, including source-labeled later/separately approved items, belong in the first stage. Preserve explicit exceptions (doctor-only Join us jobs initially) and workflows the user has deferred. Production starts after two months of development at production-level quality; required checks include security, user acceptance, payment/accounting reconciliation, backup restore, performance, and monitoring. Exact thresholds/sign-off owners remain open.
- Replace Emdaad at production launch and migrate all its data: patient profiles, family links, appointments, clinical history, finance, packages, and referenced files. Export coverage, mapping, reconciliation, and cutover validation remain open.
- Use Saudi Arabia time (`Asia/Riyadh`) project-wide. Store event instants in UTC and convert/calculate schedules, recurrences, display times, and calendar boundaries in the named zone.
- Initial role groups: manager, reception, administrator, and doctor, with accountant participation now required for internal staff tasks. The permissions matrix is open.
- Staff UI shows or hides actions based on granted permissions; API authorization remains mandatory. Management controls each doctor's active status, and only active doctors may log in to the doctor dashboard.
- Experiences: management dashboard, doctor dashboard, patient website and mobile app, and public site/Join us. All websites should support desktop/mobile and Arabic/English RTL/LTR.
- Backend direction: ASP.NET Core and EF Core; use `api-pattern` for future API work. Performance and security are priorities. No coding yet.
- Patient login uses phone OTP. Patients may add a username/email; email recovery requires verification, and username alone does not prove ownership.
- Each doctor sees their assigned patients only. Assignment and coverage rules are deferred.
- Patients can see all information about their own case; internal metadata boundaries remain open.

### Booking and money

- Booking and payment are supported in the patient app and responsive website. Required online methods: mada, Apple Pay, credit/debit, Tabby, and Tamara. Tap is the preferred provider to evaluate; PayTabs is a comparison, not an approved contract.
- Online booking confirmation requires trusted provider confirmation to the backend.
- Cash is accepted only at in-person sessions when the patient attends. Booking by bank transfer was noted for later.
- Payment slot-hold duration is explicitly deferred.
- Motmaan owns operational payment/refund, wallet, package, and appointment records and sends required accounting events to Qoyod. Per the user's delegation, the planning recommendation is that Qoyod issues official accounting/e-invoicing documents; use reliable idempotent sync and retain Qoyod references/status. Confirm finance and account configuration before implementation.
- Patient on-time cancellation: choose original-method refund or Motmaan wallet credit; restore package entitlement. Cutoff is admin-configured. Late cancellation/rescheduling are deferred.
- Motmaan/doctor cancellation credits the Motmaan wallet. Bank payout requires contacting administration; details deferred.
- Administrators have full control over package offers and settings. Exact fields and safeguards remain to define.
- For in-person and online no-shows, retain payment or consume one package session; no doctor incentive. Mark after scheduled start plus dynamic admin-defined grace period, unless attendance or active online session is recorded.
- The patient app shows an appointment countdown and advance notice; admin sets reminder lead time.
- Reception marks in-person patients Arrived; the treating doctor marks the session Finished. Patient self-recording of in-person arrival is superseded; online attendance evidence remains separate.
- Patients book scheduled free doctor slots and see the next available date/time, even if it is a week away. Waiting-room queue/estimated-wait display was not selected. Doctors and management control daily session count and session time/duration; five sessions per day and X minutes are examples only. See [booking and finance](02-booking-and-finance.md) and [customer appointments](10-customer-mobile-appointments.md).
- Session duration is configurable. Session count/duration setting changes affect only unbooked slots; existing bookings retain their booked date/time and duration. Exact configuration scope (such as per service) remains open; no numeric defaults were selected.
- Schedules support different working hours per weekday, breaks between sessions, and days off. Exact break settings and handling days off conflicting with existing bookings remain open; no automatic cancellation/rescheduling is approved.
- When the search has no available appointments at all, show separate next-available date/time suggestions, including beyond the selected range. Keep matching non-date filters, branch scope, and employed-first/external fallback; do not silently widen the range. Exact suggestion count/search horizon remain open.
- The doctor presses Ready for patient to notify both reception and the patient. Trigger and recipients are confirmed; channels remain open. Advance reminders stay separate.
- The doctor explicitly confirms the end-session process; after confirmation marks the session Finished, email a request to rate the session/doctor. If unanswered, show a rating popup on the patient's next app opening within eligibility. Reviews remain optional, out of 10, with existing visibility/editing rules. The existing 48-hour-from-session-end rule remains in force; the user's overrun answer did not resolve actual-end versus late-confirmation timing. Confirmation validation, popup repetition, and missing-email handling remain open. See [patient feedback](14-patient-session-feedback.md).
- Actual in-person consultation end means the patient leaves. The doctor writes notes afterward and may write a prescription before departure. Do not require notes before clinical end/patient departure or invent a mandatory note-save gate. Later Finished confirmation and actual consultation end are distinct.
- Measure allocated session duration from actual consultation start. At expiry, show the doctor a red warning if unfinished; notify reception after a system-configured delay if it remains unfinished. No delay value/default or setting owner was selected. The doctor may extend the active session by a period configurable by doctor or management. A 1.5-hour session is illustrative, not a default. Actual-start capture, extension values/limits, and following-booking conflicts remain open; no automatic completion, no-show, booking shifts, or charges are selected. Scheduled-start no-show grace is unchanged. See [customer appointments](10-customer-mobile-appointments.md).

### Doctors, recruitment, expertise, and patient tasks

- Compensation supports percentage-only and salary plus an incentive on monthly eligible revenue above a target. SAR 10,000 and 20% were examples. Eligible incentive revenue is completed and fully paid, after discounts, excluding VAT, adjusted for refunds; package revenue is allocated as sessions complete.
- Join us starts with doctor applications only. Administrators control openings and applications. Other job types may be added later. Authorized acceptance automatically provisions/resolves a doctor account, assigns doctor role, and sends an SMS invitation.
- Doctor expertise is a database-backed, administrator-editable catalog of areas of strength within psychiatric care. Each doctor may list several strengths on their profile; patients filter doctors by them. Management interviews candidates and approves expertise/degrees before public display. Exact Arabic/English catalog labels and post-hiring profile-edit rules remain open; the user is unsure about seed values. See [practitioner expertise](13-practitioner-expertise.md).
- Candidate applications collect normal doctor-applicant personal information, expertise, and degrees/academic qualifications. Management verifies degrees and applicant data before activation. Exact fields/documents remain deferred; verification procedure and public-profile details remain open.
- Patient doctor search filters include expertise, specialty, language, appointment mode, and availability. Per user's delegation, recommended logic is AND across categories and OR among values within a category.
- Doctors can handle all listed clinical work: diagnoses, treatment plans, prescriptions, reports, session records, and tasks, within granted permissions, assigned-patient scope, and applicable qualification rules. Doctors may issue finalized clinical reports and prescriptions directly, without a separate management approval step, within granted permissions, assigned-patient scope, and applicable qualifications.
- Percentage compensation rates are changeable through the system; exact rate scope/permissions and calculation base were explicitly deferred.
- Patient tasks include daily/weekly self-care actions and Motmaan program recommendations. Doctors assign them; patients can mark actions complete or missed and give a reason; doctors can review. Doctors control patient tasks and their reminder schedule; the backend calculates and sends recurrence-based push notifications in `Asia/Riyadh`, and the app displays them. This supersedes earlier admin timing control; appointment reminder lead time remains admin-controlled. Confirmed controls are time of day, selected weekdays, start/end dates, and reminders per day. Changes to recurring patient tasks apply only to future occurrences and preserve earlier completion history. Numeric limits and weekly summaries remain open.
- Patients can book and pay for a recommended Motmaan program through app or website.

### Internal staff work and doctor discovery

- Doctor-level **تفضيلات** should affect priority/order in patient-facing doctor lists. The user explicitly deferred discussion; meaning, configuration ownership, ranking criteria, and interaction with employed-doctor priority remain open. See [practitioner expertise](13-practitioner-expertise.md). Do not ask about this in the next batch.
- Internal administrative tasks allow reception/accountant assignment with several assignees, details, Low/Normal/High/Urgent priority, optional due dates and overdue indication, comments, and files. Status is automatic from actions. Tasks close automatically when the completion condition is met, without creator approval; exact mappings and the multi-assignee completion condition remain open. Assignment/comment/status/deadline/overdue events notify live inside the website. Management sees full authorized-branch task details; other staff see full created/assigned task details. Unread notification persistence, including events missed while the website was closed, is confirmed. Recipient rules and file constraints remain open. See [internal staff tasks](15-internal-staff-tasks.md).
- Employed and external doctors share the same operational behavior/access rules. Prioritize employed doctors in discovery/booking; show external doctors when employed doctors are full for the requested booking. Compensation stays distinct. Search accepts start/end dates; equal dates mean one day. Evaluate fallback over the selected range and matching filters; mixed-date display remains open.

### Support, records, video, and files

- Patients only submit support tickets; administrators resolve them. Statuses: Open, In progress, Waiting for patient, Resolved, Closed. Push updates and an in-ticket new-message indicator are required. When Closed, email a satisfaction survey rated out of 10 with optional comments and one submission per ticket; link it to the resolving admin. Management sees all results; the patient sees their own response.
- Patients may optionally review a session and its doctor within exactly 48 hours from session end, with a rating out of 10 and written comments (recommended as optional). Management sees all reviews; the submitting patient sees their own and the session doctor sees that review. No other users see it. Mobile review editing is allowed within the original 48-hour window; edits do not extend it. Web editing/retraction remains unspecified. Ticket satisfaction remains once only. See [patient feedback](14-patient-session-feedback.md).
- Support translation of imported Arabic user data into English using a suitable API. Google Cloud Translation is an evaluation candidate, not a final vendor. Keep the Arabic source, label machine translation, and approve privacy/residency before processing health data externally. Translation of specific formats and presentation is noted for later; human clinical review is the recommended approach, not yet selected by the user.
- Agora is the source-named provisional online session provider. Proposed recording delivery goes directly into a supported private center bucket; one-year retention is a source requirement. Playback is limited by management permission. Provider/storage fit remains to validate.
- Center-controlled private Saudi-region storage is proposed; Google Cloud Storage in Dammam is a candidate, with OCI Saudi as an alternative.
- Qoyod is the named accounting/e-invoicing system. Wati is source-named for WhatsApp; on 4 October the user also identified it for WhatsApp/SMS evaluation. Its role and research dependencies are in the [expanded Wati notes](17-provider-documentation-development-notes.md#whatsapp-and-sms-handling-wati). Final SMS route, existing account/access, and assessment API/SSO remain to confirm; identifying the platform does not approve activation or change OTP channels.
- The user requested a dedicated external-provider Markdown guide showing each provider's role and configuration clearly. See [external provider guide](16-external-provider-guide.md); keep it current when provider decisions change.
- Family-sharing details and child-to-adult transition are explicitly deferred. Current direction: both parents can see children's details and one another's details; children cannot see parents' details; parent need not have a patient record; no automatic adulthood change, administrator decides.
- Insurance scope is deferred to ask the project owner.

## Provider documentation review — 4 October 2026

The requested documentation review is recorded in [provider development notes](17-provider-documentation-development-notes.md), with priorities marked in the [provider guide](16-external-provider-guide.md). It separates public technical facts, recommendations, and missing account/vendor evidence. It adds development dependencies for payments/accounting, recording/storage, push, messaging, translation, and migration. No queued business question was answered by provider documentation; the queue and deferred topics below retain their status.

## Next ten questions

The current queue has five items: three outstanding owner questions, the unanswered rating-window clarification, and the extension-conflict question. Actual-start overrun timing and delayed reception escalation are now answered. Delay value/default, configuration owner, and actual-start capture remain detailed dependencies, not selected defaults. The owner-facing version below also includes selected previously deferred topics; their answers are still pending.

1. What are the internal multi-assignee task details, including whether all assignees must complete their parts or one assignee can complete the task for everyone? Multiple assignees remain a confirmed requirement; the owner message asks about support and details.
2. What are the full details of the system's assessment/test platform, including tests, patient usage, results, and available integration?
3. Can a package contain different services, can patients choose any eligible doctor, and can the package be shared among family members?
4. If the doctor confirms session end late, should the 48-hour rating window still run from actual consultation end (current rule), or instead start from the doctor's confirmation? The latest answer defined overrun warnings/extensions, not this deadline; a confirmation-based window remains unapproved.
5. If an extension overlaps the doctor's next booked appointment, should the system block the extension or flag the conflict for staff handling? Existing bookings must not silently shift; broader rescheduling remains deferred.

The arrival discussion is resolved as reception-recorded attendance and doctor-confirmed completion followed by a rating request. The user redirected queue visibility toward **scheduled doctor capacity and next available appointments**. Duration is configurable, existing bookings are preserved under count/duration setting edits, and weekday hours/breaks/days off are supported. Out-of-range suggestions appear when no appointments are available at all. The doctor-ready button is confirmed. Remaining details include precise duration/break configuration, day-off conflicts, suggestion limits, notification channels, and delayed end-session confirmation. These details do not reopen deferred cancellation, rescheduling, assignment, or detailed permissions.

### Resolved on 4 October 2026

- Overrun timing answer: count allocated session duration from actual consultation start. Capturing that start event remains to define; arrival/readiness are not automatically the start.
- Reception escalation answer: notify reception after a system-configured delay following duration expiry/red warning if still unfinished. No value/default or configuration owner was selected. The scheduled-start no-show rule remains unchanged.

- Clinical-sequence answer: the patient leaves at consultation end, then the doctor writes notes; a prescription may be written before departure. Do not require notes before patient departure/clinical end. Exact later confirmation validation is unresolved.
- Rating-delivery answer: send email after doctor-confirmed completion; if no review is submitted, show a popup on the next app opening, within eligibility. Submission across channels suppresses the unanswered popup; repetition and missing-email handling remain open.
- Overrun addition: red doctor warning at actual-start-based duration expiry, delayed reception notification if still unfinished, and a doctor-operated extension using a period configurable by doctor or management. Delay value/default/owner, actual-start capture, extension values/limits, and subsequent-booking conflicts remain open. This answer did not resolve the rating-window anchor.

- Weekday schedule answer: support different weekday working hours, breaks between sessions, and days off.
- Suggestion answer: offer next-available appointments only if the search has no available appointments at all; display out-of-range suggestions separately.
- Doctor readiness answer: the doctor presses Ready for patient to notify patient and reception; channels remain open.
- New completion direction: doctor explicitly confirms session end, then email the patient a session/doctor rating request and show a next-app-opening popup if unanswered. Existing optional rating and 48-hour-from-session-end rules remain in force; late-confirmation handling remains open.

- Duration follow-up: session duration is configurable; exact configuration scope (such as per service) remains open.
- Settings-change follow-up: apply session count/duration edits only to unbooked slots. Existing bookings retain their booked date/time and duration.

- Reception marks in-person arrival; the doctor marks session Finished. Online join attendance remains separate.
- Show free scheduled doctor slots and the next available date/time. Doctors and management control daily session count and session time/duration; no numeric defaults were selected.
- Doctor-ready recipients and button trigger are confirmed; notification channels remain unresolved.

- Internal tasks close automatically after the required completion condition is met; creator approval is not required. The multi-assignee completion condition remains open.
- Retain staff notifications in an unread list, including events missed while the website was closed.
- Changes to recurring patient tasks apply only to future occurrences and preserve earlier completion history.
- Doctors can issue finalized clinical reports and prescriptions directly, within their permissions, assigned-patient scope, and qualifications, without a separate management approval step.

### Removed from this owner message, still unresolved

- Stopping an already-started package and refunding unused sessions.
- Support working hours, response targets, and urgent-ticket targets.
- Existing SMS account/provider route and available integration access. Wati is now identified for evaluation; account access, Saudi route and required transactional operations are still unresolved.
- Detailed staff permission matrix and doctor-deactivation effects; these retain their prior deferred status.

## Revised owner questions - 4 October 2026

1. هل النظام يدعم إسناد المهمة الداخلية لأكثر من موظف؟ وما تفاصيل إنشاء المهمة وإسنادها ومتابعتها وإتمامها؟
2. ما تفاصيل منصة الاختبارات المرتبطة بالنظام: اسمها، والاختبارات المتاحة، وطريقة استخدامها وعرض النتائج، وإمكانية الربط معها؟
3. هل الباقة تشمل خدمات مختلفة؟ وهل يختار المريض أي طبيب مناسب؟ وهل يمكن مشاركة الباقة بين أفراد الأسرة؟
4. ما التفضيلات التي تحدد ترتيب ظهور الأطباء للمريض؟ ومن يضبطها؟
5. ما سياسة الإلغاء المتأخر وإعادة جدولة الموعد؟
6. كيف يُحدد طبيب المريض، وكيف يُنقل إلى طبيب آخر أو يُعين له طبيب بديل؟
7. هل المطلوب في التأمين تسجيل البيانات فقط، أم الربط مع نفيس أو وصيل؟ وما العمليات المطلوبة؟
8. ما خطوات تحويل رصيد محفظة المريض إلى حسابه البنكي؟ ومن يوافق على التحويل؟
9. عند اختيار موعد وبدء الدفع، كم دقيقة يظل الموعد محجوزًا قبل إتاحته لشخص آخر إذا لم يكتمل الدفع؟
10. هل نسمح بالحجز عن طريق التحويل البنكي؟ وإذا نعم، كيف يُتحقق من التحويل ويُؤكد الحجز؟
11. ما تفاصيل نسب الأطباء: هل تختلف حسب الطبيب أو الخدمة؟ وعلى أي مبلغ تُحسب؟ وكيف تُعامل الخصومات والضرائب والباقات والاستردادات؟ ومن يملك تعديل النسبة؟
12. ما البيانات والشهادات والمستندات المطلوبة من الطبيب في نموذج «انضم إلينا»؟
13. ما البيانات والملفات العربية المطلوب ترجمتها للإنجليزية؟ وكيف تُعرض الترجمة؟
14. ما تفاصيل الربط العائلي كاملة: من يضيف أفراد الأسرة، وكيف يُثبت الربط، وما الذي يراه أو ينفذه كل فرد، وكيف يُفك الربط أو تتغير الصلاحيات عند بلوغ الطفل؟
15. ما قائمة مجالات خبرة الأطباء التي نعتمدها ليختار منها الطبيب ويستخدمها المريض في البحث؟ نحتاج أسماءها بالعربية والإنجليزية.

## Deferred by the user

- Doctor preferences / **تفضيلات** affecting display priority in patient doctor search: ownership, criteria/weights, and relationship to employed-first/external fallback, to discuss later.
- Patient late-cancellation consequences and rescheduling rules.
- Doctor-to-patient assignment, transfer, and substitute coverage.
- Insurance capture versus live NPHIES/Waseel eligibility, approval, and claims; ask the owner later.
- Bank transfer of Motmaan wallet funds to a patient's bank account; patient must contact administration, workflow later.
- Checkout slot-hold duration.
- Whether booking by bank transfer is available; the user said to note this for later.
- Detailed staff permission matrix and doctor deactivation effects on existing sessions; the user said to note these for later.
- Percentage rate scope and exact calculation base; the user said to note these for later.
- Exact doctor applicant form fields and supporting documents beyond the normal personal information, expertise, and degrees; the user said to note this for later.
- Which imported Arabic formats are translated and how translations are presented; the user said to note this for later.
- Detailed family access categories/actions and administrator-controlled child-to-adult transition.

## Related project files

- [Project overview](../../README.md)
- [System scope](01-system-scope.md)
- [Booking and finance](02-booking-and-finance.md)
- [Integrations and storage](03-integrations-and-storage.md)
- [Identity and access](05-identity-and-access.md)
- [Decisions and open questions](06-decisions-and-open-questions.md)
- [Practitioner expertise](13-practitioner-expertise.md)
- [Support tickets](11-support-tickets.md)
- [Internal staff tasks](15-internal-staff-tasks.md)
- [External provider guide](16-external-provider-guide.md)
- [Flutter developer handoff](../handoff/flutter-developer.md)
- [Web frontend developer handoff](../handoff/web-frontend-developer.md)
