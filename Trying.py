
speed = 50
min_speed = 0
max_speed = 3000
duty_cycle = (speed - min_speed) / (max_speed - min_speed) * 100


# Gradually adjust the duty cycle to the desired speed
current_speed = 0
while current_speed < speed:
    current_speed += 10
    if current_speed > speed:
        current_speed = speed
    current_duty_cycle = (current_speed - min_speed) / (max_speed - min_speed) * 100
    print(current_duty_cycle)



