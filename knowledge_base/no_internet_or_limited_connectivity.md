# No Internet or Limited Connectivity

## Category
Network

## Subcategory
Wired or Wireless Network

## Symptoms
Users may report that the device is connected to ethernet or Wi-Fi but cannot access the internet or organizational services.

Common signs include:
- Windows shows "No Internet" or "Limited Connectivity"
- Websites do not load
- The device receives a self-assigned IP address
- Internal resources work but public websites do not, or the reverse
- Other users are affected in the same area
- The connection drops repeatedly

## Likely Causes
- The network cable is disconnected or damaged
- The wireless signal is weak
- DHCP did not assign a valid address
- DNS is not resolving names
- The network adapter is disabled or frozen
- A proxy or VPN setting is interfering
- The local switch or access point is unavailable
- A broader network outage is occurring

## Troubleshooting Steps
1. Confirm whether the connection is wired or wireless.
2. Check whether other devices are affected.
3. Confirm the ethernet cable is connected or the correct Wi-Fi network is selected.
4. Disable and re-enable the network adapter.
5. Restart the computer.
6. Disconnect from VPN and retest when appropriate.
7. Check the assigned IP address, gateway, and DNS servers.
8. Renew the IP address using the approved support procedure.
9. Test access by hostname and by IP address to identify a DNS issue.
10. Test another cable, wall port, or wireless location.
11. Forget and reconnect to the wireless network if applicable.
12. Check for a known network outage.
13. Record the device location, port, IP address, and error messages.

## Escalation Notes
Escalate if:
- Multiple users are affected
- The device does not receive a valid IP address
- A wall port, switch, or access point appears unavailable
- DNS fails for multiple devices
- Connectivity drops repeatedly after local troubleshooting
- A network outage is suspected

Possible escalation team:
Network Operations / Desktop Support

## Suggested Ticket Comment
I confirmed the connection type, tested the cable or wireless connection, refreshed the network adapter and IP configuration, and checked whether the issue affects other users or locations. I also tested DNS and reviewed whether a broader network outage is present.
The ticket will be escalated if the issue is related to network infrastructure, DHCP, DNS, or the local switch or access point.
