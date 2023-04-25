FREEZING_POINT = 0
BOILING_POINT = 100


def water_state(temp):
    if temp <= FREEZING_POINT:
        return "Solid"
    elif FREEZING_POINT < temp < BOILING_POINT:
        return "Liquid"
    else:
        return "Gas"
