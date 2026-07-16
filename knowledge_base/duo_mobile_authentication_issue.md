# Duo Mobile Authentication Issue

## Category
Access

## Subcategory
Multi-Factor Authentication

## Symptoms
Users may report that they cannot approve a Duo prompt, receive a passcode, or complete authentication.

Common signs include:
- Duo Push is not received
- The user replaced or reset their phone
- The Duo account shows an old phone number or device
- The activation link has expired
- The user is locked out after repeated attempts
- The phone has no internet connection
- Duo Mobile opens but shows no account
- User cannot sign in to managed websites

## Likely Causes
- The device was not enrolled correctly
- The user changed phones or phone numbers
- Notifications are disabled
- The phone has no data or Wi-Fi connection
- Automatic date and time are disabled
- The Duo activation link expired
- The account or device requires reactivation
- The user is selecting the wrong authentication method

## Troubleshooting Steps
1. Confirm the user can access the phone associated with Duo.
2. Confirm the phone has an internet connection.
3. Open Duo Mobile and check whether the organizational account appears.
4. Confirm notifications are enabled for Duo Mobile.
5. Enable automatic date and time on the phone.
6. Retry authentication and select Send Me a Push.
7. If push fails, test a passcode, phone call, or SMS method if permitted.
8. Confirm whether the user recently changed or reset their phone.
9. Reactivate or re-enroll the device using the approved identity verification process.
10. Remove an outdated device only after verifying the user's identity.
11. Test the new enrollment before closing the ticket.

## Escalation Notes
Escalate if:
- The user cannot be securely identity-verified
- The Duo account is locked or disabled
- The device cannot be reactivated
- No backup authentication method is available
- Multiple users are not receiving Duo prompts

Possible escalation team:
Identity and Access Management / Security Operations

## Suggested Ticket Comment
I verified the user's identity, confirmed the registered device, checked the phone's connectivity and notification settings, and tested the available Duo authentication methods. The device was reactivated or re-enrolled where required.

The ticket will be escalated if the Duo account or identity system requires an administrative reset.
