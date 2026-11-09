"""Locations that are missing from data already fetched, grouped by model group.

Generated 2026-11-09 by a sanity check of every zone file in
`data/raw/soil era5/` and `data/processed/Temperature/` against
`fieldshift_gdhy_spaced_coordinates.py` (150 planned points per model, daily
2000-01-01 to 2019-12-31). Each list holds [latitude, longitude] pairs
in WGS84, in the same order as MODEL_LOCATIONS, ready to feed into a fetch script.

ERA5 soil:
  1,109 of 1,200 planned points present, 91 never fetched.
  Every location that IS present in ERA5 soil passed all checks:
  all 7305 days from 2000-01-01 to 2019-12-31, no duplicated
  id+date rows, no internal date gaps, no blank/NaN, unparseable or sentinel values,
  and no coordinates outside the plan. The gap is fetch coverage, not the date pipeline.

NASA POWER merged temperature:
  1,200 of 1,200 planned points present, 0 never fetched.
  NASA POWER temperature: every location IS present but the following value/date defects were also
  found and must be repaired, not just refetched:
      nan: 26
"""

# ERA5 SOIL — missing locations

# M1: 10 of 150 missing  (ids m1024, m1065, m1067, m1090, m1091, m1105, m1115, m1136, m1137, m1141)
MISSING_ERA5_SOIL_M1 = [
    [-2.75, -65.25],  # planned point #24
    [8.25, -82.25],  # planned point #65
    [7.75, -80.25],  # planned point #67
    [-0.25, 9.25],  # planned point #90
    [1.75, 9.75],  # planned point #91
    [1.75, 101.75],  # planned point #105
    [-0.25, 119.75],  # planned point #115
    [5.75, 125.25],  # planned point #136
    [8.75, 126.25],  # planned point #137
    [8.75, 124.75],  # planned point #141
]

# M2: 6 of 150 missing  (ids m2006, m2028, m2039, m2058, m2060, m2104)
MISSING_ERA5_SOIL_M2 = [
    [22.75, 77.75],  # planned point #6
    [21.75, 88.75],  # planned point #28
    [20.25, 93.25],  # planned point #39
    [20.75, 106.75],  # planned point #58
    [10.25, 106.75],  # planned point #60
    [-15.75, -48.25],  # planned point #104
]

# M3: 2 of 150 missing  (ids m3060, m3111)
MISSING_ERA5_SOIL_M3 = [
    [16.25, -13.75],  # planned point #60
    [24.25, 70.25],  # planned point #111
]

# M4: 20 of 150 missing  (ids m4016, m4024, m4034, m4035, m4057, m4061, m4062, m4065, m4068, m4069, m4072, m4073, m4075, m4076, m4078, m4080, m4089, m4090, m4108, m4115)
MISSING_ERA5_SOIL_M4 = [
    [33.25, -117.25],  # planned point #16
    [40.75, -8.75],  # planned point #24
    [37.75, -0.75],  # planned point #34
    [39.25, -0.25],  # planned point #35
    [40.75, 14.25],  # planned point #57
    [38.25, 15.75],  # planned point #61
    [37.25, 15.25],  # planned point #62
    [41.75, 13.25],  # planned point #65
    [42.75, 10.75],  # planned point #68
    [41.75, 12.25],  # planned point #69
    [36.75, 22.25],  # planned point #72
    [40.75, 23.75],  # planned point #73
    [37.75, 23.75],  # planned point #75
    [38.25, 21.25],  # planned point #76
    [38.25, 22.75],  # planned point #78
    [43.75, 15.75],  # planned point #80
    [36.75, 27.75],  # planned point #89
    [38.75, 26.75],  # planned point #90
    [35.25, -4.75],  # planned point #108
    [35.75, 10.75],  # planned point #115
]

# M5: 23 of 150 missing  (ids m5009, m5010, m5024, m5031, m5032, m5033, m5035, m5052, m5054, m5055, m5056, m5060, m5073, m5086, m5088, m5110, m5114, m5124, m5127, m5128, m5129, m5137, m5144)
MISSING_ERA5_SOIL_M5 = [
    [43.75, -74.25],  # planned point #9
    [39.75, -74.25],  # planned point #10
    [37.75, -75.75],  # planned point #24
    [45.75, -82.75],  # planned point #31
    [43.25, -82.25],  # planned point #32
    [43.75, -77.25],  # planned point #33
    [44.75, -81.75],  # planned point #35
    [52.25, 5.25],  # planned point #52
    [52.25, 13.25],  # planned point #54
    [53.75, 10.75],  # planned point #55
    [50.75, 3.25],  # planned point #56
    [45.25, -1.25],  # planned point #60
    [45.25, 26.75],  # planned point #73
    [-30.75, -57.75],  # planned point #86
    [-34.25, -53.75],  # planned point #88
    [38.25, 114.25],  # planned point #110
    [39.25, 121.75],  # planned point #114
    [37.75, 126.25],  # planned point #124
    [-38.75, 175.75],  # planned point #127
    [-36.25, 174.25],  # planned point #128
    [-40.75, 172.75],  # planned point #129
    [-41.75, 171.75],  # planned point #137
    [-38.75, 146.25],  # planned point #144
]

# M6: 8 of 150 missing  (ids m6029, m6036, m6061, m6096, m6122, m6125, m6143, m6150)
MISSING_ERA5_SOIL_M6 = [
    [52.25, -113.75],  # planned point #29
    [54.25, -113.75],  # planned point #36
    [51.25, 37.75],  # planned point #61
    [46.25, 81.75],  # planned point #96
    [47.75, 124.25],  # planned point #122
    [45.25, 124.25],  # planned point #125
    [46.75, 27.75],  # planned point #143
    [47.75, 102.75],  # planned point #150
]

# M7: 19 of 150 missing  (ids m7012, m7023, m7029, m7030, m7031, m7042, m7044, m7052, m7053, m7063, m7075, m7078, m7082, m7088, m7092, m7093, m7094, m7098, m7145)
MISSING_ERA5_SOIL_M7 = [
    [60.25, -141.25],  # planned point #12
    [61.75, -137.25],  # planned point #23
    [65.75, -114.25],  # planned point #29
    [65.75, -121.25],  # planned point #30
    [61.25, -110.25],  # planned point #31
    [56.25, -101.75],  # planned point #42
    [56.75, -108.25],  # planned point #44
    [53.25, -98.25],  # planned point #52
    [54.75, -94.25],  # planned point #53
    [54.25, -72.25],  # planned point #63
    [62.25, 25.75],  # planned point #75
    [63.25, 21.75],  # planned point #78
    [62.25, 30.75],  # planned point #82
    [67.75, 14.75],  # planned point #88
    [65.25, 11.75],  # planned point #92
    [68.75, 17.25],  # planned point #93
    [64.75, -18.75],  # planned point #94
    [64.25, -16.25],  # planned point #98
    [59.75, 161.25],  # planned point #145
]

# M8: 3 of 150 missing  (ids m8078, m8083, m8091)
MISSING_ERA5_SOIL_M8 = [
    [28.75, 83.25],  # planned point #78
    [31.25, 76.75],  # planned point #83
    [30.25, 80.25],  # planned point #91
]

MISSING_ERA5_SOIL_BY_MODEL = {
    "M1": MISSING_ERA5_SOIL_M1,
    "M2": MISSING_ERA5_SOIL_M2,
    "M3": MISSING_ERA5_SOIL_M3,
    "M4": MISSING_ERA5_SOIL_M4,
    "M5": MISSING_ERA5_SOIL_M5,
    "M6": MISSING_ERA5_SOIL_M6,
    "M7": MISSING_ERA5_SOIL_M7,
    "M8": MISSING_ERA5_SOIL_M8,
}

MISSING_ERA5_SOIL_ALL = [p for pts in MISSING_ERA5_SOIL_BY_MODEL.values() for p in pts]

# NASA POWER TEMPERATURE — missing locations

# M1: 0 of 150 missing
MISSING_POWER_M1 = []

# M2: 0 of 150 missing
MISSING_POWER_M2 = []

# M3: 0 of 150 missing
MISSING_POWER_M3 = []

# M4: 0 of 150 missing
MISSING_POWER_M4 = []

# M5: 0 of 150 missing
MISSING_POWER_M5 = []

# M6: 0 of 150 missing
MISSING_POWER_M6 = []

# M7: 0 of 150 missing
MISSING_POWER_M7 = []

# M8: 0 of 150 missing
MISSING_POWER_M8 = []

MISSING_POWER_BY_MODEL = {
    "M1": MISSING_POWER_M1,
    "M2": MISSING_POWER_M2,
    "M3": MISSING_POWER_M3,
    "M4": MISSING_POWER_M4,
    "M5": MISSING_POWER_M5,
    "M6": MISSING_POWER_M6,
    "M7": MISSING_POWER_M7,
    "M8": MISSING_POWER_M8,
}

MISSING_POWER_ALL = [p for pts in MISSING_POWER_BY_MODEL.values() for p in pts]

