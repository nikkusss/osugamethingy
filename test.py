import osu.circle
import time
o = osu.circle.Circle(200,1,1,5, 5)
for i in range(500):
    print(f"{o.isClose(i)} -- {i}")
    time.sleep(1 / 120)