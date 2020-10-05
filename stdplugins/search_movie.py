"""

Syntax:
 .mverse <search query>
 .bflix <search query>
 .aflix <search query>
 .mnation <search query>
"""


from telethon import events
import os
import requests
import json
from uniborg.util import admin_cmd



@borg.on(admin_cmd(pattern="mverse (.*)"))
async def _(event):

    if event.fwd_from:
        return

    input_str = event.pattern_match.group(1)
    sample_url = "https://da.gd/s?url=https://moviesverse.com/?s={}&t=h_&ia=about".format(input_str.replace(" ","+"))
    response_api = requests.get(sample_url).text
    if response_api:

        await event.edit("Here is the result from moviesverse for {}:\n👉 [{}]({})\nReport Broken Link or Request movie [Here](https://t.me/moviesflixnet)".format(input_str,input_str,response_api.rstrip()))

    else:

        await event.edit("Something went wrong. Please try again later")


@borg.on(admin_cmd(pattern="mnation (.*)"))
async def _(event):

    if event.fwd_from:
        return

    input_str = event.pattern_match.group(1)
    sample_url = "https://da.gd/s?url=https://moviesnation.in/?s={}&t=h_&ia=about".format(input_str.replace(" ","+"))
    response_api = requests.get(sample_url).text
    if response_api:

        await event.edit("Here is the result from [MoviesNation](Moviesnation.in) for {}:\n👉 [{}]({})\nReport Broken Link or Request movie [Here](https://t.me/joinchat/OC-vh0_o_IH3KVtxRsigvg)".format(input_str,input_str,response_api.rstrip()))

    else:

        await event.edit("Something went wrong. Please try again later")


@borg.on(admin_cmd(pattern="aflix (.*)"))
async def _(event):

    if event.fwd_from:
        return

    input_str = event.pattern_match.group(1)
    sample_url = "https://da.gd/s?url=https://animeflix.in/?s={}&t=h_&ia=about".format(input_str.replace(" ","+"))
    response_api = requests.get(sample_url).text
    if response_api:

        await event.edit("Here is the result from animeflix for {}:\n👉 [{}]({})\nReport Broken Link or Request movie [Here](https://t.me/animeflixin)".format(input_str,input_str,response_api.rstrip()))

    else:

        await event.edit("Something went wrong. Please try again later")




@borg.on(admin_cmd(pattern="bflix (.*)"))
async def _(event):

    if event.fwd_from:
        return

    input_str = event.pattern_match.group(1)
    sample_url = "https://da.gd/s?url=https://bollyflixhd.xyz/?s={}&t=h_&ia=about".format(input_str.replace(" ","+"))
    response_api = requests.get(sample_url).text
    if response_api:

        await event.edit("Here is the result from bollyflix for {}:\n👉 [{}]({})\nReport Broken Link or Request movie [Here](https://t.me/moviesflixnet)".format(input_str,input_str,response_api.rstrip()))

    else:

        await event.edit("Something went wrong. Please try again later")
