# Delta time = calculates seconds between given dates considering year, month, day, hour, minute, second and UTC

def time_delta(t1, t2):
    def days_til_current_month(date):
        y = int(date.split(" ")[3])
        m = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug",
             "Sep", "Oct", "Nov", "Dec"].index(date.split(" ")[2]) + 1
        d = int(date.split(" ")[1])

        devir = 0
        # function to calculate how many leap years are there between given years
        for i in list(range(1583, y)):
            if i % 4 == 0:
                if i % 100 == 0:
                    if i % 400 == 0:
                        devir += 1
                else:
                    devir += 1

        y_today = (y-1583)*365 + (devir * 1)

        if m == 1:
            m_today = 0
        elif m == 2:
            m_today = 31
        else:
            if y % 4 == 0:
                if y % 100 == 0:
                    if y % 400 == 0:
                        m_today = [0, 31, 59, 90, 120, 151, 181,
                                   212, 243, 273, 304, 334][m-1] + 1
                    else:
                        m_today = [0, 31, 59, 90, 120, 151,
                                   181, 212, 243, 273, 304, 334][m-1]
                else:
                    m_today = [0, 31, 59, 90, 120, 151, 181,
                               212, 243, 273, 304, 334][m-1] + 1
            else:
                m_today = [0, 31, 59, 90, 120, 151,
                           181, 212, 243, 273, 304, 334][m-1]

        totday = y_today + m_today
        return totday

    def secs_from_month_starts(date):
        x = date.split(" ")
        day_tosec = int(x[1])*3600*24

        time = x[4].split(":")
        time_tosec = int(time[0]) * 3600 + int(time[1]) * 60 + int(time[2]) * 1

        utc = x[5]
        utc_h = int(utc[1]+utc[2])
        utc_m = int(utc[3]+utc[4])
        utc_tosec = utc_h * 3600 + utc_m * 60

        if utc[0] == "+":
            cur_sec_in_month = day_tosec + time_tosec - utc_tosec
        elif utc[0] == "-":
            cur_sec_in_month = day_tosec + time_tosec + utc_tosec

        return cur_sec_in_month

    totsec_a = days_til_current_month(t1)*24*3600 + secs_from_month_starts(t1)
    totsec_b = days_til_current_month(t2)*24*3600 + secs_from_month_starts(t2)

    delta = totsec_a - totsec_b

    if delta < 0:
        delta *= -1

    return str(delta)


print("Date format must be in following format : Day dd Mon yyyy hh:mm:ss +xxxx")
print("Sample input format: Sun 22 Jun 2200 04:54:19 +0500")
print()
t1 = input("Please enter a date: ")
t2 = input("Please enter a date: ")
print()

delta = time_delta(t1, t2)
print(delta, "seconds")
