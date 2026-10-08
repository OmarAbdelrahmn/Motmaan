# Provider documentation: important points for future development

Reviewed: 4 October 2026; MyFatoorah sources revisited 7 October 2026. **Planning research only.** Official public documentation was reviewed from the links in the [provider guide](16-external-provider-guide.md), with related official references where needed. No provider account, private API, payment, message, or integration was tested.

**Documented** describes provider behavior in the cited public reference. **Recommendation** is a proposed Motmaan development safeguard. **Open** requires account-specific evidence or a project decision. Research does not select providers, approve health-data processing, answer deferred business questions, or authorize implementation. Recheck versions, limits, and merchant configuration when development starts.

## Current account inventory clarification

After the earlier public-documentation review, the owner reported no external-provider accounts available as of 4 October and retained responsibility for all accounts. On 7 October the owner reported the MyFatoorah account and Tabby/Tamara integrations ready; credential access, enabled methods and successful integration remain to document technically. [Provider setup questions P01–P12](16-external-provider-guide.md) track the remaining evidence. Staff login is username/verified email/phone plus password, with default-on self-managed SMS verification and authorized administrator control; patient OTP uses SMS with the confirmed six-digit/five-minute/60-second/five-attempt defaults; the SMS route remains unselected and untested. Public provider documentation does not resolve the remaining authentication/authorization policies.

## Priority markers

| Marker | Meaning |
|---|---|
| **P1 — dependency** | Resolve before committing to the affected provider or workflow; could change scope, cost, data handling, or architecture. |
| **P2 — development** | Carry into implementation contracts and verification after implementation is authorized. |

## Payment: MyFatoorah — selected 7 October 2026

**User decision:** MyFatoorah is the online payment provider. The owner reports Tabby and Tamara integrations ready for integration. This does not specify whether those methods are connected through MyFatoorah or directly, and no account-specific transaction has been verified in this documentation review.

- **Documented / P1:** MyFatoorah lists mada, Apple Pay, cards and Tamara among its payment methods, while noting that availability depends on the account and agreement. Tabby was not established by the published method list reviewed here. Obtain the enabled methods for Motmaan and the intended Tabby/Tamara route. [Integration options and method list](https://docs.myfatoorah.com/docs/choose-your-payment-integration).
- **Documented / P2:** Webhook V2 uses a required secret/signature and supports payment and refund status events. MyFatoorah advises combining authenticated webhooks with server-side payment-status retrieval; redirects can be lost and duplicate events can occur. Use provider-verified state for booking confirmation and idempotent reconciliation. [Webhook V2](https://docs.myfatoorah.com/docs/webhook-v2), [status guidelines](https://docs.myfatoorah.com/docs/v3-updating-payment-status-guidelines).
- **Open / P1:** Confirm account/test/live access, supported checkout pattern for both clients, seven-minute hold compatibility, late successful payments, capture and refund paths for each enabled method, settlement references, and whether MyFatoorah or a direct BNPL integration owns each operation. Do not issue both gateway and direct captures/refunds for one order.

### Historical comparison: Tap Payments

Status: previously preferred evaluation candidate; superseded by the MyFatoorah selection.

- **Documented / P2:** Test/live public and secret keys are separate. Secret keys belong on the backend. Web SDK domains and mobile bundle IDs require registration. Hosted checkout and tokenization are different integration paths; authorization is not supported by every method. [Tap setup](https://developers.tap.company/docs/get-started).
- **Documented / P2:** Webhooks use `post.url`; validate `hashstring` with HMAC-SHA256 over Tap's specified field sequence. Amount formatting matters: SAR uses two decimal places. This is not a generic hash of the raw JSON body. [Webhook verification](https://developers.tap.company/docs/webhook).
- **Documented / P2:** `reference.idempotent` protects charge/authorization/refund retries for **24 hours**. [Idempotency](https://developers.tap.company/docs/idempotency).
- **Recommendation / P2:** Persist one key per logical payment attempt or refund operation, reuse it for retries, and retain local duplicate protection beyond the provider window. A deliberate new attempt needs a distinct identity and reconciliation of the earlier attempt. Verify merchant, environment, amount, currency, and Motmaan reference before changing booking state.
- **Documented / P2:** Full/partial refunds exist. `PENDING` or `ACCEPTED` is not `REFUNDED`; the documented refund-v2 logic requires support activation and is marked beta. [Refund lifecycle](https://developers.tap.company/reference/refunds).
- **Open / P1:** Obtain written all-method approval for Motmaan's business category, enabled refund lifecycle, fees, settlements, SDK coverage, and Tabby/Tamara capture handling through Tap. Motmaan's slot hold is now confirmed as seven minutes; align the provider flow with that deadline and define late-payment handling.

**Future verification:** Duplicate taps; lost redirect; invalid signature; SAR amount formatting; timeout followed by retry; retry after 24 hours; partial refund; accepted refund that later fails; payment arriving after a slot is released. The last scenario requires an explicit resolution policy.

## Payment candidate research: Moyasar — 6 October 2026

Status: historical researched comparison candidate only. Public pages and developer documentation were reviewed; no Motmaan account, merchant approval, sandbox transaction, or integration was tested.

- **Documented / P2:** Moyasar advertises mada, Visa, Mastercard, American Express, Apple Pay and Samsung Pay, with STC Pay also listed in its FAQ and developer overview. It offers a Flutter SDK for cards, Apple Pay, Samsung Pay and STC Pay, as well as web checkout options. Confirm the exact required mada/debit behavior and method availability for Motmaan's account and each client. [Methods and FAQ](https://moyasar.com/en/resources/faqs/), [Flutter SDK](https://docs.moyasar.com/sdk/flutter/installation), [developer overview](https://docs.moyasar.com/).
- **Documented / P2:** Payment creation supports a merchant-supplied `given_id` for idempotency; payment operations include retrieval, capture, void and full/partial refunds. Webhooks include paid, failed, authorized, captured, voided and refunded events. Verify event authentication and reconcile provider status server-side before confirming a booking. [Create payment](https://docs.moyasar.com/api/payments/01-create-payment), [payment operations](https://docs.moyasar.com/guides/payment-operations), [webhook events](https://docs.moyasar.com/api/other/webhooks/available-webhooks).
- **Documented / P1:** Moyasar says its service currently focuses on Saudi Arabia, offers sandbox exploration, and requires sales activation for live payments. Fees are quoted by sales; advertised approval timing is not a Motmaan commitment. [FAQ and activation](https://moyasar.com/en/resources/faqs/).
- **Open / P1:** Public materials reviewed did not establish Tabby or Tamara as available Moyasar payment methods. Since both are required on the patient app and website, obtain written confirmation that Moyasar can provide both under one Motmaan merchant setup, including healthcare eligibility, settlement, capture, cancellation and refund responsibility. If not, it does not meet the current one-gateway evaluation requirement without changing scope or adding another integration.
- **Open / P1:** Request Motmaan-specific merchant eligibility, all-method activation, commercial fees, settlement timing/reserves, dispute process, refund constraints, and confirmation that the clinical-services business model is acceptable. Public PCI/regulatory statements do not establish Motmaan's account approval or compliance obligations.

**Historical assessment:** This candidate has a documented Flutter path and payment lifecycle controls, but its Tabby/Tamara coverage and merchant approval were unconfirmed. MyFatoorah is now selected; revisit this comparison only if the provider plan changes.

## Installments: Tabby

Status: required method; owner reports integration ready. MyFatoorah-mediated versus direct connection remains to be specified.

- **Documented / P1:** Direct Saudi integrations use **`https://api.tabby.sa`** for all calls. Examples using `api.tabby.ai` must not be copied indiscriminately; cross-region routing is incomplete. Test/live behavior is determined by keys. [Regional API hosts](https://docs.tabby.ai/api-reference/overview).
- **Documented / P2:** Capture applies to authorized payments; partial capture leaves the payment authorized until completed or closed. Capture/refund requests expose operation `reference_id` values for idempotency. [Capture](https://docs.tabby.ai/api-reference/payments/capture-a-payment), [refund](https://docs.tabby.ai/api-reference/payments/refund-a-payment).
- **Documented / P2:** Webhooks use lowercase statuses; retrieval uses uppercase. An `authorized` notification can contain capture confirmation, and a refund may retain `closed` status. Inspect capture/refund records as well as status. Registration is per merchant-code/key pair, with an optional configured authentication header. Only HTTP 200 acknowledges delivery; duplicate and unordered delivery is possible, with finite retries. [Payment webhooks](https://docs.tabby.ai/pay-in-4-custom-integration/webhooks).
- **Recommendation / P2:** Authenticate, durably retain required event data, deduplicate, and prevent state regression. An unmatched event needs retry or durable recovery; do not acknowledge and discard it. Do not trigger another capture from capture confirmation.
- **Open / P1:** Establish whether MyFatoorah exposes Tabby for Motmaan or whether the ready integration is direct; assign capture timing, refunds, disputes, required fields and eligibility accordingly. Direct Tabby rules do not prove a MyFatoorah contract.

**Future verification:** Saudi retrieval/refund endpoint; capture event before authorization event; webhook before local commit; duplicate capture/refund; declined eligibility; partial capture and refund reconciliation.

## Installments: Tamara

Status: required method; owner reports integration ready. MyFatoorah-mediated versus direct connection remains to be specified.

- **Documented / P2:** Direct integration has sandbox/production base URLs and separate API, notification, and public widget credentials. Verify the `tamaraToken` JWT using the notification token and HS256; decoding alone does not establish authenticity. [API setup and notification authentication](https://docs.tamara.co/reference/tamara-api-reference-documentation).
- **Documented / P2:** HTTPS webhooks distinguish approved, authorised, captured, canceled, refunded, declined, and expired orders, with separate operation IDs and amounts. [Webhook events](https://docs.tamara.co/reference/getting-started-with-webhooks).
- **Documented / P1:** The authorise endpoint follows approval unless the merchant's supported auto-authorisation flow is enabled. The reference documents auto-capture after **21 days** from authorisation if capture has not occurred. [Authorise order](https://docs.tamara.co/reference/authoriseorder).
- **Recommendation / P2:** Store order and operation references, validate token and transaction identity, and map provider states explicitly. Approval, capture, and settlement must not collapse into one generic success flag.
- **Open / P1:** Confirm the MyFatoorah-mediated or direct lifecycle, auto-authorisation/capture configuration, healthcare eligibility, package/advance-booking behavior, and refund handling. Do not add direct Tamara calls alongside MyFatoorah without an agreed responsibility boundary.

**Future verification:** Forged token; duplicate approval; authorisation timeout; delayed capture; auto-capture boundary; partial refund; canceled/expired checkout; the same order arriving through multiple event paths.

## Accounting: Qoyod

Status: source-named; accepted planning recommendation assigns official accounting/e-invoicing documents to Qoyod.

- **Documented / P2:** The public API uses an `API-KEY` header and includes customers, products, invoices, invoice payments, credit notes, receipts, and journal entries. Invoice examples contain line-item product/unit/tax/discount fields and payment references. Index endpoints support search/sort, defaulting to ascending ID. [Qoyod API](https://apidoc.qoyod.com/).
- **Recommendation / P2:** Agree customer/service/account/tax mappings with finance; retain local-to-Qoyod references and separate operational success from accounting-sync status. Persist accounting work reliably with the financial transaction, process with bounded retries, and reconcile an ambiguous remote creation before repeating it. Never hold a database transaction across Qoyod calls.
- **Open / P1:** Verify account API entitlement, test environment, quotas/pagination, reference uniqueness/idempotency guarantees, invoice issuance versus draft behavior, tax/e-invoice configuration, correction/credit-note operations, and reconciliation ownership. Public resources alone do not prove Motmaan's account is ready for official issuance.

**Future verification:** Paid booking while Qoyod is down; timeout after invoice creation; duplicate financial event; discounts/VAT/refunds/package allocation; cash receipt; daily reconciliation of amounts and external references.

## Online sessions and recording: Agora

Status: source-named provisional choice; exact storage and processing arrangement unverified.

- **Documented / P1:** Cloud Recording supports customer cloud storage and automatic backup on Agora servers when the destination fails. [Recording overview](https://docs.agora.io/en/realtime-media/cloud-recording).
- **Documented / P1:** The current storage reference lists Google Cloud with `vendor=6`, `region=0`; it also lists an S3-compatible path with `vendor=11`, `region=0`, and `extensionParams.endpoint`. These recorder values do not select a Saudi processing location. S3 compatibility is a documented option, but does not establish compatibility with a particular OCI bucket. [Storage configuration](https://docs.agora.io/en/realtime-media/cloud-recording/reference/region-vendor).
- **Documented / P2:** Event 31 means all recording files reached specified storage. Event 32 means at least one file used Agora Cloud Backup. Signature headers distinguish HMAC-SHA1 and HMAC-SHA256 verification; use the algorithm matching the selected header. [Recording notifications](https://docs.agora.io/en/realtime-media/cloud-recording/build/handle-events/receive-notifications).
- **Confirmed AUD-06 / engineering follow-up P2:** keep media unavailable for playback until complete verified assets, retryable processing/renditions and manifest validation; track every asset, recorder attempt, and identifier. Apply appointment/branch authorization before call-token issuance and independent recording-playback permission before playback URLs. See the existing [recording workflow](04-online-sessions.md).
- **Open / P1:** Prove direct upload to the exact Saudi private bucket, credential compatibility, temporary/fallback storage and processing locations, consent/start policy, and whether backup behavior meets center-controlled retention requirements.

**Future verification:** Mobile/web reconnection; duplicate start; start timeout with remote success; destination failure; event 32 without local assets; delayed finalization; unauthorized playback; missing HLS segment; deletion of all assets.

## Private storage: Google Cloud Storage and OCI alternative

Status: Dammam GCS proposed; Saudi OCI alternative.

- **Documented / P1:** Google lists Dammam `me-central2`; KSA billing addresses purchase Google Cloud through CNTXT. Oracle lists Riyadh `me-riyadh-1` and Jeddah `me-jeddah-1`. Region existence is not proof of account access or recorder compatibility. [Google locations](https://docs.cloud.google.com/storage/docs/locations), [Dammam access](https://docs.cloud.google.com/docs/dammam-region-access), [Oracle regions](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/regions.htm).
- **Documented / P2:** Google signed URLs grant whoever possesses them temporary access; they are not a replacement for Motmaan authorization. [Signed URLs](https://docs.cloud.google.com/storage/docs/access-control/signed-urls).
- **Documented / P1:** New buckets normally receive a **seven-day soft-delete policy**; deleted content can remain recoverable until it expires. [Soft delete](https://docs.cloud.google.com/storage/docs/soft-delete).
- **Recommendation / P2:** Resolve permanent deletion semantics alongside one-year recording retention, versions, replicas, soft delete, and backup restore. Keep private medical/recruitment objects separate from public media; issue short-lived scoped access and verify every HLS asset. Validate upload type/size and quarantine untrusted files.
- **Open / P1:** Center account onboarding, bucket and processing locations, recorder authentication, cost/egress budget, retention starting instant, recovery period, and final deletion evidence. Do not enable irreversible retention locks before agreeing the policy.

**Future verification:** Cross-patient/branch denial; expired and shared URL behavior; oversized/unsafe upload; lifecycle expiry including versions and recoverable copies; restoring backups without reintroducing expired recordings.

## Mobile push: Firebase Cloud Messaging / APNs

Status: proposed, not selected.

- **Documented / P2:** Flutter iOS setup needs push/background capabilities and an uploaded APNs authentication key. APNs token availability matters before FCM API calls; subscribe to `onTokenRefresh`. [Flutter setup](https://firebase.google.com/docs/cloud-messaging/flutter/get-started).
- **Documented / P2:** Delivery behavior differs in foreground/background/terminated states. iOS swipe-away and Android settings force-stop can require reopening; permissions and prior registration also affect reception. [Receiving messages](https://firebase.google.com/docs/cloud-messaging/flutter/receive-messages).
- **Recommendation / P2:** Push supplements persisted appointment/task/ticket state; it cannot guarantee a precise reminder or prove the patient read it. Store device/account associations, update rotated tokens, unbind on logout/account switch, minimize lock-screen content, and fetch authorized details after a notification tap. Backend recurrence uses `Asia/Riyadh`; edits affect future occurrences only.
- **Open / P1:** Firebase/APNs account setup, approved metadata handling, reminder channels, delivery targets, and token-retention policy. Website staff unread notifications remain a separate persisted Motmaan capability; FCM is not automatically its transport.

**Future verification:** Real Android/iOS devices; denied permission; foreground/background/terminated/force-stopped states; token rotation; logout/shared device; delayed reminder after task edit; tap on a now-inaccessible record.

## WhatsApp and SMS handling: Wati

Status: source-named for WhatsApp; user identified Wati for WhatsApp/SMS evaluation on 4 October 2026. Account, subscription, Saudi SMS route, and activation remain unverified. This clarification does not select a final SMS provider or change patient login channels.

- **Documented / P2:** Outbound template messages outside the 24-hour service window need approved templates. Parameters are positional; their order must match placeholders. HTTP 200 means accepted, with final delivery/failure reported through webhooks. Tenant path, bearer credential permissions, and workspace/plan access matter; authorization failures may lack a JSON body. [Template messaging](https://docs.wati.io/reference/sendtemplatemessage).
- **Documented / P2:** Wati recommends API V3 for new integrations, using `/api/ext/v3/...` without a tenant path segment. Legacy V1/V2 routes include the workspace tenant ID. The existing template/OTP examples use legacy routes; verify equivalent V3 operations and workspace entitlement rather than mixing versions. [API versions and routing](https://docs.wati.io/reference/introduction).
- **Documented / P1:** Wati's Twilio integration supports SMS-only campaigns and automatic SMS fallback for failed WhatsApp delivery. It requires the Business plan and an active Twilio subscription, configured with Account SID, Auth Token, and a phone number. The guide currently permits one connected Twilio number. SMS templates can be linked to WhatsApp templates. [Wati–Twilio setup](https://support.wati.io/en/articles/11694867-how-to-integrate-wati-with-twilio).
- **Documented / P2:** WhatsApp OTP uses an approved authentication template; Wati documents SMS fallback through the connected Twilio account and mapped OTP template. Authentication templates do not support URLs/media/emojis. This is a delivery flow, not evidence that Wati generates or verifies Motmaan login challenges. [OTP and SMS fallback](https://support.wati.io/en/articles/11463224-how-to-send-otp-on-whatsapp-using-wati-api).
- **Documented / P1:** Twilio's Saudi guide says domestic-brand sender-ID registration is unsupported, two-way SMS is unsupported, and message URLs require allowlisting. **Open:** Confirm a supported domestic Motmaan sending route with Wati/Twilio before assuming this integration can replace the existing SMS service. The generic connected-phone-number setup alone is insufficient. [Twilio Saudi delivery constraints](https://www.twilio.com/en-us/guidelines/sa/sms).
- **Recommendation / P2:** Version Arabic/English template mappings, normalize destination numbers to the provider's format, retain message references and delivery states, and prevent duplicate sends after uncertain responses. Keep health details out of message previews; links should require Motmaan authorization.
- **Recommendation / P2:** Keep OTP expiry, single-use verification, attempts, and resend limits in the backend's challenge lifecycle. A delayed fallback must not deliver an already-expired/superseded code; it must not reset expiry or generate a second active challenge. Correlate WhatsApp and SMS attempts under the same notification/challenge and keep transport receipts separate from successful login.
- **Open / P1:** Confirm workspace/plan, V3 endpoints for transactional SMS/OTP/invitations and fallback, automatic-fallback timing/cancellation, authenticated receipts, Saudi sender approval, Arabic encoding/segment cost, quotas and combined Wati/Twilio charges, consent handling, and health-data location/retention. SMS campaign UI documentation does not establish a general-purpose transactional SMS API. Patient SMS OTP is confirmed; WhatsApp-first login is not selected. Doctor acceptance SMS remains required. AUD-04 keeps Wati evaluated without replacing it; verify Saudi OTP, registered sender, Arabic content, receipts and reliability.

**Future verification:** Rejected template; mismatched placeholders; expired session; offline tenant; 401/403 without JSON; accepted-then-failed delivery; repeated callback; Arabic rendering and Saudi network delivery; WhatsApp failure followed by SMS; late fallback after code expiry/resend; duplicate receipts across channels; SMS invitation link allowed by the route; standalone transactional SMS access. Tests remain future work, with synthetic content and approved recipients.

## Current owner clarification for media/files and hosting

Dated provider facts below remain research, not newly verified account capabilities. [04](04-online-sessions.md) owns confirmed readiness, resumable ingestion/recovery and adaptive playback (AUD-06); [03](03-integrations-and-storage.md#secure-file-lifecycle--aud-23) applies supported transfer reliability to ordinary files (AUD-23). Validate provider-controlled delivery separately from client uploads and irrecoverable live-capture loss. [22](22-azure-hosting-and-deployment.md) owns Qatar interim data-suitability gates and approved-only Saudi migration; regional/provider evidence remains pending.

## Translation: Google Cloud Translation

Status: evaluation candidate for confirmed Arabic-to-English capability.

- **Documented / P1:** Advanced Translation documents global and EU/US multi-regional endpoints; the default is global. This reference does **not establish Saudi processing**. A Dammam storage bucket does not determine translation processing location. [Endpoints](https://docs.cloud.google.com/translate/docs/advanced/endpoints).
- **Documented:** Google's data-use FAQ limits content use to providing the service. This alone does not establish suitability for Motmaan health data. [Data use](https://docs.cloud.google.com/translate/data-usage).
- **Recommendation / P2:** Preserve Arabic, label machine output, record provider/model/language/source version, bound requests and spending, and review clinical meaning before relying on translations. Human clinical review remains a recommendation.
- **Open / P1:** AUD-16 resolves general display-language behavior beyond medical text, including names transliteration and original preservation. Exact file formats remain open/noted for later. Resolve approved data categories, processing terms/location, supported edition/endpoint, retention, quotas, and clinical-review procedure before sensitive content is submitted.

**Future verification:** Arabic names use appropriate transliteration rather than semantic meanings; Web/Flutter selected-language display, original preservation, corrected derived values and no translation of IDs/codes/phones/financial identifiers. Also verify approved clinical terminology, numbers/dosages, negation and RTL, changed-source invalidation, partial failure and quota exhaustion. These are future checks; document 03 owns approved behavior.

## Comparison providers

These are alternatives, not additional mandatory integrations.

| Provider | Documented point to retain | Development implication / open dependency |
|---|---|---|
| PayTabs | `payment_methods: ["all"]` shows methods configured on that account. Callback/IPN HMAC-SHA256 checks the raw body with the profile server key; browser-return verification is a different procedure. [Methods](https://support.paytabs.com/en/support/solutions/articles/60000805455-request-parameters-payment-methods-payment-methods-), [verification](https://support.paytabs.com/en/support/solutions/articles/60000718961) | **P1:** All-method activation is account-specific. **P2:** Keep return and callback validators separate; compare refunds, capture, SDKs, reconciliation, and merchant terms with Tap. |
| Moyasar | Historical comparison: public docs describe Flutter SDKs, mada/cards and wallets, `given_id` idempotency, payment retrieval, capture/void/refund, and payment webhooks. [FAQ](https://moyasar.com/en/resources/faqs/), [Flutter SDK](https://docs.moyasar.com/sdk/flutter/installation), [API](https://docs.moyasar.com/api/payments/01-create-payment) | Its Tabby/Tamara coverage and Motmaan eligibility were unconfirmed; MyFatoorah is now the selected provider. |
| LiveKit | Self-hosted recording requires deploying Egress separately; managed Egress is available in LiveKit Cloud. [Egress](https://docs.livekit.io/transport/media/ingress-egress/egress/) | **P1:** Include media connectivity, recorder capacity, operational support, and chosen storage/processing location in comparison. |
| Daily | Its customer Amazon S3 recording flow writes directly to the bucket and requires versioning plus IAM setup. [Customer recording storage](https://docs.daily.co/guides/products/live-streaming-recording/storing-recordings-in-a-custom-s3-bucket) | **P1:** This establishes an Amazon S3 flow, not compatibility with the proposed GCS/OCI destination. Version retention also affects deletion. |

## Missing documentation and scope dependencies

| Connection | Current evidence gap | Important future action |
|---|---|---|
| SMS | Wati identified for evaluation; documented Twilio path has unresolved Saudi domestic-route and transactional API dependencies | Confirm the actual existing SMS service/account, supported Motmaan sender route, OTP ownership, expiry/resend/attempt limits, Arabic support, authenticated receipts, quotas and invitation flow. Platform identity is now recorded; account and integration access remain unresolved. See the Wati section. |
| Email/SMTP | Vendor/transport contract unavailable | Obtain sending/authentication setup, delivery/bounce contract, quotas, and credential handling. Define single-use recovery/verification/survey links without assuming a vendor. |
| Assessment platform | Existing platform per user; name/API/SSO/result contract unavailable | Forward [programmer questions](18-assessment-platform-integration-questions.md) for authentication, patient/family matching, assessment IDs, paid-access rules, results/sample files, versioning, corrections and ordering-doctor attribution. Platform existence is resolved; integration capabilities remain unverified. |
| Emdaad | Export/schema/files unverified | Request complete export inventory and file access; reconcile record counts, relationships, balances, packages, attachments, and file checksums in a trial migration. No ongoing Emdaad integration is assumed. |
| Daftra | Fallback only; not evaluated in this review | If Qoyod is unsuitable, compare actual invoice/payment/credit-note APIs, account access, correction and reconciliation guarantees before replacing it. |
| Nafath / Wasfaty | Exact Motmaan use cases and onboarding/API access unavailable | Source requirements are in first-stage scope under current direction, but obtain approved use cases, official integration package, credentials/sandbox and responsibility boundaries. Do not infer activation from source naming. |
| NPHIES / Waseel | No current insurance; future integration readiness requested | Live insurance operations remain future work. Obtain official contracts/use cases when the owner returns to implementation; readiness does not authorize provider activation. |
| Hosting, monitoring, backup | Topology/providers not selected | Agree measurable performance, restore and availability objectives before selecting infrastructure; do not invent hosting SDKs or quotas. |

This review records gaps rather than claiming inaccessible/private specifications were read. Qoyod and Tamara's large documentation pages could not be fully fetched by the browser research tool; the specific facts above were available through official indexed excerpts and related official pages. Full account-specific specifications and sandbox verification remain pending.

## Shared recommendations for implementation planning

- Keep secrets on the server and segregate test/live configuration. Public SDK configuration is allowed only where the provider explicitly supports it.
- Backend authorization must enforce user, branch, patient, appointment, and file scope. Provider IDs, redirects, push payloads, and possession of an object key do not grant resource access.
- Persist provider attempts, operation references, trusted status, retry/reconciliation state, and safe diagnostic identifiers. Retain only necessary sensitive event fields under an explicit access/retention policy.
- Protect slot ownership, wallet balances, package entitlements, refunds, and accounting publication with appropriate database concurrency controls and atomic local commits. External HTTP effects are not rolled back by database transactions.
- For reliable external work, plan durable scheduling/publication with idempotent workers and bounded retries; acknowledge valid webhooks only after processing or durable acceptance. Establish recovery for events that arrive before their local record.
- Verify ambiguous remote outcomes before repeating payments, invoices, refunds, or recording starts. Measure backlog, failures, latency, reconciliation differences, and storage usage with representative volumes.
- Use the [api-pattern reliability reference](C:/Users/omarf/.codex/skills/api-pattern/references/reliability.md) and [verification reference](C:/Users/omarf/.codex/skills/api-pattern/references/verification.md) in future backend work. Their historical infrastructure examples do not select infrastructure. Current owner choices are Azure SQL and outbox/Hangfire; AUD-21 preserves SQL-first/later selective Redis.

Related: [decisions](06-decisions-and-open-questions.md), [user tracker](12-user-notes-and-open-questions.md), [Flutter handoff](../handoff/flutter-developer.md), [web handoff](../handoff/web-frontend-developer.md).
