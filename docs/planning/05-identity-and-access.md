# Identity roles permissions and dashboard access

Updated: 4 October 2026. Status: user-requested access direction with a proposed detailed model.

The user wants management, doctor or specialist, and patient experiences. Management and specialist dashboards must show details based on permissions, and entry must be restricted to authorized staff. The recommendation is one coherent identity and authorization model serving these experiences, with stronger staff authentication and a separate patient OTP flow.

## Active authentication and authorization planning — 4 October 2026

**Current confirmed access answers:** Patient login uses SMS with a six-digit code, five-minute validity, resend after 60 seconds and five failed attempts per challenge. Imported-record links are preverified during migration where adequate evidence exists, with reception handling unverified/ambiguous cases before access; this approach was selected by the assistant under explicit user delegation. Clinical-record and recording access require separate grants. The owner explicitly authorizes access-management administrators who may assign those grants within branch/patient scope. If a patient loses both phone and verified email, reception verifies identity and an authorized account administrator approves recovery. A deactivated doctor may finish/save only an already-active consultation; new work is blocked immediately and the remaining access ends when that consultation is closed. Proof checklists, detailed role defaults and technical session mechanisms remain to specify.

The user has returned to authentication, authorization and external providers for detailed planning. The earlier discussion deferral for staff permissions/deactivation is superseded for this selected workflow; no permission matrix is approved yet. Related family/assignment access questions can be clarified here, while unrelated financial rules, Emdaad export formats, multi-assignee task completion and translation-format deferrals remain unchanged. See [the detailed workflow](21-authentication-and-authorization-workflows.md).

Confirmed role baseline: reception handles scoped branch bookings/contact details, accountants handle scoped finance, doctors handle assigned patients, and managers receive only owner-assigned operational/reporting permissions. Separate clinical/recording grants remain required; the full granular action matrix is not approved by this baseline. Confirmed self-service safeguard: turning staff SMS verification off or changing its phone requires password confirmation and an SMS code to the existing verified phone. A lost phone uses the approved administrator recovery process. Detailed audit, conflict handling and administrator-change safeguards remain proposals.

Staff lost-phone recovery is approved through an authorized account administrator after identity verification; recovery of the last available administrator requires owner verification. An adult family member must explicitly consent before a parent or another authorized family member can view their clinical records. Family membership, package sharing and payment rights do not establish clinical consent; detailed consent/proof/revocation and minor rules remain open.

**New confirmed answers:** Staff/doctors sign in with username, verified email or phone number plus password. SMS additional verification is enabled by default; each user manages their own setting, and an administrator with the appropriate permission can manage it for all accounts. This concerns staff/doctor additional verification, not optional bypass of patient login OTP. No external-provider accounts are currently available; the project owner will be responsible for all of them. Existing provider preferences are not final selections.


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

**Confirmed:** Reception can assign internal administrative work to accountant and vice versa, with priority and details. This requires accountant participation in the staff workspace; exact role grants are under active clarification. Doctor-controlled patient tasks are a separate workflow. Internal tasks support several assignees; management sees full authorized-branch task details and other staff see full created/assigned task details. Live event subscriptions and attachment access must enforce the same scope.

**Proposed:** Apply branch and task-action permissions to internal tasks. A task assignment does not grant clinical-record access or authority to spend money, approve refunds, or post accounting entries. See [internal staff tasks](15-internal-staff-tasks.md).

## Roles and permissions

Roles are configurable bundles of permissions. Initial staff roles from the requirements are General Manager, Executive Manager, System Administrator, Accountant, Reception or Customer Service, Marketing, and Specialist. Different practitioner types may need separate role templates.

**User's current-stage direction:** Start with manager, reception, administrator, and doctor, with accountant participation now required for internal staff tasks. The exact permission matrix is now under active clarification, including whether administrator means system or operational administrator. Do not grant broad access solely from a role label. Management verifies doctor degrees and applicant data before activation; the verification procedure remains open.

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

**Confirmed user direction superseding broader source wording:** Each doctor may view records only for their own assigned patients, including external doctors. This is narrower than the source document's permission for all center specialists to read complete medical records. Apply the user's narrower access rule. Practitioner changes support session-only assignment and transfer of ongoing follow-up, as confirmed below. Selection/approval authority, coverage and emergency access remain open. Editing remains tied to the authorized encounter. Patient-visible reports versus internal notes also remain to be defined.

### Confirmed practitioner-change modes — 4 October 2026

| Mode | Confirmed behavior | Details still open |
|---|---|---|
| Session only | New practitioner provides the selected session; the existing follow-up practitioner retains ongoing responsibility | Who selects/approves, which prior case records may be read, and when temporary access begins/ends |
| Transfer ongoing follow-up | New practitioner becomes responsible for ongoing follow-up | Who selects/approves, effective date, former practitioner's retained access, and handling of existing appointments, treatment tasks and pending assessments |

Both options are explicitly required. No default mode or automatic transfer from merely booking another practitioner is selected. **Proposed safeguard:** Record the assignment scope and effective period, and enforce it on the server for reads, clinical actions, summaries, exports and files. Session-only work needs authorized access to that patient's relevant case; it does not grant access to unrelated patients. Exact record categories and post-session access remain unresolved. Preserve existing clinical history under either mode.

**Confirmed patient visibility:** Patients may view all information about their own case through the patient experience. The user has not defined which operational or administrative metadata is outside "their case"; preserve that as an open content boundary.

## Identity and patient relationships

Proposed concepts are Account, StaffProfile, PractitionerProfile, Patient, and AccountPatientAccess or a similarly named relationship. One person may have more than one profile; the operational context must remain explicit.

Account is the authenticated actor. Patient is the beneficiary. A shared phone number is not sufficient evidence that someone may read another person's record. Family access needs a recorded relationship, allowed actions, and revocation behavior. Decide rules for minors, adult family members, adult transition, and delegated access.

Each patient retains independent identity and medical history. Package sessions are explicitly shareable across linked family members. Paying-account ownership, wallet ownership, and who may initiate or approve actions for another member remain to define; sharing a package is not permission to withdraw another person's money.

**Confirmed family visibility direction:** When both parents have patient records, the father and mother can each see their own details, the other parent's details, and their children's details. Children cannot see their parents' details. A parent does not need a patient record for the family to use the system; for example, if the mother has no patient record, the father and children can still have records and use the system normally. Do not create an empty patient record just to represent a parent.

**Latest confirmed family actions:** The father or mother adds members. Each member can view their own reports, sessions, diagnoses, and invoices if they paid. Each member can press «الخروج من العائلة»; notify the family head and give the departing member independent booking and the full ordinary patient capabilities. This does not grant staff permissions or access to anyone else's case.

The earlier direction that parents see one another's and children's details, while children cannot see parents' details, has not been explicitly withdrawn. The latest answer specifies own-record categories; adult clinical-record consent is now explicitly required, including between parents. Exact cross-member categories, evidence/withdrawal of consent, relationship evidence and acting on another adult's behalf remain open. Package sharing does not resolve those permissions.

**Child-to-adult transition:** The earlier administrator-controlled transition remains unresolved in its details. The latest self-exit answer does not specify age restrictions or how self-exit interacts with minors/guardian access; clarify that intersection rather than silently granting unrestricted minor self-exit or removing guardian rights. No automatic adulthood change is selected.

**Proposed revocation safeguards:** After an eligible member leaves, revoke former family grants across reads, booking, notifications, exports, and file links; preserve that member's records and financial history. Existing bookings, shared package entitlements, payer invoices, and any retained parental rights need explicit decisions. Exiting must not erase records, transfer money, or duplicate package balances.

Candidates applying through the public Join us page receive no practitioner access from submission or contact verification alone. **Confirmed:** Authorized management acceptance automatically provisions the doctor account and practitioner linkage, assigns the configured doctor role, and schedules an SMS invitation. No separate manual account-creation or role-assignment step is required. Credential checks required for the acceptance decision should happen before that decision. Proposed first access verifies the invitation recipient and establishes staff authentication; the patient OTP route still cannot grant staff access. See [practitioner compensation and recruitment](08-practitioner-compensation-and-recruitment.md).

The acceptance workflow can assign only the approved doctor role template, not arbitrary roles supplied by a public application. Existing patient or staff identities require safe identity reconciliation without duplicate users or automatic merging by phone alone. Doctor permissions become usable through the staff authentication context. Practitioner scheduling and compensation details may need configuration after account creation; missing schedules must not accidentally publish bookable availability.

## Login and access changes

- Patient authentication uses phone OTP as confirmed. Optional username/email setup and recovery require account ownership checks; email recovery uses a previously verified address. Exact challenge limits and recovery assurance remain open.
- **Confirmed on 4 October 2026:** Additional verification for staff/doctor sign-in is a configurable option that can be enabled or disabled. When enabled, deliver the verification code by SMS. Mandatory additional verification for every staff account is not selected. The latest answers select username/verified email/phone plus password, SMS enabled by default, self-service control of the user's own setting and control of all accounts by an administrator with the relevant permission. Self-service disable/phone changes require password plus existing-phone SMS proof; lost-factor recovery uses an authorized account administrator after identity verification, or owner verification for the last administrator. Detailed evidence/audit mechanics and granular permissions remain open in document 21. Staff onboarding is managed by administration in the initial requirements.
- After staff authentication, derive allowed workspaces and effective permissions from trusted server-side assignments.
- A requested workspace or role from the browser is not proof of authorization.
- Staff authentication must not be satisfied solely by a lower-assurance patient session.
- Missing authentication generally leads to 401; an authenticated identity lacking required access generally leads to 403. Keep login responses from exposing sensitive account details.
- Suspend, disable, and role-change actions must invalidate affected access promptly. Avoid permission claims remaining effective for the lifetime of a long-lived token after revocation.
- Distinguish practitioner suspension from account disablement: the source discusses stopping new bookings. Confirmed: block new work immediately and allow only finishing/saving the already-active consultation. Detailed continuation expiry and future-appointment handover remain open.

Browser cookie or BFF versus bearer-token delivery, mobile token management, session expiry, recovery assurance and technical mechanisms, and the exact identity store remain implementation decisions. Patient recovery functionality is confirmed; its detailed safeguards are proposed. Do not choose session mechanisms merely because dashboards have separate URLs.

## Data exposure and audit

The backend should return only data needed and permitted for the caller, rather than sending full patient objects and hiding fields in the UI. Split contact information, finance, clinical details, and recordings into deliberately authorized query contracts. Filter lists, searches, exports, downloads, and counts consistently.

Audit role changes, sensitive grants, refunds, wallet spending, policy overrides, schedule changes, clinical reads, and recording access. Protect audit records against normal modification or deletion. Record enough context to investigate an action without logging credentials or unneeded clinical payloads.

Use authorization in application workflows as well as HTTP entry points so background or internal callers cannot bypass the rules. Patient ownership and practitioner scope must come from trusted context, not unchecked request identifiers.

## ASP.NET Core direction

Use role membership for grouping, policy-based authorization for supported actions, and resource-based authorization for record scope. ASP.NET Core Identity is a candidate for account and role management; its adoption is proposed, not confirmed. Our dynamic permission catalog and policy-version invalidation need a deliberate design.

## Questions to settle

The operational role baseline and sensitive-grant authority are confirmed in document 21. Agree the staff landing experience, remaining granular action defaults, clinical visibility in the patient portal, the adult-child access transition and exact family data/actions, practitioner prescribing eligibility, and permission-revocation behavior. Establish a controlled first-admin/bootstrap process without implicitly granting every person medical and financial access.

## References

- [ASP.NET Core role authorization](https://learn.microsoft.com/en-us/aspnet/core/security/authorization/roles?view=aspnetcore-10.0)
- [ASP.NET Core policy authorization](https://learn.microsoft.com/en-us/aspnet/core/security/authorization/policies?view=aspnetcore-10.0)
- [ASP.NET Core resource authorization](https://learn.microsoft.com/en-us/aspnet/core/security/authorization/resource-based?view=aspnetcore-10.0)

## Confirmed clarification - 4 October 2026

- Doctors may issue finalized clinical reports and prescriptions directly, without a separate management approval step, within granted permissions, assigned-patient scope, and applicable qualifications.

## Wallet approval scope — latest clarification

The patient requests withdrawal within the wallet; a system administrator or accountant may approve only service-refund-origin funds, not coupons. This names approver actors without granting every such account a financial wildcard. Detailed staff permissions are now under active clarification; approval, execution, and bank verification must remain distinct. Family package access does not authorize viewing or withdrawing another member's wallet.
