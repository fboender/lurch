# Lurch - the ugly assistant

Lurch is a unixy launcher and auto-typer. *Some assembly required*.

It presents the user with a fuzzy filterable list of entries. When activated,
the entries can do any number of things. For example: auto-type your password
in the currently focussed window, open URLs or run programs and scripts.

Lurch is unixy. It reads entries to show and filter from stdin. This allows
you to have complete control over what Lurch lets you do and in which order it
shows the entries. You can feed Lurch dynamically generated entries, have
multiple Lurches that do different things and even Lurches that launch
sub-lurches.

**NO SUPPORT: There is absolutely ZERO support on this project. Due to time
constraints, I don't take bug or features reports and probably won't accept
your pull requests.**

This is what it looks like. Ugly, but effective.

![](https://raw.githubusercontent.com/fboender/lurch/master/screenshot.png)

## Features

* Fuzzy filtering as-you-type.
* Execute commands.
* Open new browser tabs.
* Auto-type into currently focussed window
* Auto-type TOTP / rfc6238 / two-factor / Google Authenticator codes.
* Unixy and composable. Reads entries from stdin.

You can use and combine these features to do many things:

* Auto-type passwords
* Switch between currently opened windows by typing a part of its title (using
  wmctrl to list and switch to windows)
* As a generic (and very customizable) application launcher by parsing
  .desktop entries or whatever.
* Quickly `cd` to parts of your filesystem using auto-type.
* Open browser tabs and search via google or specific search engines.
* List all entries in your SSH configuration and quickly launch an ssh session
  to one of them.
* Etc.


## Requirements

* A window manager that lets you launch applications through a keybinding.
* Python v3.4
* Python Tkinter
* Some python libs (see `requirements.txt`)


## Installation

    git clone git@github.com:fboender/lurch.git
    cd lurch
    sudo pip3 install -r requirements.txt
    sudo apt install python3-tk
    make install


## Usage

Pass input into Lurch:

    $ lurch < entries.txt

Or from a script:

    $ ./gen_entries.py | lurch

You'll want to instruct your window manager to bind a key combination that
launches Lurch. Otherwise, it's mostly pointless.

The input is a list of entries to show, separated with an empty line. For
example:

    type: autotype
    title: pass fboender@server.example.com
    value: MyS3cr3tPasw0rd

    type: exec
    title: cmd edit SSH configuration
    value: tilix -e vi /home/fboender/.ssh/config
    shell: true

    type: totp
    title: totp github fboender
    value: 2URYDFAKEKMH66KK

    type: browser
    title: web search
    value: https://www.startpage.com/do/asearch?query={filter}
    always: true


The text `{filter}` is replaced with whatever the user typed in.


You can generate input with a script. This lets you build dynamic filter lists
such as entries to ssh to all the hosts in your `~/.ssh/config` file, XDG
Desktop entries, passwords from your password manager, directories to switch
to, etc. *Some assembly required*.

An example generator is included: `gen_entries.sh`. It may or may not work
properly for you. Build your own.

Each item in the list takes a few default keys:

* **`type`**: One of `autotype`, `browser`, `exec` or `totp`.
* **`title`**: The title shown as the entry by Lurch.
* **`value`**: Usually the actual thing Lurch will do.
* **`always`**: Always show the entry, regardless of what the user typed.

The types should speak for themselves. Some take extra options:

* **`exec`**:
    * `shell`: Launch the command in a shell. Defaults to `false`.

## Frequently Asked Questions I made up

* "**I found a bug...**".

    I don't provide support for this project.

* "**I'd like feature...**".

    I don't provide support for this project.

* "**It doesn't work...**".

    I don't provide support for this project.

* "**How do I...**".

    I don't provide support for this project.

* **Isn't storing passwords / secrets in plain text insecure?**

    `chmod 600`, encrypt your disk and lock your PC when you're not around.

* **You seem rude...**.

    I'm sorry! I'm very pressed for time, so I don't like wasting it on
    non-essential things. Being polite is not essential in this case. ;-)

## License

MIT License

    Copyright (c) 2018 Ferry Boender

    Permission is hereby granted, free of charge, to any person obtaining a
    copy of this software and associated documentation files (the "Software"),
    to deal in the Software without restriction, including without limitation
    the rights to use, copy, modify, merge, publish, distribute, sublicense,
    and/or sell copies of the Software, and to permit persons to whom the
    Software is furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in
    all copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
    THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
    FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
    DEALINGS IN THE SOFTWARE.

