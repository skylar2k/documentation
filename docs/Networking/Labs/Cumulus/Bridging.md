## Introduction
This lab is for gaining familiarity with basic L2 functionality in the Cumulus platform.

## Topology
This is the network topology used in this lab:

![[Pasted image 20240210125527.png]]
PC1 and PC2 are two clients in the same L2 domain (VLAN 10) that want to communicate with each other.
## Bridging on Cumulus
Since Cumulus is based on Debian Linux, it uses the traditional concept of a Linux bridge. Meaning it behaves like a virtual switch and interconnects different network interfaces on the same host. Linux bridging supports VLAN filtering, which allows us to configure different VLANs on the bridge port.
```shell
# Configure the default bridge called br_default, this bridge has no ports assigned by default
cumulus@cumulus:mgmt:~$ nv set interface swp1-2 bridge domain br_default
cumulus@cumulus:mgmt:~$ nv set bridge domain br_default vlan 10,20
cumulus@cumulus:mgmt:~$ nv set bridge domain br_default untagged 1
# Drop untagged frames
cumulus@cumulus:mgmt:~$ nv set interface swp1 bridge domain br_default untagged none
# Port port into access mode
cumulus@cumulus:mgmt:~$ nv set interface swp2 bridge domain br_default access 10
cumulus@cumulus:mgmt:~$ nv config apply
```
Repeat this configuration on the second switch and bridging should be functional.
## Verification
- Hosts can now ping each other:
![[Pasted image 20240210133526.png]] 
- Output for bridge domain br_default:
![[Pasted image 20240210134149.png]]
- VLAN filter list for links:
![[Pasted image 20240210134949.png]]