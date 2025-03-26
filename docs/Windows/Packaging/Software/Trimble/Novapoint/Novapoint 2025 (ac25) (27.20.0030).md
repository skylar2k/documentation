## Installation
- Arch: x86_64
## Registry changes
???- info "HKLM\Software\Microsoft\Windows\CurrentVersion\Uninstall"
	- `{20BD8A00-F4C1-4FE7-A48F-FDB58E0EAC8F}`
		- DisplayName: Novapoint 2025 (ac25)
		- DisplayVersion: 27.20.0030
		- UninstallString: `MsiExec.exe /X{20BD8A00-F4C1-4FE7-A48F-FDB58E0EAC8F}`
## Intune
### Detection Rules
#### Rule type: Registry
???- info "Key Path: `HKLM\Software\Microsoft\Windows\CurrentVersion\Uninstall\{20BD8A00-F4C1-4FE7-A48F-FDB58E0EAC8F}`"
	- Value name: DisplayVersion
	- Detection method: Version comparison
	- Operator: Equals
	- Value: `27.20.0030`
## Tests
- [ ] Application installs on Autopilot VMs
- [ ] Application is detected in Intune
- [ ] Application uninstalls
- [ ] Application reinstalls on Autopilot VMs
- [ ] License activates