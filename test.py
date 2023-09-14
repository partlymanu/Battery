import psutil,time
while False:
	battery = psutil.sensors_battery()
	percent = battery.percent
	charging = battery.power_plugged
	print(f'battery={percent} and {charging}')
	# time.sleep(300)
battery = psutil.sensors_battery()
percent = battery.percent
charging = battery.power_plugged
print(f'battery={percent} and {charging}')