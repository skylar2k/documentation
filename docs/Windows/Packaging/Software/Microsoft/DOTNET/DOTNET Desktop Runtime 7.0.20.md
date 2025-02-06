## Installation
- Arch: x64

## Registry changes
???- info "HKLM\SOFTWARE\dotnet\Setup\InstalledVersions\x64"
	- `sharedhost`
		- Version: Equal to 7.0.20
		- Path: `C:\Program Files\dotnet\`
???- info "HKLM\Software\Microsoft\Windows\CurrentVersion\Uninstall"
	- `{221BB52A-B763-4C9D-AA62-4B0B6C9AAD62}`
		- DisplayName: Microsoft .NET Runtime - 7.0.20 (x64)
		- Version: 944782160
		- UninstallString: `MsiExec.exe /X{221BB52A-B763-4C9D-AA62-4B0B6C9AAD62}`
		- DisplayVersion: `56.80.15184`
	- `{72C29BED-666F-4E5E-BC49-DF44C890742E}`
		- DisplayName: Microsoft Windows Desktop Runtime - 7.0.20 (x64)
		- Version: 944782221
		- UninstallString: `MsiExec.exe /X{72C29BED-666F-4E5E-BC49-DF44C890742E}`
		- DisplayVersion: 56.80.15245

## File paths
- `C:\Program Files\dotnet\shared\Microsoft.WindowsDesktop.App\7.0.20`
- `C:\Program Files\dotnet\shared\Microsoft.NETCore.App\7.0.20`

## Intune
### Detection Rules
#### Rule type: File
???- info "Path: `C:\Program Files\dotnet\shared\Microsoft.WindowsDesktop.App`"
	- File or Folder: 7.0.20
	- Detection method: File or folder exists
## Tests
 - [X] Application installs on Autopilot VMs
 - [x] Application is detected in Intune