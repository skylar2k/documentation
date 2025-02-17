## Installation
- Arch: x64
- Silent install: windowsdesktop-runtime-6.0.36-win-x64.exe /install /quiet /norestart
- Silent uninstall: windowsdesktop-runtime-6.0.36-win-x64.exe /uninstall /quiet /norestart
## Registry changes
???- info "HKLM\Software\Microsoft\Windows\CurrentVersion\Uninstall"
	- `{61D4736B-3325-4D4A-BD41-8BD206C6A86E}`
		- DisplayName: Microsoft Windows Desktop Runtime - 6.0.36 (x64)
		- DisplayVersion: 48.144.23186
		- UninstallString: `MsiExec.exe /X{61D4736B-3325-4D4A-BD41-8BD206C6A86E}`
	- `{A9E32B25-994B-4856-A12B-0EBED3050410}`
		- DisplayName: Microsoft .NET Host FX Resolver - 6.0.36 (x64)
		- DisplayVersion: 48.144.23141
		- UninstallString: `MsiExec.exe /X{A9E32B25-994B-4856-A12B-0EBED3050410}`
	- `{C912E33F-956A-4921-9F55-CC11AE8F09AF}`
		- DisplayName: Microsoft .NET Runtime - 6.0.36 (x64)
		- DisplayVersion: 48.144.23141
		- UninstallString: `MsiExec.exe /X{C912E33F-956A-4921-9F55-CC11AE8F09AF}`
	- `{D6932D97-36F1-40B8-9CDC-CA8365B21000}`
		- DisplayName: Microsoft .NET Host - 6.0.36 (x64)
		- DisplayVersion: 48.144.23141
		- UninstallString: `MsiExec.exe /X{D6932D97-36F1-40B8-9CDC-CA8365B21000}`
???- info "HKLM\Software\dotnet\Setup\InstalledVersions\x64"
	- `sharedhost`
		- Version: 6.0.36
		- Path: `C:\Program Files\dotnet\`
???- info "HKLM\Software\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall"
	- `{0532b8f2-12d7-43de-95fc-7b87006758a8}`
		- DisplayName: Microsoft Windows Desktop Runtime - 6.0.36 (x64)
		- DisplayVersion: 6.0.36.34217
		- UninstallString: `"C:\ProgramData\Package Cache\{0532b8f2-12d7-43de-95fc-7b87006758a8}\windowsdesktop-runtime-6.0.36-win-x64.exe"  /uninstall`
		- QuietUninstallString: `"C:\ProgramData\Package Cache\{0532b8f2-12d7-43de-95fc-7b87006758a8}\windowsdesktop-runtime-6.0.36-win-x64.exe" /uninstall /quiet`
???- info "HKLM\Software\WOW6432Node\dotnet\Setup\InstalledVersions\x64\sharedfx"
	- `Microsoft.NETCore.App`
		- 6.0.36: 1
	- `Microsoft.WindowsDesktop.App`
		- 6.0.36: 1
## File paths
- `C:\Program Files\dotnet\shared\Microsoft.NETCore.App\6.0.36\`
- `C:\Program Files\dotnet\shared\Microsoft.WindowsDesktop.App\6.0.36\`
## Intune
### Detection Rules
#### Rule type: Detection script
```powershell title="Custom detection script"
[string]$RegistryPath = "HKLM:\SOFTWARE\WOW6432Node\dotnet\Setup\InstalledVersions\x64\sharedfx"
[version]$MinVer = '6.0.36'
[array]$runtimes = $null

if (Test-Path -Path $RegistryPath -PathType Container) {
	[array]$runtimes = Get-ChildItem -Path "$RegistryPath" |
	Where-Object PSChildName -eq "Microsoft.WindowsDesktop.App" |
	Select-Object -ExpandProperty Property |
	Where-Object { ($_ -like "6.0.*") -and ($_ -ge $MinVer) }
}
if ($null -eq $runtimes) {
	Write-Error "Application not installed, minimum version not met."
	exit 1
}
Write-Output "Application detected, minimum version is met."
```
## Tests
- [ ] Application installs on Autopilot VMs
- [ ] Application is detected in Intune
- [ ] Application reinstalls on Autopilot VMs
- [ ] License activates