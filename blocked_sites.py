"""
Blocks predefined sites
"""

import socket


class SiteBlocker:

    def __init__(self, block_sites: list):
        self._block_sites = block_sites
        hostname = socket.gethostname()
        self._redirect = socket.gethostbyname(hostname)
        host_filepath = 'C:\Windows\System32\drivers\etc\hosts2'
        self.site_block(self._block_sites, self._redirect, host_filepath)

    def site_block(self, blocked_sites, redirect, host_filepath):
        with open(host_filepath, 'r+') as file:
            content = file.read()
            for website in blocked_sites:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")



