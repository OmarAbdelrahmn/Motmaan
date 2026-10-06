# Customer mobile appointment countdown and reminders

Updated: 4 October 2026. Status: confirmed mobile capabilities with proposed detailed behavior. This note is for planning the customer iOS and Android applications; no app or API code has been created.

## Confirmed direction

- The customer app should show a timer for an upcoming in-person session. It is interpreted as a countdown until the scheduled appointment starts, based on the surrounding request for advance reminders.
- The customer should receive a reminder before the session, with the lead time determined by administration.
- Patient no-shows keep the session payment or consume one package session for both in-person and online appointments.
- Automatically evaluate no-show at scheduled start plus an admin-configured grace period, provided no attendance or active consultation has been recorded.

Both reminder lead time and no-show grace period are administration-configured; no numeric values have been approved. They are different settings. The timer is not a hard limit on online consultation duration. Extending countdown presentation to online appointments is a compatible proposed UI behavior, not an additional confirmed requirement.

## Proposed app presentation

An upcoming appointment card shows patient beneficiary, specialist, service, appointment mode, exact date and time, and time remaining. A countdown supplements the absolute appointment time so users can understand after-midnight Ramadan appointments and family bookings.

When the appointment starts, change the countdown to an appropriate status instead of displaying an unexplained negative duration. Reception marks an in-person patient Arrived; the patient app displays that status. Online Join follows its separately authorized rules. The doctor marks the session Finished; do not mark it completed because its display timer expires.

Calculate the displayed countdown from the server-supplied appointment instant and time reference. Refresh authoritative state after app resume, changes, or connectivity restoration; continuous API polling every second is unnecessary. Device clock changes must not determine booking deadlines, attendance, or financial effects.

## Reminder scheduling

**Confirmed on 4 October 2026:** Weekly patient treatment-task progress summaries are for both the patient and their assigned doctor. This resolves recipients only; contents, calculation boundaries, delivery channels, and timing remain open. It does not change doctor-controlled task reminder schedules or grant access to unrelated patients.

Administration configures the advance-reminder lead time. Proposed scheduling computes a due instant from the appointment start minus that lead time and stores a durable reminder job. Numeric defaults, one versus multiple reminders, effective timing of setting changes, and service/mode-specific overrides remain open.

App push is the initial proposed mobile reminder channel; the existing WhatsApp/SMS preferences remain part of the broader notification plan. Decide whether reminders also use those channels or a fallback. The notification should carry minimal information and open the authorized appointment details rather than expose clinical content.

The backend schedules reminders independently of whether the mobile app is open. Store a logical reminder identity and delivery attempts; deduplicate duplicate scheduling, record provider outcomes, and define bounded retries and useful deadlines. Do not promise exact notification display timing on a device.

**Patient task notifications:** Doctors control assigned daily/weekly tasks and their reminder schedule, including time of day, selected weekdays, start/end dates, and number of reminders per day. The backend calculates and sends push notifications according to these settings and task recurrence; the mobile app displays them. Use `Asia/Riyadh`. Changes to recurring patient tasks apply only to future occurrences and preserve earlier completion history. Numeric defaults/limits and weekly-summary behavior remain open. This supersedes earlier admin-controlled patient-task timing; appointment reminder lead time stays admin-controlled.

Rescheduling should invalidate stale reminders and schedule replacements. Cancellation, postponement, and completion should suppress reminders that are no longer applicable. For bookings made after the reminder's intended time, define whether to send an immediate acknowledgment/reminder or skip it. Agree notification recipients for family bookings and device registration across web/mobile sessions.

## Attendance and no-show

**Confirmed on 4 October 2026:** Reception marks the patient Arrived for an in-person appointment, and the treating doctor marks the session Finished. This supersedes the source's patient-operated in-person Arrived action. The patient app/website displays authoritative attendance and completion; a patient tap, countdown expiry, or delivered notification does not record either event. Online attendance evidence on joining remains a separate workflow; this clarification does not require reception confirmation of an online join. Attendance correction rules remain open.

The user replaced the source's scheduled-end timing with scheduled start plus an admin-configured grace period. Recorded attendance or an active online consultation prevents automatic no-show even before completion is recorded. The API's cutoff and attendance state are authoritative; the mobile display does not perform the financial transition. Define optional UI text during the grace window without confusing the countdown-to-start with attendance eligibility.

Patient no-show retention applies to paid sessions and package entitlements. Preserve No-show as a distinct classification and consume only once. The doctor receives no completed-session incentive for that appointment. Do not automatically classify clinician absence or an online service failure as patient absence.

## Arrival, doctor capacity, and next available appointments

Clarified on 4 October 2026:

- **Confirmed:** Reception records Arrived. The doctor explicitly confirms the end-session process; after that confirmation the session is Finished and the patient receives a request to rate the session/doctor. Attendance, readiness, completion, and feedback remain separate; see [patient feedback](14-patient-session-feedback.md).
- **Confirmed:** Patient booking is based on the doctor's scheduled free appointment slots. Show the next available date/time, even if it is a week away. A patient waiting-queue position or estimated waiting-room time was not selected.
- **Confirmed:** Both doctors and management can control doctor session count and session time/duration. Duration is configurable. Five sessions per day and X minutes were examples, not fixed limits or defaults. Schedules support different weekday working hours, breaks between sessions, and days off. Count/duration setting changes apply only to unbooked slots; existing bookings retain their date/time and duration. Exact duration configuration scope, break settings, and handling days off that conflict with existing bookings remain open.
- **Confirmed:** The doctor presses Ready for patient to notify both patient and reception. Channels remain open; this is separate from advance appointment reminders and does not change the booked time.

Keep existing no-show rules, selected-date-range search, salary-paid availability priority/external fallback, and branch scope in force. **Confirmed:** Only when the search returns no available appointments at all, show separate next-available suggestions, which may fall beyond the selected date range. Retain matching non-date filters and existing doctor-priority rules; do not silently change the range. Existing results do not trigger extra out-of-range suggestions merely because one doctor has no slots. Suggestion count and search horizon remain open. Preserving existing bookings under session count/duration setting changes is confirmed. Proposed safeguard: prevent new slots from overlapping existing reservations. Patient cancellation/modification is blocked with less than 24 hours remaining; staff exceptions, assignment and detailed permissions remain open/deferred.

## Clinical end, overrun warnings, and extension

Confirmed on 4 October 2026:

- The in-person consultation ends when the patient leaves; the doctor writes session notes afterward and may write a prescription before the patient leaves. Keep actual consultation end and later doctor-confirmed Finished status distinct. The rating email follows Finished confirmation; an unanswered review prompts a popup on the patient's next app opening, within eligibility. See [patient feedback](14-patient-session-feedback.md).
- Measure the allocated session duration from the actual consultation start. When that duration expires while the session remains unfinished, show a red warning to the doctor. If it remains unfinished after a system-configured delay from the warning/expiry, notify reception about the overrun. A 1.5-hour session is an example, not a universal duration. No reception-delay value, default, or setting owner has been selected. How actual consultation start is recorded remains open; do not equate arrival or Ready for patient with actual start without a decision.
- The doctor can explicitly extend the active session by a period configured in the system by the doctor or management. Exact period values, defaults, limits, repeat-extension rules, and authority scope remain open. This is a deliberate extension of the active session, distinct from general duration-setting edits that preserve existing bookings.
- When extending into a later booked appointment, allow the extension and warn the doctor that another patient is waiting. Do not automatically shift the later booking. Exact waiting/conflict detection and warning wording remain open; a patient-facing queue display is not selected by this answer.
- The review window starts at actual consultation end and lasts 48 hours, including when Finished confirmation is delayed. Reception records actual in-person session end if the doctor forgets; detailed recording/correction permissions remain open. Recording actual end is distinct from the existing doctor-confirmed Finished/invitation step.
- The warning must not automatically mark Finished, terminate an attended consultation, apply a no-show, or send a rating request. An active consultation still prevents no-show under the existing rule.

Proposed safeguards: record extensions and distinguish booked duration, effective end, actual consultation end, and confirmation time; recalculate warning/escalation eligibility after an extension or completion and avoid stale/duplicate reception alerts. Do not silently move subsequent bookings or change fees/incentives. Extension with a waiting-patient warning is confirmed; exact detection, warning dismissal after the patient has left but documentation is pending, applicability to online sessions, and any extension pricing consequences remain unresolved. Patient changes within 24 hours are now blocked; staff exceptions and detailed permissions remain open/deferred.

Timing clarification: the original overrun warning is due at actual consultation start plus allocated duration; reception escalation is due after the configured delay if still unfinished. Extension recalculation remains a proposed safeguard until its detailed behavior is settled. The no-show cutoff still uses scheduled appointment start plus its separate attendance grace period; this answer changes overrun timing only.

## Planned verification

**Review follow-up R07/R11, 4 October 2026:** Specify whether overrun alerts stop at actual clinical end while notes/Finished confirmation remain pending; “unfinished” currently spans two different conditions. Define actual-start capture, late-arrival correction and stale notification handling in a transition table. Patient-task occurrences also need explicit completion/missed cutoffs, edit boundaries and summary calculation rules. These are recommendations for completing contracts, not changes to confirmed timing or deferred permissions. See the [readiness review](20-development-readiness-review.md).

Verify countdowns on app resume and changed device clocks, Arabic/English and after-midnight dates, reschedule/cancel reminder and cutoff invalidation, multiple devices and duplicate jobs, family beneficiary/recipient correctness, attendance racing the configured cutoff, online overrun, and no duplicate package consumption. These are future verification scenarios.

Related notes: [Booking and finance](02-booking-and-finance.md), [Online sessions](04-online-sessions.md), [Integrations and storage](03-integrations-and-storage.md), and [Open questions](06-decisions-and-open-questions.md).
