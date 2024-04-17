def month_to_season(mouth_number = int):
    if (mouth_number == 12) or (mouth_number == 1) or (mouth_number == 2):
        result = 'Зима'
    elif (mouth_number == 3) or (mouth_number == 4) or (mouth_number == 5):
        result = 'Весна'
    elif (mouth_number == 6) or (mouth_number == 7) or (mouth_number == 8):
        result = 'Лето'
    else:
        result = 'Осень'  
    return result

print(month_to_season(4))             


