# Customers
## Preferred properties
All customers can at most have 3 preferred properties

## Weekly spend limit
All customers have a weekly spend limit, based on a minimum spend limit, max spend limit and your relationship with the NPC. This number is then multiplied by the order limit multiplier.

The order limit is set using linear interpolation between two points, current rank multiplier and next rank multiplier. It uses your current tier to find a point between these two.

Example 1:
```
Current Rank: Hoodlum
Current Tier: 1
Multiplier: 1.25
```
Example 2:
```
Current Rank: Hoodlum
Current Tier: 4
Multiplier: 1.4375
```
I've implemented the calculations for this in Rust: [Schedule1/orderlimit.rs at main · skylar2k/Schedule1](https://github.com/skylar2k/Schedule1/blob/main/orderlimit.rs)