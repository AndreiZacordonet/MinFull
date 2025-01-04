
# using tuples for the immutable behaviour (MIN_SPEED, MAX_SPEED, BASE_SPEED, SLOPE_ANGLE, TURN_ANGLE)
# SEGMENT1 = (50, 100, 60, 0.05, 0)
# SEGMENT2 = (50, 100, 60, 0.05, 200)
# SEGMENT3 = (40, 70, 50, 0.05, 200)
# SEGMENT4 = (60, 100, 70, 0.05, 200)

SEGMENT1 = (50, 100, 60, 0.05, 0)       # Straight road, slight incline
SEGMENT2 = (50, 100, 60, 0.05, 200)     # Moderate curve
SEGMENT3 = (40, 70, 50, 0.05, 200)      # Tight curve
SEGMENT4 = (60, 100, 70, 0.05, 200)     # Gentle curve
SEGMENT5 = (40, 90, 60, 0.1, 0)         # Hilly straight road
SEGMENT6 = (50, 110, 70, -0.03, 0)      # Downhill straight
SEGMENT7 = (30, 60, 40, 0.08, 300)      # Sharp turn uphill
SEGMENT8 = (50, 80, 65, 0.02, -100)     # Gentle downhill curve
SEGMENT9 = (40, 70, 50, 0.06, 180)      # Moderate curve with incline
SEGMENT10 = (30, 60, 45, 0.12, 350)     # Steep uphill, tight turn
SEGMENT11 = (60, 100, 75, -0.02, 0)     # Straight downhill
SEGMENT12 = (50, 90, 70, 0.04, -150)    # Curving descent
SEGMENT13 = (50, 100, 65, 0.03, 50)     # Slight curve
SEGMENT14 = (40, 80, 55, 0.07, 250)     # Curve with moderate slope
SEGMENT15 = (60, 110, 80, 0.01, 0)      # Straight and fast
SEGMENT16 = (30, 60, 40, 0.15, 400)     # Sharp turn with steep incline
SEGMENT17 = (50, 90, 65, -0.04, -180)   # Moderate curve downhill
SEGMENT18 = (40, 70, 50, 0.02, 100)     # Gentle curve with small incline
SEGMENT19 = (50, 100, 70, 0.05, -200)   # Moderate curve
SEGMENT20 = (30, 50, 35, 0.2, 350)      # Very steep uphill, tight turn
SEGMENT21 = (50, 90, 60, -0.06, 0)      # Steep downhill straight
SEGMENT22 = (40, 80, 55, 0.03, 150)     # Slight curve uphill
SEGMENT23 = (60, 100, 75, 0, 0)         # Flat, straight road
SEGMENT24 = (30, 60, 40, -0.1, -200)    # Steep downhill with sharp turn
SEGMENT25 = (50, 130, 90, 0.01, 0)      # Long, fast, flat straight

SEGMENTS = [SEGMENT1, SEGMENT2, SEGMENT3, SEGMENT4, SEGMENT5, SEGMENT6, SEGMENT7, SEGMENT8, SEGMENT9, SEGMENT10,
            SEGMENT11, SEGMENT12, SEGMENT13, SEGMENT14, SEGMENT15, SEGMENT16, SEGMENT17, SEGMENT18, SEGMENT19,
            SEGMENT20, SEGMENT21, SEGMENT22, SEGMENT23, SEGMENT24, SEGMENT25]
