# Your Calculator Project
# Name: 
# Description: Metric to Imperial (or other way around) Calculator for temperature, speed, or length.
# ================================
# Your code below:
print("Welcome to the Metric to Imperial calculator (but Metric > Imperial guys)")

while 1==True:
    task=int(input("Would you like me to convert Celsius to Fahrenheit, KPH to MPH, Kilometers to Miles, or reverse conversions? (choose number 1-4)"))
    if task==1:
        c=float(input("What is the celsius you want converted?"))
        f=(c*1.8)+32
        print(f"That's {f} Fahrenheit!")
        pass
    elif task==2:
        kph=float(input("What is the KPH you want converted?"))
        mph=kph*0.621371
        print(f"That's around {mph} MPH!")
        pass
    elif task==3:
        km=float(input("What is the number of Kilometers you want converted?"))
        mi=km*0.621
        print(f"That's approximately {mi} miles!")
        pass
    elif task==4:
        print("Conversions reversed!")
        while 1==True:
            task=int(input("Would you like me to convert Fahrenheit to Celsius, MPH to KPH, Miles to Kilometers, or reverse conversions? (choose number 1-4)"))
            if task==1:
                f=float(input("What is the Fahrenheit you want converted?"))
                c=(f-32)/1.8
                print(f"That's {c} Celsius!")
                pass
            elif task==2:
                mph=float(input("What is the MPH you want converted?"))
                kph=mph*1.609344
                print(f"That's around {kph} KPH!")
                pass
            elif task==3:
                mi=float(input("What is the number of Miles you want converted?"))
                km=mi*1.609344
                print(f"That's approximately {km} Kilometers!")
                pass
            elif task==4:
                print("Reset Calc to reverse again.")




