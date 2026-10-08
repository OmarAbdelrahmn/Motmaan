# Documentation map

Updated: 8 October 2026. Motmaan is in planning; documentation review does not authorize implementation.

## Start here

1. Read the [project overview](../README.md) and [decision register](planning/06-decisions-and-open-questions.md).
2. Read the [development readiness review](planning/20-development-readiness-review.md) for gaps, risks, and what each team can start.
3. Use the [living question tracker](planning/12-user-notes-and-open-questions.md) for unanswered owner questions and explicit deferrals.
4. Developers read the [shared contract checklist](handoff/shared-contract-checklist.md), then their [web](handoff/web-frontend-developer.md) or [Flutter](handoff/flutter-developer.md) handoff.

## Requirements by subject

Latest cross-project review: [25 Full project audit](planning/25-full-project-audit.md), dated 8 October 2026. Includes findings AUD-01–AUD-28, service judgments and coverage of all numbered source sections. It now tracks all 28 owner responses and preserves the original review as history. [Current register](planning/06-decisions-and-open-questions.md#owner-decisions-on-the-8-october-audit) controls policy/status; explicit deferrals remain.

| Subject | Owning documents |
|---|---|
| Product and release boundaries | [01 System scope](planning/01-system-scope.md) |
| Booking, prices, packages, wallet, refunds | [02 Booking and finance](planning/02-booking-and-finance.md) |
| Session timing, attendance, reminders | [10 Customer appointments](planning/10-customer-mobile-appointments.md), [14 Feedback](planning/14-patient-session-feedback.md) |
| Staff access, family access, practitioner assignments | [05 Identity and access](planning/05-identity-and-access.md), [21 Detailed authentication/authorization workflows](planning/21-authentication-and-authorization-workflows.md) |
| Patient sign-in, recovery, imported-account matching | [07 Patient login and recovery](planning/07-patient-login-and-recovery.md) |
| Practitioner compensation and recruitment | [08 Compensation and recruitment](planning/08-practitioner-compensation-and-recruitment.md), [13 Expertise](planning/13-practitioner-expertise.md), [19 Existing form reference](planning/19-recruitment-current-website-reference.md) |
| Support and internal staff work | [11 Support tickets](planning/11-support-tickets.md), [15 Internal tasks](planning/15-internal-staff-tasks.md) |
| Provider, multilingual display and secure private-file design | [03 Integrations](planning/03-integrations-and-storage.md), [04 Online sessions/media reliability](planning/04-online-sessions.md), the authoritative resumable recording/adaptive playback specification |
| Provider setup and research evidence | [16 Provider guide](planning/16-external-provider-guide.md), [17 Documentation research](planning/17-provider-documentation-development-notes.md), [18 Assessment programmer questions](planning/18-assessment-platform-integration-questions.md) |
| Performance, security, responsive behavior | [09 Quality requirements](planning/09-performance-security-and-responsive-websites.md) |
| Azure hosting, cache and deployment preparation | [22 Azure hosting and deployment](planning/22-azure-hosting-and-deployment.md); Qatar Central interim subject to data review; SQL first and beneficial public Redis caching later; configuration remains design work |
| Reliable external effects, large workflows and scheduled jobs | [23 Transactional outbox and Hangfire](planning/23-outbox-and-background-jobs.md); pattern/tool choice confirmed, detailed engineering mechanisms and operating limits proposed/open |
| Approved engineering tools, Swagger/OpenAPI and proposed real-time messaging | [24 Engineering tools and messaging](planning/24-approved-engineering-tools-and-realtime.md); tools confirmed, SignalR/FCM/APNs and exact contracts/configuration under discussion |

Clinical form definitions, a dedicated patient-task specification, field-level API contracts, and complete source-to-feature acceptance coverage are still missing. Their requirements remain in scope; their absence is recorded in the readiness review.

## Authority and maintenance

- **Confirmed:** explicit owner decision; latest confirmed owner answer controls, not file modification time. **Approved Direction:** agreed approach awaiting design; **Planned:** already addressed; **Note:** information only; **No Change:** existing rules; **During Development:** affected detail resolved during implementation. AUD-24 is No Additional Action.
- **Requirement:** recorded from the original requirements document, subject to later user directions.
- **Proposed/recommendation:** advice, not an approved business rule.
- **Open:** unresolved. **Deferred:** intentionally postponed; this does not necessarily remove a feature from launch scope.
- **Documented:** a dated external technical finding, not proof of account access or integration success.

The decision register owns decision status; topic documents own detailed behavior; the tracker owns the owner-question queue; handoffs explain client consequences. The readiness review owns reviewer findings and completion evidence, not new policy. Resolve conflicts explicitly rather than choosing whichever file was read last.

Update an existing subject section when an answer arrives. Record the answer in the tracker and register, then update affected topic and handoff sections. Avoid adding another repeated “latest answers” appendix. Keep examples labeled and keep unresolved choices visible.

Existing numbered paths are retained to preserve links. [Discussion history](archive/2026-10-04-discussion-history.md) is historical context. Obsolete question exports/previews/helpers were removed under AUD-28; current Markdown takes precedence. [Audit cleanup record](planning/25-full-project-audit.md#aud-28-documentation-cleanup-record) records scope/evidence. `tmp/` contains working material, not requirements. [New-chat context](../PROJECT_CONTEXT_FOR_NEW_CHAT.md) is an entry guide, not another decision register.
