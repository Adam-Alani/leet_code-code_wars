def reformatDate(date):
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
              "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

    date = date.split(" ")
    day = date[0][:-2]
    if len(day) == 1:
      day = "0" + day

    month = months.index(date[1]) + 1
    if len(str(month)) == 1:
      month = "0" + str(month)
      
    year = date[2]
    return "{}-{}-{}".format(year, month, day)


print(reformatDate("6th Jan 2052"))
