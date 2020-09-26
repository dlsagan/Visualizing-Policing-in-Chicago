import pandas as pd

def school_survey_cleaner(series):

    if series == 'VERY WEAK':
        return 1

    elif series == 'WEAK':
        return 2

    elif series == 'NEUTRAL':
        return 3

    elif series == 'STRONG':
        return 4
    
    elif series == 'VERY STRONG':
        return 5

    else:
        return 0

def school_growth_cleaner(series):

    if series == 'FAR BELOW AVERAGE':
        return 1

    elif series == 'BELOW AVERAGE':
        return 2

    elif series == 'AVERAGE':
        return 3

    elif series == 'ABOVE AVERAGE':
        return 4

    elif series == 'FAR ABOVE AVERAGE':
        return 5

    else:
        return 0
