
#Given minute and hour, return the angle between hour hand and minute hand

def calc_angle(hour,minute):
    hour_hand_angle = int(hour)*30 + int(minute)*0.5
    minute_hand_angle = int(minute)*6
    return min((abs(hour_hand_angle-minute_hand_angle),360-abs(hour_hand_angle-minute_hand_angle)))

hour = raw_input('Enter hour value: ')
minute = raw_input('Enter minute value: ')
print calc_angle(hour,minute)