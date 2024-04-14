import asyncio
import datetime

from prettytable import PrettyTable
from pyrogram import Client, filters
from config import OWNER_ID
from config import CMD_HANDLER as cmd

from X.helpers.aiohttp_helper import AioHttp

from .help import *

@Client.on_message(filters.command("corona", cmd) & filters.me)
async def corona_all(client, message):
    try:
        r = await AioHttp().get_json("https://api.rootnet.in/covid19-in/stats/latest")
        data = r["data"]["summary"]
        last_refreshed = r["lastRefreshed"]
        
        ac = PrettyTable()
        ac.header = False
        ac.title = "Global Statistics"
        ac.add_row(["Total Cases", f"{data['total']:,}"])
        ac.add_row(["Cases Today", f"{data['confirmedCasesIndian'] + data['confirmedCasesForeign']:,}"])
        ac.add_row(["Deaths", f"{data['deaths']:,}"])
        ac.add_row(["Deaths Today", "N/A"])
        ac.add_row(["Recovered", f"{data['discharged']:,}"])
        ac.add_row(["Active", f"{data['total'] - data['discharged'] - data['deaths']:,}"])
        ac.add_row(["Critical", "N/A"])
        ac.add_row(["Cases/Million", "N/A"])
        ac.add_row(["Deaths/Million", "N/A"])
        ac.add_row(["Tests", "N/A"])
        ac.add_row(["Tests/Million", "N/A"])
        ac.align = "l"

        await message.edit(f"```{str(ac)}```\nLast updated on: {last_refreshed}")
    except Exception as e:
        await message.edit("`The corona API could not be reached`")
        await asyncio.sleep(3)
        await message.delete()

# Ensure to maintain other functions and imports as per your requirement.


@Client.on_message(filters.command("coronasrch", cmd) & filters.me)
async def corona_search(client, message):
    cmd = message.command

    if not (len(cmd) >= 2):
        await message.edit("```Not enough params provided```")
        await asyncio.sleep(3)
        await message.delete()
        return

    country = cmd[1]
    await message.edit(f"```Getting Corona statistics for {country}```")

    r = await AioHttp().get_json(f"https://api.api-ninjas.com/v1/covid19?country=/{country}")
    if "cases" not in r:
        await message.edit("```The country could not be found!```")
        await asyncio.sleep(3)
        await message.delete()
    else:
        last_updated = datetime.datetime.fromtimestamp(r["updated"] / 1000).strftime(
            "%Y-%m-%d %I:%M:%S"
        )

        cc = PrettyTable()
        cc.header = False
        country = r["countryInfo"]["iso3"] if len(r["country"]) > 12 else r["country"]
        cc.title = f"Corona Cases in {country}"
        cc.add_row(["Cases", f"{r['cases']:,}"])
        cc.add_row(["Cases Today", f"{r['todayCases']:,}"])
        cc.add_row(["Deaths", f"{r['deaths']:,}"])
        cc.add_row(["Deaths Today", f"{r['todayDeaths']:,}"])
        cc.add_row(["Recovered", f"{r['recovered']:,}"])
        cc.add_row(["Active", f"{r['active']:,}"])
        cc.add_row(["Critical", f"{r['critical']:,}"])
        cc.add_row(["Cases/Million", f"{r['casesPerOneMillion']:,}"])
        cc.add_row(["Deaths/Million", f"{r['deathsPerOneMillion']:,}"])
        cc.add_row(["Tests", f"{r['tests']:,}"])
        cc.add_row(["Tests/Million", f"{r['testsPerOneMillion']:,}"])
        cc.align = "l"
        await message.edit(f"```{str(cc)}```\nLast updated on: {last_updated}")


add_command_help(
    "corona",
    [
        [".corona", "Sends global corona stats: cases, deaths, recovered, and active cases"],
        [
            ".coronasrch Country",
            "Sends cases, new cases, deaths, new deaths, recovered, active cases, critical cases, "
            "and cases/deaths per one million people for a specific country",
        ],
    ],
      ) 
