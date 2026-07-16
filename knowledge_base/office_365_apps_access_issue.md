# Unable to Access Office 365 Apps

## Category
Software

## Subcategory
Microsoft 365 Applications

## Symptoms
Users may report that Outlook, Word, Excel, PowerPoint, Teams, or another Microsoft 365 application will not open or shows an activation or sign-in error.

Common signs include:
- Office displays "Unlicensed Product"
- The user is repeatedly prompted to sign in
- Applications open in reduced functionality mode
- The user can sign in through a browser but not the desktop application
- Office applications close immediately after launch
- The user receives a message stating that no license is assigned

## Likely Causes
- A Microsoft 365 license is missing or incorrectly assigned
- The user is signed in with the wrong account
- Cached Microsoft credentials are corrupted
- The Office installation is damaged
- The device has not completed license synchronization
- The computer date and time are incorrect
- A network, proxy, or conditional-access policy is blocking activation

## Troubleshooting Steps
1. Confirm which Microsoft 365 application is affected.
2. Confirm whether the user can sign in at the Microsoft 365 web portal.
3. Verify that the user is signing in with the correct organizational account.
4. Confirm that the required Microsoft 365 license is assigned.
5. Sign out of all Office applications.
6. Close the applications and restart the computer.
7. Sign back in with the organizational account.
8. Remove outdated Microsoft credentials from Credential Manager when permitted.
9. Confirm the computer date, time, and time zone are correct.
10. Run Microsoft 365 Quick Repair.
11. If needed, run Online Repair.
12. Test the application on another managed computer or through the web version.
13. Record the exact error message and affected applications.

## Escalation Notes
Escalate if:
- The user has no required Microsoft 365 license
- The license is assigned but does not activate after synchronization
- Conditional-access or tenant policy errors appear
- Office repair does not resolve the issue
- Multiple users are affected

Possible escalation team:
Microsoft 365 Administration / Desktop Support / Identity and Access Management

## Suggested Ticket Comment
I confirmed the affected Microsoft 365 applications, verified the account being used, and checked whether the required license is assigned. I also tested web access, refreshed the Office sign-in, and ran the appropriate Office repair steps.
The ticket will be escalated to Microsoft 365 administration if the license or tenant configuration requires correction.
