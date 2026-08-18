## Oppsett av miljøet
Last ned og installer siste versjon av:

- [Visual Studio Code - Code Editing. Redefined](https://code.visualstudio.com/)
- [Git](https://git-scm.com/)
- [Python](https://www.python.org/)
- [getsops/sops: Simple and flexible tool for managing secrets](https://github.com/getsops/sops)
- [microsoft/Microsoft-Win32-Content-Prep-Tool: A tool to wrap Win32 App and then it can be uploaded to Intune](https://github.com/microsoft/Microsoft-Win32-Content-Prep-Tool)
- [Gpg4win - Secure email and file encryption with GnuPG for Windows](https://www.gpg4win.org/)
### Git
For å benytte git må du sette navn og epost til det samme du har i GitLab. Anbefaler å lese [Using Git - GitHub Docs](https://docs.github.com/en/get-started/using-git) for en liten introduksjon.

1. Navn: `git config --global user.name "John Doe"`
2. Epost: `git config --global user.email johndoe@example.com`
#### SSH-nøkler
Disse brukes til å sikre tilgang til våre Git-repos. Siden vi alle har Yubikeys benytter vi oss av dem for passordløs autentisering. Du er derfor avhengig av å ha denne når du gjør endringer og skal publisere dem til resten av Teamet.

1. Gener ssh-nøkkel: `ssh-keygen.exe -t ed25519-sk -O resident -C "skylar@unix.rs"`
2. Last opp public key til [SSH Keys · User Settings · GitLab](https://gitlab.com/-/user_settings/ssh_keys). Her fyllet du inn innholdet fra filen `"C:\Users\<USERNAME>\.ssh\id_ed25519_sk.pub"`
### Pipx
Pipx brukes til å installere python program i et lukket miljø per program.

1. Installer via `python3.exe -m pip install --user pipx`
2. Legg til stien du får fra `python3.exe -m pipx ensurepath` i din PATH miljø variabel.
3. Lukk alle CMD/Powershell vindu og åpne så et nytt.
	1. Om du ikke benyttet system miljøvariabler må du trolig logge inn og ut igjen.
4. Installer pipx program:
	1. `pipx install copier`
	2. `pipx install pre-commit`
### SOPS - Kryptering av filer
TODO
# Gpg4win
TODO, GPG kryptering på Windows