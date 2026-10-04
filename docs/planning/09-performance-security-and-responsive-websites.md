# Performance security and responsive websites

Updated: 3 October 2026. The user confirmed performance and security as priorities and required all websites to work well on mobile and desktop. The detailed engineering controls below are proposed implementation standards, not claims of tested behavior.

## Implementation approach

Use the api-pattern skill at `C:/Users/omarf/.codex/skills/api-pattern/SKILL.md` when implementation is requested. Follow controller, service/use-case, Result/Error, DTO validation, and EF Core patterns. Load the relevant module-boundary, data/performance, reliability, and verification references for each change. Historical example packages and project names in the skill are not automatic project decisions.

No scaffolding, endpoints, migrations, or deployment have been created. The database engine, .NET version, job system, and hosting arrangement remain open.

## Performance design

- Apply trusted authorization scope, filtering, ordering, and bounded pagination in SQL before loading results.
- Project only fields needed by the caller. Use AsNoTracking for read-only entity queries and avoid unnecessary navigation graphs and N+1 access.
- Add indexes for measured filter/order patterns; inspect generated SQL and representative execution plans. Index every column is not a strategy.
- Avoid a single patient-page response containing all clinical history, financial history, files, and messages. Load authorized sections through bounded queries.
- Evaluate availability over a bounded date range, with efficient schedule and overlap lookups. Revalidate capacity transactionally when reserving; cached availability cannot authorize a booking.
- Use short transactions and bounded concurrency. Never run simultaneous EF operations on the same DbContext.
- Keep external provider calls out of database transactions. Move report generation, imports, large exports, recording post-processing, and durable notifications into appropriate background workflows.
- Cache public catalog and brand content where useful, with invalidation rules. Do not share patient or staff data across users through cache keys or public caching.
- Use managed private storage for large files and direct supported recorder delivery; do not route all video bytes through normal API requests.
- Measure response latency, query cost, memory, resource utilization, job backlog, and provider failures under representative data before adding infrastructure.

Agree measurable endpoint and frontend budgets, including percentile latency, payload size, concurrency, and error-rate targets. No numeric performance promise has been approved. Use the expected 10,000-plus patient histories and growth assumptions for planning, not just empty-database demonstrations.

## Security design

Enforce identity, portal assurance, action permission, and resource scope on every applicable workflow. Protect exports and file access as well as screen data. Keep staff authentication distinct from patient OTP and recovery. Promptly invalidate permission changes and revoked sessions.

Validate requests and database constraints. Use transaction/concurrency protection for overlapping bookings, wallet spending, package consumption, and compensation updates. Authenticate provider callbacks, deduplicate retryable effects, and reconcile ambiguous outcomes.

Keep files private by default, scope upload and download grants, validate content, and scan untrusted uploads before access. Candidate attachments do not inherit medical-record visibility. Keep secrets in approved server-side configuration and exclude secrets, OTPs, and unnecessary health data from logs.

Rate-limit expensive public, login, recovery, recruitment, upload, and payment operations based on their risks and deployment topology. Per-instance limits must not be described as global limits without shared enforcement. Protect cookie-based actions against CSRF where applicable; finalize browser session design before choosing controls.

Protect audit integrity, backups, retention jobs, and recovery procedures. Use safe errors with trace references and production diagnostics that do not leak private information. A Saudi storage region is an infrastructure choice, not by itself a complete assurance of regulatory compliance.

## Responsive public and authenticated websites

The mobile/desktop requirement applies to the main branded website, Join us forms, patient booking and account pages, management dashboard, specialist dashboard, and video-session screens. Tablet support from the source remains included.

Plan layouts and interactions for narrow and wide screens, Arabic RTL and English LTR, touch and keyboard use, clear labels, readable type, and accessible focus behavior. Adapt dense tables and calendars without making permissions or important actions disappear. Keep upload, verification, booking/payment, and session flows usable on a phone.

Serve appropriately sized images, load recordings on demand, keep JavaScript and large dependencies bounded, and measure page behavior on representative mobile networks/devices. Public brand assets may use public caching; authenticated medical and financial responses need appropriate private cache policies.

Branding interpretation: display the center's name, logo, and identity consistently on public pages. Exact design, content management permissions, assets, and frontend stack remain open.

## Confirmed production-readiness checks

All proposed checks are required: security, user acceptance, payment/accounting reconciliation, successful backup restoration, representative performance verification, and monitoring. The two-month target does not prove readiness. Exact thresholds, sign-off owners, and milestones remain open.

Proposed acceptance coverage includes branch restrictions on queries, reports, exports, files, and background workflows; no clinical or financial privilege gained from internal task assignment; employed-doctor priority and external-doctor fallback. These are future checks, not verified implementation behavior.

## Verification when implementation starts

Use meaningful authorization, ownership, concurrency, retry, and business-rule tests for affected workflows. Use the real database provider for provider-specific transaction and query behavior. Check performance with representative histories and peak usage. Verify critical flows on mobile and desktop with RTL/LTR and keyboard/touch use. Repeat checks when changes justify it rather than adding boilerplate tests that mirror the implementation.

Acceptance should include denied direct API access, cross-patient identifier substitution, stale permission revocation, duplicate webhook processing, contested booking, safe recruitment uploads, repeated candidate acceptance without duplicate doctor accounts, SMS delivery retries, monthly incentive threshold crossing and refund corrections, contact recovery boundaries, and measurable booking/search/report performance. Define exact acceptance thresholds before claiming completion.

## References

- [EF Core efficient querying](https://learn.microsoft.com/en-us/ef/core/performance/efficient-querying)
- [OWASP authorization guidance](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html)
- [OWASP file upload guidance](https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html)
