Alle applikasjoner har sitt eget Git-repo, Git funker slik at utviklere (oss) har en lokal-kopi og historikk av koden og endringer, i tillegg har vi en felles remote kopi og historikk (Gitlab). Når vi jobber begår vi endringer i den lokale kopien, når vi er fornøyd og ønsker å gjøre disse endringene tilgjengelig for resten av teamet "pusher" vi dem til vår felles remote.

Alle pakker benytter en standard mal som vi oppdaterer til nyeste versjon av PSADT underveis: [MrFylke / PSADT / template · GitLab](https://gitlab.com/mrfylke/psadt/template).

1. Opprett ny lokalkopi og remote repo(sitory)
	1. `copier copy --trust gl:mrfylke/psadt/template "Stream Deck"`
	   ![[Pasted image 20250925114253.png]]
	2. Dette oppretter også et privat repo i Gitlab
	   ![[Pasted image 20250925121532.png]]
2. Lag ny branch for utvikling
	1. `git checkout -b 7.0.0.22005`
	   ![[Pasted image 20250925115633.png]]
3. Begå en endring. Jeg velger å starte med å fylle ut Install delen av scriptet
   ![[Pasted image 20250925120141.png]]
4. Sjekk og verifiserer endringene som er begått, eventuelt test endringen.
	1. `git status`: Viser filer som har endret seg og om endringene er staged
	   ![[Pasted image 20250925122340.png]]
	2. `git diff`: Se i detalj hva som har endret seg i fil(er)
	   ![[Pasted image 20250925122756.png]]
5. Stage endringer. Dette forteller git at du ønsker å utføre disse endringene i historikken ved neste commit
	1. `git add Invoke-AppDeployToolkit.ps1`: Stager endringene i `Invoke-AppDeployToolkit.ps1` filen for neste commit.
		1. `git add .` vil stage alle endringer.
	2. Disse filene vil nå ligge under "Changes to be committed" når man nå kjører `git status`
	   ![[Pasted image 20250925130827.png]]
6. Commit endringene. Dette vil faktisk begå endringene i ditt lokale git repo.
	1. `git commit -m "Ferdig med Install-ADTDeployment"`
		1. `-m` flagget brukes for message, alle endringer i historikken må ha en melding.
	2. Dette vil også kjøre pre-commit hooks, som skal stoppe og rette opp i lettere feil i koden. Min commit ble ikke begått fordi jeg hadde en feil ved slutten av scriptet, men pre-commit fikset det.
	   ![[Pasted image 20250925131539.png]]
		1. Jeg må derfor stage den nye endringen utført av pre-commit og commite på nytt.
		   ![[Pasted image 20250925131807.png]]
	3. Slik skal det se ut når en commit går gjennom
	   ![[Pasted image 20250925132147.png]]
7. Gjenta fra steg 3 til du er klar for å pushe endringene til remote.
8. Jeg har nå opprettet 2 forskjellige commits
   ![[Pasted image 20250925134715.png]]
9. `git push -u origin HEAD` dette pusher endringene til Gitlab og gjør dem tilgjengelig på branch `7.0.0.22005`
   ![[Pasted image 20250925134942.png]]
10. Følg lenken du får over for å merge endringene til master branch. Tykk på "Create merge request"
    ![[Pasted image 20250925135151.png]]
11. Tykk så på "Merge", dette "merger" endringene gjort på branch `7.0.0.22005` til `master` branch.
    ![[Pasted image 20250925135330.png]]
12. Endringene og historikken ligger nå tilgjengelig remote
    ![[Pasted image 20250925140342.png]]
13. `git checkout master` endrer branch tilbake til master, siden vi er ferdig med utviklingen knyttet til branch `7.0.0.22005`.
14. `git pull` hent og utfør alle endringene fra remote.
15. `git branch -d 7.0.0.22005` sletter gammel branch.