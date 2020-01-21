#!/usr/bin/env python3

import iterm2


# Thanks to Emojipedia(https://emojipedia.org)
animals = [
    "🐒", "🦍", "🐕", "🦝", "🐈",
    "🐅", "🐆", "🐎", "🦓", "🦌",
    "🐂", "🐄", "🐖", "🐏", "🦙",
    "🦒", "🐘", "🐁", "🐿️", "🐇",
    "🦘", "🐓", "🦆", "🐢", "🐍",
    ] * 4


async def main(connection):
    component = iterm2.StatusBarComponent(
        short_description="Animal Bar",
        detailed_description="Show Animals Bar",
        knobs=[],
        exemplar="[Animals Bar]",
        update_cadence=1,
        identifier="koh-sh.iterm2-animalbar"
    )

    @iterm2.StatusBarRPC
    async def animalbar(knobs):
        first = animals[0]
        animals.remove(first)
        animals.append(first)
        ret = ["\r{}".format("  ".join(animals[:i])) for i in range(len(animals), 0, -1)]
        return ret

    await component.async_register(connection, animalbar)

iterm2.run_forever(main)
