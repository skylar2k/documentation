## Installation
- Arch: x86_64
## Registry changes
???- info "HKLM\SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall"
	- `DSMT7`
		- DisplayName: MathType 7
		- DisplayVersion: 7.8.0
		- UninstallString: `"C:\Program Files (x86)\MathType\Setup.exe" -R`
## Intune
### Detection Rules
#### Rule type: Registry
???- info "Key path: `HKLM\SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall\DSMT7`"
	- Value name: DisplayVersion
	- Detection method: Version comparison
	- Operator: Equals
	- Value: `7.8.0`
## Tests
- [x] Application installs on Autopilot VMs
- [x] License activates
- [x] Application uninstalls from Autopilot VMs
- [x] Application reinstalls on Autopilot VMs