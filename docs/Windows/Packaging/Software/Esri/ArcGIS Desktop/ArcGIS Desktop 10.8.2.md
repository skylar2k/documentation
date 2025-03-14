## Installation
- Arch: x86_64
## Dependencies
- Microsoft Visual C++ 2015-2019  x86 Redistributable
## Registry changes
???- info "HKLM\Software\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall"
	- `{791AB03F-1AF2-43FE-8F5D-8FDC9509D7CF}`
		- DisplayName: ArcGIS Desktop 10.8.2
		- DisplayVersion: 10.8.28388
	- `ArcGIS Desktop 10.8.2`
		- DisplayName: ArcGIS Desktop 10.8.2
		- DisplayVersion: 10.8.28388
		- UninstallString: `"C:\Program Files (x86)\Common Files\ArcGIS\Support\ESRI.exe" msiexec.exe /x {791AB03F-1AF2-43FE-8F5D-8FDC9509D7CF}`
???- info "HKLM\Software\WOW6432Node\ESRI\Desktop10.8"
	- `Settings`
		- EnableEUEI: 0
		- BlockAddIns: 0
	- `CoreRuntime`
		- InstallVersion: 10.8.28388
		- ProductName: ArcGIS Desktop 10.8.2
		- RealVersion: 10.8.2
???- info "HKLM\Software\WOW6432Node\ESRI\"
	- `Desktop10.8`
		- BuildNumber: 28388
		- ProductName: ArcGIS Desktop 10.8.2
		- RealVersion: 10.8.2
		- Version: 10.8.28388
		- ProductLanguage: 1033
## File paths
- `C:\Program Files (x86)\ArcGIS\Desktop10.8`
## Intune
### Detection Rules
#### Rule type: Registry
???- info "Key Path: `HKLM\Software\MRFK\Esri\ArcGIS Desktop`"
	- Value name: Version
	- Detection method: Version comparison
	- Operator: equal to
	- Value: `10.8.2`
## Tests
- [ ] Application installs on Autopilot VMs
- [ ] Application is detected in Intune
- [ ] Application uninstalls
- [ ] Application reinstalls on Autopilot VMs
- [ ] License activates
## Resources
- [[Installing ArcGIS Desktop silently—ArcMap  Documentation]]
- [[Uninstalling ArcGIS Desktop—ArcMap  Documentation]]