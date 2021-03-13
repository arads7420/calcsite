#Decimal to Binary
def decimal_to_binary(num):
    try:
        num = int(num)
        if num < 0:
            return 'Must be a positive integer'
        elif num == 0:
            return '0'
        else:
            return str(decimal_to_binary(num // 2) + str(num % 2)).lstrip('0')
    except:
        error = {
            'error': 'Decimal value is invalid'
        }
        return error


#Decimal to Octal
def decimal_to_octal(num):
    try:
        num = int(num)
        if num < 0:
            return 'Must be a positive integer'
        elif num == 0:
            return '0'
        else:
            return str(decimal_to_octal(num // 8) + str(num % 8)).lstrip('0')
    except:
        error = {
            'error': 'Decimal value is invalid'
        }
        return error

#Decimal to Hexadecimal
def decimal_to_hexadecimal(num):
    try:
        num = int(num)
        if num == 0:
            return '0'
        else:
            return hex(num).strip('0x').upper()
    except:
        error = {
            'error': 'Decimal value is invalid'
        }
        return error

# result = decimal_to_hexadecimal('0')
# print(result)

def decimal_to_binary_octal_hex(num):
    try:
        binary = decimal_to_binary(num)
        octal = decimal_to_octal(num)
        hexa = decimal_to_hexadecimal(num)
        values = [binary, octal, hexa]
        if not 'error' in binary and not 'error' in octal and not 'error' in hexa:
            result = {
                'binary': binary,
                'octal': octal,
                'hexa': hexa
            }
            return result
        else:
            error = {
                'error': 'Decimal value is invalid'
            }
            return error
    except: 
        error = {
            'error': 'Decimal value is invalid'
        }
        return error


# result = decimal_to_hexadecimal('34t2')
# print(result['error'])


#Binary to Decimal
def binary_to_decimal(num):
    try:
        if num == '0':
            return '0'
        decimal = 0
        power = len(str(num)) - 1
        for c in str(num):
            if c == '0' or c == '1':
                decimal += int(c) * (2 ** power)
                power -= 1
            else:
                error = {
                    'error': "A binary number cannot have values other than 0 or 1"
                }
                return error

        return str(decimal).lstrip('0')
    except:
        error = {
            'error': 'Binary value is invalid'
        }
        return error

#Octal to Decimal
def octal_to_decimal(num):
    try:
        if num == '0':
            return '0'
        octal = 0
        power = len(str(num)) - 1
        for c in str(num):
            octal += int(c) * (8 ** power)
            power -= 1
        return str(octal).lstrip('0')
    except:
        error = {
            'error': 'Octal value is invalid'
        }
        return error

# result = octal_to_decimal('342')
# print(result)

#Hexadecimal to Decimal
def hex_to_decimal(num):
    try: 
        num = str(num)
        hexa = 0
        power = len(num) - 1
        for c in str(num):
            c = c.upper()
            if c == 'A':
                c = 10
            elif c == 'B':
                c = 11
            elif c == 'C':
                c = 12
            elif c == 'D':
                c = 13
            elif c == 'E':
                c = 14
            elif c == 'F':
                c = 15
            hexa += int(c) * (16 ** power)
            power -= 1
        if hexa == 0:
            return str(hexa)
        else:
            return str(hexa).lstrip('0')
    except:
        error = {
            'error': 'Hexadecimal value is invalid'
        }
        return error


#Decimal to arbitrary base
def decimal_to_base(num, base):
    num = int(num)
    base = int(base)
    try:
        if num < 0:
            return 'Must be a positive integer'
        elif num == 0:
            return '0'
        else:
            return decimal_to_base(num // base, base) + str(num % base)
    except:
        error = {
            'error': 'Decimal value is invalid'
        }
        return error


#Convert decimal to fraction
def decimal_to_fraction(dec):
    try:
        from fractions import Fraction
        return Fraction(dec).limit_denominator()
    except:
        error = {
            'error': 'Decimal value is invalid'
        }
        return error

#Convert Decimal to Percentage
def decimal_to_percent(dec):
    try:
        return str(float(dec) * 100) + '%'
    except:
        error = {
            'error': 'Decimal value is invalid'
        }
        return error

#Convert Percentage to Decimal
def percent_to_decimal(dec):
    try:
        dec = dec.strip('%')
        return str(float(float(dec) / 100)) 
    except:
        error = {
            'error': 'Percentage value is invalid'
        }
        return error

#Degrees to deg, min, sec
def deg_to_dms(dec):
    try:
        dec = float(dec.strip('°'))
        degrees = int(dec)
        minutes = abs(int(round((abs(dec) - abs(float(degrees))) * 60, 9)))
        seconds = format(abs((abs(dec) - abs(float(degrees)) - (abs(minutes) / 60)) * 3600), '.2f')
        dms = {
            'deg': str(degrees) + "°",
            'min': str(minutes) + "′" , 
            'sec': str(seconds) + "″"
        }
        return dms
    except:
        error = {
            'error': "Value of degree is invalid"
        }
        return error



# result = deg_to_dms('521.4440')
# print(result)

#dms to degree
def dms_to_degree(deg, m, s):
    try:
        if deg == '': deg = '0'
        if m == '': m = '0'
        if s == '': s = '0'

        deg = format(float(deg.strip('°')), '.5f')
        m = format(float(m.strip('′')), '.5f')
        s = format(float(s.strip('″')), '.5f')
        if float(deg) < 0 or float(m) < 0 or float(s) < 0:
            return '-' + format(abs(float(deg)) + abs(float(m) / 60) + abs(float(s) / 3600), '.5f') + '°'
        else:
            return format(abs(float(deg)) + abs(float(m) / 60) + abs(float(s) / 3600), '.5f') + "°"
            
    except:
        error = {
            'error': "Check the values again"
        }
        return error
    
def octal_to_binary(octal):
    try:
        decimal_val = octal_to_decimal(octal)
        binary_val = decimal_to_binary(decimal_val)
        if not 'error' in decimal_val and not 'error' in binary_val:
            return binary_val
        else:
            error = {
                'error': 'Octal value is invalid'
            }
            return error
    except:
        error = {
            'error': 'Octal value is invalid'
        }
        return error
    
def binary_to_octal(binary):
    try:
        decimal_val = binary_to_decimal(binary)
        octal_val = decimal_to_octal(decimal_val)
        if not 'error' in decimal_val and not 'error' in octal_val:
            return octal_val
        else:
            error = {
                'error': 'Binary value is invalid'
            }
            return error
    except:
        error = {
            'error': 'Binary value is invalid'
        }
        return error

    
def hex_to_binary(hexa):
    try:
        decimal_val = hex_to_decimal(hexa)
        binary_val = decimal_to_binary(decimal_val)
        if not 'error' in decimal_val and not 'error' in binary_val:
            return binary_val
        else:
            error = {
                'error': 'Hexadecimal value is invalid'
            }
            return error
    except:
        error = {
            'error': 'Hexadecimal value is invalid'
        }
        return error

# result = hex_to_binary('0')
# print(result)

    
def binary_to_hex(binary):
    try:
        if binary == '0':
            return '0'
        decimal_val = binary_to_decimal(binary)
        hex_val = decimal_to_hexadecimal(decimal_val)
        if not 'error' in decimal_val and not 'error' in hex_val:
            return hex_val
        else:
            error = {
                'error': 'Binary value is invalid'
            }
            return error
    except:
        error = {
            'error': 'Binary value is invalid'
        }
        return error



# result = deg_to_dms('34.684')
# print(result)

#1. Age Calculator
#2. BMI Calculator
#3. Time Calculator
#4. Investment Calculator
#5. Calorie Calculator 

#Age Calculator
def age_calculate(dob, other_date):
    try:
        from datetime import date
        d0 = date(dob['year'], dob['month'], dob['day'])
        d1 = date(other_date['year'], other_date['month'], other_date['day'])
        delta = d1 - d0
        return delta.days
    except:
        error = {
            'error': 'Age value is invalid'
        }
        return error
# d0 = {
#     'year': 2000, 
#     'month': 4,
#     'day': 7
# }
# d1 = {
#     'year': 2010, 
#     'month': 8,
#     'day': 2
# }

# result = age_calculate(d0, d1)
# print(result)

