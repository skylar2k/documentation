## Ranks
```rust
enum ERank {
	Street_Rat,
	Hoodlum,
	Peddler,
	Hustler,
	Bagman,
	Enforcer,
	Shot_Caller,
	Block_Boss,
	Underlord,
	Baron,
	Kingpin
}
```
## Tiers
Each rank has a tier, if your tier is under 5 it will add + 1 tier. Otherwise it will give you the next rank and set your tier to one. The exception to this is the Kingpin rank, from here on you will just endlessly go up in tiers. 