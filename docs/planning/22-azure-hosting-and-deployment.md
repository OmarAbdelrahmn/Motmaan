# Azure hosting and deployment preparation

Updated: 8 October 2026. Planning guidance only; no Azure resources, purchases, application code or deployments have been created.

## Decision status

**Confirmed:** Use **Azure SQL Database (SQL Server)** for the backend. Azure Managed Redis remains the confirmed fifth service in the discussed Azure hosting plan. These selections do not approve tiers, prices, provisioning or production activation. **AUD-05 confirms Qatar Central as the interim preference; a suitable verified Azure Saudi region is preferred long term.**

**Confirmed on 8 October:** Use the **transactional outbox pattern with Hangfire** for reliable external effects and appropriate lengthy/scheduled work. [Background workflow design](23-outbox-and-background-jobs.md) owns the execution, retry, security and recovery details. SQL storage for Hangfire and its worker host are proposed below; exact deployment configuration remains open.

The working Azure plan below includes selected Azure SQL Database and Redis, and the now-approved OpenTelemetry/Application Insights monitoring choice. HybridCache is approved for suitable local/shared caching. App Service, private Blob Storage and Key Vault remain proposals. Qatar Central is the confirmed interim region. Service availability/access, tiers, budget and full topology remain open; initial recovery/operational targets are in [quality requirements](09-performance-security-and-responsive-websites.md#initial-operational-targets-and-reporting--aud-26). Earlier GCS Dammam and OCI storage candidates remain alternatives until Azure storage location and recording compatibility are proven. This answer does not move the project out of planning. [Approved engineering tools](24-approved-engineering-tools-and-realtime.md) also records the still-proposed SignalR/FCM/APNs design; Azure SignalR Service is not a selected or provisioned resource.

| Item | Service | Purpose / status |
|---|---|---|
| 1 | Azure App Service | Proposed ASP.NET Core API host; Linux code deployment is the recommended simple starting option if dependencies permit |
| 2 | Azure SQL Database | Confirmed SQL Server database service for the backend; tier, regional service access and provisioning remain open |
| 3 | Private Azure Blob Storage | Proposed documents and recordings destination; exact approved location and recorder compatibility unverified |
| 4 | Azure Key Vault and Application Insights | Key Vault remains proposed for secrets; OpenTelemetry with Application Insights is approved for monitoring on 8 October. These are separate resources grouped as one plan item; Application Insights also uses a Log Analytics workspace. Location, configuration, cost and provisioning remain open |
| 5 | Azure Managed Redis | Confirmed inclusion for shared caching; region, tier, capacity and purchase timing open |

## Interim Qatar deployment and Saudi migration — AUD-05

**Confirmed:** Microsoft Azure remains the platform, Azure SQL the database direction, and **Azure Qatar Central** the temporary hosting region until an appropriate Saudi Azure region is confirmed available and suitable. This preference is **not authorization to transfer production patient information internationally**.

Before production patient data is deployed to Qatar, verify applicable Saudi health-data residency, privacy, regulatory, contractual and cross-border transfer requirements through responsible reviewers. If Qatar cannot legally or operationally host the required data, flag a **production deployment blocker** and obtain an approved alternative; do not silently choose another region. Validate regional service availability, subscription/tier access and compatibility for every selected/proposed service, including media processing/fallback, storage, logs, backups and disaster recovery. No availability/compliance result is claimed here.

When a Saudi region becomes available: verify actual services and subscription/tier access; compare costs and infrastructure compatibility; check network/database/storage/backup/disaster-recovery capabilities; prepare a controlled migration plan; execute only after approval. An announcement must not trigger automatic migration. The dated announcement reference below is historical research, not current availability evidence. Existing GCS/OCI alternatives are not selected by this decision.

## Before creating resources

1. Keep subscription, billing and recovery under Motmaan ownership. Give developers individual scoped access and protect administrator accounts with MFA; do not share owner credentials.
2. Verify actual regional availability and subscription access for every service, including Redis and the monitoring workspace. Microsoft announced Saudi Arabia East for November 2026; as of this research date this is a future announcement, not verified availability. Do not substitute an overseas region for production health data without an approved data-handling decision. Synthetic-data development elsewhere is a separate proposal.
3. Confirm supported .NET runtime, expected concurrency, recording volume, monthly budget, availability and recovery objectives. Price the App Service plan, Azure SQL Database, Redis, storage/retention, network/private endpoints, telemetry, backups and support together. Budget alerts notify; they are not a hard spending cap.
4. Prepare isolated staging and production resource groups, identities, databases, storage, Redis, secrets and telemetry. Example names are `motmaan-staging` and `motmaan-production`; final names are open. Separate resource groups alone do not isolate data or permissions.

## Proposed setup order after authorization

| Order | Action | Result / important configuration |
|---|---|---|
| 1 | Create staging resource group and network | Choose validated region; plan virtual network integration, private endpoints and private DNS. These supporting resources are additional to the five plan items |
| 2 | Create SQL and approved Storage resources | For the selected Azure SQL Database, create the logical SQL server/database, Entra administrator, backups and required availability tier. Disable anonymous blob access; separate documents, recordings and recruitment containers. Provision selected Azure Managed Redis later only when measured public caching use cases and the hosting plan are ready; then validate TLS, Entra authentication and private connectivity |
| 3 | Create Key Vault and monitoring | Vault stores external-provider secrets; configure recovery protection and scoped access. Create Application Insights/workspace, diagnostic retention, latency/error/dependency alerts and cost controls; exclude OTPs, tokens and clinical payloads |
| 4 | Create App Service plan and API app | Select supported .NET runtime and a tier supporting required networking/deployment features; enforce HTTPS. Enable the API's managed identity and connect its outbound traffic to the virtual network. Outbound VNet integration does not itself make the API private |
| 5 | Grant the API identity service access | Give minimum database runtime permissions, scoped Blob permissions, Key Vault secret-read permission and Redis data access. Use a separate deployment identity for schema changes; do not make the runtime identity a database administrator |
| 6 | Configure API settings and deploy | Supply SQL endpoint/database, Storage account/container names, Redis endpoint and telemetry configuration. Use managed identity for supported Azure connections and Key Vault references for remaining secrets. Deploy through Visual Studio for an initial staging trial or a GitHub Actions pipeline with federated identity for repeatable releases |
| 7 | Initialize and verify staging | Apply reviewed EF migrations through the deployment process; use synthetic data and sandbox integrations. Prove connectivity, denied access, cache refresh/failure handling, webhook retries, contested bookings, file access and useful monitoring |
| 8 | Prepare production and cut over | Reproduce reviewed settings with separate identities/data/secrets; connect approved API domain/TLS and clients, authenticate public provider callbacks, execute required readiness checks and the migration/cutover plan. Owner approval after successful tests remains required for production activation |

The websites and Flutter binaries need their own release arrangements. Web clients and Flutter call the HTTPS API; they never receive SQL, Redis, Storage account or Key Vault credentials. Browser CORS permits only approved website origins; CORS is not API authorization. A publicly reachable API can use private connections to its backing services.

Private Blob connectivity must also support the agreed browser/mobile upload/playback and recorder ingestion paths. Anonymous-access blocking and a private network endpoint solve different problems. A signed URL does not bypass a storage firewall. Do not claim Agora can write to this destination until the exact credentials, network path, regional processing/fallback and recording output are tested.

Background imports, reminders and accounting synchronization use the confirmed outbox/Hangfire direction. Proposed starting arrangement: outbox records share the business SQL transaction, while Hangfire uses a dedicated schema through its SQL Server storage. Ordinary EF commits and Hangfire enqueue calls remain separate durability boundaries. Validate a continuously available dispatcher and worker host, bounded queues/concurrency, restart recovery, least-privilege runtime access and restricted dashboard access. Worker isolation or a separate job database may require additional resources if measurements justify them. Exact tiers/topology remain open. The five services and Hangfire do not automatically provide multi-instance live-notification transport; that separate requirement remains open. See [the detailed design and acceptance checks](23-outbox-and-background-jobs.md).

## Cache behavior

- Cache public service/expertise catalogs and approved doctor profiles with bounded expiry and invalidation on changes. **AUD-21:** optimize and measure EF Core/SQL first: indexes, pagination, projections and fewer unnecessary reads. HybridCache stays selected; Redis follows later for beneficial public mobile API doctor listings/available-doctor discovery, profiles and service/category catalogs. Define invalidation across instances explicitly; other servers' existing local entries are not automatically cleared by shared-store invalidation.
- SQL remains authoritative for reservations, payment state, wallet balance, package consumption and financial records. Revalidate cached availability transactionally when reserving. Redis expiry alone does not implement the seven-minute booking/payment lifecycle.
- Avoid patient-data caching initially. Any later private cache requires identity/branch/resource scope, authorization and permission-revocation handling. Shared OTP limits/session revocation require an explicit multi-instance design; selecting Redis does not approve that design.
- Redis is recoverable cache data, not the only copy of business records. Cache-only operations may use bounded database fallback during outage; security controls must not silently disappear if Redis fails. Choose and verify outage handling for each use case.
- Redis remains selected; do not provision it before use cases/hosting readiness justify it. Define expiration and multi-instance invalidation; measure benefit/capacity before choosing a tier. SQL remains authoritative for capacity, finance/payment status and sensitive authorization; booking must revalidate availability.

## Required evidence before production

Complete the project's required security, user-acceptance, payment/accounting reconciliation, representative performance, monitoring and successful backup-restoration checks. Verify SQL/file consistency, retention/deletion behavior, protected logs, rollback and named operating/recovery owners. A deployment slot or previous API build does not roll back a database schema automatically.

## Official sources checked on 6 October 2026

- [Saudi Arabia East announcement for November 2026](https://news.microsoft.com/source/emea/2026/08/microsoft-announces-saudi-arabia-east-datacenter-region-will-be-available-in-november-2026/).
- [App Service .NET deployment](https://learn.microsoft.com/en-us/azure/app-service/quickstart-dotnetcore) and [GitHub Actions deployment](https://learn.microsoft.com/en-us/azure/app-service/deploy-github-actions).
- [SQL connection using managed identity](https://learn.microsoft.com/en-us/azure/app-service/tutorial-connect-msi-sql-database); example permissions must be narrowed to Motmaan runtime/deployment responsibilities.
- [App Service Key Vault references](https://learn.microsoft.com/en-us/azure/app-service/app-service-key-vault-references) and [outbound VNet integration](https://learn.microsoft.com/en-us/azure/app-service/overview-vnet-integration).
- [Blob anonymous-access controls](https://learn.microsoft.com/en-us/azure/storage/blobs/anonymous-read-access-configure) and [App Service monitoring](https://learn.microsoft.com/en-us/azure/app-service/monitor-app-service?tabs=aspnetcore).
- [Azure Managed Redis security](https://learn.microsoft.com/en-us/azure/redis/secure-azure-managed-redis), [.NET connection example](https://learn.microsoft.com/en-us/azure/redis/dotnet) and [retirement of the older Azure Cache for Redis](https://learn.microsoft.com/en-us/azure/azure-cache-for-redis/cache-whats-new).

Public documentation supports preparation guidance; it does not prove Motmaan account access, deployed behavior, Saudi service availability or recorder compatibility.
