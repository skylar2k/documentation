## Introduction
This lab uses a spine-leaf topology and configures the following:

- BGP unnumbered on spines and leafs 
- MLAG between leaf pairs
- AlmaLinux with LACP bonding
## Topology
The following topology is used:

![[Pasted image 20240219121202.png]]
## Configuration
???+ example "Interfaces"

	=== "leaf1"
		```bash linenums="1"
		nv set interface lo ip address 10.10.10.1/32
		nv set interface swp1,swp10-11,swp23-24
		nv set interface bond1 bond member swp1
		nv set interface bond1 bond mlag id 1
		nv set interface bond1 bridge domain br_default
		```
	=== "leaf2"
		```bash linenums="1"
		nv set interface lo ip address 10.10.10.2/32
		nv set interface swp1,swp10-11,swp23-24
		nv set interface bond1 bond member swp1
		nv set interface bond1 bond mlag id 1
		nv set interface bond1 bridge domain br_default
		```
	=== "leaf3"
		```bash linenums="1"
		nv set interface lo ip address 10.10.10.3/32
		nv set interface swp1,swp10-11,swp23-24
		nv set interface bond1 bond member swp1
		nv set interface bond1 bond mlag id 1
		nv set interface bond1 bridge domain br_default
		```
	=== "leaf4"
		```bash linenums="1"
		nv set interface lo ip address 10.10.10.4/32
		nv set interface swp1,swp10-11,swp23-24
		nv set interface bond1 bond member swp1
		nv set interface bond1 bond mlag id 1
		nv set interface bond1 bridge domain br_default
		```
	=== "spine1"
		```bash linenums="1"
		nv set interface lo ip address 10.10.10.101/32
		nv set interface swp1-4
		```
	=== "spine2"
		```bash linenums="1"
		nv set interface lo ip address 10.10.10.102/32
		nv set interface swp1-4
		```
???+ example "Peer links"
	=== "leaf1"
		```bash linenums="1"
		nv set interface peerlink bond member swp10-11
		nv set mlag mac-address 44:38:39:BE:EF:AA
		nv set mlag backup 10.10.10.2
		nv set mlag peer-ip linklocal
		```
	=== "leaf2"
		```bash linenums="1"
		nv set interface peerlink bond member swp10-11
		nv set mlag mac-address 44:38:39:BE:EF:AA
		nv set mlag backup 10.10.10.1
		nv set mlag peer-ip linklocal
		```
	=== "leaf3"
		```bash linenums="1"
		nv set interface peerlink bond member swp10-11
		nv set mlag mac-address 44:38:39:BE:EF:AA
		nv set mlag backup 10.10.10.4
		nv set mlag peer-ip linklocal
		```
	=== "leaf4"
		```bash linenums="1"
		nv set interface peerlink bond member swp10-11
		nv set mlag mac-address 44:38:39:BE:EF:AA
		nv set mlag backup 10.10.10.3
		nv set mlag peer-ip linklocal
		```
???+ example "VLANs"
	=== "leaf1"
		```bash linenums="1"
		nv set interface vlan10 ip address 10.1.10.2/24
		nv set interface vlan10 ip vrr address 10.1.10.1/24
		nv set interface vlan10 ip vrr state up
		nv set interface vlan20 ip address 10.1.20.2/24
		nv set interface vlan20 ip vrr address 10.1.20.1/24
		nv set interface vlan20 ip vrr state up
		nv set interface bond1 bridge domain br_default access 10
		nv set bridge domain br_default vlan 10,20
		nv set bridge domain br_default untagged 1
		```
	=== "leaf2"
		```bash linenums="1"
		nv set interface vlan10 ip address 10.1.10.3/24
		nv set interface vlan10 ip vrr address 10.1.10.1/24
		nv set interface vlan10 ip vrr state up
		nv set interface vlan20 ip address 10.1.20.3/24
		nv set interface vlan20 ip vrr address 10.1.20.1/24
		nv set interface vlan20 ip vrr state up
		nv set interface bond1 bridge domain br_default access 10
		nv set bridge domain br_default vlan 10,20
		nv set bridge domain br_default untagged 1
		```
	=== "leaf3"
		```bash linenums="1"
		nv set interface vlan30 ip address 10.1.30.2/24
		nv set interface vlan30 ip vrr address 10.1.30.1/24
		nv set interface vlan30 ip vrr state up
		nv set interface vlan40 ip address 10.1.40.2/24
		nv set interface vlan40 ip vrr address 10.1.40.1/24
		nv set interface vlan40 ip vrr state up
		nv set interface bond1 bridge domain br_default access 40
		nv set bridge domain br_default vlan 30,40
		nv set bridge domain br_default untagged 1
		```
	=== "leaf4"
		```bash linenums="1"
		nv set interface vlan30 ip address 10.1.30.3/24
		nv set interface vlan30 ip vrr address 10.1.30.1/24
		nv set interface vlan30 ip vrr state up
		nv set interface vlan40 ip address 10.1.40.3/24
		nv set interface vlan40 ip vrr address 10.1.40.1/24
		nv set interface vlan40 ip vrr state up
		nv set interface bond1 bridge domain br_default access 40
		nv set bridge domain br_default vlan 30,40
		nv set bridge domain br_default untagged 1
		```
???+ example "BGP"
	=== "leaf1"
		```bash linenums="1"
		nv set router bgp autonomous-system 65101
		nv set router bgp router-id 10.10.10.1
		nv set vrf default router bgp neighbor swp24 remote-as external
		nv set vrf default router bgp neighbor swp23 remote-as external
		nv set vrf default router bgp address-family ipv4-unicast network 10.10.10.1/32
		nv set vrf default router bgp address-family ipv4-unicast redistribute connected
		nv config apply
		```
	=== "leaf2"
		```bash linenums="1"
		nv set router bgp autonomous-system 65102
		nv set router bgp router-id 10.10.10.2
		nv set vrf default router bgp neighbor swp24 remote-as external
		nv set vrf default router bgp neighbor swp23 remote-as external
		nv set vrf default router bgp address-family ipv4-unicast network 10.10.10.2/32
		nv set vrf default router bgp address-family ipv4-unicast redistribute connected
		nv config apply
		```
	=== "leaf3"
		```bash linenums="1"
		nv set router bgp autonomous-system 65103
		nv set router bgp router-id 10.10.10.3
		nv set vrf default router bgp neighbor swp24 remote-as external
		nv set vrf default router bgp neighbor swp23 remote-as external
		nv set vrf default router bgp address-family ipv4-unicast network 10.10.10.3/32
		nv set vrf default router bgp address-family ipv4-unicast redistribute connected
		nv config apply
		```
	=== "leaf4"
		```bash linenums="1"
		nv set router bgp autonomous-system 65104
		nv set router bgp router-id 10.10.10.4
		nv set vrf default router bgp neighbor swp24 remote-as external
		nv set vrf default router bgp neighbor swp23 remote-as external
		nv set vrf default router bgp address-family ipv4-unicast network 10.10.10.4/32
		nv set vrf default router bgp address-family ipv4-unicast redistribute connected
		nv config apply
		```
	=== "spine1"
		```bash linenums="1"
		nv set router bgp autonomous-system 65199
		nv set router bgp router-id 10.10.10.101
		nv set vrf default router bgp neighbor swp1 remote-as external
		nv set vrf default router bgp neighbor swp2 remote-as external
		nv set vrf default router bgp neighbor swp3 remote-as external
		nv set vrf default router bgp neighbor swp4 remote-as external
		nv set vrf default router bgp address-family ipv4-unicast network 10.10.10.101/32
		nv config apply
		```
	=== "spine2"
		```bash linenums="1"
		nv set router bgp autonomous-system 65199
		nv set router bgp router-id 10.10.10.102
		nv set vrf default router bgp neighbor swp1 remote-as external
		nv set vrf default router bgp neighbor swp2 remote-as external
		nv set vrf default router bgp neighbor swp3 remote-as external
		nv set vrf default router bgp neighbor swp4 remote-as external
		nv set vrf default router bgp address-family ipv4-unicast network 10.10.10.102/32
		nv config apply
		```

???+ example "Servers"
	=== "srv1"
		```bash linenums="1"
		nmcli con del "System eth0"
		nmcli con del "Wired connection 1"
		nmcli con add type bond ifname bond1 con-name bond1 bond.options "mode=802.3ad"
		nmcli con add type ethernet ifname eth0 master bond1
		nmcli con add type ethernet ifname eth1 master bond1
		nmcli con modify bond1 ipv4.address 10.1.10.10/24	
		nmcli con modify bond1 ipv4.gateway 10.1.10.1
		nmcli con down bond1 && nmcli con up bond1
		```
	=== "srv2"
		```bash linenums="1"
		nmcli con del "System eth0"
		nmcli con del "Wired connection 1"
		nmcli con add type bond ifname bond1 con-name bond1 bond.options "mode=802.3ad"
		nmcli con add type ethernet ifname eth0 master bond1
		nmcli con add type ethernet ifname eth1 master bond1
		nmcli con modify bond1 ipv4.address 10.1.40.10/24	
		nmcli con modify bond1 ipv4.gateway 10.1.40.1
		nmcli con down bond1 && nmcli con up bond1
		```
	