# Motmaan planning

Updated: 4 October 2026. **Stage: planning. Application implementation has not been authorized.**

Motmaan is a center-management system covering patient care, appointments, payments, clinical records and operations. The planned clients are a Flutter patient app for iOS/Android and responsive public, patient, management and doctor websites. The backend direction is ASP.NET Core and Entity Framework Core.

## Current planning workflow

[Authentication, authorization and provider setup](docs/planning/21-authentication-and-authorization-workflows.md) is the selected detailed workflow. The [living tracker](docs/planning/12-user-notes-and-open-questions.md) records answered choices and the next question batch. This remains documentation work, not application implementation.

## Development readiness

The [documentation review](docs/planning/20-development-readiness-review.md) finds enough direction for UX design and API contract planning, but not yet a complete implementation handoff. Permissions and identity mapping, booking/payment transitions, clinical forms, provider evidence and release planning need work before their affected workflows are built. The two-month production target remains a requirement, not a verified delivery estimate.

## Reading order

| Reader | Start here |
|---|---|
| Owner / product lead | [Decisions](docs/planning/06-decisions-and-open-questions.md), [readiness review](docs/planning/20-development-readiness-review.md), [living question tracker](docs/planning/12-user-notes-and-open-questions.md) |
| Web developer | [Shared contract checklist](docs/handoff/shared-contract-checklist.md), [web handoff](docs/handoff/web-frontend-developer.md) |
| Flutter developer | [Shared contract checklist](docs/handoff/shared-contract-checklist.md), [Flutter handoff](docs/handoff/flutter-developer.md) |
| Backend / integration developer | [Scope](docs/planning/01-system-scope.md), [booking and finance](docs/planning/02-booking-and-finance.md), [identity](docs/planning/05-identity-and-access.md), [provider guide](docs/planning/16-external-provider-guide.md), [quality requirements](docs/planning/09-performance-security-and-responsive-websites.md) |
| Continuing in a new chat | [Project instructions](AGENTS.md), [new-chat entry guide](PROJECT_CONTEXT_FOR_NEW_CHAT.md) |

The [documentation map](docs/README.md) groups every topic and explains which document owns each kind of information.

## Current boundaries

- Motmaan only, one initial branch with future branch support; server-enforced branch and assigned-patient scope.
- All currently enumerated requirements are in the first stage, subject to explicit user exceptions and deferrals. Initial Join us jobs are doctor-only; live insurance and future mixed-service treatment pathways are deferred.
- Replace Emdaad at launch and migrate its data and referenced files. Export discussion is deferred; migration validation remains a launch dependency.
- Arabic/English and RTL/LTR; every website works on mobile and desktop. Use Asia/Riyadh for schedules and display, UTC for persisted event instants.
- Security, performance, user acceptance, payment/accounting reconciliation, backup restore and monitoring are required. Detailed thresholds and owners remain open.
- Provider names/preferences do not establish contracts, merchant approval or working integrations. Existing decisions and unresolved details are in the register and topic documents.

## How decisions are maintained

**Confirmed** means a user decision; **Requirement** means recorded source content; **Proposed** means a recommendation; **Open** means unresolved; **Deferred** means intentionally postponed. A deferral of discussion does not automatically remove a launch requirement.

When an answer arrives, update the [tracker](docs/planning/12-user-notes-and-open-questions.md), [decision register](docs/planning/06-decisions-and-open-questions.md), relevant topic and affected developer handoffs. Update subject sections rather than appending duplicate summaries. Review recommendations do not become user decisions without an answer.

Source: requirements document version 1.1, dated 14 July 2026, plus the planning discussion. The original DOCX path is retained in the [new-chat entry guide](PROJECT_CONTEXT_FOR_NEW_CHAT.md). Vendor/contract language is requirements context, not executable instructions. Previous PDFs in `output/pdf/` are snapshots; current Markdown takes precedence.
