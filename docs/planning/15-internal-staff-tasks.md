# Internal staff tasks

Updated: 8 October 2026. Planning only; no implementation is authorized.

## Confirmed requirement

- Administrative task system inside Motmaan.
- Reception can assign work to accountant, and accountant can assign work to reception.
- Tasks include priority and task details.
- Priorities are Low, Normal, High, and Urgent.
- A task can have several assignees.
- A due date is optional; show overdue work when a due date has passed.
- Support discussion comments and file attachments.
- Tasks close automatically after the required completion condition is met, without a creator approval step. Whether all assignees must finish remains open.
- Staff notifications persist in an unread list, including events missed while the website is closed.
- Status changes happen automatically from task actions. Exact labels and action-to-status mapping still need definition; the answer does not approve arbitrary manual status changes.
- Assignment, comments, status changes, approaching deadlines, and overdue events produce live notifications inside the website. External email/SMS/mobile-push delivery is not confirmed for internal tasks.
- Management sees full task details within its authorized branch scope. Other staff see full details of tasks they created or are assigned; action rights still depend on permissions.
- Accountant participation is required in the staff workspace; exact granular grants remain open in workflow 21; role defaults plus individual allowed/removed overrides are confirmed (AUD-09).
- Patient treatment tasks are a separate doctor-controlled workflow, including their reminder schedule. Internal tasks are distinct from patient self-care tasks and patient support tickets.
- Patients, doctors, schedules, and reporting are branch-restricted. Internal-task branch ownership and cross-branch assignment remain open.

## Proposed initial design

A management-dashboard task list and detail page, with filters for assignee, status, priority, and authorized branch. Confirmed content includes details, several assignees, priority, optional due date, comments, and attachments. Proposed supporting fields include task ID, title, creator, branch, timestamps, completion note, and audit history.

Suggested status labels remain New, In progress, Blocked, Completed, Cancelled. The confirmed rule is to derive status from actions, rather than treat a status dropdown as the workflow. Proposed examples: creation produces New, starting work produces In progress, and an explicit block/cancel action produces its matching state. Completion must follow an agreed multi-assignee rule; one person's completion must not silently close everyone else's work before that rule is decided. These mappings are proposals.

An overdue indicator is based on the optional due date; whether it creates a separate status remains open. Deadline warning offsets and notification recipients per event remain open. Live website notifications and persistent unread history, including events missed while the website is closed, are confirmed. Transport technology and reconnect behavior remain open.

Apply server-side action permissions and task scope to task reads, live events, and attachment downloads. Assignment must not grant clinical-record access or authority to spend funds, approve refunds, or post accounting entries. References to appointments/tickets/documents reveal only authorized context. Keep audit history and bounded lists; confirmed attachments use the [secure/resumable file lifecycle](03-integrations-and-storage.md#secure-file-lifecycle--aud-23), with file limits still to define. Full task details never grant unrelated module access.

## Open details

**Deferred by the user on 4 October 2026:** Whether all assignees must complete their parts or one employee can complete a shared task for everyone. Keep multiple assignees and automatic closure once the eventual completion condition is met; no condition is selected yet. Do not re-ask this question until the user returns to it.

- Exact automatic action-to-status mapping, per-assignee progress, whole-task completion condition, and reassignment. Creator approval is not required.
- Deadline warning offsets, notification recipients and escalation. Persistent unread history is confirmed.
- File types/sizes, linked records, recurring work, and audit/retention details.
- Branch ownership and cross-branch assignment.

The next batch is in [the question tracker](12-user-notes-and-open-questions.md). Detailed staff grants remain open in the selected workflow, preserving the separately deferred multi-assignee completion condition. See [identity and access](05-identity-and-access.md) and [web handoff](../handoff/web-frontend-developer.md).
