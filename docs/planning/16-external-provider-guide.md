# External providers: purpose and configuration

Updated: 8 October 2026. Planning only. MyFatoorah is selected for online payments; its account and Tabby/Tamara integrations are reported ready by the owner. Technical access, enabled methods and completed integration have not been verified here.

This is the practical provider inventory for Motmaan. It explains each provider's role, what we need to configure it, who handles the work, and the expected setup effort. Detailed integration decisions remain in [integrations and storage](03-integrations-and-storage.md).

## Current owner answers and setup workflow

**Confirmed:** On 4 October, no external-provider accounts were available. The project owner remains responsible for them. On 7 October the owner selected MyFatoorah and reported its account and Tabby/Tamara integrations ready. Technical access, enabled methods and activation evidence have not yet been documented. The assessment platform still exists according to the earlier user answer; its name/API/integration access remains unavailable.

**Confirmed ownership/delegation:** Create organization accounts and billing under Motmaan's business identity; the owner retains ownership, billing and recovery. Developers receive limited individual access for setup/integration. The owner approves production activation after successful tests. Do not share the owner's password. Use a controlled recovery arrangement so loss of one person's phone does not orphan every provider. Final delegates and recovery contacts remain open. Ownership is a responsibility decision, not a grant to read all clinical data.

The first implemented authentication workflow needs working SMS delivery, transactional email and a selected hosting/secrets arrangement. Push, payment, accounting, assessments and recording have their own workflow gates; they do not need to become login dependencies. Provider setup remains planning work until the necessary configuration/purchasing actions are authorized.

**Confirmed Azure selections:** Use Azure SQL Database (SQL Server) for the backend and include Azure Managed Redis as the fifth service in the discussed hosting plan. OpenTelemetry with Application Insights and HybridCache are now approved on 8 October. App Service, private Blob Storage and Key Vault remain working proposals. AUD-05 selects Qatar Central interim, subject to production health-data/cross-border suitability review, and a verified suitable Saudi region long term. AUD-21 requires SQL first and later selective public Redis caching. See [Azure deployment preparation](22-azure-hosting-and-deployment.md) for regional service/access, cost/recorder and migration gates. [Engineering/messaging notes](24-approved-engineering-tools-and-realtime.md) retain SignalR/FCM/APNs as recommendations; P08 provider/account evidence remains open. No resource creation or production activation is authorized by these answers.

### Provider questions and recommended answers

| ID | Question | Current answer / recommendation | Evidence needed to close |
|---|---|---|---|
| P01 | Which accounts exist and who owns them? | **Resolved ownership:** project owner responsible. None available was the 4 October inventory; 7 October owner reports MyFatoorah account and Tabby/Tamara ready, with technical access/route evidence pending | Account creation/access evidence is future work; it does not undo the answered ownership decision |
| P02 | Which route sends patient OTP, staff SMS verification and doctor invitations? | Staff and patient SMS are confirmed; patient challenge defaults are recorded in workflow 21. Evaluate a supported Saudi transactional SMS route; keep Wati for evaluation rather than assuming its campaign feature fits authentication | Sender eligibility, standalone transactional API, Arabic delivery, receipts, expiry-safe retry/fallback, invitation-link support, quotas, cost and test evidence |
| P03 | Which provider sends recovery/verification email and surveys? | Vendor open. Recommend a transactional sender under Motmaan's domain with authenticated sending, bounce handling and separate test/live setup | Domain/DNS access, account, API/SMTP contract, message templates, recovery-link return paths and delivery evidence |
| P04 | How are secrets, test/live configuration and provider settings managed? | Confirmed owner business/billing/recovery control and limited individual developer setup/integration access. Proposed backend/infrastructure secret storage; management UI shows masked configuration/status, never readable secret values | Hosting choice, scoped administrator/developer grants, rotation/recovery and audit procedure; no secrets in Markdown or clients |
| P05 | How will selected MyFatoorah and ready Tabby/Tamara integrations connect? | **Provider and account status resolved by owner report:** MyFatoorah for online payment; account and Tabby/Tamara integrations ready. Required cards/mada/Apple Pay/Tabby/Tamara remain. Route through MyFatoorah versus direct BNPL connection is unresolved | Technical merchant/test access, enabled method list, BNPL route and responsibility boundary, checkout/capture/refund lifecycle, settlements, sandbox and app/domain setup |
| P06 | How is Qoyod connected? | Existing planning direction: Motmaan owns operational transactions; Qoyod issues official accounting documents. No account access yet | Finance-validated account/tax mapping, API entitlement, issuance/correction behavior, ambiguous-create recovery and reconciliation |
| P07 | Which call/recording/storage combination is usable? | Agora provisional; private Azure Blob Storage is proposed in the discussed Azure plan, with GCS Dammam and OCI Saudi retained as alternatives. Mandatory recording readiness/reliable transfer/adaptive playback (AUD-06) and independent playback grants remain confirmed; [04](04-online-sessions.md) owns media requirements | Consent/refusal/recorder-failure policy, exact destination/credential/network test, interim Qatar suitability/service access, processing/fallback arrangement, resumable transfer/asset processing, retention/deletion evidence and real-device tests |
| P08 | Which push service and mobile-store accounts? | FCM/APNs proposed; none were available at the 4 October inventory. Owner controls business/store identity, developers get scoped access | Apple/Google account setup, signing/app IDs, device-token lifecycle, privacy/data handling and device delivery evidence |
| P09 | How does the existing assessment platform authenticate and exchange results? | **Deferred AUD-17:** integrate existing platform when development reaches it; no invented API/SSO/results/payment contract. Prepared questions in document 18 retained | Platform name/link, programmer contact, contract/sample data, sandbox, identity/SSO/payment/result/revocation behavior |
| P10 | Which hosting, database, monitoring and backup services? | Partially answered: Azure SQL Database and Azure Managed Redis selected; OpenTelemetry/Application Insights and HybridCache approved on 8 October. App Service, private Blob and Key Vault remain proposals. [Setup guide](22-azure-hosting-and-deployment.md) | Budget/tiers, Qatar data suitability and regional service access, processing/recording fit, telemetry, later Redis provisioning and validation of [AUD-26 baselines](09-performance-security-and-responsive-websites.md#initial-operational-targets-and-reporting--aud-26) remain engineering/evidence work |
| P11 | How are translation, Nafath/Wasfaty and future insurance handled? | AUD-16 display-language behavior confirmed beyond medical text; translation/transliteration candidate and sensitive-data processing approval remain open, exact formats noted for later. Nafath/Wasfaty need defined use cases/access; do not make Nafath replace confirmed phone login. Live insurance remains future work | Relevant official onboarding contracts and data-handling acceptance; no speculative activation or assumption that one provider covers all functions |
| P12 | Who approves and verifies a provider change or production activation? | Confirmed owner approval of production activation after successful tests; proposed owner approval of commercial/data-handling choice; responsible developer demonstrates technical flow; finance/clinical reviewer signs relevant business behavior | Named contacts, provider-specific acceptance evidence and handover/runbook. No activation is performed in this planning task |

Each provider row needs: selected product/plan, business owner, technical delegate, account status, documentation/version, test/live separation, data sent, processing/storage location, enabled features, setup cost/ongoing cost, evidence links, next action and due date. Unknown means unknown, not unsupported or already purchased.

### Recommended setup sequence

1. Use confirmed patient SMS and staff/security decisions; settle remaining detailed settings in [authentication workflows](21-authentication-and-authorization-workflows.md). Obtain the Motmaan domain/account ownership details and identify responsible technical delegates.
2. Validate the proposed SMS route and transactional email contract; define templates, challenge expiry/retry behavior and error states. Use synthetic data and authorized test recipients when testing is later authorized.
3. Agree hosting/secret management and establish isolated development/test environments after implementation/setup authorization. Credential checks and webhooks run on the backend.
4. Start payment merchant, Qoyod, assessment and recording/storage prerequisite work early; these external lead times can affect delivery even when screens are designed.
5. Prepare mobile-store identity/signing and push setup in time for device integration and review. Public client configuration must be distinguished from secrets.
6. Before production, complete each provider's acceptance scenarios, callbacks/reconciliation, monitoring, recovery and ownership handover. Account creation alone does not establish readiness.

### Saudi transactional SMS concern — AUD-04 (Note)

Keep Wati evaluated under the existing plan; this note selects no replacement. A specialized Saudi SMS provider may be needed if the actual route cannot meet OTP, sender registration, Arabic content, delivery receipts and reliability requirements. Verify these before production. SMS remains the confirmed authentication channel; do not switch to WhatsApp. Account/route evidence must also cover invitations, expiry-safe delivery, and outages.

### Authentication delivery contract

Motmaan owns challenge purpose, value, expiry, resend/attempt limits and verification. A delivery adapter accepts a message request and returns safe attempt/provider references; later receipts update delivery status only. Authentication must never succeed because a provider says “delivered.” Do not allow provider outage or a delayed fallback to disable staff verification, extend code validity or bind the wrong account. Message content includes only what the verification task requires.

Provider callbacks must be authenticated according to the actual provider contract and deduplicated. Store safe delivery/error references; keep OTPs, credentials and clinical details out of ordinary logs. Recheck challenge validity before queued sends/retries. A timeout can mean unknown delivery rather than definite failure; reconcile where supported and avoid uncontrolled repeated sends.

**Rechecked public evidence on 4 October 2026:** Wati documents SMS campaigns/fallback through an active Twilio account and its Business plan. This does not establish Motmaan's standalone transactional SMS capability or Saudi sender eligibility. Validate the exact route using the vendor's response and delivery tests. [Wati setup](https://support.wati.io/en/articles/11694867-how-to-integrate-wati-with-twilio), [Twilio Saudi route guidance](https://www.twilio.com/en-us/guidelines/sa/sms). No account-specific test or message was performed.

### Provider acceptance and outage handling — proposed runbook

Updated planning detail: 5 October 2026. The owner has confirmed control/delegation and production approval; the procedures below are recommendations. No account, paid plan, merchant entitlement or successful integration test currently exists as project evidence.

| Connection | Minimum acceptance evidence before its workflow uses it | Proposed failure behavior |
|---|---|---|
| Patient/staff SMS and invitations | Account/route entitlement; Saudi Arabic-message delivery to authorized test recipients; expiry/resend/receipt behavior; exact transactional API and invitation-link capability | Show delivery unavailable/pending safely. Keep proof expiry and enabled verification in force; do not authenticate on a delivery receipt. Invitation retry does not create another doctor |
| Recovery/verification email | Business domain/sender control, authenticated sending, tested link destinations, expiry/replay, bounce handling and test/live separation | Preserve the existing contact until replacement completes. Show generic request outcome; offer approved recovery review rather than attaching an unverified email |
| Payment gateway/methods | Motmaan merchant approval for each required method; method-specific checkout, authenticated events, pending/late success, refunds, settlements and reconciliation | Keep unknown payment outcome pending for reconciliation. No client-only success, duplicate charge or automatic retry with a new charge merely after timeout |
| Qoyod | Finance-reviewed mapping/tax documents; API entitlement; issue/correct/refund examples and unknown-create reconciliation | Operational transaction remains traceable; queue/reconcile accounting failures and prevent duplicate official documents |
| Video/recording/private storage | Scoped join and playback, exact recorder/bucket test, complete recording asset, interruption behavior, storage/processing evidence and deletion/restore checks | Recording failure follows the still-open stop/continuation/replacement policy. Never quietly run an unrecorded session or claim compliance from a Saudi bucket alone |
| Mobile push/store accounts | Motmaan business account control, scoped signing/delegation, real-device Android/iOS delivery, permission denied and stale-device/account-switch checks | App/server state remains authoritative if push is late/missing. No clinical content in proposed notification payloads; deep links recheck current account access |
| Assessment platform | Documented trust protocol, verified patient mapping, sandbox, permissions, result ownership/correction and account revocation behavior | Report unavailable/pending integration safely; do not export general Motmaan tokens, duplicate identities or substitute an undocumented embedded page for SSO |
| Hosting/secrets/backup | Selected regions and access, separate test/live config, secret rotation, monitored failure and demonstrated backup restore | Escalate to named operator; use agreed recovery targets. AUD-26 planning baselines require hosting/restore validation; clinical continuity details remain open |

A provider evidence record should contain the product/plan/API version, test case, environment, sanitized result, tester, review date, unresolved limitations and owner approval reference. Never keep keys, passwords, OTPs, clinical test records or unredacted provider payloads in these Markdown files.

Proposed activation sequence: responsible developer demonstrates the agreed flow → operational/finance/clinical reviewer checks the relevant behavior → owner approves activation after successful tests → authorized technical delegate applies configuration → reviewer confirms monitoring and rollback/recovery readiness. Owner activation approval is confirmed; exact reviewer names and change/runbook procedure remain open. A vendor preference may be accepted now while account-specific capability remains unproven.

## Important points marked for later development

Official documentation was reviewed on 4 October 2026. The [provider documentation development notes](17-provider-documentation-development-notes.md) retain the technical findings, direct sources, evidence gaps, and future verification scenarios. **P1** means resolve before committing to the affected provider/workflow; **P2** means carry into future development. These markers are planning priorities, not provider selection or new business decisions.

| Provider / connection | Marked priorities |
|---|---|
| MyFatoorah | **P1:** Motmaan account access, enabled methods and Tabby/Tamara route. **P2:** Authenticated webhook/status reconciliation, operation-specific duplicate protection and pending refund handling. |
| Tabby / Tamara | **P1:** Gateway versus direct responsibilities and service/package capture rules. **P2:** Regional configuration, distinct lifecycle states, authenticated events, and operation references. |
| Qoyod | **P1:** Account/tax/correction behavior and ambiguous-create recovery. **P2:** Durable accounting sync, mappings, and reconciliation. |
| Agora / GCS / OCI | **P1:** Exact bucket compatibility, processing/fallback locations, and deletion/recovery policy. **P2:** Recorder lifecycle, final asset verification, scoped playback, and complete asset deletion. |
| FCM / APNs | **P1:** Account and data-handling approval. **P2:** Device-token lifecycle, permission/OS delivery limits, and persisted app state. |
| Wati / SMS route | **P1:** Workspace/plan, supported Saudi sender route, transactional API and fallback contract. **P2:** API version, template mapping, channel receipts, and expiry-safe retries. |
| Translation | **P1:** Approved processing/data categories/vendor; exact file formats remain open. **P2:** Confirmed language-aware display, names transliteration, original preservation, derived provenance/cache and clinical safety controls; see document 03. |
| SMS / email / assessments / Emdaad | **P1:** Identify missing vendors/contracts or obtain complete export material; do not infer undocumented capabilities. |
| Comparison and source-only connections | Retain alternatives and unresolved onboarding; no insurance currently; future NPHIES/Waseel readiness is requested. See the review's evidence-gap table. |

Review coverage includes the publicly documented primary candidates and key alternatives. Where identity, private specifications, or account access is missing, the review marks a dependency instead of claiming the integration was validated.

## How to read the guide

- **User preference:** preferred for evaluation, not a signed contract or activated account.
- **Source-named:** specified in the supplied requirements document; still needs technical/account validation.
- **Proposed:** recommendation, not selected by the user.
- **Unknown:** provider identity or integration contract is missing.
- Setup effort is our planning estimate, not a provider guarantee: **Easy** means a small setup once access is available; **Medium** needs several systems or approvals; **High** involves accounting, video/storage, sensitive data, or unknown APIs. Commercial approval time is separate from coding effort.

## Current provider inventory

| Provider / service | Role in Motmaan | Current status | Configuration needed | Setup estimate / main dependency |
|---|---|---|---|---|
| Azure hosting plan | API, selected Azure SQL database, private files, secrets/monitoring and shared cache | Azure SQL Database and Azure Managed Redis selected; OpenTelemetry/Application Insights and HybridCache approved; App Service, Blob Storage and Key Vault remain proposals | Motmaan subscription, scoped access, validated region/tiers, private network/DNS, API managed identity, isolated test/live services, telemetry filtering, retention/backup and deployment pipeline | Medium to High; Saudi availability, budget and recording compatibility remain open. [Preparation guide](22-azure-hosting-and-deployment.md) |
| MyFatoorah | Selected online payment provider for app and website | **User-selected; owner reports account ready**; merchant method activation still to verify technically | Motmaan merchant/test access, account-enabled methods, checkout/return and webhook configuration, status/refund access, app/domain setup | Medium; verify required methods and the Tabby/Tamara route. [Payment integration options](https://docs.myfatoorah.com/docs/choose-your-payment-integration) and [status guidelines](https://docs.myfatoorah.com/docs/v3-updating-payment-status-guidelines) |
| Tabby | Installment-payment option | Required; owner reports integration ready for integration | Confirm MyFatoorah-mediated versus direct route, account access, allowed flows, capture/refund rules, transaction references | Medium; direct and gateway paths have different contracts. [Payment API](https://docs.tabby.ai/api-reference/payments/retrieve-a-payment) |
| Tamara | Installment-payment option | Required; owner reports integration ready for integration | Confirm MyFatoorah-mediated versus direct route, account access, transaction lifecycle/refunds and event handling | Medium; public MyFatoorah list includes Tamara but actual account activation must be checked. [Webhook documentation](https://docs.tamara.co/reference/getting-started-with-webhooks) |
| Qoyod | Accounting and official accounting/e-invoicing documents under the accepted planning recommendation | Source-named | Motmaan account/API access, customer/service mapping, tax/account configuration, external references, reconciliation process | High; finance must validate mappings and correction behavior. Public API reference alone does not establish account capabilities. [Official API](https://apidoc.qoyod.com/) |
| SMS delivery route | Patient phone OTP, doctor acceptance invitations, approved operational SMS | Required capability; user identified Wati for evaluation, actual route/account unconfirmed | See Wati below; validate Saudi sender, transactional API access, Arabic support, delivery receipts, OTP ownership and limits | High/Unknown until domestic route and API fit are confirmed; retain existing-provider question |
| Agora | Online audio/video sessions and session recording | Source-named provisional choice | Project/app identity, token/recording credentials, enabled recording product, supported storage destination and region, event/status integration | High; prove mobile/web calls and recording delivery to the exact private bucket. [Cloud Recording](https://docs.agora.io/en/realtime-media/cloud-recording) |
| Private object storage: Google Cloud Storage in Dammam | Medical files, reports, recordings, recruitment documents; isolated public media where needed | Proposed candidate; OCI Saudi is an alternative | Center-owned account, regional access/billing, buckets, limited service access, retention/backup settings, browser upload rules if needed | Medium to High; regional onboarding and recorder compatibility remain to validate. [Storage locations](https://docs.cloud.google.com/storage/docs/bucket-locations), [Dammam access](https://docs.cloud.google.com/docs/dammam-region-access) |
| Firebase Cloud Messaging, with Apple APNs setup for iOS | Backend-triggered app push: appointments, doctor-assigned tasks, tickets, approved updates | Proposed | Firebase project, Android/iOS app IDs/configuration, server access, APNs authentication/capabilities, user permission and device registration | Medium; both mobile platforms and foreground/background delivery need verification. [Flutter setup](https://firebase.google.com/docs/cloud-messaging/flutter/get-started) |
| Transactional email / existing SMTP, provider unknown | Verified email recovery/setup, closed-ticket satisfaction survey, approved documents and messages | Required capability; vendor unknown | Sending account/domain, server credentials, sender identity, domain authentication, templates, delivery/bounce handling | Easy to Medium after provider selection; domain ownership and delivery quality matter |
| Wati | WhatsApp confirmations/reminders and approved messages; SMS campaigns/fallback through documented Twilio integration | Source-named for WhatsApp; user-identified WhatsApp/SMS evaluation candidate | WABA/number, workspace/API V3 access, approved templates, authenticated events; Business plan and connected Twilio account for documented SMS path | Medium for WhatsApp; High/Unknown for Motmaan SMS until Saudi route and transactional API are verified. [API introduction](https://docs.wati.io/reference/introduction), [SMS integration](https://support.wati.io/en/articles/11694867-how-to-integrate-wati-with-twilio) |
| Existing center assessment platform, name/API unknown | Psychological tests: requests, paid access, SSO, completion and result import | User says it exists and is expected to launch this week; integrate it, technical contract unknown | [Programmer questions](18-assessment-platform-integration-questions.md): docs/sandbox, server auth, SSO, patient/family matching, catalog, order/entitlement/payment owner, signed events and result/report contracts | High/Unknown until documentation, access and sample results are available |
| Google Cloud Translation | Translate user-imported Arabic data into English while preserving Arabic | User requires translation; Google is an evaluation candidate | Cloud project, enabled API, server authentication, edition/processing endpoint, Arabic/English settings, quota/budget; approved data handling | Medium technically; health-data processing location/terms and clinical review remain unresolved. [Text API](https://docs.cloud.google.com/translate/docs/translate-text) |
| Emdaad export | Full migration of existing records and referenced files into Motmaan | Confirmed one-time migration source; replace at launch | Export/schema access, file archive/retrieval, field/ID mapping, duplicates, trial import, financial/file reconciliation, cutover plan | High; validate that every requested data category is actually exportable |

Mada and Apple Pay are payment methods within the selected payment setup, rather than additional Motmaan business backends. Apple Pay may still require its own domain/app registration steps. The owner reports the MyFatoorah account and Tabby/Tamara integrations ready; the BNPL route and enabled-method evidence still need to be recorded for the technical handoff.

Wati can coordinate WhatsApp and SMS in one platform, but its documented SMS transport depends on Twilio. Treat SMS delivery as a dependency of that option, not a second requirement to integrate directly with Twilio. Ownership and SMS OTP are confirmed; actual Motmaan Saudi route, account access, invitation support and costs remain open; see the [Wati development notes](17-provider-documentation-development-notes.md#whatsapp-and-sms-handling-wati).

## Alternatives and scope requiring clarification

| Provider / connection | Why it appears in the project | Current treatment |
|---|---|---|
| Tap Payments | Previously preferred evaluation candidate | Historical comparison only after the 7 October MyFatoorah selection. [Official setup](https://developers.tap.company/docs/get-started) |
| PayTabs | Alternative gateway researched for the required methods | Historical comparison only; no second gateway selected. [Method configuration](https://support.paytabs.com/en/support/solutions/articles/60000805455-request-parameters-payment-methods-payment-methods-) |
| Moyasar | Saudi-focused alternative with a documented Flutter SDK | Historical comparison only; public docs reviewed on 6 October did not establish Tabby/Tamara coverage. [Moyasar development notes](17-provider-documentation-development-notes.md#payment-candidate-research-moyasar--6-october-2026) |
| LiveKit / Daily | Alternatives to Agora | Evaluate only if Agora cannot meet the network/storage/operational requirements; detailed tradeoffs are in the integration note |
| OCI Object Storage | Saudi-region alternative to proposed Google storage | Confirm region, center access, recorder support, cost, and terms before selecting. [Oracle regions](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/regions.htm) |
| Daftra | Accounting fallback if Qoyod cannot meet requirements | No additional integration selected |
| NPHIES / Waseel | Future insurance capability | No current insurance. Prepare integration boundaries; live operations/contracts are explicitly future work |
| Nafath / Wasfaty | Source-named identity/prescription capabilities | Broad first-stage scope includes source-labeled later features, but exact use cases, access, and approvals still need clarification; no provider activation is authorized |

Internal staff tasks require live in-website notifications for assignment, comments, status changes, approaching deadlines, and overdue work. Notifications are retained in an unread list, including events missed while the website was closed. The delivery transport and deployment topology remain undecided; no additional external provider is selected for this capability. Patient-task mobile push remains a separate channel.

Support tickets, the internal staff-task system, wallets, compensation rules, and permissions are Motmaan modules. No external SaaS provider has been selected for those workflows. Azure Managed Redis inclusion is confirmed; the complete hosting, monitoring and backup configuration remains open under the working [Azure plan](22-azure-hosting-and-deployment.md).

## Who owns configuration

The project owner is confirmed responsible for all provider accounts. Technical delegation and detailed configuration permissions remain recommendations under the active authorization discussion; they are not approved role assignments.

| Role / team | Responsibilities |
|---|---|
| Motmaan owner / management | Own provider accounts/contracts; approve costs, business eligibility, processing arrangements, and launch readiness |
| Accountant / finance lead | Validate Qoyod mappings, taxes, payment/refund reconciliation, settlement references, and trial migration balances |
| Backend developer | Server integration, trusted status verification, data mapping, retries/deduplication, delivery tracking, authorization, branch/resource scope |
| Infrastructure administrator | Manage secrets, approved regions, private storage, access policies, callback endpoints, monitoring, backup and restore configuration |
| Flutter developer | Provider public app configuration, chosen checkout/video SDKs, device-token lifecycle, notification display, API-authorized states |
| Web frontend developer | Chosen checkout/video UI, approved domain/public configuration, permission-based settings screens, authoritative API state |
| Doctor | Control assigned patient tasks and reminder schedules; use authorized clinical/video workflows. No provider-secret access from the doctor role |
| Reception / operational staff | Use approved booking, ticket, messaging, and internal-task workflows; provider configuration requires a separate permission |
| Patient | Use approved checkout, calls, notifications, and surveys. No provider account or secret configuration |

## Make configuration manageable

**Proposed:** Keep a backend-managed integration-settings area in the management dashboard. Each integration shows its purpose, Test/Live environment, enabled state, masked configuration references, last verified connection, and recent delivery/sync failures. Settings visibility requires a specific permission; a role label alone grants no configuration access.

Separate editable business settings from secret infrastructure settings:

| Kind | Examples | Proposed location |
|---|---|---|
| Business settings | Appointment reminder lead time, approved templates, no-show grace, allowed operational notification channels | Permission-controlled management settings with audit history |
| Doctor treatment settings | Patient-task recurrence, reminder times, weekdays, start/end dates, and reminder count per day | Doctor dashboard, within assigned-patient and branch scope |
| Provider non-secret settings | Merchant/project IDs, template IDs, approved bucket/region references, callback configuration | Restricted server configuration; expose only necessary safe fields to authorized management |
| Provider secrets | Secret API keys, recording credentials, private signing keys, email/SMS credentials, storage credentials | Server secret storage; exclude from Markdown, Git, browser, mobile app, and logs |
| Client public configuration | Approved public SDK keys, Firebase app configuration, permitted app/domain IDs | Client only when the provider design permits it; never substitute a secret key |

Use separate test and production accounts/configuration. A safe connection check must clearly say what it checks; sending a real SMS/email or charging a payment is a separate action. Replacing a provider is a controlled integration change, not a dashboard dropdown that guarantees compatibility.

## Essential flows to verify before production

- **Payment:** API creates an attempt → patient uses provider checkout → backend verifies provider status → booking is confirmed exactly once → accounting sync/reconciliation. Browser/app success alone never confirms payment.
- **Recording:** Authorized session → backend starts approved recording flow → recorder delivers to the supported private bucket → backend verifies final output before marking it ready → permission-controlled playback/retention. Avoid downloading recordings to the API server merely to upload them again.
- **Patient tasks:** Doctor sets recurrence/reminders → backend schedules → push provider delivers → app opens API-authorized details. Appointment reminders remain administration-configured.
- **Tickets:** Patient/staff ticket activity → minimal push update → Closed email survey → one satisfaction submission per ticket, with optional comments and resolver attribution.
- **Migration:** Full export/files → mapped trial import → data/file and financial reconciliation → approved cutover. No Emdaad export or live migration has been performed.

Exact SDKs/API contracts, connection-check behavior, access grants, service limits, cost budgets, failure handling, and acceptance thresholds remain open. Refresh provider documentation and commercial terms when implementation begins.

Related: [decisions](06-decisions-and-open-questions.md), [question tracker](12-user-notes-and-open-questions.md), [Flutter handoff](../handoff/flutter-developer.md), [web handoff](../handoff/web-frontend-developer.md).

## Wallet and scope update — 4 October 2026

Booking by bank transfer is prohibited. Wallet bank withdrawal is separate: refund-origin funds only, request inside wallet, system administrator/accountant approval. Bank executor/API/provider and verification/reconciliation remain unknown; no additional bank provider is selected. Seven-minute checkout hold and patient changes blocked within 24 hours are current business rules and supersede earlier deferrals.

## Latest sign-in, recording and migration decisions — 4 October 2026

- Staff/doctors use username, verified email or phone number plus password. SMS additional verification is enabled by default, self-managed, and controllable for all accounts by an administrator with the relevant permission. Require the eventual SMS provider to support these backend-controlled challenges; this does not select Wati/final SMS routing. Patient OTP also uses SMS with confirmed challenge defaults. The 4 October no-account inventory predates the owner's report of a ready MyFatoorah account; the owner remains responsible for provider accounts.
- Every online consultation must be recorded for safety and performance review. Agora remains provisional and Saudi storage/processing/fallback compatibility still needs validation. Recorder readiness, consent/refusal and recorder-failure handling are now prerequisites for the mandatory-recording flow; restricted playback and one-year source retention remain in force.
- Existing data must be seeded/imported before operation. Preserve the confirmed full migration and future reconciliation/cutover checks; seeded login identifiers and account-to-patient access mapping remain open, while export-format discussion remains deferred. No seed/import or provider configuration has been executed.
