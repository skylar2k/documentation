## Installation
- BMIx Desktop is no longer bundled.
- Install Path: `C:\Program Files\Graphisoft\Archicad 28`
### Registry changes
- `HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall`
	- `{00060000-0000-1004-8002-0000C06B5161}`
		- DisplayName: WibuKey Setup (WibuKey Remove)
		- UninstallString: `"C:\Program Files (x86)\WIBUKEY\Setup\Setup64.exe" /R:{00060000-0000-1004-8002-0000C06B5161}`
	- `{546B9053-4996-4194-A67A-81F01A7CA413}`
		- DisplayName: CodeMeter Runtime Kit v8.20
		- UninstallString: `MsiExec.exe /I{546B9053-4996-4194-A67A-81F01A7CA413}`
	- `Archicad 28.0 NOR FULL R1 1`
		- DisplayName: Archicad 28 R1 NOR
		- UninstallString: `"C:\Program Files\Graphisoft\Archicad 28\Uninstall.AC\Uninstall.exe"`
	- `License Manager Tool 20.0 INT FULL R1 1`
		- DisplayName: GRAPHISOFT License Manager Tool
		- UninstallString: `"C:\Program Files\Graphisoft\License Manager Tool\Uninstall.LMT\Uninstall.exe"`