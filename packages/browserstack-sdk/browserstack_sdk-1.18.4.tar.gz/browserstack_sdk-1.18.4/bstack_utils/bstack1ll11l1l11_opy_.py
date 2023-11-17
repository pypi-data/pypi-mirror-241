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
import datetime
import json
import logging
import os
import threading
from bstack_utils.helper import bstack1l1ll111ll_opy_, bstack11l111ll_opy_, get_host_info, bstack1l1ll11ll1_opy_, bstack1l1l1llll1_opy_, bstack1l11ll11l1_opy_, \
    bstack1l11l11l1l_opy_, bstack1l11l1l111_opy_, bstack1llll1l11l_opy_, bstack1l111ll11l_opy_, bstack1l11ll1111_opy_, bstack1l1lll1111_opy_
from bstack_utils.bstack11l1ll1111_opy_ import bstack11l1ll1l1l_opy_
from bstack_utils.bstack11l11ll1l1_opy_ import bstack11l11ll1ll_opy_
bstack111lll1lll_opy_ = [
    bstack1ll_opy_ (u"ࠬࡒ࡯ࡨࡅࡵࡩࡦࡺࡥࡥࠩኹ"), bstack1ll_opy_ (u"࠭ࡃࡃࡖࡖࡩࡸࡹࡩࡰࡰࡆࡶࡪࡧࡴࡦࡦࠪኺ"), bstack1ll_opy_ (u"ࠧࡕࡧࡶࡸࡗࡻ࡮ࡇ࡫ࡱ࡭ࡸ࡮ࡥࡥࠩኻ"), bstack1ll_opy_ (u"ࠨࡖࡨࡷࡹࡘࡵ࡯ࡕ࡮࡭ࡵࡶࡥࡥࠩኼ"),
    bstack1ll_opy_ (u"ࠩࡋࡳࡴࡱࡒࡶࡰࡉ࡭ࡳ࡯ࡳࡩࡧࡧࠫኽ"), bstack1ll_opy_ (u"ࠪࡘࡪࡹࡴࡓࡷࡱࡗࡹࡧࡲࡵࡧࡧࠫኾ"), bstack1ll_opy_ (u"ࠫࡍࡵ࡯࡬ࡔࡸࡲࡘࡺࡡࡳࡶࡨࡨࠬ኿")
]
bstack111lll11ll_opy_ = bstack1ll_opy_ (u"ࠬ࡮ࡴࡵࡲࡶ࠾࠴࠵ࡣࡰ࡮࡯ࡩࡨࡺ࡯ࡳ࠯ࡲࡦࡸ࡫ࡲࡷࡣࡥ࡭ࡱ࡯ࡴࡺ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡥࡲࡱࠬዀ")
logger = logging.getLogger(__name__)
class bstack11l1l1l1_opy_:
    bstack11l1ll1111_opy_ = None
    bs_config = None
    @classmethod
    @bstack1l1lll1111_opy_(class_method=True)
    def launch(cls, bs_config, bstack111llll1ll_opy_):
        cls.bs_config = bs_config
        if not cls.bstack11l1111lll_opy_():
            return
        cls.bstack111lll1111_opy_()
        bstack1l1l1lll1l_opy_ = bstack1l1ll11ll1_opy_(bs_config)
        bstack1l1l1ll111_opy_ = bstack1l1l1llll1_opy_(bs_config)
        data = {
            bstack1ll_opy_ (u"࠭ࡦࡰࡴࡰࡥࡹ࠭዁"): bstack1ll_opy_ (u"ࠧ࡫ࡵࡲࡲࠬዂ"),
            bstack1ll_opy_ (u"ࠨࡲࡵࡳ࡯࡫ࡣࡵࡡࡱࡥࡲ࡫ࠧዃ"): bs_config.get(bstack1ll_opy_ (u"ࠩࡳࡶࡴࡰࡥࡤࡶࡑࡥࡲ࡫ࠧዄ"), bstack1ll_opy_ (u"ࠪࠫዅ")),
            bstack1ll_opy_ (u"ࠫࡳࡧ࡭ࡦࠩ዆"): bs_config.get(bstack1ll_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡒࡦࡳࡥࠨ዇"), os.path.basename(os.path.abspath(os.getcwd()))),
            bstack1ll_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡤ࡯ࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩወ"): bs_config.get(bstack1ll_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩዉ")),
            bstack1ll_opy_ (u"ࠨࡦࡨࡷࡨࡸࡩࡱࡶ࡬ࡳࡳ࠭ዊ"): bs_config.get(bstack1ll_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡅࡧࡶࡧࡷ࡯ࡰࡵ࡫ࡲࡲࠬዋ"), bstack1ll_opy_ (u"ࠪࠫዌ")),
            bstack1ll_opy_ (u"ࠫࡸࡺࡡࡳࡶࡢࡸ࡮ࡳࡥࠨው"): datetime.datetime.now().isoformat(),
            bstack1ll_opy_ (u"ࠬࡺࡡࡨࡵࠪዎ"): bstack1l11ll11l1_opy_(bs_config),
            bstack1ll_opy_ (u"࠭ࡨࡰࡵࡷࡣ࡮ࡴࡦࡰࠩዏ"): get_host_info(),
            bstack1ll_opy_ (u"ࠧࡤ࡫ࡢ࡭ࡳ࡬࡯ࠨዐ"): bstack11l111ll_opy_(),
            bstack1ll_opy_ (u"ࠨࡤࡸ࡭ࡱࡪ࡟ࡳࡷࡱࡣ࡮ࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨዑ"): os.environ.get(bstack1ll_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡄࡘࡍࡑࡊ࡟ࡓࡗࡑࡣࡎࡊࡅࡏࡖࡌࡊࡎࡋࡒࠨዒ")),
            bstack1ll_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࡢࡸࡪࡹࡴࡴࡡࡵࡩࡷࡻ࡮ࠨዓ"): os.environ.get(bstack1ll_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡖࡊࡘࡕࡏࠩዔ"), False),
            bstack1ll_opy_ (u"ࠬࡼࡥࡳࡵ࡬ࡳࡳࡥࡣࡰࡰࡷࡶࡴࡲࠧዕ"): bstack1l1ll111ll_opy_(),
            bstack1ll_opy_ (u"࠭࡯ࡣࡵࡨࡶࡻࡧࡢࡪ࡮࡬ࡸࡾࡥࡶࡦࡴࡶ࡭ࡴࡴࠧዖ"): {
                bstack1ll_opy_ (u"ࠧࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡑࡥࡲ࡫ࠧ዗"): bstack111llll1ll_opy_.get(bstack1ll_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡳࡧ࡭ࡦࠩዘ"), bstack1ll_opy_ (u"ࠩࡓࡽࡹ࡫ࡳࡵࠩዙ")),
                bstack1ll_opy_ (u"ࠪࡪࡷࡧ࡭ࡦࡹࡲࡶࡰ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ዚ"): bstack111llll1ll_opy_.get(bstack1ll_opy_ (u"ࠫ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠨዛ")),
                bstack1ll_opy_ (u"ࠬࡹࡤ࡬ࡘࡨࡶࡸ࡯࡯࡯ࠩዜ"): bstack111llll1ll_opy_.get(bstack1ll_opy_ (u"࠭ࡳࡥ࡭ࡢࡺࡪࡸࡳࡪࡱࡱࠫዝ"))
            }
        }
        config = {
            bstack1ll_opy_ (u"ࠧࡢࡷࡷ࡬ࠬዞ"): (bstack1l1l1lll1l_opy_, bstack1l1l1ll111_opy_),
            bstack1ll_opy_ (u"ࠨࡪࡨࡥࡩ࡫ࡲࡴࠩዟ"): cls.default_headers()
        }
        response = bstack1llll1l11l_opy_(bstack1ll_opy_ (u"ࠩࡓࡓࡘ࡚ࠧዠ"), cls.request_url(bstack1ll_opy_ (u"ࠪࡥࡵ࡯࠯ࡷ࠳࠲ࡦࡺ࡯࡬ࡥࡵࠪዡ")), data, config)
        if response.status_code != 200:
            os.environ[bstack1ll_opy_ (u"ࠫࡇ࡙࡟ࡕࡇࡖࡘࡔࡖࡓࡠࡄࡘࡍࡑࡊ࡟ࡄࡑࡐࡔࡑࡋࡔࡆࡆࠪዢ")] = bstack1ll_opy_ (u"ࠬ࡬ࡡ࡭ࡵࡨࠫዣ")
            os.environ[bstack1ll_opy_ (u"࠭ࡂࡔࡡࡗࡉࡘ࡚ࡏࡑࡕࡢࡎ࡜࡚ࠧዤ")] = bstack1ll_opy_ (u"ࠧ࡯ࡷ࡯ࡰࠬዥ")
            os.environ[bstack1ll_opy_ (u"ࠨࡄࡖࡣ࡙ࡋࡓࡕࡑࡓࡗࡤࡈࡕࡊࡎࡇࡣࡍࡇࡓࡉࡇࡇࡣࡎࡊࠧዦ")] = bstack1ll_opy_ (u"ࠤࡱࡹࡱࡲࠢዧ")
            os.environ[bstack1ll_opy_ (u"ࠪࡆࡘࡥࡔࡆࡕࡗࡓࡕ࡙࡟ࡂࡎࡏࡓ࡜ࡥࡓࡄࡔࡈࡉࡓ࡙ࡈࡐࡖࡖࠫየ")] = bstack1ll_opy_ (u"ࠦࡳࡻ࡬࡭ࠤዩ")
            bstack111llll111_opy_ = response.json()
            if bstack111llll111_opy_ and bstack111llll111_opy_[bstack1ll_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ࠭ዪ")]:
                error_message = bstack111llll111_opy_[bstack1ll_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧያ")]
                if bstack111llll111_opy_[bstack1ll_opy_ (u"ࠧࡦࡴࡵࡳࡷ࡚ࡹࡱࡧࠪዬ")] == bstack1ll_opy_ (u"ࠨࡇࡕࡖࡔࡘ࡟ࡊࡐ࡙ࡅࡑࡏࡄࡠࡅࡕࡉࡉࡋࡎࡕࡋࡄࡐࡘ࠭ይ"):
                    logger.error(error_message)
                elif bstack111llll111_opy_[bstack1ll_opy_ (u"ࠩࡨࡶࡷࡵࡲࡕࡻࡳࡩࠬዮ")] == bstack1ll_opy_ (u"ࠪࡉࡗࡘࡏࡓࡡࡄࡇࡈࡋࡓࡔࡡࡇࡉࡓࡏࡅࡅࠩዯ"):
                    logger.info(error_message)
                elif bstack111llll111_opy_[bstack1ll_opy_ (u"ࠫࡪࡸࡲࡰࡴࡗࡽࡵ࡫ࠧደ")] == bstack1ll_opy_ (u"ࠬࡋࡒࡓࡑࡕࡣࡘࡊࡋࡠࡆࡈࡔࡗࡋࡃࡂࡖࡈࡈࠬዱ"):
                    logger.error(error_message)
                else:
                    logger.error(error_message)
            else:
                logger.error(bstack1ll_opy_ (u"ࠨࡄࡢࡶࡤࠤࡺࡶ࡬ࡰࡣࡧࠤࡹࡵࠠࡃࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࠦࡔࡦࡵࡷࠤࡔࡨࡳࡦࡴࡹࡥࡧ࡯࡬ࡪࡶࡼࠤ࡫ࡧࡩ࡭ࡧࡧࠤࡩࡻࡥࠡࡶࡲࠤࡸࡵ࡭ࡦࠢࡨࡶࡷࡵࡲࠣዲ"))
            return [None, None, None]
        logger.debug(bstack1ll_opy_ (u"ࠧࡕࡧࡶࡸࠥࡕࡢࡴࡧࡵࡺࡦࡨࡩ࡭࡫ࡷࡽࠥࡈࡵࡪ࡮ࡧࠤࡨࡸࡥࡢࡶ࡬ࡳࡳࠦࡓࡶࡥࡦࡩࡸࡹࡦࡶ࡮ࠤࠫዳ"))
        os.environ[bstack1ll_opy_ (u"ࠨࡄࡖࡣ࡙ࡋࡓࡕࡑࡓࡗࡤࡈࡕࡊࡎࡇࡣࡈࡕࡍࡑࡎࡈࡘࡊࡊࠧዴ")] = bstack1ll_opy_ (u"ࠩࡷࡶࡺ࡫ࠧድ")
        bstack111llll111_opy_ = response.json()
        if bstack111llll111_opy_.get(bstack1ll_opy_ (u"ࠪ࡮ࡼࡺࠧዶ")):
            os.environ[bstack1ll_opy_ (u"ࠫࡇ࡙࡟ࡕࡇࡖࡘࡔࡖࡓࡠࡌ࡚ࡘࠬዷ")] = bstack111llll111_opy_[bstack1ll_opy_ (u"ࠬࡰࡷࡵࠩዸ")]
            os.environ[bstack1ll_opy_ (u"࠭ࡃࡓࡇࡇࡉࡓ࡚ࡉࡂࡎࡖࡣࡋࡕࡒࡠࡅࡕࡅࡘࡎ࡟ࡓࡇࡓࡓࡗ࡚ࡉࡏࡉࠪዹ")] = json.dumps({
                bstack1ll_opy_ (u"ࠧࡶࡵࡨࡶࡳࡧ࡭ࡦࠩዺ"): bstack1l1l1lll1l_opy_,
                bstack1ll_opy_ (u"ࠨࡲࡤࡷࡸࡽ࡯ࡳࡦࠪዻ"): bstack1l1l1ll111_opy_
            })
        if bstack111llll111_opy_.get(bstack1ll_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡠࡪࡤࡷ࡭࡫ࡤࡠ࡫ࡧࠫዼ")):
            os.environ[bstack1ll_opy_ (u"ࠪࡆࡘࡥࡔࡆࡕࡗࡓࡕ࡙࡟ࡃࡗࡌࡐࡉࡥࡈࡂࡕࡋࡉࡉࡥࡉࡅࠩዽ")] = bstack111llll111_opy_[bstack1ll_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡢ࡬ࡦࡹࡨࡦࡦࡢ࡭ࡩ࠭ዾ")]
        if bstack111llll111_opy_.get(bstack1ll_opy_ (u"ࠬࡧ࡬࡭ࡱࡺࡣࡸࡩࡲࡦࡧࡱࡷ࡭ࡵࡴࡴࠩዿ")):
            os.environ[bstack1ll_opy_ (u"࠭ࡂࡔࡡࡗࡉࡘ࡚ࡏࡑࡕࡢࡅࡑࡒࡏࡘࡡࡖࡇࡗࡋࡅࡏࡕࡋࡓ࡙࡙ࠧጀ")] = str(bstack111llll111_opy_[bstack1ll_opy_ (u"ࠧࡢ࡮࡯ࡳࡼࡥࡳࡤࡴࡨࡩࡳࡹࡨࡰࡶࡶࠫጁ")])
        return [bstack111llll111_opy_[bstack1ll_opy_ (u"ࠨ࡬ࡺࡸࠬጂ")], bstack111llll111_opy_[bstack1ll_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡠࡪࡤࡷ࡭࡫ࡤࡠ࡫ࡧࠫጃ")], bstack111llll111_opy_[bstack1ll_opy_ (u"ࠪࡥࡱࡲ࡯ࡸࡡࡶࡧࡷ࡫ࡥ࡯ࡵ࡫ࡳࡹࡹࠧጄ")]]
    @classmethod
    @bstack1l1lll1111_opy_(class_method=True)
    def stop(cls):
        if not cls.on():
            return
        if os.environ[bstack1ll_opy_ (u"ࠫࡇ࡙࡟ࡕࡇࡖࡘࡔࡖࡓࡠࡌ࡚ࡘࠬጅ")] == bstack1ll_opy_ (u"ࠧࡴࡵ࡭࡮ࠥጆ") or os.environ[bstack1ll_opy_ (u"࠭ࡂࡔࡡࡗࡉࡘ࡚ࡏࡑࡕࡢࡆ࡚ࡏࡌࡅࡡࡋࡅࡘࡎࡅࡅࡡࡌࡈࠬጇ")] == bstack1ll_opy_ (u"ࠢ࡯ࡷ࡯ࡰࠧገ"):
            print(bstack1ll_opy_ (u"ࠨࡇ࡛ࡇࡊࡖࡔࡊࡑࡑࠤࡎࡔࠠࡴࡶࡲࡴࡇࡻࡩ࡭ࡦࡘࡴࡸࡺࡲࡦࡣࡰࠤࡗࡋࡑࡖࡇࡖࡘ࡚ࠥࡏࠡࡖࡈࡗ࡙ࠦࡏࡃࡕࡈࡖ࡛ࡇࡂࡊࡎࡌࡘ࡞ࠦ࠺ࠡࡏ࡬ࡷࡸ࡯࡮ࡨࠢࡤࡹࡹ࡮ࡥ࡯ࡶ࡬ࡧࡦࡺࡩࡰࡰࠣࡸࡴࡱࡥ࡯ࠩጉ"))
            return {
                bstack1ll_opy_ (u"ࠩࡶࡸࡦࡺࡵࡴࠩጊ"): bstack1ll_opy_ (u"ࠪࡩࡷࡸ࡯ࡳࠩጋ"),
                bstack1ll_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬጌ"): bstack1ll_opy_ (u"࡚ࠬ࡯࡬ࡧࡱ࠳ࡧࡻࡩ࡭ࡦࡌࡈࠥ࡯ࡳࠡࡷࡱࡨࡪ࡬ࡩ࡯ࡧࡧ࠰ࠥࡨࡵࡪ࡮ࡧࠤࡨࡸࡥࡢࡶ࡬ࡳࡳࠦ࡭ࡪࡩ࡫ࡸࠥ࡮ࡡࡷࡧࠣࡪࡦ࡯࡬ࡦࡦࠪግ")
            }
        else:
            cls.bstack11l1ll1111_opy_.shutdown()
            data = {
                bstack1ll_opy_ (u"࠭ࡳࡵࡱࡳࡣࡹ࡯࡭ࡦࠩጎ"): datetime.datetime.now().isoformat()
            }
            config = {
                bstack1ll_opy_ (u"ࠧࡩࡧࡤࡨࡪࡸࡳࠨጏ"): cls.default_headers()
            }
            bstack1l11llllll_opy_ = bstack1ll_opy_ (u"ࠨࡣࡳ࡭࠴ࡼ࠱࠰ࡤࡸ࡭ࡱࡪࡳ࠰ࡽࢀ࠳ࡸࡺ࡯ࡱࠩጐ").format(os.environ[bstack1ll_opy_ (u"ࠤࡅࡗࡤ࡚ࡅࡔࡖࡒࡔࡘࡥࡂࡖࡋࡏࡈࡤࡎࡁࡔࡊࡈࡈࡤࡏࡄࠣ጑")])
            bstack111ll1ll1l_opy_ = cls.request_url(bstack1l11llllll_opy_)
            response = bstack1llll1l11l_opy_(bstack1ll_opy_ (u"ࠪࡔ࡚࡚ࠧጒ"), bstack111ll1ll1l_opy_, data, config)
            if not response.ok:
                raise Exception(bstack1ll_opy_ (u"ࠦࡘࡺ࡯ࡱࠢࡵࡩࡶࡻࡥࡴࡶࠣࡲࡴࡺࠠࡰ࡭ࠥጓ"))
    @classmethod
    def bstack11l1111l11_opy_(cls):
        if cls.bstack11l1ll1111_opy_ is None:
            return
        cls.bstack11l1ll1111_opy_.shutdown()
    @classmethod
    def bstack1ll1l1lll1_opy_(cls):
        if cls.on():
            print(
                bstack1ll_opy_ (u"ࠬ࡜ࡩࡴ࡫ࡷࠤ࡭ࡺࡴࡱࡵ࠽࠳࠴ࡵࡢࡴࡧࡵࡺࡦࡨࡩ࡭࡫ࡷࡽ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡨࡵ࡭࠰ࡤࡸ࡭ࡱࡪࡳ࠰ࡽࢀࠤࡹࡵࠠࡷ࡫ࡨࡻࠥࡨࡵࡪ࡮ࡧࠤࡷ࡫ࡰࡰࡴࡷ࠰ࠥ࡯࡮ࡴ࡫ࡪ࡬ࡹࡹࠬࠡࡣࡱࡨࠥࡳࡡ࡯ࡻࠣࡱࡴࡸࡥࠡࡦࡨࡦࡺ࡭ࡧࡪࡰࡪࠤ࡮ࡴࡦࡰࡴࡰࡥࡹ࡯࡯࡯ࠢࡤࡰࡱࠦࡡࡵࠢࡲࡲࡪࠦࡰ࡭ࡣࡦࡩࠦࡢ࡮ࠨጔ").format(os.environ[bstack1ll_opy_ (u"ࠨࡂࡔࡡࡗࡉࡘ࡚ࡏࡑࡕࡢࡆ࡚ࡏࡌࡅࡡࡋࡅࡘࡎࡅࡅࡡࡌࡈࠧጕ")]))
    @classmethod
    def bstack111lll1111_opy_(cls):
        if cls.bstack11l1ll1111_opy_ is not None:
            return
        cls.bstack11l1ll1111_opy_ = bstack11l1ll1l1l_opy_(cls.bstack111ll1l1l1_opy_)
        cls.bstack11l1ll1111_opy_.start()
    @classmethod
    def bstack111ll1l1ll_opy_(cls, bstack111lll1l1l_opy_, bstack111lllllll_opy_=bstack1ll_opy_ (u"ࠧࡢࡲ࡬࠳ࡻ࠷࠯ࡣࡣࡷࡧ࡭࠭጖")):
        if not cls.on():
            return
        bstack1l1l11ll_opy_ = bstack111lll1l1l_opy_[bstack1ll_opy_ (u"ࠨࡧࡹࡩࡳࡺ࡟ࡵࡻࡳࡩࠬ጗")]
        bstack11l11111l1_opy_ = {
            bstack1ll_opy_ (u"ࠩࡗࡩࡸࡺࡒࡶࡰࡖࡸࡦࡸࡴࡦࡦࠪጘ"): bstack1ll_opy_ (u"ࠪࡘࡪࡹࡴࡠࡕࡷࡥࡷࡺ࡟ࡖࡲ࡯ࡳࡦࡪࠧጙ"),
            bstack1ll_opy_ (u"࡙ࠫ࡫ࡳࡵࡔࡸࡲࡋ࡯࡮ࡪࡵ࡫ࡩࡩ࠭ጚ"): bstack1ll_opy_ (u"࡚ࠬࡥࡴࡶࡢࡉࡳࡪ࡟ࡖࡲ࡯ࡳࡦࡪࠧጛ"),
            bstack1ll_opy_ (u"࠭ࡔࡦࡵࡷࡖࡺࡴࡓ࡬࡫ࡳࡴࡪࡪࠧጜ"): bstack1ll_opy_ (u"ࠧࡕࡧࡶࡸࡤ࡙࡫ࡪࡲࡳࡩࡩࡥࡕࡱ࡮ࡲࡥࡩ࠭ጝ"),
            bstack1ll_opy_ (u"ࠨࡎࡲ࡫ࡈࡸࡥࡢࡶࡨࡨࠬጞ"): bstack1ll_opy_ (u"ࠩࡏࡳ࡬ࡥࡕࡱ࡮ࡲࡥࡩ࠭ጟ"),
            bstack1ll_opy_ (u"ࠪࡌࡴࡵ࡫ࡓࡷࡱࡗࡹࡧࡲࡵࡧࡧࠫጠ"): bstack1ll_opy_ (u"ࠫࡍࡵ࡯࡬ࡡࡖࡸࡦࡸࡴࡠࡗࡳࡰࡴࡧࡤࠨጡ"),
            bstack1ll_opy_ (u"ࠬࡎ࡯ࡰ࡭ࡕࡹࡳࡌࡩ࡯࡫ࡶ࡬ࡪࡪࠧጢ"): bstack1ll_opy_ (u"࠭ࡈࡰࡱ࡮ࡣࡊࡴࡤࡠࡗࡳࡰࡴࡧࡤࠨጣ"),
            bstack1ll_opy_ (u"ࠧࡄࡄࡗࡗࡪࡹࡳࡪࡱࡱࡇࡷ࡫ࡡࡵࡧࡧࠫጤ"): bstack1ll_opy_ (u"ࠨࡅࡅࡘࡤ࡛ࡰ࡭ࡱࡤࡨࠬጥ")
        }.get(bstack1l1l11ll_opy_)
        if bstack111lllllll_opy_ == bstack1ll_opy_ (u"ࠩࡤࡴ࡮࠵ࡶ࠲࠱ࡥࡥࡹࡩࡨࠨጦ"):
            cls.bstack111lll1111_opy_()
            cls.bstack11l1ll1111_opy_.add(bstack111lll1l1l_opy_)
        elif bstack111lllllll_opy_ == bstack1ll_opy_ (u"ࠪࡥࡵ࡯࠯ࡷ࠳࠲ࡷࡨࡸࡥࡦࡰࡶ࡬ࡴࡺࡳࠨጧ"):
            cls.bstack111ll1l1l1_opy_([bstack111lll1l1l_opy_], bstack111lllllll_opy_)
    @classmethod
    @bstack1l1lll1111_opy_(class_method=True)
    def bstack111ll1l1l1_opy_(cls, bstack111lll1l1l_opy_, bstack111lllllll_opy_=bstack1ll_opy_ (u"ࠫࡦࡶࡩ࠰ࡸ࠴࠳ࡧࡧࡴࡤࡪࠪጨ")):
        config = {
            bstack1ll_opy_ (u"ࠬ࡮ࡥࡢࡦࡨࡶࡸ࠭ጩ"): cls.default_headers()
        }
        response = bstack1llll1l11l_opy_(bstack1ll_opy_ (u"࠭ࡐࡐࡕࡗࠫጪ"), cls.request_url(bstack111lllllll_opy_), bstack111lll1l1l_opy_, config)
        bstack1l1l1lll11_opy_ = response.json()
    @classmethod
    @bstack1l1lll1111_opy_(class_method=True)
    def bstack11l1111l1l_opy_(cls, bstack111lllll11_opy_):
        bstack111llll1l1_opy_ = []
        for log in bstack111lllll11_opy_:
            bstack111ll1lll1_opy_ = {
                bstack1ll_opy_ (u"ࠧ࡬࡫ࡱࡨࠬጫ"): bstack1ll_opy_ (u"ࠨࡖࡈࡗ࡙ࡥࡌࡐࡉࠪጬ"),
                bstack1ll_opy_ (u"ࠩ࡯ࡩࡻ࡫࡬ࠨጭ"): log[bstack1ll_opy_ (u"ࠪࡰࡪࡼࡥ࡭ࠩጮ")],
                bstack1ll_opy_ (u"ࠫࡹ࡯࡭ࡦࡵࡷࡥࡲࡶࠧጯ"): log[bstack1ll_opy_ (u"ࠬࡺࡩ࡮ࡧࡶࡸࡦࡳࡰࠨጰ")],
                bstack1ll_opy_ (u"࠭ࡨࡵࡶࡳࡣࡷ࡫ࡳࡱࡱࡱࡷࡪ࠭ጱ"): {},
                bstack1ll_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨጲ"): log[bstack1ll_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩጳ")],
            }
            if bstack1ll_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩጴ") in log:
                bstack111ll1lll1_opy_[bstack1ll_opy_ (u"ࠪࡸࡪࡹࡴࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪጵ")] = log[bstack1ll_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫጶ")]
            elif bstack1ll_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠬጷ") in log:
                bstack111ll1lll1_opy_[bstack1ll_opy_ (u"࠭ࡨࡰࡱ࡮ࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭ጸ")] = log[bstack1ll_opy_ (u"ࠧࡩࡱࡲ࡯ࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧጹ")]
            bstack111llll1l1_opy_.append(bstack111ll1lll1_opy_)
        cls.bstack111ll1l1ll_opy_({
            bstack1ll_opy_ (u"ࠨࡧࡹࡩࡳࡺ࡟ࡵࡻࡳࡩࠬጺ"): bstack1ll_opy_ (u"ࠩࡏࡳ࡬ࡉࡲࡦࡣࡷࡩࡩ࠭ጻ"),
            bstack1ll_opy_ (u"ࠪࡰࡴ࡭ࡳࠨጼ"): bstack111llll1l1_opy_
        })
    @classmethod
    @bstack1l1lll1111_opy_(class_method=True)
    def bstack111lll1ll1_opy_(cls, steps):
        bstack11l111111l_opy_ = []
        for step in steps:
            bstack111lll11l1_opy_ = {
                bstack1ll_opy_ (u"ࠫࡰ࡯࡮ࡥࠩጽ"): bstack1ll_opy_ (u"࡚ࠬࡅࡔࡖࡢࡗ࡙ࡋࡐࠨጾ"),
                bstack1ll_opy_ (u"࠭࡬ࡦࡸࡨࡰࠬጿ"): step[bstack1ll_opy_ (u"ࠧ࡭ࡧࡹࡩࡱ࠭ፀ")],
                bstack1ll_opy_ (u"ࠨࡶ࡬ࡱࡪࡹࡴࡢ࡯ࡳࠫፁ"): step[bstack1ll_opy_ (u"ࠩࡷ࡭ࡲ࡫ࡳࡵࡣࡰࡴࠬፂ")],
                bstack1ll_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫፃ"): step[bstack1ll_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬፄ")],
                bstack1ll_opy_ (u"ࠬࡪࡵࡳࡣࡷ࡭ࡴࡴࠧፅ"): step[bstack1ll_opy_ (u"࠭ࡤࡶࡴࡤࡸ࡮ࡵ࡮ࠨፆ")]
            }
            if bstack1ll_opy_ (u"ࠧࡵࡧࡶࡸࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧፇ") in step:
                bstack111lll11l1_opy_[bstack1ll_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨፈ")] = step[bstack1ll_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩፉ")]
            elif bstack1ll_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪፊ") in step:
                bstack111lll11l1_opy_[bstack1ll_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫፋ")] = step[bstack1ll_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠬፌ")]
            bstack11l111111l_opy_.append(bstack111lll11l1_opy_)
        cls.bstack111ll1l1ll_opy_({
            bstack1ll_opy_ (u"࠭ࡥࡷࡧࡱࡸࡤࡺࡹࡱࡧࠪፍ"): bstack1ll_opy_ (u"ࠧࡍࡱࡪࡇࡷ࡫ࡡࡵࡧࡧࠫፎ"),
            bstack1ll_opy_ (u"ࠨ࡮ࡲ࡫ࡸ࠭ፏ"): bstack11l111111l_opy_
        })
    @classmethod
    @bstack1l1lll1111_opy_(class_method=True)
    def bstack11l11111ll_opy_(cls, screenshot):
        cls.bstack111ll1l1ll_opy_({
            bstack1ll_opy_ (u"ࠩࡨࡺࡪࡴࡴࡠࡶࡼࡴࡪ࠭ፐ"): bstack1ll_opy_ (u"ࠪࡐࡴ࡭ࡃࡳࡧࡤࡸࡪࡪࠧፑ"),
            bstack1ll_opy_ (u"ࠫࡱࡵࡧࡴࠩፒ"): [{
                bstack1ll_opy_ (u"ࠬࡱࡩ࡯ࡦࠪፓ"): bstack1ll_opy_ (u"࠭ࡔࡆࡕࡗࡣࡘࡉࡒࡆࡇࡑࡗࡍࡕࡔࠨፔ"),
                bstack1ll_opy_ (u"ࠧࡵ࡫ࡰࡩࡸࡺࡡ࡮ࡲࠪፕ"): datetime.datetime.utcnow().isoformat() + bstack1ll_opy_ (u"ࠨ࡜ࠪፖ"),
                bstack1ll_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪፗ"): screenshot[bstack1ll_opy_ (u"ࠪ࡭ࡲࡧࡧࡦࠩፘ")],
                bstack1ll_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫፙ"): screenshot[bstack1ll_opy_ (u"ࠬࡺࡥࡴࡶࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠬፚ")]
            }]
        }, bstack111lllllll_opy_=bstack1ll_opy_ (u"࠭ࡡࡱ࡫࠲ࡺ࠶࠵ࡳࡤࡴࡨࡩࡳࡹࡨࡰࡶࡶࠫ፛"))
    @classmethod
    @bstack1l1lll1111_opy_(class_method=True)
    def bstack1l11ll111_opy_(cls, driver):
        current_test_uuid = cls.current_test_uuid()
        if not current_test_uuid:
            return
        cls.bstack111ll1l1ll_opy_({
            bstack1ll_opy_ (u"ࠧࡦࡸࡨࡲࡹࡥࡴࡺࡲࡨࠫ፜"): bstack1ll_opy_ (u"ࠨࡅࡅࡘࡘ࡫ࡳࡴ࡫ࡲࡲࡈࡸࡥࡢࡶࡨࡨࠬ፝"),
            bstack1ll_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࠫ፞"): {
                bstack1ll_opy_ (u"ࠥࡹࡺ࡯ࡤࠣ፟"): cls.current_test_uuid(),
                bstack1ll_opy_ (u"ࠦ࡮ࡴࡴࡦࡩࡵࡥࡹ࡯࡯࡯ࡵࠥ፠"): cls.bstack111llllll1_opy_(driver)
            }
        })
    @classmethod
    def on(cls):
        if os.environ.get(bstack1ll_opy_ (u"ࠬࡈࡓࡠࡖࡈࡗ࡙ࡕࡐࡔࡡࡍ࡛࡙࠭፡"), None) is None or os.environ[bstack1ll_opy_ (u"࠭ࡂࡔࡡࡗࡉࡘ࡚ࡏࡑࡕࡢࡎ࡜࡚ࠧ።")] == bstack1ll_opy_ (u"ࠢ࡯ࡷ࡯ࡰࠧ፣"):
            return False
        return True
    @classmethod
    def bstack11l1111lll_opy_(cls):
        return bstack1l11ll1111_opy_(cls.bs_config.get(bstack1ll_opy_ (u"ࠨࡶࡨࡷࡹࡕࡢࡴࡧࡵࡺࡦࡨࡩ࡭࡫ࡷࡽࠬ፤"), False))
    @staticmethod
    def request_url(url):
        return bstack1ll_opy_ (u"ࠩࡾࢁ࠴ࢁࡽࠨ፥").format(bstack111lll11ll_opy_, url)
    @staticmethod
    def default_headers():
        headers = {
            bstack1ll_opy_ (u"ࠪࡇࡴࡴࡴࡦࡰࡷ࠱࡙ࡿࡰࡦࠩ፦"): bstack1ll_opy_ (u"ࠫࡦࡶࡰ࡭࡫ࡦࡥࡹ࡯࡯࡯࠱࡭ࡷࡴࡴࠧ፧"),
            bstack1ll_opy_ (u"ࠬ࡞࠭ࡃࡕࡗࡅࡈࡑ࠭ࡕࡇࡖࡘࡔࡖࡓࠨ፨"): bstack1ll_opy_ (u"࠭ࡴࡳࡷࡨࠫ፩")
        }
        if os.environ.get(bstack1ll_opy_ (u"ࠧࡃࡕࡢࡘࡊ࡙ࡔࡐࡒࡖࡣࡏ࡝ࡔࠨ፪"), None):
            headers[bstack1ll_opy_ (u"ࠨࡃࡸࡸ࡭ࡵࡲࡪࡼࡤࡸ࡮ࡵ࡮ࠨ፫")] = bstack1ll_opy_ (u"ࠩࡅࡩࡦࡸࡥࡳࠢࡾࢁࠬ፬").format(os.environ[bstack1ll_opy_ (u"ࠥࡆࡘࡥࡔࡆࡕࡗࡓࡕ࡙࡟ࡋ࡙ࡗࠦ፭")])
        return headers
    @staticmethod
    def current_test_uuid():
        return getattr(threading.current_thread(), bstack1ll_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤࡺࡥࡴࡶࡢࡹࡺ࡯ࡤࠨ፮"), None)
    @staticmethod
    def bstack111llllll1_opy_(driver):
        return {
            bstack1l11l1l111_opy_(): bstack1l11l11l1l_opy_(driver)
        }
    @staticmethod
    def bstack111ll1llll_opy_(exception_info, report):
        return [{bstack1ll_opy_ (u"ࠬࡨࡡࡤ࡭ࡷࡶࡦࡩࡥࠨ፯"): [exception_info.exconly(), report.longreprtext]}]
    @staticmethod
    def bstack1l11l111l1_opy_(typename):
        if bstack1ll_opy_ (u"ࠨࡁࡴࡵࡨࡶࡹ࡯࡯࡯ࠤ፰") in typename:
            return bstack1ll_opy_ (u"ࠢࡂࡵࡶࡩࡷࡺࡩࡰࡰࡈࡶࡷࡵࡲࠣ፱")
        return bstack1ll_opy_ (u"ࠣࡗࡱ࡬ࡦࡴࡤ࡭ࡧࡧࡉࡷࡸ࡯ࡳࠤ፲")
    @staticmethod
    def bstack11l1111111_opy_(func):
        def wrap(*args, **kwargs):
            if bstack11l1l1l1_opy_.on():
                return func(*args, **kwargs)
            return
        return wrap
    @staticmethod
    def bstack111lllll1l_opy_(test, hook_name=None):
        bstack111ll1ll11_opy_ = test.parent
        if hook_name in [bstack1ll_opy_ (u"ࠩࡶࡩࡹࡻࡰࡠࡥ࡯ࡥࡸࡹࠧ፳"), bstack1ll_opy_ (u"ࠪࡸࡪࡧࡲࡥࡱࡺࡲࡤࡩ࡬ࡢࡵࡶࠫ፴"), bstack1ll_opy_ (u"ࠫࡸ࡫ࡴࡶࡲࡢࡱࡴࡪࡵ࡭ࡧࠪ፵"), bstack1ll_opy_ (u"ࠬࡺࡥࡢࡴࡧࡳࡼࡴ࡟࡮ࡱࡧࡹࡱ࡫ࠧ፶")]:
            bstack111ll1ll11_opy_ = test
        scope = []
        while bstack111ll1ll11_opy_ is not None:
            scope.append(bstack111ll1ll11_opy_.name)
            bstack111ll1ll11_opy_ = bstack111ll1ll11_opy_.parent
        scope.reverse()
        return scope[2:]
    @staticmethod
    def bstack11l1111ll1_opy_(hook_type):
        if hook_type == bstack1ll_opy_ (u"ࠨࡂࡆࡈࡒࡖࡊࡥࡅࡂࡅࡋࠦ፷"):
            return bstack1ll_opy_ (u"ࠢࡔࡧࡷࡹࡵࠦࡨࡰࡱ࡮ࠦ፸")
        elif hook_type == bstack1ll_opy_ (u"ࠣࡃࡉࡘࡊࡘ࡟ࡆࡃࡆࡌࠧ፹"):
            return bstack1ll_opy_ (u"ࠤࡗࡩࡦࡸࡤࡰࡹࡱࠤ࡭ࡵ࡯࡬ࠤ፺")
    @staticmethod
    def bstack111lll1l11_opy_(bstack1lll111ll1_opy_):
        try:
            if not bstack11l1l1l1_opy_.on():
                return bstack1lll111ll1_opy_
            if os.environ.get(bstack1ll_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡕࡉࡗ࡛ࡎࠣ፻"), None) == bstack1ll_opy_ (u"ࠦࡹࡸࡵࡦࠤ፼"):
                tests = os.environ.get(bstack1ll_opy_ (u"ࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡗࡋࡒࡖࡐࡢࡘࡊ࡙ࡔࡔࠤ፽"), None)
                if tests is None or tests == bstack1ll_opy_ (u"ࠨ࡮ࡶ࡮࡯ࠦ፾"):
                    return bstack1lll111ll1_opy_
                bstack1lll111ll1_opy_ = tests.split(bstack1ll_opy_ (u"ࠧ࠭ࠩ፿"))
                return bstack1lll111ll1_opy_
        except Exception as exc:
            print(bstack1ll_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡳࡧࡵࡹࡳࠦࡨࡢࡰࡧࡰࡪࡸ࠺ࠡࠤᎀ"), str(exc))
        return bstack1lll111ll1_opy_
    @classmethod
    def bstack111lll111l_opy_(cls, event: str, bstack111lll1l1l_opy_: bstack11l11ll1ll_opy_):
        bstack111llll11l_opy_ = {
            bstack1ll_opy_ (u"ࠩࡨࡺࡪࡴࡴࡠࡶࡼࡴࡪ࠭ᎁ"): event,
            bstack111lll1l1l_opy_.bstack11l111l1l1_opy_(): bstack111lll1l1l_opy_.bstack11l11l1111_opy_(event)
        }
        bstack11l1l1l1_opy_.bstack111ll1l1ll_opy_(bstack111llll11l_opy_)