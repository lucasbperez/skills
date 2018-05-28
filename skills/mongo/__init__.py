from opsdroid.matchers import match_regex

@match_regex(r'remember (.*)')
async def remember(opsdroid, config, message):
    remember = message.regex.group(1)
    await opsdroid.memory.put("remember", remember)
    await message.respond("OK I'll remember that")

@match_regex(r'remind me')
async def remember(opsdroid, config, message):
    information = await opsdroid.memory.get("remember")
    await message.respond(information)