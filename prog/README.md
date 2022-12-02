# Prog Piano (temp)

3-parts programmation challenge about ASCII piano keyboards and chords.

These challenges must be run using python3.

NOTE : from now on, and for lisibility purposes, 'ASCII piano keyboard' will be abbreviated to Apk

## About chords

Throughout these stages, the player will encounter 4 chord types, which are :

* major
* minor
* aug
* dim

These chord types only represent the distance between the first note of the chord and the rest of the chords.

The chord name is the name of the first note aswell as the chord indicator ('', 'm', '+' or '-', is explained in details at due time)

### Major chords

After the first note of a major chord, you have 4 semitons before the 2nd note, and 3 semitons before the third.

### Minor chords

After the first note of a minor chord, you have 3 semitons before the 2nd note, and 4 semitons before the third.

### Major chords

After the first note of a major chord, you have 4 semitons before the 2nd note, and 4 semitons before the third.

### Major chords

After the first note of a major chord, you have 3 semitons before the 2nd note, and 3 semitons before the third.


## About Apks

For comprehension, an single ASCII piano keyboard will be refered as an Apk unit. 

```
_____________________________
|  | | | |  |  | | | | | |  |
|  | | | |  |  | | | | | |  |
|  | | | |  |  | | | | | |  |
|  |_| |_|  |  |_| |_| |_|  |
|   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |
|___|___|___|___|___|___|___|
```

## About first stage (piano1)

The goal of this challenge is to provide an Apk with a certain note marked 12 times in a row (one for each possible note).
The note names are in english. Note that the asked note can be a sharp note (indicated with the `#` symbol)

### Example

Input :

```
Give me the 4th G# plz
``` 

Solution :

```
_________________________________________________________________________________________________________________
|  | | | |  |  | | | | | |  |  | | | |  |  | | | | | |  |  | | | |  |  | | | | | |  |  | | | |  |  | | | | | |  |
|  | | | |  |  | | | | | |  |  | | | |  |  | | | | | |  |  | | | |  |  | | | | | |  |  | | | |  |  | | | | | |  |
|  | | | |  |  | | | | | |  |  | | | |  |  | | | | | |  |  | | | |  |  | | | | | |  |  | | | |  |  | | |X| | |  |
|  |_| |_|  |  |_| |_| |_|  |  |_| |_|  |  |_| |_| |_|  |  |_| |_|  |  |_| |_| |_|  |  |_| |_|  |  |_| |_| |_|  |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|

``` 

## About second stage (piano2)

The goal of this challenge is to find the chord corresponding to the Apk received in input 50 times in a row. The maximum time limit per Apk is 1 second.
The chord names are in english. Note that the asked chord can be a sharp chord (indicated with the `#` symbol)

Possible chords are all chords from major and minor scales containing 3 notes.

### Answer format

As this stage only contains major and minor scales, aswer format are pretty straightforward.

#### Answer format examples

for major chords : `G` 50 times in a row. The maximum time limit per Apk is 1 second.
for minor chords : `Gm`
for sharp major chords : `G#`
for sharp minor chords : `G#m`

### Example

Input : 

```
_________________________________________________________
|  | | | |  |  | | | | | |  |  | | | |  |  | | | | | |  |
|  | | | |  |  | | | | | |  |  | | | |  |  | | | | | |  |
|  | | |X|  |  | | | | | |  |  | | | |  |  | | |X| | |  |
|  |_| |_|  |  |_| |_| |_|  |  |_| |_|  |  |_| |_| |_|  |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| X |   |   |   |   |   |   |   |   |   |   |   |   |   |
|___|___|___|___|___|___|___|___|___|___|___|___|___|___|

Chord ?
```

Solution :

```
G#
```

## About third stage (piano3)

The goal of this challenge is to find the chord corresponding to the Apk received in input 50 times in a row. The maximum time limit per Apk is 1 second.

It distinguishes itself from second stage by implementing 2 new chord types (aug and dim), aswell as sending various Apk with various sizes, ranging from 3 to 8 units.

### Answer format

For major and minor scales, the answer format is the same as for second stage.

#### Answer format example

for aug chord : `G+`
for dim chord : `G-`
for sharp aug chord : `G#+`
for sharp dim chord : `G#-`

### Example

Input :

```
_____________________________________________________________________________________________________________________________________________
|  | | | |  |  | | | | | |  |  | | | |  |  | | | | | |  |  | | | |  |  | | | | | |  |  | | | |  |  | | | | | |  |  | | | |  |  | | | | | |  |
|  | | | |  |  | | | | | |  |  | | | |  |  | | | | | |  |  | | | |  |  | | | | | |  |  | | | |  |  | | | | | |  |  | | | |  |  | | | | | |  |
|  |X| | |  |  | | | | | |  |  | | | |  |  | | |X| | |  |  | | | |  |  | | | | | |  |  | | | |  |  | | | | | |  |  | | | |  |  | | | | | |  |
|  |_| |_|  |  |_| |_| |_|  |  |_| |_|  |  |_| |_| |_|  |  |_| |_|  |  |_| |_| |_|  |  |_| |_|  |  |_| |_| |_|  |  |_| |_|  |  |_| |_| |_|  |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   |   |   |   |
|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|

Chord ?
``` 

Solution : 

```
C#m
```