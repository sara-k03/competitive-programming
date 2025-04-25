
def sign( month, day ):
    month = month.lower()
    
    if month == 'mar':
        if day >= 21:
            return 'Aries'
        else:
            return 'Pisces'
    elif month == 'apr':
        if day <= 20:
            return 'Aries'
        else:
            return 'Taurus'
    elif month == 'may':
        if day <= 20:
            return 'Taurus'
        else:
            return 'Gemini'
    elif month == 'jun':
        if day <= 21:
            return 'Gemini'
        else:
            return 'Cancer'
    elif month == 'jul':
        if day <= 22:
            return 'Cancer'
        else:
            return 'Leo'
    elif month == 'aug':
        if day <= 22:
            return 'Leo'
        else:
            return 'Virgo'
    elif month == 'sep':
        if day <= 21:
            return 'Virgo'
        else:
            return 'Libra'
    elif month == 'oct':
        if day <= 22:
            return 'Libra'
        else:
            return 'Scorpio'
    elif month == 'nov':
        if day <= 22:
            return 'Scorpio'
        else:
            return 'Sagittarius'
    elif month == 'dec':
        if day <= 21:
            return 'Sagittarius'
        else:
            return 'Capricorn'
    elif month == 'jan':
        if day <= 20:
            return 'Capricorn'
        else:
            return 'Aquarius'
    elif month == 'feb':
        if day <= 19:
            return 'Aquarius'
        else:
            return 'Pisces'
    else:
        return ''

n = int(input())

for i in range(n):
    inputs = input().split(' ')
    day = int(inputs[0])
    month = inputs[1]
    
    print(sign(month, day))