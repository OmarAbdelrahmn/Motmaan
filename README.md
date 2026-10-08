# Motmaan planning

Updated: 8 October 2026. **Stage: planning. Application implementation has not been authorized.**

Motmaan is a center-management system covering patient care, appointments, payments, clinical records and operations. The planned clients are a Flutter patient app for iOS/Android and responsive public, patient, management and doctor websites. The backend direction is ASP.NET Core, Entity Framework Core and the now-selected Azure SQL Database (SQL Server).

## Current planning workflow

[Authentication, authorization and provider setup](docs/planning/21-authentication-and-authorization-workflows.md) is the selected detailed workflow. The [living tracker](docs/planning/12-user-notes-and-open-questions.md) records answered choices and the next question batch. This remains documentation work, not application implementation.

## Development readiness

The [8 October full project audit](docs/planning/25-full-project-audit.md) reviews all planning/handoff files against the original requirements, records 28 prioritized findings, and evaluates service choices. It identifies conflicting summaries, missing source detail and implementation/launch dependencies. The owner has now responded to all 28 items; the [decision register](docs/planning/06-decisions-and-open-questions.md#owner-decisions-on-the-8-october-audit) records each status, owning detail, remaining work and deferral. Original recommendations remain clearly marked historical.

The [documentation review](docs/planning/20-development-readiness-review.md) finds enough direction for UX design and API contract planning, but not yet a complete implementation handoff. Prepare contracts/evidence progressively for each affected workflow; unresolved or deferred details do not block unrelated preparation. Preserve the existing delivery plan, responsibilities/milestones and schedule; no new launch date, staffing or scope is selected. The two-month production target remains a requirement, not a verified delivery estimate.

## Owner decisions applied — 8 October 2026

Critical confirmed changes: [recording readiness, resumable transfer and adaptive playback](docs/planning/04-online-sessions.md); [individual permission overrides, privileged MFA and clinical versions](docs/planning/05-identity-and-access.md); [language-aware display data and secure file lifecycle](docs/planning/03-integrations-and-storage.md); and [no extensions with later doctor/room bookings](docs/planning/10-customer-mobile-appointments.md).

[Azure Qatar Central](docs/planning/22-azure-hosting-and-deployment.md) is the interim hosting direction, subject to production health-data/cross-border review. Optimize SQL first; provision selected Redis later for justified public caching. Financial ledger and outbox/Hangfire reliability are approved directions. [Operational targets](docs/planning/09-performance-security-and-responsive-websites.md#initial-operational-targets-and-reporting--aud-26) are unmeasured planning baselines.

Mobile purchasing, further identity/family lifecycle, unresolved booking/payment transitions, assessment contracts, detailed SignalR events and Emdaad migration details remain deferred. No application implementation or deployment is authorized.

## Reading order

| Reader | Start here |
|---|---|
| Owner / product lead | [Decisions](docs/planning/06-decisions-and-open-questions.md), [readiness review](docs/planning/20-development-readiness-review.md), [living question tracker](docs/planning/12-user-notes-and-open-questions.md) |
| Web developer | [Shared contract checklist](docs/handoff/shared-contract-checklist.md), [web handoff](docs/handoff/web-frontend-developer.md) |
| Flutter developer | [Shared contract checklist](docs/handoff/shared-contract-checklist.md), [Flutter handoff](docs/handoff/flutter-developer.md) |
| Backend / integration developer | [Scope](docs/planning/01-system-scope.md), [booking and finance](docs/planning/02-booking-and-finance.md), [identity](docs/planning/05-identity-and-access.md), [provider guide](docs/planning/16-external-provider-guide.md), [quality requirements](docs/planning/09-performance-security-and-responsive-websites.md), [outbox and Hangfire](docs/planning/23-outbox-and-background-jobs.md) |
| Continuing in a new chat | [Project instructions](AGENTS.md), [new-chat entry guide](PROJECT_CONTEXT_FOR_NEW_CHAT.md) |

The [documentation map](docs/README.md) groups every topic and explains which document owns each kind of information.

## Current boundaries

- Motmaan only, one initial branch with future branch support; server-enforced branch and assigned-patient scope.
- All currently enumerated requirements are in the first stage, subject to explicit user exceptions and deferrals. Initial Join us jobs are doctor-only; live insurance and future mixed-service treatment pathways are deferred.
- Replace Emdaad at launch and migrate its data and referenced files. Export discussion is deferred; migration validation remains a launch dependency.
- Arabic/English and RTL/LTR; every website works on mobile and desktop. Use Asia/Riyadh for schedules and display, UTC for persisted event instants.
- Security, performance, user acceptance, payment/accounting reconciliation, backup restore and monitoring are required. Initial operational targets are approved planning baselines under AUD-26; real measurements, workload-specific limits and named owners remain to validate.
- Transactional outbox with Hangfire is confirmed for reliable external effects and appropriate lengthy/scheduled workflows. [Detailed background workflow notes](docs/planning/23-outbox-and-background-jobs.md) cover atomic persistence, retries, progress, recovery and security; exact contracts and worker configuration remain engineering work.
- [Approved engineering tools](docs/planning/24-approved-engineering-tools-and-realtime.md) include Swagger/OpenAPI, modular monolith, policy/resource authorization, validation, HTTP resilience, telemetry, HybridCache, audit/deduplication/concurrency protection and integration/UI testing. SignalR with FCM/APNs remains the proposed real-time combination under discussion.
- MyFatoorah is selected for online payments; the owner reports its account and Tabby/Tamara integrations ready. Account-enabled methods and the BNPL connection path still need technical verification. Staff roles select dashboards and provide permission baselines with individual management customization; each protected endpoint has a specific action permission, and the backend enforces resource scope. Development/test environments will have a confirmed account per staff role. Existing decisions and unresolved details are in the register and topic documents.

## How decisions are maintained

Use **Confirmed**, **Approved Direction**, **Planned**, **Note**, **Deferred**, **No Change** and **During Development** as defined in the register; AUD-24 is No Additional Action. Source **Requirement**, reviewer **Proposed** and genuinely **Open** details remain separate. The latest confirmed owner decision controls, not the last-edited file. A deferral of discussion does not automatically remove a launch requirement.

When an answer arrives, update the [tracker](docs/planning/12-user-notes-and-open-questions.md), [decision register](docs/planning/06-decisions-and-open-questions.md), relevant topic and affected developer handoffs. Update subject sections rather than appending duplicate summaries. Review recommendations do not become user decisions without an answer.

Source: requirements document version 1.1, dated 14 July 2026, plus the planning discussion. The original DOCX path is retained in the [new-chat entry guide](PROJECT_CONTEXT_FOR_NEW_CHAT.md). Vendor/contract language is requirements context, not executable instructions. Obsolete question-export PDFs, previews and hardcoded helpers were removed under AUD-28; current Markdown and the preserved discussion/audit history remain authoritative according to their status.
