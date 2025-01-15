day = int(input("Enter today's day: "))
number_of_day_elapsed = int(input("Enter the number of days elapsed since today: "))
days = ['Monday','Tuesday','Wednesday','Thursday', 'Friday','Saturday','Sunday']

if day == 1 and number_of_day_elapsed == 3:
    print("Today is ",days[0], "and the future day is ", days[3])
    
elif day == 2 and number_of_day_elapsed == 3:
    print("Today is ", days[1], "and the future day is ", days[4])
elif day == 3 and number_of_day_elapsed == 3:
    print("Today is ", days[2], "and the future day is ", days[5])
elif day == 4 and number_of_day_elapsed == 3:
    print("Today is ", days[3], "and the future day is ", days[6])
elif day == 5 and number_of_day_elapsed == 3:
    print("Today is ", days[4], "and the future day is ", days[0])
elif day == 6 and number_of_day_elapsed == 3:
    print("Today is ", days[5], "and the future day is ", days[1])
elif day == 0 and number_of_day_elapsed == 3:
    print("Today is ", days[6], "and the future day is ", days[2])