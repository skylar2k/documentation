Virtual routing and forwarding.
## What is it?
VRF is a technology that enables IP routers to contain multiple instances of a [[routing table]] at the same time. One or more physical or logical interfaces may have a VRF and these VRFs do not share routes. This means that packets are only forwarded between interfaces on the same VRF. VRFs are essentially the L3 equivalent to VLANs. Since routing instances are independent, the same or overlapping IP addresses can be used without conflict. This improves the network functionality since network paths can be segmented without needing multiple routers. 
## Resources
- [rdomain(4) - OpenBSD manual pages](https://man.openbsd.org/rdomain.4)
- [Virtual Routing and Forwarding (VRF) — The Linux Kernel documentation](https://docs.kernel.org/networking/vrf.html)