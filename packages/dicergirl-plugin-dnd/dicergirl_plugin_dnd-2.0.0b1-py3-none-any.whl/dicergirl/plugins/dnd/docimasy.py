import random


def dnd_doc(result, dc, adventurer=None):
    """DND 技能检定结果"""
    if not adventurer:
        adventurer = "该冒险者"
    r = f"事件难度: {dc}\n"
    r += f"检定数据: {result}\n"
    if result >= 20:
        r += "检定结果: 大成功.\n"
        r += "检定结论: 被命运眷顾的幸运者, 这毫无疑问是一次完美的成功."
    elif result > dc:
        r += "检定结果: 成功.\n"
        r += "检定结论: 前进吧, 冒险者, 异世的诗篇还在等着你."
    elif result <= dc / 2:
        r += "检定结果: 大失败.\n"
        r += "检定结论: 冒险不是自寻死路, 有时候, 放弃也是一个好的选择."
    elif result < dc:
        r += "检定结果: 失败.\n"
        r += "检定结论: 成功与失败总是相辅相成, 不要让一次失败打倒你."
    else:
        result = random.randint(0, 1)
        if result:
            r += "检定结果: 成功.\n"
            r += "检定结论: 小心, 你的成功完全是一次偶然, 不要认为这样的偶然稀松平常, 冷静与冲动并存, 才是一个合格的冒险者."
        else:
            r += "检定结果: 失败.\n"
            r += "检定结论: 成功与失败由于一体两面, 无论是哪一种都是可能的, 但是你不必气馁, 失败与成功都是冒险的一部分."
    return r
