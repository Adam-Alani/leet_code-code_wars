def make_readable(seconds):
    minutes, hours = 0,0
    while seconds >= 60:
        if seconds >= 60:
            seconds = seconds - 60
            minutes += 1
            while minutes >= 60:
                if minutes >= 60:
                      minutes = minutes - 60
                      hours += 1
    return(str(hours).zfill(2) + ":" + str(minutes).zfill(2) + ":" + str(seconds).zfill(2))

