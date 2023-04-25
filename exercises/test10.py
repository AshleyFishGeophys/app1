def get_max_min():
    grades = [9.6, 9.2, 9.7]
    return max(grades), min(grades)

max_val, min_val = get_max_min()

print(f"Max: {max_val}, Min: {min_val}")
