from dicergirl.utils.docimasy import dnd_doc
from dicergirl.utils.dicer import Dicer
from .dndcards import dnd_cards, dnd_attrs_dict as attrs_dict
from .adventurer import Adventurer

def dnd_at(event, args):
    inv = Adventurer().load(dnd_cards.get(event))
    method = "+"

    if args:
        d = Dicer().parse(args).roll()
    else:
        d = Dicer().parse("1d6").roll()

    if "d" in inv.db():
        db = Dicer(inv.db()).roll()
        dbtotal = db.outcome
        db = db.db
    else:
        db = int(inv.db())
        dbtotal = db
        if db < 0:
            method = ""

    return f"投掷 {d.db}{method}{db}=({d.outcome}+{dbtotal})={d.outcome+dbtotal}\n造成了 {d.outcome+dbtotal}点 伤害."

def dnd_dam(event, args):
    card = dnd_cards.get(event)
    if not card:
        return "未找到缓存数据, 请先使用`.dnd`指令进行车卡生成角色卡并`.set`进行保存."
    max_hp = card["hp_max"]
    if len(args) == 1:
        if not args[0] in ["check", "c"]:
            arg = int(args[0])
            card["hp"] -= arg
            r = f"[Orcale] {card['name']} 失去了 {arg}点 生命"
        else:
            r = "检查特工状态"
    elif len(args) == 0:
        d = Dicer().parse("1d6").roll()
        card["hp"] -= d.outcome
        r = "投掷 1D6={d}\n受到了 {d}点 伤害".format(d=d.calc())
    elif len(args) == 3:
        if args[1] != "d":
            r = "未知的指令格式."
        else:
            d = Dicer().parse(f"{args[0]}{args[1]}{args[2]}").roll()
            card["hp"] -= d.outcome
            r = f"投掷 {args[0]}D{args[2]}={d.calc()}\n受到了 {d.calc()}点 伤害"
    if card["hp"] <= 0:
        card["hp"] = 0
        r += f", 特工 {card['name']} 已死亡."
    elif (max_hp * 0.8 <= card["hp"]) and (card["hp"] < max_hp):
        r += f", 特工 {card['name']} 具有轻微伤势."
    elif (max_hp * 0.6 <= card["hp"]) and (card['hp'] <= max_hp * 0.8):
        r += f", 特工 {card['name']} 具有轻微伤."
    elif (max_hp * 0.4 <= card["hp"]) and (card["hp"] <= max_hp * 0.6):
        r += f", 特工 {card['name']} 具有轻伤."
    elif (max_hp * 0.2 <= card["hp"]) and (card["hp"] <= max_hp * 0.4):
        r += f", 特工 {card['name']} 身负重伤."
    elif max_hp * 0.2 >= card["hp"]:
        r += f", 特工 {card['name']} 濒死."
    else:
        r += "."
    dnd_cards.update(event, card)
    return r

def dnd_ra(event, args):
    if len(args) == 0:
        return "你在整什么花活, 技能检定没技能可还行."
    if len(args) > 2:
        return "错误: 参数过多(最多2需要但%d给予)." % len(args)

    if len(args) == 2:
        dc = int(args[1])
    else:
        dc = 12

    card_data = dnd_cards.get(event)
    if not card_data:
        return "在执行参数检定前, 请先执行`.dnd`车卡并执行`.set`保存."

    inv = Adventurer().load(card_data)
    is_base = False
    for _, alias in attrs_dict.items():
        if args[0] in alias:
            v = int(eval("inv.{prop}".format(prop=alias[0]))[1])
            is_base = True
            break

    is_skill = False
    if not is_base:
        for skill in inv.skills:
            if args[0] == skill:
                v = int(inv.skills[skill])
                is_skill = True
                break

    if not is_base and not is_skill:
        return "唔, 没有这个数据或技能."

    outcome = Dicer("1d20").roll().calc() + v
    return dnd_doc(outcome, dc, adventurer=card_data["name"])