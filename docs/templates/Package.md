## Installation
- Arch:
- Silent install:
- Silent uninstall
## Registry changes
???- info "HKLM\"
	- ``
		- DisplayName: 
		- DisplayVersion: 
		- UninstallString: ``
## File paths
- ``
???- info "Shared DLLs"
- ``
## Intune
### Detection Rules
#### Rule type: Registry
???- info "Key Path: ``"
	- Value name: Version
	- Detection method: Version comparison
	- Operator: Greater than or equal to
	- Value: ``
## Tests
- [ ] Application installs on Autopilot VMs
- [ ] Application is detected in Intune
- [ ] Application uninstalls
- [ ] Application reinstalls on Autopilot VMs
- [ ] License activates