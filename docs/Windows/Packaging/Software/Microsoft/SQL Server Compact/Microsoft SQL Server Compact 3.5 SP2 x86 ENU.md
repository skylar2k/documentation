## Installation
- Arch: x86
- Silent install: msiexec /i SSCERuntime_x86-ENU.msi /qn /norestart
- Silent uninstall: msiexec /x "{3A9FC03D-C685-4831-94CF-4EDFD3749497}" /qn /norestart
## Registry changes
???- info "HKLM\Software\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall"
	- `{3A9FC03D-C685-4831-94CF-4EDFD3749497}`
		- DisplayName: Microsoft SQL Server Compact 3.5 SP2 ENU
		- DisplayVersion: 3.5.8080.0
		- UninstallString: `MsiExec.exe /I{3A9FC03D-C685-4831-94CF-4EDFD3749497}`
???- info "HKLM\Software\WOW6432Node\Microsoft\Microsoft SQL Server Compact Edition"
	- `v3.5`
		- Version: 3.5.8080.0
		- ServicePackLevel: 2
	- `v3.5\ENU`
		- DesktopRuntimeServicePackLevel: 2
		- DesktopRuntimeVersion: 3.5.8080.0
## File paths
- `C:\Program Files (x86)\Microsoft SQL Server Compact Edition\v3.5\ReadmeSSCE35_ENU.htm`
- `C:\Program Files (x86)\Microsoft Synchronization Services\ADO.NET\v1.0\ReadMeSyncServices_ENU.htm`
## Intune
### Detection Rules
#### Rule type: Registry
???- info "Key Path: `HKLM\Software\WOW6432Node\Microsoft\Microsoft SQL Server Compact Edition\v3.5`"
	- Value name: Version
	- Detection method: Version comparison
	- Operator: Greater than or equal to
	- Value: `3.5.8080.0`
???- info "Key Path: `HKLM\Software\WOW6432Node\Microsoft\Microsoft SQL Server Compact Edition\v3.5`"
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