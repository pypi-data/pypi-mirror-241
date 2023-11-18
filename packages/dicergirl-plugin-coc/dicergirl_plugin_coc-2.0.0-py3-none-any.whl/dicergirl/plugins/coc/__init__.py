from .investigator import Investigator
from .handlers import commands
from .cards import coc_cards, coc_cache_cards, coc_attrs_dict
from .backend import at, dam, ra, en
from .initialize import init


init()
coc_cards.load()

__version__ = "2.0.0"

__type__ = "plugin"
__charactor__ = Investigator
__name__ = "coc"
__cname__ = "调查员"
__cards__ = coc_cards
__cache__ = coc_cache_cards
__nbhandler__ = handlers
__nbcommands__ = commands
__commands__ = {
    "at": at,
    "dam": dam,
    "ra": ra,
    "en": en
}
__baseattrs__ = coc_attrs_dict
__description__ = "COC 模式是以H.P.洛夫克拉夫特《克苏鲁的呼唤(Call of Cthulhu)》为背景的 TRPG 跑团模式."