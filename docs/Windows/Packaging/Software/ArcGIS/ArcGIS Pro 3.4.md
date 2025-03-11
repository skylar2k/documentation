## Installation
- Arch: x86_64
## Dependencies 
- [[Microsoft Windows Desktop Runtime - 8.0.13 (x64)]]
## Registry changes
???- info "HKLM\Software\Microsoft\Windows\CurrentVersion\Uninstall"
	- `ArcGISPro`
		- DisplayName:  ArcGIS Pro
		- DisplayVersion: 3.4.55405
		- UninstallString: `msiexec.exe /x {F6FDD729-EC3F-4361-A98E-B592EEF0D445}`
	- `{F6FDD729-EC3F-4361-A98E-B592EEF0D445}`
		- DisplayName: ArcGIS Pro
		- DisplayVersion: 3.4.55405
		- UninstallString: `MsiExec.exe /I{F6FDD729-EC3F-4361-A98E-B592EEF0D445}`
???- info "HKLM\Software\ESRI"
	- `ArcGISPro`
		- LPVersion: 3.4
		- ProductCode:  `{F6FDD729-EC3F-4361-A98E-B592EEF0D445}`
		- ProductName: ArcGIS Pro
		- ProductLangauge: 1033
		- Version: 3.4.0.55405
		- RealVersion: 3.4.0
	- `ArcGISPro\Licensing`
		- SOFTWARE_CLASS_FN: ``
		- LICENSE_SERVER: @Not_Set
		- LOCK_AUTH_SETTINGS: ``
		- AUTHORIZATION_TYPE: ``
		- SOFTWARET_TYPE: ``
		- ARCPRO_AUTH_TYPE: ``
	- `ArcGISPro\Settings`
		- EnableEUEI: 0
		- CheckForUpdatesAtStartup: 0
		- BlockAddins: 0
## File paths
- `C:\Program Files\ArcGIS\Pro`
## Intune
### Detection Rules
#### Rule type: Registry
???- info "Key Path: `HKLM\Software\ESRI\ArcGISPro`"
	- Value name: RealVersion
	- Detection method: Version comparison
	- Operator: Equal to
	- Value: `3.4.0`
## Tests
- [ ] Application installs on Autopilot VMs
- [ ] Application is detected in Intune
- [ ] Application uninstalls
- [ ] Application reinstalls on Autopilot VMs
- [ ] License activates