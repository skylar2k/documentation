- Purpose:
	- Firewall
	- Router
- Services:
	- pf
	- dhcpd
	- sshd
	- ldapd
- OS: OpenBSD 7.6
## Config
### Allow 'sky' to use doas
???+ example "/etc/doas.conf"
	```bash linenums="1"
	permit persist sky as root
	```
### LDAPD
