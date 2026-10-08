# Motmaan full planning and service architecture audit

Reviewed and owner responses applied: 8 October 2026. **Current tracker above historical original review. Planning only; no application remediation/tests claimed.**

## Current owner-response tracker

The owner responded to all 28 findings. [Decision register](06-decisions-and-open-questions.md#owner-decisions-on-the-8-october-audit) owns authority, linked updates, remaining work/dependencies and deferrals. Status here records owner disposition, not implementation completion.

| Audit ID | Owner-defined status | Current disposition |
|---|---|---|
| AUD-01 | Confirmed | Latest confirmed owner decision controls; reconcile stale summaries. |
| AUD-02 | Approved Direction — Progressive Discovery | Preserve full scope; refine features progressively. |
| AUD-03 | Planned | Preserve established delivery arrangements and two-month target. |
| AUD-04 | Note | Keep Wati under evaluation; verify Saudi transactional SMS. |
| AUD-05 | Confirmed | Azure Qatar Central interim; verified Saudi region long term. |
| AUD-06 | Confirmed — Critical Requirement | Recording readiness gate; reliable resumable ingestion and adaptive playback. |
| AUD-07 | Deferred | Preserve MyFatoorah; mobile purchase classification later. |
| AUD-08 | Confirmed | Mandatory stronger verification/MFA and sensitive-action step-up. |
| AUD-09 | Confirmed — Important Clarification | Role defaults plus explicit individual allowed/removed overrides. |
| AUD-10 | Deferred | Preserve confirmed identity/family/consent rules. |
| AUD-11 | Deferred | Keep seven-minute holds/payment/package/free-visit rules. |
| AUD-12 | Confirmed | Block extension if affected doctor or room has a later booking. |
| AUD-13 | Approved Direction | Immutable financial ledger/corrections and reliable reconciliation. |
| AUD-14 | During Development | Keep formulas; settle compensation boundaries during affected development. |
| AUD-15 | Confirmed | Mandatory version history for clinical reports/relevant medical documents. |
| AUD-16 | Confirmed — Requirement Clarification | Suitable dynamic data follows selected interface language; preserve originals. |
| AUD-17 | Deferred | Integrate existing assessment platform when development reaches it. |
| AUD-18 | No Change | Recurring patient-task changes affect future occurrences only. |
| AUD-19 | Confirmed Clarification / Otherwise No Change | Reception may perform authorized operational closure if doctor forgets. |
| AUD-20 | Deferred | Detailed SignalR event design later; selection stays proposed. |
| AUD-21 | Confirmed | Optimize/measure SQL first, selective Redis public caching later. |
| AUD-22 | Approved Direction | Keep outbox/Hangfire with durable dispatch, retries and crash recovery. |
| AUD-23 | Confirmed — Align With AUD-06 | Secure resumable private-file lifecycle; shared media specification. |
| AUD-24 | No Additional Action | No new broad UI/parity redesign; preserve approved functionality/Figma. |
| AUD-25 | Deferred | Preserve Emdaad replacement/full migration at launch. |
| AUD-26 | Approved Direction | Document practical measurable planning targets and operational reports. |
| AUD-27 | Note | Future recommendations within salaried practitioner group only. |
| AUD-28 | Confirmed — Delete Obsolete Artifacts | Delete obsolete question-export helpers/PDFs/previews; repair table rows. |

Documentation actions have been applied; feature/provider evidence remains future work. AUD-03 is Planned because existing delivery arrangements are acknowledged; the original audit's missing-plan conclusion below is not the current owner status. AUD-28 cleanup is recorded at the end.

## Historical original audit — 8 October 2026

**Everything in the original assessment, findings, service judgments and recommendations below is retained as review history.** It records the pre-response state and must not override the owner responses above. In particular, earlier optional privileged verification, allowed overlapping extensions and undecided interim region have been superseded. Deferred recommendations are not execution instructions.

## Original assessment

The selected ASP.NET Core/EF Core modular monolith, Azure SQL, server authorization, transactional outbox, Hangfire, and shared web/Flutter contracts are a sensible foundation. Replacing the stack would not solve the main problems. The largest risks are incomplete business transitions, conflicting summaries, unproven provider arrangements, and a broad launch commitment without a resourced delivery plan.

The project is ready for detailed design and contract preparation. It is not ready for an unrestricted full-product implementation handoff. Each workflow needs its own agreed behavior and evidence before implementation; unrelated design work can continue. No application or provider behavior has been tested in this review.

My strongest recommendations are to resolve documentation drift, review privileged staff verification, prove SMS and recording/hosting fit early, classify mobile purchases by product, and settle booking/finance transitions before building them. Keep the confirmed stack; avoid treating each approved tool as something that must be provisioned immediately.

## Coverage and evidence limits

- Reviewed the 32 Markdown files present at the start: root instructions/entry guides, documentation map, planning documents 01–24, all three developer handoffs, and the discussion archive. The source and current files were compared by subject, including conflicting confirmed/proposed/deferred labels.
- Read the text and table content of the original requirements DOCX, version 1.1 dated 14 July 2026, at the path recorded in [the entry guide](../../PROJECT_CONTEXT_FOR_NEW_CHAT.md). Source section numbers below refer to its headings, not guessed page numbers. This was a semantic requirements review, not a Word layout audit. Vendor/contract instructions were treated as context only.
- Inventoried the three historical PDF exports and their PNG previews. Their formatting was not re-audited and they were not regenerated. Reviewed the supporting Python helpers as historical export/update machinery; checked their syntax without executing their mutations.
- Checked local Markdown link targets and table column consistency. Initial result: no missing local file targets; two over-wide rows in the shared contract checklist. This check does not prove external URL health or every heading fragment.
- Rechecked selected official provider documentation where it could change a recommendation: Azure Saudi announcement, Agora storage, Wati/Twilio SMS, MyFatoorah payment methods, mobile purchase rules, caching, job scheduling and SignalR scaling. Other dated provider research remains evidence to refresh before integration, not newly tested account capability.
- No application projects, APIs, schema, automated application tests or deployed environments were found in the project inventory. Findings are planning defects, design risks and missing contracts, not demonstrated production vulnerabilities.
- The working tree already contained substantial modified planning files and untracked documents 22–24. This audit preserves that work. It does not change confirmed business rules, select a provider, reopen deferred questions or authorize implementation.

Severity: **High** = can cause incorrect access/money/care behavior, major rework or blocked release; **Medium** = material design/operations gap before its workflow or launch; **Low** = documentation usability. Confidence concerns the observed gap, not a prediction that an incident will occur. Owners listed below are suggested responsibilities, not assigned people or permission grants.

## Original findings

### AUD-01 — High — Current summaries contradict resolved decisions

**Evidence:** [New-chat guide, Current selected discussion](../../PROJECT_CONTEXT_FOR_NEW_CHAT.md) still says no provider accounts exist and recommends Tap-first evaluation. [Provider guide P01](16-external-provider-guide.md) says none are currently available although its introduction/P05 records the reported ready MyFatoorah account. The provider-guide row in [the decision register](06-decisions-and-open-questions.md) repeats the old inventory. [Integration note, Supporting services](03-integrations-and-storage.md) and [Wati research](17-provider-documentation-development-notes.md) still call patient SMS versus WhatsApp-first open. SMS is confirmed in document 21. The [web handoff](../handoff/web-frontend-developer.md) calls all self-change safeguards proposed despite confirming password plus existing-phone SMS at its top. Documents 01, 08 and 15 retain blanket deferred-access/deactivation statements superseded in 21. The tracker repeats older proposed-change-safeguard wording in its resolved notes.

**Impact:** A new developer can select the wrong payment direction, design WhatsApp login, omit a confirmed security check or delay a resolved behavior depending on which summary they read.

**Recommendation:** Correct these statements from the existing confirmed decisions, date historical inventory explicitly, and replace repeated policy paragraphs with references to one owning section. Keep unresolved evidence, detailed permission defaults and deactivation continuation limits open. The blanket source late-change language in document 02 also needs a superseded label: it must not reintroduce patient changes inside 24 hours.

**Closure:** Documentation owner reconciles these exact locations; searches for old provider/channel/deferral wording return only clearly labeled history. Confidence: high. Existing review R02/R03/R09, with new concrete drift examples.

### AUD-02 — High — Broad first-stage scope has no complete acceptance inventory

**Evidence:** [Scope](01-system-scope.md) includes all enumerated requirements with explicit exceptions, but its feature table is much shorter than source sections 5–30. Examples not sufficiently represented in detailed contracts include fixed therapeutic worksheets, requested stamped reports, staff POS/cashbox operations, performance alerts, setup/tutorial flows, recorded training courses and predictive analytics. The source coverage table later in this review identifies these rather than silently removing them.

**Impact:** Teams can finish their handoff lists and still omit paid-for or expected capabilities. Conversely, a broad phrase can cause substantial unestimated work.

**Recommendation:** Create a feature inventory with source section, current user override, owning module, surfaces, state contract, acceptance examples, owner and release dependency. Mark source-only details unresolved for reconciliation. Do not equate doctor recruitment with the full marketplace or normal sessions with group/recorded courses. Do not invent insurance work from superseded source requirements.

**Closure:** Product owner and leads review the inventory and explicitly settle ambiguous scope. Confidence: high. Extends R01.

### AUD-03 — High — The two-month target has no credible delivery basis yet

**Evidence:** [README](../../README.md), [scope](01-system-scope.md) and [readiness review](20-development-readiness-review.md) retain the two-month production target, full Emdaad replacement and broad release. Team capacity, estimates, owners, provider lead times and sign-offs are absent. Source section 31 requires approved Figma designs before development; handoffs permit isolated presentation work after its design baseline, without fully reconciling whole-project versus workflow design approval.

**Recommendation:** Estimate complete journeys with actual staffing and external dependencies. Agree design approval granularity explicitly. Use workflow milestones and release evidence; do not promise the date from a list of tools. If the forecast misses the target, present scope/date/staffing options for owner decision. My recommendation is staged internal delivery and rehearsal, while preserving the currently confirmed launch scope until changed.

**Closure:** Named team, dependency-based schedule, design approval record and launch sign-off owners. Confidence: high. Extends R14.

### AUD-04 — High — Wati should not be the default SMS choice without a proven domestic route

**Evidence:** P02 in [provider guide](16-external-provider-guide.md) remains unverified. Wati's documented Twilio option requires its Business plan and an active Twilio account; it documents campaigns/fallback. Twilio states that domestic-brand sender registration is unsupported through its route. This is a concrete suitability concern for Motmaan, not proof that every possible Wati arrangement fails. [Wati setup](https://support.wati.io/en/articles/11694867-how-to-integrate-wati-with-twilio), [Twilio Saudi guidance](https://www.twilio.com/en-us/guidelines/sa/sms).

**Recommendation:** Keep Wati evaluated for WhatsApp, but prefer a proven Saudi transactional SMS route for authentication/invitations if Wati cannot demonstrate one. Evaluate actual API calls, registered sender, Arabic delivery, receipts, invitation URLs, expiry and cost. Keep one backend-owned challenge lifecycle behind a small delivery adapter. Do not route urgent OTP through campaign logic or an unbounded fallback chain.

**Closure:** Integration owner supplies account-specific route confirmation and authorized synthetic delivery evidence across intended Saudi networks. Confidence: high on missing evidence; suitability remains conditional. Extends R09/P02.

### AUD-05 — High — Saudi Azure deployment remains a schedule dependency

**Evidence:** [Azure plan](22-azure-hosting-and-deployment.md) correctly marks service availability open. Microsoft's announcement specifies November 2026, which is future relative to this 8 October review. It does not prove that every chosen service/tier will be available to Motmaan. [Microsoft announcement](https://news.microsoft.com/source/emea/2026/08/microsoft-announces-saudi-arabia-east-datacenter-region-will-be-available-in-november-2026/).

**Recommendation:** Keep the selected Azure SQL/Redis direction, but require service-by-service availability, subscription access, networking, cost and recovery evidence before promising production hosting. Prepare a dated decision point and an owner-reviewed contingency if a required service is unavailable. Synthetic development elsewhere is an option, not permission to move patient data. Count all resources: worker, web hosting, network/private endpoints, monitoring workspace, backups and any real-time service exceed the five grouped plan items.

**Closure:** Infrastructure lead produces a deployable topology and budget with no unknown mandatory region/service dependency. Confidence: high. Extends P10/R14.

### AUD-06 — High — Recording is a clinical workflow gate, not just a storage integration

**Evidence:** [Recording design](04-online-sessions.md) makes recording mandatory but leaves consent refusal, failed startup, mid-call failure and abandoned sessions open. Its sequence joins participants before starting the recorder; prose separately warns against clinical conversation before readiness. The exact center-owned-storage interpretation and fallback processing remain unresolved.

**Recommendation:** Add an explicit waiting/readiness state to the sequence and UI before clinical conversation starts. Agree interruption/continuation actions with the clinical owner, preserving the mandatory-recording decision. Validate Agora before replacing it; its current storage reference includes Microsoft Azure as a supported vendor option, so Azure should not be described as categorically unsupported. That does not prove the exact Saudi bucket, firewall, credentials, media processing or fallback arrangement. Prefer a supported direct recording path; assess alternatives only against unmet constraints. [Agora storage reference](https://docs.agora.io/en/realtime-media/cloud-recording/reference/region-vendor).

**Closure:** Approved failure table plus future synthetic web/iOS/Android evidence covering readiness, interruption, complete assets, restricted playback and deletion. Confidence: high. Extends R08/P07.

### AUD-07 — High — A single mobile checkout policy cannot be assumed for every product

**Evidence:** MyFatoorah is selected across the patient clients, while source sections 18.9 and 26 also include paid assessments and group/recorded training. [Flutter handoff](../handoff/flutter-developer.md) does not classify these purchases. Apple distinguishes real-time one-to-one services from one-to-many services and digital content. Google describes conditions for its one-to-one exemption including replay availability in a Play-distributed app. [Apple purchase rules](https://developer.apple.com/app-store/review/guidelines/#person-to-person-services), [Google Play payment guidance](https://support.google.com/googleplay/android-developer/answer/10281818).

**Recommendation:** Build a product/platform purchase matrix for in-person care, live one-to-one care, assessments, group sessions and recorded courses, including bundles. Do not infer that private staff-only quality recordings automatically invalidate an exemption; assess who can replay them and where. Record the applicable store route and evidence before coding checkout. Do not add in-app purchases or website workarounds by assumption.

**Closure:** Mobile lead and owner approve product classification for intended storefronts and implementable checkout contracts. Confidence: high on the missing classification; final store treatment is unverified. Extends R13 with a concrete scope dependency.

### AUD-08 — High — Optional verification is a weak default for privileged staff

**Evidence:** [Authentication WF-AUTH-02](21-authentication-and-authorization-workflows.md) explicitly allows every staff member to disable SMS verification, including privileged administrators. The password/existing-phone proof protects the setting change, but future privileged logins can still use only a password.

**Recommendation requiring a user policy change:** Require stronger verification for access administrators, clinical/recording access and sensitive finance actions. Evaluate phishing-resistant authenticators/passkeys for staff, with controlled recovery; retain the existing patient OTP choice unless separately revised. A step-up before a refund or grant change is also worth considering. This recommendation does not silently override the confirmed self-managed SMS policy. [OWASP MFA guidance](https://cheatsheetseries.owasp.org/cheatsheets/Multifactor_Authentication_Cheat_Sheet.html).

**Closure:** Owner chooses the privileged-account policy; backend lead documents enrollment, recovery, device loss and sensitive-action checks. Confidence: high on the policy tradeoff, not a finding of an implemented bypass.

### AUD-09 — High — Permission granularity needs an understandable evaluator

**Evidence:** [Identity](05-identity-and-access.md) and [A06](21-authentication-and-authorization-workflows.md) confirm endpoint actions, role baselines and individual customization, but leave multi-role precedence, removals, delegation ceilings and some sensitive-grant boundaries open.

**Recommendation:** Keep the required endpoint coverage. Use a stable developer-maintained action catalog grouped by business function in the management UI; avoid presenting hundreds of raw route names. Draft explicit precedence, with deny/removal behavior and examples, for owner review. Show inherited, added, removed and effective permissions. Define grant expiry, delegation limits and audit; test two same-role staff with different permissions. Do not use a generic service-level edit flag or administrator wildcard. Avoid turning the application into a general-purpose policy language before there is a need.

**Closure:** Reviewed evaluator truth table, minimum per-workflow matrix and revocation tests. Confidence: high. Extends R03/A06.

### AUD-10 — High — Identity and family relationships need evidence and lifecycle contracts

**Evidence:** [Patient identity](07-patient-login-and-recovery.md) and [WF-AUTH-01/08](21-authentication-and-authorization-workflows.md) establish good boundaries, but evidence checklists, duplicate/recycled contacts, guardian rules, consent duration, self-exit and transfer effects remain open.

**Recommendation:** Separate the authenticating account, beneficiary, payer, guardian/representative, family membership and clinical consent. Do not collapse them into one family-owner flag. Keep verified import links distinct from candidate matches. Define identity correction/merge review, retention of source IDs, consent withdrawal and notifications to former delegates. Specify the restricted deactivated-doctor continuation, including an abandoned encounter and session expiry, so an unclosed consultation cannot preserve indefinite access.

**Closure:** Operations/clinical owner approves evidence and lifecycle examples; backend/web/Flutter share the contract. Explicitly deferred subtopics stay deferred and their dependent work waits. Confidence: high. Extends R03/R04/A04/A09/A10.

### AUD-11 — High — Booking and payment have no complete transition contract

**Evidence:** [Booking](02-booking-and-finance.md) has a seven-minute hold and trusted payment confirmation but room-capacity guarantee, staff cash reservation and late payment remain deferred. The diagram can appear more settled than the text. Package and free visits also cannot require a new payment simply because they use the booking endpoint.

**Recommendation:** Create separate booking, payment-attempt, attendance and entitlement states with explicit transitions for self-service, reception, package and free visits. Reserve suitable room capacity atomically while retaining reception's confirmed named-room selection. Define how this works with room types and fragmented availability; a total-room count alone can miss interval conflicts. Select the capacity guarantee policy before implementation. Preserve old reservation rights during rescheduling until the replacement/price difference has a defined outcome.

**Closure:** Operations/finance settle the deferred rules when they return to them; developers supply examples for last-slot races, delayed provider success, duplicate callbacks, cash arrival and failed reschedule. Confidence: high. Existing R05/R06, not newly reopened questions.

### AUD-12 — High — Allowed overruns conflict with physical capacity unless modeled separately

**Evidence:** [Appointment timing](10-customer-mobile-appointments.md) allows an extension into the next booking without moving it. [Booking](02-booking-and-finance.md) requires protected room/practitioner capacity and retains booked times. Actual start, actual end and documentation completion are distinct but incomplete.

**Recommendation:** Preserve planned reservation times separately from actual occupancy and documentation state. A permitted overrun must raise an operational conflict for both practitioner and room, including the next appointment for a different doctor in that room. Agree who resolves it and what the next patient sees. Stop occupancy warnings at clinical end and use a separate documentation reminder if the owner accepts that proposal. Do not automatically shift appointments or bill extensions.

**Closure:** A timeline example covers late start, extension, occupied room, next patient arrival, actual end and later Finished. Confidence: high. Extends R07.

### AUD-13 — High — Wallet and refunds require complete ownership and reconciliation rules

**Evidence:** [Finance](02-booking-and-finance.md) distinguishes transactions and credit origin but leaves mixed funds, payer/beneficiary ownership, negative package refund remainder, tax/rounding, failed payouts and price differences open. Payment/BNPL accounts are owner-reported ready; connection ownership is unverified.

**Recommendation:** Keep an auditable ledger with immutable entries and corrective entries, funds reserved for payouts, and separate total/spendable/withdrawable amounts. Map each provider operation to exactly one Motmaan operation; do not let gateway and direct BNPL paths both capture or refund it. Prefer a supported provider checkout to custom card handling. MyFatoorah's method list is account-dependent and lists Tamara; it does not establish Tabby for Motmaan. [MyFatoorah methods](https://docs.myfatoorah.com/docs/choose-your-payment-integration).

Add chargeback/dispute and unknown-outcome cases to the finance contract. Keep verified payment, settlement, Qoyod issuance and payout execution distinct. Finance must decide what Qoyod receives for wallet-related liabilities and reconciliation; the source's operational-wallet separation does not answer accounting treatment. No tax ruling is made by this audit.

**Closure:** Finance-approved worked examples balance money, entitlements and external references under retries, partial refunds, mixed credit and failures. Confidence: high. Extends R06/P05/P06.

### AUD-14 — Medium — Compensation is underspecified at period boundaries

**Evidence:** [Compensation](08-practitioner-compensation-and-recruitment.md) gives a correct above-target formula but leaves paid/completed month attribution, mid-month changes, refunds after close and full-payroll scope open. The source also mentions a fixed-amount-per-service alternative after target; its current status is not reconciled explicitly.

**Recommendation:** Prefer an auditable period statement based on effective-dated terms and eligible service facts over continually overwriting a cumulative amount. A running estimate can remain provisional. Select how corrections affect a closed period, and distinguish earned, approved and paid. Keep package refund repricing separate from session revenue allocation. Do not turn compensation reporting into a payroll engine without a scope decision.

**Closure:** Finance reviews threshold crossing, late payment, later refund, practitioner transfer, rounding and source alternative status. Confidence: high. Extends R06.

### AUD-15 — High — Clinical documents need versioned content and professional eligibility

**Evidence:** [Scope](01-system-scope.md), [clinical access](05-identity-and-access.md) and the web handoff permit direct report edits and direct prescription issuance, with qualifications and history required but no field dictionary. Source 11.1 includes vital signs, symptoms, diagnosis, treatment, templates, stamps/signatures and PDF delivery; 18.10 adds report requests and tracking.

**Recommendation:** Keep the confirmed direct-edit experience, but preserve protected immutable content versions beneath it. A prior exported PDF/signature must still identify its content version; changing the current report must not falsely validate an old artifact as current. Define drafts, signing/issuance, correction reason, concurrent editing and patient-visible revision behavior. Specify professional eligibility by practitioner type, license validity and action; the shared doctor role alone cannot decide prescribing authority.

**Closure:** Clinical lead approves form/report/request inventory and examples; developers define versions, access, signature meaning and stale-edit outcomes. Confidence: high. Extends R10.

### AUD-16 — Medium — Translation scope and report review have drifted from the source

**Evidence:** Source 4.2 describes automatic translation of Arabic-entered data, language choice before report issuance, and the ability to review/edit medical translations. Current [integration](03-integrations-and-storage.md) and handoff language concentrates on imported data and calls clinical review a recommendation; the web handoff specifies side-by-side display despite presentation being deferred.

**Recommendation:** Record separately: confirmed imported-data translation, broader source-entered-data coverage to reconcile, source report-language/review capability, and the still-proposed mandatory review policy. Preserve Arabic and source versions; distinguish machine draft from clinician-approved translation. Translate approved categories only, with approved provider data handling. Do not silently narrow the source or invent the deferred presentation.

**Closure:** Product/clinical owner reconciles source coverage when returning to translation; fields, provenance, retranslation and review status are specified. Confidence: high. Extends R01/R10; deferral preserved.

### AUD-17 — High — Assessment integration has no technical contract yet

**Evidence:** [Document 18](18-assessment-platform-integration-questions.md) is a good questionnaire, but name/API/sandbox/SSO/result/payment behavior are still unknown. Source 24.2 includes ordering-practitioner attribution and commission implications.

**Recommendation:** Do not rebuild the platform or use a WebView as proof of integration. Obtain a complete synthetic journey, stable external identifiers, revocable beneficiary access, payment owner, attempts, result versions/corrections and failure recovery. Commission eligibility for an assessment requires its own completion rule. A maintained server adapter is sufficient; avoid speculative SSO infrastructure before the actual protocol is known.

**Closure:** Assessment programmer and integration lead provide a reviewed contract and later test evidence. Confidence: high. Existing R09/P09.

### AUD-18 — Medium — Patient tasks need an occurrence model and missing source capabilities

**Evidence:** Documents [01](01-system-scope.md), [10](10-customer-mobile-appointments.md) and both handoffs describe recurrence and future-only edits. They do not define completion cutoffs, late/backdated entries, summary denominators, transfer ownership or task attachments fully. Source 12 also includes fixed therapeutic worksheets, low-adherence alerts, administrative adherence views and team follow-up.

**Recommendation:** Distinguish task definition/version, scheduled occurrence, response and reminder. Define what counts as future when today's occurrence exists or a reminder was sent. Keep history stable after edits and practitioner transfer. Compute progress from a documented denominator; missed, not yet due and excused must not be conflated. Keep administrative follow-up content within its authorization scope. Use the existing job system, not a new workflow engine.

**Closure:** Clinical/product owner reviews daily/weekly/one-time examples, missed reasons, worksheet visibility and weekly summaries. Confidence: high. Extends R11.

### AUD-19 — Medium — Feedback and task state machines contain unresolved edge cases

**Evidence:** [Feedback](14-patient-session-feedback.md) sends a request after Finished but expires eligibility 48 hours after actual end; delayed confirmation can make the invitation unusable. Email is optional for patients. [Tickets](11-support-tickets.md) allow unlimited-time reopening with one survey, but resolver attribution after reassignment/reclosure is undefined. [Internal tasks](15-internal-staff-tasks.md) leave multi-assignee completion deferred.

**Recommendation:** Preserve the deadline and one-survey rule; specify whether an expired invitation is suppressed and what users see. Define missing-email behavior. Snapshot the resolver associated with the eligible survey rather than changing history whenever ticket ownership changes. Model per-assignee progress separately from whole-task status once the deferred completion rule is chosen. Broad task-detail visibility means task authors must not paste otherwise restricted medical records into staff comments.

**Closure:** Product/operations approve transitions and examples without adding another survey entitlement or guessing shared-task completion. Confidence: high. Extends R07/R11.

### AUD-20 — Medium — SignalR is suitable, but event delivery needs a modest, complete contract

**Evidence:** [Real-time proposal](24-approved-engineering-tools-and-realtime.md) already handles durable recovery, duplicates and authorization. Still open: message/event taxonomy, recipients, ordering, read semantics, latency, retention, Flutter compatibility and worker-to-client publication.

**Recommendation:** Keep HTTP for durable commands/history and use live events to notify or refresh authorized state. Persist important inbox entries, not every transient presence/refresh event. Separate business event, notification, recipient read state and channel delivery attempts. Use one stable identity across push/live delivery. Define foreground push suppression carefully; connection presence is not proof of reading. Validate the Flutter candidate and choose one multi-instance publication path. A managed SignalR service is conditional on scale, region and operations, not automatically another required purchase. [SignalR scaling](https://learn.microsoft.com/en-us/aspnet/core/signalr/scale?view=aspnetcore-10.0).

**Closure:** Shared event contract and future device/reconnect/revocation evidence. Confidence: high. Extends R11/R12 and document 24.

### AUD-21 — Medium — Redis is selected before workload and operating cost are established

**Evidence:** [Azure/cache plan](22-azure-hosting-and-deployment.md) selects Redis but leaves tier/timing open. Source estimates are 25 practitioners, 60 daily appointments and 10,000-plus patient records. Those counts alone neither demand nor rule out Redis; concurrent usage, query cost and topology matter.

**Recommendation:** Preserve its selected status but delay provisioning/tier choice until a measured need or a specific shared-state requirement exists. Start by bounding/projecting/indexing SQL reads. Use approved public catalogs/profiles as initial cache candidates; keep money/capacity authoritative in SQL. Never repurpose an evictable cache as the only durable security or business store. HybridCache's per-instance coordination does not establish cross-server freshness. [HybridCache behavior](https://learn.microsoft.com/en-us/aspnet/core/performance/caching/hybrid?view=aspnetcore-10.0).

**Closure:** Technical lead documents each cache use, hit/miss benefit, freshness limit, outage behavior and monthly cost. Confidence: high on missing measurement; Redis itself is not a defect.

### AUD-22 — Medium — Outbox and Hangfire are sound but need one recovery design

**Evidence:** [Background design](23-outbox-and-background-jobs.md) correctly distinguishes SQL commit, enqueue and remote effects. Exact retry ownership, leases, worker allocation and latency remain open.

**Recommendation:** Keep the pattern selectively for durable work. Use the outbox for reliable dispatch and one defined retry owner for each failure stage; a dispatcher can recover missing/stalled jobs without competing with every Hangfire retry. Separate urgent readiness/OTP delivery from bulk reports/imports. Scheduled jobs check eligibility; they are not the authoritative clock. Hangfire's recurring scheduler uses a minute interval, so it is unsuitable as the only mechanism for near-immediate readiness alerts. [Hangfire recurring tasks](https://docs.hangfire.io/en/latest/background-methods/performing-recurrent-tasks.html).

Do not turn every ordinary read or small CRUD action into a pending background operation. Do not introduce a generic distributed workflow framework merely because a use case has several steps. Persist the actual business operation and provider references.

**Closure:** Backend lead specifies dispatch/retry transitions and proves crashes around commit, enqueue, external success and lease expiry. Confidence: high. Mostly positive design review with required completion work.

### AUD-23 — High — Private files need a complete access, network and lifecycle design

**Evidence:** [Storage](03-integrations-and-storage.md), [authentication](21-authentication-and-authorization-workflows.md) and [Azure](22-azure-hosting-and-deployment.md) already acknowledge short-lived links, revocation limits, scanning and private-network constraints. Exact architecture is unresolved, as are medical/recruitment retention and recording restore behavior.

**Recommendation:** Choose access per data class. Direct signed delivery can suit lower-risk approved files, while recordings may justify an authorization gateway or similarly controlled delivery where revocation requirements demand it. This is a tradeoff, not a promise to recall downloaded data. Cover every HLS asset, grant expiry, browser cache and actual access logging. Keep upload quarantine and scanning before access, including files received from integrations. Private endpoints must still permit the intended recorder/client path; signed URLs do not bypass a firewall.

Define retention by class, source event, versions/replicas/backups, deletion evidence and any approved hold process. Reconcile the source's immutable audit wording with retention/privacy requirements through the responsible owner; do not silently enable irreversible locks or universal deletion.

**Closure:** Infrastructure/security/clinical owners approve the data-flow and retention matrix; staging tests demonstrate authorized delivery, denied access and consistent restoration. Confidence: high. Extends R08/R13/R14.

### AUD-24 — Medium — UX and client parity are requirements, not yet a screen contract

**Evidence:** Both [handoffs](../handoff/shared-contract-checklist.md) repeatedly depend on API-authoritative state, but no field-level contract or complete bilingual screen inventory exists. Source 4.2 makes Arabic default; sections 2/4/18 require portal/app parity, while later answers specifically confirm some mobile behaviors and leave web equivalents open.

**Recommendation:** Build a screen/state matrix with explicit shared, platform-specific and unresolved behavior. Preserve later specific answers; reconcile source parity for reviews, popups and all other features. Include narrow-screen staff calendars/tables, keyboard/focus behavior, accessible Arabic/English forms, RTL with phone/ID/money fields, uploads, long clinical drafts and provider returns. Choose the web stack from team skills and required rendering/hosting behavior. Prefer shared web components with distinct public/patient/staff routes or shells over a separate application per staff role.

**Closure:** Approved Figma/design baseline, field/state/error examples, device matrix and API compatibility policy. Confidence: high. Extends R02/R12.

### AUD-25 — High — Full Emdaad replacement needs more than importing records

**Evidence:** [Scope](01-system-scope.md) requires all data/files and replacement at launch; export discussion stays deferred. Source 27 says a SQL database copy is expected, but no actual export/schema/sample or completeness evidence exists.

**Recommendation:** Preserve the deferral and record the launch dependency. Plan entity/file inventory, source-to-target IDs, timestamp interpretation, duplicate review, verified account links, financial opening balances and transaction lineage, attachment checksums and unresolved-record queues. Trial import must be repeatable. Define data freeze or delta capture, cutover reconciliation, rollback before new transactions and recovery once Motmaan has accepted new transactions; a simple database restore can lose post-launch payments/bookings.

**Closure:** Migration owner/finance/clinical reviewers approve a rehearsal and operational cutover plan when source access is available. Confidence: high. Extends R04/R14.

### AUD-26 — High — Production operation, ownership and recovery have no acceptance targets

**Evidence:** [Quality requirements](09-performance-security-and-responsive-websites.md) names required checks but no numeric latency, peak load, uptime, recovery time/data-loss targets or owners. [Azure](22-azure-hosting-and-deployment.md) is infrastructure preparation, not a complete operating plan. Source 28/32 includes daily backups, after-midnight operation, support and training.

**Recommendation:** Agree critical journeys and measurable targets, then test representative data and peak traffic. Define downtime reception/care/payment procedures, on-call escalation, reconciliation during provider outage, incident response and audited recovery. Specify deployment/schema compatibility with old mobile clients, secret/signing-key rotation, environment separation and ownership of release accounts/repositories. Clinical record access logs and diagnostic telemetry serve different purposes; keep necessary protected audit data without logging clinical payloads everywhere.

**Closure:** Named operators, supported service hours, tested restore, incident/runbook exercises and signed release evidence. Confidence: high. Extends R12–R14.

### AUD-27 — Medium — Recruitment, ranking and configuration need product limits

**Evidence:** [Recruitment](08-practitioner-compensation-and-recruitment.md), [expertise](13-practitioner-expertise.md), [observed fields](19-recruitment-current-website-reference.md) and source 9 contain credential review, public profile approvals, performance alerts and different practitioner types. Salary-paid priority is confirmed, but mixed-date fallback and tie-breaks are unresolved. Source 11/29 allows custom fields and policies without a complete configuration contract.

**Recommendation:** Preserve automatic account provisioning on authorized acceptance, with verified identity conflicts handled before activation and invitation retries separated. Classify which observed form choices apply to initial doctor-only recruitment; the administrative/training reference is not blanket launch authorization. Define license expiry/reverification and restrictions independently of employment pay model. Keep clinically eligible matches first; evaluate whether strict external-doctor hiding unnecessarily delays care and present an optional policy change for owner review. Do not alter the confirmed ranking silently.

Use typed, constrained settings with version/effective date, authority, audit and effects on existing bookings. Avoid a universal form builder or arbitrary workflow/status editor unless required details justify it. Review necessity of sensitive recruitment fields with the owner; do not delete the accepted baseline by assumption.

**Closure:** Product/clinical/operations approve supported choices, qualification lifecycle, ranking examples and configuration matrix. Confidence: high. Extends R01/R03/R11.

### AUD-28 — Medium — Documentation and export machinery can revive obsolete questions

**Evidence:** [Shared checklist](../handoff/shared-contract-checklist.md) has a two-column table with three cells in the permission-coverage and development-fixture rows; renderer behavior may drop the last cell. `tmp/pdfs/create_open_questions.py` and `create_user_notes.py` embed old question lists rather than reading current decisions. They still ask answered items such as the seven-minute hold and insurance scope. `tmp/update_owner_questions.py` is a one-time string-replacement migration tied to old dates/text; it is not a safe ongoing maintenance tool. Existing PDFs are already documented as historical, but filenames can appear current outside the repository.

**Recommendation:** Fix the two table rows. Mark legacy scripts/exports clearly and do not rerun them as the current publishing path. Future exports should derive from reviewed current Markdown and contain a source revision/date and status legend. Preserve original requirements in controlled project storage with provenance rather than depending only on a personal Downloads path. Keep binary preview churn out of the active planning surface where possible without deleting historical evidence.

**Closure:** Documentation owner verifies rendered checklist, status labels and a future reproducible export process. Confidence: high. No application-code defect is claimed.

## Service choices I would keep or reconsider

| Choice | Review judgment | Recommended action |
|---|---|---|
| ASP.NET Core, EF Core, modular monolith, Azure SQL | Good fit for the current scale and cross-module transactions | Keep; write module ownership and use-case boundaries, not microservices or generic repository layers by default |
| Action/resource authorization | Necessary and correctly directed | Finish precedence/delegation; keep endpoint coverage and a usable management interface |
| Swagger/OpenAPI | Good shared contract tool | Write behavior contracts first; generated Swagger does not resolve business rules |
| Outbox + Hangfire | Appropriate for durable integration and scheduled/bulk work | Use selectively, coordinate retries, and isolate urgent work |
| SignalR + FCM/APNs + API recovery | Good proposed combination | Validate Flutter and hosting; keep selection status proposed |
| HybridCache + Redis | Reasonable option; provisioning need unmeasured | Keep selection, decide timing/tier from workload; avoid sensitive authoritative state in cache |
| MyFatoorah | No evidence here requiring replacement | Verify enabled methods and BNPL ownership; classify mobile product payments |
| Qoyod | Sensible separation of official accounting and operational workflow | Prove invoice/correction/unknown-create behavior; finance approves mappings |
| Wati | Reasonable WhatsApp candidate; questionable default SMS dependency | Prefer a proven domestic transactional route unless Wati supplies the required evidence |
| Agora | Plausible managed provider, not proven unsuitable | Gate selection on recording, processing/fallback, storage/network and real-device evidence |
| Private Blob/GCS/OCI | Conditional alternatives | Choose one evidence-backed storage plan; avoid adding clouds merely to compensate for untested assumptions |
| Google translation candidate | Capability is plausible; sensitive-data workflow incomplete | Reconcile source scope, processing approval and report review before integration |
| Existing assessment platform | Correct to integrate rather than rebuild | Obtain actual contract before choosing embedding/SSO |
| Custom tasks, tickets, wallet and compensation | Fit Motmaan-specific rules | Keep separate domain models; do not force them into one generic workflow/status table |
| Broad self-managed staff SMS toggle | Weak for highly privileged access | Recommend a policy revision for sensitive staff/actions; owner decision required |
| Full scope plus fixed two-month launch | Unverified and high risk | Estimate with team and dependencies; owner chooses adjustments if needed |

These judgments are recommendations. They do not remove Redis, change the SMS policy, select SignalR or replace any confirmed provider.

## Source requirements coverage and reconciliation checklist

This covers all numbered source sections at subject level. It is not a completed field-by-field acceptance matrix. Requirements below remain subject to later user overrides; absence from a detailed handoff is a gap, not an approved deletion.

| Source sections | Current coverage | Details needing explicit reconciliation or contract |
|---|---|---|
| 1–2 Purpose, scope, operating volume | 01, README | Full source-to-feature inventory; broad first-stage scope versus explicit exceptions; delivery ownership |
| 3 Roles and permissions | 05, 21 | Granular defaults/overrides; role list versus current starting roles; narrower assigned-patient access supersedes source-wide clinician access |
| 4 Platforms, language, architecture | 01, 03, handoffs | Arabic default; web/app parity; entered-data translation and report language/review; quick search; future marketplace boundary |
| 5.1–5.3 Booking and staff requests | 02, 10 | Doctor-requested extra service on current versus new appointment; staff payment-link deadlines; package/free paths; canonical customizable labels |
| 5.4–5.7 Changes, attendance, operational calendar | 02, 10 | Late-change source exception superseded for patients; beneficiary change; closure conflicts; serial notes privacy; reception arrival overrides source self-arrival |
| 5.8–5.10 Follow-up, Ramadan, calendar | 02, 10, 03 | Free-follow-up eligibility/unavailable slots; overnight display; Ramadan overrides; add-to-calendar versus actual synchronization, updates/cancellation and privacy |
| 6 Waitlist | 01, 02 | Preference matching, minimum notice, offer expiry, exclusive capacity claim, fairness and competition with direct booking; distinct from unselected waiting-room queue |
| 7 Catalog and packages | 01, 02 | Service codes, per-practitioner price/duration, enabled versus publicly bookable; sale window versus purchased entitlement expiry; source one-year default status; current repeated-session packages override mixed-service source |
| 8 Rooms | 02, 10 | Reception selection overrides source auto-assignment; room types, capacity guarantee, closure, active occupancy and operational room schedule |
| 9 Practitioner profiles and performance | 08, 13, 19 | License dates, public start date/experience computation, source leave-conflict policy, complaint/rating alerts with current ten-point scale; temporary/permanent restrictions |
| 10 Video and recording | 04 | Consent/readiness/failure and abandoned-session contract; center-storage interpretation and one-year lifecycle |
| 11 Clinical and family | 05, 07, 21; 01 overview | Clinical fields, configurable patient fields, ICD/medicine catalog provenance, report templates/signatures and correction; beneficiary identity changes and guardian scope |
| 12 Treatment follow-up | 01, 10; handoffs | Fixed therapeutic worksheets, adherence thresholds, administrative views, follow-up results, occurrence rules and summaries |
| 13 Finance | 02, 03 | POS/cashboxes and receipts, complete reconciliation, payer ownership and corrections; bank-transfer booking prohibited; tax rule requires finance validation |
| 14 Loyalty | 01 overview | Earn/redeem/expire/reverse, service exclusions, mixed funds and historical balances; disabled by default does not mean absent from scope |
| 15 Compensation | 08, 02 | Fixed-amount alternative status, completion/payment period attribution, assessment attribution, closed-period corrections and payroll boundary |
| 16 Offers and discounts | 01/02 overview | Permanent patient discounts, stacking precedence, usage-limit races, eligibility, refund clawbacks and price snapshots |
| 17 Messaging | 03, 10, 16, 24 | Transactional versus optional educational/marketing preferences, quiet times, source re-engagement messages, channel matrix and template authority; OTP channel is already SMS |
| 18 Patient surfaces | Flutter/web handoffs | Report request tracking, files, calendar, receipts, current-state recovery and explicit parity; patient recording access is not approved |
| 19 Reports | 01 and handoffs overview | Named report dictionary, formulas, dimensions, authorized fields, export formats and reconciliation; POS/gateway/method must not double-count the same payment |
| 20 Analytics | 01 overview | Occupancy denominator, cancellations/holds/overruns, retention metrics, seasonal inputs, heatmaps; predictive analytics usefulness/data readiness and release status |
| 21 Audit | 09, 24 | Event/field history, read access, protected clinical versions, retention, privileged operator access and artifact version lineage |
| 22 Staff tasks | 15 | Later multiple-assignee/unread rules apply; deferred completion condition, branch scope and sensitive content boundaries |
| 23 Unified patient page | 05, 09, handoffs | Bounded authorized sections; quick links cannot imply blanket record/finance visibility |
| 24 Integrations | 03, 16–18 | Account-specific evidence, adapter ownership, assessment/payment/result attribution and downtime behavior |
| 25 Insurance | 01, 03, decisions | Later no-current-insurance/future-readiness decision controls; avoid speculative claims/onboarding implementation |
| 26 Other capabilities | 01, 03, 08 overview | Nafath/Wasfaty access; external-practitioner wallets/marketplace scope; full training lifecycle, group capacity, materials/certificates and mobile billing; prediction status |
| 27 Migration | 01, 20 | Source expects SQL copy, actual availability unproven; files, historical identities/times/money and full cutover evidence; discussion deferral retained |
| 28 Quality | 09, 22 | Daily backup requirement, measurable recovery/performance, after-midnight operations, data-handling review and real-device evidence |
| 29 Policy settings | Distributed topics | Typed/versioned settings; approval/effective dates; effect on existing bookings; source exceptions reconciled with later decisions |
| 30 Setup/tutorial | 01 mentions setup progress | Required steps, completion validation, repeatability, permissions, safe bootstrap and first-use instructional flows |
| 31 Design and schedule | 01, 20 | Whole-project versus workflow Figma approval, real operational reviews, milestones and owner feedback timing |
| 32 Support/training | 09/20 launch outline | Staff training, manuals, support hours/severity/escalation, handover and maintenance ownership |
| 33–34 Commercial and reference terms | Original source | Cost/ownership/deliverable checklist for owner review; not executable instructions or authority to buy, deploy or send messages |
| Appendices A–C | Decisions partly reconciled | Preserve specific user supersession; track provider costs, source-code/license ownership and unanswered vendor evidence |

## Recommended next work in dependency order

1. **Documentation repair:** resolve AUD-01 and the checklist table, mark historical helpers/exports, and create stable feature/decision IDs. These are consistency changes based on existing answers, not new business decisions.
2. **Product and delivery agreement:** reconcile source coverage, design approval and the actual team/schedule. Identify owner/clinical/finance decisions separately from developer-written contracts.
3. **Provider evidence:** work on SMS/email, Azure service access, payment/BNPL route, Qoyod, recording/storage, assessments and mobile purchase classification. No patient data or provider activation is needed to prepare the evidence checklist.
4. **First workflow contract:** finish authentication/authorization and its UI states first. Prepare discovery → hold → payment → appointment → staff view next, while keeping its deferred decisions as explicit gates.
5. **Other workflow contracts:** clinical/report versions, finance/compensation, patient tasks, recruitment, support/internal tasks, reporting and source-only capabilities. Prioritize independent ready work without dropping launch scope.
6. **After implementation authorization:** validate the riskiest provider/client paths with synthetic data, then build complete slices and meaningful tests. Do not substitute mocks for integration evidence.
7. **Before launch:** complete migration rehearsal, financial reconciliation, security/access checks, restore/performance tests, store review preparation, operational training and named sign-offs.

The owner need not decide endpoint names, database indexes or polling implementation. Developers should propose these with evidence. The owner/clinical/finance team must decide access authority, patient outcomes, financial policy, service scope, acceptable data handling and release tradeoffs.

## Completion evidence for this review

The review produces this findings register and its source-coverage checklist. It links to existing R01–R14/A/P records rather than treating previously known gaps as newly discovered bugs. New follow-ups are indexed in the living tracker and decision register as recommendations. No finding is marked remediated solely because it is documented. The current confirmed choices and explicit deferrals remain in force.

## AUD-28 documentation cleanup record

**Applied 8 October 2026:** removed only the obsolete question-list workflow after checking helper contents, repository references and active Python/helper processes. No matching helper process was active; references were confined to the obsolete helpers and explicitly historical audit evidence. The sampled `question-review-1.png` shows the obsolete 3 October question-list export, confirming the review previews belong to that workflow. Paths were resolved and checked to stay within Motmaan; deletion used explicit files, with no recursive directory deletion.

Deleted **36 files**: three hardcoded export/update scripts, three historical question PDFs and thirty previews. Exact inventory:

- `output/pdf/motmaan-all-unresolved-questions-ar-rtl.pdf`
- `output/pdf/motmaan-open-questions-ar-rtl.pdf`
- `output/pdf/motmaan-user-notes-ar-rtl.pdf`
- `tmp/pdfs/all-unresolved-01.png`
- `tmp/pdfs/all-unresolved-02.png`
- `tmp/pdfs/all-unresolved-03.png`
- `tmp/pdfs/all-unresolved-04.png`
- `tmp/pdfs/all-unresolved-05.png`
- `tmp/pdfs/all-unresolved-06.png`
- `tmp/pdfs/all-unresolved-07.png`
- `tmp/pdfs/all-unresolved-08.png`
- `tmp/pdfs/all-unresolved-09.png`
- `tmp/pdfs/all-unresolved-10.png`
- `tmp/pdfs/all-unresolved-11.png`
- `tmp/pdfs/all-unresolved-12.png`
- `tmp/pdfs/create_open_questions.py`
- `tmp/pdfs/create_user_notes.py`
- `tmp/pdfs/open-questions-01.png`
- `tmp/pdfs/open-questions-02.png`
- `tmp/pdfs/open-questions-03.png`
- `tmp/pdfs/open-questions-04.png`
- `tmp/pdfs/open-questions-05.png`
- `tmp/pdfs/open-questions-06.png`
- `tmp/pdfs/open-questions-07.png`
- `tmp/pdfs/open-questions-08.png`
- `tmp/pdfs/open-questions-09.png`
- `tmp/pdfs/open-questions-10.png`
- `tmp/pdfs/question-review-1.png`
- `tmp/pdfs/question-review-2.png`
- `tmp/pdfs/question-review-3.png`
- `tmp/pdfs/question-review-4.png`
- `tmp/pdfs/question-review-5.png`
- `tmp/pdfs/question-review-6.png`
- `tmp/pdfs/user-notes-1.png`
- `tmp/pdfs/user-notes-2.png`
- `tmp/update_owner_questions.py`

The two malformed shared-checklist rows now use the declared two columns. Current planning/decision documents, handoffs, source provenance and discussion history are retained. Unrelated audit working files (`tmp/audit_planning_files.py` and `tmp/audit-source-requirements.txt`) were preserved; obsolete helpers were not rerun. No authoritative current document depends on the removed exports. Original evidence above names deleted files as history, not active tools.

## Owner-update documentation validation

Validation on 8 October 2026 covered 33 Markdown documents: **467 local links/file targets and heading fragments**, **692 table rows** with consistent declared columns, and all **28 owner-defined status rows** compared directly with the supplied owner task in both the register and audit tracker. Results: zero missing local targets, invalid heading references, table-column errors or status mismatches. `git diff --check` passed. All 36 deletion targets are absent; current documentation has no active dependency on them.

Targeted contradiction checks and manual review reconciled interim Qatar hosting, mandatory privileged verification, within-role overrides, later-booking extension blocking, report versions, selected-language display, known provider-account status and patient SMS channel. Original contradictory audit/readiness text remains explicitly historical; six newly deferred AUD topics and older specific deferrals are preserved. Changed files are planning/handoff Markdown only, plus the explicitly authorized obsolete-artifact deletions. Existing working-tree changes and unrelated audit tools remain.

Limits: external URLs were not re-fetched, provider/account capabilities and legal/data-transfer suitability were not verified, and no application code, database migrations, provider setup, deployment, media/restore/performance tests or real-device tests were executed. Detailed delivery milestone/staffing evidence was not independently verified; owner status AUD-03 Planned is honored without inventing a schedule. Future acceptance scenarios and operational targets are planning requirements, not results.
