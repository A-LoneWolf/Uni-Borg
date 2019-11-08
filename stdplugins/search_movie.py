"""

Search module Plugin by @A_L0neWolf
Syntax:
 .mflix <search query>
 .hflix <search query>
 .bflix <search query>
 .aflix <search query>

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

        await event.edit("Here is the result from moviesflix for {}:\n👉 [{}]({})\nReport Broken Link or Request movie [Here](https://t.me/moviesflixnet)".format(input_str,input_str,response_api.rstrip()))

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

        await event.edit("Here is the result from flixhubhd for {}:\n👉 [{}]({})\nReport Broken Link or Request movie [Here](https://t.me/flixhubmovie)".format(input_str,input_str,response_api.rstrip()))

    else:

        await event.edit("Something went wrong. Please try again later or report @A_L0neWolf.")


@borg.on(admin_cmd(pattern="aflix (.*)"))
async def _(event):

    if event.fwd_from:
        return

    input_str = event.pattern_match.group(1)
    sample_url = "https://da.gd/s?url=https://animeflix.in/?s={}&t=h_&ia=about".format(input_str.replace(" ","+"))
    response_api = requests.get(sample_url).text
    if response_api:

        await event.edit("Here is the result from animeflix for {}:\n👉 [{}]({})\nReport Broken Link or Request movie [Here](https://t.me/moviesflixnet)".format(input_str,input_str,response_api.rstrip()))

    else:

        await event.edit("Something went wrong. Please try again later or report @A_L0neWolf.")




@borg.on(admin_cmd(pattern="bflix (.*)"))
async def _(event):

    if event.fwd_from:
        return

    input_str = event.pattern_match.group(1)
    sample_url = "https://da.gd/s?url=https://bollyflix.in/?s={}&t=h_&ia=about".format(input_str.replace(" ","+"))
    response_api = requests.get(sample_url).text
    if response_api:

        await event.edit("Here is the result from bollyflix for {}:\n👉 [{}]({})\nReport Broken Link or Request movie [Here](https://t.me/moviesflixnet)".format(input_str,input_str,response_api.rstrip()))

    else:

        await event.edit("Something went wrong. Please try again later or report @A_L0neWolf.")
