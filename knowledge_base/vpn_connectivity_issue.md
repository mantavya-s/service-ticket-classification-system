# VPN Connectivity Issue

## Category
Network

## Subcategory
Remote Access VPN

## Symptoms
Users may report that the VPN will not connect, disconnects frequently, or connects without providing access to internal resources.

Common signs include:
- The VPN client displays a connection failure
- Authentication or Duo completes, but the VPN does not connect
- The VPN connects and then immediately disconnects
- Internal websites or network drives remain unavailable
- The VPN works on one network but not another
- The client reports a certificate, gateway, or timeout error

## Likely Causes
- The device has no stable internet connection
- The VPN client is outdated or corrupted
- The user is entering incorrect credentials
- Duo authentication is failing
- The device certificate is missing or expired
- The user's VPN entitlement is missing
- The local router, firewall, or internet provider is blocking VPN traffic
- The VPN service is unavailable

## Troubleshooting Steps
1. Confirm the device has working internet access without the VPN.
2. Record the VPN client name and exact error message.
3. Confirm the correct VPN gateway or profile is selected.
4. Verify the user's organizational credentials.
5. Confirm Duo authentication completes.
6. Restart the VPN client.
7. Restart the computer.
8. Test from another internet connection, such as a mobile hotspot.
9. Update or reinstall the approved VPN client.
10. Confirm the device date and time are correct.
11. Verify the required device certificate exists and is valid.
12. Confirm the user is authorized for VPN access.
13. Test access to a known internal resource after connecting.
14. Check for a known VPN service outage.

## Escalation Notes
Escalate if:
- The user lacks VPN entitlement
- The required certificate is missing or expired
- Multiple users cannot connect
- The VPN service is unavailable
- The issue occurs across multiple internet connections
- Authentication succeeds but internal routes or resources are unavailable

Possible escalation team:
Network Operations / Identity and Access Management / Security Operations

## Suggested Ticket Comment
I confirmed the user's internet connection, verified the VPN profile and credentials, tested Duo authentication, and checked the VPN client and device certificate. I also tested the connection from an alternate network and confirmed whether internal resources were reachable.
The ticket will be escalated if VPN authorization, certificate, gateway, or routing changes are required.
