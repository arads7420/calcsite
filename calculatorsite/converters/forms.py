from django import forms

class DecimalInput(forms.Form):
    decimal_input = forms.CharField(label="Decimal Number", max_length=100, label_suffix='')

class BinaryInput(forms.Form):
    binary_input = forms.CharField(label="Binary Number", max_length=100, label_suffix='')

class PercentInput(forms.Form):
    percent_input = forms.CharField(label="Percentage Value (%)", max_length=100, label_suffix='')

class OctalInput(forms.Form):
    octal_input = forms.CharField(label="Octal Number", max_length=100, label_suffix='')

class HexInput(forms.Form):
    hex_input = forms.CharField(label="Hexadecimal Value", max_length=100, label_suffix='')

class DecimalInput_Base(forms.Form):
    decimal_input = forms.CharField(label="Decimal Number", max_length=100, label_suffix='')
    base_input = forms.CharField(label="Base", max_length=100, label_suffix='')

class DegreeInput(forms.Form):
    degree_input = forms.CharField(label="Degrees Value (°)", max_length=100, label_suffix='')

class DegMinSecInput(forms.Form):
    deg_input = forms.CharField(label="Degrees (°)", max_length=100, label_suffix='')
    min_input = forms.CharField(label="Minutes (′)", max_length=100, label_suffix='')
    sec_input = forms.CharField(label="Seconds (″)", max_length=100, label_suffix='')

class LengthInput(forms.Form):
    units = [('dm', 'Decimeter (dm)'), ('ly', 'Light Year (ly'), ('mm', 'Millimeter (mm)'), 
    ('km', 'Kilometer (km)'), ('cm', 'Centimeter (cm)'), ('m', 'Meter (m)'), 
    ('μm', 'Micrometer (μm)'), ('guz', 'Guz (guz)'), ('pc', 'Parsec (pc)'), ('AU', 'Astronomical Unit (AU)'), 
    ('LD', 'Lunar Distance (LD)'), ('pm', 'Picometer (pm)'), ('nm', 'Nanometer (nm)'), 
    ('fur', 'Furlong (fur)'), ('fm', 'Fathom (fm)'), ('yd', 'Yard (yd)'), 
    ('nmi', 'Nautical Mile (nmi)'), ('ft', 'Foot (ft)'), 
    ('mi', 'Mile (mi)'), ('in', 'Inch (in)')]

    first_unit = forms.CharField(label="From", widget=forms.Select(choices=units), initial=('m', 'meter (m)'))
    value = forms.CharField(label="Value",  max_length=100, label_suffix='')
    second_unit = forms.CharField(label="To", widget=forms.Select(choices=units), initial=('km', 'kilometer (km)'))

class TempInput(forms.Form):
    units = [('°F', 'Degree Fahrenheit (°F)'), ('°C', 'Degree Celsius (°C)'),
    ('K', 'Kelvin (K)'), ('°Re', 'Degree Reaumur (°Re)'), ('°R', 'Degree Rankine (°R)'),
    ('°De', 'Delisle (°De)'), ('°N', 'Newton (°N)'), ('°Rø', 'Rømer (°Rø)')]

    first_unit = forms.CharField(label="From", widget=forms.Select(choices=units), initial=('°C', 'Degree Celsius (°C)'))
    value = forms.CharField(label="Value",  max_length=100, label_suffix='')
    second_unit = forms.CharField(label="To", widget=forms.Select(choices=units), initial=('°F', 'Degree Fahrenheit (°F)'))

class AreaInput(forms.Form):
    units = [('m²', 'Square Meter (m²)'), ('dm²', 'Square Centimeter (cm²)'),
    ('km²', 'Sqaure Kilometer (km²)'), ('mm²', 'Square Millimeter (mm²)'),
    ('ar', 'Are (ar)'), ('ha', 'Hectare (ha)'), ('mi²', 'Square Mile (mi²)'),
    ('rd²', 'Sqaure Rod (rd²)'), ('yd²', 'Sqaure Yard (yd²)'), ('ft²', 'Square Foot (ft²)'),
    ('ac','Acre (ac)'), ('in²', 'Square Inch (in²)')]

    first_unit = forms.CharField(label="From", widget=forms.Select(choices=units), initial=('m²', 'Square Meter (m²)'))
    value = forms.CharField(label="Value",  max_length=100, label_suffix='')
    second_unit = forms.CharField(label="To", widget=forms.Select(choices=units), initial=('ha', 'Hectare (ha)'))

class WeightInput(forms.Form):
    units = [('g', 'Gram (g)'), ('μg', 'Microgram (μg)'), ('q', 'Quintal (q)'), ('ct', 'Carat (ct)'),
    ('t', 'Ton (t)'), ('mg', 'Milligram (mg)'), ('kg', 'Kilogram (kg)'), ('st', 'Short Ton (st)'),
    ('lt', 'Long Ton (lt)'), ('oz', 'Ounce (oz)'), ('gr', 'Grain (gr)'), ('dr', 'Dram (dr)'),
    ('sh cwt', 'Short Hundredweight (sh cwt)'), ('lb', 'Pound (lb)'), ('st', 'Stone (st)'),
    ('lg cwt', 'Long Hundredweight (lg cwt)')]

    first_unit = forms.CharField(label="From", widget=forms.Select(choices=units), initial=('g', 'Gram (g)'))
    value = forms.CharField(label="Value",  max_length=100, label_suffix='')
    second_unit = forms.CharField(label="To", widget=forms.Select(choices=units), initial=('oz', 'Ounce (oz)'))

class PowerInput(forms.Form):
    units = [('J/s', 'Joule/second (J/s)'), ('Btu/s', 'British Thermal Unit/Second (Btu/s)'),
    ('PS', 'Metric Horsepower (PS)'), ('kg·m/s', 'Kilogram-meter/second (kg·m/s)'),
    ('kcal/s', 'Kilocalorie/second (kcal/s)'), ('W', 'Watt (W)'), ('hp', 'Imperial Horsepower (hp)'),
    ('ft·lb/s', 'Foot-pound/second (ft·lb/s)'), ('N·m/s', 'Newton-meter/second (N·m/s)'),
    ('kW', 'Kilowatt (kW)')]

    first_unit = forms.CharField(label="From", widget=forms.Select(choices=units), initial=('W', 'Watt (W)'))
    value = forms.CharField(label="Value",  max_length=100, label_suffix='')
    second_unit = forms.CharField(label="To", widget=forms.Select(choices=units), initial=('kcal/s', 'Kilocalorie/second (kcal/s)'))

class PressureInput(forms.Form):
    units = [('mmH2O', 'Millimeter of Water (mmH2O)'), ('psf', 'Pounds/sqare foot (psf)'),
    ('kgf/cm²','Kilogram-force/square centimeter (kgf/cm²)'), ('psi', 'Pounds/square inch (psi)'),
    ('mmHg', 'Millimeter of Mercury'), ('bar', 'Bar'), ('inHg', 'Inch of Mercury (inHg)'),
    ('mbar', 'Millibar (mbar)'), ('hPa', 'Hectopascal (hPa)'), ('atm', 'Standard Atmosphere (atm)'), 
    ('kPa', 'Kilopascal (kpa)'), ('kgf/m²', 'Kilogram-force/square meter (kgf/m²)'), 
    ('MPa', 'Megapascal (MPa)')]

    first_unit = forms.CharField(label="From", widget=forms.Select(choices=units), initial=('bar', 'Bar'))
    value = forms.CharField(label="Value",  max_length=100, label_suffix='')
    second_unit = forms.CharField(label="To", widget=forms.Select(choices=units), initial=('atm', 'Standard Atmosphere (atm)'))

class FrequencyInput(forms.Form):
    units = [('Hz', 'hertz (Hz)'), ('kHz', 'kilohertz (kHz)'), 
    ('MHz', 'megahertz (MHz)'), ('GHz', 'gigahertz (GHz)'), ('THz', 'terahertz (THz)'), 
    ('PHz', 'petahertz (PHz)'), ('EHz', 'exahertz (EHz)'), ('ZHz', 'zettahertz (ZHz)'), 
    ('YHz', 'yottahertz (YHz)')]

    first_unit = forms.CharField(label="From", widget=forms.Select(choices=units), initial=('g', 'Gram (g)'))
    value = forms.CharField(label="Value",  max_length=100, label_suffix='')
    second_unit = forms.CharField(label="To", widget=forms.Select(choices=units), initial=('kg', 'Kilogram (kg)'))

class SpeedInput(forms.Form):
    units = [('c', 'Speed of light (c)'), ('km/s', 'Kilometer/second (km/s)'),
    ('mph', 'Mile/hour (mph)'), ('Ma', 'Mach (Ma)'), ('in/s', 'Inch/second (in/s)'),
    ('m/s', 'Meter/second (m/s)'), ('km/h', 'Kilometer/hour (km/h)')]

    first_unit = forms.CharField(label="From", widget=forms.Select(choices=units), initial=('m/s', 'Meter/second (m/s)'))
    value = forms.CharField(label="Value",  max_length=100, label_suffix='')
    second_unit = forms.CharField(label="To", widget=forms.Select(choices=units), initial=('km/h', 'Kilometer/hour (km/h)'))

class VolumeInput(forms.Form):
    units = [('hl', 'Hectoliter (hl)'), ('m³', 'Cubic meter (m³)'), ('cm³', 'Cubic centimeter (cm³)'),
    ('dl', 'Deciliter (dl)'), ('cl', 'Centiliter (cl)'), ('dm³', 'Cubic decimeter (dm³)'), 
    ('l', 'Liter (l)'), ('mm³', 'Cubic millimeter (mm³)'), ('ml', 'Milliliter (ml)'), ('ft³', 'Cubic foot (ft³)'),
    ('US fl oz', 'US fluid ounce (US fl oz)'), ('yd³', 'Cubic yard (yd³)'), ('in³', 'Cubic inch (in³)'), 
    ('af³', 'Acre-foot (af³)'), ('UK gal', 'UK gallon (UK gal)'), ('US gal', 'US gallon (US gal)'), 
    ('UK fl oz','UK fluid ounce (UK fl oz)')]

    first_unit = forms.CharField(label="From", widget=forms.Select(choices=units), initial=('ml', 'Milliliter (ml)'))
    value = forms.CharField(label="Value",  max_length=100, label_suffix='')
    second_unit = forms.CharField(label="To", widget=forms.Select(choices=units), initial=('l', 'Liter (l)'))