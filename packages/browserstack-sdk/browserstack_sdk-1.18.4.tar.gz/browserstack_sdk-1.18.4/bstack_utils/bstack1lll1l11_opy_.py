# coding: UTF-8
import sys
bstack111ll1l_opy_ = sys.version_info [0] == 2
bstack1l1lll_opy_ = 2048
bstack1llllll_opy_ = 7
def bstack1ll_opy_ (bstack1l111l1_opy_):
    global bstack1lllll1_opy_
    bstack1l11l1_opy_ = ord (bstack1l111l1_opy_ [-1])
    bstack1l11l1l_opy_ = bstack1l111l1_opy_ [:-1]
    bstack11ll111_opy_ = bstack1l11l1_opy_ % len (bstack1l11l1l_opy_)
    bstack1l11l_opy_ = bstack1l11l1l_opy_ [:bstack11ll111_opy_] + bstack1l11l1l_opy_ [bstack11ll111_opy_:]
    if bstack111ll1l_opy_:
        bstack1l1l1_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1lll_opy_ - (bstack1ll1_opy_ + bstack1l11l1_opy_) % bstack1llllll_opy_) for bstack1ll1_opy_, char in enumerate (bstack1l11l_opy_)])
    else:
        bstack1l1l1_opy_ = str () .join ([chr (ord (char) - bstack1l1lll_opy_ - (bstack1ll1_opy_ + bstack1l11l1_opy_) % bstack1llllll_opy_) for bstack1ll1_opy_, char in enumerate (bstack1l11l_opy_)])
    return eval (bstack1l1l1_opy_)
import re
from bstack_utils.bstack11l1ll1lll_opy_ import bstack11l1llll11_opy_
def bstack11l1lll11l_opy_(fixture_name):
    if fixture_name.startswith(bstack1ll_opy_ (u"ࠧࡠࡺࡸࡲ࡮ࡺ࡟ࡴࡧࡷࡹࡵࡥࡦࡶࡰࡦࡸ࡮ࡵ࡮ࡠࡨ࡬ࡼࡹࡻࡲࡦࠩረ")):
        return bstack1ll_opy_ (u"ࠨࡵࡨࡸࡺࡶ࠭ࡧࡷࡱࡧࡹ࡯࡯࡯ࠩሩ")
    elif fixture_name.startswith(bstack1ll_opy_ (u"ࠩࡢࡼࡺࡴࡩࡵࡡࡶࡩࡹࡻࡰࡠ࡯ࡲࡨࡺࡲࡥࡠࡨ࡬ࡼࡹࡻࡲࡦࠩሪ")):
        return bstack1ll_opy_ (u"ࠪࡷࡪࡺࡵࡱ࠯ࡰࡳࡩࡻ࡬ࡦࠩራ")
    elif fixture_name.startswith(bstack1ll_opy_ (u"ࠫࡤࡾࡵ࡯࡫ࡷࡣࡹ࡫ࡡࡳࡦࡲࡻࡳࡥࡦࡶࡰࡦࡸ࡮ࡵ࡮ࡠࡨ࡬ࡼࡹࡻࡲࡦࠩሬ")):
        return bstack1ll_opy_ (u"ࠬࡺࡥࡢࡴࡧࡳࡼࡴ࠭ࡧࡷࡱࡧࡹ࡯࡯࡯ࠩር")
    elif fixture_name.startswith(bstack1ll_opy_ (u"࠭࡟ࡹࡷࡱ࡭ࡹࡥࡴࡦࡣࡵࡨࡴࡽ࡮ࡠࡨࡸࡲࡨࡺࡩࡰࡰࡢࡪ࡮ࡾࡴࡶࡴࡨࠫሮ")):
        return bstack1ll_opy_ (u"ࠧࡵࡧࡤࡶࡩࡵࡷ࡯࠯ࡰࡳࡩࡻ࡬ࡦࠩሯ")
def bstack11l1lll1l1_opy_(fixture_name):
    return bool(re.match(bstack1ll_opy_ (u"ࠨࡠࡢࡼࡺࡴࡩࡵࡡࠫࡷࡪࡺࡵࡱࡾࡷࡩࡦࡸࡤࡰࡹࡱ࠭ࡤ࠮ࡦࡶࡰࡦࡸ࡮ࡵ࡮ࡽ࡯ࡲࡨࡺࡲࡥࠪࡡࡩ࡭ࡽࡺࡵࡳࡧࡢ࠲࠯࠭ሰ"), fixture_name))
def bstack11ll11111l_opy_(fixture_name):
    return bool(re.match(bstack1ll_opy_ (u"ࠩࡡࡣࡽࡻ࡮ࡪࡶࡢࠬࡸ࡫ࡴࡶࡲࡿࡸࡪࡧࡲࡥࡱࡺࡲ࠮ࡥ࡭ࡰࡦࡸࡰࡪࡥࡦࡪࡺࡷࡹࡷ࡫࡟࠯ࠬࠪሱ"), fixture_name))
def bstack11ll1111l1_opy_(fixture_name):
    return bool(re.match(bstack1ll_opy_ (u"ࠪࡢࡤࡾࡵ࡯࡫ࡷࡣ࠭ࡹࡥࡵࡷࡳࢀࡹ࡫ࡡࡳࡦࡲࡻࡳ࠯࡟ࡤ࡮ࡤࡷࡸࡥࡦࡪࡺࡷࡹࡷ࡫࡟࠯ࠬࠪሲ"), fixture_name))
def bstack11ll1111ll_opy_(fixture_name):
    if fixture_name.startswith(bstack1ll_opy_ (u"ࠫࡤࡾࡵ࡯࡫ࡷࡣࡸ࡫ࡴࡶࡲࡢࡪࡺࡴࡣࡵ࡫ࡲࡲࡤ࡬ࡩࡹࡶࡸࡶࡪ࠭ሳ")):
        return bstack1ll_opy_ (u"ࠬࡹࡥࡵࡷࡳ࠱࡫ࡻ࡮ࡤࡶ࡬ࡳࡳ࠭ሴ"), bstack1ll_opy_ (u"࠭ࡂࡆࡈࡒࡖࡊࡥࡅࡂࡅࡋࠫስ")
    elif fixture_name.startswith(bstack1ll_opy_ (u"ࠧࡠࡺࡸࡲ࡮ࡺ࡟ࡴࡧࡷࡹࡵࡥ࡭ࡰࡦࡸࡰࡪࡥࡦࡪࡺࡷࡹࡷ࡫ࠧሶ")):
        return bstack1ll_opy_ (u"ࠨࡵࡨࡸࡺࡶ࠭࡮ࡱࡧࡹࡱ࡫ࠧሷ"), bstack1ll_opy_ (u"ࠩࡅࡉࡋࡕࡒࡆࡡࡄࡐࡑ࠭ሸ")
    elif fixture_name.startswith(bstack1ll_opy_ (u"ࠪࡣࡽࡻ࡮ࡪࡶࡢࡸࡪࡧࡲࡥࡱࡺࡲࡤ࡬ࡵ࡯ࡥࡷ࡭ࡴࡴ࡟ࡧ࡫ࡻࡸࡺࡸࡥࠨሹ")):
        return bstack1ll_opy_ (u"ࠫࡹ࡫ࡡࡳࡦࡲࡻࡳ࠳ࡦࡶࡰࡦࡸ࡮ࡵ࡮ࠨሺ"), bstack1ll_opy_ (u"ࠬࡇࡆࡕࡇࡕࡣࡊࡇࡃࡉࠩሻ")
    elif fixture_name.startswith(bstack1ll_opy_ (u"࠭࡟ࡹࡷࡱ࡭ࡹࡥࡴࡦࡣࡵࡨࡴࡽ࡮ࡠ࡯ࡲࡨࡺࡲࡥࡠࡨ࡬ࡼࡹࡻࡲࡦࠩሼ")):
        return bstack1ll_opy_ (u"ࠧࡵࡧࡤࡶࡩࡵࡷ࡯࠯ࡰࡳࡩࡻ࡬ࡦࠩሽ"), bstack1ll_opy_ (u"ࠨࡃࡉࡘࡊࡘ࡟ࡂࡎࡏࠫሾ")
    return None, None
def bstack11ll111l11_opy_(hook_name):
    if hook_name in [bstack1ll_opy_ (u"ࠩࡶࡩࡹࡻࡰࠨሿ"), bstack1ll_opy_ (u"ࠪࡸࡪࡧࡲࡥࡱࡺࡲࠬቀ")]:
        return hook_name.capitalize()
    return hook_name
def bstack11l1lll1ll_opy_(hook_name):
    if hook_name in [bstack1ll_opy_ (u"ࠫࡸ࡫ࡴࡶࡲࡢࡪࡺࡴࡣࡵ࡫ࡲࡲࠬቁ"), bstack1ll_opy_ (u"ࠬࡹࡥࡵࡷࡳࡣࡲ࡫ࡴࡩࡱࡧࠫቂ")]:
        return bstack1ll_opy_ (u"࠭ࡂࡆࡈࡒࡖࡊࡥࡅࡂࡅࡋࠫቃ")
    elif hook_name in [bstack1ll_opy_ (u"ࠧࡴࡧࡷࡹࡵࡥ࡭ࡰࡦࡸࡰࡪ࠭ቄ"), bstack1ll_opy_ (u"ࠨࡵࡨࡸࡺࡶ࡟ࡤ࡮ࡤࡷࡸ࠭ቅ")]:
        return bstack1ll_opy_ (u"ࠩࡅࡉࡋࡕࡒࡆࡡࡄࡐࡑ࠭ቆ")
    elif hook_name in [bstack1ll_opy_ (u"ࠪࡸࡪࡧࡲࡥࡱࡺࡲࡤ࡬ࡵ࡯ࡥࡷ࡭ࡴࡴࠧቇ"), bstack1ll_opy_ (u"ࠫࡹ࡫ࡡࡳࡦࡲࡻࡳࡥ࡭ࡦࡶ࡫ࡳࡩ࠭ቈ")]:
        return bstack1ll_opy_ (u"ࠬࡇࡆࡕࡇࡕࡣࡊࡇࡃࡉࠩ቉")
    elif hook_name in [bstack1ll_opy_ (u"࠭ࡴࡦࡣࡵࡨࡴࡽ࡮ࡠ࡯ࡲࡨࡺࡲࡥࠨቊ"), bstack1ll_opy_ (u"ࠧࡵࡧࡤࡶࡩࡵࡷ࡯ࡡࡦࡰࡦࡹࡳࠨቋ")]:
        return bstack1ll_opy_ (u"ࠨࡃࡉࡘࡊࡘ࡟ࡂࡎࡏࠫቌ")
    return hook_name
def bstack11ll111111_opy_(node, scenario):
    if hasattr(node, bstack1ll_opy_ (u"ࠩࡦࡥࡱࡲࡳࡱࡧࡦࠫቍ")):
        parts = node.nodeid.rsplit(bstack1ll_opy_ (u"ࠥ࡟ࠧ቎"))
        params = parts[-1]
        return bstack1ll_opy_ (u"ࠦࢀࢃࠠ࡜ࡽࢀࠦ቏").format(scenario.name, params)
    return scenario.name
def bstack11l1llllll_opy_(node):
    try:
        examples = []
        if hasattr(node, bstack1ll_opy_ (u"ࠬࡩࡡ࡭࡮ࡶࡴࡪࡩࠧቐ")):
            examples = list(node.callspec.params[bstack1ll_opy_ (u"࠭࡟ࡱࡻࡷࡩࡸࡺ࡟ࡣࡦࡧࡣࡪࡾࡡ࡮ࡲ࡯ࡩࠬቑ")].values())
        return examples
    except:
        return []
def bstack11l1lllll1_opy_(feature, scenario):
    return list(feature.tags) + list(scenario.tags)
def bstack11l1llll1l_opy_(report):
    try:
        status = bstack1ll_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧቒ")
        if report.passed or (report.failed and hasattr(report, bstack1ll_opy_ (u"ࠣࡹࡤࡷࡽ࡬ࡡࡪ࡮ࠥቓ"))):
            status = bstack1ll_opy_ (u"ࠩࡳࡥࡸࡹࡥࡥࠩቔ")
        elif report.skipped:
            status = bstack1ll_opy_ (u"ࠪࡷࡰ࡯ࡰࡱࡧࡧࠫቕ")
        bstack11l1llll11_opy_(status)
    except:
        pass
def bstack1ll11l11_opy_(status):
    try:
        bstack11l1lll111_opy_ = bstack1ll_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫቖ")
        if status == bstack1ll_opy_ (u"ࠬࡶࡡࡴࡵࡨࡨࠬ቗"):
            bstack11l1lll111_opy_ = bstack1ll_opy_ (u"࠭ࡰࡢࡵࡶࡩࡩ࠭ቘ")
        elif status == bstack1ll_opy_ (u"ࠧࡴ࡭࡬ࡴࡵ࡫ࡤࠨ቙"):
            bstack11l1lll111_opy_ = bstack1ll_opy_ (u"ࠨࡵ࡮࡭ࡵࡶࡥࡥࠩቚ")
        bstack11l1llll11_opy_(bstack11l1lll111_opy_)
    except:
        pass
def bstack11ll111l1l_opy_(item=None, report=None, summary=None, extra=None):
    return