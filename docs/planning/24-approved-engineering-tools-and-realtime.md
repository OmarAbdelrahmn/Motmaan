# Approved engineering tools and proposed real-time messaging

Updated: 8 October 2026. Planning choices and developer design guidance; no application implementation or resource provisioning is authorized.

## Decision status

The user selected **Swagger with OpenAPI contracts** and approved the remaining recommendations from the 8 October technical discussion, while asking for further advice about SignalR across platforms. The approved choices below are confirmed. **SignalR, the Flutter SignalR client, FCM/APNs and a managed SignalR service remain recommendations awaiting selection and technical validation.** Approval of engineering tools does not settle unresolved business rules, API payloads, package/runtime versions, regional service access, resource tiers or costs. AUD-05 now confirms Qatar Central interim subject to data review; AUD-20 defers detailed SignalR events without selecting SignalR/FCM/APNs.

## Confirmed choices and their responsibilities

| Choice | Motmaan responsibility | Details still to specify |
|---|---|---|
| Modular monolith | One backend with explicit ownership for identity, booking, clinical care, finance and integrations; cross-module work uses application contracts | Actual project/module names, dependency boundaries and contracts |
| ASP.NET Core policy and resource authorization | Evaluate endpoint action permissions and branch/patient/assignment/consent scope; enforce separate clinical/recording grants for HTTP, jobs, files and live subscriptions | Within-role allowed/removed overrides confirmed (AUD-09); multi-role conflicts/delegation, granular matrix and technical mechanisms remain open; privileged assurance mandatory (AUD-08) |
| FluentValidation | Validate input contracts consistently, invoking asynchronous rules explicitly; business invariants and database constraints remain enforced in the owning use case | Validator placement/registration, error codes, Arabic/English presentation and per-field rules |
| Swagger UI with OpenAPI contracts | Publish the agreed request/response/error schemas for backend, web and Flutter developers, with interactive API exploration | Compatible OpenAPI generator/UI packages and versions, development/staging access and production exposure policy |
| Typed HttpClient and .NET HTTP resilience | Isolate provider adapters and configure timeouts, bounded retries, circuit breakers and concurrency per dependency | Provider-specific retry/idempotency guarantees, timeout budgets, failure mapping and coordination with Hangfire retries |
| OpenTelemetry with Application Insights | Correlate API, SQL, background jobs and provider calls; monitor latency, failures and backlog | Approved location/access, telemetry filtering, retention, sampling, alerts and resource tier/budget |
| HybridCache with selected Azure Managed Redis | Optimize/measure SQL first, then cache beneficial public mobile doctor/discovery/profile/service/category endpoints using local/shared layers; Redis provisioning later (AUD-21) | Expiry, capacity, multi-instance invalidation and outage behavior; sensitive-data caching remains a separate design choice |
| SQL Server integration tests with Testcontainers | Verify actual SQL transaction/concurrency behavior for bookings, wallet/package effects, callbacks and background recovery | Test runner, container/runtime support, representative fixtures and Azure-specific staging verification |
| Playwright web tests and Flutter integration tests | Exercise meaningful user journeys, Arabic/English, RTL/LTR, responsive behavior and interruption/resume | Supported browsers/devices, critical scenarios, CI arrangement and real-device checks |
| Protected audit/edit history | Preserve evidence of sensitive permission changes, clinical edits, refunds and recovery actions | AUD-15 mandates clinical original/updated versions, author/time, exported version files and signature lineage. Exact storage, authorized presentation and retention remain design work |
| Incoming-webhook deduplication and database concurrency protection | Prevent repeated events or competing requests from duplicating financial effects, consuming entitlements twice or double-booking capacity | Event identities, uniqueness, version/conditional-write/isolation choices and safe conflict/reconciliation outcomes |

Transactional outbox with Hangfire was already confirmed and is detailed in [background workflow design](23-outbox-and-background-jobs.md). These additions complement that design.

## API contracts and Swagger

OpenAPI describes the HTTP interface; Swagger UI displays that specification and lets authorized developers explore it. Agree request/response types, nullability, action permissions, status transitions, validation/conflict/error responses, idempotency behavior and bounded queries with the web and Flutter developers. Include UTC instants, server deadlines and safe operation references for asynchronous work.

Choose a maintained OpenAPI generator and Swagger UI integration compatible with the eventual .NET version. Built-in ASP.NET Core OpenAPI generation and Swagger UI can be combined; the user selected the documentation approach, not a specific generator package. Protect interactive documentation according to the environment and do not store production credentials or real clinical examples in specifications.

Use synthetic examples. Generated documentation must match the implemented behavior and agreed workflow contracts. A generated specification does not supply missing business rules, authorization or client compatibility policy. Older installed Flutter versions need an explicit compatible API-change policy.

## Reliability, audit and caching details

- Provider HTTP retries must be configured per operation. The standard .NET resilience handler can retry unsafe methods by default; disable those retries until duplicate protection and unknown-outcome reconciliation are verified. Coordinate retry layers so HttpClient, Hangfire and outbox scheduling do not multiply calls. Never hold a SQL transaction during a provider request.
- Protect audit history independently of ordinary diagnostic logs. Record actor/service authority, action, scoped resource, time and correlation/reference information. Clinical versions/diffs containing health data require protected clinical storage/access; redact ordinary logs and telemetry. Final clinical report editing stays direct, with mandatory version/export/signature history (AUD-15); prescription/accounting correction policy remains open.
- Deduplicate authenticated incoming callbacks using durable provider/event identities and legal state transitions. Persist the deduplication result with the relevant local change where required. Different event IDs can describe the same business effect, so business operation uniqueness is also necessary. Reconcile late, out-of-order and ambiguous outcomes.
- SQL rowversion/conditional updates can detect competing edits, but capacity, money and entitlement invariants need appropriate constraints and transaction/isolation design. A version column alone does not prevent every overlapping booking or multi-row conflict. Verify with the selected provider.
- HybridCache invalidation affects the current process and shared storage; other servers' existing local entries need an explicit refresh/version/expiry strategy. Do not let stale cache entries preserve revoked permissions or authorize a reservation. Begin with approved public data and measure benefit.
- Testcontainers supplies SQL Server behavior in tests; it does not prove Azure networking, managed identity, regional availability, backups or deployed service behavior. Cover those separately in staging. UI tests cover meaningful workflows; synthetic data and negative authorization tests remain required.

## Deferred SignalR event design — AUD-20

**Deferred:** no event taxonomy, ordering, delivery semantics or scaling architecture is finalized here. The prior illustrative proposals below remain recommendations for later review; SignalR/Flutter client/FCM/APNs/managed service selection retains its proposed status. Do not treat the described flow as a decided contract.

## Prior proposed messaging across platforms

**Recommendation:** Use **ASP.NET Core SignalR** for live updates while a website or app is connected, combined with **FCM/APNs** for mobile notification delivery in background/terminated states where the operating system permits. Store messages/notifications and their recipient state in Motmaan SQL so clients can recover missed updates through an authorized API.

| Platform/state | Recommended delivery | Recovery behavior |
|---|---|---|
| Management, reception, doctor and patient websites while connected | Official SignalR JavaScript client | Reconnect, restore authorized subscriptions and fetch missing/current state |
| Flutter patient app while active | A validated Flutter SignalR client | Refresh credentials safely, reconnect after network changes and fetch missed messages |
| Android app in background or terminated | FCM with approved notification payloads | OS delivery may be delayed/blocked; refresh authorized SQL state when opened |
| iOS app in background or terminated | FCM configured with APNs or an agreed direct APNs path | Same durable recovery; validate permission, app lifecycle and force-close limitations on real devices |
| Client offline or notifications disabled | Persisted inbox/message history through the application API on return | Recover missed entries, unread state and current resource access |

Microsoft documents official JavaScript, .NET, Java and Swift clients. A Dart/Flutter connection requires an evaluated community client or a separately designed native bridge; do not treat it as an official Microsoft Dart SDK. `signalr_netcore` is one candidate, not a selected dependency. Verify current maintenance, license, protocol/runtime compatibility, token refresh, reconnect, network switching, app lifecycle, logout/account switching and duplicate delivery on Android/iOS before committing to it.

Suggested delivery flow:

1. An authorized use case commits the message/notification, recipient references and required outbox work together with its business change.
2. Hangfire processes the delivery work, rechecking recipients, scope and expiry, then sends a minimal live update through SignalR and an eligible push notification. Define whether a push is suppressed for an active device; presence is advisory and cannot prove a message was read.
3. Every channel carries the same stable application message/notification identity so clients can deduplicate. Define seen/read actions separately from send attempts, provider acceptance and device delivery. Exact account-versus-device read semantics remain open.
4. On reconnect, app opening or account change, the client fetches authorized missed messages/current state using bounded pagination or a cursor. Push and live delivery may both be lost or duplicated; SQL and API state support recovery.

Authenticate connections and hub methods, derive recipient/group membership on the server and recheck access after role/branch/assignment/consent changes. Group names and a client-supplied patient ID do not grant permission. Invalidate subscriptions on logout/deactivation/revocation. Avoid sensitive medical content in push/lock-screen payloads and logs; open the app and fetch protected content after current authorization.

OpenAPI/Swagger documents the HTTP history/read/status APIs. SignalR hub methods, event names, payload versions, ordering/deduplication, authorization, reconnect and missed-message recovery need a separate event contract shared by web and Flutter. A live event should request a refresh or convey an authorized update without making the frontend decide financial or clinical transitions.

## Proposed hosting and open decisions

SignalR is a suitable protocol/library for the selected ASP.NET Core backend. Azure SignalR Service is a separate managed hosting/scaling resource and remains unapproved. For multiple API instances, choose and verify a common delivery arrangement; Microsoft recommends Azure SignalR Service for Azure-hosted SignalR apps, while a Redis backplane is another documented option with its own affinity and connection requirements. Redis cache selection does not configure a backplane automatically.

Validate location, data processing, cost, concurrent connections and latency before selecting a managed real-time service. One API process can host SignalR initially if measured load and availability requirements support it; a separate Hangfire worker still needs a defined route for live publication. `IHubContext` in an isolated worker process alone does not reach clients connected to another API process. Choose shared transport or an authenticated publication path as part of the deployment design.

SignalR cannot promise immediate background mobile delivery. FCM/APNs also depend on permissions, connectivity and OS lifecycle rules; Android force-stop and iOS background-message limits require recovery after manual app opening. Confirm the P08 account/data-handling setup and real-device evidence before activation.

Open decisions: confirm SignalR/FCM/APNs selection, Flutter client, hosting/backplane, message channels and payloads, latency targets, ordering/read semantics, retention, offline recovery contract, service region/cost and account access. This recommendation supports the existing ticket/task/readiness requirements; it does not add a general patient-doctor chat product or select unapproved recipient rules.

## Official and maintainer references

Technical references checked in the 8 October discussion:

- [Swagger/OpenAPI in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/tutorials/web-api-help-pages-using-swagger) and [OpenAPI generation](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/openapi/overview).
- [Resource authorization](https://learn.microsoft.com/en-us/aspnet/core/mvc/security/authorization/resource-based) and [FluentValidation asynchronous invocation](https://docs.fluentvalidation.net/en/latest/aspnet.html).
- [HTTP resilience and unsafe-method retries](https://learn.microsoft.com/en-us/dotnet/core/resilience/http-resilience).
- [OpenTelemetry with Application Insights](https://learn.microsoft.com/en-us/azure/azure-monitor/app/opentelemetry-enable) and [telemetry filtering](https://learn.microsoft.com/en-us/azure/azure-monitor/app/opentelemetry-filter).
- [HybridCache behavior](https://learn.microsoft.com/en-us/aspnet/core/performance/caching/hybrid) and [EF concurrency](https://learn.microsoft.com/en-us/ef/core/saving/concurrency).
- [SQL Server Testcontainers](https://dotnet.testcontainers.org/modules/mssql/), [Playwright](https://playwright.dev/docs/intro) and [Flutter testing](https://docs.flutter.dev/testing/overview).
- [SignalR supported clients](https://learn.microsoft.com/en-us/aspnet/core/signalr/supported-platforms?view=aspnetcore-10.0), [hosting/scaling](https://learn.microsoft.com/en-us/aspnet/core/signalr/scale) and [Flutter client candidate](https://pub.dev/packages/signalr_netcore).
- [FCM Flutter foreground/background/terminated handling](https://firebase.google.com/docs/cloud-messaging/flutter/receive-messages).

Documentation supports these design choices; no Motmaan runtime, provider account or device delivery has been tested by this planning work.
