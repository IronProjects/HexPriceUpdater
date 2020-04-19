from coinpaprika import client as Coinpaprika
import time
from datetime import datetime

client = Coinpaprika.Client()
now = datetime.now()
current_time = now.strftime("%H:%M:%S")

a = client.today("hex-hex")
print("Hex Price Updater, to cancel press CTRL + C")
time.sleep(0.25)
print("---")
time.sleep(0.25)
balance = int(input("How much HEX do you have: " ))
time.sleep(1)
delay = int(input("Choose delay between price updates (in seconds): "))
time.sleep(1)
print("---")

while True:
    print ('Hex current price is: $', a[0]['open'],)
    if a[0]['open'] > 1:
        break
    else:
        time.sleep(0.5)
        print(("Your Hex is valued at: $"),int(balance*a[0]['open']))
        time.sleep(1)
        print("Current Time =", current_time)
        time.sleep(1)
        print("---")
        time.sleep(delay)

