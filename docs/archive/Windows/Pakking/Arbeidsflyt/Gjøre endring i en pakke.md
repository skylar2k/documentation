## Ikke tidligere jobbet på

1. Begynne med å finne pakken på vår remote [PSADT · GitLab](https://gitlab.com/mrfylke/psadt). Jeg skal gjøre endring i stream-deck pakken.
   ![[Pasted image 20250925143138.png]]
2. Jeg må nå clone denne pakken til min lokale pc. Kopier det som står under "Code > Clone with SSH"
   ![[Pasted image 20250925143538.png]]
3. Kjør `git clone git@gitlab.com:mrfylke/psadt/stream-deck.git`. Nå har jeg en lokal kopi jeg kan jobbe med
   ![[Pasted image 20250925143714.png]]
4. Oppretter ny branch å jobbe på med `git checkout -b readme`
5. Gjør endringer.
   ![[Pasted image 20250925144331.png]]
6. Stager og commiter endringer med `git commit -am "Kilde til setup fila"`
	1. `-a` flagget stager alle filer som git allerede vet om og har historikk på.
   ![[Pasted image 20250925144506.png]]
7. Jeg hadde glemt å laste opp bilde fil (logo til programmet), så jeg velger å også gjøre det nå. Kopierer `image.png` til mappen og kjører `git add image.png`
8. Lagger ny commit med: `git commit -m "Logo bildefil"`
9. Hent siste endringene fra remote: `git pull origin master`
10. Push min lokale readme branch til remote: `git push origin readme`
11. Følg lenken fra meldingen du får etter push, trykk "Create merge request" og vent til alle testene er ferdig
    ![[Pasted image 20250925145839.png]]
12. Trykk så Merge. dette sletter readme branchen på vår remote etter at endringene blir merget til master branch.
13. `git checkout master` for å endre branch tilbake, `git pull` hente endringene fra merge og `git branch -d readme` for å slette readme branch lokalt.
14. Nå ligger der kilde til installer på Gitlab, samt image.png.