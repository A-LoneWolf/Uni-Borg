"""Get Syntax of plugins
`.syntax` <plugin name>
`.exec ls stdplugins` to get List of the plugins 
"""


from uniborg.util import admin_cmd


@borg.on(admin_cmd(pattern="syntax (.*)"))
async def _(event):
    if event.fwd_from:
        return
    plugin_name = event.pattern_match.group(1)
    if plugin_name in borg._plugins:
        help_string = borg._plugins[plugin_name].__doc__
        unload_string = f"Use `.unload {plugin_name}` to remove this plugin.\n"
        if help_string:
            plugin_syntax = f"Syntax for plugin **{plugin_name}**:\n\n\n{help_string}\n{unload_string}"
        else:
            plugin_syntax = f"No DOCSTRING has been setup for {plugin_name} plugin"
    else:
        plugin_syntax = "Enter valid **Plugin** name.\nDo `.exec ls stdplugins` or `.helpme` to get list of valid plugin names."
    await event.edit(plugin_syntax)
