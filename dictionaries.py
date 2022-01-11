from pprint import pprint

d1 = dict()  # empty dict
d2 = {'a': 5, 'm': 16, 'c': 4}
d3 = {}  # empty dict

airports = {
    'EWR': 'Newark',
    'YYZ': 'Toronto',
    'MCI': 'Kansas City',
    'SFO': 'San Francisco',
    'RDU': 'Raleigh-Durham',
    'SJC': 'San Jose',
    'MCO': 'Orlando',
    'YCC': 'Calgary',
    'ABQ': 'Albuquerque',
    'OAK': 'Oakland',
    'SMF': 'Sacramento',
    'YOW': 'Ottawa',
    'IAD': 'Dulles',
}

airports['ATL'] = 'Atlanta'
airports['LAX'] = 'Los Angeles'
airports['RDU'] = 'Greensboro'
print(airports)

print(airports['MCO'])
print(airports['RDU'])
print()

for code in 'RDU', 'LAX', 'GXM', 'WOMBAT', 'IAD':
    print(code, airports.get(code, 'NOT FOUND'))
print()


codes = {}
codes['a'] = []
codes['b'] = []

codes['a'].append(5)
codes['a'].append(10)
codes['b'].append(2)

print(codes)
print(airports)

counts = {}
with open('DATA/words.txt') as words_in:
    for word in words_in:
        first_letter = word[0]

        if first_letter not in counts:
            counts[first_letter] = 0

        counts[first_letter] += 1
        #  counts[first_letter] = counts[first_letter] + 1

pprint(counts)










