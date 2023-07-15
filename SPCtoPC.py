import serial


if __name__ == '__main__':
    ser = serial.Serial('COM4', baudrate=9600)
    while True:
        line = ser.readline()
        print(line)
        '''
        get_cm = str(line).split(":")
        value1 = get_cm[1][0:8]
        value2 = get_cm[2][0:8]
        print(f"value1:{value1}")
        print(f"value2:{value2}")'''