# https://py.checkio.org/en/mission/sun-angle/


def sun_angle(time):
    degree_range = 180
    minute_a_day = 12 * 60
    one_minute_value = degree_range / minute_a_day

    time_hour = int(time[0:2])
    time_minutes = int(time[3:])

    minutes = (time_hour - 6) * 60 + time_minutes
    if minute_a_day >= minutes >= 0:
        return minutes * one_minute_value
    return "I don't see the sun!"


if __name__ == '__main__':
    print("Example:")
    print(sun_angle("07:00"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert sun_angle("07:00") == 15
    assert sun_angle("01:23") == "I don't see the sun!"
    print("Coding completed")