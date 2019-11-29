- Only two of the environment variables are mandatory.
- This is because of `telethon.errors.rpc_error_list.ApiIdPublishedFloodError`
    - `APP_ID`:   You can get this value from https://my.telegram.org
    - `API_HASH`:   You can get this value from https://my.telegram.org
- The userbot will work without setting the non-mandatory environment variables.


## design

The modular design of the project enhances your Telegram experience
through [plugins](https://github.com/A-LoneWolf/uniborg/tree/master/stdplugins)
which you can enable or disable on demand.

Each plugin gets the `borg`, `logger`, `Config`, `tgbot` and `storage` magical
variables
to ease their use. Thus creating a plugin as easy as adding
a new file under the plugin directory to do the job:

```python
# stdplugins/myplugin.py
from telethon import events
from uniborg.util import admin_cmd

@borg.on(admin_cmd("hi"))
async def handler(event):
    await event.reply("hey")
```


## learning

Check out the already-mentioned [plugins](https://github.com/A-LoneWolf/UniBorg/tree/master/stdplugins) directory to learn how to write your own, and consider reading [Telethon's documentation](http://telethon.readthedocs.io/).
