import winsound
winsound.Beep(100, 1000)

print("--------------")

for freq in range(50, 100):
    print("freq:", freq)
    winsound.Beep(freq, 1000)

print("--------------")