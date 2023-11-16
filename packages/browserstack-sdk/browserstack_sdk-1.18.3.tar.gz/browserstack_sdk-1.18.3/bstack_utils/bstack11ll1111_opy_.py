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
import os
import json
import requests
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import logging
from urllib.parse import urlparse
from datetime import datetime
from bstack_utils.constants import bstack1l1ll1ll1l_opy_ as bstack1l1llll111_opy_
from bstack_utils.helper import bstack1111ll111_opy_, bstack1ll1111ll_opy_, bstack1l1lllll1l_opy_, bstack1l1llll1ll_opy_, bstack1ll111111_opy_, get_host_info, bstack1l1ll1ll11_opy_, bstack11111l11l_opy_, bstack1l1lll11l1_opy_
from browserstack_sdk._version import __version__
logger = logging.getLogger(__name__)
@bstack1l1lll11l1_opy_(class_method=False)
def _1l1ll1l11l_opy_(driver):
  response = {}
  try:
    caps = driver.capabilities
    response = {
        bstack111ll1l_opy_ (u"ࠬࡵࡳࡠࡰࡤࡱࡪ࠭ವ"): caps.get(bstack111ll1l_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡏࡣࡰࡩࠬಶ"), None),
        bstack111ll1l_opy_ (u"ࠧࡰࡵࡢࡺࡪࡸࡳࡪࡱࡱࠫಷ"): caps.get(bstack111ll1l_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯࡙ࡩࡷࡹࡩࡰࡰࠪಸ"), None),
        bstack111ll1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡢࡲࡦࡳࡥࠨಹ"): caps.get(bstack111ll1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡒࡦࡳࡥࠨ಺"), None),
        bstack111ll1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡤࡼࡥࡳࡵ࡬ࡳࡳ࠭಻"): caps.get(bstack111ll1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳ಼࠭"), None)
    }
  except Exception as error:
    logger.debug(bstack111ll1l_opy_ (u"࠭ࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥ࡬ࡥࡵࡥ࡫࡭ࡳ࡭ࠠࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࠢࡧࡩࡹࡧࡩ࡭ࡵࠣࡻ࡮ࡺࡨࠡࡧࡵࡶࡴࡸࠠ࠻ࠢࠪಽ") + str(error))
  return response
def bstack1l1ll1ll1_opy_(config):
  return config.get(bstack111ll1l_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧಾ"), False) or any([p.get(bstack111ll1l_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨಿ"), False) == True for p in config[bstack111ll1l_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬೀ")]])
def bstack1lll1l11_opy_(config, bstack1lll1l11l_opy_):
  try:
    if not bstack1ll1111ll_opy_(config):
      return False
    bstack1l1ll1l111_opy_ = config.get(bstack111ll1l_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪು"), False)
    bstack1ll1111111_opy_ = config[bstack111ll1l_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧೂ")][bstack1lll1l11l_opy_].get(bstack111ll1l_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬೃ"), None)
    if bstack1ll1111111_opy_ != None:
      bstack1l1ll1l111_opy_ = bstack1ll1111111_opy_
    bstack1l1llll1l1_opy_ = os.getenv(bstack111ll1l_opy_ (u"࠭ࡂࡔࡡࡄ࠵࠶࡟࡟ࡋ࡙ࡗࠫೄ")) is not None and len(os.getenv(bstack111ll1l_opy_ (u"ࠧࡃࡕࡢࡅ࠶࠷࡙ࡠࡌ࡚ࡘࠬ೅"))) > 0 and os.getenv(bstack111ll1l_opy_ (u"ࠨࡄࡖࡣࡆ࠷࠱࡚ࡡࡍ࡛࡙࠭ೆ")) != bstack111ll1l_opy_ (u"ࠩࡱࡹࡱࡲࠧೇ")
    return bstack1l1ll1l111_opy_ and bstack1l1llll1l1_opy_
  except Exception as error:
    logger.debug(bstack111ll1l_opy_ (u"ࠪࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡹࡩࡷ࡯ࡦࡺ࡫ࡱ࡫ࠥࡺࡨࡦࠢࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡶࡩࡸࡹࡩࡰࡰࠣࡻ࡮ࡺࡨࠡࡧࡵࡶࡴࡸࠠ࠻ࠢࠪೈ") + str(error))
  return False
def bstack1l1lll1ll1_opy_(bstack1l1lllllll_opy_, test_tags):
  bstack1l1lllllll_opy_ = os.getenv(bstack111ll1l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡠࡃࡆࡇࡊ࡙ࡓࡊࡄࡌࡐࡎ࡚࡙ࡠࡅࡒࡒࡋࡏࡇࡖࡔࡄࡘࡎࡕࡎࡠ࡛ࡐࡐࠬ೉"))
  if bstack1l1lllllll_opy_ is None:
    return True
  bstack1l1lllllll_opy_ = json.loads(bstack1l1lllllll_opy_)
  try:
    include_tags = bstack1l1lllllll_opy_[bstack111ll1l_opy_ (u"ࠬ࡯࡮ࡤ࡮ࡸࡨࡪ࡚ࡡࡨࡵࡌࡲ࡙࡫ࡳࡵ࡫ࡱ࡫ࡘࡩ࡯ࡱࡧࠪೊ")] if bstack111ll1l_opy_ (u"࠭ࡩ࡯ࡥ࡯ࡹࡩ࡫ࡔࡢࡩࡶࡍࡳ࡚ࡥࡴࡶ࡬ࡲ࡬࡙ࡣࡰࡲࡨࠫೋ") in bstack1l1lllllll_opy_ and isinstance(bstack1l1lllllll_opy_[bstack111ll1l_opy_ (u"ࠧࡪࡰࡦࡰࡺࡪࡥࡕࡣࡪࡷࡎࡴࡔࡦࡵࡷ࡭ࡳ࡭ࡓࡤࡱࡳࡩࠬೌ")], list) else []
    exclude_tags = bstack1l1lllllll_opy_[bstack111ll1l_opy_ (u"ࠨࡧࡻࡧࡱࡻࡤࡦࡖࡤ࡫ࡸࡏ࡮ࡕࡧࡶࡸ࡮ࡴࡧࡔࡥࡲࡴࡪ್࠭")] if bstack111ll1l_opy_ (u"ࠩࡨࡼࡨࡲࡵࡥࡧࡗࡥ࡬ࡹࡉ࡯ࡖࡨࡷࡹ࡯࡮ࡨࡕࡦࡳࡵ࡫ࠧ೎") in bstack1l1lllllll_opy_ and isinstance(bstack1l1lllllll_opy_[bstack111ll1l_opy_ (u"ࠪࡩࡽࡩ࡬ࡶࡦࡨࡘࡦ࡭ࡳࡊࡰࡗࡩࡸࡺࡩ࡯ࡩࡖࡧࡴࡶࡥࠨ೏")], list) else []
    excluded = any(tag in exclude_tags for tag in test_tags)
    included = len(include_tags) == 0 or any(tag in include_tags for tag in test_tags)
    return not excluded and included
  except Exception as error:
    logger.debug(bstack111ll1l_opy_ (u"ࠦࡊࡸࡲࡰࡴࠣࡻ࡭࡯࡬ࡦࠢࡹࡥࡱ࡯ࡤࡢࡶ࡬ࡲ࡬ࠦࡴࡦࡵࡷࠤࡨࡧࡳࡦࠢࡩࡳࡷࠦࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡢࡦࡨࡲࡶࡪࠦࡳࡤࡣࡱࡲ࡮ࡴࡧ࠯ࠢࡈࡶࡷࡵࡲࠡ࠼ࠣࠦ೐") + str(error))
  return False
def bstack11111lll_opy_(config, bstack1l1lll1l1l_opy_, bstack1ll11111l1_opy_):
  bstack1ll11111ll_opy_ = bstack1l1lllll1l_opy_(config)
  bstack1l1llllll1_opy_ = bstack1l1llll1ll_opy_(config)
  if bstack1ll11111ll_opy_ is None or bstack1l1llllll1_opy_ is None:
    logger.error(bstack111ll1l_opy_ (u"ࠬࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡࡹ࡫࡭ࡱ࡫ࠠࡤࡴࡨࡥࡹ࡯࡮ࡨࠢࡷࡩࡸࡺࠠࡳࡷࡱࠤ࡫ࡵࡲࠡࡄࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࠠࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱ࠾ࠥࡓࡩࡴࡵ࡬ࡲ࡬ࠦࡡࡶࡶ࡫ࡩࡳࡺࡩࡤࡣࡷ࡭ࡴࡴࠠࡵࡱ࡮ࡩࡳ࠭೑"))
    return [None, None]
  try:
    settings = json.loads(os.getenv(bstack111ll1l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡢࡅࡈࡉࡅࡔࡕࡌࡆࡎࡒࡉࡕ࡛ࡢࡇࡔࡔࡆࡊࡉࡘࡖࡆ࡚ࡉࡐࡐࡢ࡝ࡒࡒࠧ೒"), bstack111ll1l_opy_ (u"ࠧࡼࡿࠪ೓")))
    data = {
        bstack111ll1l_opy_ (u"ࠨࡲࡵࡳ࡯࡫ࡣࡵࡐࡤࡱࡪ࠭೔"): config[bstack111ll1l_opy_ (u"ࠩࡳࡶࡴࡰࡥࡤࡶࡑࡥࡲ࡫ࠧೕ")],
        bstack111ll1l_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡐࡤࡱࡪ࠭ೖ"): config.get(bstack111ll1l_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧ೗"), os.path.basename(os.getcwd())),
        bstack111ll1l_opy_ (u"ࠬࡹࡴࡢࡴࡷࡘ࡮ࡳࡥࠨ೘"): bstack1111ll111_opy_(),
        bstack111ll1l_opy_ (u"࠭ࡤࡦࡵࡦࡶ࡮ࡶࡴࡪࡱࡱࠫ೙"): config.get(bstack111ll1l_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡊࡥࡴࡥࡵ࡭ࡵࡺࡩࡰࡰࠪ೚"), bstack111ll1l_opy_ (u"ࠨࠩ೛")),
        bstack111ll1l_opy_ (u"ࠩࡶࡳࡺࡸࡣࡦࠩ೜"): {
            bstack111ll1l_opy_ (u"ࠪࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡔࡡ࡮ࡧࠪೝ"): bstack1l1lll1l1l_opy_,
            bstack111ll1l_opy_ (u"ࠫ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱࡖࡦࡴࡶ࡭ࡴࡴࠧೞ"): bstack1ll11111l1_opy_,
            bstack111ll1l_opy_ (u"ࠬࡹࡤ࡬ࡘࡨࡶࡸ࡯࡯࡯ࠩ೟"): __version__
        },
        bstack111ll1l_opy_ (u"࠭ࡳࡦࡶࡷ࡭ࡳ࡭ࡳࠨೠ"): settings,
        bstack111ll1l_opy_ (u"ࠧࡷࡧࡵࡷ࡮ࡵ࡮ࡄࡱࡱࡸࡷࡵ࡬ࠨೡ"): bstack1l1ll1ll11_opy_(),
        bstack111ll1l_opy_ (u"ࠨࡥ࡬ࡍࡳ࡬࡯ࠨೢ"): bstack1ll111111_opy_(),
        bstack111ll1l_opy_ (u"ࠩ࡫ࡳࡸࡺࡉ࡯ࡨࡲࠫೣ"): get_host_info(),
        bstack111ll1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠬ೤"): bstack1ll1111ll_opy_(config)
    }
    headers = {
        bstack111ll1l_opy_ (u"ࠫࡈࡵ࡮ࡵࡧࡱࡸ࠲࡚ࡹࡱࡧࠪ೥"): bstack111ll1l_opy_ (u"ࠬࡧࡰࡱ࡮࡬ࡧࡦࡺࡩࡰࡰ࠲࡮ࡸࡵ࡮ࠨ೦"),
    }
    config = {
        bstack111ll1l_opy_ (u"࠭ࡡࡶࡶ࡫ࠫ೧"): (bstack1ll11111ll_opy_, bstack1l1llllll1_opy_),
        bstack111ll1l_opy_ (u"ࠧࡩࡧࡤࡨࡪࡸࡳࠨ೨"): headers
    }
    response = bstack11111l11l_opy_(bstack111ll1l_opy_ (u"ࠨࡒࡒࡗ࡙࠭೩"), bstack1l1llll111_opy_ + bstack111ll1l_opy_ (u"ࠩ࠲ࡸࡪࡹࡴࡠࡴࡸࡲࡸ࠭೪"), data, config)
    bstack1ll111111l_opy_ = response.json()
    if bstack1ll111111l_opy_[bstack111ll1l_opy_ (u"ࠪࡷࡺࡩࡣࡦࡵࡶࠫ೫")]:
      logger.info(bstack111ll1l_opy_ (u"ࠫࡸࡺࡡࡵࡷࡶࠤࡨࡵࡤࡦࠢࠪ೬") + str(response.status_code) + bstack111ll1l_opy_ (u"ࠬࡢ࡮ࠨ೭") + str(bstack1ll111111l_opy_))
      parsed = json.loads(os.getenv(bstack111ll1l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡢࡅࡈࡉࡅࡔࡕࡌࡆࡎࡒࡉࡕ࡛ࡢࡇࡔࡔࡆࡊࡉࡘࡖࡆ࡚ࡉࡐࡐࡢ࡝ࡒࡒࠧ೮"), bstack111ll1l_opy_ (u"ࠧࡼࡿࠪ೯")))
      parsed[bstack111ll1l_opy_ (u"ࠨࡵࡦࡥࡳࡴࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩ೰")] = bstack1ll111111l_opy_[bstack111ll1l_opy_ (u"ࠩࡧࡥࡹࡧࠧೱ")][bstack111ll1l_opy_ (u"ࠪࡷࡨࡧ࡮࡯ࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠫೲ")]
      os.environ[bstack111ll1l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡠࡃࡆࡇࡊ࡙ࡓࡊࡄࡌࡐࡎ࡚࡙ࡠࡅࡒࡒࡋࡏࡇࡖࡔࡄࡘࡎࡕࡎࡠ࡛ࡐࡐࠬೳ")] = json.dumps(parsed)
      return bstack1ll111111l_opy_[bstack111ll1l_opy_ (u"ࠬࡪࡡࡵࡣࠪ೴")][bstack111ll1l_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࡚࡯࡬ࡧࡱࠫ೵")], bstack1ll111111l_opy_[bstack111ll1l_opy_ (u"ࠧࡥࡣࡷࡥࠬ೶")][bstack111ll1l_opy_ (u"ࠨ࡫ࡧࠫ೷")]
    else:
      logger.error(bstack111ll1l_opy_ (u"ࠩࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥࡽࡨࡪ࡮ࡨࠤࡷࡻ࡮࡯࡫ࡱ࡫ࠥࡈࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࠤࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮࠻ࠢࠪ೸") + bstack1ll111111l_opy_[bstack111ll1l_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫ೹")])
      if bstack1ll111111l_opy_[bstack111ll1l_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬ೺")] == bstack111ll1l_opy_ (u"ࠬࡏ࡮ࡷࡣ࡯࡭ࡩࠦࡣࡰࡰࡩ࡭࡬ࡻࡲࡢࡶ࡬ࡳࡳࠦࡰࡢࡵࡶࡩࡩ࠴ࠧ೻"):
        for bstack1l1lllll11_opy_ in bstack1ll111111l_opy_[bstack111ll1l_opy_ (u"࠭ࡥࡳࡴࡲࡶࡸ࠭೼")]:
          logger.error(bstack1l1lllll11_opy_[bstack111ll1l_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨ೽")])
      return None, None
  except Exception as error:
    logger.error(bstack111ll1l_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤࡼ࡮ࡩ࡭ࡧࠣࡧࡷ࡫ࡡࡵ࡫ࡱ࡫ࠥࡺࡥࡴࡶࠣࡶࡺࡴࠠࡧࡱࡵࠤࡇࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࠣࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴ࠺ࠡࠤ೾") +  str(error))
    return None, None
def bstack1lll1l1ll1_opy_():
  if os.getenv(bstack111ll1l_opy_ (u"ࠩࡅࡗࡤࡇ࠱࠲࡛ࡢࡎ࡜࡚ࠧ೿")) is None:
    return {
        bstack111ll1l_opy_ (u"ࠪࡷࡹࡧࡴࡶࡵࠪഀ"): bstack111ll1l_opy_ (u"ࠫࡪࡸࡲࡰࡴࠪഁ"),
        bstack111ll1l_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ࠭ം"): bstack111ll1l_opy_ (u"࠭ࡂࡶ࡫࡯ࡨࠥࡩࡲࡦࡣࡷ࡭ࡴࡴࠠࡩࡣࡧࠤ࡫ࡧࡩ࡭ࡧࡧ࠲ࠬഃ")
    }
  data = {bstack111ll1l_opy_ (u"ࠧࡦࡰࡧࡘ࡮ࡳࡥࠨഄ"): bstack1111ll111_opy_()}
  headers = {
      bstack111ll1l_opy_ (u"ࠨࡃࡸࡸ࡭ࡵࡲࡪࡼࡤࡸ࡮ࡵ࡮ࠨഅ"): bstack111ll1l_opy_ (u"ࠩࡅࡩࡦࡸࡥࡳࠢࠪആ") + os.getenv(bstack111ll1l_opy_ (u"ࠥࡆࡘࡥࡁ࠲࠳࡜ࡣࡏ࡝ࡔࠣഇ")),
      bstack111ll1l_opy_ (u"ࠫࡈࡵ࡮ࡵࡧࡱࡸ࠲࡚ࡹࡱࡧࠪഈ"): bstack111ll1l_opy_ (u"ࠬࡧࡰࡱ࡮࡬ࡧࡦࡺࡩࡰࡰ࠲࡮ࡸࡵ࡮ࠨഉ")
  }
  response = bstack11111l11l_opy_(bstack111ll1l_opy_ (u"࠭ࡐࡖࡖࠪഊ"), bstack1l1llll111_opy_ + bstack111ll1l_opy_ (u"ࠧ࠰ࡶࡨࡷࡹࡥࡲࡶࡰࡶ࠳ࡸࡺ࡯ࡱࠩഋ"), data, { bstack111ll1l_opy_ (u"ࠨࡪࡨࡥࡩ࡫ࡲࡴࠩഌ"): headers })
  try:
    if response.status_code == 200:
      logger.info(bstack111ll1l_opy_ (u"ࠤࡅࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࠡࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲ࡚ࠥࡥࡴࡶࠣࡖࡺࡴࠠ࡮ࡣࡵ࡯ࡪࡪࠠࡢࡵࠣࡧࡴࡳࡰ࡭ࡧࡷࡩࡩࠦࡡࡵࠢࠥ഍") + datetime.utcnow().isoformat() + bstack111ll1l_opy_ (u"ࠪ࡞ࠬഎ"))
      return {bstack111ll1l_opy_ (u"ࠫࡸࡺࡡࡵࡷࡶࠫഏ"): bstack111ll1l_opy_ (u"ࠬࡹࡵࡤࡥࡨࡷࡸ࠭ഐ"), bstack111ll1l_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧ഑"): bstack111ll1l_opy_ (u"ࠧࠨഒ")}
    else:
      response.raise_for_status()
  except requests.RequestException as error:
    logger.error(bstack111ll1l_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤࡼ࡮ࡩ࡭ࡧࠣࡱࡦࡸ࡫ࡪࡰࡪࠤࡨࡵ࡭ࡱ࡮ࡨࡸ࡮ࡵ࡮ࠡࡱࡩࠤࡇࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࠣࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠠࡕࡧࡶࡸࠥࡘࡵ࡯࠼ࠣࠦഓ") + str(error))
    return {
        bstack111ll1l_opy_ (u"ࠩࡶࡸࡦࡺࡵࡴࠩഔ"): bstack111ll1l_opy_ (u"ࠪࡩࡷࡸ࡯ࡳࠩക"),
        bstack111ll1l_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬഖ"): str(error)
    }
def bstack1ll1ll1l_opy_(caps, options):
  try:
    bstack1l1lll1l11_opy_ = caps.get(bstack111ll1l_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯࠿ࡵࡰࡵ࡫ࡲࡲࡸ࠭ഗ"), {}).get(bstack111ll1l_opy_ (u"࠭ࡤࡦࡸ࡬ࡧࡪࡔࡡ࡮ࡧࠪഘ"), caps.get(bstack111ll1l_opy_ (u"ࠧࡥࡧࡹ࡭ࡨ࡫ࠧങ"), bstack111ll1l_opy_ (u"ࠨࠩച")))
    if bstack1l1lll1l11_opy_:
      logger.warn(bstack111ll1l_opy_ (u"ࠤࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࠦࡷࡪ࡮࡯ࠤࡷࡻ࡮ࠡࡱࡱࡰࡾࠦ࡯࡯ࠢࡇࡩࡸࡱࡴࡰࡲࠣࡦࡷࡵࡷࡴࡧࡵࡷ࠳ࠨഛ"))
      return False
    browser = caps.get(bstack111ll1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡒࡦࡳࡥࠨജ"), bstack111ll1l_opy_ (u"ࠫࠬഝ")).lower()
    if browser != bstack111ll1l_opy_ (u"ࠬࡩࡨࡳࡱࡰࡩࠬഞ"):
      logger.warn(bstack111ll1l_opy_ (u"ࠨࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰࠣࡻ࡮ࡲ࡬ࠡࡴࡸࡲࠥࡵ࡮࡭ࡻࠣࡳࡳࠦࡃࡩࡴࡲࡱࡪࠦࡢࡳࡱࡺࡷࡪࡸࡳ࠯ࠤട"))
      return False
    browser_version = caps.get(bstack111ll1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠨഠ"), caps.get(bstack111ll1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡡࡹࡩࡷࡹࡩࡰࡰࠪഡ")))
    if browser_version and browser_version != bstack111ll1l_opy_ (u"ࠩ࡯ࡥࡹ࡫ࡳࡵࠩഢ") and int(browser_version) <= 94:
      logger.warn(bstack111ll1l_opy_ (u"ࠥࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠠࡸ࡫࡯ࡰࠥࡸࡵ࡯ࠢࡲࡲࡱࡿࠠࡰࡰࠣࡇ࡭ࡸ࡯࡮ࡧࠣࡦࡷࡵࡷࡴࡧࡵࠤࡻ࡫ࡲࡴ࡫ࡲࡲࠥ࡭ࡲࡦࡣࡷࡩࡷࠦࡴࡩࡣࡱࠤ࠾࠺࠮ࠣണ"))
      return False
    if not options is None:
      bstack1l1ll11lll_opy_ = options.to_capabilities().get(bstack111ll1l_opy_ (u"ࠫ࡬ࡵ࡯ࡨ࠼ࡦ࡬ࡷࡵ࡭ࡦࡑࡳࡸ࡮ࡵ࡮ࡴࠩത"), {})
      if bstack111ll1l_opy_ (u"ࠬ࠳࠭ࡩࡧࡤࡨࡱ࡫ࡳࡴࠩഥ") in bstack1l1ll11lll_opy_.get(bstack111ll1l_opy_ (u"࠭ࡡࡳࡩࡶࠫദ"), []):
        logger.warn(bstack111ll1l_opy_ (u"ࠢࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠤࡼ࡯࡬࡭ࠢࡱࡳࡹࠦࡲࡶࡰࠣࡳࡳࠦ࡬ࡦࡩࡤࡧࡾࠦࡨࡦࡣࡧࡰࡪࡹࡳࠡ࡯ࡲࡨࡪ࠴ࠠࡔࡹ࡬ࡸࡨ࡮ࠠࡵࡱࠣࡲࡪࡽࠠࡩࡧࡤࡨࡱ࡫ࡳࡴࠢࡰࡳࡩ࡫ࠠࡰࡴࠣࡥࡻࡵࡩࡥࠢࡸࡷ࡮ࡴࡧࠡࡪࡨࡥࡩࡲࡥࡴࡵࠣࡱࡴࡪࡥ࠯ࠤധ"))
        return False
    return True
  except Exception as error:
    logger.debug(bstack111ll1l_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡷࡣ࡯࡭ࡩࡧࡴࡦࠢࡤ࠵࠶ࡿࠠࡴࡷࡳࡴࡴࡸࡴࠡ࠼ࠥന") + str(error))
    return False
def set_capabilities(caps, config):
  try:
    bstack1l1lll1111_opy_ = config.get(bstack111ll1l_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࡑࡳࡸ࡮ࡵ࡮ࡴࠩഩ"), {})
    bstack1l1lll1111_opy_[bstack111ll1l_opy_ (u"ࠪࡥࡺࡺࡨࡕࡱ࡮ࡩࡳ࠭പ")] = os.getenv(bstack111ll1l_opy_ (u"ࠫࡇ࡙࡟ࡂ࠳࠴࡝ࡤࡐࡗࡕࠩഫ"))
    bstack1l1lll1lll_opy_ = json.loads(os.getenv(bstack111ll1l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡡࡄࡇࡈࡋࡓࡔࡋࡅࡍࡑࡏࡔ࡚ࡡࡆࡓࡓࡌࡉࡈࡗࡕࡅ࡙ࡏࡏࡏࡡ࡜ࡑࡑ࠭ബ"), bstack111ll1l_opy_ (u"࠭ࡻࡾࠩഭ"))).get(bstack111ll1l_opy_ (u"ࠧࡴࡥࡤࡲࡳ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠨമ"))
    caps[bstack111ll1l_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨയ")] = True
    if bstack111ll1l_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬࠼ࡲࡴࡹ࡯࡯࡯ࡵࠪര") in caps:
      caps[bstack111ll1l_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭࠽ࡳࡵࡺࡩࡰࡰࡶࠫറ")][bstack111ll1l_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࡓࡵࡺࡩࡰࡰࡶࠫല")] = bstack1l1lll1111_opy_
      caps[bstack111ll1l_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯࠿ࡵࡰࡵ࡫ࡲࡲࡸ࠭ള")][bstack111ll1l_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࡕࡰࡵ࡫ࡲࡲࡸ࠭ഴ")][bstack111ll1l_opy_ (u"ࠧࡴࡥࡤࡲࡳ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠨവ")] = bstack1l1lll1lll_opy_
    else:
      caps[bstack111ll1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࡏࡱࡶ࡬ࡳࡳࡹࠧശ")] = bstack1l1lll1111_opy_
      caps[bstack111ll1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࡐࡲࡷ࡭ࡴࡴࡳࠨഷ")][bstack111ll1l_opy_ (u"ࠪࡷࡨࡧ࡮࡯ࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠫസ")] = bstack1l1lll1lll_opy_
  except Exception as error:
    logger.debug(bstack111ll1l_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡸࡪ࡬ࡰࡪࠦࡳࡦࡶࡷ࡭ࡳ࡭ࠠࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠤࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵ࠱ࠤࡊࡸࡲࡰࡴ࠽ࠤࠧഹ") +  str(error))
def bstack1l1lll11ll_opy_(driver, bstack1l1ll1lll1_opy_):
  try:
    session = driver.session_id
    if session:
      bstack1l1ll1l1l1_opy_ = True
      current_url = driver.current_url
      try:
        url = urlparse(current_url)
      except Exception as e:
        bstack1l1ll1l1l1_opy_ = False
      bstack1l1ll1l1l1_opy_ = url.scheme in [bstack111ll1l_opy_ (u"ࠧ࡮ࡴࡵࡲࠥഺ"), bstack111ll1l_opy_ (u"ࠨࡨࡵࡶࡳࡷ഻ࠧ")]
      if bstack1l1ll1l1l1_opy_:
        if bstack1l1ll1lll1_opy_:
          logger.info(bstack111ll1l_opy_ (u"ࠢࡔࡧࡷࡹࡵࠦࡦࡰࡴࠣࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡸࡪࡹࡴࡪࡰࡪࠤ࡭ࡧࡳࠡࡵࡷࡥࡷࡺࡥࡥ࠰ࠣࡅࡺࡺ࡯࡮ࡣࡷࡩࠥࡺࡥࡴࡶࠣࡧࡦࡹࡥࠡࡧࡻࡩࡨࡻࡴࡪࡱࡱࠤࡼ࡯࡬࡭ࠢࡥࡩ࡬࡯࡮ࠡ࡯ࡲࡱࡪࡴࡴࡢࡴ࡬ࡰࡾ࠴഼ࠢ"))
          driver.execute_async_script(bstack111ll1l_opy_ (u"ࠣࠤࠥࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡨࡵ࡮ࡴࡶࠣࡧࡦࡲ࡬ࡣࡣࡦ࡯ࠥࡃࠠࡢࡴࡪࡹࡲ࡫࡮ࡵࡵ࡞ࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸ࠴࡬ࡦࡰࡪࡸ࡭ࠦ࠭ࠡ࠳ࡠ࠿ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࡩ࡯࡯ࡵࡷࠤ࡫ࡴࠠ࠾ࠢࠫ࠭ࠥࡃ࠾ࠡࡽࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡸ࡫ࡱࡨࡴࡽ࠮ࡢࡦࡧࡉࡻ࡫࡮ࡵࡎ࡬ࡷࡹ࡫࡮ࡦࡴࠫࠫࡆ࠷࠱࡚ࡡࡗࡅࡕࡥࡓࡕࡃࡕࡘࡊࡊࠧ࠭ࠢࡩࡲ࠷࠯࠻ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࡩ࡯࡯ࡵࡷࠤࡪࠦ࠽ࠡࡰࡨࡻࠥࡉࡵࡴࡶࡲࡱࡊࡼࡥ࡯ࡶࠫࠫࡆ࠷࠱࡚ࡡࡉࡓࡗࡉࡅࡠࡕࡗࡅࡗ࡚ࠧࠪ࠽ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡸ࡫ࡱࡨࡴࡽ࠮ࡥ࡫ࡶࡴࡦࡺࡣࡩࡇࡹࡩࡳࡺࠨࡦࠫ࠾ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࢂࡁࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡤࡱࡱࡷࡹࠦࡦ࡯࠴ࠣࡁࠥ࠮ࠩࠡ࠿ࡁࠤࢀࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡻ࡮ࡴࡤࡰࡹ࠱ࡶࡪࡳ࡯ࡷࡧࡈࡺࡪࡴࡴࡍ࡫ࡶࡸࡪࡴࡥࡳࠪࠪࡅ࠶࠷࡙ࡠࡖࡄࡔࡤ࡙ࡔࡂࡔࡗࡉࡉ࠭ࠬࠡࡨࡱ࠭ࡀࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡧࡦࡲ࡬ࡣࡣࡦ࡯࠭࠯࠻ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡿࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡪࡳ࠮ࠩ࠼ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠨࠢࠣഽ"))
          logger.info(bstack111ll1l_opy_ (u"ࠤࡄࡹࡹࡵ࡭ࡢࡶࡨࠤࡹ࡫ࡳࡵࠢࡦࡥࡸ࡫ࠠࡦࡺࡨࡧࡺࡺࡩࡰࡰࠣ࡬ࡦࡹࠠࡴࡶࡤࡶࡹ࡫ࡤ࠯ࠤാ"))
        else:
          driver.execute_script(bstack111ll1l_opy_ (u"ࠥࠦࠧࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡣࡰࡰࡶࡸࠥ࡫ࠠ࠾ࠢࡱࡩࡼࠦࡃࡶࡵࡷࡳࡲࡋࡶࡦࡰࡷࠬࠬࡇ࠱࠲࡛ࡢࡊࡔࡘࡃࡆࡡࡖࡘࡔࡖࠧࠪ࠽ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡻ࡮ࡴࡤࡰࡹ࠱ࡨ࡮ࡹࡰࡢࡶࡦ࡬ࡊࡼࡥ࡯ࡶࠫࡩ࠮ࡁࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠦࠧࠨി"))
      return bstack1l1ll1lll1_opy_
  except Exception as e:
    logger.error(bstack111ll1l_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡷࡹࡧࡲࡵ࡫ࡱ࡫ࠥࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡧࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠢࡶࡧࡦࡴࠠࡧࡱࡵࠤࡹ࡮ࡩࡴࠢࡷࡩࡸࡺࠠࡤࡣࡶࡩ࠿ࠦࠢീ") + str(e))
    return False
def bstack1l1llll11l_opy_(driver, item):
  try:
    bstack1l1ll1l1ll_opy_ = [item.cls.__name__] if not item.cls is None else []
    bstack1l1lll111l_opy_ = {
        bstack111ll1l_opy_ (u"ࠧࡹࡡࡷࡧࡕࡩࡸࡻ࡬ࡵࡵࠥു"): True,
        bstack111ll1l_opy_ (u"ࠨࡴࡦࡵࡷࡈࡪࡺࡡࡪ࡮ࡶࠦൂ"): {
            bstack111ll1l_opy_ (u"ࠢ࡯ࡣࡰࡩࠧൃ"): item.name,
            bstack111ll1l_opy_ (u"ࠣࡶࡨࡷࡹࡘࡵ࡯ࡋࡧࠦൄ"): os.environ.get(bstack111ll1l_opy_ (u"ࠩࡅࡗࡤࡇ࠱࠲࡛ࡢࡘࡊ࡙ࡔࡠࡔࡘࡒࡤࡏࡄࠨ൅")),
            bstack111ll1l_opy_ (u"ࠥࡪ࡮ࡲࡥࡑࡣࡷ࡬ࠧെ"): str(item.path),
            bstack111ll1l_opy_ (u"ࠦࡸࡩ࡯ࡱࡧࡏ࡭ࡸࡺࠢേ"): [item.module.__name__, *bstack1l1ll1l1ll_opy_, item.name],
        },
        bstack111ll1l_opy_ (u"ࠧࡶ࡬ࡢࡶࡩࡳࡷࡳࠢൈ"): _1l1ll1l11l_opy_(driver)
    }
    driver.execute_async_script(bstack111ll1l_opy_ (u"ࠨࠢࠣࠌࠣࠤࠥࠦࠠࠡࠢࠣࡧࡴࡴࡳࡵࠢࡦࡥࡱࡲࡢࡢࡥ࡮ࠤࡂࠦࡡࡳࡩࡸࡱࡪࡴࡴࡴ࡝ࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷ࠳ࡲࡥ࡯ࡩࡷ࡬ࠥ࠳ࠠ࠲࡟࠾ࠎࠥࠦࠠࠡࠢࠣࠤࠥࡺࡨࡪࡵ࠱ࡶࡪࡹࠠ࠾ࠢࡱࡹࡱࡲ࠻ࠋࠢࠣࠤࠥࠦࠠࠡࠢ࡬ࡪࠥ࠮ࡡࡳࡩࡸࡱࡪࡴࡴࡴ࡝࠳ࡡ࠳ࡹࡡࡷࡧࡕࡩࡸࡻ࡬ࡵࡵࠬࠤࢀࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡼ࡯࡮ࡥࡱࡺ࠲ࡦࡪࡤࡆࡸࡨࡲࡹࡒࡩࡴࡶࡨࡲࡪࡸࠨࠨࡃ࠴࠵࡞ࡥࡔࡂࡒࡢࡘࡗࡇࡎࡔࡒࡒࡖ࡙ࡋࡒࠨ࠮ࠣࠬࡪࡼࡥ࡯ࡶࠬࠤࡂࡄࠠࡼࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡼ࡯࡮ࡥࡱࡺ࠲ࡹࡧࡰࡕࡴࡤࡲࡸࡶ࡯ࡳࡶࡨࡶࡉࡧࡴࡢࠢࡀࠤࡪࡼࡥ࡯ࡶ࠱ࡨࡪࡺࡡࡪ࡮࠾ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡴࡩ࡫ࡶ࠲ࡷ࡫ࡳࠡ࠿ࠣࡻ࡮ࡴࡤࡰࡹ࠱ࡸࡦࡶࡔࡳࡣࡱࡷࡵࡵࡲࡵࡧࡵࡈࡦࡺࡡ࠼ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡨࡧ࡬࡭ࡤࡤࡧࡰ࠮ࡴࡩ࡫ࡶ࠲ࡷ࡫ࡳࠪ࠽ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡿࠬ࠿ࠏࠦࠠࠡࠢࠣࠤࠥࠦࡽࠋࠢࠣࠤࠥࠦࠠࠡࠢࡦࡳࡳࡹࡴࠡࡧࠣࡁࠥࡴࡥࡸࠢࡆࡹࡸࡺ࡯࡮ࡇࡹࡩࡳࡺࠨࠨࡃ࠴࠵࡞ࡥࡔࡆࡕࡗࡣࡊࡔࡄࠨ࠮ࠣࡿࠥࡪࡥࡵࡣ࡬ࡰ࠿ࠦࡡࡳࡩࡸࡱࡪࡴࡴࡴ࡝࠳ࡡࠥࢃࠩ࠼ࠌࠣࠤࠥࠦࠠࠡࠢࠣࡻ࡮ࡴࡤࡰࡹ࠱ࡨ࡮ࡹࡰࡢࡶࡦ࡬ࡊࡼࡥ࡯ࡶࠫࡩ࠮ࡁࠊࠡࠢࠣࠤࠥࠦࠠࠡ࡫ࡩࠤ࠭ࠧࡡࡳࡩࡸࡱࡪࡴࡴࡴ࡝࠳ࡡ࠳ࡹࡡࡷࡧࡕࡩࡸࡻ࡬ࡵࡵࠬࠤࢀࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡨࡧ࡬࡭ࡤࡤࡧࡰ࠮ࠩ࠼ࠌࠣࠤࠥࠦࠠࠡࠢࠣࢁࠏࠦࠠࠡࠢࠥࠦࠧ൉"), bstack1l1lll111l_opy_)
    logger.info(bstack111ll1l_opy_ (u"ࠢࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡵࡧࡶࡸ࡮ࡴࡧࠡࡨࡲࡶࠥࡺࡨࡪࡵࠣࡸࡪࡹࡴࠡࡥࡤࡷࡪࠦࡨࡢࡵࠣࡩࡳࡪࡥࡥ࠰ࠥൊ"))
  except Exception as bstack1l1ll1llll_opy_:
    logger.error(bstack111ll1l_opy_ (u"ࠣࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡴࡨࡷࡺࡲࡴࡴࠢࡦࡳࡺࡲࡤࠡࡰࡲࡸࠥࡨࡥࠡࡲࡵࡳࡨ࡫ࡳࡴࡧࡧࠤ࡫ࡵࡲࠡࡶ࡫ࡩࠥࡺࡥࡴࡶࠣࡧࡦࡹࡥ࠻ࠢࠥോ") + item.path + bstack111ll1l_opy_ (u"ࠤࠣࡉࡷࡸ࡯ࡳࠢ࠽ࠦൌ") + str(bstack1l1ll1llll_opy_))