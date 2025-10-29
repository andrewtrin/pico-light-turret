# Turret Main - Continuous Sweep
from machine import Pin, PWM, ADC
from time import sleep

# Hardware Setup
pan_servo = PWM(Pin(15))
pan_servo.freq(50)
light_sensor = ADC(26)

# Helper functions
def angle_to_duty(angle):
    # Maps angle and returns duty cycle for sweep
    return int(1640 + (angle/180) * 6550)

def scan_and_update(angle, max_light, best_angle):
    # Moves servo, reads sensor, and updates memory if brighter light found
    pan_servo.duty_u16(angle_to_duty(angle))
    current_light = light_sensor.read_u16()
    
    if current_light > max_light:
        max_light = current_light
        best_angle = angle
    
    sleep(0.01) # Slows down the scan
    return max_light, best_angle

# Main loop
while True:
    # Resets memory before scan
    max_light_level = 0
    best_angle = 90 # Assume best angle is in middle to start
    
    # L-R sweep
    for angle in range(0, 181, 1):
        max_light_level, best_angle = scan_and_update(angle, max_light_level, best_angle)
    
    # R-L sweep
    for angle in range(181, 0, -1):
        max_light_level, best_angle = scan_and_update(angle, max_light_level, best_angle)
        
    # Move and lock to brightest
    pan_servo.duty_u16(angle_to_duty(best_angle))
    sleep(2)

