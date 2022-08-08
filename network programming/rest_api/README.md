# REST API

This program, based on information from Discogs(https://www.discogs.com/), checks whether members (current or former) of a given band played together in any other bands.
As the output, the names of these other bands and the names of the musicians are displayed. The numeric identifier of the team in the Discogs database is given as an argument to the program.

## Run

In command line run:

```bash
python3 rest_api.py band_numer_in_discogs
```

## Example

Input:
python3 rest_api.py 359282

Output:
359282 is Budka Suflera . According to Discogs, it's players are/were [['Krzysztof Cugowski', 516821], ['Krzysztof Mandziara', 543450]] who also played in band: Cross (6) with id: 1435
365
359282 is Budka Suflera . According to Discogs, it's players are/were [['Andrzej Sidło', 1005147], ['Romuald Czystaw', 1005163]] who also played in band: Partita with id: 952543
359282 is Budka Suflera . According to Discogs, it's players are/were [['Marek Stefankiewicz', 532854], ['Mieczysław Jurecki', 702387]] who also played in band: Perfect (7) with id: 66
9348
359282 is Budka Suflera . According to Discogs, it's players are/were [['Tomasz Zeliszewski', 516820], ['Mieczysław Jurecki', 702387]] who also played in band: Wieko with id: 4751291
