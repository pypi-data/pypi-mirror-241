from .adventurer import Adventurer
from .nbhandlers import commands
from .dndcards import dnd_cards, dnd_cache_cards, dnd_attrs_dict
from .dndutils import dnd_at, dnd_dam, dnd_ra

dnd_cards.load()

__version__ = "1.1.0"

__type__ = "plugin"
__charactor__ = Adventurer
__name__ = "dnd"
__cname__ = "冒险者"
__cards__ = dnd_cards
__cache__ = dnd_cache_cards
__nbhandler__ = nbhandlers
__nbcommands__ = commands
__commands__ = {
    "at": dnd_at,
    "dam": dnd_dam,
    "ra": dnd_ra,
}
__baseattrs__ = dnd_attrs_dict
__description__ = "DND 模式是以游戏 龙与地下城(Dungeons & Dragons) 为背景的 TRPG 跑团模式."