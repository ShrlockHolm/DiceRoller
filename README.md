# DiceRoller
## Features
Stealing the features from [here](https://dice-roller.github.io/documentation/guide/notation/modifiers.html#compounding)
### Dice
- basic roll: any number of any size dice
	- AdB = roll qty A of B-sided dice
    - results are 1 to dieSize
    - return both the sum of the dice and the result of each die individually
- Custom/funky dice
    - Fate/fudge dice
    - dice with unique/custom distributions or non-numeric results (nice to have, not requirement)
### Modifiers/functions
An order of operations must be applied to make sure that everything calculates correctly
1. Min/Max
    - causes any die result below a certain value (min) or above a certain value (max) to be set to that value instead
2. Exploding
	- if a specific result is achieved (usually the maximum of that die) then the die is rolled again and added to the current result
3. re-roll
	- similar to exploding
	- if a specific result is achieved (usually the minimum of a die) then the die is rolled again and the previous result is dropped
	- r = rerolls whenever the result is achieved
	- ro = rerolls only once
4. keep (first) / drop (second)
	- rolls qty A dice and keeps or drops qty X dice. The selection of which dice to drop depends on the function picked.
		- keep highest X
		- keep lowest X
		- drop highest X
		- drop lowest X
5. dice pool
	- target success
	- target failure
