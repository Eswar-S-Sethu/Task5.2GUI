import RPi.GPIO as GPIO
import tkinter as tk

# Set up GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
led_pins = [17, 18, 24]  # GPIO pins for LEDs
GPIO.setup(led_pins, GPIO.OUT)

# Set up PWM
led_pwms = [GPIO.PWM(led_pin, 100) for led_pin in led_pins]  # Frequency = 100 Hz
for led_pwm in led_pwms:
    led_pwm.start(0)  # Start with duty cycle of 0 (off)

# Function to handle slider movement
def change_intensity(led_pwm, intensity):
    led_pwm.ChangeDutyCycle(intensity)

# Function to update LED intensity
def update_intensity(led_index, value):
    change_intensity(led_pwms[led_index], int(value))

# GUI setup
root = tk.Tk()
root.title("LED Intensity Controller")

# Create sliders for each LED
sliders = []
for i, led_pin in enumerate(led_pins):
    slider = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, command=lambda value, index=i: update_intensity(index, value), label=f"LED {i+1} Intensity")
    slider.pack()
    sliders.append(slider)

# Timer function to change intensity
def start_intensity_change():
    for slider in sliders:
        slider.set(50)  # Set intensity to 50% for all LEDs

# Start intensity change after 2 seconds (2000 milliseconds)
root.after(2000, start_intensity_change)

# Exit button
exit_button = tk.Button(root, text="Exit", command=root.destroy)
exit_button.pack()

root.mainloop()

# Clean up GPIO
for led_pwm in led_pwms:
    led_pwm.stop()
GPIO.cleanup()
