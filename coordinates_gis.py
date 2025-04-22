# conversion of DMS to degree 
# Decimal = Degrees + (Minutes / 60) + (Seconds / 3600)
# If S or W → make it negative

def manual_dms_converter():
    hour = float(input("Input Hour: "))
    minutes = float(input("Input Minutes: "))
    seconds = float(input("Input Seconds: "))

    minutes_convert = (minutes/60)
    seconds_converted = (seconds/3600)

    coordinate = hour + minutes_convert + seconds_converted
    print(f"Degree Value: {coordinate}")


# upgraded version
# use space for separator
# example 34h 39m 35s
converting = True
while converting: 
    dms = input("\nWelcome to Josh dms to degree converter cause josh is lazy\nInput your dms values: ").split(" ")
    try:
        converted_dms = int(dms[0]) + int(dms[1])/60 + int(dms[2])/3600
    except IndexError:
        print("missing 1-2 more values\nExample: 30 30 30")
    except ValueError:
        print("Please enter an integer")
    else:
        print(converted_dms)
    finally:
        choice = input("Would you like to continue? (Y/N): ").upper()
        if choice == "N":
            converting = False