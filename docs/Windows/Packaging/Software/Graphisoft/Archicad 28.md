## Installation
- BMIx Desktop is no longer bundled.
- Install Path: `C:\Program Files\Graphisoft\Archicad 28`
- Don't remove installed components, since this can break other installed software that depends on them.
- License Manager Tool could potentially be packaged on its own.
### Registry changes
???- info "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall"
	- `{00060000-0000-1004-8002-0000C06B5161}`
		- DisplayName: WibuKey Setup (WibuKey Remove)
		- UninstallString: `"C:\Program Files (x86)\WIBUKEY\Setup\Setup64.exe" /R:{00060000-0000-1004-8002-0000C06B5161}`
	- `{546B9053-4996-4194-A67A-81F01A7CA413}`
		- DisplayName: CodeMeter Runtime Kit v8.20
		- UninstallString: `MsiExec.exe /I{546B9053-4996-4194-A67A-81F01A7CA413}`
	- `Archicad 28.0 NOR FULL R1 1`
		- DisplayName: Archicad 28 R1 NOR
		- UninstallString: `"C:\Program Files\Graphisoft\Archicad 28\Uninstall.AC\Uninstall.exe"`
		- DisplayVersion: `28.0.0.3001`
	- `License Manager Tool 20.0 INT FULL R1 1`
		- DisplayName: GRAPHISOFT License Manager Tool
		- UninstallString: `"C:\Program Files\Graphisoft\License Manager Tool\Uninstall.LMT\Uninstall.exe"`

## Intune
### Detection Rules
- Rule type: Registry
	- Key path: `HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\Archicad 28.0 NOR FULL R1 1`
	- Value name: DisplayVersion
	- Detection method: Version comparison
	- Operator: Equals
	- Value: `28.0.0.3001`
## Tests
- [x] Application installs on Autopilot VMs
- [x] Application has working license
- [x] Application is detected in Intune
- [x] Application uninstalls from Autopilot VMs
- [x] Application reinstalls on Autopilot VMs