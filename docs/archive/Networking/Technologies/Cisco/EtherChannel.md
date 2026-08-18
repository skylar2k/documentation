## What is it?
EtherChannel is a port link aggregation technology used primarily on Cisco switches. It allows grouping several physical Ethernet links to create one logical Ethernet link for the purpose of providing fault-tolerance and high-speed links between devices.

## Port Modes
EtherChannel can be configured manually or you can use protocols for link aggregation. Protocols that can be used with EtherChannel are PAgP and LACP. The port states that results in aggregations are listed below for both protocols:
### PAgP
| PAgP Channel Mode | ON | AUTO | DESIRABLE |
| ---- | ---- | ---- | ---- |
| ON | Yes | No | No |
| AUTO | No | No | Yes |
| DESIRABLE | No | Yes | Yes |

### LACP
| LACP Channel Mode | ON | PASSIVE | ACTIVE |
| ---- | ---- | ---- | ---- |
| ON | Yes | No | No |
| PASSIVE | No | No | Yes |
| ACTIVE | No | Yes | Yes |


