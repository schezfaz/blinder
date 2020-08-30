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
        self.time_start = datetime.now()
        self.work_duration_hours = int(input("How many hours would you like to work?\n"))
        self.work_duration_minutes = int(input("How many minutes would you like to work?\n"))

    def endtime(self):
        '''
        Establishes when the work day ends
        '''
        self.time_start = datetime.now()
        self.work_end = (self.time_start + timedelta(hours = self.work_duration_hours, minutes= self.work_duration_minutes)).strftime("%H:%M")
        return(self.work_end)

    def timer_alert(self):
        '''
        Sets a notifications sound to be played at intervals of 30 minutes
        should have a gui aspect as well
        '''
        c=1
        alert = self.time_start + timedelta(seconds = 15)
        while True:
            if datetime.now() >= alert and c%4 != 0:
                playsound("notification.mp3")
                c+=1
                alert = datetime.now() + timedelta(seconds = 15)
            elif c%4 == 0:
                playsound("notification.mp3")
                time.sleep(0.5)
                playsound("notification.mp3")
                c+=1
            else:
                continue