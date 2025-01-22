from gpiozero import LED
from gpiozero import Button
import time
import requests

def send_line_notify(message, token):
    line_notify_api = "https://notify-api.line.me/api/notify"
    headers = {"Authorization": "Bearer " + "token"}
    data = {"message": message}
    requests.post(line_notify_api, headers=headers, data=data)

line_notify_token = "token"

pump = LED(27)
sensor = Button(4)
while True:
    if sensor.is_pressed:
        print("High soil!")
        message_high = "High soil detected!"
        send_line_notify(message_high, line_notify_token)
    else:
        message = "Low soil!"
        send_line_notify(message, line_notify_token)
        print("Pump ON!")
        pump.on()
        time.sleep(2)
        for i in range(1, 4):
            print(i)
            time.sleep(1)
        pump.off()
        print("Pump OFF!")
        message_stop = "Pump stopped!"
        send_line_notify(message_stop, line_notify_token)
    time.sleep(60)
