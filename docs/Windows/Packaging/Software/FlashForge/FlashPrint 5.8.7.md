## Installation
- Arch: x64
- All of the contents in the exe can be extracted using the `extract` parameter, this allows us to manually install drivers. Because this program install sucks ass and will prompt to install drivers even though they are installed, we will manually install it tar.gz style.
- In the PSADT script I create my own registry key for installed version
## Registry changes
???- info "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\"
	- `{5690AC53-CA8D-4365-8AAD-12FA23957B43}`
		- DisplayName: FlashPrint 5
		- DisplayVersion: 5.8.7
		- InstallLocation: `C:\Program Files\FlashForge\FlashPrint 5
		- Language: `0x00000409` (1033)
		- ModifyPath: `MsiExec.exe /X{5690AC53-CA8D-4365-8AAD-12FA23957B43}`
		- UninstallString: `MsiExec.exe /X{5690AC53-CA8D-4365-8AAD-12FA23957B43}`
		- Version: `0x05080007` (84410375)
		- VersionMajor: `0x00000005`
		- VersionMinor: `0x00000008`
## Intune
### Detection Rules
#### Rule type: Registry
???- info "Key path: `HKLM\Software\MRFK\FlashForge\FlashPrint 5`"
	- Value name: version
	- Detection method: Version comparison
	- Operator: Greater than or equal to
	- Value: `5.8.7`
## Tests
- [ ] Application installs on Autopilot VMs
- [ ] Application uninstalls from Autopilot VMs
- [ ] Application reinstalls on Autopilot VMs