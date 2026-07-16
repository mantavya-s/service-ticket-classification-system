# Suspicious Email or Phishing Report

## Category
Security

## Subcategory
Email Security

## Symptoms
Users may report an unexpected email asking them to click a link, open an attachment, provide credentials, send money, or approve a login.

Common signs include:
- The sender name and email address do not match
- The message creates urgency or threatens account closure
- The email requests a password, MFA approval, gift card, or financial transfer
- A link points to an unfamiliar domain
- The attachment was not expected
- The message appears to come from a colleague but has unusual wording

## Likely Causes
- A phishing or credential-harvesting attempt
- A compromised external account
- Sender-name spoofing
- A malicious attachment or link
- Business email compromise
- A legitimate message that requires verification

## Troubleshooting Steps
1. Tell the user not to click links, open attachments, reply, or approve MFA prompts.
2. Preserve the message for investigation.
3. Review the full sender address, reply-to address, links, and message headers using approved tools.
4. Verify the request through a trusted communication channel.
5. Report the message using the organization's phishing-report function.
6. If the user clicked a link, determine whether credentials were entered.
7. If credentials were entered, reset the password and revoke sessions according to the incident procedure.
8. If an attachment was opened, disconnect the device from the network if malicious activity is suspected.
9. Run the approved endpoint security scan.
10. Check for unusual mailbox rules, forwarding, or sign-in activity when authorized.
11. Do not delete the message until security confirms it is no longer required.

## Escalation Notes
Escalate immediately if:
- Credentials were entered
- An MFA request was approved
- A suspicious attachment was opened
- Money, gift cards, payroll, or banking information is involved
- The account shows unusual sign-ins or mailbox rules
- Multiple users received the same message

Possible escalation team:
Security Operations / Incident Response / Microsoft 365 Security

## Suggested Ticket Comment
The reported message has been preserved and submitted for security review. The user was advised not to interact with the message, and I confirmed whether any links, attachments, credentials, or MFA prompts were involved.
Security escalation has been initiated where account compromise or malicious activity may have occurred.
