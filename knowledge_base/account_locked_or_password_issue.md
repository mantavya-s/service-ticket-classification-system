# Account Locked or Password Not Working

## Category
Access

## Subcategory
Account Authentication

## Symptoms
Users may report that their password is rejected, their account is locked, or they cannot sign in to organizational services.

Common signs include:
- "Incorrect password" or "Account locked" appears
- The user recently changed their password
- The new password works on one service but not another
- The user is repeatedly prompted for credentials
- The device continues using an old stored password
- The account locks again shortly after being unlocked

## Likely Causes
- The password was entered incorrectly
- Caps Lock or keyboard layout is incorrect
- The password expired
- The account was locked after repeated failed attempts
- A phone, mapped drive, email client, or scheduled task is using an old password
- Password synchronization has not completed
- The account is disabled
- The user is entering a personal account instead of the organizational account

## Troubleshooting Steps
1. Confirm the username and organizational account format.
2. Check Caps Lock, Num Lock, and keyboard layout.
3. Ask the user to test sign-in through the approved password portal.
4. Confirm whether the password recently changed.
5. Unlock the account or initiate a password reset using the approved identity verification process.
6. Have the user sign out and back in on affected devices.
7. Update stored passwords in mobile mail, mapped drives, VPN clients, and applications.
8. Remove stale credentials from Credential Manager when permitted.
9. Monitor whether the account locks again.
10. Record the affected services and time of the lockout.

## Escalation Notes
Escalate if:
- The account is disabled
- The user cannot be securely identity-verified
- The account repeatedly locks after stored credentials are updated
- Password synchronization fails
- Authentication logs indicate suspicious activity

Possible escalation team:
Identity and Access Management / Security Operations

## Suggested Ticket Comment
I verified the user's account information, checked for a lockout or expired password, and completed the approved unlock or password reset process. I also reviewed devices and applications that may still be using an old saved password.

The ticket will be escalated if the account continues to lock or requires an identity-system change.
