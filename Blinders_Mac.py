"""Rough Start - currenlty written for mac. So far creates a list of
restricted apps."""

import getpass


class Blinders():

    def __init__(self):
        system_username = getpass.getuser()
        apps_string = subprocess.run(
            ['find', '/Applications', '-user', 'system_username',
             '-name', '*.app'], stdout=subprocess.PIPE).stdout.decode('utf-8')
        self._apps = apps_string.split('\n')

    def restricted_apps(self, wanted_apps: list):
        """
        args:
            wanted_apps - list - List of apps that the user wants to use

        Returns a list of restricted_apps
        """
        restricted_apps = []
        for app in self._apps:
            for wanted_app in wanted_app:
                if wanted_app not in app:
                    restricted_apps.append(not_wanted_app)
        return restricted_apps
