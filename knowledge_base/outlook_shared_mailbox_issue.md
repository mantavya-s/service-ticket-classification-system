# Outlook Shared Mailbox Issue

## Category
Access

## Subcategory
Shared Mailbox Permissions

## Symptoms
Users may report that a shared mailbox is missing, cannot be opened, or does not allow them to send messages.

Common signs include:
- The mailbox does not appear in Outlook
- Outlook displays "Cannot expand the folder"
- The user can read the mailbox but cannot send from it
- The user receives a permission error
- The mailbox works in Outlook on the web but not the desktop application
- Newly assigned access is not yet visible

## Likely Causes
- Full Access permission is missing
- Send As or Send on Behalf permission is missing
- Permission changes have not completed synchronization
- Outlook automapping did not add the mailbox
- The mailbox was added using the wrong account or method
- Cached Outlook profile data is outdated
- The mailbox has been hidden, renamed, or removed

## Troubleshooting Steps
1. Confirm the exact shared mailbox name and email address.
2. Confirm what access the user requires: read access, Send As, or Send on Behalf.
3. Verify the user has the required mailbox permissions.
4. Allow time for newly assigned permissions to synchronize.
5. Restart Outlook.
6. Test the shared mailbox in Outlook on the web.
7. Manually add the shared mailbox if automapping did not work.
8. Remove and re-add the mailbox if the configuration is incorrect.
9. Create a new Outlook profile if the issue appears to be profile-related.
10. Record the exact error and whether reading or sending is affected.

## Escalation Notes
Escalate if:
- Required permissions are missing
- Send As or Send on Behalf must be assigned
- The mailbox is not found in the directory
- Permissions are correct but access still fails after synchronization
- Multiple users cannot access the same mailbox

Possible escalation team:
Microsoft 365 Administration / Identity and Access Management

## Suggested Ticket Comment
I confirmed the shared mailbox and the level of access required, checked whether Full Access and sending permissions are assigned, and tested the mailbox in both Outlook and Outlook on the web. I also refreshed the Outlook mailbox configuration where applicable.
The ticket will be escalated if mailbox permissions or Microsoft 365 configuration changes are required.
