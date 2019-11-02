#!/bin/python3

def time_conversion(s):
    time = s[:-2]
    hr, mm, ss = map(int, time.split(":"))
    mer = s[-2:]
    if mer.upper() == "PM" and hr != 12:
        hr = 12 + hr
    if mer.upper() == "AM" and hr == 12:
        hr = 0
    return "{:02d}:{:02d}:{:02d}".format(hr,mm,ss)


if __name__ == "__main__":
    '''
    Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.

    input:
    07:45:23PM
    output:
    19:45:23
    '''
    s = input()
    result = timeConversion(s)
    print(result)