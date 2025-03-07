## Installation
- Arch: x86_64
- Silent install: windowsdesktop-runtime-8.0.13-win-x64.exe /install /quiet /norestart
- Silent uninstall: windowsdesktop-runtime-8.0.13-win-x64.exe /uninstall /quiet /norestart
## Registry changes
???- info "HKLM\Software\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall"
	- `{e882eb81-b18c-4676-88f0-9a6ea9db6090}`
		- DisplayName: Microsoft Windows Desktop Runtime - 8.0.13 (x64)
		- DisplayVersion: 8.0.13.34517
		- UninstallString: `"C:\ProgramData\Package Cache\{e882eb81-b18c-4676-88f0-9a6ea9db6090}\windowsdesktop-runtime-8.0.13-win-x64.exe"  /uninstall`
		- QuietUninstallString: `"C:\ProgramData\Package Cache\{e882eb81-b18c-4676-88f0-9a6ea9db6090}\windowsdesktop-runtime-8.0.13-win-x64.exe" /uninstall /quiet`
???- info "HKLM\Software\WOW6432Node\dotnet\Setup\InstalledVersions\x64\sharedfx"
	- `Microsoft.NETCore.App`
		- 8.0.13: 1
	- `Microsoft.WindowsDesktop.App`
		- 8.0.13: 1
???- info "HKLM\Software\WOW6432Node\dotnet\Setup\InstalledVersions"
	- `hostfxr`
		- Version: 8.0.13
???- info "HKLM\Software\dotnet\Setup\InstalledVersions\x64"
	- `sharedhost`
		- Version 8.0.13
		- Path: `C:\Program Files\dotnet`
## File paths
- `C:\Program Files\dotnet\shared\Microsoft.WindowsDesktop.App\8.0.13`
- `C:\Program Files\dotnet\shared\Microsoft.NETCore.App\8.0.13`
## Intune
### Detection Rules
#### Rule type: Detection script
```powershell title="Custom detection script"
[string]$RegistryPath = "HKLM:\SOFTWARE\WOW6432Node\dotnet\Setup\InstalledVersions\x64\sharedfx"
[version]$MinVer = '8.0.13'
[array]$runtimes = $null

if (Test-Path -Path $RegistryPath -PathType Container) {
    $runtimes = Get-ChildItem -Path "$RegistryPath" |
    Where-Object PSChildName -eq "Microsoft.WindowsDesktop.App" |
    Select-Object -ExpandProperty Property |
    Where-Object { ($_ -like "8.0.*") -and ($_ -ge $MinVer) }
}
if ($null -eq $runtimes) {
    Write-Output "Minimum version: $MinVer for Windows Desktop Runtime not detected"
    exit 1
}
Write-Output "Minimum version: $MinVer for Windows Desktop Runtime detected"
exit 0
```
## Tests
- [ ] Application installs on Autopilot VMs
- [ ] Application is detected in Intune
- [ ] Application uninstalls
- [ ] Application reinstalls on Autopilot VMs
- [ ] License activates