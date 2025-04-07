## Value calculation
Example of calculation, where the starting value depends on the base value of the product.
```py
value: float = 35.0
tmp: float = 1.0
for property in product['properties']:
	value += property['value_change']
	value += product['base_value'] * property['vmultiple']
	tmp *= property['value_multiplier']
round(value * tmp)	
```
## Drug affinities
Customers have something called `ProductAffinites` that determine what type of product they prefer:
- -1: hates
- 0: neutral
- 1: loves
The affinities are serialized like so: 
```json
"ProductAffinities": [
    0.0,
    1.0,
    -0.27000001072883608
]
```
Where the order is based on the following enum:
```c#
public enum EDrugType  
{  
    Marijuana,  
    Methamphetamine,  
    Cocaine,  
    MDMA,  
    Shrooms,  
    Heroin  
}
```
