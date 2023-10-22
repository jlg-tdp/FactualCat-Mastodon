# FactualCat on Mastodon

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/template/2C8OdB?referralCode=qZMlb1)

[@FactualCat](https://botsin.space/@FactualCat) is a bot on Mastodon that shares cat facts and pictures. It posts facts about cats sourced from the [Meow Facts API](https://github.com/wh-iterabb-it/meowfacts/tree/main) and pictures from [The Cat API](https://thecatapi.com/).

This project serves as a starting point for those interested in building bots on Mastodon. The bot is written in Python and utilizes [Mastodon.py](https://github.com/halcy/Mastodon.py).

## Getting Started 

1. First, set up an account for your bot. [BotsIn.Space](https://BotsIn.Space/) is a server dedicated to hosting bot accounts and is an ideal place to begin.
2. Configure your bot account in the account profile section, just as you would a regular account. This includes adding a bio, profile picture, heading, and any other desired metadata.
3. Ensure you check the box labeled "This is a bot account".
4. [Create a developer application](https://botsin.space/settings/applications) for your bot, ensuring it has scopes for `read`, `write`, and `follow`.
5. If needed, update your Redirect URI. However, the default `urn:ietf:wg:oauth:2.0:oob` should suffice for most testing purposes.

## Timing

The frequency at which the bot shares posts is governed by the schedule set in a [cron job](https://docs.railway.app/reference/cron-jobs). This schedule is defined within the `railway.toml` file. As of the current configuration, the bot is programmed to make a post every 6 hours.

```toml
[deploy]
cronSchedule = "0 */6 * * *"
```

The cronSchedule value `0 */6 * * *` translates to a post being made at the start of every 6-hour interval throughout the day.

## Using this Code Sample

1. Install the necessary packages using: `pip install -r requirements.txt`
2. To run the sample locally, execute: `python main.py`

## Resources 

- [Easy Guide to Building Mastodon Bots](https://shkspr.mobi/blog/2018/08/easy-guide-to-building-mastodon-bots/)
- [Getting Started with the Mastodon API in Python](https://martinheinz.dev/blog/86)
