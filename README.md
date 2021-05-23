# Infinity Request

![Discord](https://img.shields.io/badge/Discord-project-brightgreen)
![python](https://img.shields.io/badge/Language-Python-blueviolet)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## About

> :warning: This project is a POC of a request bot. It was done quickly, and may have bugs.

Infinity Request is a bot that allows people to "raise their hand" by putting a command on discord. Once accepted by
another person, a support category is created.

Here is the list of available commands: 
- `!request <content>` allows you to start a request
- `!cancel`allows you to cancel a request
- `!place` allows you to know your place in the queue
- `!enable` [MOD] allows you to open the queue
- `!disable` [MOD] allows you to close the queue

## Getting started

1. **First, you will have to clone the project.**

```shell
git clone git@github.com:gastbob40/infinity-request.git
```


2. **Create a `virtual environment`, in order to install dependencies locally.** For more information about virtual environments, [click here](https://docs.python.org/3/library/venv.html).

```shell
python -m venv venv
```


3. **Activate the virtual environment**

Linux/macOS:

```shell
# Using bash/zsh
source venv/bin/activate
# Using fish
. venv/bin/activate.fish
# Using csh/tcsh
source venv/bin/activate.csh
``` 

Windows:

```
# cmd.exe
.venv\Scripts\activate.bat
# PowerShell
.venv\Scripts\Activate.ps1
```


4. **Finally, install the dependencies**

````shell
pip install -r requirements.txt
````

5. **Configure Infinity Request**. This is necessary to use the bot. Check the next section for instructions.

6. **Run `python index.py` to launch Infinity Request.** Also make sure that the venv is activated when you launch EpiModo (you should see `venv` to the left of your command prompt).

## Configuration

The `run/config` folder contains all the data of the program configuration.

This `token.default.yml` file contain all data about thge bot. This file looks like this:

```yaml
discord_token: ~          # A discord bot token
request_channel_id: ~     # The channel ID to put request message of user
guild_id: ~               # The ID of the guild where the bot should be use
teacher_ids: ~            # A *list* of discord ID of teachers
```

You must fill in the file and rename it to `tokens.yml`.
Warning, `teacher_ids` is a list of Discord user IDs.
