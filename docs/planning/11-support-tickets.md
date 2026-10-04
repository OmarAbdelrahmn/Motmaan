# Support ticket system

Updated: 3 October 2026. Status: patient support-ticket flow and basic statuses are confirmed; remaining operational details are open. No implementation has started.

## Goal

Give patients a trackable way to ask Motmaan for help and give authorized staff a queue to review, respond, and resolve requests. This should be a ticket workflow with ownership and history, not an untracked message sent to a shared inbox.

## Proposed first workflow

1. A signed-in patient opens a support request from the mobile app or patient website.
2. The patient chooses a request category, enters a subject and message, and optionally adds an attachment if allowed.
3. The API creates a ticket number and initial status and returns it to the patient.
4. Authorized management/support staff see the ticket in a work queue, assign an owner, and reply or change status.
5. The patient sees replies and status updates in the same ticket and receives configured notifications.
6. Preserve the conversation, assignment, status changes, and resolution in the ticket history.

**Confirmed:** Only patients submit support tickets. Administrators handle and resolve them. Use the statuses Open, In progress, Waiting for patient, Resolved, and Closed. Send push notifications and show a new-message/update indicator in the patient's ticket experience. When the ticket is Closed, email the patient a satisfaction survey with a rating out of 10 and optional written comments; allow one submission per ticket and associate it with the resolving administrator. Management sees all results; the patient sees their own response. Other users do not see it. Survey expiry and service targets remain open.

## Suggested ticket data

- Ticket number, requester account, optional patient/appointment reference, category, subject, message thread, status, assigned support staff member, created/updated/resolved timestamps, and resolution reason.
- Keep public replies separate from internal staff notes.
- Store attachments privately with access checked for every download. Do not copy medical-record attachments into ticket storage implicitly.
- Log assignment and status changes. Return only ticket content the current requester or authorized staff member may access.

## Security and privacy

- A patient can access only their own tickets, unless a separately approved family authorization permits acting for another patient.
- Support staff need explicit permissions for the support queue. A ticket role does not grant access to the patient's clinical record.
- If a ticket is linked to an appointment or case, show only the minimum authorized context; opening a ticket must not bypass doctor assignment or clinical-record rules.
- Validate, limit, and scan attachments. Do not expose public storage URLs or file credentials.
- Keep audit history, rate-limit public ticket creation, and avoid putting unnecessary medical details into email, SMS, or push notifications.
- A closed-ticket satisfaction response links to the resolved ticket and its resolving administrator. Management sees all responses; the patient sees their own. See [patient session feedback](14-patient-session-feedback.md).

## Questions before implementation

- Which administrator/support permissions allow viewing, assigning, replying, resolving, and closing tickets?
- Can patients reopen a resolved ticket, and for how long?
- Are attachments supported, which file types/sizes are allowed, and how long are they retained?
- What comment length, survey response deadline, and reopened/reclosed ticket behavior should apply? Optional comments and one submission per ticket are confirmed.
- What response hours, priorities, escalation rules, and service targets apply?
- Can staff link or convert a support ticket to an appointment, clinical follow-up, or internal task?

## Related notes

- [System scope](01-system-scope.md)
- [Identity and access](05-identity-and-access.md)
- [Performance, security, and responsive websites](09-performance-security-and-responsive-websites.md)
- [Decisions and open questions](06-decisions-and-open-questions.md)
