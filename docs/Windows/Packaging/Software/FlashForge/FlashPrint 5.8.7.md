## Installation
- Arch: x64
- All of the contents in the exe can be extracted using the `extract` parameter, this allows us to manually install drivers. Because this program install sucks ass and will prompt to install drivers even though they are installed, we will manually install it tar.gz style.
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
## Tests
- [ ] Application installs on Autopilot VMs
- [ ] Application uninstalls from Autopilot VMs
- [ ] Application reinstalls on Autopilot VMs