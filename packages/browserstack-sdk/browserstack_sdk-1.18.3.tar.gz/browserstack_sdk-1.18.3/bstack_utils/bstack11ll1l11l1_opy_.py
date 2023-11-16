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
import json
import os
import threading
from bstack_utils.helper import bstack1l11l1llll_opy_, bstack11l1llll1_opy_, bstack11l11l11_opy_, bstack11l111lll_opy_, \
    bstack1l11lll11l_opy_
def bstack11l11lll1_opy_(bstack11l1lll1l1_opy_):
    for driver in bstack11l1lll1l1_opy_:
        try:
            driver.quit()
        except Exception as e:
            pass
def bstack1l1ll1111_opy_(type, name, status, reason, bstack1ll11l111l_opy_, bstack11l111111_opy_):
    bstack1l1ll111l_opy_ = {
        bstack111ll1l_opy_ (u"ࠪࡥࡨࡺࡩࡰࡰࠪራ"): type,
        bstack111ll1l_opy_ (u"ࠫࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠧሬ"): {}
    }
    if type == bstack111ll1l_opy_ (u"ࠬࡧ࡮࡯ࡱࡷࡥࡹ࡫ࠧር"):
        bstack1l1ll111l_opy_[bstack111ll1l_opy_ (u"࠭ࡡࡳࡩࡸࡱࡪࡴࡴࡴࠩሮ")][bstack111ll1l_opy_ (u"ࠧ࡭ࡧࡹࡩࡱ࠭ሯ")] = bstack1ll11l111l_opy_
        bstack1l1ll111l_opy_[bstack111ll1l_opy_ (u"ࠨࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠫሰ")][bstack111ll1l_opy_ (u"ࠩࡧࡥࡹࡧࠧሱ")] = json.dumps(str(bstack11l111111_opy_))
    if type == bstack111ll1l_opy_ (u"ࠪࡷࡪࡺࡓࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠫሲ"):
        bstack1l1ll111l_opy_[bstack111ll1l_opy_ (u"ࠫࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠧሳ")][bstack111ll1l_opy_ (u"ࠬࡴࡡ࡮ࡧࠪሴ")] = name
    if type == bstack111ll1l_opy_ (u"࠭ࡳࡦࡶࡖࡩࡸࡹࡩࡰࡰࡖࡸࡦࡺࡵࡴࠩስ"):
        bstack1l1ll111l_opy_[bstack111ll1l_opy_ (u"ࠧࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠪሶ")][bstack111ll1l_opy_ (u"ࠨࡵࡷࡥࡹࡻࡳࠨሷ")] = status
        if status == bstack111ll1l_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩሸ") and str(reason) != bstack111ll1l_opy_ (u"ࠥࠦሹ"):
            bstack1l1ll111l_opy_[bstack111ll1l_opy_ (u"ࠫࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠧሺ")][bstack111ll1l_opy_ (u"ࠬࡸࡥࡢࡵࡲࡲࠬሻ")] = json.dumps(str(reason))
    bstack1lll1ll111_opy_ = bstack111ll1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࢀࠫሼ").format(json.dumps(bstack1l1ll111l_opy_))
    return bstack1lll1ll111_opy_
def bstack1ll1l1l111_opy_(url, config, logger, bstack11l1l1lll_opy_=False):
    hostname = bstack11l1llll1_opy_(url)
    is_private = bstack11l111lll_opy_(hostname)
    try:
        if is_private or bstack11l1l1lll_opy_:
            file_path = bstack1l11l1llll_opy_(bstack111ll1l_opy_ (u"ࠧ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠧሽ"), bstack111ll1l_opy_ (u"ࠨ࠰ࡥࡷࡹࡧࡣ࡬࠯ࡦࡳࡳ࡬ࡩࡨ࠰࡭ࡷࡴࡴࠧሾ"), logger)
            if os.environ.get(bstack111ll1l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡎࡒࡇࡆࡒ࡟ࡏࡑࡗࡣࡘࡋࡔࡠࡇࡕࡖࡔࡘࠧሿ")) and eval(
                    os.environ.get(bstack111ll1l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡏࡓࡈࡇࡌࡠࡐࡒࡘࡤ࡙ࡅࡕࡡࡈࡖࡗࡕࡒࠨቀ"))):
                return
            if (bstack111ll1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࠨቁ") in config and not config[bstack111ll1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࠩቂ")]):
                os.environ[bstack111ll1l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡒࡏࡄࡃࡏࡣࡓࡕࡔࡠࡕࡈࡘࡤࡋࡒࡓࡑࡕࠫቃ")] = str(True)
                bstack11l1lll1ll_opy_ = {bstack111ll1l_opy_ (u"ࠧࡩࡱࡶࡸࡳࡧ࡭ࡦࠩቄ"): hostname}
                bstack1l11lll11l_opy_(bstack111ll1l_opy_ (u"ࠨ࠰ࡥࡷࡹࡧࡣ࡬࠯ࡦࡳࡳ࡬ࡩࡨ࠰࡭ࡷࡴࡴࠧቅ"), bstack111ll1l_opy_ (u"ࠩࡱࡹࡩ࡭ࡥࡠ࡮ࡲࡧࡦࡲࠧቆ"), bstack11l1lll1ll_opy_, logger)
    except Exception as e:
        pass
def bstack11l11111l_opy_(caps, bstack11l1lll11l_opy_):
    if bstack111ll1l_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭࠽ࡳࡵࡺࡩࡰࡰࡶࠫቇ") in caps:
        caps[bstack111ll1l_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮࠾ࡴࡶࡴࡪࡱࡱࡷࠬቈ")][bstack111ll1l_opy_ (u"ࠬࡲ࡯ࡤࡣ࡯ࠫ቉")] = True
        if bstack11l1lll11l_opy_:
            caps[bstack111ll1l_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡀ࡯ࡱࡶ࡬ࡳࡳࡹࠧቊ")][bstack111ll1l_opy_ (u"ࠧ࡭ࡱࡦࡥࡱࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩቋ")] = bstack11l1lll11l_opy_
    else:
        caps[bstack111ll1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮࡭ࡱࡦࡥࡱ࠭ቌ")] = True
        if bstack11l1lll11l_opy_:
            caps[bstack111ll1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯࡮ࡲࡧࡦࡲࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪቍ")] = bstack11l1lll11l_opy_
def bstack11ll1lll11_opy_(bstack11l1llll11_opy_):
    bstack11l1llll1l_opy_ = bstack11l11l11_opy_(threading.current_thread(), bstack111ll1l_opy_ (u"ࠪࡸࡪࡹࡴࡔࡶࡤࡸࡺࡹࠧ቎"), bstack111ll1l_opy_ (u"ࠫࠬ቏"))
    if bstack11l1llll1l_opy_ == bstack111ll1l_opy_ (u"ࠬ࠭ቐ") or bstack11l1llll1l_opy_ == bstack111ll1l_opy_ (u"࠭ࡳ࡬࡫ࡳࡴࡪࡪࠧቑ"):
        threading.current_thread().testStatus = bstack11l1llll11_opy_
    else:
        if bstack11l1llll11_opy_ == bstack111ll1l_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧቒ"):
            threading.current_thread().testStatus = bstack11l1llll11_opy_