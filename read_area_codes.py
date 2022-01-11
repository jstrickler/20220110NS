import csv
from pprint import pprint

area_codes = {}

with open('area_codes.csv') as area_codes_in:
    rdr = csv.reader(area_codes_in)
    for row in rdr:
        area_codes[row[0]] = row[1:]

pprint(area_codes)
print()
print("Iowa area codes:", area_codes['Iowa'])
print('-' * 60)

# for key, value in DICT.items()
for state, codes in area_codes.items():
    print(state)
    for code in sorted(codes):
        print(f"  {code}")

