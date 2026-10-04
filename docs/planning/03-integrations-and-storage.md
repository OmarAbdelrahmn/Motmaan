# Integrations and file storage

Updated: 4 October 2026. Provider choices remain provisional unless required by the source document; source naming does not establish merchant approval, account access, or a final contract.

See [external provider guide](16-external-provider-guide.md) for each provider's purpose, configuration checklist, responsibility, selection status, and estimated setup effort. The guide is maintained alongside this integration note.

The [official provider documentation review](17-provider-documentation-development-notes.md) marks dependencies and future development checks. It adds research evidence without changing provider selections or deferred business policies.

## Providers named in the requirements

| Provider | Purpose | Backend responsibilities |
|---|---|---|
| MyFatoorah | Online payment, including enabled Mada, card, and Apple Pay methods | Checkout or payment links, verified statuses, authenticated callbacks, refunds |
| Tabby | Installment payment | Provider-specific checkout, authorization, capture where applicable, status reconciliation, cancellation and refunds |
| Tamara | Installment payment | Provider-specific checkout, authorization, capture where applicable, status notifications, cancellation and refunds |
| Qoyod | Accounting and electronic invoicing | Customer and service mapping, invoices, payment records, credit notes, receipts, reconciliation |
| Wati | WhatsApp delivery; user-identified SMS handling candidate | Templates, confirmations, reminders, payment links, treatment/assessment notifications and delivery history; evaluate documented SMS path and actual transactional API in [Wati notes](17-provider-documentation-development-notes.md#whatsapp-and-sms-handling-wati) |
| SMS delivery route | SMS messaging | Patient OTP, accepted-doctor invitations, operational messages and receipts. Wati is identified for evaluation; actual existing account and supported Saudi route remain unconfirmed |
| Translation API | Arabic-to-English translation for data imported by users | Candidate: Google Cloud Translation. Run calls server-side; preserve source text and translated text, expose machine-translation provenance, and confirm health-data privacy/residency and clinical-review requirements before enabling clinical data translation. |
| Agora | Embedded audio/video and recording | Call authorization, tokens, recording lifecycle, events, recording references |
| Center assessment platform | Psychological tests and scales | SSO, paid access, assessment requests, result import, ordering-specialist attribution |

## Payment gateway research (2 October 2026)

**Confirmed payment-method requirement from the user:** Offer mada, Apple Pay, credit/debit cards, Tabby, and Tamara together for patient checkout on both the mobile app and patient website. The user has not selected a gateway.

Official provider material reviewed for a single-gateway setup:

| Candidate | Publicly documented fit | Conditions to confirm |
|---|---|---|
| Tap Payments | Tap's Saudi pages list mada, Apple Pay, cards, Tabby, and Tamara under one regional setup. Its API docs cover mada and Apple Pay on web/mobile; its support lists Tabby for KSA and its Saudi Tamara page describes API/SDK checkout and refunds. | Obtain a Motmaan merchant quote and written confirmation that all five methods can be enabled for a Saudi healthcare/mental-health business on one merchant setup. Tabby/Tamara activation depends on eligibility and approval. |
| PayTabs | Its Saudi support and technical docs list mada, Apple Pay, cards, Tabby, and Tamara as configured payment methods available through PayTabs payment pages/API. | Mada activation requires a Saudi business account and bank approval; Tabby and Tamara require their merchant review/approval. Confirm one profile supports both BNPL methods, app and website flows, refund coverage, settlement, and fees. |

**User preference note:** Tap Payments is the current preferred gateway candidate. Evaluate PayTabs as a comparison. Public documentation indicates both can present the requested methods through one integration, but it does not establish Motmaan's merchant eligibility, final pricing, settlement schedule, or contract terms. Treat Tap as a preference, not a completed merchant/provider selection, until Motmaan gets written confirmation for its business category and all required methods. Keep payment processing behind a backend adapter. Online bookings are confirmed only after trusted provider confirmation; client redirects alone do not confirm payment.

References: [Tap Saudi payment options](https://www.tap.company/en-sa), [Tap Saudi multi-market checkout](https://www.tap.company/en-sa/products/multi-market-payments), [Tap payment methods](https://support.tap.company/en/support/solutions/articles/153000140246-accepted-payment-method-types-with-tap), [Tap Apple Pay integration](https://developers.tap.company/docs/apple-pay), [Tap mada integration](https://developers.tap.company/docs/mada), [PayTabs payment methods API](https://support.paytabs.com/en/support/solutions/articles/60000805455-request-parameters-payment-methods-payment-methods-), [PayTabs mada activation](https://support.paytabs.com/en/support/solutions/articles/60001041280), [PayTabs Tabby workflow](https://support.paytabs.com/en/support/solutions/articles/60001016783), and [PayTabs Tamara workflow](https://support.paytabs.com/en/support/solutions/articles/60001378098-tamara-activation-and-workflow).

Qoyod records accounting and issues the official accounting/e-invoicing documents under the accepted planning recommendation; payment providers collect money. Internal wallets, package entitlements, appointment states, and operational transaction records remain in Motmaan. Motmaan reliably syncs required financial events to Qoyod and stores external document references/status for reconciliation. Confirm the Qoyod account configuration, API behavior, tax setup, and finance workflow before implementation. Use an outbox/retry and idempotency approach so transient failures do not lose events or create duplicate official invoices.

**User direction supersedes the source's split-provider shortlist for required online methods:** Patient checkout must offer mada, Apple Pay, credit/debit cards, Tabby, and Tamara together. Evaluate one payment gateway integration that exposes all of them, instead of assuming MyFatoorah plus separate BNPL integrations. Gateway choice remains open; see the provider research above.

Provider callbacks or server-side status checks must confirm success before an online booking is confirmed. Store Motmaan's payment/refund transaction record, reconcile gateway events idempotently, and sync the necessary accounting details to Qoyod. Cash is accepted only at an attended in-person session. Booking by bank transfer is deferred for later discussion.

## Supporting services to select

- **User clarification / research:** Evaluate Wati for WhatsApp and SMS handling. The [Wati review](17-provider-documentation-development-notes.md#whatsapp-and-sms-handling-wati) records its documented SMS integration and Saudi delivery dependencies. Do not assume the campaign/fallback capability supplies every required transactional SMS operation. Existing SMS account/access and patient OTP channel policy remain open; acceptance SMS remains required.

- **Proposed:** Firebase Cloud Messaging for app push, with APNs setup for iOS.
- **User requirement:** Translate user-imported Arabic-language data into English using a suitable API; Google Cloud Translation is the named candidate to evaluate, not a final vendor choice. Retain the Arabic original, store translation provenance, and make clear when text is machine-translated. Before sending patient/clinical data, approve data-processing terms, data location, retention, and applicable health-data requirements. The user deferred exact formats and presentation.
- **Recommendation:** A clinician should review machine translations before relying on them in clinical decisions or approved reports. The user has not yet chosen the review workflow.

Google's official documentation describes a text translation API and states that API content is used only to provide the Cloud Translation service; the Advanced API also documents regionalized endpoints. These facts do not by themselves approve it for Motmaan health records or prove a required Saudi processing location. Verify exact data paths and contractual suitability before use.
- **Open:** Existing SMTP or a transactional email provider for email verification, account recovery, contact-change alerts, invoices, and reports.
- **Open:** Saudi-region hosting and private object storage in an account controlled by the center.

## Video alternatives

Agora is the initial candidate because the document specifies it and a managed service reduces media infrastructure work. It is not yet proven to be the best provider for the center's actual networks and retention constraints.

LiveKit is an alternative when center-controlled hosting is important. Self-hosting requires operating media connectivity, TURN, capacity, monitoring, and a separate recording component. Daily is a managed alternative with documented delivery into customer-owned Amazon S3; verify fit with the chosen location and infrastructure.

Run a small proof of concept across intended clients: join, interruption and reconnection, recording, delivery to the exact bucket, finalization, and restricted playback. Compare reliability, latency, processing locations, supported storage, and total call plus recording plus storage cost.

## Storage shortlist

| Candidate | Confirmed public capability | Remaining check |
|---|---|---|
| Google Cloud Storage in Dammam, me-central2 | Documented Saudi object-storage location; KSA billing goes through CNTXT | Recorder compatibility, access, regional configuration, terms, and cost |
| Oracle OCI Object Storage in Riyadh or Jeddah | Operating Saudi regions and managed object storage | Recorder compatibility, access, configuration, terms, and cost |

Our proposed starting candidate is Google Cloud Storage in Dammam under the center's account. This is conditional on successful direct recording delivery and confirmation of the processing/storage arrangement. Agora's current reference documents an S3-compatible storage option; that does not establish compatibility with every destination or the particular proposed OCI Saudi bucket. Verify the exact endpoint, credentials, and recording output. See the [storage configuration review](17-provider-documentation-development-notes.md#online-sessions-and-recording-agora).

Cloud storage in the center's account is the interpretation discussed for center-controlled storage. Obtain clarity on whether the source's prohibition on third-party storage means no provider-owned retained recordings or requires physically center-owned infrastructure. Saudi storage alone does not establish the location of live-media processing or temporary recording backup.

## File ownership and access

| Data | Proposed location |
|---|---|
| Patients, diagnoses, appointments, finance | Relational database |
| Medical attachments, prescriptions, reports | Private medical-files bucket |
| Session recordings and their output assets | Separate private recordings bucket |
| Public profiles and service images | Public-media bucket or separately controlled public delivery |
| Owner, patient or appointment link, object key, size, type, checksum, status, retention due date | Database metadata |

Private file requests pass through API authorization. Issue a short-lived URL only after checking the specific resource, and record access grants and available playback/storage access events. Keep credentials on the server, use generated object keys without patient identifiers, validate uploads, and quarantine uploaded content for scanning.

Recording retention is one year in the source. Coordinate lifecycle deletion with versions, replicas, and backup policies so deleted recordings are not unintentionally retained or restored. Medical documents need a separately agreed retention policy. Object-storage durability does not replace a recovery plan for accidental deletion or database/file consistency.

## Additional connections and scope dependencies

- Insurance scope, including actual NPHIES/Waseel exchange, remains explicitly user-deferred. Wasfaty and Nafath source requirements are included in the user's broad first-stage direction, but exact use cases, onboarding, and API access remain unresolved. Source wording about separate approval does not override the latest user scope decision or authorize provider activation.
- Daftra is an alternative to Qoyod if its APIs cannot meet the requirements.
- ICD-10 and medication catalogs can be maintained as imported reference datasets; confirm source, license, and update process.
- Calendar addition can use export or native calendar support; full synchronization needs a separate definition.
- Google reviews use a link. Bank transfers use staff verification in the source. Neither requires an additional live API by default.
- Emdaad is a migration source, not a proposed ongoing live integration.

## Integration prerequisites

Obtain account ownership, API documentation, sandbox credentials, enabled products, callback setup, limits, reconciliation behavior, and example transactions. Prioritize SMS, the preferred Tap gateway evaluation (all required methods), Qoyod, assessments, Agora, and compatible private storage. MyFatoorah remains source-named; no additional gateway is automatically required. Avoid sending private source-document content to providers during this planning stage.

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
