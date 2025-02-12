## Installation
- Arch: x86
- Silent install: vcredist_x86.exe /lang 1033 /q
- Silent uninstall: vcredist_x86.exe /lang 1033 /qu
## Registry changes
???- info "HKLM\Software\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall\"
	- `{9BE518E6-ECC6-35A9-88E4-87755C07200F}`
		- DisplayName: Microsoft Visual C++ 2008 Redistributable - x86 9.0.30729.6161
		- DisplayVersion: 9.0.30729.6161
		- UninstallString: `MsiExec.exe /X{9BE518E6-ECC6-35A9-88E4-87755C07200F}`
		- Language: 1033
???- info "HKLM\Software\WOW6432Node\Microsoft\DevDiv\VC\Servicing\9.0\RED\"
	- `1033`
		- Install: 1
		- Version: 30729.6161
		- InstallerType MSI
		- SP: 1
		- SPIndex: 1
		- SPName: SP1
## File paths
- `c:\Program Files (x86)\Common Files\Microsoft Shared\VC\msdia90.dll`
## Intune
### Detection Rules
#### Rule type: Registry
???- info "Key Path: `HKLM\Software\WOW6432Node\Microsoft\DevDiv\VC\Servicing\9.0\RED\1033`"
	- Value name: Version
	- Detection method: Version comparison
	- Operator: Greater than or equal to
	- Value: `30729.6161`
## Tests
- [X] Application installs on Autopilot VMs
- [x] Application is detected in Intune