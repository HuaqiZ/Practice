import schedule
import time
from job_run_once import main

main()

schedule.every(30).minutes.do(main)

while True:
    schedule.run_pending()
    time.sleep(1)
