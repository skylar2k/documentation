## Installation
- Arch: x64
- Silent install: vcredist_x64.exe /lang 1033 /q
- Silent uninstall: vcredist_x64.exe /lang 1033 /qu
## Registry changes
???- info "HKLM\Software\Microsoft\Windows\CurrentVersion\Uninstall"
	- `{5FCE6D76-F5DC-37AB-B2B8-22AB8CEDB1D4}`
		- DisplayName: Microsoft Visual C++ 2008 Redistributable - x64 9.0.30729.6161
		- DisplayVersion: 9.0.30729.6161
		- UninstallString: `MsiExec.exe /X{5FCE6D76-F5DC-37AB-B2B8-22AB8CEDB1D4}`
		- Language: 1033
???- info "HKLM\Software\Microsoft\DevDiv\VC\Servicing\9.0\RED"
	- `1033`
		- Install: 1
		- Version: 30729.6161
		- InstallerType MSI
		- SP: 1
		- SPIndex: 1
		- SPName: SP1
## File paths
- `c:\Program Files\Common Files\Microsoft Shared\VC\msdia90.dll`
## Intune
### Detection Rules
#### Rule type: Registry
???- info "Key Path: `HKLM\Software\Microsoft\DevDiv\VC\Servicing\9.0\RED\1033`"
	- Value name: Version
	- Detection method: Version comparison
	- Operator: Greater than or equal to
	- Value: `30729.6161`
## Tests
- [X] Application installs on Autopilot VMs
- [x] Application is detected in Intune