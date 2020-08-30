"""
Time Management portion of the project
"""
from datetime import datetime
from datetime import timedelta
from datetime import datetime
import os
from playsound import playsound
import time

class TimeManagment():

    def __init__(self):
        self._time_start = datetime.now()
        self._work_duration_hours = int(input(
            "How many hours would you like to work?\n"))
        self._work_duration_minutes = int(input(
            "How many minutes would you like to work?\n"))
        self._work_end = self._time_start + timedelta(
            hours = self._work_duration_hours,
            minutes= self._work_duration_minutes)

    def timer_alert(self):
        '''
        Sets a notifications sound to be played at intervals of 30 minutes
        should have a gui aspect as well
        '''
        c=1
        alert = self._time_start + timedelta(minutes = 25)
        while True:
            if datetime.now() >= alert and c%4 != 0:
                playsound("notification.mp3")
                c+=1
                alert = datetime.now() + timedelta(minutes = 25)
            elif c%4 == 0:
                playsound("notification.mp3")
                time.sleep(0.5)
                playsound("notification.mp3")
                c+=1
            else:
                continue
