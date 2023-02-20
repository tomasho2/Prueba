def convert_gender(gender: str):
    gender = gender.upper()
    if gender == "M":
        return "Male"
    elif gender == "F":
        return "Female"
    else:
        return "Unkown gender"
