def format_duration(seconds):
    sec = seconds
    yrs,day,hrs,mns,final = 0,0,0,0,0
    if seconds == 0:
        return ("now")

    while sec >=  60: mns += 1; sec -=  60;
    while mns >=  60: hrs += 1; mns -=  60;
    while hrs >=  24: day += 1; hrs -=  24;
    while day >= 365: yrs += 1; day -= 365;

    year,days,hour,minute,second = "year","day",'hour','minute','second'

    if yrs > 1:
        year = "years"
    if day > 1:
        days = "days"
    if hrs > 1:
        hour = "hours"
    if mns > 1:
        minute = "minutes"
    if sec > 1:
        second = "seconds"

    if yrs == 0:
        year = ""
    if day == 0:
        days = ""
    if hrs == 0:
        hour = ""
    if mns == 0:
        minute = ""
    if sec > 0:
        second = ""











print((format_duration(120)))