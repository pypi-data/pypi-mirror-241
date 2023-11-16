# coding: UTF-8
import sys
bstack1ll111l_opy_ = sys.version_info [0] == 2
bstack111ll1_opy_ = 2048
bstack1llll1_opy_ = 7
def bstack111ll1l_opy_ (bstack11llll_opy_):
    global bstack111lll1_opy_
    bstack111l1_opy_ = ord (bstack11llll_opy_ [-1])
    bstack1ll1lll_opy_ = bstack11llll_opy_ [:-1]
    bstack11111l1_opy_ = bstack111l1_opy_ % len (bstack1ll1lll_opy_)
    bstack1l111l_opy_ = bstack1ll1lll_opy_ [:bstack11111l1_opy_] + bstack1ll1lll_opy_ [bstack11111l1_opy_:]
    if bstack1ll111l_opy_:
        bstack1111l11_opy_ = unicode () .join ([unichr (ord (char) - bstack111ll1_opy_ - (bstack11ll111_opy_ + bstack111l1_opy_) % bstack1llll1_opy_) for bstack11ll111_opy_, char in enumerate (bstack1l111l_opy_)])
    else:
        bstack1111l11_opy_ = str () .join ([chr (ord (char) - bstack111ll1_opy_ - (bstack11ll111_opy_ + bstack111l1_opy_) % bstack1llll1_opy_) for bstack11ll111_opy_, char in enumerate (bstack1l111l_opy_)])
    return eval (bstack1111l11_opy_)
import re
from bstack_utils.bstack11ll1l11l1_opy_ import bstack11ll1lll11_opy_
def bstack11ll1l1l1l_opy_(fixture_name):
    if fixture_name.startswith(bstack111ll1l_opy_ (u"ࠨࡡࡻࡹࡳ࡯ࡴࡠࡵࡨࡸࡺࡶ࡟ࡧࡷࡱࡧࡹ࡯࡯࡯ࡡࡩ࡭ࡽࡺࡵࡳࡧࠪᇸ")):
        return bstack111ll1l_opy_ (u"ࠩࡶࡩࡹࡻࡰ࠮ࡨࡸࡲࡨࡺࡩࡰࡰࠪᇹ")
    elif fixture_name.startswith(bstack111ll1l_opy_ (u"ࠪࡣࡽࡻ࡮ࡪࡶࡢࡷࡪࡺࡵࡱࡡࡰࡳࡩࡻ࡬ࡦࡡࡩ࡭ࡽࡺࡵࡳࡧࠪᇺ")):
        return bstack111ll1l_opy_ (u"ࠫࡸ࡫ࡴࡶࡲ࠰ࡱࡴࡪࡵ࡭ࡧࠪᇻ")
    elif fixture_name.startswith(bstack111ll1l_opy_ (u"ࠬࡥࡸࡶࡰ࡬ࡸࡤࡺࡥࡢࡴࡧࡳࡼࡴ࡟ࡧࡷࡱࡧࡹ࡯࡯࡯ࡡࡩ࡭ࡽࡺࡵࡳࡧࠪᇼ")):
        return bstack111ll1l_opy_ (u"࠭ࡴࡦࡣࡵࡨࡴࡽ࡮࠮ࡨࡸࡲࡨࡺࡩࡰࡰࠪᇽ")
    elif fixture_name.startswith(bstack111ll1l_opy_ (u"ࠧࡠࡺࡸࡲ࡮ࡺ࡟ࡵࡧࡤࡶࡩࡵࡷ࡯ࡡࡩࡹࡳࡩࡴࡪࡱࡱࡣ࡫࡯ࡸࡵࡷࡵࡩࠬᇾ")):
        return bstack111ll1l_opy_ (u"ࠨࡶࡨࡥࡷࡪ࡯ࡸࡰ࠰ࡱࡴࡪࡵ࡭ࡧࠪᇿ")
def bstack11ll1l111l_opy_(fixture_name):
    return bool(re.match(bstack111ll1l_opy_ (u"ࠩࡡࡣࡽࡻ࡮ࡪࡶࡢࠬࡸ࡫ࡴࡶࡲࡿࡸࡪࡧࡲࡥࡱࡺࡲ࠮ࡥࠨࡧࡷࡱࡧࡹ࡯࡯࡯ࡾࡰࡳࡩࡻ࡬ࡦࠫࡢࡪ࡮ࡾࡴࡶࡴࡨࡣ࠳࠰ࠧሀ"), fixture_name))
def bstack11ll1l1l11_opy_(fixture_name):
    return bool(re.match(bstack111ll1l_opy_ (u"ࠪࡢࡤࡾࡵ࡯࡫ࡷࡣ࠭ࡹࡥࡵࡷࡳࢀࡹ࡫ࡡࡳࡦࡲࡻࡳ࠯࡟࡮ࡱࡧࡹࡱ࡫࡟ࡧ࡫ࡻࡸࡺࡸࡥࡠ࠰࠭ࠫሁ"), fixture_name))
def bstack11ll1ll111_opy_(fixture_name):
    return bool(re.match(bstack111ll1l_opy_ (u"ࠫࡣࡥࡸࡶࡰ࡬ࡸࡤ࠮ࡳࡦࡶࡸࡴࢁࡺࡥࡢࡴࡧࡳࡼࡴࠩࡠࡥ࡯ࡥࡸࡹ࡟ࡧ࡫ࡻࡸࡺࡸࡥࡠ࠰࠭ࠫሂ"), fixture_name))
def bstack11ll1l1lll_opy_(fixture_name):
    if fixture_name.startswith(bstack111ll1l_opy_ (u"ࠬࡥࡸࡶࡰ࡬ࡸࡤࡹࡥࡵࡷࡳࡣ࡫ࡻ࡮ࡤࡶ࡬ࡳࡳࡥࡦࡪࡺࡷࡹࡷ࡫ࠧሃ")):
        return bstack111ll1l_opy_ (u"࠭ࡳࡦࡶࡸࡴ࠲࡬ࡵ࡯ࡥࡷ࡭ࡴࡴࠧሄ"), bstack111ll1l_opy_ (u"ࠧࡃࡇࡉࡓࡗࡋ࡟ࡆࡃࡆࡌࠬህ")
    elif fixture_name.startswith(bstack111ll1l_opy_ (u"ࠨࡡࡻࡹࡳ࡯ࡴࡠࡵࡨࡸࡺࡶ࡟࡮ࡱࡧࡹࡱ࡫࡟ࡧ࡫ࡻࡸࡺࡸࡥࠨሆ")):
        return bstack111ll1l_opy_ (u"ࠩࡶࡩࡹࡻࡰ࠮࡯ࡲࡨࡺࡲࡥࠨሇ"), bstack111ll1l_opy_ (u"ࠪࡆࡊࡌࡏࡓࡇࡢࡅࡑࡒࠧለ")
    elif fixture_name.startswith(bstack111ll1l_opy_ (u"ࠫࡤࡾࡵ࡯࡫ࡷࡣࡹ࡫ࡡࡳࡦࡲࡻࡳࡥࡦࡶࡰࡦࡸ࡮ࡵ࡮ࡠࡨ࡬ࡼࡹࡻࡲࡦࠩሉ")):
        return bstack111ll1l_opy_ (u"ࠬࡺࡥࡢࡴࡧࡳࡼࡴ࠭ࡧࡷࡱࡧࡹ࡯࡯࡯ࠩሊ"), bstack111ll1l_opy_ (u"࠭ࡁࡇࡖࡈࡖࡤࡋࡁࡄࡊࠪላ")
    elif fixture_name.startswith(bstack111ll1l_opy_ (u"ࠧࡠࡺࡸࡲ࡮ࡺ࡟ࡵࡧࡤࡶࡩࡵࡷ࡯ࡡࡰࡳࡩࡻ࡬ࡦࡡࡩ࡭ࡽࡺࡵࡳࡧࠪሌ")):
        return bstack111ll1l_opy_ (u"ࠨࡶࡨࡥࡷࡪ࡯ࡸࡰ࠰ࡱࡴࡪࡵ࡭ࡧࠪል"), bstack111ll1l_opy_ (u"ࠩࡄࡊ࡙ࡋࡒࡠࡃࡏࡐࠬሎ")
    return None, None
def bstack11ll1llll1_opy_(hook_name):
    if hook_name in [bstack111ll1l_opy_ (u"ࠪࡷࡪࡺࡵࡱࠩሏ"), bstack111ll1l_opy_ (u"ࠫࡹ࡫ࡡࡳࡦࡲࡻࡳ࠭ሐ")]:
        return hook_name.capitalize()
    return hook_name
def bstack11ll1l1111_opy_(hook_name):
    if hook_name in [bstack111ll1l_opy_ (u"ࠬࡹࡥࡵࡷࡳࡣ࡫ࡻ࡮ࡤࡶ࡬ࡳࡳ࠭ሑ"), bstack111ll1l_opy_ (u"࠭ࡳࡦࡶࡸࡴࡤࡳࡥࡵࡪࡲࡨࠬሒ")]:
        return bstack111ll1l_opy_ (u"ࠧࡃࡇࡉࡓࡗࡋ࡟ࡆࡃࡆࡌࠬሓ")
    elif hook_name in [bstack111ll1l_opy_ (u"ࠨࡵࡨࡸࡺࡶ࡟࡮ࡱࡧࡹࡱ࡫ࠧሔ"), bstack111ll1l_opy_ (u"ࠩࡶࡩࡹࡻࡰࡠࡥ࡯ࡥࡸࡹࠧሕ")]:
        return bstack111ll1l_opy_ (u"ࠪࡆࡊࡌࡏࡓࡇࡢࡅࡑࡒࠧሖ")
    elif hook_name in [bstack111ll1l_opy_ (u"ࠫࡹ࡫ࡡࡳࡦࡲࡻࡳࡥࡦࡶࡰࡦࡸ࡮ࡵ࡮ࠨሗ"), bstack111ll1l_opy_ (u"ࠬࡺࡥࡢࡴࡧࡳࡼࡴ࡟࡮ࡧࡷ࡬ࡴࡪࠧመ")]:
        return bstack111ll1l_opy_ (u"࠭ࡁࡇࡖࡈࡖࡤࡋࡁࡄࡊࠪሙ")
    elif hook_name in [bstack111ll1l_opy_ (u"ࠧࡵࡧࡤࡶࡩࡵࡷ࡯ࡡࡰࡳࡩࡻ࡬ࡦࠩሚ"), bstack111ll1l_opy_ (u"ࠨࡶࡨࡥࡷࡪ࡯ࡸࡰࡢࡧࡱࡧࡳࡴࠩማ")]:
        return bstack111ll1l_opy_ (u"ࠩࡄࡊ࡙ࡋࡒࡠࡃࡏࡐࠬሜ")
    return hook_name
def bstack11ll1l1ll1_opy_(node, scenario):
    if hasattr(node, bstack111ll1l_opy_ (u"ࠪࡧࡦࡲ࡬ࡴࡲࡨࡧࠬም")):
        parts = node.nodeid.rsplit(bstack111ll1l_opy_ (u"ࠦࡠࠨሞ"))
        params = parts[-1]
        return bstack111ll1l_opy_ (u"ࠧࢁࡽࠡ࡝ࡾࢁࠧሟ").format(scenario.name, params)
    return scenario.name
def bstack11ll1ll1l1_opy_(node):
    try:
        examples = []
        if hasattr(node, bstack111ll1l_opy_ (u"࠭ࡣࡢ࡮࡯ࡷࡵ࡫ࡣࠨሠ")):
            examples = list(node.callspec.params[bstack111ll1l_opy_ (u"ࠧࡠࡲࡼࡸࡪࡹࡴࡠࡤࡧࡨࡤ࡫ࡸࡢ࡯ࡳࡰࡪ࠭ሡ")].values())
        return examples
    except:
        return []
def bstack11ll1lll1l_opy_(feature, scenario):
    return list(feature.tags) + list(scenario.tags)
def bstack11ll1l11ll_opy_(report):
    try:
        status = bstack111ll1l_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨሢ")
        if report.passed or (report.failed and hasattr(report, bstack111ll1l_opy_ (u"ࠤࡺࡥࡸࡾࡦࡢ࡫࡯ࠦሣ"))):
            status = bstack111ll1l_opy_ (u"ࠪࡴࡦࡹࡳࡦࡦࠪሤ")
        elif report.skipped:
            status = bstack111ll1l_opy_ (u"ࠫࡸࡱࡩࡱࡲࡨࡨࠬሥ")
        bstack11ll1lll11_opy_(status)
    except:
        pass
def bstack1lll111ll1_opy_(status):
    try:
        bstack11ll1ll11l_opy_ = bstack111ll1l_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬሦ")
        if status == bstack111ll1l_opy_ (u"࠭ࡰࡢࡵࡶࡩࡩ࠭ሧ"):
            bstack11ll1ll11l_opy_ = bstack111ll1l_opy_ (u"ࠧࡱࡣࡶࡷࡪࡪࠧረ")
        elif status == bstack111ll1l_opy_ (u"ࠨࡵ࡮࡭ࡵࡶࡥࡥࠩሩ"):
            bstack11ll1ll11l_opy_ = bstack111ll1l_opy_ (u"ࠩࡶ࡯࡮ࡶࡰࡦࡦࠪሪ")
        bstack11ll1lll11_opy_(bstack11ll1ll11l_opy_)
    except:
        pass
def bstack11ll1ll1ll_opy_(item=None, report=None, summary=None, extra=None):
    return