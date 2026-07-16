# Unable to Access Managed Website

## Category
Security

## Subcategory
Certificate / Trusted Website Access

## Symptoms
Users may report that an internal or managed website does not open, shows a certificate warning, or is blocked as untrusted.

Common signs include:
- The browser displays "Your connection is not private"
- The site reports an invalid or untrusted certificate
- The website works on another managed computer
- The user can access public websites but not the managed site
- The browser shows a certificate chain or issuer error
- The issue appears after a device replacement or reimage

## Likely Causes
- A required root or intermediate certificate is missing
- The computer certificate store is outdated
- The browser is using an outdated certificate cache
- The computer date and time are incorrect
- The website certificate has expired or does not match the site name
- The device has not received the required group policy
- A proxy, SSL inspection, or security agent certificate is missing

## Troubleshooting Steps
1. Confirm the exact website address and browser error.
2. Open the same website on a known working managed computer.
3. View the certificate details on the working computer.
4. Record the certificate issuer, subject, expiration date, and certificate chain.
5. Open the certificate details on the affected computer.
6. Compare the root and intermediate certificates on both computers.
7. Confirm the required certificates exist in the appropriate trusted certificate stores.
8. Do not bypass or permanently accept an untrusted certificate warning.
9. Confirm the affected computer's date, time, and time zone.
10. Run a group policy update and restart the computer if certificates are deployed through policy.
11. Confirm the device is connected to the organizational network or VPN.
12. Clear the browser cache and restart the browser.
13. If an approved certificate is missing, install or deploy it using the organization's authorized process.
14. If the website certificate itself is expired or mismatched, stop troubleshooting the endpoint and escalate the website certificate issue.

## Escalation Notes
Escalate if:
- The website certificate is expired, mismatched, or revoked
- The required root or intermediate certificate is not available through the approved source
- Group policy does not deploy the certificate
- Multiple managed computers are affected
- The issue involves SSL inspection, proxy, or endpoint-security certificates
- The user is being asked to bypass a certificate warning

Possible escalation team:
Security Operations / Public Key Infrastructure Team / Web Application Support / Endpoint Management

## Suggested Ticket Comment
I reproduced the website issue and compared the certificate chain on the affected computer with a known working managed computer. I checked the root and intermediate certificate stores, confirmed the system date and time, refreshed group policy, and verified network or VPN connectivity.
The ticket will be escalated if the website certificate or centrally managed certificate deployment requires correction.
