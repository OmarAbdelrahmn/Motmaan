# Planning discussion history

Archived during the 4 October 2026 documentation review. Historical answer batches are preserved here; current decisions and outstanding questions are maintained in the [decision register](../planning/06-decisions-and-open-questions.md) and [living tracker](../planning/12-user-notes-and-open-questions.md). Historical deferrals can be superseded by later answers. This file grants no implementation authorization.

## Ten cross-scope answers

- Historical Q1 Packages: composition was deferred in that earlier batch; superseded by the latest repeated-session, practitioner-specific package answer.
- Q2 Staff tasks: multi-assignee completion condition deferred; existing multiple assignees and automatic closure requirements remain.
- Q3 Support: patients can reopen resolved/closed tickets; the latest reply confirms no time limit. One satisfaction response per ticket remains unchanged.
- Historical Q4 Assessments: discussion was deferred in that earlier batch; the user has now returned to it and requested programmer integration questions.
- Q5 Clinical reports: doctor edits the finalized report directly instead of issuing a separate revised report. Maintain permissions and assigned-patient/branch scope. Protected edit history is proposed; no audit deletion is authorized and no prescription/accounting correction policy changes follow from this answer.
- Q6 Recovery: proof through previously verified email is sufficient to replace a lost phone number without administration review. Use an established-email recovery challenge and verify control of the replacement phone; no newly supplied email/phone proves old-account ownership.
- Q7 Doctor profiles: management approves post-hiring public biography/expertise changes before publication. Exact review/rejection workflow remains open.
- Q8 Treatment tasks: weekly progress summaries go to both patient and assigned doctor. Content, timing, and channels remain open.
- Q9 Management dashboard: include all four offered figures—revenue, bookings, unpaid amounts, and patient satisfaction—within authorized branch scope. Definitions, reporting periods, order/layout, and drill-downs remain open.
- Q10 Migration: Emdaad export formats/options discussion deferred. Full data/file migration and replacement at launch remain confirmed.

- Overrun timing answer: count allocated session duration from actual consultation start. Capturing that start event remains to define; arrival/readiness are not automatically the start.
- Reception escalation answer: notify reception after a system-configured delay following duration expiry/red warning if still unfinished. No value/default or configuration owner was selected. The scheduled-start no-show rule remains unchanged.

- Clinical-sequence answer: the patient leaves at consultation end, then the doctor writes notes; a prescription may be written before departure. Do not require notes before patient departure/clinical end. Exact later confirmation validation is unresolved.
- Rating-delivery answer: send email after doctor-confirmed completion; if no review is submitted, show a popup on the next app opening, within eligibility. Submission across channels suppresses the unanswered popup; repetition and missing-email handling remain open.
- Overrun addition: red doctor warning at actual-start-based duration expiry, delayed reception notification if still unfinished, and a doctor-operated extension using a period configurable by doctor or management. Delay value/default/owner, actual-start capture and extension values/limits remain open. Latest answers settle the rating-window anchor at actual end and allow extension with a waiting-patient warning; exact waiting/conflict detection remains open.

- Weekday schedule answer: support different weekday working hours, breaks between sessions, and days off.
- Suggestion answer: offer next-available appointments only if the search has no available appointments at all; display out-of-range suggestions separately.
- Doctor readiness answer: the doctor presses Ready for patient to notify patient and reception; channels remain open.
- New completion direction: doctor explicitly confirms session end, then email the patient a session/doctor rating request and show a next-app-opening popup if unanswered. Latest answer confirms 48 hours from actual consultation end even if confirmation is delayed; reception records actual in-person end if the doctor forgets. Other delivery details remain open.

- Duration follow-up: session duration is configurable; exact configuration scope (such as per service) remains open.
- Settings-change follow-up: apply session count/duration edits only to unbooked slots. Existing bookings retain their booked date/time and duration.

- Reception marks in-person arrival; the doctor marks session Finished. Online join attendance remains separate.
- Show free scheduled doctor slots and the next available date/time. Doctors and management control daily session count and session time/duration; no numeric defaults were selected.
- Doctor-ready recipients and button trigger are confirmed; notification channels remain unresolved.

- Internal tasks close automatically after the required completion condition is met; creator approval is not required. The multi-assignee completion condition remains open.
- Retain staff notifications in an unread list, including events missed while the website was closed.
- Changes to recurring patient tasks apply only to future occurrences and preserve earlier completion history.
- Doctors can issue finalized clinical reports and prescriptions directly, within their permissions, assigned-patient scope, and qualifications, without a separate management approval step.
