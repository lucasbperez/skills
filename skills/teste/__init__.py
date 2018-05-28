from opsdroid.matchers import match_regex

@match_regex(r"(h|H)ow are yo(u\?|u)")
async def how_are_you(opsdroid, config, message):
    await message.respond("I'm fine thanks!")
