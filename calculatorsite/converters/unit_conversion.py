from decimal import Decimal

#Length Converter
def length_converter(first_unit, second_unit, value):
    try:
        if(first_unit == second_unit):
            return value + ' ' + second_unit
        if(value == '0'):
            return '0' + ' ' + second_unit
        SI_units = {
                    'pm': 1e12,
                    'nm': 1e9,
                    'μm': 1e6,
                    'mm': 1e3,
                    'cm': 1e2,
                    'dm': 1e1,
                   'guz': 1.0989, 
                     'm': 1e0,
                    'km': 1e-3,
                    'pc': 3.24077e-17,
                    'ly': 1.057e-16,
                    'AU': 6.6846e-12,
                    'LD': 2.6041e-8,
                   'fur': 0.004971,
                    'fm': 0.5468066,
                    'yd': 1.0936133,
                   'nmi': 0.00054,
                    'ft': 3.2808399,
                    'mi': 0.0006214,
                    'in': 39.3700787
                }

        calc =  float(value) * (SI_units[second_unit] / SI_units[first_unit]) 
        if calc > 1e5 or calc < 1e-5:
            return str(f"{Decimal(calc):.2E}") + ' ' + second_unit
        else:
            return str(calc) + ' ' + second_unit
    except:
        error = {
            'error': 'Length value is invalid'
        }
        return error


#Temperature Converter
def temperature_converter(first_unit, second_unit, value):
    try:
        if(first_unit == second_unit):
            return value + ' ' + second_unit

        value = float(value)
        calc = {}

        if first_unit == '°C':
            calc = {
                '°F': value * 1.80 + 32,
                 'K': value + 273.15,
                '°R': (value + 273.15) * 1.80,
               '°Re': value * 0.80,
               '°De': (100 - value) * 1.50,
                '°N': value * 0.33,
               '°Rø': value * 0.5250 + 7.5
            }
        elif first_unit == '°F':
            calc = {
                '°C': (value - 32) * 0.5556,
                 'K': (value + 459.67) * 0.5556,
                '°R': value + 459.67,
               '°Re': (value - 32) * 0.4444,
               '°De': (212 - value) * 0.8333,
                '°N': (value - 32) * 0.1833,
               '°Rø': (value - 32) * 0.2917 + 7.5               
            }
        elif first_unit == 'K':
            calc = {
                '°C': value - 273.15,
                '°F': (value * 1.8000) - 459.67,
                '°R': value * 1.8000,
               '°Re': (value - 273.15) * 0.8000,
               '°De': (373.15 - value) * 1.5000,
                '°N': (value - 273.15) * 0.33,
               '°Rø': (value - 273.15) * 0.5250 + 7.5   
            }
        elif first_unit == '°R':
            cal = {
                '°C': (value-491.67)*0.5556,
                '°F': value - 459.67,
                 'K': value * 0.5556,
               '°Re': (value - 491.67) * 0.4444,
               '°De': (671.67 - value) * 0.8333,
                '°N': (value - 491.67) * 0.1833,
               '°Rø': (value - 491.67) * 0.2917 + 7.5                
            }
        elif first_unit == '°De':
            cal = {
                '°C': 100 - value * 0.6667,
                '°F': 212 - value * 1.2000,
                 'K': 373.15 - value * 0.6667,
               '°Re': 80 - value * 0.5333,
                '°R': 671.67- value * 1.2000,
                '°N': 33 - value * 0.2200,
               '°Rø': 60 - value * 0.3500              
            }
        elif first_unit == '°N':
            calc = {
                '°C': value * 3.0303,
                '°F': value * 5.4545 + 32,
                 'K': value * 3.0303 + 273.15,
               '°Re': value * 2.4242,
                '°R': value * 5.4545 + 491.67,
               '°De': (33 - value) * 4.5455,
               '°Rø': value * 1.5909 + 7.5                     
            }     
        elif first_unit == '°Re':
            calc = {
                '°C': value * 1.2500,
                '°F': value * 2.2500 + 32,
                 'K': value * 1.2500 + 273.15,
                '°N': value * 0.4125,
                '°R': value * 2.2500 + 491.67,
               '°De': (80 - value) * 1.8750,
               '°Rø':  value * 0.6563 + 7.5         
            }  
        elif first_unit == '°Rø':
            calc = {
                '°C': (value - 7.5) * 1.9048,
                '°F': (value - 7.5) * 3.4286 + 32,
                 'K': (value - 7.5) * 1.9048 + 273.15,
                '°N': (value - 7.5) * 0.6286,
                '°R': (value - 7.5) * 3.4286 + 491.67,
               '°De': (60 - value) * 2.8571,
               '°Re': (value - 7.5) * 1.5238          
            }      

        result = str(calc[second_unit]) + ' ' + second_unit

        return result
    except:
        error = {
            'error': 'Temperature value is invalid'
        }
        return error


#Area Conversion
def area_converter(first_unit, second_unit, value):
    try:
        if(first_unit == second_unit):
            return value + ' ' + second_unit
        if(value == '0'):
            return '0' + ' ' + second_unit
        SI_units = {
                    'm²': 1.00,
                    'ha': 1e-4,
                   'dm²': 1e2,
                   'cm²': 1e4,
                   'km²': 1e-6,
                   'mm²': 1e6,
                    'ar': 0.01,
                   'mi²': 3.861e-7,
                   'rd²': 0.0395369,
                   'yd²': 1.19599,
                   'ft²': 10.7639104,
                    'ac': 0.0002471,
                   'in²': 1550.0031
                }

        calc =  float(value) * (SI_units[second_unit] / SI_units[first_unit]) 
        if calc > 1e5 or calc < 1e-5:
            return str(f"{Decimal(calc):.2E}") + ' ' + second_unit
        else:
            return str(calc) + ' ' + second_unit
    except:
        error = {
            'error': 'Area value is invalid'
        }
        return error


#Weight Conversion
def weight_converter(first_unit, second_unit, value):
    try:
        if(first_unit == second_unit):
            return value + ' ' + second_unit
        if(value == '0'):
            return '0' + ' ' + second_unit
        SI_units = {
                    'g': 1.00,
                    't': 1e-6,
                   'μg': 1e6,
                    'q': 1e-5,
                   'ct': 5,
                   'mg': 1e3,
                   'kg': 1e-3,
                   'st': 0.0000011023,
                   'lt': 9.842e-7,
                   'oz': 0.0352739619,
                   'gr': 15.4323583529,
                   'dr': 0.5643833912,
               'sh cwt': 0.0000220462,
                   'lb': 0.0022046226,
                   'st': 0.000157473,
               'lg cwt': 0.0000196841
                }

        calc =  float(value) * (SI_units[second_unit] / SI_units[first_unit]) 
        if calc > 1e5 or calc < 1e-5:
            return str(f"{Decimal(calc):.2E}") + ' ' + second_unit
        else:
            return str(calc) + ' ' + second_unit
    except:
        error = {
            'error': 'Weight value is invalid'
        }
        return error

#Power Conversion
def power_converter(first_unit, second_unit, value):
    try:
        if(first_unit == second_unit):
            return value + ' ' + second_unit
        if(value == '0'):
            return '0' + ' ' + second_unit
        SI_units = {
                    'W': 1,
                  'J/s': 1,
                'Btu/s': 0.0009478171,
                   'PS': 0.0013596216,
               'kg·m/s': 0.1019716213,
               'kcal/s': 0.000239,
                   'hp': 0.0013410221,
              'ft·lb/s': 0.7375621489,
                'N·m/s': 1,
                   'kW': 0.001
                }

        calc =  float(value) * (SI_units[second_unit] / SI_units[first_unit]) 
        if calc > 1e5 or calc < 1e-5:
            return str(f"{Decimal(calc):.2E}") + ' ' + second_unit
        else:
            return str(calc) + ' ' + second_unit
    except:
        error = {
            'error': 'Power value is invalid'
        }
        return error

#Power Conversion
def pressure_converter(first_unit, second_unit, value):
    try:
        if(first_unit == second_unit):
            return value + ' ' + second_unit
        if(value == '0'):
            return '0' + ' ' + second_unit
        SI_units = {
                'bar': 1,
              'mmH2O': 10197.16,
                'psf': 2088.543512,
            'kgf/cm²': 1.0197,
                'psi': 14.503774,
               'mmHg': 750.0617,
               'inHg': 29.53,
               'mbar': 1000,
                'hPa': 1000,
                'atm': 0.986923,
                'kPa': 100,
             'kgf/m²': 10197.1621,
                'MPa': 0.1
                }

        calc =  float(value) * (SI_units[second_unit] / SI_units[first_unit]) 
        if calc > 1e5 or calc < 1e-5:
            return str(f"{Decimal(calc):.2E}") + ' ' + second_unit
        else:
            return str(calc) + ' ' + second_unit
    except:
        error = {
            'error': 'Pressure value is invalid'
        }
        return error

#Power Conversion
def frequency_converter(first_unit, second_unit, value):
    try:
        if(first_unit == second_unit):
            return value + ' ' + second_unit
        if(value == '0'):
            return '0' + ' ' + second_unit
        SI_units = {
                'Hz': 1,
               'kHz': 1e-3,
               'MHz': 1e-6,
               'GHz': 1e-9,
               'THz': 1e-12,
               'PHz': 1e-15,
               'EHz': 1e-18,
               'ZHz': 1e-21,
               'YHz': 1e-24 
            }

        calc =  float(value) * (SI_units[second_unit] / SI_units[first_unit]) 
        if calc > 1e5 or calc < 1e-5:
            return str(f"{Decimal(calc):.2E}") + ' ' + second_unit
        else:
            return str(calc) + ' ' + second_unit
    except:
        error = {
            'error': 'Frequency value is invalid'
        }
        return error

#Speed Conversion
def speed_converter(first_unit, second_unit, value):
    try:
        if(first_unit == second_unit):
            return value + ' ' + second_unit
        if(value == '0'):
            return '0' + ' ' + second_unit
        SI_units = {
                'km/s': 1,
                   'c': 0.0000033356,
                 'mph': 2236.936,
                  'Ma': 2.9386,
                'in/s': 39370.079,
                 'm/s': 1000,
                'km/h': 3600
            }

        calc =  float(value) * (SI_units[second_unit] / SI_units[first_unit]) 
        if calc > 1e5 or calc < 1e-5:

            return str(f"{Decimal(calc):.2E}") + ' ' + second_unit
        else:
            return str(calc) + ' ' + second_unit
    except:
        error = {
            'error': 'Speed value is invalid'
        }
        return error

#Volume Conversion
def volume_converter(first_unit, second_unit, value):
    try:
        if(first_unit == second_unit):
            return value + ' ' + second_unit
        if(value == '0'):
            return '0' + ' ' + second_unit
        SI_units = {
                 'l': 1.00,
                'hl': 0.01,
                'm³': 0.001,
               'cm³': 1000.0,
                'dl': 10.0,
                'cl': 100.0,
               'dm³': 1.00,
               'mm³': 1e6,
                'ml': 1000.0,
               'ft³': 0.0353147248,
          'US fl oz': 34.1646737274,
               'yd³': 0.0013079528,
               'in³': 61.0238445022,
               'af³': 8.107e-7,
            'UK gal': 0.2199691573,
            'US gal': 0.2641720524,
          'UK fl oz': 35.198873636
        }

        calc =  float(value) * (SI_units[second_unit] / SI_units[first_unit]) 
        if calc > 1e5 or calc < 1e-5:

            return str(f"{Decimal(calc):.2E}") + ' ' + second_unit
        else:
            return str(calc) + ' ' + second_unit
    except:
        error = {
            'error': 'Volume value is invalid'
        }
        return error
