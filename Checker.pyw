from plyer import notification
import psutil
import time 

delay=300

while True:

	battery = psutil.sensors_battery()
	percent = battery.percent
	charging = battery.power_plugged

	print('Checking: ',end='')
	if percent<30 and not charging:
		notification.notify(
			title="Fast! Get the charger!!",
			message=f"Battery at {percent}%",
			app_icon="assets/low.ico",
			timeout=5
		)
		print(f"Got 30: {percent}")

	elif percent>70 and percent<100 and charging:
		notification.notify(
			title="Charged Enough!!",
			message=f"Battery at {percent}%",
			app_icon="assets/charged.ico",
			timeout=5
		)
		print(f'Got 70 -> {percent}')
	elif percent == 100 and charging:
		notification.notify(
			title="Damn boi!! Remove yo Charger!",
			message="It's overflowin'",
			app_icon="assets/full.ico",
			timeout=5
			)
		print('Got 100')
	else:
		print(f'Got nothing -> {percent}')
	
	time.sleep(delay)
