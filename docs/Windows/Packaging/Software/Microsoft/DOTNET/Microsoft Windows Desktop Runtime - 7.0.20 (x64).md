## Installation
- Arch: x64

## Registry changes
???- info "HKLM\SOFTWARE\dotnet\Setup\InstalledVersions\x64"
	- `sharedhost`
		- Version: 7.0.20
		- Path: `C:\Program Files\dotnet\`
???- info "HKLM\Software\Microsoft\Windows\CurrentVersion\Uninstall"
	- `{221BB52A-B763-4C9D-AA62-4B0B6C9AAD62}`
		- DisplayName: Microsoft .NET Runtime - 7.0.20 (x64)
		- Version: 944782160
		- UninstallString: `MsiExec.exe /X{221BB52A-B763-4C9D-AA62-4B0B6C9AAD62}`
		- DisplayVersion: 56.80.15184
	- `{72C29BED-666F-4E5E-BC49-DF44C890742E}`
		- DisplayName: Microsoft Windows Desktop Runtime - 7.0.20 (x64)
		- Version: 944782221
		- UninstallString: `MsiExec.exe /X{72C29BED-666F-4E5E-BC49-DF44C890742E}`
		- DisplayVersion: 56.80.15245
???- info "HKLM\Software\WOW6432Node\dotnet\Setup\InstalledVersions\x64\sharedfx"
	- `Microsoft.NETCore.App`
		- 7.0.20: 1
	- `Microsoft.WindowsDesktop.App`
		- 7.0.20: 1

## File paths
- `C:\Program Files\dotnet\shared\Microsoft.WindowsDesktop.App\7.0.20`
- `C:\Program Files\dotnet\shared\Microsoft.NETCore.App\7.0.20`

## Intune
### Detection Rules
#### Rule type: Detection script
```powershell title="Custom detection script"
[string]$RegistryPath = "HKLM:\SOFTWARE\WOW6432Node\dotnet\Setup\InstalledVersions\x64\sharedfx"
[version]$MinVer = '7.0.20'
[array]$runtimes = $null

if (Test-Path -Path $RegistryPath -PathType Container) {
    [array]$runtimes = Get-ChildItem -Path "$RegistryPath" |
    Where-Object PSChildName -eq "Microsoft.WindowsDesktop.App" |
    Select-Object -ExpandProperty Property |
    Where-Object { ($_ -like "7.0.*") -and ($_ -ge $MinVer) }
}
if ($null -eq $runtimes) {
    Write-Error "Application not installed, minimum version not met."
    exit 1

}
Write-Output "Application detected, minimum version is met."
```
## Tests
- [X] Application installs on Autopilot VMs
- [x] Application is detected in Intune