# builtin
# 3rd-party (semi-official)
# local (locally developed)
import sys  # run-time info
#   from pkg.pkg import module
#  find john/math/geometry.py
from john.math import geometry

a1 = geometry.circle_area(25)
a2 = geometry.square_area(10)
a3 = geometry.rectangle_area(5, 10)

print(a1, a2, a3)

print(geometry.MAX_SIZE)

# search strategy
# 1. current folder
# 2. folders in PYTHONPATH
# 3. builtin folders

for path in sys.path:
    print(path)

