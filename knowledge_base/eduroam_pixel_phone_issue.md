# Eduroam Connectivity Issue on a Pixel Phone

## Category
Network

## Subcategory
Android / Google Pixel Wi-Fi

## Symptoms
Users with a Google Pixel phone may report that eduroam does not connect or repeatedly asks for certificate and authentication information.

Common signs include:
- The user cannot connect to eduroam
- The phone asks the user to choose a CA certificate
- The user is unsure which domain or identity settings to enter
- The phone shows "Saved" but does not connect
- Authentication fails even with the correct password
- The phone connected previously but stopped after an Android update or password change
- The connection works on another device

## Likely Causes
- The eduroam profile was manually configured incorrectly
- The required CA certificate settings are missing
- The phone is using the wrong identity format
- The saved eduroam profile contains an old password
- The Android version requires a managed configuration profile
- The device date and time are incorrect
- The user attempted to trust an unverified certificate manually

## Troubleshooting Steps
1. Confirm the phone is a Google Pixel or another Android device using similar settings.
2. Forget the existing eduroam network.
3. Open the Google Play Store.
4. Download the official eduroam configuration application recommended by the institution, such as the eduroam CAT or geteduroam app.
5. Select the correct institution in the application.
6. Download and install the institution's approved eduroam configuration profile.
7. Enter the organizational username in the required format.
8. Enter the current organizational password.
9. Allow the application to configure the Wi-Fi profile.
10. Connect to eduroam.
11. Confirm the phone has internet access.
12. Remove any duplicate manually created eduroam profiles.
13. Confirm automatic date and time are enabled.
14. Do not manually accept an unexpected certificate warning.

## Escalation Notes
Escalate if:
- The institution does not appear in the approved configuration application
- The downloaded configuration profile fails to install
- The user's credentials work elsewhere but not on the Pixel phone
- Multiple Android users are affected
- Authentication logs show a certificate or identity-system failure

Possible escalation team:
Network Operations / Identity and Access Management / Mobile Device Support

## Suggested Ticket Comment
I removed the manually configured eduroam profile and used the approved eduroam configuration application from the Google Play Store to install the institution's wireless settings. I then verified the organizational username format, current password, and automatic date and time settings.

The ticket will be escalated if the approved profile fails or the wireless authentication service rejects the device.
