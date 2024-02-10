## What is it?
A routing table, also known as routing information base (RIB), is a data table stored in a router or network host that lists the routes to distinct network destinations. The routing table contains information about the immediately surrounding network topology.

[[Networking/Technologies/Routing protocols/index|Routing protocols]] are responsible for the construction of the routing table. Static routes are entries that are fixed, rather than discovered by routing protocols.

## Contents
A routing table consists of at least three information fields:

1. *network identifier*: The destination subnet and netmask
2. *metric*: The routing metric of the path through which the packet is to be sent. The route will go in the direction of the gateway with the lowest metric.
3. *next hop*: The next hop, or gateway, is the address of the next station to which the packet is to be sent on the way to its final destination.

Certain applications and implementations can also contain additional values for path selection:

1. *quality of service* associated with the route. For example, the U flag indicates that an IP route is up.
2. *filtering criteria*: ACLs associated with the route
3. *interface*: Such as eth0 for the first Ethernet card.

Example routing table:
![[Pasted image 20240210121907.png]]