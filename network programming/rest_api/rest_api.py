# Kinga Syta
import time
import requests
import sys

if len(sys.argv) != 2:
    print("Pass the artist number as a second argument")
    sys.exit(1)

id_of_given_band = sys.argv[1]
response = requests.get('https://api.discogs.com/artists/' + str(id_of_given_band))

if response.status_code != requests.codes.ok:
    print("Ouuups! Status code", response.status_code)
    sys.exit(1)
else:
    members = response.json()['members']

dict = {}  # {band_name: player_id}
artist_dict = {}  # {player_id: player_name}
band_dict = {}  # {band_name: band_id}
for member in members:
    artist_dict[member['id']] = member['name']
    res = requests.get(member['resource_url'])
    while res.status_code != requests.codes.ok:
        time.sleep(5)
        res = requests.get(member['resource_url'])
        print("Waiting...")
    else:
        artist_groups = res.json()['groups']
        if len(artist_groups) > 1:  # if musician played in any other band than id_of_given_band
            for group in artist_groups:
                if group['name'] not in dict.keys():
                    band_dict[group['name']] = group['id']
                    dict[group['name']] = [res.json()['id']]
                else:
                    dict[group['name']].append(res.json()['id'])

for band_name, artist_ids in sorted(dict.items(), key=lambda x: x[0]):  # sorted on band_name
    if len(artist_ids) > 1 and str(band_name) != str(response.json()['name']):
        print(id_of_given_band, "is", response.json()['name'], ". According to Discogs, it's players are/were",
              [[artist_dict[x], x] for x in artist_ids], "who also played in band:", band_name, "with id:", band_dict[band_name])

sys.exit(0)
