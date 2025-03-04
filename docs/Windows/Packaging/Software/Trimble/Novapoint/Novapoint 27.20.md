## Installation
- Arch: x86_64
- Silent install: Novapoint 2025 (ac25).msi /qn
- Silent uninstall:
## Dependencies
- [[Microsoft Windows Desktop Runtime - 7.0.20 (x64)]]
- [[Microsoft Visual C++ 2008 Redistributable - x64 9.0.30729.6161]]
- [[Microsoft Visual C++ 2008 Redistributable - x86 9.0.30729.6161]]
- [[Microsoft Visual C++ 2010  x64 Redistributable - 10.0.40219]]
- [[Microsoft Visual C++ 2010  x86 Redistributable - 10.0.40219]]
- Microsoft Visual C++ 2022 Redistributable Package
- [[Microsoft SQL Server Compact 3.5 SP2 x86 ENU]]
- [[Microsoft SQL Server Compact 3.5 SP2 x64 ENU]]
## Registry changes
???- info "HKLM\Software\Microsoft\Windows\CurrentVersion\Uninstall"
	- `{9127EA02-16C5-4273-988D-520981CDBF6D}`
		- DisplayName: Novapoint 2025 (ac25)
		- DisplayVersion: 27.20.0001
		- UninstallString: `MsiExec.exe /X{9127EA02-16C5-4273-988D-520981CDBF6D}`
## Intune
### Detection Rules
#### Rule type: Registry
???- info "Key path: `HKLM\Software\Microsoft\Windows\CurrentVersion\Uninstall\{9127EA02-16C5-4273-988D-520981CDBF6D}`"
	- Value name: DisplayVersion
	- Detection method: Version comparison
	- Operator: Greater than or equal to
	- Value: `27.20.0001`
## Tests
- [ ] Application installs on Autopilot VMs
- [ ] License activates
- [ ] Application uninstalls from Autopilot VMs
- [ ] Application reinstalls on Autopilot VMs