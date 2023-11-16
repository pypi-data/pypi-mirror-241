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
import datetime
import json
import logging
import os
import threading
from bstack_utils.helper import bstack1l1ll1ll11_opy_, bstack1ll111111_opy_, get_host_info, bstack1l1lllll1l_opy_, bstack1l1llll1ll_opy_, bstack1l1l11llll_opy_, \
    bstack1l1l1l111l_opy_, bstack1l1l11l1l1_opy_, bstack11111l11l_opy_, bstack1l1l111l1l_opy_, bstack1l1l11ll11_opy_, bstack1l1lll11l1_opy_
from bstack_utils.bstack11ll111l11_opy_ import bstack11ll11l111_opy_
from bstack_utils.bstack11l1l11l11_opy_ import bstack11l1l11ll1_opy_
bstack11l111ll1l_opy_ = [
    bstack111ll1l_opy_ (u"࠭ࡌࡰࡩࡆࡶࡪࡧࡴࡦࡦࠪ኉"), bstack111ll1l_opy_ (u"ࠧࡄࡄࡗࡗࡪࡹࡳࡪࡱࡱࡇࡷ࡫ࡡࡵࡧࡧࠫኊ"), bstack111ll1l_opy_ (u"ࠨࡖࡨࡷࡹࡘࡵ࡯ࡈ࡬ࡲ࡮ࡹࡨࡦࡦࠪኋ"), bstack111ll1l_opy_ (u"ࠩࡗࡩࡸࡺࡒࡶࡰࡖ࡯࡮ࡶࡰࡦࡦࠪኌ"),
    bstack111ll1l_opy_ (u"ࠪࡌࡴࡵ࡫ࡓࡷࡱࡊ࡮ࡴࡩࡴࡪࡨࡨࠬኍ"), bstack111ll1l_opy_ (u"࡙ࠫ࡫ࡳࡵࡔࡸࡲࡘࡺࡡࡳࡶࡨࡨࠬ኎"), bstack111ll1l_opy_ (u"ࠬࡎ࡯ࡰ࡭ࡕࡹࡳ࡙ࡴࡢࡴࡷࡩࡩ࠭኏")
]
bstack11l11ll1ll_opy_ = bstack111ll1l_opy_ (u"࠭ࡨࡵࡶࡳࡷ࠿࠵࠯ࡤࡱ࡯ࡰࡪࡩࡴࡰࡴ࠰ࡳࡧࡹࡥࡳࡸࡤࡦ࡮ࡲࡩࡵࡻ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡦࡳࡲ࠭ነ")
logger = logging.getLogger(__name__)
class bstack1l11lll1l_opy_:
    bstack11ll111l11_opy_ = None
    bs_config = None
    @classmethod
    @bstack1l1lll11l1_opy_(class_method=True)
    def launch(cls, bs_config, bstack11l11l11ll_opy_):
        cls.bs_config = bs_config
        if not cls.bstack11l11l1l11_opy_():
            return
        cls.bstack11l11l1lll_opy_()
        bstack1ll11111ll_opy_ = bstack1l1lllll1l_opy_(bs_config)
        bstack1l1llllll1_opy_ = bstack1l1llll1ll_opy_(bs_config)
        data = {
            bstack111ll1l_opy_ (u"ࠧࡧࡱࡵࡱࡦࡺࠧኑ"): bstack111ll1l_opy_ (u"ࠨ࡬ࡶࡳࡳ࠭ኒ"),
            bstack111ll1l_opy_ (u"ࠩࡳࡶࡴࡰࡥࡤࡶࡢࡲࡦࡳࡥࠨና"): bs_config.get(bstack111ll1l_opy_ (u"ࠪࡴࡷࡵࡪࡦࡥࡷࡒࡦࡳࡥࠨኔ"), bstack111ll1l_opy_ (u"ࠫࠬን")),
            bstack111ll1l_opy_ (u"ࠬࡴࡡ࡮ࡧࠪኖ"): bs_config.get(bstack111ll1l_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡓࡧ࡭ࡦࠩኗ"), os.path.basename(os.path.abspath(os.getcwd()))),
            bstack111ll1l_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡥࡩࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪኘ"): bs_config.get(bstack111ll1l_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪኙ")),
            bstack111ll1l_opy_ (u"ࠩࡧࡩࡸࡩࡲࡪࡲࡷ࡭ࡴࡴࠧኚ"): bs_config.get(bstack111ll1l_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡆࡨࡷࡨࡸࡩࡱࡶ࡬ࡳࡳ࠭ኛ"), bstack111ll1l_opy_ (u"ࠫࠬኜ")),
            bstack111ll1l_opy_ (u"ࠬࡹࡴࡢࡴࡷࡣࡹ࡯࡭ࡦࠩኝ"): datetime.datetime.now().isoformat(),
            bstack111ll1l_opy_ (u"࠭ࡴࡢࡩࡶࠫኞ"): bstack1l1l11llll_opy_(bs_config),
            bstack111ll1l_opy_ (u"ࠧࡩࡱࡶࡸࡤ࡯࡮ࡧࡱࠪኟ"): get_host_info(),
            bstack111ll1l_opy_ (u"ࠨࡥ࡬ࡣ࡮ࡴࡦࡰࠩአ"): bstack1ll111111_opy_(),
            bstack111ll1l_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡠࡴࡸࡲࡤ࡯ࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩኡ"): os.environ.get(bstack111ll1l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡅ࡙ࡎࡒࡄࡠࡔࡘࡒࡤࡏࡄࡆࡐࡗࡍࡋࡏࡅࡓࠩኢ")),
            bstack111ll1l_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࡣࡹ࡫ࡳࡵࡵࡢࡶࡪࡸࡵ࡯ࠩኣ"): os.environ.get(bstack111ll1l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡗࡋࡒࡖࡐࠪኤ"), False),
            bstack111ll1l_opy_ (u"࠭ࡶࡦࡴࡶ࡭ࡴࡴ࡟ࡤࡱࡱࡸࡷࡵ࡬ࠨእ"): bstack1l1ll1ll11_opy_(),
            bstack111ll1l_opy_ (u"ࠧࡰࡤࡶࡩࡷࡼࡡࡣ࡫࡯࡭ࡹࡿ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠨኦ"): {
                bstack111ll1l_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡒࡦࡳࡥࠨኧ"): bstack11l11l11ll_opy_.get(bstack111ll1l_opy_ (u"ࠩࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡴࡡ࡮ࡧࠪከ"), bstack111ll1l_opy_ (u"ࠪࡔࡾࡺࡥࡴࡶࠪኩ")),
                bstack111ll1l_opy_ (u"ࠫ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱࡖࡦࡴࡶ࡭ࡴࡴࠧኪ"): bstack11l11l11ll_opy_.get(bstack111ll1l_opy_ (u"ࠬ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡸࡨࡶࡸ࡯࡯࡯ࠩካ")),
                bstack111ll1l_opy_ (u"࠭ࡳࡥ࡭࡙ࡩࡷࡹࡩࡰࡰࠪኬ"): bstack11l11l11ll_opy_.get(bstack111ll1l_opy_ (u"ࠧࡴࡦ࡮ࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬክ"))
            }
        }
        config = {
            bstack111ll1l_opy_ (u"ࠨࡣࡸࡸ࡭࠭ኮ"): (bstack1ll11111ll_opy_, bstack1l1llllll1_opy_),
            bstack111ll1l_opy_ (u"ࠩ࡫ࡩࡦࡪࡥࡳࡵࠪኯ"): cls.default_headers()
        }
        response = bstack11111l11l_opy_(bstack111ll1l_opy_ (u"ࠪࡔࡔ࡙ࡔࠨኰ"), cls.request_url(bstack111ll1l_opy_ (u"ࠫࡦࡶࡩ࠰ࡸ࠴࠳ࡧࡻࡩ࡭ࡦࡶࠫ኱")), data, config)
        if response.status_code != 200:
            os.environ[bstack111ll1l_opy_ (u"ࠬࡈࡓࡠࡖࡈࡗ࡙ࡕࡐࡔࡡࡅ࡙ࡎࡒࡄࡠࡅࡒࡑࡕࡒࡅࡕࡇࡇࠫኲ")] = bstack111ll1l_opy_ (u"࠭ࡦࡢ࡮ࡶࡩࠬኳ")
            os.environ[bstack111ll1l_opy_ (u"ࠧࡃࡕࡢࡘࡊ࡙ࡔࡐࡒࡖࡣࡏ࡝ࡔࠨኴ")] = bstack111ll1l_opy_ (u"ࠨࡰࡸࡰࡱ࠭ኵ")
            os.environ[bstack111ll1l_opy_ (u"ࠩࡅࡗࡤ࡚ࡅࡔࡖࡒࡔࡘࡥࡂࡖࡋࡏࡈࡤࡎࡁࡔࡊࡈࡈࡤࡏࡄࠨ኶")] = bstack111ll1l_opy_ (u"ࠥࡲࡺࡲ࡬ࠣ኷")
            os.environ[bstack111ll1l_opy_ (u"ࠫࡇ࡙࡟ࡕࡇࡖࡘࡔࡖࡓࡠࡃࡏࡐࡔ࡝࡟ࡔࡅࡕࡉࡊࡔࡓࡉࡑࡗࡗࠬኸ")] = bstack111ll1l_opy_ (u"ࠧࡴࡵ࡭࡮ࠥኹ")
            bstack11l11ll111_opy_ = response.json()
            if bstack11l11ll111_opy_ and bstack11l11ll111_opy_[bstack111ll1l_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧኺ")]:
                error_message = bstack11l11ll111_opy_[bstack111ll1l_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨኻ")]
                if bstack11l11ll111_opy_[bstack111ll1l_opy_ (u"ࠨࡧࡵࡶࡴࡸࡔࡺࡲࡨࠫኼ")] == bstack111ll1l_opy_ (u"ࠩࡈࡖࡗࡕࡒࡠࡋࡑ࡚ࡆࡒࡉࡅࡡࡆࡖࡊࡊࡅࡏࡖࡌࡅࡑ࡙ࠧኽ"):
                    logger.error(error_message)
                elif bstack11l11ll111_opy_[bstack111ll1l_opy_ (u"ࠪࡩࡷࡸ࡯ࡳࡖࡼࡴࡪ࠭ኾ")] == bstack111ll1l_opy_ (u"ࠫࡊࡘࡒࡐࡔࡢࡅࡈࡉࡅࡔࡕࡢࡈࡊࡔࡉࡆࡆࠪ኿"):
                    logger.info(error_message)
                elif bstack11l11ll111_opy_[bstack111ll1l_opy_ (u"ࠬ࡫ࡲࡳࡱࡵࡘࡾࡶࡥࠨዀ")] == bstack111ll1l_opy_ (u"࠭ࡅࡓࡔࡒࡖࡤ࡙ࡄࡌࡡࡇࡉࡕࡘࡅࡄࡃࡗࡉࡉ࠭዁"):
                    logger.error(error_message)
                else:
                    logger.error(error_message)
            else:
                logger.error(bstack111ll1l_opy_ (u"ࠢࡅࡣࡷࡥࠥࡻࡰ࡭ࡱࡤࡨࠥࡺ࡯ࠡࡄࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࠠࡕࡧࡶࡸࠥࡕࡢࡴࡧࡵࡺࡦࡨࡩ࡭࡫ࡷࡽࠥ࡬ࡡࡪ࡮ࡨࡨࠥࡪࡵࡦࠢࡷࡳࠥࡹ࡯࡮ࡧࠣࡩࡷࡸ࡯ࡳࠤዂ"))
            return [None, None, None]
        logger.debug(bstack111ll1l_opy_ (u"ࠨࡖࡨࡷࡹࠦࡏࡣࡵࡨࡶࡻࡧࡢࡪ࡮࡬ࡸࡾࠦࡂࡶ࡫࡯ࡨࠥࡩࡲࡦࡣࡷ࡭ࡴࡴࠠࡔࡷࡦࡧࡪࡹࡳࡧࡷ࡯ࠥࠬዃ"))
        os.environ[bstack111ll1l_opy_ (u"ࠩࡅࡗࡤ࡚ࡅࡔࡖࡒࡔࡘࡥࡂࡖࡋࡏࡈࡤࡉࡏࡎࡒࡏࡉ࡙ࡋࡄࠨዄ")] = bstack111ll1l_opy_ (u"ࠪࡸࡷࡻࡥࠨዅ")
        bstack11l11ll111_opy_ = response.json()
        if bstack11l11ll111_opy_.get(bstack111ll1l_opy_ (u"ࠫ࡯ࡽࡴࠨ዆")):
            os.environ[bstack111ll1l_opy_ (u"ࠬࡈࡓࡠࡖࡈࡗ࡙ࡕࡐࡔࡡࡍ࡛࡙࠭዇")] = bstack11l11ll111_opy_[bstack111ll1l_opy_ (u"࠭ࡪࡸࡶࠪወ")]
            os.environ[bstack111ll1l_opy_ (u"ࠧࡄࡔࡈࡈࡊࡔࡔࡊࡃࡏࡗࡤࡌࡏࡓࡡࡆࡖࡆ࡙ࡈࡠࡔࡈࡔࡔࡘࡔࡊࡐࡊࠫዉ")] = json.dumps({
                bstack111ll1l_opy_ (u"ࠨࡷࡶࡩࡷࡴࡡ࡮ࡧࠪዊ"): bstack1ll11111ll_opy_,
                bstack111ll1l_opy_ (u"ࠩࡳࡥࡸࡹࡷࡰࡴࡧࠫዋ"): bstack1l1llllll1_opy_
            })
        if bstack11l11ll111_opy_.get(bstack111ll1l_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡡ࡫ࡥࡸ࡮ࡥࡥࡡ࡬ࡨࠬዌ")):
            os.environ[bstack111ll1l_opy_ (u"ࠫࡇ࡙࡟ࡕࡇࡖࡘࡔࡖࡓࡠࡄࡘࡍࡑࡊ࡟ࡉࡃࡖࡌࡊࡊ࡟ࡊࡆࠪው")] = bstack11l11ll111_opy_[bstack111ll1l_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡣ࡭ࡧࡳࡩࡧࡧࡣ࡮ࡪࠧዎ")]
        if bstack11l11ll111_opy_.get(bstack111ll1l_opy_ (u"࠭ࡡ࡭࡮ࡲࡻࡤࡹࡣࡳࡧࡨࡲࡸ࡮࡯ࡵࡵࠪዏ")):
            os.environ[bstack111ll1l_opy_ (u"ࠧࡃࡕࡢࡘࡊ࡙ࡔࡐࡒࡖࡣࡆࡒࡌࡐ࡙ࡢࡗࡈࡘࡅࡆࡐࡖࡌࡔ࡚ࡓࠨዐ")] = str(bstack11l11ll111_opy_[bstack111ll1l_opy_ (u"ࠨࡣ࡯ࡰࡴࡽ࡟ࡴࡥࡵࡩࡪࡴࡳࡩࡱࡷࡷࠬዑ")])
        return [bstack11l11ll111_opy_[bstack111ll1l_opy_ (u"ࠩ࡭ࡻࡹ࠭ዒ")], bstack11l11ll111_opy_[bstack111ll1l_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡡ࡫ࡥࡸ࡮ࡥࡥࡡ࡬ࡨࠬዓ")], bstack11l11ll111_opy_[bstack111ll1l_opy_ (u"ࠫࡦࡲ࡬ࡰࡹࡢࡷࡨࡸࡥࡦࡰࡶ࡬ࡴࡺࡳࠨዔ")]]
    @classmethod
    @bstack1l1lll11l1_opy_(class_method=True)
    def stop(cls):
        if not cls.on():
            return
        if os.environ[bstack111ll1l_opy_ (u"ࠬࡈࡓࡠࡖࡈࡗ࡙ࡕࡐࡔࡡࡍ࡛࡙࠭ዕ")] == bstack111ll1l_opy_ (u"ࠨ࡮ࡶ࡮࡯ࠦዖ") or os.environ[bstack111ll1l_opy_ (u"ࠧࡃࡕࡢࡘࡊ࡙ࡔࡐࡒࡖࡣࡇ࡛ࡉࡍࡆࡢࡌࡆ࡙ࡈࡆࡆࡢࡍࡉ࠭዗")] == bstack111ll1l_opy_ (u"ࠣࡰࡸࡰࡱࠨዘ"):
            print(bstack111ll1l_opy_ (u"ࠩࡈ࡜ࡈࡋࡐࡕࡋࡒࡒࠥࡏࡎࠡࡵࡷࡳࡵࡈࡵࡪ࡮ࡧ࡙ࡵࡹࡴࡳࡧࡤࡱࠥࡘࡅࡒࡗࡈࡗ࡙ࠦࡔࡐࠢࡗࡉࡘ࡚ࠠࡐࡄࡖࡉࡗ࡜ࡁࡃࡋࡏࡍ࡙࡟ࠠ࠻ࠢࡐ࡭ࡸࡹࡩ࡯ࡩࠣࡥࡺࡺࡨࡦࡰࡷ࡭ࡨࡧࡴࡪࡱࡱࠤࡹࡵ࡫ࡦࡰࠪዙ"))
            return {
                bstack111ll1l_opy_ (u"ࠪࡷࡹࡧࡴࡶࡵࠪዚ"): bstack111ll1l_opy_ (u"ࠫࡪࡸࡲࡰࡴࠪዛ"),
                bstack111ll1l_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ࠭ዜ"): bstack111ll1l_opy_ (u"࠭ࡔࡰ࡭ࡨࡲ࠴ࡨࡵࡪ࡮ࡧࡍࡉࠦࡩࡴࠢࡸࡲࡩ࡫ࡦࡪࡰࡨࡨ࠱ࠦࡢࡶ࡫࡯ࡨࠥࡩࡲࡦࡣࡷ࡭ࡴࡴࠠ࡮࡫ࡪ࡬ࡹࠦࡨࡢࡸࡨࠤ࡫ࡧࡩ࡭ࡧࡧࠫዝ")
            }
        else:
            cls.bstack11ll111l11_opy_.shutdown()
            data = {
                bstack111ll1l_opy_ (u"ࠧࡴࡶࡲࡴࡤࡺࡩ࡮ࡧࠪዞ"): datetime.datetime.now().isoformat()
            }
            config = {
                bstack111ll1l_opy_ (u"ࠨࡪࡨࡥࡩ࡫ࡲࡴࠩዟ"): cls.default_headers()
            }
            bstack1l11lllll1_opy_ = bstack111ll1l_opy_ (u"ࠩࡤࡴ࡮࠵ࡶ࠲࠱ࡥࡹ࡮ࡲࡤࡴ࠱ࡾࢁ࠴ࡹࡴࡰࡲࠪዠ").format(os.environ[bstack111ll1l_opy_ (u"ࠥࡆࡘࡥࡔࡆࡕࡗࡓࡕ࡙࡟ࡃࡗࡌࡐࡉࡥࡈࡂࡕࡋࡉࡉࡥࡉࡅࠤዡ")])
            bstack11l11ll11l_opy_ = cls.request_url(bstack1l11lllll1_opy_)
            response = bstack11111l11l_opy_(bstack111ll1l_opy_ (u"ࠫࡕ࡛ࡔࠨዢ"), bstack11l11ll11l_opy_, data, config)
            if not response.ok:
                raise Exception(bstack111ll1l_opy_ (u"࡙ࠧࡴࡰࡲࠣࡶࡪࡷࡵࡦࡵࡷࠤࡳࡵࡴࠡࡱ࡮ࠦዣ"))
    @classmethod
    def bstack11l1111l11_opy_(cls):
        if cls.bstack11ll111l11_opy_ is None:
            return
        cls.bstack11ll111l11_opy_.shutdown()
    @classmethod
    def bstack111l11l11_opy_(cls):
        if cls.on():
            print(
                bstack111ll1l_opy_ (u"࠭ࡖࡪࡵ࡬ࡸࠥ࡮ࡴࡵࡲࡶ࠾࠴࠵࡯ࡣࡵࡨࡶࡻࡧࡢࡪ࡮࡬ࡸࡾ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡩ࡯࡮࠱ࡥࡹ࡮ࡲࡤࡴ࠱ࡾࢁࠥࡺ࡯ࠡࡸ࡬ࡩࡼࠦࡢࡶ࡫࡯ࡨࠥࡸࡥࡱࡱࡵࡸ࠱ࠦࡩ࡯ࡵ࡬࡫࡭ࡺࡳ࠭ࠢࡤࡲࡩࠦ࡭ࡢࡰࡼࠤࡲࡵࡲࡦࠢࡧࡩࡧࡻࡧࡨ࡫ࡱ࡫ࠥ࡯࡮ࡧࡱࡵࡱࡦࡺࡩࡰࡰࠣࡥࡱࡲࠠࡢࡶࠣࡳࡳ࡫ࠠࡱ࡮ࡤࡧࡪࠧ࡜࡯ࠩዤ").format(os.environ[bstack111ll1l_opy_ (u"ࠢࡃࡕࡢࡘࡊ࡙ࡔࡐࡒࡖࡣࡇ࡛ࡉࡍࡆࡢࡌࡆ࡙ࡈࡆࡆࡢࡍࡉࠨዥ")]))
    @classmethod
    def bstack11l11l1lll_opy_(cls):
        if cls.bstack11ll111l11_opy_ is not None:
            return
        cls.bstack11ll111l11_opy_ = bstack11ll11l111_opy_(cls.bstack11l11l1111_opy_)
        cls.bstack11ll111l11_opy_.start()
    @classmethod
    def bstack11l11lll11_opy_(cls, bstack11l11ll1l1_opy_, bstack11l111lll1_opy_=bstack111ll1l_opy_ (u"ࠨࡣࡳ࡭࠴ࡼ࠱࠰ࡤࡤࡸࡨ࡮ࠧዦ")):
        if not cls.on():
            return
        bstack111l11l1_opy_ = bstack11l11ll1l1_opy_[bstack111ll1l_opy_ (u"ࠩࡨࡺࡪࡴࡴࡠࡶࡼࡴࡪ࠭ዧ")]
        bstack11l1111ll1_opy_ = {
            bstack111ll1l_opy_ (u"ࠪࡘࡪࡹࡴࡓࡷࡱࡗࡹࡧࡲࡵࡧࡧࠫየ"): bstack111ll1l_opy_ (u"࡙ࠫ࡫ࡳࡵࡡࡖࡸࡦࡸࡴࡠࡗࡳࡰࡴࡧࡤࠨዩ"),
            bstack111ll1l_opy_ (u"࡚ࠬࡥࡴࡶࡕࡹࡳࡌࡩ࡯࡫ࡶ࡬ࡪࡪࠧዪ"): bstack111ll1l_opy_ (u"࠭ࡔࡦࡵࡷࡣࡊࡴࡤࡠࡗࡳࡰࡴࡧࡤࠨያ"),
            bstack111ll1l_opy_ (u"ࠧࡕࡧࡶࡸࡗࡻ࡮ࡔ࡭࡬ࡴࡵ࡫ࡤࠨዬ"): bstack111ll1l_opy_ (u"ࠨࡖࡨࡷࡹࡥࡓ࡬࡫ࡳࡴࡪࡪ࡟ࡖࡲ࡯ࡳࡦࡪࠧይ"),
            bstack111ll1l_opy_ (u"ࠩࡏࡳ࡬ࡉࡲࡦࡣࡷࡩࡩ࠭ዮ"): bstack111ll1l_opy_ (u"ࠪࡐࡴ࡭࡟ࡖࡲ࡯ࡳࡦࡪࠧዯ"),
            bstack111ll1l_opy_ (u"ࠫࡍࡵ࡯࡬ࡔࡸࡲࡘࡺࡡࡳࡶࡨࡨࠬደ"): bstack111ll1l_opy_ (u"ࠬࡎ࡯ࡰ࡭ࡢࡗࡹࡧࡲࡵࡡࡘࡴࡱࡵࡡࡥࠩዱ"),
            bstack111ll1l_opy_ (u"࠭ࡈࡰࡱ࡮ࡖࡺࡴࡆࡪࡰ࡬ࡷ࡭࡫ࡤࠨዲ"): bstack111ll1l_opy_ (u"ࠧࡉࡱࡲ࡯ࡤࡋ࡮ࡥࡡࡘࡴࡱࡵࡡࡥࠩዳ"),
            bstack111ll1l_opy_ (u"ࠨࡅࡅࡘࡘ࡫ࡳࡴ࡫ࡲࡲࡈࡸࡥࡢࡶࡨࡨࠬዴ"): bstack111ll1l_opy_ (u"ࠩࡆࡆ࡙ࡥࡕࡱ࡮ࡲࡥࡩ࠭ድ")
        }.get(bstack111l11l1_opy_)
        if bstack11l111lll1_opy_ == bstack111ll1l_opy_ (u"ࠪࡥࡵ࡯࠯ࡷ࠳࠲ࡦࡦࡺࡣࡩࠩዶ"):
            cls.bstack11l11l1lll_opy_()
            cls.bstack11ll111l11_opy_.add(bstack11l11ll1l1_opy_)
        elif bstack11l111lll1_opy_ == bstack111ll1l_opy_ (u"ࠫࡦࡶࡩ࠰ࡸ࠴࠳ࡸࡩࡲࡦࡧࡱࡷ࡭ࡵࡴࡴࠩዷ"):
            cls.bstack11l11l1111_opy_([bstack11l11ll1l1_opy_], bstack11l111lll1_opy_)
    @classmethod
    @bstack1l1lll11l1_opy_(class_method=True)
    def bstack11l11l1111_opy_(cls, bstack11l11ll1l1_opy_, bstack11l111lll1_opy_=bstack111ll1l_opy_ (u"ࠬࡧࡰࡪ࠱ࡹ࠵࠴ࡨࡡࡵࡥ࡫ࠫዸ")):
        config = {
            bstack111ll1l_opy_ (u"࠭ࡨࡦࡣࡧࡩࡷࡹࠧዹ"): cls.default_headers()
        }
        response = bstack11111l11l_opy_(bstack111ll1l_opy_ (u"ࠧࡑࡑࡖࡘࠬዺ"), cls.request_url(bstack11l111lll1_opy_), bstack11l11ll1l1_opy_, config)
        bstack1ll111111l_opy_ = response.json()
    @classmethod
    @bstack1l1lll11l1_opy_(class_method=True)
    def bstack11l111l1ll_opy_(cls, bstack11l11llll1_opy_):
        bstack11l11l11l1_opy_ = []
        for log in bstack11l11llll1_opy_:
            bstack11l1111l1l_opy_ = {
                bstack111ll1l_opy_ (u"ࠨ࡭࡬ࡲࡩ࠭ዻ"): bstack111ll1l_opy_ (u"ࠩࡗࡉࡘ࡚࡟ࡍࡑࡊࠫዼ"),
                bstack111ll1l_opy_ (u"ࠪࡰࡪࡼࡥ࡭ࠩዽ"): log[bstack111ll1l_opy_ (u"ࠫࡱ࡫ࡶࡦ࡮ࠪዾ")],
                bstack111ll1l_opy_ (u"ࠬࡺࡩ࡮ࡧࡶࡸࡦࡳࡰࠨዿ"): log[bstack111ll1l_opy_ (u"࠭ࡴࡪ࡯ࡨࡷࡹࡧ࡭ࡱࠩጀ")],
                bstack111ll1l_opy_ (u"ࠧࡩࡶࡷࡴࡤࡸࡥࡴࡲࡲࡲࡸ࡫ࠧጁ"): {},
                bstack111ll1l_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩጂ"): log[bstack111ll1l_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪጃ")],
            }
            if bstack111ll1l_opy_ (u"ࠪࡸࡪࡹࡴࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪጄ") in log:
                bstack11l1111l1l_opy_[bstack111ll1l_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫጅ")] = log[bstack111ll1l_opy_ (u"ࠬࡺࡥࡴࡶࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠬጆ")]
            elif bstack111ll1l_opy_ (u"࠭ࡨࡰࡱ࡮ࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭ጇ") in log:
                bstack11l1111l1l_opy_[bstack111ll1l_opy_ (u"ࠧࡩࡱࡲ࡯ࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧገ")] = log[bstack111ll1l_opy_ (u"ࠨࡪࡲࡳࡰࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨጉ")]
            bstack11l11l11l1_opy_.append(bstack11l1111l1l_opy_)
        cls.bstack11l11lll11_opy_({
            bstack111ll1l_opy_ (u"ࠩࡨࡺࡪࡴࡴࡠࡶࡼࡴࡪ࠭ጊ"): bstack111ll1l_opy_ (u"ࠪࡐࡴ࡭ࡃࡳࡧࡤࡸࡪࡪࠧጋ"),
            bstack111ll1l_opy_ (u"ࠫࡱࡵࡧࡴࠩጌ"): bstack11l11l11l1_opy_
        })
    @classmethod
    @bstack1l1lll11l1_opy_(class_method=True)
    def bstack11l111l111_opy_(cls, steps):
        bstack11l111llll_opy_ = []
        for step in steps:
            bstack11l11l1l1l_opy_ = {
                bstack111ll1l_opy_ (u"ࠬࡱࡩ࡯ࡦࠪግ"): bstack111ll1l_opy_ (u"࠭ࡔࡆࡕࡗࡣࡘ࡚ࡅࡑࠩጎ"),
                bstack111ll1l_opy_ (u"ࠧ࡭ࡧࡹࡩࡱ࠭ጏ"): step[bstack111ll1l_opy_ (u"ࠨ࡮ࡨࡺࡪࡲࠧጐ")],
                bstack111ll1l_opy_ (u"ࠩࡷ࡭ࡲ࡫ࡳࡵࡣࡰࡴࠬ጑"): step[bstack111ll1l_opy_ (u"ࠪࡸ࡮ࡳࡥࡴࡶࡤࡱࡵ࠭ጒ")],
                bstack111ll1l_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬጓ"): step[bstack111ll1l_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ࠭ጔ")],
                bstack111ll1l_opy_ (u"࠭ࡤࡶࡴࡤࡸ࡮ࡵ࡮ࠨጕ"): step[bstack111ll1l_opy_ (u"ࠧࡥࡷࡵࡥࡹ࡯࡯࡯ࠩ጖")]
            }
            if bstack111ll1l_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨ጗") in step:
                bstack11l11l1l1l_opy_[bstack111ll1l_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩጘ")] = step[bstack111ll1l_opy_ (u"ࠪࡸࡪࡹࡴࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪጙ")]
            elif bstack111ll1l_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫጚ") in step:
                bstack11l11l1l1l_opy_[bstack111ll1l_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠬጛ")] = step[bstack111ll1l_opy_ (u"࠭ࡨࡰࡱ࡮ࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭ጜ")]
            bstack11l111llll_opy_.append(bstack11l11l1l1l_opy_)
        cls.bstack11l11lll11_opy_({
            bstack111ll1l_opy_ (u"ࠧࡦࡸࡨࡲࡹࡥࡴࡺࡲࡨࠫጝ"): bstack111ll1l_opy_ (u"ࠨࡎࡲ࡫ࡈࡸࡥࡢࡶࡨࡨࠬጞ"),
            bstack111ll1l_opy_ (u"ࠩ࡯ࡳ࡬ࡹࠧጟ"): bstack11l111llll_opy_
        })
    @classmethod
    @bstack1l1lll11l1_opy_(class_method=True)
    def bstack11l111l11l_opy_(cls, screenshot):
        cls.bstack11l11lll11_opy_({
            bstack111ll1l_opy_ (u"ࠪࡩࡻ࡫࡮ࡵࡡࡷࡽࡵ࡫ࠧጠ"): bstack111ll1l_opy_ (u"ࠫࡑࡵࡧࡄࡴࡨࡥࡹ࡫ࡤࠨጡ"),
            bstack111ll1l_opy_ (u"ࠬࡲ࡯ࡨࡵࠪጢ"): [{
                bstack111ll1l_opy_ (u"࠭࡫ࡪࡰࡧࠫጣ"): bstack111ll1l_opy_ (u"ࠧࡕࡇࡖࡘࡤ࡙ࡃࡓࡇࡈࡒࡘࡎࡏࡕࠩጤ"),
                bstack111ll1l_opy_ (u"ࠨࡶ࡬ࡱࡪࡹࡴࡢ࡯ࡳࠫጥ"): datetime.datetime.utcnow().isoformat() + bstack111ll1l_opy_ (u"ࠩ࡝ࠫጦ"),
                bstack111ll1l_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫጧ"): screenshot[bstack111ll1l_opy_ (u"ࠫ࡮ࡳࡡࡨࡧࠪጨ")],
                bstack111ll1l_opy_ (u"ࠬࡺࡥࡴࡶࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠬጩ"): screenshot[bstack111ll1l_opy_ (u"࠭ࡴࡦࡵࡷࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭ጪ")]
            }]
        }, bstack11l111lll1_opy_=bstack111ll1l_opy_ (u"ࠧࡢࡲ࡬࠳ࡻ࠷࠯ࡴࡥࡵࡩࡪࡴࡳࡩࡱࡷࡷࠬጫ"))
    @classmethod
    @bstack1l1lll11l1_opy_(class_method=True)
    def bstack1lll1111l_opy_(cls, driver):
        current_test_uuid = cls.current_test_uuid()
        if not current_test_uuid:
            return
        cls.bstack11l11lll11_opy_({
            bstack111ll1l_opy_ (u"ࠨࡧࡹࡩࡳࡺ࡟ࡵࡻࡳࡩࠬጬ"): bstack111ll1l_opy_ (u"ࠩࡆࡆ࡙࡙ࡥࡴࡵ࡬ࡳࡳࡉࡲࡦࡣࡷࡩࡩ࠭ጭ"),
            bstack111ll1l_opy_ (u"ࠪࡸࡪࡹࡴࡠࡴࡸࡲࠬጮ"): {
                bstack111ll1l_opy_ (u"ࠦࡺࡻࡩࡥࠤጯ"): cls.current_test_uuid(),
                bstack111ll1l_opy_ (u"ࠧ࡯࡮ࡵࡧࡪࡶࡦࡺࡩࡰࡰࡶࠦጰ"): cls.bstack11l1111lll_opy_(driver)
            }
        })
    @classmethod
    def on(cls):
        if os.environ.get(bstack111ll1l_opy_ (u"࠭ࡂࡔࡡࡗࡉࡘ࡚ࡏࡑࡕࡢࡎ࡜࡚ࠧጱ"), None) is None or os.environ[bstack111ll1l_opy_ (u"ࠧࡃࡕࡢࡘࡊ࡙ࡔࡐࡒࡖࡣࡏ࡝ࡔࠨጲ")] == bstack111ll1l_opy_ (u"ࠣࡰࡸࡰࡱࠨጳ"):
            return False
        return True
    @classmethod
    def bstack11l11l1l11_opy_(cls):
        return bstack1l1l11ll11_opy_(cls.bs_config.get(bstack111ll1l_opy_ (u"ࠩࡷࡩࡸࡺࡏࡣࡵࡨࡶࡻࡧࡢࡪ࡮࡬ࡸࡾ࠭ጴ"), False))
    @staticmethod
    def request_url(url):
        return bstack111ll1l_opy_ (u"ࠪࡿࢂ࠵ࡻࡾࠩጵ").format(bstack11l11ll1ll_opy_, url)
    @staticmethod
    def default_headers():
        headers = {
            bstack111ll1l_opy_ (u"ࠫࡈࡵ࡮ࡵࡧࡱࡸ࠲࡚ࡹࡱࡧࠪጶ"): bstack111ll1l_opy_ (u"ࠬࡧࡰࡱ࡮࡬ࡧࡦࡺࡩࡰࡰ࠲࡮ࡸࡵ࡮ࠨጷ"),
            bstack111ll1l_opy_ (u"࠭ࡘ࠮ࡄࡖࡘࡆࡉࡋ࠮ࡖࡈࡗ࡙ࡕࡐࡔࠩጸ"): bstack111ll1l_opy_ (u"ࠧࡵࡴࡸࡩࠬጹ")
        }
        if os.environ.get(bstack111ll1l_opy_ (u"ࠨࡄࡖࡣ࡙ࡋࡓࡕࡑࡓࡗࡤࡐࡗࡕࠩጺ"), None):
            headers[bstack111ll1l_opy_ (u"ࠩࡄࡹࡹ࡮࡯ࡳ࡫ࡽࡥࡹ࡯࡯࡯ࠩጻ")] = bstack111ll1l_opy_ (u"ࠪࡆࡪࡧࡲࡦࡴࠣࡿࢂ࠭ጼ").format(os.environ[bstack111ll1l_opy_ (u"ࠦࡇ࡙࡟ࡕࡇࡖࡘࡔࡖࡓࡠࡌ࡚ࡘࠧጽ")])
        return headers
    @staticmethod
    def current_test_uuid():
        return getattr(threading.current_thread(), bstack111ll1l_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡴࡦࡵࡷࡣࡺࡻࡩࡥࠩጾ"), None)
    @staticmethod
    def bstack11l1111lll_opy_(driver):
        return {
            bstack1l1l11l1l1_opy_(): bstack1l1l1l111l_opy_(driver)
        }
    @staticmethod
    def bstack11l111l1l1_opy_(exception_info, report):
        return [{bstack111ll1l_opy_ (u"࠭ࡢࡢࡥ࡮ࡸࡷࡧࡣࡦࠩጿ"): [exception_info.exconly(), report.longreprtext]}]
    @staticmethod
    def bstack1l11ll1l1l_opy_(typename):
        if bstack111ll1l_opy_ (u"ࠢࡂࡵࡶࡩࡷࡺࡩࡰࡰࠥፀ") in typename:
            return bstack111ll1l_opy_ (u"ࠣࡃࡶࡷࡪࡸࡴࡪࡱࡱࡉࡷࡸ࡯ࡳࠤፁ")
        return bstack111ll1l_opy_ (u"ࠤࡘࡲ࡭ࡧ࡮ࡥ࡮ࡨࡨࡊࡸࡲࡰࡴࠥፂ")
    @staticmethod
    def bstack11l11l1ll1_opy_(func):
        def wrap(*args, **kwargs):
            if bstack1l11lll1l_opy_.on():
                return func(*args, **kwargs)
            return
        return wrap
    @staticmethod
    def bstack11l11111ll_opy_(test, hook_name=None):
        bstack11l11l111l_opy_ = test.parent
        if hook_name in [bstack111ll1l_opy_ (u"ࠪࡷࡪࡺࡵࡱࡡࡦࡰࡦࡹࡳࠨፃ"), bstack111ll1l_opy_ (u"ࠫࡹ࡫ࡡࡳࡦࡲࡻࡳࡥࡣ࡭ࡣࡶࡷࠬፄ"), bstack111ll1l_opy_ (u"ࠬࡹࡥࡵࡷࡳࡣࡲࡵࡤࡶ࡮ࡨࠫፅ"), bstack111ll1l_opy_ (u"࠭ࡴࡦࡣࡵࡨࡴࡽ࡮ࡠ࡯ࡲࡨࡺࡲࡥࠨፆ")]:
            bstack11l11l111l_opy_ = test
        scope = []
        while bstack11l11l111l_opy_ is not None:
            scope.append(bstack11l11l111l_opy_.name)
            bstack11l11l111l_opy_ = bstack11l11l111l_opy_.parent
        scope.reverse()
        return scope[2:]
    @staticmethod
    def bstack11l1l11111_opy_(hook_type):
        if hook_type == bstack111ll1l_opy_ (u"ࠢࡃࡇࡉࡓࡗࡋ࡟ࡆࡃࡆࡌࠧፇ"):
            return bstack111ll1l_opy_ (u"ࠣࡕࡨࡸࡺࡶࠠࡩࡱࡲ࡯ࠧፈ")
        elif hook_type == bstack111ll1l_opy_ (u"ࠤࡄࡊ࡙ࡋࡒࡠࡇࡄࡇࡍࠨፉ"):
            return bstack111ll1l_opy_ (u"ࠥࡘࡪࡧࡲࡥࡱࡺࡲࠥ࡮࡯ࡰ࡭ࠥፊ")
    @staticmethod
    def bstack11l111ll11_opy_(bstack1l11l1lll_opy_):
        try:
            if not bstack1l11lll1l_opy_.on():
                return bstack1l11l1lll_opy_
            if os.environ.get(bstack111ll1l_opy_ (u"ࠦࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡖࡊࡘࡕࡏࠤፋ"), None) == bstack111ll1l_opy_ (u"ࠧࡺࡲࡶࡧࠥፌ"):
                tests = os.environ.get(bstack111ll1l_opy_ (u"ࠨࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡘࡅࡓࡗࡑࡣ࡙ࡋࡓࡕࡕࠥፍ"), None)
                if tests is None or tests == bstack111ll1l_opy_ (u"ࠢ࡯ࡷ࡯ࡰࠧፎ"):
                    return bstack1l11l1lll_opy_
                bstack1l11l1lll_opy_ = tests.split(bstack111ll1l_opy_ (u"ࠨ࠮ࠪፏ"))
                return bstack1l11l1lll_opy_
        except Exception as exc:
            print(bstack111ll1l_opy_ (u"ࠤࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡴࡨࡶࡺࡴࠠࡩࡣࡱࡨࡱ࡫ࡲ࠻ࠢࠥፐ"), str(exc))
        return bstack1l11l1lll_opy_
    @classmethod
    def bstack11l11lll1l_opy_(cls, event: str, bstack11l11ll1l1_opy_: bstack11l1l11ll1_opy_):
        bstack11l11lllll_opy_ = {
            bstack111ll1l_opy_ (u"ࠪࡩࡻ࡫࡮ࡵࡡࡷࡽࡵ࡫ࠧፑ"): event,
            bstack11l11ll1l1_opy_.bstack11l1l11l1l_opy_(): bstack11l11ll1l1_opy_.bstack11l1l1l1l1_opy_(event)
        }
        bstack1l11lll1l_opy_.bstack11l11lll11_opy_(bstack11l11lllll_opy_)