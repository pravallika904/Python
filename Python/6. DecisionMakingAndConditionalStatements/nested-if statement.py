weather = "sunny"
time_of_day = "night"

if weather == "sunny":
    if time_of_day == "day":
        print("You can play with your car toy.")
    else:
        print("It's night. Time to sleep.")
elif weather == "rainy":
    print("You play with your boat toy.")
elif weather == "snowy":
    if time_of_day == "night":
        print("You play with your teddy bear toy.")
    else:
        print("You play with your snowman toy.")
else:
    print("You stay inside and read a storybook.") 