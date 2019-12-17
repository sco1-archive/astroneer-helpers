# Astroneer helpers

Yay!

## BOM
Reduce the provided build list into a table of base resources

```py
from bom import build_table


ELA_ROVER = {
    "FLOODLIGHT": 2,
    "DRILL_STRENGTH_2": 2,
    "MEDIUM_CANISTER": 2,
    "MEDIUM_STORAGE": 1,
    "MEDIUM_STORAGE_SILO": 6,
    "PAVER": 1,
    "ROVER_SEAT": 1,
    "RTG": 1,
    "CRANE": 1,
    "LARGE_STORAGE": 2,
    "LARGE_ROVER": 2,
}

print(build_table(ELA_ROVER))
```

```
ALUMINUM   5
ARGON      2
CARBON     9
CERAMIC    6
COMPOUND   4
COPPER     5
GLASS      2
GRAPHITE   3
HELIUM     1
HYDROGEN   3
IRON       2
LITHIUM    1
METHANE    2
NITROGEN   3
ORGANIC    4
QUARTZ     2
RESIN      8
TITANIUM  16
TUNGSTEN   9
```
