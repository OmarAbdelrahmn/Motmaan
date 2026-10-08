# Patient login profile verification and account recovery

Updated: 8 October 2026. Status: patient direction and established-email lost-phone recovery confirmed, with proposed detailed workflows. No implementation has started.

Patients sign in with a phone number and a sent verification code. After sign-in they can optionally add a username or email in the patient dashboard or mobile application and recover access using verified evidence. The website and apps use the same account and backend rules.

The sent PIN described in the conversation is interpreted as a one-time password or OTP, not a permanent personal PIN. No permanent PIN or password-based patient login has been requested.

## Active authentication and authorization planning — 4 October 2026

**Current confirmed access answers:** Patient login uses SMS with a six-digit code, five-minute validity, resend after 60 seconds and five failed attempts per challenge. Imported-record links are preverified during migration where adequate evidence exists, with reception handling unverified/ambiguous cases before access; this approach was selected by the assistant under explicit user delegation. Clinical-record and recording access require separate grants. The owner explicitly authorizes access-management administrators who may assign those grants within branch/patient scope. If a patient loses both phone and verified email, reception verifies identity and an authorized account administrator approves recovery. A deactivated doctor may finish/save only an already-active consultation; new work is blocked immediately and the remaining access ends when that consultation is closed. Proof checklists, detailed role defaults and technical session mechanisms remain to specify.

The user has returned to authentication, authorization and external providers for detailed planning. The earlier discussion deferral for staff permissions/deactivation is superseded for this selected workflow; no permission matrix is approved yet. Further identity/family lifecycle details are deferred under AUD-10; confirmed access rules remain, while unrelated financial rules, Emdaad export formats, multi-assignee task completion and translation-format deferrals remain unchanged. See [the detailed workflow](21-authentication-and-authorization-workflows.md).

Staff lost-phone recovery is approved through an authorized account administrator after identity verification; recovery of the last available administrator requires owner verification. An adult family member must explicitly consent before a parent or another authorized family member can view their clinical records. Family membership, package sharing and payment rights do not establish clinical consent; detailed consent/proof/revocation and minor rules remain open.

**Earlier confirmed answers:** Staff/doctors sign in with username, verified email or phone number plus password. Ordinary staff SMS is enabled by default and self/authorized-administrator managed, subject to mandatory privileged verification/step-up (AUD-08). This concerns staff/doctor additional verification, not optional bypass of patient login OTP. The project owner is responsible for external-provider accounts. The 4 October inventory found none available then; the later MyFatoorah selection and Tabby/Tamara readiness report need account-specific access details.


## Confirmed direction

- Phone number plus a sent SMS verification code is the initial sign-in method. Confirmed configurable defaults: six digits, five-minute validity, resend after 60 seconds and five failed attempts per challenge.
- Username and email setup are optional after sign-in.
- Verification is required for recovery and account changes.
- The capabilities must work in the patient website and mobile apps.

## Identifiers and proof of ownership

| Item | Purpose | Verification |
|---|---|---|
| Phone number | Initial login identifier and code destination | Successful purpose-bound phone OTP challenge |
| Email | Optional contact and proposed alternate recovery channel | Successful verification link or code sent to that address |
| Username | Optional unique account alias and recovery lookup | Set by the authenticated owner after recent verification; validate availability and format |

A username has no inbox and cannot receive a verification code. Knowing a username, phone number, email address, or patient identity number does not itself establish account ownership. Recovery by username must resolve to a previously established verified channel or a separately approved identity-check process.

Email verification establishes control of that email address, not legal identity. **Confirmed on 4 October 2026:** Proof through the patient's previously established verified email is sufficient to recover and replace a lost phone number, without an administration review requirement. The recovery challenge must go to that established address; a newly supplied email is not ownership proof. Verify control of the replacement phone before completing the change, as in the proposed recovery flow.

## Proposed sign-in workflow

1. The patient enters a normalized phone number, including country code.
2. The API creates a short-lived login challenge and sends its code through the configured provider. SMS is selected. Use the confirmed configurable patient defaults: six digits, five-minute validity, 60-second resend interval and five failed attempts per challenge; provider routing remains to validate.
3. The patient submits the code and challenge reference.
4. The API verifies purpose, destination, expiry, attempt limit, and single-use status, then consumes the challenge atomically.
5. Sign in to the existing account, or create a new account through the approved registration flow after phone verification. Collect required profile fields and consent as appropriate.

Verify ownership and migration matching before exposing an existing medical file. Do not automatically merge imported patient histories solely because they share a phone number. Family beneficiaries are separate patient profiles, not duplicate login accounts with the same phone.

**Confirmed and delegated approach, 4 October 2026:** Existing data is seeded/imported before operation. The owner delegated imported-record linking design: prepare evidence-backed, verified account-to-patient links during migration; reception reviews unverified, duplicate/shared/recycled-phone and ambiguous cases before record access. Successful SMS login authenticates the account but does not by itself link an imported record. Candidate matches must remain separate from verified grants; do not merge family clinical histories. The approach is resolved; exact proof checklist, link-finalization grants, seeded fields and correction handling remain open in [workflow 21](21-authentication-and-authorization-workflows.md). Emdaad export-format discussion remains deferred.

## Optional setup in account settings

For username or recovery-email setup, require an authenticated patient session plus recent verification of an established trusted channel. A forgotten-phone recovery flow is a separate exception, not permission to attach arbitrary new contacts from an old session.

For an email addition or change, verify the proposed address before making it eligible for recovery. Keep the current verified address active until replacement is completed. Alert established safe channels to sensitive changes. Define email uniqueness and normalization rules before allowing recovery lookup.

For username setup, validate uniqueness and allowed format and attach it to the existing account. Do not create another account or request an impossible verification code "to the username".

The recommended initial regular login remains phone OTP. Username/email-assisted recovery is included; using email OTP or username plus another factor for everyday sign-in remains open. A password is not implied by adding either identifier.

## Proposed recovery cases

| Situation | Proposed flow |
|---|---|
| Still controls the phone | Normal phone OTP sign-in; no password reset is needed |
| Lost the phone and has an established verified email | Identify the account, verify a recovery challenge sent to that email, receive limited recovery authority, then verify the replacement phone before completing recovery |
| Remembers only the username | Use it for lookup; send proof to an established verified channel without granting access from the username alone |
| No access to verified phone or email | **Confirmed:** reception verifies identity and an authorized account administrator approves recovery; evidence/checklist and restricted recovery mechanics remain to define |
| Changes phone while signed in | Recently verify ownership through an established channel, verify the new phone, and check account conflicts before replacing the old contact |

A code sent to a newly supplied phone proves control of that new phone, not ownership of the old account. Do not move medical records, wallet funds, family grants, or staff privileges on that evidence alone.

After successful recovery, retain the same immutable account identity and existing patient relationships. Revoke old sessions and outstanding challenges, then require normal sign-in. Notify established safe channels. Updating a number must not overwrite an account already using it; resolve collisions through an approved workflow.

## Challenge and session rules

Use single-use expiring challenges with limited attempts and resend controls. Keep login, email verification, phone change, and recovery challenges purpose-bound. Recovery grants should allow only the intended recovery steps until the flow is complete. Do not put codes or secrets in logs.

Rate-limit delivery and verification without allowing arbitrary recovery requests to permanently lock another person's account. Recovery responses should not disclose whether an account exists. Use supported website links and mobile app links for verification, while the backend enforces the same challenge semantics.

Phone OTP and email recovery must remain patient authentication contexts even when the account also has a staff profile. Staff access still requires its own approved authentication strength and permissions.

## Open and deferred details

**AUD-10: Deferred.** Further identity/family/guardian/beneficiary/consent lifecycle/evidence choices below are preserved for later; do not redesign or invent them. Existing patient SMS, recovery actors, verified linking and consent rules remain. Nondeferred technical mechanics can be designed without changing policy.

- **Review follow-up R13, 4 October 2026:** Define account deletion request/status, identity verification, active appointments and balances, family-grant revocation, retained-data explanation and web/mobile entry points. Account deletion is distinct from logout, disablement and leaving a family; no medical-record destruction policy is selected. See the store-policy evidence and recommended release work in the [readiness review](20-development-readiness-review.md).

- Patient SMS defaults are resolved: six digits, five-minute validity, 60-second resend and five failed attempts. Aggregate delivery/abuse limits, staff-code defaults and email/invitation lifetimes remain separate technical proposals.
- Whether username/email can initiate normal sign-in as well as recovery lookup.
- Established verified-email recovery is sufficient for phone replacement without administration review (confirmed). Exact challenge/session mechanics remain open.
- Center-assisted recovery actors are resolved: reception verifies identity; authorized account administrator approves. Exact evidence, review/audit checklist and safe contact-conflict resolution remain open.
- Phone recycling, duplicate contact conflicts and username/email normalization/uniqueness. Imported-record linking uses the delegated verified-prelink/reception-exception approach; exact evidence and correction checklist remain open.
- Browser and mobile session mechanisms, device management, and notification delivery provider.

## Messaging candidate clarification — 4 October 2026

The user identified Wati for WhatsApp/SMS handling. The [provider review](17-provider-documentation-development-notes.md#whatsapp-and-sms-handling-wati) records its authentication-message and fallback capabilities and unresolved Saudi route/API dependencies. This does not select WhatsApp-first login or prove Wati provides challenge generation/verification. Preserve the purpose-bound, single-use backend challenge, expiry, resend and attempt controls across transport retries or fallback; late delivery must not extend validity. Patient SMS channel and four basic defaults are now confirmed; final vendor/route, aggregate limits and any fallback behavior remain open.

## Reference

[OWASP recovery guidance](https://cheatsheetseries.owasp.org/cheatsheets/Forgot_Password_Cheat_Sheet.html) supports expiring single-use recovery challenges, consistent responses, abuse controls, and session invalidation after recovery. Its password-reset examples inform these controls; this plan does not add patient passwords.
