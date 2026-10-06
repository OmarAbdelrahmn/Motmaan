# Practitioner expertise catalog and patient filters

Updated: 4 October 2026. Status: expertise requirement and management approval of post-hiring public biography/expertise updates confirmed; detailed workflow remains open. No implementation has started.

## Goal

Maintain a database-backed catalog of areas in which each psychiatric doctor has expertise. A doctor may be strong in several areas; keep those areas on the doctor's profile so patients can filter and choose. The user clarified the earlier example as expertise areas within a psychiatric clinic, rather than one literal catalog entry called “علاج العصبية.” Exact initial Arabic/English labels still need clinical/management review.

## Confirmed direction

- The expertise list is stored in the database and can be edited by administrators.
- Doctor applicants select several therapeutic expertise values as part of Join us; multi-selection is explicitly confirmed. Exact Arabic/English labels and selection limits remain open.
- Patient-facing discovery uses these expertise entries as doctor filters, helping match a patient's concern to doctors who treat it.
- Doctor search filters should also include specialty, language, appointment mode, and availability.
- Initial public recruitment is doctor-only; administrators control openings/applications.
- Management approves the candidate's expertise/degrees for the public profile and interviews the candidate before acceptance.
- Management verifies degrees and applicant data before doctor activation; the verification procedure remains open.
- Prioritize available salary-paid practitioners in patient discovery/booking. Preserve external fallback when prioritized practitioners are full over the selected dates and matching filters. Both use the same operational access rules; compensation remains distinct.
- Availability search accepts start and end dates. Equal dates mean a single-day search; different dates mean the selected date range. Evaluate salary-paid availability priority/external fallback over that selection, using the same matching filters.

## Recommended model

- Keep a controlled, curated catalog rather than exposing arbitrary free-text as filter values. Each entry can have a stable ID, Arabic and English labels, enabled/archived state, sort order, and optional parent category or synonyms.
- Since the user has not chosen seed labels, have a psychiatric clinical lead propose the initial Arabic/English expertise list for management approval; administrators can then maintain the approved catalog.
- Let applicants select from active catalog entries and optionally suggest a missing entry. A suggestion goes to management review and must not publish a new filter value automatically.
- Keep applicant-provided selections separate from approved public profile expertise. Management reviews the candidate's expertise and degrees, interviews the candidate, and approves public profile fields as part of recruitment.
- Link approved catalog entries to a practitioner profile through an explicit many-to-many relation. Preserve old application selections/audit history if the catalog later changes.
- Patient filters should be backed by server-side, bounded queries and return only public profile information. Do not expose clinical records, private application files, or internal reviewer notes through profile search.
- **Recommended filter logic, accepted by user delegation:** combine different filter categories with AND (for example, specialty and language must both match), and allow OR among multiple selected values within one category (for example, Arabic or English). Keep availability as a current server-side eligibility filter.
- Make labels and filters usable in Arabic/English and on mobile/desktop. Treat expertise labels as discovery information, not proof of license, credential, or guaranteed outcome.

## Open decisions

### Confirmed doctor display priority

The user clarified preferences as **salary-paid and available** practitioners taking priority ahead of percentage-paid practitioners. This resolves the deferred criteria question. Apply the current branch, date-range and matching-filter rules, and the prior external fallback when prioritized doctors are fully booked. No exact tie-break order, configurable weights, or mixed-date presentation is approved; configuration ownership remains open. Render API-authoritative order and do not expose compensation contracts/rates to patients.

### Other open details

- Exact catalog categories and Arabic/English labels for psychiatric treatment expertise.
- **Confirmed on 4 October 2026:** Post-hiring public biography and expertise changes require management approval before publication. Exact submission/rejection workflow remains open. Proposed presentation: keep the last approved public values visible while an update awaits review.
- Whether candidates may suggest new expertise values or only select existing ones.
- Current-site personal/qualification/document baseline is recorded in [recruitment reference](19-recruitment-current-website-reference.md); expertise labels/limits, extra supporting evidence, and public-field mapping remain open.
- How management verifies degrees/applicant data and any additional license checks before activation; baseline documents are CV and health-specialties certificate, with extra documents and verification procedure still open.
- Availability calculation/display and treatment of mixed results when employed doctors have slots on some selected dates. Single-day and date-range selection are confirmed; apply branch and selected search filters consistently. No arbitrary date-range limit is approved yet.
- Whether additional patient filters are needed beyond expertise/concern, specialty, language, appointment mode, and availability.
- Evidence/credential verification, who may edit the catalog, translations, archive behavior, and review/audit permissions.

## Relevant surfaces

- **Join us:** candidate selects or describes expertise alongside application information; no dashboard account is created before authorized acceptance.
- **Management:** authorized administrators maintain the catalog and review candidate/profile expertise according to rules still to be decided.
- **Doctor profile:** show only approved public information. Post-hiring biography/expertise updates require management approval before publication; update submission and rejection details remain open.
- **Patient website/app:** filter public doctor results using active catalog entries. Search must respect availability and booking eligibility returned by the API.

Related: [System scope](01-system-scope.md), [recruitment and compensation](08-practitioner-compensation-and-recruitment.md), [decisions and open questions](06-decisions-and-open-questions.md), [Flutter handoff](../handoff/flutter-developer.md), and [web handoff](../handoff/web-frontend-developer.md).
