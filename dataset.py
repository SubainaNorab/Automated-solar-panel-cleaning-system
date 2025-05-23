import csv
import random
from datetime import datetime, timedelta

num_records = 300 # record
V_CLEAN = 0.9 # to compare dust level
K = 0.5
start_time = datetime.now()

with open("solar_clean_data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["date", "time", "dust_value", "voltage", "current", "decision"])
# generating data
    for i in range(num_records):
        now = start_time + timedelta(minutes=10 * i)
        date = now.strftime("%Y-%m-%d")
        time = now.strftime("%H:%M:%S")

        vo = round(random.uniform(0.8, 3.6), 2)
        dust_value = max((vo - V_CLEAN) / K, 0)

        voltage = round(random.uniform(16, 20) - dust_value * 0.1, 2) #panel voltage
        current = round(random.uniform(2000, 3000) * (1 - dust_value / 15), 2) # panel current

        # label
        decision = "needs_cleaning" if dust_value > 3 and current < 2000 else "clean"

        writer.writerow([date, time, dust_value, voltage, current, decision])

print(" Dataset  saved as 'solar_clean_data.csv'")
