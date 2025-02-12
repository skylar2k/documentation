## Installation
- Arch: x86-x64

## Registry changes
???- info "HKLM\SOFTWARE\Microsoft\NET Framework Setup\NDP\v4\Full"
	- Release: Greater than or equal to 533320

## Intune
### Detection Rules
#### Rule type: Registry
???- info "Key path: `HKLM\SOFTWARE\Microsoft\NET Framework Setup\NDP\v4\Full`"
	- Value name: Release
	- Detection method: Integer comparison
	- Operator Greater than or equal to
	- Value: `533320`
## Tests
- [X] Application installs on Autopilot VMs
- [x] Application is detected in Intune