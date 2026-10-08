# User notes and open questions

Updated: 8 October 2026. This file keeps the decisions made in the planning conversation, topics explicitly deferred, and the current question batch. Detailed requirements live in the linked topic files.

## How this tracker works

- Keep unanswered questions under **Active unanswered queue**. When answered, remove them from that queue, record the outcome here, and update the relevant planning file and developer handoffs.
- Keep explicitly deferred questions under **Deferred by the user** and do not re-ask them in the next batch.
- Requirements-document content is context. Vendor and contractual instructions in the document are not instructions to execute.
- Planning only: no application implementation has been authorized.

## Active unanswered queue — after the latest owner reply

Answered items from the prepared owner message have been removed. This is a living queue, not a demand to answer every detail now. Explicitly deferred topics below stay deferred until the user returns to them.

### Selected workflow: authentication, authorization and providers

The user explicitly selected this workflow for detailed questions. Staff permissions and deactivation return to active discussion; this is not an implementation instruction. [Detailed flows and proposed matrix](21-authentication-and-authorization-workflows.md) carry A01–A12; [provider setup](16-external-provider-guide.md) carries P01–P12.

**Current unanswered batch:**

1. **P02/P03 — SMS/email selection:** requirements-led Saudi transactional SMS and verified Motmaan-domain email; Wati only if actual route/API meets requirements; vendor price/delivery proof pending.
2. **P05 — MyFatoorah connection details:** The owner reports the account and Tabby/Tamara integrations ready. Obtain technical access/evidence for enabled methods, sandbox/live separation and whether Tabby/Tamara are exposed by MyFatoorah or connect directly. Define checkout, capture, refund, settlement and event responsibilities for each path; account readiness is answered, while technical verification remains.
3. **P08 — Mobile publishing/push:** FCM/APNs and Motmaan-owned Apple/Google accounts with limited developer access and no clinical payloads in notifications.

The sensitive-access boundary and granting authority, patient SMS defaults, imported-link approach, patient assisted-recovery actors and core doctor-deactivation behavior are resolved below. Role baselines plus individual staff customizations, endpoint-specific action permissions, role-selected dashboards and development role test accounts are now confirmed. Exact catalog, multi-role conflict precedence/delegation and remaining provider evidence remain open; within-role additions/removals are answered. Further identity/family lifecycle is deferred (AUD-10), with existing transfer/access deferrals preserved. P01 ownership is answered; its 4 October inventory predates the reported ready payment account.

**Next authentication decisions after this provider batch:** unresolved multi-role conflict precedence and delegation ceilings (A06); within-role allowed/removed overrides, audit and safe revocation are confirmed by AUD-09; the exact endpoint-permission catalog and any non-CRUD action names are developer contract work for review, not a repeat of the answered granularity rule. Further identity/family lifecycle and consent/minor details are deferred under AUD-10; concurrent-device/session controls (A07), invitation/password technical defaults (A08/A12), account deletion (A11) and already separately parked transfer details retain their status. Identity evidence checklists and operation contracts are proposed review artifacts, not owner answers.

Earlier room-allocation ownership, mandatory recording, interruption review and pre-operation seeding remain confirmed. Their unresolved business details remain in the topic files.

### Other unresolved topics — outside the selected batch

1. **تفاصيل تغيير الأخصائي:** الخياران معتمدان: جلسة فقط أو نقل مسؤولية المتابعة. من يختار نوع التغيير ومن يوافق عليه؟ متى يبدأ وينتهي الاطلاع المؤقت، وما صلاحيات الأخصائي السابق بعد نقل المتابعة؟ ما أثر النقل على المواعيد والمهام والمقاييس القائمة؟ البديل عند الغياب يحتاج قاعدة مستقلة.
2. **بقية تفاصيل الباقات — خارج الدفعة الحالية بطلب المستخدم:** عدم إعادة الفرق عند الانتقال لأخصائي أقل سعرًا، واستخدام السعر الأساسي خارج الباقة للجلسات المستهلكة بما فيها عدم الحضور محسومان. نسبة سعر الأخصائي الأصلي أو المنفذ بعد النقل، ومعاملة فروق الأسعار المدفوعة تبقى تفاصيل غير محسومة؛ لا يعاد سؤال السعر الأساسي مقابل السعر المخفض.
3. **المحفظة:** ما بيانات الحساب والتحقق المطلوبة، ومن ينفذ التحويل بعد الموافقة، وكم يستغرق؟ ما الحالات/الرفض/التنفيذ الفاشل؟ كيف توزع دفعة خدمة استُخدم فيها مال وكوبون ثم استُردت؟ الطلب من داخل المحفظة والجهة الموافقة وعدم سحب الكوبونات محسومة.
4. **النسب — أثناء التطوير (AUD-14):** تُوثق نسبة كل طبيب وأساس صافي الإيراد وصيغ الحوافز الحالية كما هي. إسناد الفترة وتصحيحات الاسترداد والتغييرات وسط الفترة والكشوف المغلقة والمكتسب مقابل المصروف تُحسم عند تطويرها بموافقة المالك/المالية عند تغيير سياسة مالية؛ بقية الخصومات ومعدلات الخدمة تحتاج موافقة.
5. **التوظيف والخبرات:** ما قائمة الخبرات العلاجية العربية والإنجليزية وحدود الاختيار؟ هل طلب مراجعة نموذج الإداري مرجع فقط، أم مطلوب توسيع نطاق وظائف الإطلاق السابق؟ تحقق الشهادات والمرفقات الإضافية وقيود الملفات تحتاج تفاصيل؛ الحقول الحالية موثقة وليست سؤالًا يعاد بالكامل.
6. **الترجمة:** سلوك العرض حسب لغة الواجهة محسوم (AUD-16) ويشمل البيانات المناسبة غير الطبية والأسماء مع حفظ الأصل. المتبقي اختيار المزود والموافقة على معالجة البيانات الحساسة وصيغ الملفات وآلية المراجعة السريرية؛ لا يُعاد سؤال طريقة العرض العامة.

تفاصيل ضبط ترتيب الأطباء والتعادل، استثناءات تعديل/إلغاء الموظفين، ضرائب/تقريب الاسترداد، ومن يحجز باسم فرد الأسرة تبقى تبعيات مفتوحة في ملفات الموضوع. مهلة السبع دقائق ومنع التحويل البنكي وحد 24 ساعة ليست أسئلة مفتوحة.


### Other previously parked unresolved items

- Azure hosting follow-ups: service-by-service Qatar interim suitability and service/account access, later Saudi availability; tiers/monthly budget, baseline validation, operator and later selective Redis provisioning; Blob recorder/network compatibility. Azure SQL Database and Azure Managed Redis are answered and must not be re-asked. See [deployment preparation](22-azure-hosting-and-deployment.md).
- Background processing follow-ups: transactional outbox and Hangfire are confirmed, so technology selection is answered. Exact job/API contracts, worker/storage topology, provider idempotency/reconciliation guarantees, batch/concurrency/retry limits, latency/retention/alert thresholds and recovery ownership remain engineering work. See [detailed background workflow design](23-outbox-and-background-jobs.md). Existing deferred booking/payment rules remain deferred.
- Engineering tools are selected as recorded below; exact package versions, contracts and operating limits remain developer design work. Detailed SignalR event design is deferred (AUD-20); transport choice remains proposed: SignalR for connected clients with FCM/APNs for eligible mobile push is recommended; Flutter client, shared transport/hosting, message/read/recovery contracts and P08 provider setup remain unconfirmed. See [approved tools and proposed messaging](24-approved-engineering-tools-and-realtime.md).
- Support working hours, response targets, and urgent-ticket targets.
- Existing SMS account/provider route and available integration access. Wati is now identified for evaluation; account access, Saudi route and required transactional operations are still unresolved.
- Detailed staff permission matrix and doctor-deactivation effects are now in the selected active authentication/authorization discussion; separate sensitive grants, their owner-authorized granting administrators and current-consultation-only deactivation are confirmed; remaining granular defaults/mechanics are open; further identity/family lifecycle is deferred (AUD-10).

### Review follow-ups — recommendations, not owner answers

The [readiness review](20-development-readiness-review.md) classifies findings R01–R14 by affected implementation/launch gate. It does not reopen the deferred policy questions below. The authentication/authorization/provider batch above replaces the earlier priority batch.

Newly surfaced questions are recorded for later discussion, not presented as approved rules:

- **R05, booking — discussion deferred by owner on 7 October:** How does a cash visit enter the schedule before attendance, and when is room capacity guaranteed during self-service checkout? What happens to verified payment arriving after a released hold? Keep as a gate before booking/payment implementation.
- **R07, completion:** What should happen to the rating invitation if doctor confirmation is after the fixed 48-hour window? Do overrun alerts stop at actual clinical end while documentation remains pending?
- **R13, account lifecycle:** How are account deletion requests handled with active bookings, family grants, wallet funds and retained records? This is distinct from family exit.
- **R01/R14, release evidence:** AUD-03 confirms planning already addressed. Preserve existing milestones/responsibilities/schedule; only missing documentation links, acceptance/sign-off evidence or named operating contacts need follow-up, without inventing staffing or dates.

Engineering follow-ups: workflow contracts and examples (R02), clinical form inventory (R10), task/notification/metric definitions (R11), shared UI and client compatibility baseline (R12), and provider evidence (R09). Assign owners without inventing business policy. Permission and related family/transfer access questions are now part of the selected discussion; unrelated package and migration-export deferrals retain their existing status.

## Resolved owner audit responses — 8 October 2026

All 28 owner responses are recorded in the [decision register](06-decisions-and-open-questions.md#owner-decisions-on-the-8-october-audit) and [audit tracker](25-full-project-audit.md#current-owner-response-tracker). Do not re-ask resolved policy or infer implementation from documentation:

- Confirmed: authority/reconciliation (AUD-01), Qatar interim with production data review (05), recording reliability/readiness/adaptive playback (06), privileged verification (08), within-role allowed/removed overrides with 90/85 example (09), later-booking extension block (12), clinical versions (15), language-aware dynamic display (16), reception operational closure (19), SQL first/selective Redis later (21), shared reliable file lifecycle (23), obsolete-artifact deletion/table repair (28). See owning topic links in the register.
- Approved directions: progressive discovery (02), financial ledger (13), outbox/Hangfire reliability (22), measurable operational baselines/reporting (26). Engineering contracts/evidence remain, not repeat owner-selection questions.
- Planned: existing delivery/two-month arrangements (03); preserve milestones, responsibilities and target. Do not recreate a missing-plan question from historical audits.
- During Development: compensation period/correction treatment (14), with owner/finance approval of unresolved policy.
- No Change: future-only patient-task edits (18); No Additional Action: broad UI/parity audit concern (24).
- Notes only: Wati/Saudi SMS concern (04), future practitioner suggestions within the salaried group (27); neither authorizes replacement or ranking changes.
- Deferred and unresolved: AUD-07/10/11/17/20/25, as listed below. This response does not reopen previously deferred multi-assignee/task, package-edge or transfer details.

## Deferred by the user

- **AUD-07:** mobile purchasing/product classification; retain MyFatoorah, no new store payment route.
- **AUD-10:** further identity/family/guardian/beneficiary/consent lifecycle, including evidence, minor/self-exit and cross-member details. Preserve all confirmed rules.
- **AUD-17:** assessment API/SSO/result/payment contract when development reaches the integration; [prepared questions](18-assessment-platform-integration-questions.md) retained for that stage.
- **AUD-20:** detailed SignalR event taxonomy, ordering, delivery semantics and scaling; selection remains proposed.
- **AUD-25:** Emdaad migration details; full replacement/data-and-file migration remains a release dependency, with no invented cutover date.


- Detailed booking questions about room-capacity guarantee, cash booking before attendance and payment after an expired hold are deferred for discussion. Booking/payment implementation still needs those answers; the seven-minute hold and existing payment rules remain confirmed.
- Future treatment pathways involving multiple practitioners/services; current repeated-session practitioner packages are resolved.
- Internal multi-assignee task completion: all assignees finish versus one person finishing for everyone (Q2).
- Emdaad export formats/options and availability discussion (Q10); the full migration-at-launch requirement remains in force.

- Ranking ownership, tie-breaks and mixed-date display remain open; salary-paid availability priority is resolved.
- Further staff change/override rules remain open; patient cancellation/modification within 24 hours is blocked.
- Practitioner-change selection/approval, effective timing, detailed access and substitute coverage remain open; session-only and ongoing-follow-up transfer modes are confirmed.
- Live NPHIES/Waseel insurance operations are future work; no insurance currently.
- Bank execution/verification/reconciliation details remain open; request within wallet and system administrator/accountant approval are resolved.
- Additional deductions, optional service-specific rates, edit permissions and refund/period-close corrections remain open.
- Extra credential evidence, verification procedure, upload constraints and recruitment scope expansion remain open; current website baseline is recorded.
- Exact imported file/content formats remain open/noted for later; general selected-language display is confirmed (AUD-16).
- Remaining cross-member family access, relationship consent/proof, minor/self-exit and administrator-controlled adulthood interaction retain unresolved/deferred details.

## Resolved notes

### Engineering tools and Swagger/OpenAPI — 8 October 2026

- **Confirmed:** Swagger UI with OpenAPI contracts. The user approved the other recommendations: modular monolith, ASP.NET Core policy/resource authorization, FluentValidation, typed HttpClient with .NET HTTP resilience, OpenTelemetry/Application Insights, HybridCache with Redis, SQL Server integration tests using Testcontainers, Playwright and Flutter integration tests. Protected audit/edit history, incoming-webhook deduplication and database concurrency protection are approved as technical foundations.
- [Detailed notes](24-approved-engineering-tools-and-realtime.md) record responsibilities, safe retries, audit/caching behavior and client/testing consequences. Exact contracts/versions/configuration remain open; approving the approach does not finalize an API specification or authorize implementation.
- **Still under discussion:** The user asked whether SignalR is suitable across platforms. SignalR plus eligible FCM/APNs delivery and SQL-backed message recovery is the recommendation; SignalR, the Flutter client and the push/hosting choices are not confirmed by approval of the remaining tools. The existing P08 provider/account batch remains unanswered.

### Reliable background workflows — 8 October 2026

- **Confirmed:** Use the transactional outbox pattern with Hangfire for reliable external effects and appropriate lengthy/scheduled work. Save business state and required outbox records in the same Azure SQL transaction, then dispatch durable jobs with idempotent processing and recovery. Applies to accounting synchronization, required notifications and suitable imports, exports, reports, reminders and scheduled checks; critical booking/finance invariants retain database concurrency protection.
- [Detailed notes](23-outbox-and-background-jobs.md) record the recommended transaction/dispatch flow, duplicate and unknown-outcome handling, workflow checkpoints, security, hosting, client progress and future acceptance checks. The tool/pattern choice is confirmed; exact engineering contracts, limits and topology remain to specify. This records planning approval, not application implementation or resource provisioning.

### Backend readiness answers — 7 October 2026

- **Confirmed development role testing and permission granularity:** Create one confirmed/active nonproduction account per staff role with that role's full baseline permissions. Adding a service's permissions to a role automatically updates that role's default test account's effective access. Every protected backend endpoint has a specific action permission; create, read/get, update and delete are separate, and other operations need their own permissions. The role selects the staff dashboard; effective permissions determine the components and actions shown in it. Existing per-person customization remains supported. Production accounts and patient access are outside these development fixtures; server resource scope and separate sensitive grants still apply.
- **Confirmed database:** Azure SQL Database (SQL Server). Hosting region, tier, cost and provisioning still need validation.
- **Confirmed staff access model:** Each staff role provides permissions; authorized management can customize permissions for an individual staff member, so people with the same role can differ. The frontend uses the individual's effective permissions to show controls, while every backend action independently checks permission and branch/patient/resource scope. Patients are outside this configurable staff-role model, but their own and family access remains server-enforced. Separate clinical-record and recording grants still require administrators explicitly authorized by the owner. Effective permission precedence and management delegation details remain open.
- **Confirmed provider readiness report:** The owner says the MyFatoorah account and Tabby/Tamara integrations are ready. Technical access, exact BNPL route, enabled method evidence and test results remain to document.
- **Deferred discussion:** The owner requested that the booking-rule questions from the readiness list be left for later. This does not waive the booking workflow gate.

### Online payment provider — 7 October 2026

- **Confirmed:** Use [MyFatoorah](https://www.myfatoorah.com/) for online payments. The owner says Tabby (“tabbi”) and Tamara integrations are ready for integration. Tap is no longer the preferred provider; PayTabs and Moyasar remain historical research/comparison only.
- The app and patient website still need mada, Apple Pay, credit/debit cards, Tabby and Tamara. “Ready for integration” is the owner's status report, not evidence that Motmaan's MyFatoorah account has every method enabled or that a production transaction has passed. The MyFatoorah versus direct Tabby/Tamara connection path and operational ownership remain in P05.

### Azure caching and deployment discussion — 6 October 2026

- **Confirmed on 6 October:** Include **Azure Managed Redis** as the fifth service in the discussed Azure plan. Azure SQL Database was conditional at that time and was selected on 7 October. Application Insights/OpenTelemetry and HybridCache were approved on 8 October; App Service, private Blob Storage and Key Vault remain proposals. Regions, tiers, cost and final topology remain open.
- The user asked how deployment would start if they choose to proceed. [Azure deployment preparation](22-azure-hosting-and-deployment.md) records the recommended setup order and client/backend boundaries. This is guidance, not authorization to implement, create resources, purchase services or activate production.

### Authentication and provider batch — 4 October 2026

- **A06 operational roles:** Confirmed role baseline: reception handles scoped branch bookings/contact details, accountants handle scoped finance, doctors handle assigned patients, and managers receive only owner-assigned operational/reporting permissions. Separate clinical/recording grants remain required; the full granular action matrix is not approved by this baseline.
- **A02 self-service security changes:** Confirmed self-service safeguard: turning staff SMS verification off or changing its phone requires password confirmation and an SMS code to the existing verified phone. A lost phone uses the approved administrator recovery process. Detailed audit, conflict handling and administrator-change safeguards remain proposals.
- **P04/P12 provider administration:** Confirmed provider control: the owner retains business ownership, billing and recovery; developers receive limited individual access for setup/integration. Production activation requires owner approval after successful tests. Named delegates, vendor selection and test evidence remain open.

- **A08 recovery authority confirmed:** authorized account administrator verifies staff identity and restores lost SMS verification; owner verifies last-available-administrator recovery. Evidence and initial setup remain open.
- **A10 adult consent confirmed:** explicit adult consent precedes cross-member clinical-record access, including parent access. Family membership and package sharing remain separate; consent mechanics/minor rules remain open.

- **A07 session limits confirmed:** staff web 30 minutes inactive/eight hours total; patient web 30 minutes inactive/24 hours total; patient app 30 inactive days/90 days total. Active consultations and unsaved forms support safe reauthentication. The 15-minute access-token lifetime and technical/session-device details remain proposals.

- **A03 confirmed:** Patient login uses SMS with six digits, five-minute validity, resend after 60 seconds and five failed attempts per challenge. These defaults are configurable; provider/fallback and aggregate rate budgets are separate open details.
- **A04 adopted by delegation:** The owner asked the assistant to choose the correct linking approach. Use evidence-backed verified account-to-patient links prepared during migration, with reception reviewing ambiguous/unverified cases before first record access. This does not claim existing records are already verified or reopen Emdaad export formats. Exact proof/finalization/correction checklist remains open.
- **A06 confirmed:** Clinical-record and recording permissions require separate grants, including for system administrators, with branch/patient scope enforced. Only administrators explicitly authorized by the owner for access management may assign sensitive grants. Remaining role defaults/delegation ceilings remain open.
- **A05 recovery actors confirmed:** When the patient cannot access phone or established verified email, reception verifies identity and an authorized account administrator approves recovery. Evidence and safe contact-change mechanics remain to specify; established-email recovery remains sufficient without this review.
- **A09 core behavior confirmed:** Deactivation immediately blocks new doctor work. A doctor with an already-active consultation can finish and save only that consultation; access exception ends on its closure. Abandonment expiry, exact permitted actions and future-booking handover remain open; no new login or unrelated chart access is granted.
- **A01 confirmed:** Staff and doctors may use username, verified email or phone number with their password. Patient login remains phone OTP.
- **A02 confirmed:** Staff/doctor SMS additional verification is enabled by default. Each person can manage their own setting; an administrator with the appropriate permission can control it for all accounts. This does not let patients disable the OTP needed for patient login. Sensitive setting-change/recovery safeguards are recommendations pending review.
- **P01 confirmed, 4 October:** No external-provider accounts were available then. The project owner will be responsible for all accounts. On 7 October the owner reported the MyFatoorah account and Tabby/Tamara integrations ready; current credential access and method configuration have not been documented here. Recommendation: center-owned business accounts and billing with limited delegated developer access. The existing assessment platform remains reported to exist; its integration access is unavailable.
- The user has returned to authentication/authorization details, including previously deferred staff permissions and deactivation. The remaining matrix and related access questions are open, not answered by the login choices. Unrelated deferrals remain in place.


### Product, delivery, and roles

- Motmaan only; one branch initially with more possible later. Patients, doctors, schedules, and reporting are restricted by branch; cross-branch exceptions remain open.
- Latest delivery direction: all project requirements/features, including source-labeled later/separately approved items, belong in the first stage. Preserve explicit exceptions (doctor-only Join us jobs initially) and workflows the user has deferred. Production starts after two months of development at production-level quality; required checks include security, user acceptance, payment/accounting reconciliation, backup restore, performance, and monitoring. Initial operational baselines are approved under AUD-26; validation and named sign-off evidence remain open.
- Replace Emdaad at production launch and migrate all its data: patient profiles, family links, appointments, clinical history, finance, packages, and referenced files. Export coverage, mapping, reconciliation, and cutover validation remain open.
- Use Saudi Arabia time (`Asia/Riyadh`) project-wide. Store event instants in UTC and convert/calculate schedules, recurrences, display times, and calendar boundaries in the named zone.
- Initial role groups: manager, reception, administrator, and doctor, with accountant participation now required for internal staff tasks. The permissions matrix is open.
- Staff UI shows or hides actions based on granted permissions; API authorization remains mandatory. Management controls each doctor's active status, and only active doctors may log in to the doctor dashboard.
- Experiences: management dashboard, doctor dashboard, patient website and mobile app, and public site/Join us. All websites should support desktop/mobile and Arabic/English RTL/LTR.
- Backend direction: ASP.NET Core and EF Core; use `api-pattern` for future API work. Performance and security are priorities. No coding yet.
- Patient login uses phone OTP. Patients may add a username/email; email recovery requires verification, and username alone does not prove ownership.
- Each doctor sees their assigned patients only. Practitioner changes support both session-only assignment and transfer of ongoing follow-up; who selects/approves, effective periods, detailed access and coverage remain open.
- Patients can see all information about their own case; internal metadata boundaries remain open.

### Booking and money

- Booking and payment are supported in the patient app and responsive website. Required online methods: mada, Apple Pay, credit/debit, Tabby, and Tamara. MyFatoorah is the confirmed online payment provider; see the 7 October note above for the reported BNPL readiness and remaining connection details.
- Online booking confirmation requires trusted provider confirmation to the backend.
- Cash is accepted only at in-person sessions when the patient attends. Booking by bank transfer is not allowed.
- Checkout holds the selected appointment for seven minutes, shows a countdown, then releases unpaid capacity and displays «انتهى وقت الدفع، يرجى المحاولة مرة أخرى». API/server expiry is authoritative.
- Motmaan owns operational payment/refund, wallet, package, and appointment records and sends required accounting events to Qoyod. Per the user's delegation, the planning recommendation is that Qoyod issues official accounting/e-invoicing documents; use reliable idempotent sync and retain Qoyod references/status. Confirm finance and account configuration before implementation.
- Patient cancellation or appointment modification is blocked with less than 24 hours remaining. At/above the cutoff retain original-method refund/wallet choice and package entitlement restoration. This supersedes the earlier unspecified admin cutoff; staff exceptions and further change rules remain open.
- Motmaan/doctor cancellation credits the wallet. The patient now requests bank payout inside the wallet for service-refund-origin funds only; system administrator or accountant approves. Coupon credit cannot be withdrawn; bank execution details remain open.
- Administrators have full control over package offers and settings. Exact fields and safeguards remain to define.
- For in-person and online no-shows, retain payment or consume one package session; no doctor incentive. Mark after scheduled start plus dynamic admin-defined grace period, unless attendance or active online session is recorded.
- The patient app shows an appointment countdown and advance notice; admin sets reminder lead time.
- Reception marks in-person patients Arrived; the treating doctor normally marks Finished; reception may perform authorized operational closure if the doctor forgets (AUD-19), without clinical signing. Patient self-recording of in-person arrival is superseded; online attendance evidence remains separate.
- Patients book scheduled free doctor slots and see the next available date/time, even if it is a week away. Waiting-room queue/estimated-wait display was not selected. Doctors and management control daily session count and session time/duration; five sessions per day and X minutes are examples only. See [booking and finance](02-booking-and-finance.md) and [customer appointments](10-customer-mobile-appointments.md).
- Session duration is configurable. Session count/duration setting changes affect only unbooked slots; existing bookings retain their booked date/time and duration. Exact configuration scope (such as per service) remains open; no numeric defaults were selected.
- Schedules support different working hours per weekday, breaks between sessions, and days off. Exact break settings and handling days off conflicting with existing bookings remain open; no automatic cancellation/rescheduling is approved.
- When the search has no available appointments at all, show separate next-available date/time suggestions, including beyond the selected range. Keep matching non-date filters, branch scope, and salary-paid availability priority/external fallback; do not silently widen the range. Exact suggestion count/search horizon remain open.
- The doctor presses Ready for patient to notify both reception and the patient. Trigger and recipients are confirmed; channels remain open. Advance reminders stay separate.
- The doctor explicitly confirms the end-session process; after confirmation marks the session Finished, email a request to rate the session/doctor. If unanswered, show a rating popup on the patient's next app opening within eligibility. Reviews remain optional, out of 10, with existing visibility/editing rules. The 48-hour window starts at actual consultation end even if confirmation is delayed; reception records the actual in-person end if the doctor forgets. Recording/correction permissions, confirmation validation, popup repetition, and missing-email handling remain open. See [patient feedback](14-patient-session-feedback.md).
- Actual in-person consultation end means the patient leaves. The doctor writes notes afterward and may write a prescription before departure. Do not require notes before clinical end/patient departure or invent a mandatory note-save gate. Later Finished confirmation and actual consultation end are distinct.
- Measure allocated session duration from actual consultation start. At expiry, show the doctor a red warning if unfinished; notify reception after a system-configured delay if it remains unfinished. No delay value/default or setting owner was selected. The doctor may extend the active session by a period configurable by doctor or management. AUD-12 supersedes the earlier permission: block extension if the doctor or room has a later booking; no automatic shifts/delays, and actual overruns are recorded separately. A 1.5-hour session is illustrative, not a default. Actual-start capture, extension values/limits and exact waiting/conflict detection remain open; no automatic completion, no-show, or charges are selected. Scheduled-start no-show grace is unchanged. See [customer appointments](10-customer-mobile-appointments.md).

### Doctors, recruitment, expertise, and patient tasks

- Compensation supports percentage-only and salary plus an incentive on monthly eligible revenue above a target. SAR 10,000 and 20% were examples. Eligible incentive revenue is completed and fully paid, after discounts, excluding VAT, adjusted for refunds; package revenue is allocated as sessions complete.
- Join us starts with doctor applications only. Administrators control openings and applications. Other job types may be added later. Authorized acceptance automatically provisions/resolves a doctor account, assigns doctor role, and sends an SMS invitation.
- Doctor expertise is a database-backed, administrator-editable catalog of areas of strength within psychiatric care. Each doctor may list several strengths on their profile; patients filter doctors by them. Management interviews candidates and approves expertise/degrees before public display. Management approval of post-hiring public biography/expertise changes is confirmed; exact review workflow and Arabic/English catalog labels remain open; the user is unsure about seed values. See [practitioner expertise](13-practitioner-expertise.md).
- Applicant fields/documents use the [existing website baseline](19-recruitment-current-website-reference.md), plus therapeutic expertise multi-select. The specialist's required uploads are CV and health-specialties certificate. Management verifies qualifications/data before activation; verification and public-field mapping remain open. The administrative form is recorded as a reference, without changing initial doctor-only recruitment.
- Patient doctor search filters include expertise, specialty, language, appointment mode, and availability. Per user's delegation, recommended logic is AND across categories and OR among values within a category.
- Doctors can handle all listed clinical work: diagnoses, treatment plans, prescriptions, reports, session records, and tasks, within granted permissions, assigned-patient scope, and applicable qualification rules. Doctors may issue finalized clinical reports and prescriptions directly, without a separate management approval step, within granted permissions, assigned-patient scope, and applicable qualifications.
- Percentage compensation rates vary by practitioner and use net revenue after tax and discounts. Further deductions, service-specific overrides, edit permissions, rounding and refund corrections remain open. Above-target commissions on additional eligible revenue are reconfirmed.
- Patient tasks include daily/weekly self-care actions and Motmaan program recommendations. Doctors assign them; patients can mark actions complete or missed and give a reason; doctors can review. Doctors control patient tasks and their reminder schedule; the backend calculates and sends recurrence-based push notifications in `Asia/Riyadh`, and the app displays them. This supersedes earlier admin timing control; appointment reminder lead time remains admin-controlled. Confirmed controls are time of day, selected weekdays, start/end dates, and reminders per day. Changes to recurring patient tasks apply only to future occurrences and preserve earlier completion history. Weekly summaries go to both patient and assigned doctor; numeric task limits and summary content, timing and channels remain open.
- Patients can book and pay for a recommended Motmaan program through app or website.

### Internal staff work and doctor discovery

- Doctor-priority criteria are confirmed as salary-paid and available. Preserve branch/date/filter scope and prior external fallback. Ownership, tie-breaks and mixed-date presentation remain open; see [practitioner expertise](13-practitioner-expertise.md).
- Internal administrative tasks allow reception/accountant assignment with several assignees, details, Low/Normal/High/Urgent priority, optional due dates and overdue indication, comments, and files. Status is automatic from actions. Tasks close automatically when the completion condition is met, without creator approval; exact mappings and the multi-assignee completion condition remain open. Assignment/comment/status/deadline/overdue events notify live inside the website. Management sees full authorized-branch task details; other staff see full created/assigned task details. Unread notification persistence, including events missed while the website was closed, is confirmed. Recipient rules and file constraints remain open. See [internal staff tasks](15-internal-staff-tasks.md).
- Employed and external doctors share the same operational behavior/access rules. Prioritize available salary-paid practitioners in discovery/booking; preserve external fallback when prioritized practitioners are full over the selected dates and matching filters. Compensation stays distinct. Search accepts start/end dates; equal dates mean one day. Evaluate fallback over the selected range and matching filters; mixed-date display remains open.

### Support, records, video, and files

- Patients only submit support tickets; administrators resolve them. Statuses: Open, In progress, Waiting for patient, Resolved, Closed. Push updates and an in-ticket new-message indicator are required. When Closed, email a satisfaction survey rated out of 10 with optional comments and one submission per ticket; link it to the resolving admin. Management sees all results; the patient sees their own response.
- Patients may optionally review a session and its doctor within exactly 48 hours from session end, with a rating out of 10 and written comments (recommended as optional). Management sees all reviews; the submitting patient sees their own and the session doctor sees that review. No other users see it. Mobile review editing is allowed within the original 48-hour window; edits do not extend it. Web editing/retraction remains unspecified. Ticket satisfaction remains once only. See [patient feedback](14-patient-session-feedback.md).
- **Confirmed AUD-16:** suitable dynamic display data follows the selected Arabic/English interface language, beyond imported/clinical text; transliterate names and preserve originals. Evaluate a suitable API/derived representation approach. Google Cloud Translation is an evaluation candidate, not a final vendor. Keep the Arabic source, label machine translation, and approve privacy/residency before processing health data externally. Specific file formats remain open; general display-language behavior is resolved; human clinical review is the recommended approach, not yet selected by the user.
- Agora is the source-named provisional online session provider. Proposed recording delivery goes directly into a supported private center bucket; one-year retention is a source requirement. Playback is limited by management permission. Provider/storage fit remains to validate.
- Center-controlled private storage remains required/proposed according to data class; Azure Qatar Central is the interim hosting preference subject to production health-data/cross-border review (AUD-05). Private Blob fit remains unverified; GCS Dammam/OCI Saudi are retained alternatives, not selected.
- Qoyod is the named accounting/e-invoicing system. Wati is source-named for WhatsApp; on 4 October the user also identified it for WhatsApp/SMS evaluation. Its role and research dependencies are in the [expanded Wati notes](17-provider-documentation-development-notes.md#whatsapp-and-sms-handling-wati). Final SMS route, existing account/access, and assessment API/SSO remain to confirm; identifying the platform does not approve activation or change OTP channels.
- The user requested a dedicated external-provider Markdown guide showing each provider's role and configuration clearly. See [external provider guide](16-external-provider-guide.md); keep it current when provider decisions change.
- Family addition is by father or mother. Each member sees own reports/sessions/diagnoses and invoices if they paid; self-exit notifies family head and enables independent booking and ordinary patient powers. Previous parent visibility direction is not explicitly withdrawn; exact cross-member scope and self-exit/minor/guardian interaction remain open. A parent need not have a patient record; no automatic adulthood change is selected.
- No insurance currently; prepare for future NPHIES/Waseel integration. Live insurance operations remain deferred.

### Resolved on 4 October 2026

#### Wider priority batch — latest owner answers

- Staff/doctors use username, verified email or phone number plus password. SMS additional verification is enabled by default; ordinary staff manage their own SMS setting subject to AUD-08 mandatory privileged verification and an administrator with the relevant permission may manage it for all accounts. These newer answers supersede the earlier unresolved credential/default/control details. The detailed permission matrix is now under active clarification; patient OTP now uses SMS with confirmed defaults; the final SMS vendor remains open.
- Rooms are assigned per appointment by reception. Show suggestions of available rooms for the appointment; do not automatically allocate a room for a practitioner's entire shift. Selection timing, ranking and room/service constraints remain open.
- Every online session must be recorded for safety and performance review. An unrecorded online-session option is not selected. Preserve consent and restricted playback; exact consent/refusal and recorder-failure handling remain open.
- Connection-failure clarification: management may review an interrupted/incomplete online session and grant a free replacement session; the patient may open a support ticket for review. Neither interruption nor ticket creation automatically grants a session. Detailed review/grant conditions and partial-session accounting remain open.
- Existing data will be seeded/imported before operation begins. Seeded login identifiers, account-to-patient relationships, duplicate/shared-phone reconciliation and first-access proof remain unspecified. Do not infer that preseeded clinical data authorizes access solely by matching a phone number.

#### Latest package answers and discussion direction

- Switching to a cheaper practitioner does not return a price difference; prior additional-payment rules for a more expensive switch remain in force.
- Package-stop refunds reprice used sessions at standalone/base price outside the package. The reply does not explicitly select original-versus-performing practitioner price after a transfer; retain that attribution as unresolved outside the next discussion.
- Consumed no-show package sessions are also repriced at standalone/base price for a later package-stop refund. They remain excluded from doctor incentives and completed-session target progress.
- The user requested moving outside this scope to necessary, important unanswered questions across the project. The priority owner batch above records the proposed next discussion; it does not reopen explicit deferrals or authorize implementation.

#### Latest three-question batch

- Support reopening: patients may reopen their resolved/closed tickets without a time limit. Resulting status mapping remains open; one satisfaction response per ticket remains in force.
- Review deadline: exactly 48 hours from actual consultation end, including delayed doctor confirmation. Reception records actual in-person session end if the doctor forgets. Detailed recording/correction permissions remain open; AUD-19 additionally permits authorized reception operational closure when the doctor forgets, without clinical signing; actual end and closure time remain separate.
- **Superseded 4 October extension answer:** AUD-12 now blocks extension whenever the affected doctor or room has a later booking. Preserve scheduled times, no automatic moves and other rules when no later booking exists; operational overrun recording is distinct.

## Latest owner answers — resolved notes, 4 October 2026

- Assessments already exist and are expected to launch this week per user; integrate them into the app. Programmer details are pending and [questions are prepared](18-assessment-platform-integration-questions.md). Launch timing is not independently verified.
- Current packages repeat sessions for a selected practitioner. The patient selects practitioner then package; each practitioner has defined packages. Future treatment pathways involving different practitioners are explicitly later.
- Family members can consume package sessions and change practitioner, paying a difference if any. Sharing does not authorize cross-member medical access or wallet withdrawal.
- Prioritize salary-paid practitioners with availability; maintain matching filters/branch/date rules and existing external fallback.
- Block cancellation or appointment modification with less than 24 hours remaining. At exactly 24 hours the wording permits the action; this boundary is an interpretation documented for verification. Staff exceptions remain open.
- No current insurance. Prepare for future NPHIES/Waseel integration; no live insurance activation now.
- Patient requests bank payout within wallet, only for service-refund funds. A system administrator or accountant approves. Coupons/promotions are not withdrawable; execution details remain open.
- Seven-minute appointment hold with countdown; at unpaid expiry release it and show «انتهى وقت الدفع، يرجى المحاولة مرة أخرى».
- Booking by bank transfer is not allowed.
- Percentage rates differ by practitioner, calculated on net revenue after tax and discounts; unspecified further deductions are open. Above-target commissions apply to additional eligible revenue above the target.
- Stopping a package uses the original base price for used sessions: SAR 1,000 paid for four originally SAR 1,200 sessions, two used × SAR 300 = SAR 600, refund SAR 400. Discounted completed-session allocation is SAR 250 each. Example values are not defaults. Latest answers confirm standalone/base-price repricing of consumed no-show sessions and no refund of a cheaper-practitioner difference. Practitioner price attribution after transfer, paid differences, tax and commission corrections remain open outside the next discussion.
- Applicant data/documents follow [the reviewed existing website forms](19-recruitment-current-website-reference.md); add therapeutic expertise multi-select. Administrative fields are captured as requested, while expansion of initial doctor-only job scope is not assumed.
- Father or mother adds family members. Members see their own reports, sessions, diagnoses and invoices if they paid. A member exits via «الخروج من العائلة»; notify family head and enable independent booking/all ordinary patient powers. Proof/consent, other members' data, minors and financial/booking effects remain open.
- The practitioner-unspecified package hypothetical is removed because current packages specify a practitioner. The user then confirmed both practitioner-change modes: **session only**, retaining the current ongoing-follow-up practitioner, and **transfer of ongoing follow-up** to the new practitioner. The either/or question is answered and removed from the queue; only selection/approval, timing, existing-work effects and detailed access remain open. Neither mode selects a default or starts implementation.

## Provider documentation review — 4 October 2026

The requested documentation review is recorded in [provider development notes](17-provider-documentation-development-notes.md), with priorities marked in the [provider guide](16-external-provider-guide.md). It separates public technical facts, recommendations, and missing account/vendor evidence. It adds development dependencies for payments/accounting, recording/storage, push, messaging, translation, and migration. No queued business question was answered by provider documentation; the queue and deferred topics below retain their status.

## Discussion history

Older question batches and superseded deferrals are retained in [the discussion archive](../archive/2026-10-04-discussion-history.md). Current resolved rules remain above and in the topic documents.

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
