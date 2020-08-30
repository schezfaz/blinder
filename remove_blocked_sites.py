"""
Removes the changes that were made to the host file by 'blocked_sites'
"""

import socket


class SiteBlocker:

    def __init__(self, block_sites: list):
        self._block_sites = block_sites
        hostname = socket.gethostname()
        self._redirect = socket.gethostbyname(hostname)
        host_filepath = 'C:\Windows\System32\drivers\etc\hosts2'
        self.site_block_turn_off(block_sites, host_filepath)

    def site_block_turn_off(self, blocked_sites, host_filepath):
        with open(host_filepath, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in blocked_sites):
                    file.write(line)

            file.truncate()
