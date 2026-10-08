# Integrations and file storage

Updated: 8 October 2026. MyFatoorah is the user-selected online payment provider and its account is reported ready by the owner. Other provider choices remain provisional except explicit user decisions; reported readiness does not establish a tested production flow.

See [external provider guide](16-external-provider-guide.md) for each provider's purpose, configuration checklist, responsibility, selection status, and estimated setup effort. The guide is maintained alongside this integration note.

The [official provider documentation review](17-provider-documentation-development-notes.md) marks dependencies and future development checks. It adds research evidence without changing provider selections or deferred business policies.

## Providers named in the requirements

| Provider | Purpose | Backend responsibilities |
|---|---|---|
| MyFatoorah | Selected online payment provider for patient app and website | Create payment attempts/checkout, verify statuses and authenticated callbacks, reconcile and process refunds; confirm account-enabled methods |
| Tabby | Required installment method; owner reports integration ready | Confirm whether MyFatoorah exposes it or a direct connection is required; then define checkout, authorization/capture, reconciliation, cancellation and refunds |
| Tamara | Required installment method; owner reports integration ready | Confirm whether MyFatoorah exposes it or a direct connection is required; then define checkout, authorization/capture, notifications, cancellation and refunds |
| Qoyod | Accounting and electronic invoicing | Customer and service mapping, invoices, payment records, credit notes, receipts, reconciliation |
| Wati | WhatsApp delivery; user-identified SMS handling candidate | Templates, confirmations, reminders, payment links, treatment/assessment notifications and delivery history; evaluate documented SMS path and actual transactional API in [Wati notes](17-provider-documentation-development-notes.md#whatsapp-and-sms-handling-wati) |
| SMS delivery route | SMS messaging | Patient OTP, accepted-doctor invitations, operational messages and receipts. Wati is identified for evaluation; actual existing account and supported Saudi route remain unconfirmed |
| Translation API | Multilingual representations of suitable user-entered display data | Candidate: Google Cloud Translation, not selected. Preserve originals and derive appropriate translated/transliterated display values for the selected interface language; see the owning multilingual section below. Sensitive-data processing requires approval. |
| Agora | Embedded audio/video and recording | Call authorization, tokens, recording lifecycle, events, recording references |
| Center assessment platform | Psychological tests and scales | SSO, paid access, assessment requests, result import, ordering-specialist attribution |

## Online payment selection (7 October 2026)

**Confirmed:** Use [MyFatoorah](https://www.myfatoorah.com/) for online payment. Offer mada, Apple Pay, credit/debit cards, Tabby and Tamara on both the mobile app and patient website. The owner reports the MyFatoorah account and Tabby/Tamara integrations ready. Obtain technical merchant/test access and the account-enabled method list, and establish whether each BNPL method uses MyFatoorah or a direct provider connection. Do not infer that Tabby is MyFatoorah-enabled from the readiness report. [MyFatoorah's published method list](https://docs.myfatoorah.com/docs/choose-your-payment-integration) includes Tamara and says availability is account-dependent; it does not establish Tabby on Motmaan's account.

MyFatoorah's [webhook V2 documentation](https://docs.myfatoorah.com/docs/webhook-v2) and [payment-status guidance](https://docs.myfatoorah.com/docs/v3-updating-payment-status-guidelines) support authenticated event handling and server-side status retrieval. Keep one Motmaan payment attempt and refund record per logical operation, reconcile duplicate/out-of-order events, and confirm bookings only from trusted backend-verified success. Agree the seven-minute hold and late-payment/refund behavior before implementation. Provider checkout/SDK version, method lifecycle, settlement and refund ownership remain open.

### Earlier gateway research (historical comparison, 2–6 October 2026)

Official provider material reviewed for a single-gateway setup:

| Candidate | Publicly documented fit | Conditions to confirm |
|---|---|---|
| Tap Payments | Tap's Saudi pages list mada, Apple Pay, cards, Tabby, and Tamara under one regional setup. Its API docs cover mada and Apple Pay on web/mobile; its support lists Tabby for KSA and its Saudi Tamara page describes API/SDK checkout and refunds. | Obtain a Motmaan merchant quote and written confirmation that all five methods can be enabled for a Saudi healthcare/mental-health business on one merchant setup. Tabby/Tamara activation depends on eligibility and approval. |
| PayTabs | Its Saudi support and technical docs list mada, Apple Pay, cards, Tabby, and Tamara as configured payment methods available through PayTabs payment pages/API. | Mada activation requires a Saudi business account and bank approval; Tabby and Tamara require their merchant review/approval. Confirm one profile supports both BNPL methods, app and website flows, refund coverage, settlement, and fees. |

**Historical note:** Tap was previously preferred for evaluation, with PayTabs as comparison and Moyasar later researched. The 7 October MyFatoorah decision supersedes that preference. Preserve this research for reference; do not treat its candidate assumptions as the current integration plan. Keep payment processing behind a backend boundary. Client redirects alone do not confirm payment.

References: [Tap Saudi payment options](https://www.tap.company/en-sa), [Tap Saudi multi-market checkout](https://www.tap.company/en-sa/products/multi-market-payments), [Tap payment methods](https://support.tap.company/en/support/solutions/articles/153000140246-accepted-payment-method-types-with-tap), [Tap Apple Pay integration](https://developers.tap.company/docs/apple-pay), [Tap mada integration](https://developers.tap.company/docs/mada), [PayTabs payment methods API](https://support.paytabs.com/en/support/solutions/articles/60000805455-request-parameters-payment-methods-payment-methods-), [PayTabs mada activation](https://support.paytabs.com/en/support/solutions/articles/60001041280), [PayTabs Tabby workflow](https://support.paytabs.com/en/support/solutions/articles/60001016783), and [PayTabs Tamara workflow](https://support.paytabs.com/en/support/solutions/articles/60001378098-tamara-activation-and-workflow).

Qoyod records accounting and issues the official accounting/e-invoicing documents under the accepted planning recommendation; payment providers collect money. Internal wallets, package entitlements, appointment states, and operational transaction records remain in Motmaan. Motmaan reliably syncs required financial events to Qoyod and stores external document references/status for reconciliation. Confirm the Qoyod account configuration, API behavior, tax setup, and finance workflow before implementation. Use an outbox/retry and idempotency approach so transient failures do not lose events or create duplicate official invoices.

The earlier one-gateway evaluation assumption is superseded by the selected MyFatoorah provider and the owner's Tabby/Tamara readiness report. A single checkout is preferred where the actual account supports it, but the BNPL connection path has not been stated. Do not create duplicate direct and gateway captures or refunds for the same purchase.

Provider callbacks or server-side status checks must confirm success before an online booking is confirmed. Store Motmaan's payment/refund transaction record, reconcile gateway events idempotently, and sync the necessary accounting details to Qoyod. Cash is accepted only at an attended in-person session. Booking by bank transfer is not allowed.

## Supporting services to select

- **User clarification / research:** Evaluate Wati for WhatsApp and SMS handling. The [Wati review](17-provider-documentation-development-notes.md#whatsapp-and-sms-handling-wati) records its documented SMS integration and Saudi delivery dependencies. Do not assume the campaign/fallback capability supplies every required transactional SMS operation. Existing SMS account/access and Saudi transactional route remain open. Patient authentication is confirmed SMS; acceptance SMS remains required. AUD-04 records a possible specialist Saudi SMS provider without selecting one or replacing Wati. Verify OTP, sender registration, Arabic content, delivery receipts and route reliability before production.

- **Proposed:** Firebase Cloud Messaging for app push, with APNs setup for iOS.
- **Confirmed AUD-16:** Display suitable dynamic data in the selected system language, beyond clinical/imported text; preserve canonical originals. The owning multilingual section below defines field-sensitive translation/transliteration. Google Cloud Translation remains a candidate; vendor, approved processing and exact file formats remain open.
- **Recommendation:** A clinician should review machine translations before relying on them in clinical decisions or approved reports. The user has not yet chosen the review workflow.

Google's official documentation describes a text translation API and states that API content is used only to provide the Cloud Translation service; the Advanced API also documents regionalized endpoints. These facts do not by themselves approve it for Motmaan health records or prove a required Saudi processing location. Verify exact data paths and contractual suitability before use.
- **Open:** Existing SMTP or a transactional email provider for email verification, account recovery, contact-change alerts, invoices, and reports.
- **Confirmed AUD-05:** Microsoft Azure hosting with Qatar Central as the interim regional direction and a suitable verified Saudi region preferred long term; Azure SQL stays selected. Production patient-data transfer to Qatar requires residency/privacy/regulatory/contractual and cross-border checks. Final private storage/service compatibility remains open; [Azure document](22-azure-hosting-and-deployment.md) owns the blocker and migration gates.

## Video alternatives

Agora is the initial candidate because the document specifies it and a managed service reduces media infrastructure work. It is not yet proven to be the best provider for the center's actual networks and retention constraints.

LiveKit is an alternative when center-controlled hosting is important. Self-hosting requires operating media connectivity, TURN, capacity, monitoring, and a separate recording component. Daily is a managed alternative with documented delivery into customer-owned Amazon S3; verify fit with the chosen location and infrastructure.

Run a small proof of concept across intended clients: join, interruption and reconnection, recording, delivery to the exact bucket, finalization, and restricted playback. Compare reliability, latency, processing locations, supported storage, and total call plus recording plus storage cost.

## Storage shortlist

The current discussion considers an Azure plan with private Blob Storage. **Azure SQL Database (SQL Server)** is selected and **Azure Managed Redis** is confirmed as its fifth service; the storage service, full topology and regional configuration still need finalization. See [Azure hosting and deployment preparation](22-azure-hosting-and-deployment.md). Earlier GCS/OCI proposals remain alternatives, not simultaneous storage requirements.

| Candidate | Confirmed public capability | Remaining check |
|---|---|---|
| Private Azure Blob Storage in the proposed Azure plan | Azure documents authorized/private containers; this research does not establish Saudi service availability or Agora compatibility | Exact region/service access, recorder credentials and ingestion network, processing/fallback locations, client upload/playback, terms and cost |
| Google Cloud Storage in Dammam, me-central2 | Documented Saudi object-storage location; KSA billing goes through CNTXT | Recorder compatibility, access, regional configuration, terms, and cost |
| Oracle OCI Object Storage in Riyadh or Jeddah | Operating Saudi regions and managed object storage | Recorder compatibility, access, configuration, terms, and cost |

The earlier proposed starting candidate was Google Cloud Storage in Dammam under the center's account. The current Azure discussion adds Blob Storage for evaluation; no final storage selection follows from confirming Redis. Any destination is conditional on successful direct recording delivery and confirmation of the processing/storage arrangement. Agora's current reference documents an S3-compatible storage option; that does not establish compatibility with every destination or the particular proposed OCI Saudi bucket. Verify the exact endpoint, credentials, and recording output, including any proposed Azure delivery path. See the [storage configuration review](17-provider-documentation-development-notes.md#online-sessions-and-recording-agora).

Cloud storage in the center's account is the interpretation discussed for center-controlled storage. Obtain clarity on whether the source's prohibition on third-party storage means no provider-owned retained recordings or requires physically center-owned infrastructure. Saudi storage alone does not establish the location of live-media processing or temporary recording backup.

## File ownership and access

| Data | Proposed location |
|---|---|
| Patients, diagnoses, appointments, finance | Relational database |
| Medical attachments, prescriptions, reports | Private medical-files bucket |
| Session recordings and their output assets | Separate private recordings bucket |
| Public profiles and service images | Public-media bucket or separately controlled public delivery |
| Owner, patient or appointment link, object key, size, type, checksum, status, retention due date | Database metadata |

Private file requests pass through current API authorization. Choose delivery controls per data class; signed URLs alone are not sufficient for every sensitive document/recording. Check the specific resource and record grants and available access events; evaluate revocation, network restrictions and playback control. Keep credentials on the server, use generated object keys without patient identifiers, validate uploads, and quarantine uploaded content for scanning.

Recording retention is one year in the source. Coordinate lifecycle deletion with versions, replicas, and backup policies so deleted recordings are not unintentionally retained or restored. Medical documents need a separately agreed retention policy. Object-storage durability does not replace a recovery plan for accidental deletion or database/file consistency.

## Secure file lifecycle — AUD-23

**Confirmed:** Apply the [authoritative resumable transfer/recovery design](04-online-sessions.md#confirmed-resumable-transfer-and-recovery--aud-06) to supported file uploads and relevant recording ingestion. At 48% interruption, resume from the last verified server-committed part; persist upload state/session identity across restart, validate parts and final integrity, deduplicate requests, retry safely and report progress/failures accurately. Track authorized ownership/scope from upload creation through finalization and processing, cancellation/cleanup, access, retention and recovery.

Scope both upload and subsequent download access; quarantine/scan where required before releasing untrusted files. Credential refresh and resume must recheck access, not restore revoked privileges. Use lifecycle-appropriate encryption, audit and recovery controls. Signed delivery must be evaluated against revocation, network and sensitive playback requirements. Retention for medical/recruitment files and recovery/deletion details remain owner/security dependencies; recording retains its existing one-year requirement.

Video uses [recording processing and adaptive streaming](04-online-sessions.md#confirmed-processing-and-adaptive-playback--aud-06). Ordinary PDFs/images require validation and appropriate processing, **not** video transcoding or adaptive bitrate streaming. Recruitment, ticket and staff-task attachments inherit these reliability/security principles without inheriting clinical access. Future acceptance includes disconnect/resume, restart, duplicate/corrupt/missing parts, expired grants, denied access and cleanup/recovery; see document 04 for the shared scenarios.

## Multilingual display data — AUD-16

**Confirmed:** Preserve the original user-entered value and select an appropriate display representation according to the user's current Arabic/English interface language, consistently across Web and Flutter. This covers relevant dynamic display data, not just fixed labels, imported content or medical records. For example, an Arabic-entered name displays in Arabic in the Arabic interface and with an appropriate English representation in the English interface.

Use transliteration for names rather than translating the meaning of their words. Choose translation or localization by field type; do not blindly translate identity numbers, reference codes, phone numbers or financial identifiers. Allow approved manual corrections to derived representations where needed. A reusable approach should store/cache derived values with source/language/provenance tracking where appropriate, avoid unnecessary repeated requests, and keep the canonical source intact. Exact contracts/storage mechanics remain developer work.

Suitable clinical text still needs privacy and medical safety/review controls; this decision does not authorize changing clinical meaning or sending sensitive data to an unapproved provider. Google Cloud Translation remains an evaluation candidate, not a selected transliteration solution or approved health-data processor. Exact file/content-format scope, vendor and clinical-review procedure remain open; display-language behavior itself is resolved.

## Additional connections and scope dependencies

- **Confirmed:** No insurance in the current release. Prepare the system for future NPHIES/Waseel integration; live eligibility/approval/claims and provider activation are explicitly future work, with operations/contracts undecided. Wasfaty and Nafath source requirements are included in the user's broad first-stage direction, but exact use cases, onboarding, and API access remain unresolved. Source wording about separate approval does not override the latest user scope decision or authorize provider activation.
- Daftra is an alternative to Qoyod if its APIs cannot meet the requirements.
- ICD-10 and medication catalogs can be maintained as imported reference datasets; confirm source, license, and update process.
- Calendar addition can use export or native calendar support; full synchronization needs a separate definition.
- Google reviews use a link. Bank-transfer bookings appear in the source but are now prohibited by the user. Wallet bank payouts are a separate confirmed request/approval workflow; their execution channel remains undecided.
- Emdaad is a migration source, not a proposed ongoing live integration.

## Integration prerequisites

Obtain account ownership, API documentation, sandbox credentials, enabled products, callback setup, limits, reconciliation behavior, and example transactions. Prioritize SMS, MyFatoorah and the reported ready Tabby/Tamara integrations, Qoyod, assessments, Agora, and compatible private storage. Establish the exact BNPL connection and responsibility boundary before designing duplicate integrations. Avoid sending private source-document content to providers during this planning stage.

## References

- [MyFatoorah payment verification](https://docs.myfatoorah.com/docs/v3-updating-payment-status-guidelines)
- [Tabby payment API](https://docs.tabby.ai/api-reference/payments/retrieve-a-payment)
- [Tamara webhooks](https://docs.tamara.co/reference/getting-started-with-webhooks)
- [Qoyod API](https://apidoc.qoyod.com/)
- [Wati template messaging](https://docs.wati.io/reference/sendtemplatemessage)
- [Firebase Cloud Messaging](https://firebase.google.com/docs/cloud-messaging)
- [Azure Translator](https://learn.microsoft.com/en-us/azure/ai-services/translator/overview)
- [Google Cloud Translation API](https://docs.cloud.google.com/translate/docs/translate-text)
- [Google Cloud Translation data usage](https://docs.cloud.google.com/translate/data-usage)
- [Google storage locations](https://docs.cloud.google.com/storage/docs/bucket-locations)
- [Dammam purchasing and access](https://docs.cloud.google.com/docs/dammam-region-access)
- [Oracle regions](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/regions.htm)
- [LiveKit self-hosting](https://docs.livekit.io/transport/self-hosting/)
- [Daily customer-owned recording storage](https://docs.daily.co/guides/products/live-streaming-recording/storing-recordings-in-a-custom-s3-bucket)

## Existing assessment platform and future insurance — 4 October 2026

- The user reports that the assessment platform already exists and is expected to launch this week. Integrate it with Motmaan rather than recreate it. Name, URL, API/SSO, result and payment contracts are still unknown; clarification is now requested from its programmer, replacing the earlier discussion deferral. The [Arabic integration questions](18-assessment-platform-integration-questions.md) are ready to forward.
- Prepare for future NPHIES/Waseel capability without enabling insurance in the present release. Proposed planning boundary: keep patient/beneficiary identity, provider references and financial ownership explicit, with a future adapter boundary; detailed schemas and insurance-specific operations should await verified contracts. No implementation is authorized.
- Wallet bank withdrawal is distinct from prohibited booking by transfer: service-refund balance only, request inside wallet, approval by system administrator or accountant. The actual bank channel/API, execution operator, verification, statuses, and reconciliation are still open.
