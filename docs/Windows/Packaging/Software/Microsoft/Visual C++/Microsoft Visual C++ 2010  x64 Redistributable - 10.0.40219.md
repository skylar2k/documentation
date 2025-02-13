## Installation
- Arch: x64
- KBs are also listed in the registry
- Silent install: `vcredist_x64.exe /lcid 1033 /norestart /q`
- Silent uninstall: `vcredist_x64.exe /lcid 1033 /norestart /q /uninstall`
## Registry changes
???- info "HKLM\Software\Microsoft\Windows\CurrentVersion\Uninstall"
	- `{1D8E6291-B0D5-35EC-8441-6616F567A0F7}`
		- DisplayName: Microsoft Visual C++ 2010  x64 Redistributable - 10.0.40219
		- DisplayVersion: 10.0.40219
		- UninstallString: `MsiExec.exe /X{1D8E6291-B0D5-35EC-8441-6616F567A0F7}`
???- info "HKLM\Software\WOW6432Node\Microsoft\DevDiv\vc\Servicing\10.0\red\amd64"
	- `1033`
		- SP: 1
		- SPIndex: 0
		- Version: 40219.325
		- Bld: 40219
???- info "HKLM\Software\WOW6432Node\Microsoft\VisualStudio\10.0\VC\VCRedist"
	- `x64`
		- Rbld: 325
		- Installed: 1
		- Version: v10.0.40219.325
		- MinorVersion: 0
		- MajorVersion: 10
		- Bld: 40219
		- Present: 1
## File paths
- `c:\Program Files\Common Files\Microsoft Shared\VC\msdia100.dll`
## Intune
### Detection Rules
#### Rule type: Registry
???- info "Key Path: `HKLM\Software\WOW6432Node\Microsoft\VisualStudio\10.0\VC\VCRedist\x64`"
	- Value name: Bld
	- Detection method: Integer comparison
	- Operator: Greater than or equal to
	- Value: `40219`
## Tests
- [x] Application installs on Autopilot VMs
- [x] Application is detected in Intune
- [x] Application reinstalls on Autopilot VMs
- [ ] License activates