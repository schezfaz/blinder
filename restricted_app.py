"""
Checks to see if there are tasks that are running that haven't been
whitelisted for the working session. Prints 'Unwanted app
has been dected.' if app has been dected. Written for windows
"""

import pandas as pd
import os
import getpass


class RestrictedApps:

    def __init__(self, allowed_apps: list):
        computer_username = getpass.getuser()
        save_path = '"C:/Users/'+computer_username+'/desktop/running.csv"'
        os.system('TASKLIST /FO CSV > ' + save_path)
        self._restricted_app_dectected = 'N'
        self._allowed_apps = allowed_apps
        self._current_processes = pd.read_csv(
            'C:/Users/'+computer_username+'/desktop/running.csv')
        self.check_restricted(self._allowed_apps,
                              self._clean_activity_table(
                                  self._current_processes))
        if self._restricted_app_dectected == 'Y':
            print("Unwanted app has been dected.")

    def _clean_activity_table(self, current_activity_table):
        """
        args:
            current_activity_table - DataFrame

        Cleans the table that has the current running tasks and returns it to
        self._current_processes
        """
        clean_memory_amount = []
        memory_list = list(current_activity_table["Mem Usage"])
        for memory_case in memory_list:
            if "K" in memory_case:
                memory_case = memory_case.replace('K', '')
                if ',' in memory_case:
                    memory_case = memory_case.replace(',', '')
                    clean_memory_amount.append(int(memory_case))
                else:
                    clean_memory_amount.append(int(memory_case))
        self._current_processes["Mem Usage Clean"] = clean_memory_amount
        return self._current_processes

    def check_restricted(self, wanted_apps: list, current_tasks):
        """
        args:
            wanted_apps - list - List of apps that the user wants to use

        Checks the current active tasks and stores them in a list if they have
        the Session Name of 'RDP-Tcp#127' and if they are using more
        than 50000K of memory. The active list of tasks is compared to the
        allowed list of tasks. If there is a task that shouldn't be opened
        restricted app dected gets set to Y
        """
        always_allow_tasks = ['dwm.exe', 'explorer.exe',
                        'StartMenuExperienceHost.exe',
         'MicrosoftEdge.exe', 'MicrosoftEdgeCP.exe','SearchUI.exe']
        always_allow_tasks.extend(wanted_apps)
        tasks_filtered = current_tasks[
            (current_tasks["Mem Usage Clean"] > 50000) &
            (current_tasks["Session Name"] == 'RDP-Tcp#127')]
        tasks_name = list(tasks_filtered['Image Name'])
        for active_task in tasks_name:
            if active_task in always_allow_tasks:
                continue
            else:
                self._restricted_app_dectected = 'Y'
                break
