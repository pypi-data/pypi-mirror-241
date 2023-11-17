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
import json
import os
import threading
from bstack_utils.helper import bstack1l11lll1ll_opy_, bstack1ll111ll_opy_, bstack1llll11l_opy_, bstack1l11l11l1_opy_, \
    bstack1l1l111ll1_opy_
def bstack1ll1l1ll1l_opy_(bstack11l1l11111_opy_):
    for driver in bstack11l1l11111_opy_:
        try:
            driver.quit()
        except Exception as e:
            pass
def bstack11ll1111_opy_(type, name, status, reason, bstack11l1llll_opy_, bstack1lll11ll11_opy_):
    bstack1llll1l1l_opy_ = {
        bstack1ll_opy_ (u"ࠩࡤࡧࡹ࡯࡯࡯ࠩቛ"): type,
        bstack1ll_opy_ (u"ࠪࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸ࠭ቜ"): {}
    }
    if type == bstack1ll_opy_ (u"ࠫࡦࡴ࡮ࡰࡶࡤࡸࡪ࠭ቝ"):
        bstack1llll1l1l_opy_[bstack1ll_opy_ (u"ࠬࡧࡲࡨࡷࡰࡩࡳࡺࡳࠨ቞")][bstack1ll_opy_ (u"࠭࡬ࡦࡸࡨࡰࠬ቟")] = bstack11l1llll_opy_
        bstack1llll1l1l_opy_[bstack1ll_opy_ (u"ࠧࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠪበ")][bstack1ll_opy_ (u"ࠨࡦࡤࡸࡦ࠭ቡ")] = json.dumps(str(bstack1lll11ll11_opy_))
    if type == bstack1ll_opy_ (u"ࠩࡶࡩࡹ࡙ࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠪቢ"):
        bstack1llll1l1l_opy_[bstack1ll_opy_ (u"ࠪࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸ࠭ባ")][bstack1ll_opy_ (u"ࠫࡳࡧ࡭ࡦࠩቤ")] = name
    if type == bstack1ll_opy_ (u"ࠬࡹࡥࡵࡕࡨࡷࡸ࡯࡯࡯ࡕࡷࡥࡹࡻࡳࠨብ"):
        bstack1llll1l1l_opy_[bstack1ll_opy_ (u"࠭ࡡࡳࡩࡸࡱࡪࡴࡴࡴࠩቦ")][bstack1ll_opy_ (u"ࠧࡴࡶࡤࡸࡺࡹࠧቧ")] = status
        if status == bstack1ll_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨቨ") and str(reason) != bstack1ll_opy_ (u"ࠤࠥቩ"):
            bstack1llll1l1l_opy_[bstack1ll_opy_ (u"ࠪࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸ࠭ቪ")][bstack1ll_opy_ (u"ࠫࡷ࡫ࡡࡴࡱࡱࠫቫ")] = json.dumps(str(reason))
    bstack11l1ll11l_opy_ = bstack1ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࡼࡿࠪቬ").format(json.dumps(bstack1llll1l1l_opy_))
    return bstack11l1ll11l_opy_
def bstack1llllll1l1_opy_(url, config, logger, bstack1l1l11l1l_opy_=False):
    hostname = bstack1ll111ll_opy_(url)
    is_private = bstack1l11l11l1_opy_(hostname)
    try:
        if is_private or bstack1l1l11l1l_opy_:
            file_path = bstack1l11lll1ll_opy_(bstack1ll_opy_ (u"࠭࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠭ቭ"), bstack1ll_opy_ (u"ࠧ࠯ࡤࡶࡸࡦࡩ࡫࠮ࡥࡲࡲ࡫࡯ࡧ࠯࡬ࡶࡳࡳ࠭ቮ"), logger)
            if os.environ.get(bstack1ll_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡍࡑࡆࡅࡑࡥࡎࡐࡖࡢࡗࡊ࡚࡟ࡆࡔࡕࡓࡗ࠭ቯ")) and eval(
                    os.environ.get(bstack1ll_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡎࡒࡇࡆࡒ࡟ࡏࡑࡗࡣࡘࡋࡔࡠࡇࡕࡖࡔࡘࠧተ"))):
                return
            if (bstack1ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࠧቱ") in config and not config[bstack1ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࠨቲ")]):
                os.environ[bstack1ll_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡑࡕࡃࡂࡎࡢࡒࡔ࡚࡟ࡔࡇࡗࡣࡊࡘࡒࡐࡔࠪታ")] = str(True)
                bstack11l1l11l11_opy_ = {bstack1ll_opy_ (u"࠭ࡨࡰࡵࡷࡲࡦࡳࡥࠨቴ"): hostname}
                bstack1l1l111ll1_opy_(bstack1ll_opy_ (u"ࠧ࠯ࡤࡶࡸࡦࡩ࡫࠮ࡥࡲࡲ࡫࡯ࡧ࠯࡬ࡶࡳࡳ࠭ት"), bstack1ll_opy_ (u"ࠨࡰࡸࡨ࡬࡫࡟࡭ࡱࡦࡥࡱ࠭ቶ"), bstack11l1l11l11_opy_, logger)
    except Exception as e:
        pass
def bstack1ll1llll11_opy_(caps, bstack11l1l1111l_opy_):
    if bstack1ll_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬࠼ࡲࡴࡹ࡯࡯࡯ࡵࠪቷ") in caps:
        caps[bstack1ll_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭࠽ࡳࡵࡺࡩࡰࡰࡶࠫቸ")][bstack1ll_opy_ (u"ࠫࡱࡵࡣࡢ࡮ࠪቹ")] = True
        if bstack11l1l1111l_opy_:
            caps[bstack1ll_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯࠿ࡵࡰࡵ࡫ࡲࡲࡸ࠭ቺ")][bstack1ll_opy_ (u"࠭࡬ࡰࡥࡤࡰࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨቻ")] = bstack11l1l1111l_opy_
    else:
        caps[bstack1ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴࡬ࡰࡥࡤࡰࠬቼ")] = True
        if bstack11l1l1111l_opy_:
            caps[bstack1ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮࡭ࡱࡦࡥࡱࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩች")] = bstack11l1l1111l_opy_
def bstack11l1llll11_opy_(bstack11l1l111ll_opy_):
    bstack11l1l111l1_opy_ = bstack1llll11l_opy_(threading.current_thread(), bstack1ll_opy_ (u"ࠩࡷࡩࡸࡺࡓࡵࡣࡷࡹࡸ࠭ቾ"), bstack1ll_opy_ (u"ࠪࠫቿ"))
    if bstack11l1l111l1_opy_ == bstack1ll_opy_ (u"ࠫࠬኀ") or bstack11l1l111l1_opy_ == bstack1ll_opy_ (u"ࠬࡹ࡫ࡪࡲࡳࡩࡩ࠭ኁ"):
        threading.current_thread().testStatus = bstack11l1l111ll_opy_
    else:
        if bstack11l1l111ll_opy_ == bstack1ll_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭ኂ"):
            threading.current_thread().testStatus = bstack11l1l111ll_opy_