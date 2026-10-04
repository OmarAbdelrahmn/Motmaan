# External providers: purpose and configuration

Updated: 3 October 2026. Planning only. No accounts, credentials, purchases, or integrations have been configured.

This is the practical provider inventory for Motmaan. It explains each provider's role, what we need to configure it, who handles the work, and the expected setup effort. Detailed integration decisions remain in [integrations and storage](03-integrations-and-storage.md).

## How to read the guide

- **User preference:** preferred for evaluation, not a signed contract or activated account.
- **Source-named:** specified in the supplied requirements document; still needs technical/account validation.
- **Proposed:** recommendation, not selected by the user.
- **Unknown:** provider identity or integration contract is missing.
- Setup effort is our planning estimate, not a provider guarantee: **Easy** means a small setup once access is available; **Medium** needs several systems or approvals; **High** involves accounting, video/storage, sensitive data, or unknown APIs. Commercial approval time is separate from coding effort.

## Current provider inventory

| Provider / service | Role in Motmaan | Current status | Configuration needed | Setup estimate / main dependency |
|---|---|---|---|---|
| Tap Payments | Online checkout for required mada, Apple Pay, cards, Tabby, and Tamara, if all are approved for Motmaan | User's preferred gateway candidate | Merchant account/ID, separate test/live keys, enabled methods, callback/return URLs, refund access; domain/app registration where required | Medium; merchant approval and all-method activation are the key dependency. [Official setup](https://developers.tap.company/docs/get-started) |
| Tabby | Installment-payment option | Required method; evaluate activation through Tap first | Merchant eligibility, method activation, allowed flows, capture/refund rules, transaction references | Medium through gateway; separate direct integration increases work. No separate API connection is assumed. [Payment API](https://docs.tabby.ai/api-reference/payments/retrieve-a-payment) |
| Tamara | Installment-payment option | Required method; evaluate activation through Tap first | Merchant eligibility, method activation, transaction lifecycle/refunds, event handling | Medium through gateway; eligibility and gateway coverage remain to confirm. [Webhook documentation](https://docs.tamara.co/reference/getting-started-with-webhooks) |
| Qoyod | Accounting and official accounting/e-invoicing documents under the accepted planning recommendation | Source-named | Motmaan account/API access, customer/service mapping, tax/account configuration, external references, reconciliation process | High; finance must validate mappings and correction behavior. Public API reference alone does not establish account capabilities. [Official API](https://apidoc.qoyod.com/) |
| SMS provider, name unknown | Patient phone OTP, doctor acceptance invitations, approved operational SMS | Required capability; provider unknown | Account/API access, permitted sender, Arabic message support, delivery receipts, rate limits; clarify whether provider or Motmaan generates/verifies OTPs | Unknown until we identify the existing provider and test delivery |
| Agora | Online audio/video sessions and session recording | Source-named provisional choice | Project/app identity, token/recording credentials, enabled recording product, supported storage destination and region, event/status integration | High; prove mobile/web calls and recording delivery to the exact private bucket. [Cloud Recording](https://docs.agora.io/en/realtime-media/cloud-recording) |
| Private object storage: Google Cloud Storage in Dammam | Medical files, reports, recordings, recruitment documents; isolated public media where needed | Proposed candidate; OCI Saudi is an alternative | Center-owned account, regional access/billing, buckets, limited service access, retention/backup settings, browser upload rules if needed | Medium to High; regional onboarding and recorder compatibility remain to validate. [Storage locations](https://docs.cloud.google.com/storage/docs/bucket-locations), [Dammam access](https://docs.cloud.google.com/docs/dammam-region-access) |
| Firebase Cloud Messaging, with Apple APNs setup for iOS | Backend-triggered app push: appointments, doctor-assigned tasks, tickets, approved updates | Proposed | Firebase project, Android/iOS app IDs/configuration, server access, APNs authentication/capabilities, user permission and device registration | Medium; both mobile platforms and foreground/background delivery need verification. [Flutter setup](https://firebase.google.com/docs/cloud-messaging/flutter/get-started) |
| Transactional email / existing SMTP, provider unknown | Verified email recovery/setup, closed-ticket satisfaction survey, approved documents and messages | Required capability; vendor unknown | Sending account/domain, server credentials, sender identity, domain authentication, templates, delivery/bounce handling | Easy to Medium after provider selection; domain ownership and delivery quality matter |
| Wati | WhatsApp confirmations, reminders, and other approved messages | Source-named | WhatsApp Business account/number, Wati workspace/API access, approved templates, template variables, delivery events | Medium; business/template approval can block launch. Accepted API requests are not proof of delivery. [Template API](https://docs.wati.io/reference/sendtemplatemessage) |
| Center assessment platform, name/API unknown | Psychological tests: requests, paid access, SSO, completion and result import | Source-required connection; contract unknown | Vendor identity/docs, authentication/SSO agreement, patient matching, test IDs, request/result references, status/callback or polling contract | High/Unknown until documentation and sample results are available |
| Google Cloud Translation | Translate user-imported Arabic data into English while preserving Arabic | User requires translation; Google is an evaluation candidate | Cloud project, enabled API, server authentication, edition/processing endpoint, Arabic/English settings, quota/budget; approved data handling | Medium technically; health-data processing location/terms and clinical review remain unresolved. [Text API](https://docs.cloud.google.com/translate/docs/translate-text) |
| Emdaad export | Full migration of existing records and referenced files into Motmaan | Confirmed one-time migration source; replace at launch | Export/schema access, file archive/retrieval, field/ID mapping, duplicates, trial import, financial/file reconciliation, cutover plan | High; validate that every requested data category is actually exportable |

Mada and Apple Pay are payment methods within the chosen payment setup, rather than additional Motmaan business backends. Apple Pay may still require its own domain/app registration steps. Tabby/Tamara merchant approval remains necessary even if the gateway exposes them.

## Alternatives and scope requiring clarification

| Provider / connection | Why it appears in the project | Current treatment |
|---|---|---|
| PayTabs | Alternative gateway for the required payment-method combination | Comparison to Tap, not a second gateway automatically required. Validate enabled methods, merchant approval, fees, and refunds. [Method configuration](https://support.paytabs.com/en/support/solutions/articles/60000805455-request-parameters-payment-methods-payment-methods-) |
| MyFatoorah | Payment provider named by the source document | Source shortlist, not the current preferred candidate. User direction evaluates a gateway offering all required methods together. [Payment verification](https://docs.myfatoorah.com/docs/v3-updating-payment-status-guidelines) |
| LiveKit / Daily | Alternatives to Agora | Evaluate only if Agora cannot meet the network/storage/operational requirements; detailed tradeoffs are in the integration note |
| OCI Object Storage | Saudi-region alternative to proposed Google storage | Confirm region, center access, recorder support, cost, and terms before selecting. [Oracle regions](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/regions.htm) |
| Daftra | Accounting fallback if Qoyod cannot meet requirements | No additional integration selected |
| NPHIES / Waseel | Insurance eligibility/approval/claims | Explicitly deferred to the project owner; do not assume live insurance APIs are approved |
| Nafath / Wasfaty | Source-named identity/prescription capabilities | Broad first-stage scope includes source-labeled later features, but exact use cases, access, and approvals still need clarification; no provider activation is authorized |

Internal staff tasks require live in-website notifications for assignment, comments, status changes, approaching deadlines, and overdue work. The delivery transport, persistence, and deployment topology remain undecided; no additional external provider is selected for this capability. Patient-task mobile push remains a separate channel.

Support tickets, the internal staff-task system, wallets, compensation rules, and permissions are Motmaan modules. No external SaaS provider has been selected for those workflows. Hosting, monitoring, and backup infrastructure also remain undecided.

## Who owns configuration

These responsibility assignments are recommendations; detailed staff permissions remain deferred.

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
