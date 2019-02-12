def time_converter(time):
    print('=' * 10)
    hour = int((time[:2]))
    minute = int((time[3:]))

    if hour < 12:
        return am(time,minute)
    elif hour == 12:
        return pm(hour, time, True)
    else:
        return pm(hour, time, False)


def pm(hour, time, twelve):
    if not twelve:
        hour = hour - 12
    return str(hour) + time[2:] + ' p.m.'


def am(time, minute):
    if str(time[:2]) == '00':
        if minute < 10:
            minute = '0' + str(minute)
        return str(12) + ':' + str(minute) + ' a.m.'
    else:
        return time[1:] + ' a.m.'


if __name__ == '__main__':
    print("Example:")
    print(time_converter('12:30'))
