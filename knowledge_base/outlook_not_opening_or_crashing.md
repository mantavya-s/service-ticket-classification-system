# Outlook Not Opening or Crashing

## Category
Software

## Subcategory
Microsoft Outlook

## Symptoms
Users may report that Outlook will not start, freezes during startup, repeatedly crashes, or displays a loading profile message indefinitely.

Common signs include:
- Outlook remains on "Loading Profile"
- Outlook closes immediately after opening
- Outlook works in safe mode
- Outlook freezes while switching folders
- The issue starts after installing an add-in or update
- An error appears when opening the Outlook profile or data file

## Likely Causes
- A faulty Outlook add-in
- A corrupted Outlook profile
- A damaged Office installation
- An oversized or corrupted OST or PST file
- A Microsoft 365 authentication issue
- A pending Office or Windows update
- Outlook is still running in the background

## Troubleshooting Steps
1. Confirm Outlook is not already running in Task Manager.
2. Restart the computer.
3. Start Outlook in safe mode using `outlook.exe /safe`.
4. If safe mode works, disable non-essential add-ins.
5. Check whether Outlook on the web works for the same account.
6. Install pending Office and Windows updates.
7. Run Microsoft 365 Quick Repair.
8. Create a new Outlook profile and test it.
9. Rebuild the OST file when appropriate.
10. Run the Inbox Repair Tool for a suspected PST issue.
11. Record any error codes or Event Viewer application errors.

## Escalation Notes
Escalate if:
- Outlook continues to crash with a new profile
- The mailbox works in the browser but not after Office repair
- A PST file is damaged and cannot be repaired
- The issue affects multiple users
- Event logs show repeated Office application failures

Possible escalation team:
Desktop Support / Microsoft 365 Administration

## Suggested Ticket Comment
I tested Outlook in safe mode, reviewed the add-ins, confirmed webmail access, and checked the Outlook profile and local data files. I also completed the appropriate Office repair and profile troubleshooting.
The ticket will be escalated if the Outlook installation, mailbox configuration, or data file requires further repair.
