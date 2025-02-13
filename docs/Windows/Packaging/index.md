Documentation on packaging software on Windows, specifically using [PSAppDeployToolkit](https://psappdeploytoolkit.com/), Hyper-V and Intune.
## PSADT Sources
I store all of my PSADT sources on Github: [skylar2k/PSADT](https://github.com/skylar2k/PSADT).
This repo uses SOPS to encrypt secrets and a simple PowerShell-script to decrypt secrets and package applications to IntuneWin files.
To use this repo, you need:

- [getsops/sops: Simple and flexible tool for managing secrets](https://github.com/getsops/sops)
- [IntuneWInAppUtil.exe](https://github.com/microsoft/Microsoft-Win32-Content-Prep-Tool)
- [junegunn/fzf: :cherry_blossom: A command-line fuzzy finder](https://github.com/junegunn/fzf)
- [kelleyma49/PSFzf: A PowerShell wrapper around the fuzzy finder fzf](https://github.com/kelleyma49/PSFzf)
## Useful software for packaging
- [Process Monitor - Sysinternals | Microsoft Learn](https://learn.microsoft.com/en-us/sysinternals/downloads/procmon)
- [RegistryChangesView - Compare snapshots of Windows Registry](https://www.nirsoft.net/utils/registry_changes_view.html)