#If you want to send me a tip (eth/hex address): 0xaD3d60A126Ae102cFf8eed570a888Fe4Ba486D99

from coinpaprika import client as Coinpaprika
import time
from datetime import datetime

client = Coinpaprika.Client()

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
    price = client.ticker("hex-hex")
    value = list((list(price.values())[9]).values())[0]["price"]
    now = datetime.now()
    rank = client.coin("hex-hex")
    current_time = now.strftime("%H:%M:%S")
    print ('Hex current price is: $', value)
    print ('Rank:', rank['rank'])
    if value > 1:
        break
    else:
        time.sleep(0.5)
        print(("Your Hex is valued at: $"),int(balance*value))
        time.sleep(1)
        print("Current Time =", current_time)
        time.sleep(1)
        print("---")
        time.sleep(delay)
