#convert miles per hour to meters per second.
print('M/H to m/s Converter')
def converter(speed_mph):
    speed_mpers= (speed_mph / 2.237).__round__(2)
    print('The speed in meters per second is :',speed_mpers)

#mps = mph * 0.4474 OR mph / 2.237
MPH = int(input('Enter Speed in Miles Per Hour : '))
converter(MPH)