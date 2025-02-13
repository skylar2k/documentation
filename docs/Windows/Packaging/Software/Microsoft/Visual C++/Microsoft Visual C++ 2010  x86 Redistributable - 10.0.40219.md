## Installation
- Arch: x86
- KBs are also listed in registry
- Silent install: `vcredist_x86.exe /lcid 1033 /norestart /q`
- Silent uninstall: `vcredist_x86.exe /lcid 1033 /norestart /q /uninstall`
## Registry changes
???- info "HKLM\Software\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall"
	- `{F0C3E5D1-1ADE-321E-8167-68EF0DE699A5}`
		- DisplayName: Microsoft Visual C++ 2010  x86 Redistributable - 10.0.40219
		- DisplayVersion: 10.0.40219
		- UninstallString: `MsiExec.exe /X{F0C3E5D1-1ADE-321E-8167-68EF0DE699A5}`
???- info "HKLM\Software\WOW6432Node\Microsoft\DevDiv\vc\Servicing\10.0\red\x86"
	- `1033`
		- Install: 1
		- InstallerType: MSI
		- SP: 1
		- SPIndex: 0
		- Version: 40219.325
		- Bld: 40219
		- Rbld: 325
???- info "HKLM\Software\WOW6432Node\Microsoft\VisualStudio\10.0\VC\VCRedist"
	- `x86`
		- Version: v10.0.40219.325
		- Installed: 1
		- MajorVersion: 10
		- MinorVersion: 0
		- Bld: 40219
		- Rbld: 325
		- Present: 1
## File paths
- `c:\Program Files (x86)\Common Files\Microsoft Shared\VC\msdia100.dll`
## Intune
### Detection Rules
#### Rule type: Registry
???- info "Key Path: `HKLM\Software\WOW6432Node\Microsoft\VisualStudio\10.0\VC\VCRedist\x86`"
	- Value name: Bld
	- Detection method: Integer comparison
	- Operator: Greater than or equal to
	- Value: `40219`
## Tests
- [x] Application installs on Autopilot VMs
- [x] Application is detected in Intune
- [x] Application reinstalls on Autopilot VMs
- [ ] License activates