# Patient login profile verification and account recovery

Updated: 2 October 2026. Status: confirmed patient direction with proposed detailed workflows. No implementation has started.

Patients sign in with a phone number and a sent verification code. After sign-in they can optionally add a username or email in the patient dashboard or mobile application and recover access using verified evidence. The website and apps use the same account and backend rules.

The sent PIN described in the conversation is interpreted as a one-time password or OTP, not a permanent personal PIN. No permanent PIN or password-based patient login has been requested.

## Confirmed direction

- Phone number plus a sent verification code is the initial sign-in method.
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

Email verification establishes control of that email address, not legal identity. Agree whether verified-email proof alone is sufficient to replace a lost phone for an account exposing medical and financial information.

## Proposed sign-in workflow

1. The patient enters a normalized phone number, including country code.
2. The API creates a short-lived login challenge and sends its code through the configured provider. SMS is the initial candidate; delivery channel configuration remains open.
3. The patient submits the code and challenge reference.
4. The API verifies purpose, destination, expiry, attempt limit, and single-use status, then consumes the challenge atomically.
5. Sign in to the existing account, or create a new account through the approved registration flow after phone verification. Collect required profile fields and consent as appropriate.

Verify ownership and migration matching before exposing an existing medical file. Do not automatically merge imported patient histories solely because they share a phone number. Family beneficiaries are separate patient profiles, not duplicate login accounts with the same phone.

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
| No access to verified phone or email | Center-assisted recovery with a defined identity-check procedure; no automatic bypass |
| Changes phone while signed in | Recently verify ownership through an established channel, verify the new phone, and check account conflicts before replacing the old contact |

A code sent to a newly supplied phone proves control of that new phone, not ownership of the old account. Do not move medical records, wallet funds, family grants, or staff privileges on that evidence alone.

After successful recovery, retain the same immutable account identity and existing patient relationships. Revoke old sessions and outstanding challenges, then require normal sign-in. Notify established safe channels. Updating a number must not overwrite an account already using it; resolve collisions through an approved workflow.

## Challenge and session rules

Use single-use expiring challenges with limited attempts and resend controls. Keep login, email verification, phone change, and recovery challenges purpose-bound. Recovery grants should allow only the intended recovery steps until the flow is complete. Do not put codes or secrets in logs.

Rate-limit delivery and verification without allowing arbitrary recovery requests to permanently lock another person's account. Recovery responses should not disclose whether an account exists. Use supported website links and mobile app links for verification, while the backend enforces the same challenge semantics.

Phone OTP and email recovery must remain patient authentication contexts even when the account also has a staff profile. Staff access still requires its own approved authentication strength and permissions.

## Open decisions

- Code length, expiry, resend interval, and maximum attempts. No numeric defaults have been approved.
- Whether username/email can initiate normal sign-in as well as recovery lookup.
- Whether established verified email is sufficient for phone replacement, or additional evidence is needed.
- Center-assisted recovery evidence, responsible role, review, and auditing.
- Phone recycling, duplicate contact conflicts, username/email normalization and uniqueness, and imported-account matching.
- Browser and mobile session mechanisms, device management, and notification delivery provider.

## Reference

[OWASP recovery guidance](https://cheatsheetseries.owasp.org/cheatsheets/Forgot_Password_Cheat_Sheet.html) supports expiring single-use recovery challenges, consistent responses, abuse controls, and session invalidation after recovery. Its password-reset examples inform these controls; this plan does not add patient passwords.
