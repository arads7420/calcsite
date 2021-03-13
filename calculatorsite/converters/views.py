from django.shortcuts import render
from .forms import DecimalInput
from .forms import OctalInput
from .forms import HexInput
from .forms import BinaryInput
from .forms import DegMinSecInput
from .forms import DecimalInput_Base
from .forms import DegreeInput
from .forms import LengthInput
from .forms import TempInput
from .forms import AreaInput
from .forms import WeightInput
from .forms import PowerInput
from .forms import PercentInput
from .forms import FrequencyInput
from .forms import VolumeInput
from .forms import PressureInput
from .forms import SpeedInput
from . import base_conversion as base_conv
from . import unit_conversion as unit_conv


# Create your views here.
base_site_name = 'Calculator Swift'
def converters(request): 
    context = {
        'title': base_site_name + '| Converters',
    }
    return render(request, 'converters.html', context)

def numberbaseconversion(request): 
    context = {
        'title':  'Number Base Converters',
    }
    return render(request, 'baseconversion.html', context)

def decimal_to_bin_octal_hex(request):
    title = 'Converters | Decimal to Binary, Octal and Hexadecimal Converter'
    if request.method == 'POST':
        form = DecimalInput(request.POST)
        if form.is_valid():
            decimal_input = form.cleaned_data['decimal_input']
            result = base_conv.decimal_to_binary_octal_hex(decimal_input)
            context = {
                'form': form,
                'title': title,
                'data': {
                    'result': result
                }
            }
            return render(request, 'decimal-to-binary-octal-hexadecimal.html', context)
        else:
            error = {
                'error': "Input field can't be empty"
            }
            context = {
                'title': title,
                'form': form,
                'data': {
                    'result': error
                }
            }
            return render(request, 'decimal-to-binary-octal-hexadecimal.html', context)

    else:
        form = DecimalInput()
        context = {
            'title': title,
            'form': form
        }
        return render(request, 'decimal-to-binary-octal-hexadecimal.html', context)


def decimal_to_any_base(request):
    title = 'Decimal to Any Base Converter'
    if request.method == 'POST':
        form = DecimalInput_Base(request.POST)
        if form.is_valid():
            decimal_input = form.cleaned_data['decimal_input']
            base_input = form.cleaned_data['base_input']

            result = base_conv.decimal_to_base(decimal_input, base_input)

            context = {
                'title': title,
                'form': form,
                'data': {
                    'result': result
                }
            }
            return render(request, 'decimal-to-any-base.html', context)
        else:
            error = {
                'error': "Input field can't be empty"
            }
            context = {
                'title': title,
                'form': form,
                'data': {
                    'result': error
                }
            }
            return render(request, 'decimal-to-any-base.html', context)
    else:
        form = DecimalInput_Base()
        context = {
            'title': title,
            'form': form
        }
        return render(request, 'decimal-to-any-base.html', context)

def decimal_to_octal(request):
    title = 'Decimal to Octal Converter'
    if request.method == 'POST':
        form = DecimalInput(request.POST)
        if form.is_valid():
            decimal_input = form.cleaned_data['decimal_input']

            result = base_conv.decimal_to_octal(decimal_input)

            context = {
                'title': title,
                'form': form,
                'data': {
                    'result': result
                }
            }
            return render(request, 'decimal-to-octal.html', context)
        else:
            error = {
                'error': "Input field can't be empty"
            }
            context = {
                'title': title,
                'form': form,
                'data': {
                    'result': error
                }
            }
            return render(request, 'decimal-to-octal.html', context)
    else:
        form = DecimalInput()
        context = {
            'title': title,
            'form': form
        }
        return render(request, 'decimal-to-octal.html', context)

def octal_to_decimal(request):
    title = 'Octal to Decimal Converter'
    if request.method == 'POST':
        form = OctalInput(request.POST)
        if form.is_valid():
            octal_input = form.cleaned_data['octal_input']

            result = base_conv.octal_to_decimal(octal_input)

            context = {
                'title': title,
                'form': form,
                'data': {
                    'result': result
                }
            }
            return render(request, 'octal-to-decimal.html', context)
        else:
            error = {
                'error': "Input field can't be empty"
            }
            context = {
                'title': title,
                'form': form,
                'data': {
                    'result': error
                }
            }
            return render(request, 'octal-to-decimal.html', context)
    else:
        form = OctalInput()
        context = {
            'title': title,
            'form': form
        }
        return render(request, 'octal-to-decimal.html', context)

def decimal_to_hexadecimal(request):
    title = 'Decimal to Hexadecimal Converter'
    if request.method == 'POST':
        form = DecimalInput(request.POST)
        if form.is_valid():
            decimal_input = form.cleaned_data['decimal_input']

            result = base_conv.decimal_to_hexadecimal(decimal_input)

            context = {
                'title': title,
                'form': form,
                'data': {
                    'result': result
                }
            }
            return render(request, 'decimal-to-hexadecimal.html', context)
        else:
            error = {
                'error': "Input field can't be empty"
            }
            context = {
                'title': title,
                'form': form,
                'data': {
                    'result': error
                }
            }
            return render(request, 'decimal-to-hexadecimal.html', context)
    else:
        form = DecimalInput()
        context = {
            'title': title,
            'form': form
        }
        return render(request, 'decimal-to-hexadecimal.html', context)

def hexadecimal_to_decimal(request):
    title = 'Hexadecimal to Decimal Converter'
    if request.method == 'POST':
        form = HexInput(request.POST)
        if form.is_valid():
            hex_input = form.cleaned_data['hex_input']

            result = base_conv.hex_to_decimal(hex_input)

            context = {
                'title': title,
                'form': form,
                'data': {
                    'result': result
                }
            }
            return render(request, 'hexadecimal-to-decimal.html', context)
        else:
            error = {
                'error': "Input field can't be empty"
            }
            context = {
                'title': title,
                'form': form,
                'data': {
                    'result': error
                }
            }
            return render(request, 'hexadecimal-to-decimal.html', context)
    else:
        form = HexInput()
        context = {
            'title': title,
            'form': form
        }
        return render(request, 'hexadecimal-to-decimal.html', context)

def binary_to_decimal(request):
    title = 'Binary to Decimal Converter'
    if request.method == 'POST':
        form = BinaryInput(request.POST)
        if form.is_valid():
            binary_input = form.cleaned_data['binary_input']

            result = base_conv.binary_to_decimal(binary_input)

            context = {
                'title': title,
                'form': form,
                'data': {
                    'result': result
                }
            }
            return render(request, 'binary-to-decimal.html', context)
        else:
            error = {
                'error': "Input field can't be empty"
            }
            context = {
                'title': title,
                'form': form,
                'data': {
                    'result': error
                }
            }
            return render(request, 'binary-to-decimal.html', context)
    else:
        form = BinaryInput()
        context = {
            'title': title,
            'form': form
        }
        return render(request, 'binary-to-decimal.html', context)


def decimal_to_binary(request):
    title = 'Decimal to Binary Converter'
    if request.method == 'POST':
        form = DecimalInput(request.POST)
        if form.is_valid():
            decimal_input = form.cleaned_data['decimal_input']

            result = base_conv.decimal_to_binary(decimal_input)

            context = {
                'title': title,
                'form': form,
                'data': {
                    'result': result
                }
            }
            return render(request, 'decimal-to-binary.html', context)
        else:
            error = {
                'error': "Input field can't be empty"
            }
            context = {
                'title': title,
                'form': form,
                'data': {
                    'result': error
                }
            }
            return render(request, 'decimal-to-binary.html', context)
    else:
        form = DecimalInput()
        context = {
            'title': title,
            'form': form
        }
        return render(request, 'decimal-to-binary.html', context)

def decimal_to_fraction(request):
    title = 'Decimal to Fraction Converter'
    if request.method == 'POST':
        form = DecimalInput(request.POST)
        if form.is_valid():
            decimal_input = form.cleaned_data['decimal_input']

            result = base_conv.decimal_to_fraction(decimal_input)

            context = {
                'title': title,
                'form': form,
                'data': {
                    'result': result
                }
            }
            return render(request, 'decimal-to-fraction.html', context)
        else:
            error = {
                'error': "Input field can't be empty"
            }
            context = {
                'title': title,
                'form': form,
                'data': {
                    'result': error
                }
            }
            return render(request, 'decimal-to-fraction.html', context)
    else:
        form = DecimalInput()
        context = {
            'title': title,
            'form': form
        }
        return render(request, 'decimal-to-fraction.html', context)

def decimal_to_percentage(request):
    title = 'Decimal to Percentage Converter'
    if request.method == 'POST':
        form = DecimalInput(request.POST)
        if form.is_valid():
            decimal_input = form.cleaned_data['decimal_input']

            result = base_conv.decimal_to_percent(decimal_input)

            context = {
                'title': title,
                'form': form,
                'data': {
                    'result': result
                }
            }
            return render(request, 'decimal-to-percentage.html', context)
        else:
            error = {
                'error': "Input field can't be empty"
            }
            context = {
                'title': title,
                'form': form,
                'data': {
                    'result': error
                }
            }
            return render(request, 'decimal-to-percentage.html', context)
    else:
        form = DecimalInput()
        context = {
            'title': title,
            'form': form
        }
        return render(request, 'decimal-to-percentage.html', context)

def percentage_to_decimal(request):
    title = 'Percentage to Decimal Converter'
    if request.method == 'POST':
        form = PercentInput(request.POST)
        if form.is_valid():
            percent_input = form.cleaned_data['percent_input']

            result = base_conv.percent_to_decimal(percent_input)

            context = {
                'title': title,
                'form': form,
                'data': {
                    'result': result
                }
            }
            return render(request, 'percentage-to-decimal.html', context)
        else:
            error = {
                'error': "Input field can't be empty"
            }
            context = {
                'title': title,
                'form': form,
                'data': {
                    'result': error
                }
            }
            return render(request, 'percentage-to-decimal.html', context)
    else:
        form = PercentInput()
        context = {
            'title': title,
            'form': form
        }
        return render(request, 'percentage-to-decimal.html', context)

def deg_to_dms(request):
    title = 'Decimal Degrees to Degrees, Minutes and Seconds Converter'
    if request.method == 'POST':
        form = DegreeInput(request.POST)
        if form.is_valid():
            degree_input = form.cleaned_data['degree_input']

            result = base_conv.deg_to_dms(degree_input)

            context = {
                'title': title,
                'form': form,
                'data': {
                    'result': result
                }
            }
            return render(request, 'degree-to-dms.html', context)
        else:
            error = {
                'error': "Input field can't be empty"
            }
            context = {
                'title': title,
                'form': form,
                'data': {
                    'result': error
                }
            }
            return render(request, 'degree-to-dms.html', context)
    else:
        form = DegreeInput()
        context = {
            'title': title,
            'form': form
        }
        return render(request, 'degree-to-dms.html', context)

def dms_to_deg(request):
    title = 'Degrees, Minutes and Seconds to Decimal Degrees Converter'
    if request.method == 'POST':
        form = DegMinSecInput(request.POST)
        if form.is_valid():
            deg_input = form.cleaned_data['deg_input']
            min_input = form.cleaned_data['min_input']
            sec_input = form.cleaned_data['sec_input']

            result = base_conv.dms_to_degree(deg_input, min_input, sec_input)

            context = {
                'title': title,
                'form': form,
                'data': {
                    'result': result
                }
            }
            return render(request, 'dms-to-degree.html', context)
        else:
            error = {
                'error': "Input field can't be empty"
            }
            context = {
                'title': title,
                'form': form,
                'data': {
                    'result': error
                }
            }
            return render(request, 'dms-to-degree.html', context)
    else:
        form = DegMinSecInput()
        context = {
            'title': title,
            'form': form
        }
        return render(request, 'dms-to-degree.html', context)

def octal_to_binary(request):
    title = 'Octal to Binary Converter'
    if request.method == 'POST':
        form = OctalInput(request.POST)
        if form.is_valid():
            octal_input = form.cleaned_data['octal_input']

            result = base_conv.octal_to_binary(octal_input)

            context = {
                'title': title,
                'form': form,
                'data': {
                    'result': result
                }
            }
            return render(request, 'octal-to-binary.html', context)
        else:
            error = {
                'error': "Input field can't be empty"
            }
            context = {
                'title': title,
                'form': form,
                'data': {
                    'result': error
                }
            }
            return render(request, 'octal-to-binary.html', context)
    else:
        form = OctalInput()
        context = {
            'title': title,
            'form': form
        }
        return render(request, 'octal-to-binary.html', context)

def binary_to_octal(request):
    title = 'Binary to Octal Converter'
    if request.method == 'POST':
        form = BinaryInput(request.POST)
        if form.is_valid():
            binary_input = form.cleaned_data['binary_input']

            result = base_conv.binary_to_octal(binary_input)

            context = {
                'title': title,
                'form': form,
                'data': {
                    'result': result
                }
            }
            return render(request, 'binary-to-octal.html', context)
        else:
            error = {
                'error': "Input field can't be empty"
            }
            context = {
                'title': title,
                'form': form,
                'data': {
                    'result': error
                }
            }
            return render(request, 'binary-to-octal.html', context)
    else:
        form = BinaryInput()
        context = {
            'title': title,
            'form': form
        }
        return render(request, 'binary-to-octal.html', context)

def hex_to_binary(request):
    title = 'Hexadecimal to Binary Converter'
    if request.method == 'POST':
        form = HexInput(request.POST)
        if form.is_valid():
            hex_input = form.cleaned_data['hex_input']

            result = base_conv.hex_to_binary(hex_input)

            context = {
                'title': title,
                'form': form,
                'data': {
                    'result': result
                }
            }
            return render(request, 'hexadecimal-to-binary.html', context)
        else:
            error = {
                'error': "Input field can't be empty"
            }
            context = {
                'title': title,
                'form': form,
                'data': {
                    'result': error
                }
            }
            return render(request, 'hexadecimal-to-binary.html', context)
    else:
        form = HexInput()
        context = {
            'title': title,
            'form': form
        }
        return render(request, 'hexadecimal-to-binary.html', context)

def binary_to_hex(request):
    title = 'Binary to Hexadecimal Converter'
    if request.method == 'POST':
        form = BinaryInput(request.POST)
        if form.is_valid():
            binary_input = form.cleaned_data['binary_input']
    
            result = base_conv.binary_to_hex(binary_input)

            context = {
                'title': title,
                'form': form,
                'data': {
                    'result': result
                }
            }
            return render(request, 'binary-to-hexadecimal.html', context)
        else:
            error = {
                'error': "Input field can't be empty"
            }
            context = {
                'title': title,
                'form': form,
                'data': {
                    'result': error
                }
            }
            return render(request, 'binary-to-hexadecimal.html', context)
    else:
        form = BinaryInput()
        context = {
            'title': title,
            'form': form
        }
        return render(request, 'binary-to-hexadecimal.html', context)


def length_conversion(request):
    title = 'Length Conversion'
    if request.method == 'POST':
        form = LengthInput(request.POST)
        if form.is_valid():
            first_unit = form.cleaned_data['first_unit']
            second_unit = form.cleaned_data['second_unit']
            value = form.cleaned_data['value']
            result = unit_conv.length_converter(first_unit, second_unit, value)
            context = {
                'title': title,
                'form': form,
                'data': {
                    'result': result
                }
            }
            return render(request, 'lengthconversion.html', context)
        else:
            error = {
                'error': "Input field can't be empty"
            }
            context = {
                'title': title,
                'form': form,
                'data': {
                    'result': error
                }
            }
            return render(request, 'lengthconversion.html', context)
    else:
        form = LengthInput()
        context = {
            'title': title,
            'form': form
        }
        return render(request, 'lengthconversion.html', context)

def temperature_conversion(request):
    title = 'Temperature Conversion'
    if request.method == 'POST':
        form = TempInput(request.POST)
        if form.is_valid():
            first_unit = form.cleaned_data['first_unit']
            second_unit = form.cleaned_data['second_unit']
            value = form.cleaned_data['value']
            result = unit_conv.temperature_converter(first_unit, second_unit, value)
            context = {
                'title': title,
                'form': form,
                'data': {
                    'result': result
                }
            }
            return render(request, 'temperature-conversion.html', context)
        else:
            error = {
                'error': "Input field can't be empty"
            }
            context = {
                'title': title,
                'form': form,
                'data': {
                    'result': error
                }
            }
            return render(request, 'temperature-conversion.html', context)
    else:
        form = TempInput()
        context = {
            'title': title,
            'form': form
        }
        return render(request, 'temperature-conversion.html', context)

def area_conversion(request):
    title = 'Area Conversion'
    if request.method == 'POST':
        form = AreaInput(request.POST)
        if form.is_valid():
            first_unit = form.cleaned_data['first_unit']
            second_unit = form.cleaned_data['second_unit']
            value = form.cleaned_data['value']
            result = unit_conv.area_converter(first_unit, second_unit, value)
            context = {
                'title': title,
                'form': form,
                'data': {
                    'result': result
                }
            }
            return render(request, 'area-conversion.html', context)
        else:
            error = {
                'error': "Input field can't be empty"
            }
            context = {
                'title': title,
                'form': form,
                'data': {
                    'result': error
                }
            }
            return render(request, 'area-conversion.html', context)
    else:
        form = AreaInput()
        context = {
            'title': title,
            'form': form
        }
        return render(request, 'area-conversion.html', context)

def weight_conversion(request):
    title = 'Weight Conversion'
    if request.method == 'POST':
        form = WeightInput(request.POST)
        if form.is_valid():
            first_unit = form.cleaned_data['first_unit']
            second_unit = form.cleaned_data['second_unit']
            value = form.cleaned_data['value']
            result = unit_conv.weight_converter(first_unit, second_unit, value)
            context = {
                'title': title,
                'form': form,
                'data': {
                    'result': result
                }
            }
            return render(request, 'weight-conversion.html', context)
        else:
            error = {
                'error': "Input field can't be empty"
            }
            context = {
                'title': title,
                'form': form,
                'data': {
                    'result': error
                }
            }
            return render(request, 'weight-conversion.html', context)
    else:
        form = WeightInput()
        context = {
            'title': title,
            'form': form
        }
        return render(request, 'weight-conversion.html', context)

def power_conversion(request):
    title = 'Power Conversion'
    if request.method == 'POST':
        form = PowerInput(request.POST)
        if form.is_valid():
            first_unit = form.cleaned_data['first_unit']
            second_unit = form.cleaned_data['second_unit']
            value = form.cleaned_data['value']
            result = unit_conv.power_converter(first_unit, second_unit, value)
            context = {
                'title': title,
                'form': form,
                'data': {
                    'result': result
                }
            }
            return render(request, 'power-conversion.html', context)
        else:
            error = {
                'error': "Input field can't be empty"
            }
            context = {
                'title': title,
                'form': form,
                'data': {
                    'result': error
                }
            }
            return render(request, 'power-conversion.html', context)
    else:
        form = PowerInput()
        context = {
            'title': title,
            'form': form
        }
        return render(request, 'power-conversion.html', context)

def pressure_conversion(request):
    title = 'Pressure Conversion'
    if request.method == 'POST':
        form = PressureInput(request.POST)
        if form.is_valid():
            first_unit = form.cleaned_data['first_unit']
            second_unit = form.cleaned_data['second_unit']
            value = form.cleaned_data['value']
            result = unit_conv.pressure_converter(first_unit, second_unit, value)
            context = {
                'title': title,
                'form': form,
                'data': {
                    'result': result
                }
            }
            return render(request, 'pressure-conversion.html', context)
        else:
            error = {
                'error': "Input field can't be empty"
            }
            context = {
                'title': title,
                'form': form,
                'data': {
                    'result': error
                }
            }
            return render(request, 'pressure-conversion.html', context)
    else:
        form = PressureInput()
        context = {
            'title': title,
            'form': form
        }
        return render(request, 'pressure-conversion.html', context)

def frequency_conversion(request):
    title = 'Frequency Conversion'
    if request.method == 'POST':
        form = FrequencyInput(request.POST)
        if form.is_valid():
            first_unit = form.cleaned_data['first_unit']
            second_unit = form.cleaned_data['second_unit']
            value = form.cleaned_data['value']
            result = unit_conv.frequency_converter(first_unit, second_unit, value)
            context = {
                'title': title,
                'form': form,
                'data': {
                    'result': result
                }
            }
            return render(request, 'frequency-conversion.html', context)
        else:
            error = {
                'error': "Input field can't be empty"
            }
            context = {
                'title': title,
                'form': form,
                'data': {
                    'result': error
                }
            }
            return render(request, 'frequency-conversion.html', context)
    else:
        form = FrequencyInput()
        context = {
            'title': title,
            'form': form
        }
        return render(request, 'frequency-conversion.html', context)

def speed_conversion(request):
    title = 'Speed Conversion'
    if request.method == 'POST':
        form = SpeedInput(request.POST)
        if form.is_valid():
            first_unit = form.cleaned_data['first_unit']
            second_unit = form.cleaned_data['second_unit']
            value = form.cleaned_data['value']
            result = unit_conv.speed_converter(first_unit, second_unit, value)
            context = {
                'title': title,
                'form': form,
                'data': {
                    'result': result
                }
            }
            return render(request, 'speed-conversion.html', context)
        else:
            error = {
                'error': "Input field can't be empty"
            }
            context = {
                'title': title,
                'form': form,
                'data': {
                    'result': error
                }
            }
            return render(request, 'speed-conversion.html', context)
    else:
        form = SpeedInput()
        context = {
            'title': title,
            'form': form
        }
        return render(request, 'speed-conversion.html', context)

def volume_conversion(request):
    title = 'Volume Conversion'
    if request.method == 'POST':
        form = VolumeInput(request.POST)
        if form.is_valid():
            first_unit = form.cleaned_data['first_unit']
            second_unit = form.cleaned_data['second_unit']
            value = form.cleaned_data['value']
            result = unit_conv.volume_converter(first_unit, second_unit, value)
            context = {
                'title': title,
                'form': form,
                'data': {
                    'result': result
                }
            }
            return render(request, 'volume-conversion.html', context)
        else:
            error = {
                'error': "Input field can't be empty"
            }
            context = {
                'title': title,
                'form': form,
                'data': {
                    'result': error
                }
            }
            return render(request, 'volume-conversion.html', context)
    else:
        form = VolumeInput()
        context = {
            'title': title,
            'form': form
        }
        return render(request, 'volume-conversion.html', context)
