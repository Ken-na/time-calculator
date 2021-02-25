week = {
    "monday" : 1,
    "tuesday" : 2,
    "wednesday" : 3,
    "thursday" : 4,
    "friday" : 5,
    "saturday" : 6,
    "sunday" : 7,
    "na" : -1
}
def add_time(start, duration, day = "na"):
    try:
        val = start.split(":")

        startHour = int(val[0])
        val = val[1].split()

        startMinute = int(val[0])
        val = str(val[1])
        #startMinute = int(val[1][0] + val[1][1])
    except:
        return "Not formatted correctly "# + str(startHour) + ":" + str(startMinute)
    startDay = week[day.lower()]

    #val = str(start[6] + start[7])

    if val == "PM":
        startHour += 12

    #process duration
    val = duration.split(":")
    addHour = int(val[0])
    print("start hour: " + str(startHour))
    print("add hour: " + str(addHour))
    addMinute = int(val[1])
    print("start minute: " + str(startMinute))
    print("add minute: " + str(addMinute))

    finalMinute = startMinute + addMinute
    finalHour = startHour + addHour
    finalDay = startDay
    daysPassed = 0
    while finalMinute > 59:
        finalMinute -= 60
        finalHour += 1
    while finalHour > 23:
        finalHour -= 24
        daysPassed += 1
    daysProcessed = startDay + daysPassed
    while daysProcessed > 7:
        daysProcessed -= 7
    finalSig = "AM"
    if finalHour > 11:
        finalSig = "PM"
        finalHour -= 12
    if finalHour == 0:
        finalHour = 12
    if finalMinute < 10:
        finalMinute = "0" + str(finalMinute)

    weekDayMsg = ""

    if startDay != -1:
        weekDayMsg = ", "
        if daysProcessed == 1:
            weekDayMsg += "Monday"
        elif daysProcessed == 2:
            weekDayMsg += "Tuesday"
        elif daysProcessed == 3:
            weekDayMsg += "Wednesday"
        elif daysProcessed == 4:
            weekDayMsg += "Thursday"
        elif daysProcessed == 5:
            weekDayMsg += "Friday"
        elif daysProcessed == 6:
            weekDayMsg += "Saturday"
        elif daysProcessed == 7:
            weekDayMsg += "Sunday"
    daysMsg = ""
    if daysPassed == 1:
        daysMsg = " (next day)"
    elif daysPassed > 1:
        daysMsg = " (" + str(daysPassed) + " days later)"

    new_time = str(finalHour) + ":" + str(finalMinute) + " " + finalSig + weekDayMsg + daysMsg



    return new_time
