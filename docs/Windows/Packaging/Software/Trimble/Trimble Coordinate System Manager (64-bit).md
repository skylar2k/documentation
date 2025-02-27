## Installation
- Arch: x64
- Silent install: `msiexec /i "coordinatesystemmanager-3.10.1.msi" /qn`
- Silent uninstall: `msiexec /x "coordinatesystemmanager-3.10.1.msi" /qn`
## Registry changes
???- info "HKLM\Software\Microsoft\Windows\CurrentVersion\Uninstall"
	- `{f7a8afb4-e910-4bdf-9e79-52f926f23a2a}`
		- DisplayName: Trimble Coordinate System Manager (64-bit)
		- DisplayVersion: 3.10.1.0
		- UninstallString: `MsiExec.exe /I{f7a8afb4-e910-4bdf-9e79-52f926f23a2a}`
???- info "HKLM\Software\Trimble"
	- `Share`
		- SharedFilesLocation: `C:\Program Files (x86)\Common Files\Trimble\`
		- CurrentGeoDBFile: `C:\ProgramData\Trimble\GeoData\current.csd`
		- CurrentGeoDataDirectory: `C:\ProgramData\Trimble\GeoData\`
		- SystemDatabaseFile: `C:\ProgramData\Trimble\GeoData\template.cst`
???- info "HKLM\Software\WOW6432Node\Trimble"
	- `Share`
		- SharedFilesLocation: `C:\Program Files (x86)\Common Files\Trimble\`
		- CurrentGeoDBFile: `C:\ProgramData\Trimble\GeoData\current.csd`
		- CurrentGeoDataDirectory: `C:\ProgramData\Trimble\GeoData\`
		- SystemDatabaseFile: `C:\ProgramData\Trimble\GeoData\template.cst`
## File paths
???- info "Shared DLLs"
	- `C:\Program Files\Common Files\Trimble\Core\SCCalcUx64.dll`
	- `C:\Program Files\Trimble\Coordinate System Manager\GeodeticX.dll`
	- `C:\Program Files\Common Files\Trimble\Core\CSDUx64.dll`
	- `C:\Program Files\Common Files\Trimble\Core\CoreGlbx64.dll`
	- `C:\Program Files\Common Files\Trimble\Core\Gdticx64.dll`
	- `C:\Program Files (x86)\Common Files\Trimble\Core\CSDfileU.dll`
	- `C:\Program Files (x86)\Common Files\Trimble\Core\CSRprtU.dll`
	- `C:\Program Files (x86)\Common Files\Trimble\Core\CSDUIU.dll`
	- `C:\Program Files (x86)\Common Files\Trimble\Core\CSDU.dll`
	- `C:\Program Files (x86)\Common Files\Trimble\Core\CoreGlb.dll`
	- `C:\Program Files (x86)\Common Files\Trimble\Core\DC2IRec.dll`
	- `C:\Program Files (x86)\Common Files\Trimble\Core\Gdtic.dll`
	- `C:\Program Files (x86)\Common Files\Trimble\Core\GridGenU.dll`
	- `C:\Program Files (x86)\Common Files\Trimble\Core\SCCalcU.dll`
	- `C:\Program Files (x86)\Common Files\Trimble\GeoDB\Template.cst`
	- `C:\ProgramData\Trimble\GeoData\Template.cst`
	- `C:\Program Files (x86)\Common Files\Trimble\Core\CVTU.dll`
## Intune
### Detection Rules
#### Rule type: File
???- info "File: `C:\Program Files\Trimble\Coordinate System Manager"
	- File or folder: CoordinateSystemManager.exe
	- Detection method: String (version)
	- Operator: Greater than or equal to
	- Value: ``
## Tests
- [x] Application installs on Autopilot VMs
- [x] Application is detected in Intune
- [x] Application uninstalls
- [x] Application reinstalls on Autopilot VMs
- [ ] License activates