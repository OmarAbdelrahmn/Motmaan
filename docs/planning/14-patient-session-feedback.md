# Patient session feedback

Updated: 8 October 2026. Status: feedback, normal doctor completion plus permitted reception operational closure, and mobile review editing confirmed; remaining delivery/reporting details are open. No implementation has started.

## Optional session and doctor reviews

- After a session, each patient may optionally review the session and the doctor who provided it.
- **Confirmed trigger:** The doctor explicitly confirms the end-session process. After that successful confirmation marks the session Finished, send the patient a request to rate the session and doctor. **AUD-19:** when the doctor forgets, reception may perform authorized operational closure. Audit the finalizing actor and separate actual end from closure time; this does not authorize clinical signing. Scheduled end, reception attendance alone and Ready for patient do not trigger completion. Rating remains optional; it does not determine session completion or payment.
- **Confirmed clinical sequence:** The in-person clinical session ends when the patient leaves; the doctor writes session notes afterward. The doctor may write a prescription before the patient leaves. Distinguish patient departure/actual consultation end from later documentation and Finished confirmation. Do not require notes before the patient can leave or invent a mandatory note-save gate for completion; exact confirmation validation remains open.
- **Confirmed delivery:** Email the rating request after doctor-confirmed completion. If the patient has not submitted a review, show a rating popup the next time they open the app, subject to the existing review eligibility/window. A review submitted through email/web must suppress the unanswered popup in the app. Popup dismissal/repetition, multiple pending reviews, and patients without a usable email remain open. No WhatsApp/SMS or push rating delivery was selected.
- Management can see all session feedback. The patient who submitted a review can see their own review, and the doctor who treated that session can see its review. Do not expose it to other patients, unrelated doctors, or the public.
- The feedback should be linked to the patient, completed session, and treating doctor so management can review it in context.
- Do not treat feedback as a public doctor rating. Management may review and report on all session feedback.
- The patient has exactly 48 hours from session end to submit a review and may edit their submitted session/doctor review from the mobile app within that same window. Edits do not restart the deadline. The backend enforces ownership, eligibility, and the original deadline. Web review editing is not yet specified; existing web submission remains in scope.
- Written comments are supported alongside the rating. Making comments optional is a recommendation; the user confirmed allowing comments without specifying whether they are mandatory.
- The user suggested a rating out of 10. Use a ten-point rating scale; exact endpoint labels remain open.
- The patient author can view their own session review. The treating doctor can view that review for their session. Management can see all reviews. No other users can see it.

## Support-ticket satisfaction

- When a support ticket is closed, email the patient a satisfaction survey.
- Use a satisfaction rating out of 10.
- Written comments are optional. Allow only one satisfaction-survey submission per closed ticket; enforce this on the backend across retries and devices. Reopening/reclosing behavior remains open and must not silently create another response entitlement.
- Associate the response with the ticket and the administrator who resolved it. Management can see all ticket satisfaction responses and report on them. The patient can see their own response; the resolver's direct visibility remains permission-dependent.
- Do not expose ticket satisfaction responses to unrelated users or doctors.

## Proposed controls and unresolved details

- **Review follow-up R07, 4 October 2026:** If doctor-confirmed Finished occurs after the 48-hour deadline measured from actual end, specify email/invitation behavior and the expired review screen. Do not reset or extend the confirmed deadline. The current statements require a completion-triggered invitation but do not resolve this expired-at-trigger case; it needs an explicit outcome before the affected workflow is implemented.

- Proposed: send one logical rating invitation per completed session and preserve its state across retries/repeated doctor confirmation. Keep the rating form accessible in appointment details after popup dismissal. Do not send completion-based invitations for cancelled/no-show sessions. Email plus a next-app-opening popup for unanswered reviews is confirmed; wording, repeated reminders/popups, and missing-email handling remain open.
- **Confirmed on 4 October 2026:** The 48-hour review window starts at actual consultation end, even if the doctor confirms Finished later. Reception records the actual in-person session end if the doctor forgets. Later confirmation, email delivery, app opening, and review edits do not restart the deadline. Keep actual end separate from Finished/administrative closure, including authorized reception closure when the doctor forgets (AUD-19). Correction permissions and completion validation remain open; feedback delivery/eligibility and the original 48-hour deadline stay unchanged. See [session overruns](10-customer-mobile-appointments.md).

- Proposed: keep one logical review per eligible patient/session and update it through the confirmed mobile edit flow instead of creating duplicate reviews. Keep protected revision history for management; its reporting/retention details remain open.
- Keep session/doctor feedback separate from support-ticket satisfaction so a ticket survey does not become a clinical or practitioner rating.
- Define comment length, ticket-survey response window, session-review retraction/web-editing behavior, notification wording, visibility for the resolving administrator, and retention. Mobile session-review editing within the original 48-hour window is confirmed. Ticket survey comments are optional and its submission remains once only; this edit decision does not change ticket surveys.
- Avoid revealing private staff-only review details in patient notifications. Restrict feedback exports and audit management access.
- Consider a minimum-data report that helps management find service patterns while limiting unnecessary access to identifiable patient details.

Related: [Support tickets](11-support-tickets.md), [Identity and access](05-identity-and-access.md), [System scope](01-system-scope.md), and the [Flutter](../handoff/flutter-developer.md) and [web](../handoff/web-frontend-developer.md) handoffs.
