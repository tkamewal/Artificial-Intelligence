import schedule
import time
from plyer import notification

def send_notification():
    notification.notify(
        title='Reminder',
        message='Do your work now!',
        app_name='My App',
    )

# Schedule the notification to be sent every day at 5 o'clock
schedule.every().day.at("18:24").do(send_notification)

# Run the scheduler in the background
while True:
    schedule.run_pending()
    time.sleep(1)
