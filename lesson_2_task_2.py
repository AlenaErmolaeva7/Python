
def is_year_leap (year=int):
    if year % 4 == 0:
         return True
    else:
        return False
print(is_year_leap(2012))

def new_is_year_leap(year=int):
    if year % 4 == 0:
        result = True
    else:
        result = False    
    return(f'год {year}: {result}')
print(new_is_year_leap(2024))

      