For packaging I use Hyper-V with VMs for two use cases:
1. Installing software and detecting changes, uses checkpoints to restore
2. Autopilot VMs for testing the packaged application.
## Hyper-V Setup
### Installing Hyper-V
???+ example "Enable Hyper-V"
	```powershell linenums="1"
	Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V -All
	```
### Configure switch
???+ example "Switch Setup"
	```powershell linenums="1"
	New-VMSwitch "Pakking (External)" -NetAdapterInterfaceDescription "Realtek USB GbE Family Controller #2" -AllowManagementOS $true
	```
### Create VMs
#### VM for software installation
???- example "Create VM for installing software"
	```powershell linenums="1"
	$VMName = "pkg-win11-01"
	$VM = @{
		Name = $VMName
		MemoryStartupBytes = 8192MB
		Generation = 2
		NewVHDPath = "C:\Virtual Machines\$VMName\$VMName.vhdx"
		NewVHDSizeBytes = 128GB
		BootDevice = "VHD"
		Path = "C:\Virtual Machines\$VMName"
		SwitchName = "Pakking (External)"
	}
	New-VM @VM
	Add-VMDvdDrive $VMName -Path "C:\Virtual Machines\ISOs\Win11_24H2_Norwegian_x64.iso"
	Set-VMFirmware $VMName -EnableSecureBoot On -FirstBootDevice (Get-VMDvdDrive $VMname)
	Set-VMKeyProtector $VMName -NewLocalKeyProtector
	Set-VMProcessor $VMName -Count 6 -HwThreadCountPerCore 0
	Enable-VMTPM $VMName
	Set-VM $VMName -AutomaticCheckpointsEnabled $false
	```
#### Autopilot VMs
???- example "Create VMs for Autopilot"
	```powershell linenums="1"
	foreach ($num in 1..4) {
		$VMName = "autopilot-win11-{0:D2}" -f $num
		$VM = @{
			Name = $VMName
			MemoryStartupBytes = 8192MB
			Generation = 2
			NewVHDPath = "C:\Virtual Machines\$VMName\$VMName.vhdx"
			NewVHDSizeBytes = 128GB
			BootDevice = "VHD"
			Path = "C:\Virtual Machines\$VMName"
			SwitchName = "Pakking (External)"
		}
		New-VM @VM
		Add-VMDvdDrive $VMName -Path "C:\Virtual Machines\ISOs\Win11_24H2_Norwegian_x64.iso"
		Set-VMFirmware $VMName -EnableSecureBoot On -FirstBootDevice (Get-VMDvdDrive $VMname)
		Set-VMKeyProtector $VMName -NewLocalKeyProtector
		Set-VMProcessor $VMName -Count 6 -HwThreadCountPerCore 0
		Enable-VMTPM $VMName
		Set-VM $VMName -AutomaticCheckpointsEnabled $false
	}
	```
## VM Setup
### Software installation VM
After the VM is configured, run through the windows setup with a local user account, make sure to run Windows Update after OOBE and then proceed to power down and make a checkpoint.
???+ example "Create Snapshot"
	```powershell linenums="1"
	Checkpoint-VM -Name "pkg-win11-01" FreshInstallWithUpdates
	```
### Autopilot VM
Gather the HWID and other information needed during OOBE and register them in your Autopilot devices. Getting the required information can be done by pressing Ctrl+Shift+D during OOBE, this opens the diagnostic menu where you can export autopilot logs congaing the one CSV file you need.