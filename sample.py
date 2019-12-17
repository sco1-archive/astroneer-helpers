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