#!/usr/bin/env python

import sys
from knight import Knight

for name in sys.argv[1:]:
    k = Knight(name)  # name = 'Arthur', 'Lancelot', etc.
    print("Name: {} {}".format(k.title, k.name))
    print("Favorite Color:", k.color)
    print()
