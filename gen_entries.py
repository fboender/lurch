#!/usr/bin/env python3

"""
Example file for generating Lurch entries.
"""

import os
import sys
import json
import subprocess

def entry(type, title, value, **options):
    """
    Helper to generate entries.
    """
    title = ''.join([x for x in title if ord(x) < 65534])
    value = ''.join([x for x in value if ord(x) < 65534])

    print("type: {}\ntitle: {}\nvalue: {}".format(type,
                                                  title,
                                                  value))
    for option_key, option_value in options.items():
        print("{}: {}".format(option_key, option_value))
    print()

# Passwords
entry("autotype", "pass example.com ssh", "mys3cr3t")
entry("autotype", "pass example.com web", "@dm1ns3cr3t")

# Custom commands
entry("exec", "cmd edit SSH configuration", "xterm -e vi ~/.ssh/config", shell=True)

# Desktop entries
dirs = ['/usr/share/applications', os.path.expanduser('~/.local/share/applications')]
for dir in dirs:
    try:
        for fname in sorted(os.listdir(dir)):
            with open(os.path.join(dir, fname), 'r') as f:
                for line in f:
                    if line.startswith('Name='):
                        entry("exec",
                              "app {}".format(line.strip().split('=', 1)[1]),
                              "xdg-open {}".format(os.path.join(dir, fname)),
                              shell=True)
                        break
    except Exception as err:
        sys.stderr.write(err)

# Ssh hosts
try:
    with open(os.path.expanduser('~/.ssh/config'), 'r') as f:
        host_lines = [line.strip() for line in f if line.startswith('Host ')]
        for host_line in sorted(host_lines):
            host = host_line.split(' ', 1)[1]
            if host == '*':
                continue
            entry("autotype", "ssh {}".format(host), "ssh {}".format(host))
except Exception as err:
    sys.stderr.write(err)

# List of opened windows that can be switched to
try:
    p = subprocess.Popen("wmctrl -l", shell=True, stdout=subprocess.PIPE)
    stdout, stderr = p.communicate()
    for line in stdout.splitlines():
        line_utf = line.decode("utf-8")
        win_id = line_utf[0:10].strip()
        desktop = line_utf[11:13].strip()
        host, title = line_utf[14:].strip().split(' ', 1)
        entry("exec", "win {}".format(title), "wmctrl -a '{}'".format(title), shell=True)
except Exception as err:
    sys.stderr.write(err)

#TOTP / rfc6238 / two-factor / Google Authenticator
entry("totp", "totp github fboender", "qvnrFAKEg2cs5cgw")

# Chrome bookmarks
include_folders = ["/Check Later/News", "/Tools"]
def walk_bookmarks(tree, cur_path="", include=False):
    if cur_path in include_folders:
        include = True
    for child in tree["children"]:
        if child["type"] == "folder":
            walk_bookmarks(child, cur_path + "/" + child["name"], include)
        elif include is True:
            entry("browser", "bookmark {}".format(child["name"]), child["url"])

try:
    bookmarks = json.load(open(os.path.expanduser('~/.config/google-chrome/Default/Bookmarks'), 'r'))
    walk_bookmarks(bookmarks["roots"]["bookmark_bar"])
except Exception:
    pass

# Custom manual entries
entry("browser", "web search", "https://www.startpage.com/do/asearch?query={filter}", always=True)
entry("browser", "wikipedia search", "https://en.wikipedia.org/wiki/Special:Search?search={filter}&go=Go", always=True)
