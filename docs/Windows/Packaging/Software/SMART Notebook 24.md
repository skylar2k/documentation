## Installation
- Arch: x86
- Dependencies
	- [[DOTNET Runtime 4.8.1]]
	- Microsoft Visual Studio 2010 Tools for Office Runtime
## Registry changes
???- info "HKLM\SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall"
	- `{2FA63536-1209-4B62-A043-E0E4B5DF5254}`
		- DisplayName: SMART Notebook
		- DisplayVersion: 24.0.1733.0
		- InstallLocation: `C:\Program Files (x86)\SMART Technologies\Education Software\`
		- UninstallString: `MsiExec.exe /X{2FA63536-1209-4B62-A043-E0E4B5DF5254}`
	- `{87257486-5AF1-476C-99F4-C41F90251EEF}`
		- DisplayName: SMART Lesson Activity Toolkit
		- DisplayVersion: 2.0.12.0
		- UninstallString: `MsiExec.exe /X{87257486-5AF1-476C-99F4-C41F90251EEF}`
	- `{34A051B4-86CC-4409-94D6-B149E9F36404}`
		- DisplayName: SMART Education Software
		- DisplayVersion: 24.0.306.0
		- InstallLocation: `C:\Program Files (x86)\SMART Technologies\`
		- UninstallString: `MsiExec.exe /X{34A051B4-86CC-4409-94D6-B149E9F36404}`
	- `{84FE50F5-B0F3-4D18-8BE8-A4DEEE0C37AD}`
		- DisplayName: TechSmith Screen Capture Codec
		- DisplayVersion: 4.1.1.0
		- UninstallString: `MsiExec.exe /X{84FE50F5-B0F3-4D18-8BE8-A4DEEE0C37AD}`
	- `{AE4A8476-F602-4FC0-A40D-336DC76DD7EE}`
		- DisplayName: SMART Norwegian Handwriting Resources
		- DisplayVersion: 15.1.10.0
		- InstallLocation: `C:\Program Files (x86)\SMART Technologies\Education Software\`
		- UninstallString: `MsiExec.exe /X{AE4A8476-F602-4FC0-A40D-336DC76DD7EE}`
	- `{B5D5D9DC-3361-43D7-ADED-916CC6E90A03}`
		- DisplayName: SMART English (United Kingdom) Handwriting Resources
		- DisplayVersion: 15.1.10.0
		- InstallLocation: `C:\Program Files (x86)\SMART Technologies\Education Software\`
		- UninstallString: `MsiExec.exe /X{B5D5D9DC-3361-43D7-ADED-916CC6E90A03}`
	- `{BFC4DA50-D610-4BFE-92ED-CCBE6D9D3273}`
		- DisplayName: SMART Gallery Essentials
		- DisplayVersion: 2.0.7.0
		- UninstallString: `MsiExec.exe /X{BFC4DA50-D610-4BFE-92ED-CCBE6D9D3273}`
	- `{CE22E589-A241-4B0C-B99D-E08D660EC32F}`
		- DisplayName: SMART Product Drivers
		- DisplayVersion: 12.23.200.0
		- InstallLocation: `C:\Program Files (x86)\SMART Technologies\SMART Product Drivers\`
		- UninstallString: `MsiExec.exe /X{CE22E589-A241-4B0C-B99D-E08D660EC32F}`
	- `{D0FFBAE6-0470-4EEB-A098-3C04063A6A31}`
		- DisplayName: SMART Ink
		- DisplayVersion: 5.17.3.0
		- InstallLocation: `C:\Program Files (x86)\SMART Technologies\SMART Product Drivers\`
		- UninstallString: `MsiExec.exe /X{D0FFBAE6-0470-4EEB-A098-3C04063A6A31}`
## Intune
### Detection Rules
#### Rule type: Registry
???- info "Key path: `HKLM\SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall\{34A051B4-86CC-4409-94D6-B149E9F36404}`"
	- Value name: DisplayVersion
	- Detection method: Version comparison
	- Operator: Equals
	- Value: `24.0.306.0`
## Tests
- [x] Application installs on Autopilot VMs
- [x] Application uninstalls from Autopilot VMs
- [x] Application reinstalls on Autopilot VMs