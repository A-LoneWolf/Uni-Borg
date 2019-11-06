"""

Let me search That For You Plugin by @A_L0neWolf
Syntax:
 .mflix <search query>
 .hflix <search query>

"""


from telethon import events
import os
import requests
import json
from uniborg.util import admin_cmd



@borg.on(admin_cmd(pattern="mflix (.*)"))
async def _(event):

    if event.fwd_from:
        return

    input_str = event.pattern_match.group(1)
    sample_url = "https://da.gd/s?url=https://moviezflix.in/?s={}&t=h_&ia=about".format(input_str.replace(" ","+"))
    response_api = requests.get(sample_url).text
    if response_api:

        await event.edit("Here is the result from moviesflix for {}:\n👉 [{}]({})\nReport Broken Link or Request movie [Here](https://t.me/moviesflixnet)\n`Thank me later 😉` @A_L0neWolf ".format(input_str,input_str,response_api.rstrip()))

    else:

        await event.edit("Something went wrong. Please try again later or report @A_L0neWolf.")


@borg.on(admin_cmd(pattern="hflix (.*)"))
async def _(event):

    if event.fwd_from:
        return

    input_str = event.pattern_match.group(1)
    sample_url = "https://da.gd/s?url=https://flixhubhd.com/?s={}&t=h_&ia=about".format(input_str.replace(" ","+"))
    response_api = requests.get(sample_url).text
    if response_api:

        await event.edit("Here is the result from flixhubhd for {}:\n👉 [{}]({})\nReport Broken Link or Request movie [Here](https://t.me/flixhubmovie)\n`Thank me later 😉` @A_L0neWolf ".format(input_str,input_str,response_api.rstrip()))

    else:

        await event.edit("Something went wrong. Please try again later or report @A_L0neWolf.")

