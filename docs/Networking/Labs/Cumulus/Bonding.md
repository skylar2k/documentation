## Introduction
This lab uses Linux bonding to aggregate multiple network interfaces (slaves) into a single logical bonded interface (bond). This is useful for linear scaling of bandwidth, load balancing, and fail over protection.

Cumulus Linux supports these bonding modes:

- IEEE 802.3ad link aggregation mode combines one or more links to form a LAG so that a MAC client can treat the group as a single link. IEEE 802.3ad link aggregation is the default mode
- Balance-xor mode balances outgoing traffic across active ports according to the hashed protocol header information and accepts incoming traffic from any port. All slave interfaces are active for load balancing and fault tolerance. This is useful for MLAG deployments.

## Topology
## Configuration