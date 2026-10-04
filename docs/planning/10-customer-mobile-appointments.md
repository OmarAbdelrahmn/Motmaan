# Customer mobile appointment countdown and reminders

Updated: 3 October 2026. Status: confirmed mobile capabilities with proposed detailed behavior. This note is for planning the customer iOS and Android applications; no app or API code has been created.

## Confirmed direction

- The customer app should show a timer for an upcoming in-person session. It is interpreted as a countdown until the scheduled appointment starts, based on the surrounding request for advance reminders.
- The customer should receive a reminder before the session, with the lead time determined by administration.
- Patient no-shows keep the session payment or consume one package session for both in-person and online appointments.
- Automatically evaluate no-show at scheduled start plus an admin-configured grace period, provided no attendance or active consultation has been recorded.

Both reminder lead time and no-show grace period are administration-configured; no numeric values have been approved. They are different settings. The timer is not a hard limit on online consultation duration. Extending countdown presentation to online appointments is a compatible proposed UI behavior, not an additional confirmed requirement.

## Proposed app presentation

An upcoming appointment card shows patient beneficiary, specialist, service, appointment mode, exact date and time, and time remaining. A countdown supplements the absolute appointment time so users can understand after-midnight Ramadan appointments and family bookings.

When the appointment starts, change the countdown to an appropriate status instead of displaying an unexplained negative duration. The in-person Arrived action and online Join action follow their separately authorized rules. Do not mark a session completed because its display timer expires.

Calculate the displayed countdown from the server-supplied appointment instant and time reference. Refresh authoritative state after app resume, changes, or connectivity restoration; continuous API polling every second is unnecessary. Device clock changes must not determine booking deadlines, attendance, or financial effects.

## Reminder scheduling

Administration configures the advance-reminder lead time. Proposed scheduling computes a due instant from the appointment start minus that lead time and stores a durable reminder job. Numeric defaults, one versus multiple reminders, effective timing of setting changes, and service/mode-specific overrides remain open.

App push is the initial proposed mobile reminder channel; the existing WhatsApp/SMS preferences remain part of the broader notification plan. Decide whether reminders also use those channels or a fallback. The notification should carry minimal information and open the authorized appointment details rather than expose clinical content.

The backend schedules reminders independently of whether the mobile app is open. Store a logical reminder identity and delivery attempts; deduplicate duplicate scheduling, record provider outcomes, and define bounded retries and useful deadlines. Do not promise exact notification display timing on a device.

**Patient task notifications:** Doctors control assigned daily/weekly tasks and their reminder schedule, including time of day, selected weekdays, start/end dates, and number of reminders per day. The backend calculates and sends push notifications according to these settings and task recurrence; the mobile app displays them. Use `Asia/Riyadh`. Numeric defaults/limits, task-edit effects on existing occurrences, and weekly-summary behavior remain open. This supersedes earlier admin-controlled patient-task timing; appointment reminder lead time stays admin-controlled.

Rescheduling should invalidate stale reminders and schedule replacements. Cancellation, postponement, and completion should suppress reminders that are no longer applicable. For bookings made after the reminder's intended time, define whether to send an immediate acknowledgment/reminder or skip it. Agree notification recipients for family bookings and device registration across web/mobile sessions.

## Attendance and no-show

The source provides a customer Arrived action for in-person visits, attendance on online join, and authorized staff confirmation. Agree the validity checks for customer arrival and attendance corrections. A displayed countdown or a delivered notification is not evidence of attendance.

The user replaced the source's scheduled-end timing with scheduled start plus an admin-configured grace period. Recorded attendance or an active online consultation prevents automatic no-show even before completion is recorded. The API's cutoff and attendance state are authoritative; the mobile display does not perform the financial transition. Define optional UI text during the grace window without confusing the countdown-to-start with attendance eligibility.

Patient no-show retention applies to paid sessions and package entitlements. Preserve No-show as a distinct classification and consume only once. The doctor receives no completed-session incentive for that appointment. Do not automatically classify clinician absence or an online service failure as patient absence.

## Planned verification

Verify countdowns on app resume and changed device clocks, Arabic/English and after-midnight dates, reschedule/cancel reminder and cutoff invalidation, multiple devices and duplicate jobs, family beneficiary/recipient correctness, attendance racing the configured cutoff, online overrun, and no duplicate package consumption. These are future verification scenarios.

Related notes: [Booking and finance](02-booking-and-finance.md), [Online sessions](04-online-sessions.md), [Integrations and storage](03-integrations-and-storage.md), and [Open questions](06-decisions-and-open-questions.md).
