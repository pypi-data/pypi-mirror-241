from .adventurer import Adventurer
from .dndcards import dnd_cache_cards, dnd_cards, dnd_rolls

from dicergirl.utils.utils import format_msg, get_status, get_mentions, is_super_user
from dicergirl.handlers.on import on_startswith
from dicergirl.utils.parser import CommandParser, Commands, Only, Optional, Required

from nonebot.matcher import Matcher
from nonebot.adapters import Bot as Bot
from nonebot.adapters.onebot.v11 import Bot as V11Bot
from nonebot.internal.matcher.matcher import Matcher
from nonebot.adapters.onebot.v11 import GroupMessageEvent

dndcommand = on_startswith(".dnd", priority=1, block=True).handle()

async def dnd_handler(matcher: Matcher, event: GroupMessageEvent):
    """ DND 车卡指令 """
    if not get_status(event) and not event.to_me:
        return

    args = format_msg(event.get_message(), begin=".dnd", zh_en=True)
    qid = event.get_user_id()
    commands = CommandParser(
        Commands([
            Only("cache", False),
            Optional("set", int),
            Optional("age", int, 20),
            Optional("name", str),
            Optional("sex", str, "女"),
            Optional("roll", int, 1)
            ]),
        args=args,
        auto=True
        ).results
    toroll = commands["roll"]

    if commands["set"] or commands["set"] == 0:
        dnd_cards.update(event, dnd_rolls[qid][commands["set"]], save=True)
        adv = Adventurer().load(dnd_rolls[qid][commands["set"]])
        await matcher.send(f"使用序列 {commands['set']} 卡:\n{adv.output()}")
        dnd_rolls[qid] = {}
        return

    age = commands["age"]
    name = commands["name"]

    reply = ""
    if qid in dnd_rolls.keys():
        rolled = len(dnd_rolls[qid].keys())
    else:
        dnd_rolls[qid] = {}
        rolled = 0

    for i in range(toroll):
        adv = Adventurer()
        adv.age_check(age)
        adv.sex = commands["sex"]
        adv.init()
        if adv.int[0] <= 8:
            reply += "天命: null\n很遗憾, 检定新的冒险者智力不足, 弱智是不允许成为冒险者的, 该天命作废.\n"
            continue

        if name:
            adv.name = name

        dnd_rolls[qid][rolled+i] = adv.__dict__
        count = adv.rollcount()
        reply += f"天命编号: {rolled+i}\n"
        reply += adv.output() + "\n"
        reply += f"共计: {count[0]}/{count[1]}\n"

    if toroll == 1:
        dnd_cache_cards.update(event, adv.__dict__, save=False)

    reply.rstrip("\n")
    await matcher.send(reply)

commands = {"dndcommand": "dnd_handler"}