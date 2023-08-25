import time
import serial


ser = serial.Serial("/dev/ttyACM0", baudrate=9600) #Modificar el puerto serie de ser necesario

try:
    while True:
        comando = input("Ingresar comando (on/off): ")
        comando = comando + "\n"
        comandoBytes = comando.encode()
        ser.write(comandoBytes)
        time.sleep(0.1)
        read = ser.readline()
        print(read)

except KeyboardInterrupt:
    print("\nInterrupcion por teclado")
except ValueError as ve:
    print(ve)
    print("Otra interrupcion")
finally:
    ser.close()