## Installation
- Arch: x64
- Silent install: msiexec /i SSCERuntime_x64-ENU.msi /qn /norestart
- Silent uninstall: msiexec /x "{D4AD39AD-091E-4D33-BB2B-59F6FCB8ADC3}" /qn /norestart
## Dependencies
- [[Microsoft SQL Server Compact 3.5 SP2 x86 ENU]]
## Registry changes
???- info "HKLM\Software\Microsoft\Windows\CurrentVersion\Uninstall"
	- `{D4AD39AD-091E-4D33-BB2B-59F6FCB8ADC3}`
		- DisplayName: Microsoft SQL Server Compact 3.5 SP2 x64 ENU
		- DisplayVersion: 3.5.8080.0
		- UninstallString: `MsiExec.exe /I{D4AD39AD-091E-4D33-BB2B-59F6FCB8ADC3}`
???- info "HKLM\Software\Microsoft\Microsoft SQL Server Compact Edition"
	- `v3.5`
		- Version: 3.5.8080.0
		- ServicePackLevel: 2
	- `v3.5\ENU`
		- DesktopRuntimeServicePackLevel: 2
		- DesktopRuntimeVersion: 3.5.8080.0
## File paths
- `C:\Program Files\Microsoft SQL Server Compact Edition\v3.5\ReadmeSSCE35_ENU.htm`
- `C:\Program Files\Microsoft Synchronization Services\ADO.NET\v1.0\ReadMeSyncServices_ENU.htm`
## Intune
### Detection Rules
#### Rule type: Registry
???- info "Key Path: `HKLM\Software\Microsoft\Microsoft SQL Server Compact Edition\v3.5`"
	- Value name: Version
	- Detection method: Version comparison
	- Operator: Greater than or equal to
	- Value: `3.5.8080.0`
???- info "Key Path: `HKLM\Software\Microsoft\Microsoft SQL Server Compact Edition\v3.5`"
	- Value name: ServicePackLevel
	- Detection method: Integer comparison
	- Operator: Greater than or equal to
	- Value: `2`
## Tests
- [x] Application installs on Autopilot VMs
- [x] Application is detected in Intune
- [x] Application uninstalls
- [x] Application reinstalls on Autopilot VMs
- [ ] License activates