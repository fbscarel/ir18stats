#!/usr/bin/env python3

import argparse
import json
from csv import DictReader
from operator import itemgetter

totalraces = {
  '2023S1': 343,
  '2022S4': 445,
  '2022S3': 619,
  '2022S2': 673,
  '2022S1': 601,
  '2021S4': 423,
  '2021S3': 478,
  '2021S2': 556,
  '2021S1': 593,
  '2020S4': 480,
  '2020S3': 426,
  '2020S2': 572
}

blocktracks = [
  'texas',
  'longbeach',
  'barber',
  'indianapolis',
  'detroit',
  'roadamerica',
  'midohio',
  'iowa',
  'worldwide',
  'lagunaseca'
]

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--debug", help="enable debug mode", action="store_true")
args = parser.parse_args()

with open("indy.csv", 'r') as f:
  dr = DictReader(f)
  tracks = list(dr)

for idx, track in enumerate(tracks):
  tracks[idx]['weighted'] = (float(track['races']) * (1 / totalraces[track['season']])) * 100

tracks = sorted(tracks, key=itemgetter('weighted'), reverse=True)

if args.debug:
  print(json.dumps(tracks, indent=4))

out = {}
i = 0
for track in tracks:
  if i > 11:
    break
  if track['track'] not in out:
    out[track['track']] = track['type']
    i += 1

print(json.dumps(out, indent=4))
