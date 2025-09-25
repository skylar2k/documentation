## Filer
- Plassering av logfiler blir styrt av PolicyCSP fra Intune. Dette gjelder både MSI og Toolkit logs.
	- `C:\ProgramData\Microsoft\IntuneManagementExtension\Logs`
## Pakking
- Dependencies skal pakkes sammen i scripted til hoved programmet.
	- Legg dem under `SupportFiles` i PSADT.
	- Dependencies skal ikke fjernes ved avinstallasjon.
- Unngå å benytte eksterne MST filer, generer disse fra PSADT-scripted med hjelp av [New-ADTMsiTransform](https://psappdeploytoolkit.com/docs/reference/functions/New-ADTMsiTransform).
	- Dette hjelper alle med å lettere skjønne hva som faktisk blir gjort av endringer.
## Intune
- Avinstallasjon av tidligere versjoner skal ikke skje via Intune, men heller i siste versjon av PSADT-scripte.
### Navngivning av apper
Følger denne standarden: `<Bruksområde> <AppNavn> <Versjon>`
??? note "Bruksområder"
	- Felles: ingen prefiks
	- SADM: Lisensiert/tilpasset kun for sentraladministrasjonen
	- THT: Lisensiert/tilpasset kun for tannhelse.
	- VGS: Lisensiert/tilpasset kun for lærere og etter hvert elever.
	- VALE: Lisensiert/tilpasset kun for Ålesund VGS
### Tildeling
- Staff gruppe: Alle ansatte ved en skole
- Students gruppe: Alle elever ved en skole