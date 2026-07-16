# Network Shared Drive Access Issue

## Category
Access

## Subcategory
File Share Permissions

## Symptoms
Users may report that they cannot open a network drive, shared folder, or departmental file location.

Common signs include:
- The mapped drive is missing
- Access is denied
- The drive shows a red X
- The user can see the folder but cannot open or edit files
- The drive works on campus but not remotely
- A new employee or role change requires access

## Likely Causes
- The user is not connected to the organizational network or VPN
- The network drive is not mapped
- The user does not have the required group or folder permission
- Stored credentials are outdated
- The file server path has changed
- The drive mapping policy has not applied
- The file server is unavailable

## Troubleshooting Steps
1. Confirm the exact drive letter, folder name, or UNC path.
2. Confirm whether the user is on-site or remote.
3. Connect the user to the organizational network or VPN.
4. Test access using the full UNC path.
5. Confirm the user has the required security group or folder permission.
6. Remove and remap the network drive if the mapping is incorrect.
7. Clear outdated stored credentials when permitted.
8. Run a group policy update if drive mappings are policy-based.
9. Test access from another managed computer.
10. Confirm whether other users can access the same location.

## Escalation Notes
Escalate if:
- The required security group or folder permission is missing
- The file server or share is unavailable
- Multiple users are affected
- The user requires access approval from a data owner
- Permissions are correct but access is still denied

Possible escalation team:
Identity and Access Management / File Services / Server Administration

## Suggested Ticket Comment
I confirmed the requested shared drive and path, verified network or VPN connectivity, checked the drive mapping, and reviewed whether the user has the required access group or folder permission.
The ticket will be escalated to the file services or access team if permission assignment or server-side troubleshooting is required.
