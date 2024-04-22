import RPi.GPIO as GPIO
import tkinter as tk

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
led_pins = [17, 18, 24]  
GPIO.setup(led_pins, GPIO.OUT)


led_pwms = [GPIO.PWM(led_pin, 100) for led_pin in led_pins]  # Frequency = 100 Hz
for led_pwm in led_pwms:
    led_pwm.start(0)  # Start with duty cycle of 0 (off)


def change_intensity(led_pwm, intensity):
    led_pwm.ChangeDutyCycle(intensity)


def update_intensity(led_index, value):
    change_intensity(led_pwms[led_index], int(value))


root = tk.Tk()
root.title("LED Intensity Controller")


sliders = []
for i, led_pin in enumerate(led_pins):
    slider = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, command=lambda value, index=i: update_intensity(index, value), label=f"LED {i+1} Intensity")
    slider.pack()
    sliders.append(slider)


def start_intensity_change():
    for slider in sliders:
        slider.set(50)  # Set intensity to 50% for all LEDs

# Start intensity change after 2 seconds (2000 milliseconds)
root.after(2000, start_intensity_change)


exit_button = tk.Button(root, text="Exit", command=root.destroy)
exit_button.pack()

root.mainloop()


for led_pwm in led_pwms:
    led_pwm.stop()
GPIO.cleanup()
