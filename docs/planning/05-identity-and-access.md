# Identity roles permissions and dashboard access

Updated: 3 October 2026. Status: user-requested access direction with a proposed detailed model.

The user wants management, doctor or specialist, and patient experiences. Management and specialist dashboards must show details based on permissions, and entry must be restricted to authorized staff. The recommendation is one coherent identity and authorization model serving these experiences, with stronger staff authentication and a separate patient OTP flow.

## Three experiences

| Experience | Primary audience | Purpose |
|---|---|---|
| Management | Managers, system administrators, reception, accounting, marketing, other authorized staff | Operational scheduling, catalog, finance, configuration, reporting, and assigned duties |
| Specialist | Doctors, psychologists, social specialists, and other approved practitioners | Own schedule, consultation work, clinical documentation, treatment tasks, assessment requests |
| Patient | Patients and authorized family representatives | Booking, payment, packages, personal records, tasks, assessments, family management |

The specialist dashboard is a focused workspace over the same backend. It does not require a second identity database or duplicate business logic. Management does not mean every staff user receives all information.

One staff login can route staff into their allowed workspace. Distinct management and specialist entry pages are also possible but should call the same staff authentication system. A user with both authorized staff contexts can choose or switch workspaces. Final UI routing is still open.

Patient OTP login remains separate in assurance and session context. A staff member who is also a patient must not obtain staff powers by logging in through the patient OTP path.

**Confirmed patient direction:** Sign in using a phone number and a sent one-time verification code, then optionally add a username or email through the patient website or mobile app. Verify email ownership before enabling email recovery. A username is an account identifier and cannot alone prove ownership. The [patient login and recovery plan](07-patient-login-and-recovery.md) defines proposed verification and contact-change flows.

## Four different checks

1. **Authentication:** Who is using the system, and how was their identity verified?
2. **Portal access:** Is this identity allowed to enter this workspace with this authentication strength?
3. **Action permission:** May this identity perform this operation?
4. **Resource scope:** May this identity perform it on this patient, appointment, invoice, or recording?

A visible menu is a presentation decision. Every API request still requires applicable action and resource checks. Changing a patient ID or calling an endpoint directly must not bypass access rules.

An illustrative authorization rule is: active account plus appropriate authentication context plus portal entitlement plus action permission plus resource scope plus applicable business constraints.

## Branch scope and task access

**Confirmed:** Patients, doctors, schedules, and reporting are restricted by branch. Employed and external doctors use the same operational access rules, with assigned-patient scope still required. Cross-branch exception grants and central reporting remain open.

**Confirmed:** Reception can assign internal administrative work to accountant and vice versa, with priority and details. This requires accountant participation in the staff workspace; exact role grants remain deferred. Doctor-controlled patient tasks are a separate workflow. Internal tasks support several assignees; management sees full authorized-branch task details and other staff see full created/assigned task details. Live event subscriptions and attachment access must enforce the same scope.

**Proposed:** Apply branch and task-action permissions to internal tasks. A task assignment does not grant clinical-record access or authority to spend money, approve refunds, or post accounting entries. See [internal staff tasks](15-internal-staff-tasks.md).

## Roles and permissions

Roles are configurable bundles of permissions. Initial staff roles from the requirements are General Manager, Executive Manager, System Administrator, Accountant, Reception or Customer Service, Marketing, and Specialist. Different practitioner types may need separate role templates.

**User's current-stage direction:** Start with manager, reception, administrator, and doctor, with accountant participation now required for internal staff tasks. The exact permission matrix remains deferred, including whether administrator means system or operational administrator. Do not grant broad access solely from a role label. Management verifies doctor degrees and applicant data before activation; the verification procedure remains open.

The user expects the interface to show or hide actions according to each staff member's granted permissions. This is a usability rule only: every API operation still enforces the permission and resource scope on the server. Management controls each doctor's active status, and only active doctors may enter the doctor dashboard. Deactivation's effect on existing sessions, tokens, and in-progress work remains open.

Admins can create roles and select permissions from a developer-maintained catalog of supported actions. Creating a permission name in a dashboard does not create a new API capability. Avoid hardcoding clinical and financial access exclusively to a role name.

| Illustrative permission | Scope or extra restriction |
|---|---|
| portal.management.enter | Staff authentication context |
| portal.specialist.enter | Staff authentication and an approved practitioner profile |
| appointments.view | Own practitioner schedule or explicitly granted operational scope |
| appointments.create | Accessible patient and supported booking workflow |
| appointments.reschedule | Appointment scope and policy window or authorized override |
| appointments.complete | Treating practitioner or a separately approved delegated action |
| appointments.override_policy | Sensitive permission with reason and audit |
| scheduling.manage | Manage working hours, leave, breaks, and closures |
| clinical.records.view | Explicit clinical access scope with read audit |
| clinical.encounters.edit | Authorized treating encounter and document state |
| prescriptions.issue | Explicit permission and center-approved practitioner eligibility |
| assessments.request | Authorized practitioner and patient |
| finance.invoices.view | Defined financial scope; no automatic clinical access |
| finance.refunds.execute | Independent sensitive grant and audited workflow |
| finance.wallets.spend_on_behalf | Independent sensitive grant |
| recordings.view | Independent sensitive grant; not implied by clinical access |
| reports.export | Separate from on-screen view permission and bounded by accessible data |
| tasks.assign | Independent grant with allowed assignee and patient scope |
| settings.manage | Scoped configuration authority |
| access.roles.manage | Controlled permission assignment without self-escalation |
| recruitment.applications.view | Authorized recruitment staff; private candidate information |
| recruitment.applications.review | Review and contact tracking within assigned recruitment scope |
| recruitment.applications.accept | Sensitive authority that triggers automatic doctor account/role provisioning and SMS invitation; audit and idempotency required |
| practitioners.onboard | Manual correction or reissue authority where needed; not an additional required approval after acceptance |
| compensation.view | Own practitioner information or explicitly granted finance/management scope |
| compensation.manage | Independent sensitive grant for arrangements and effective dates |
| audit.view | Restricted read-only access |

Permission names are examples, not implemented contracts. Refine the catalog by use case before coding. Keep sensitive permissions explicit rather than automatically granting a wildcard to system administrators.

Proposed initial rule: roles grant permissions and multiple roles combine allowed grants. Resource scope and business constraints still apply. Avoid mixing grant and deny semantics or many individual-user overrides until a concrete requirement justifies their conflict rules.

## Starting role matrix

This matrix is a proposal for discussion, not an approved permission assignment.

| Staff category | Management workspace | Specialist workspace | Default data focus | Additional sensitive grants |
|---|---|---|---|---|
| General or executive manager | Yes | Only with eligible practitioner profile and grant | Approved operational and business reporting | Clinical reads, recordings, financial overrides require explicit decisions |
| System administrator | Yes | Only when independently eligible | Identity and configuration | No automatic clinical or recording access |
| Reception or customer service | Yes | No by default | Booking, contact details, attendance, basic payment status | Refunds, wallet spending, schedule management only if granted |
| Accountant | Yes | No by default | Payments, invoices, receipts, wallets, financial reports | Refund execution and document correction separately granted |
| Marketing | Yes, limited workspace | No by default | Approved offers and marketing reporting | No medical notes or recordings by default |
| Specialist | Only if granted | Yes | Own appointments and treatment work; clinical reads as specified below | Schedule management and recording access only if granted |

The management workspace can show a different landing page and menu for reception, accounting, and marketing without creating a separate dashboard application for every role.

**Confirmed user direction superseding broader source wording:** Each doctor may view records only for their own assigned patients, including external doctors. This is narrower than the source document's permission for all center specialists to read complete medical records. Apply the user's narrower access rule. Define how patient assignment, transfers, coverage, and emergency access work before implementation. Editing remains tied to the authorized encounter. Patient-visible reports versus internal notes also remain to be defined.

**Confirmed patient visibility:** Patients may view all information about their own case through the patient experience. The user has not defined which operational or administrative metadata is outside "their case"; preserve that as an open content boundary.

## Identity and patient relationships

Proposed concepts are Account, StaffProfile, PractitionerProfile, Patient, and AccountPatientAccess or a similarly named relationship. One person may have more than one profile; the operational context must remain explicit.

Account is the authenticated actor. Patient is the beneficiary. A shared phone number is not sufficient evidence that someone may read another person's record. Family access needs a recorded relationship, allowed actions, and revocation behavior. Decide rules for minors, adult family members, adult transition, and delegated access.

Each patient retains independent identity and medical history. The owner of wallet funds and package entitlements remains open: paying account, individual patient, or explicitly shareable entitlements.

**Confirmed family visibility direction:** When both parents have patient records, the father and mother can each see their own details, the other parent's details, and their children's details. Children cannot see their parents' details. A parent does not need a patient record for the family to use the system; for example, if the mother has no patient record, the father and children can still have records and use the system normally. Do not create an empty patient record just to represent a parent.

The precise meaning of "details" (profile, appointments, clinical records, payments, and other data) and whether parents can edit or act on one another's behalf still need definition. The user asked to defer these family-access details for a future discussion. Family visibility must be granted through explicit account-patient relationships, never inferred from a shared phone number.

**Confirmed child-to-adult transition:** Reaching adulthood does not automatically change the child's access or the parents' access. A system administrator decides whether and when to make a change. The specific administrative action, scope, and audit history are deferred for a future discussion.

Candidates applying through the public Join us page receive no practitioner access from submission or contact verification alone. **Confirmed:** Authorized management acceptance automatically provisions the doctor account and practitioner linkage, assigns the configured doctor role, and schedules an SMS invitation. No separate manual account-creation or role-assignment step is required. Credential checks required for the acceptance decision should happen before that decision. Proposed first access verifies the invitation recipient and establishes staff authentication; the patient OTP route still cannot grant staff access. See [practitioner compensation and recruitment](08-practitioner-compensation-and-recruitment.md).

The acceptance workflow can assign only the approved doctor role template, not arbitrary roles supplied by a public application. Existing patient or staff identities require safe identity reconciliation without duplicate users or automatic merging by phone alone. Doctor permissions become usable through the staff authentication context. Practitioner scheduling and compensation details may need configuration after account creation; missing schedules must not accidentally publish bookable availability.

## Login and access changes

- Patient authentication uses phone OTP as confirmed. Optional username/email setup and recovery require account ownership checks; email recovery uses a previously verified address. Exact challenge limits and recovery assurance remain open.
- Staff require stronger authentication. MFA is proposed; staff onboarding is managed by administration in the initial requirements.
- After staff authentication, derive allowed workspaces and effective permissions from trusted server-side assignments.
- A requested workspace or role from the browser is not proof of authorization.
- Staff authentication must not be satisfied solely by a lower-assurance patient session.
- Missing authentication generally leads to 401; an authenticated identity lacking required access generally leads to 403. Keep login responses from exposing sensitive account details.
- Suspend, disable, and role-change actions must invalidate affected access promptly. Avoid permission claims remaining effective for the lifetime of a long-lived token after revocation.
- Distinguish practitioner suspension from account disablement: the source discusses stopping new bookings. Decide access to existing appointments and clinical work explicitly.

Browser cookie or BFF versus bearer-token delivery, mobile token management, session expiry, recovery assurance and technical mechanisms, and the exact identity store remain implementation decisions. Patient recovery functionality is confirmed; its detailed safeguards are proposed. Do not choose session mechanisms merely because dashboards have separate URLs.

## Data exposure and audit

The backend should return only data needed and permitted for the caller, rather than sending full patient objects and hiding fields in the UI. Split contact information, finance, clinical details, and recordings into deliberately authorized query contracts. Filter lists, searches, exports, downloads, and counts consistently.

Audit role changes, sensitive grants, refunds, wallet spending, policy overrides, schedule changes, clinical reads, and recording access. Protect audit records against normal modification or deletion. Record enough context to investigate an action without logging credentials or unneeded clinical payloads.

Use authorization in application workflows as well as HTTP entry points so background or internal callers cannot bypass the rules. Patient ownership and practitioner scope must come from trusted context, not unchecked request identifiers.

## ASP.NET Core direction

Use role membership for grouping, policy-based authorization for supported actions, and resource-based authorization for record scope. ASP.NET Core Identity is a candidate for account and role management; its adoption is proposed, not confirmed. Our dynamic permission catalog and policy-version invalidation need a deliberate design.

## Questions to settle

Agree the staff landing experience, initial role matrix, who may grant sensitive permissions, clinical visibility in the patient portal, the adult-child access transition and exact family data/actions, practitioner prescribing eligibility, and permission-revocation behavior. Establish a controlled first-admin/bootstrap process without implicitly granting every person medical and financial access.

## References

- [ASP.NET Core role authorization](https://learn.microsoft.com/en-us/aspnet/core/security/authorization/roles?view=aspnetcore-10.0)
- [ASP.NET Core policy authorization](https://learn.microsoft.com/en-us/aspnet/core/security/authorization/policies?view=aspnetcore-10.0)
- [ASP.NET Core resource authorization](https://learn.microsoft.com/en-us/aspnet/core/security/authorization/resource-based?view=aspnetcore-10.0)
