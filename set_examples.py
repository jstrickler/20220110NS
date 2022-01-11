ann_countries = ['Morocco', 'India', 'Burkina Faso', 'Ireland', 'Canada', 'Spain', 'France']
bob_countries = ['France', 'India', 'Spain', 'Portugal', 'Ireland', 'Bolivia', 'Pakistan', 'Nepal']

ann = set(ann_countries)
bob = set(bob_countries)

print("common:", ann & bob)   # intersection
print("not common:", ann ^ bob)  # xor  (union - intersection)
print("all:", ann | bob)  # union
print("ann only:", ann - bob)
print("bob only:", bob - ann)

food = ['spam', 'spam', 'spam', 'spam', 'spam', 'spam', 'spam', 'toast',
        'spam', 'toast', 'spam', 'spam', 'spam', 'spam', 'ham', 'eggs', 'ham',
        'spam', 'spam', 'spam', 'spam', 'spam', 'spam', 'spam',
        'spam', 'spam', 'spam', 'spam', 'spam', 'spam']

unique_foods = set(food)
print(unique_foods)


