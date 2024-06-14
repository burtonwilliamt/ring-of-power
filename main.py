import racket

import settings
from ring_of_power import RingOfPower


def main():
    racket.run_cog(RingOfPower, token=settings.BOT_TOKEN, guilds=settings.GUILD_IDS)


if __name__ == "__main__":
    main()
