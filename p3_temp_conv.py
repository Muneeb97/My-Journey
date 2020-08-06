#temperatur conversion from *f to *c and k
print('Temeperature Converter')
far = float(input('Enter a temperature in degrees farenheit : '))

def conv(farenheit):
    celcius = (farenheit - 32) * (5/9)
    kelvin = celcius + 273.15
    print(celcius.__round__(4),' Degree Celcius')
    print(kelvin.__round__(4),' Kelvin')

conv(far)