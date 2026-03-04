import pandas as pd
import random
import matplotlib.pyplot as plt

time = []
temperature = []
vibration = []
base_temp = 70

for i in range(1, 201): 
    time.append(i)

    base_temp += random.uniform(-1, 2)
    temperature.append(round(base_temp, 2))
    vibration.append(round(random.uniform(0.2, 1.0), 2))

data = {
    "time": time,
    "temperature": temperature,
    "vibration": vibration
}

df = pd.DataFrame(data)

#SHOW ALL
pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)
print(df)

#SHOW ESTATISTICS
print(df.head())
print(df.tail())
print(df.describe())


media_temp = df["temperature"].mean()
print("\nMedia of temperature: ", round(media_temp, 2))

limit = 85

up_limit = df[df["temperature"] > limit]
print("\nCritical occurrences: \n", up_limit)

amount_critical = up_limit.shape[0]
print("\nAmount Critical occurrences: ", amount_critical)

plt.figure()
plt.plot(df["time"], df["temperature"])

plt.xlabel("Time")
plt.ylabel("Temperature")
plt.title("Machine Temperature Over Time")
plt.axhline(y=limit)

plt.show()

plt.figure()
plt.plot(df["time"], df["temperature"])
plt.axhline(y=limit)

plt.xlabel("Time")
plt.ylabel("Temperature")
plt.title("Machine Temperature Monitoring")

plt.grid()
plt.show()

df["temp_variation"] = df["temperature"].diff()
media_variation = df["temp_variation"].mean()

print("\nAverage Temperature variation per cycle: ", round(media_variation, 3))

if media_variation > 0.3:
    print("\n ⚠ WARNING ⚠: Upward temperature trend detected!")