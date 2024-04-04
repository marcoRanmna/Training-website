
def calculate_bmr(weight, height, age, gender, training_difficulty):
    if gender == 'male':
        bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    elif gender == 'female':
        bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
    else:
        raise ValueError("Invalid gender. Gender must be 'male' or 'female'.")
    
    if training_difficulty == 'sedentary':
        bmr *= 1.2
    elif training_difficulty =='lightly_active':
        bmr *= 1.375
    elif training_difficulty =='moderately_active':
        bmr *= 1.55
    elif training_difficulty =='very_active':
        bmr *= 1.725
    elif training_difficulty == 'extra_active':
        bmr *= 1.9

    return bmr
