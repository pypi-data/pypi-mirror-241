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
import os
import json
import requests
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import logging
from urllib.parse import urlparse
from datetime import datetime
from bstack_utils.constants import bstack1l1lll11l1_opy_ as bstack1l1ll11111_opy_
from bstack_utils.helper import bstack1lllll1ll1_opy_, bstack1l111lll1_opy_, bstack1l1ll11ll1_opy_, bstack1l1l1llll1_opy_, bstack11l111ll_opy_, get_host_info, bstack1l1ll111ll_opy_, bstack1llll1l11l_opy_, bstack1l1lll1111_opy_
from browserstack_sdk._version import __version__
logger = logging.getLogger(__name__)
@bstack1l1lll1111_opy_(class_method=False)
def _1l1ll1l11l_opy_(driver):
  response = {}
  try:
    caps = driver.capabilities
    response = {
        bstack1ll_opy_ (u"ࠨࡱࡶࡣࡳࡧ࡭ࡦࠩೆ"): caps.get(bstack1ll_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡒࡦࡳࡥࠨೇ"), None),
        bstack1ll_opy_ (u"ࠪࡳࡸࡥࡶࡦࡴࡶ࡭ࡴࡴࠧೈ"): caps.get(bstack1ll_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲ࡜ࡥࡳࡵ࡬ࡳࡳ࠭೉"), None),
        bstack1ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡥ࡮ࡢ࡯ࡨࠫೊ"): caps.get(bstack1ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡎࡢ࡯ࡨࠫೋ"), None),
        bstack1ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡠࡸࡨࡶࡸ࡯࡯࡯ࠩೌ"): caps.get(bstack1ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡘࡨࡶࡸ࡯࡯࡯್ࠩ"), None)
    }
  except Exception as error:
    logger.debug(bstack1ll_opy_ (u"ࠩࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡨࡨࡸࡨ࡮ࡩ࡯ࡩࠣࡴࡱࡧࡴࡧࡱࡵࡱࠥࡪࡥࡵࡣ࡬ࡰࡸࠦࡷࡪࡶ࡫ࠤࡪࡸࡲࡰࡴࠣ࠾ࠥ࠭೎") + str(error))
  return response
def bstack1l1lll1l1_opy_(config):
  return config.get(bstack1ll_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪ೏"), False) or any([p.get(bstack1ll_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫ೐"), False) == True for p in config[bstack1ll_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ೑")]])
def bstack11l11lll1_opy_(config, bstack1l1l1l1l_opy_):
  try:
    if not bstack1l111lll1_opy_(config):
      return False
    bstack1l1l1ll1l1_opy_ = config.get(bstack1ll_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭೒"), False)
    bstack1l1l1l1lll_opy_ = config[bstack1ll_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪ೓")][bstack1l1l1l1l_opy_].get(bstack1ll_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨ೔"), None)
    if bstack1l1l1l1lll_opy_ != None:
      bstack1l1l1ll1l1_opy_ = bstack1l1l1l1lll_opy_
    bstack1l1l1lllll_opy_ = os.getenv(bstack1ll_opy_ (u"ࠩࡅࡗࡤࡇ࠱࠲࡛ࡢࡎ࡜࡚ࠧೕ")) is not None and len(os.getenv(bstack1ll_opy_ (u"ࠪࡆࡘࡥࡁ࠲࠳࡜ࡣࡏ࡝ࡔࠨೖ"))) > 0 and os.getenv(bstack1ll_opy_ (u"ࠫࡇ࡙࡟ࡂ࠳࠴࡝ࡤࡐࡗࡕࠩ೗")) != bstack1ll_opy_ (u"ࠬࡴࡵ࡭࡮ࠪ೘")
    return bstack1l1l1ll1l1_opy_ and bstack1l1l1lllll_opy_
  except Exception as error:
    logger.debug(bstack1ll_opy_ (u"࠭ࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡼࡥࡳ࡫ࡩࡽ࡮ࡴࡧࠡࡶ࡫ࡩࠥࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡹࡥࡴࡵ࡬ࡳࡳࠦࡷࡪࡶ࡫ࠤࡪࡸࡲࡰࡴࠣ࠾ࠥ࠭೙") + str(error))
  return False
def bstack1l1lll111l_opy_(bstack1l1ll11lll_opy_, test_tags):
  bstack1l1ll11lll_opy_ = os.getenv(bstack1ll_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡣࡆࡉࡃࡆࡕࡖࡍࡇࡏࡌࡊࡖ࡜ࡣࡈࡕࡎࡇࡋࡊ࡙ࡗࡇࡔࡊࡑࡑࡣ࡞ࡓࡌࠨ೚"))
  if bstack1l1ll11lll_opy_ is None:
    return True
  bstack1l1ll11lll_opy_ = json.loads(bstack1l1ll11lll_opy_)
  try:
    include_tags = bstack1l1ll11lll_opy_[bstack1ll_opy_ (u"ࠨ࡫ࡱࡧࡱࡻࡤࡦࡖࡤ࡫ࡸࡏ࡮ࡕࡧࡶࡸ࡮ࡴࡧࡔࡥࡲࡴࡪ࠭೛")] if bstack1ll_opy_ (u"ࠩ࡬ࡲࡨࡲࡵࡥࡧࡗࡥ࡬ࡹࡉ࡯ࡖࡨࡷࡹ࡯࡮ࡨࡕࡦࡳࡵ࡫ࠧ೜") in bstack1l1ll11lll_opy_ and isinstance(bstack1l1ll11lll_opy_[bstack1ll_opy_ (u"ࠪ࡭ࡳࡩ࡬ࡶࡦࡨࡘࡦ࡭ࡳࡊࡰࡗࡩࡸࡺࡩ࡯ࡩࡖࡧࡴࡶࡥࠨೝ")], list) else []
    exclude_tags = bstack1l1ll11lll_opy_[bstack1ll_opy_ (u"ࠫࡪࡾࡣ࡭ࡷࡧࡩ࡙ࡧࡧࡴࡋࡱࡘࡪࡹࡴࡪࡰࡪࡗࡨࡵࡰࡦࠩೞ")] if bstack1ll_opy_ (u"ࠬ࡫ࡸࡤ࡮ࡸࡨࡪ࡚ࡡࡨࡵࡌࡲ࡙࡫ࡳࡵ࡫ࡱ࡫ࡘࡩ࡯ࡱࡧࠪ೟") in bstack1l1ll11lll_opy_ and isinstance(bstack1l1ll11lll_opy_[bstack1ll_opy_ (u"࠭ࡥࡹࡥ࡯ࡹࡩ࡫ࡔࡢࡩࡶࡍࡳ࡚ࡥࡴࡶ࡬ࡲ࡬࡙ࡣࡰࡲࡨࠫೠ")], list) else []
    excluded = any(tag in exclude_tags for tag in test_tags)
    included = len(include_tags) == 0 or any(tag in include_tags for tag in test_tags)
    return not excluded and included
  except Exception as error:
    logger.debug(bstack1ll_opy_ (u"ࠢࡆࡴࡵࡳࡷࠦࡷࡩ࡫࡯ࡩࠥࡼࡡ࡭࡫ࡧࡥࡹ࡯࡮ࡨࠢࡷࡩࡸࡺࠠࡤࡣࡶࡩࠥ࡬࡯ࡳࠢࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡥࡩ࡫ࡵࡲࡦࠢࡶࡧࡦࡴ࡮ࡪࡰࡪ࠲ࠥࡋࡲࡳࡱࡵࠤ࠿ࠦࠢೡ") + str(error))
  return False
def bstack1l1l1llll_opy_(config, bstack1l1ll1111l_opy_, bstack1l1ll1l1l1_opy_):
  bstack1l1l1lll1l_opy_ = bstack1l1ll11ll1_opy_(config)
  bstack1l1l1ll111_opy_ = bstack1l1l1llll1_opy_(config)
  if bstack1l1l1lll1l_opy_ is None or bstack1l1l1ll111_opy_ is None:
    logger.error(bstack1ll_opy_ (u"ࠨࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤࡼ࡮ࡩ࡭ࡧࠣࡧࡷ࡫ࡡࡵ࡫ࡱ࡫ࠥࡺࡥࡴࡶࠣࡶࡺࡴࠠࡧࡱࡵࠤࡇࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࠣࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴ࠺ࠡࡏ࡬ࡷࡸ࡯࡮ࡨࠢࡤࡹࡹ࡮ࡥ࡯ࡶ࡬ࡧࡦࡺࡩࡰࡰࠣࡸࡴࡱࡥ࡯ࠩೢ"))
    return [None, None]
  try:
    settings = json.loads(os.getenv(bstack1ll_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡥࡁࡄࡅࡈࡗࡘࡏࡂࡊࡎࡌࡘ࡞ࡥࡃࡐࡐࡉࡍࡌ࡛ࡒࡂࡖࡌࡓࡓࡥ࡙ࡎࡎࠪೣ"), bstack1ll_opy_ (u"ࠪࡿࢂ࠭೤")))
    data = {
        bstack1ll_opy_ (u"ࠫࡵࡸ࡯࡫ࡧࡦࡸࡓࡧ࡭ࡦࠩ೥"): config[bstack1ll_opy_ (u"ࠬࡶࡲࡰ࡬ࡨࡧࡹࡔࡡ࡮ࡧࠪ೦")],
        bstack1ll_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡓࡧ࡭ࡦࠩ೧"): config.get(bstack1ll_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡔࡡ࡮ࡧࠪ೨"), os.path.basename(os.getcwd())),
        bstack1ll_opy_ (u"ࠨࡵࡷࡥࡷࡺࡔࡪ࡯ࡨࠫ೩"): bstack1lllll1ll1_opy_(),
        bstack1ll_opy_ (u"ࠩࡧࡩࡸࡩࡲࡪࡲࡷ࡭ࡴࡴࠧ೪"): config.get(bstack1ll_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡆࡨࡷࡨࡸࡩࡱࡶ࡬ࡳࡳ࠭೫"), bstack1ll_opy_ (u"ࠫࠬ೬")),
        bstack1ll_opy_ (u"ࠬࡹ࡯ࡶࡴࡦࡩࠬ೭"): {
            bstack1ll_opy_ (u"࠭ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡐࡤࡱࡪ࠭೮"): bstack1l1ll1111l_opy_,
            bstack1ll_opy_ (u"ࠧࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭࡙ࡩࡷࡹࡩࡰࡰࠪ೯"): bstack1l1ll1l1l1_opy_,
            bstack1ll_opy_ (u"ࠨࡵࡧ࡯࡛࡫ࡲࡴ࡫ࡲࡲࠬ೰"): __version__
        },
        bstack1ll_opy_ (u"ࠩࡶࡩࡹࡺࡩ࡯ࡩࡶࠫೱ"): settings,
        bstack1ll_opy_ (u"ࠪࡺࡪࡸࡳࡪࡱࡱࡇࡴࡴࡴࡳࡱ࡯ࠫೲ"): bstack1l1ll111ll_opy_(),
        bstack1ll_opy_ (u"ࠫࡨ࡯ࡉ࡯ࡨࡲࠫೳ"): bstack11l111ll_opy_(),
        bstack1ll_opy_ (u"ࠬ࡮࡯ࡴࡶࡌࡲ࡫ࡵࠧ೴"): get_host_info(),
        bstack1ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠨ೵"): bstack1l111lll1_opy_(config)
    }
    headers = {
        bstack1ll_opy_ (u"ࠧࡄࡱࡱࡸࡪࡴࡴ࠮ࡖࡼࡴࡪ࠭೶"): bstack1ll_opy_ (u"ࠨࡣࡳࡴࡱ࡯ࡣࡢࡶ࡬ࡳࡳ࠵ࡪࡴࡱࡱࠫ೷"),
    }
    config = {
        bstack1ll_opy_ (u"ࠩࡤࡹࡹ࡮ࠧ೸"): (bstack1l1l1lll1l_opy_, bstack1l1l1ll111_opy_),
        bstack1ll_opy_ (u"ࠪ࡬ࡪࡧࡤࡦࡴࡶࠫ೹"): headers
    }
    response = bstack1llll1l11l_opy_(bstack1ll_opy_ (u"ࠫࡕࡕࡓࡕࠩ೺"), bstack1l1ll11111_opy_ + bstack1ll_opy_ (u"ࠬ࠵ࡴࡦࡵࡷࡣࡷࡻ࡮ࡴࠩ೻"), data, config)
    bstack1l1l1lll11_opy_ = response.json()
    if bstack1l1l1lll11_opy_[bstack1ll_opy_ (u"࠭ࡳࡶࡥࡦࡩࡸࡹࠧ೼")]:
      logger.info(bstack1ll_opy_ (u"ࠧࡴࡶࡤࡸࡺࡹࠠࡤࡱࡧࡩࠥ࠭೽") + str(response.status_code) + bstack1ll_opy_ (u"ࠨ࡞ࡱࠫ೾") + str(bstack1l1l1lll11_opy_))
      parsed = json.loads(os.getenv(bstack1ll_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡥࡁࡄࡅࡈࡗࡘࡏࡂࡊࡎࡌࡘ࡞ࡥࡃࡐࡐࡉࡍࡌ࡛ࡒࡂࡖࡌࡓࡓࡥ࡙ࡎࡎࠪ೿"), bstack1ll_opy_ (u"ࠪࡿࢂ࠭ഀ")))
      parsed[bstack1ll_opy_ (u"ࠫࡸࡩࡡ࡯ࡰࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠬഁ")] = bstack1l1l1lll11_opy_[bstack1ll_opy_ (u"ࠬࡪࡡࡵࡣࠪം")][bstack1ll_opy_ (u"࠭ࡳࡤࡣࡱࡲࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠧഃ")]
      os.environ[bstack1ll_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡣࡆࡉࡃࡆࡕࡖࡍࡇࡏࡌࡊࡖ࡜ࡣࡈࡕࡎࡇࡋࡊ࡙ࡗࡇࡔࡊࡑࡑࡣ࡞ࡓࡌࠨഄ")] = json.dumps(parsed)
      return bstack1l1l1lll11_opy_[bstack1ll_opy_ (u"ࠨࡦࡤࡸࡦ࠭അ")][bstack1ll_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࡖࡲ࡯ࡪࡴࠧആ")], bstack1l1l1lll11_opy_[bstack1ll_opy_ (u"ࠪࡨࡦࡺࡡࠨഇ")][bstack1ll_opy_ (u"ࠫ࡮ࡪࠧഈ")]
    else:
      logger.error(bstack1ll_opy_ (u"ࠬࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡࡹ࡫࡭ࡱ࡫ࠠࡳࡷࡱࡲ࡮ࡴࡧࠡࡄࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࠠࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱ࠾ࠥ࠭ഉ") + bstack1l1l1lll11_opy_[bstack1ll_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧഊ")])
      if bstack1l1l1lll11_opy_[bstack1ll_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨഋ")] == bstack1ll_opy_ (u"ࠨࡋࡱࡺࡦࡲࡩࡥࠢࡦࡳࡳ࡬ࡩࡨࡷࡵࡥࡹ࡯࡯࡯ࠢࡳࡥࡸࡹࡥࡥ࠰ࠪഌ"):
        for bstack1l1ll1l111_opy_ in bstack1l1l1lll11_opy_[bstack1ll_opy_ (u"ࠩࡨࡶࡷࡵࡲࡴࠩ഍")]:
          logger.error(bstack1l1ll1l111_opy_[bstack1ll_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫഎ")])
      return None, None
  except Exception as error:
    logger.error(bstack1ll_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡸࡪ࡬ࡰࡪࠦࡣࡳࡧࡤࡸ࡮ࡴࡧࠡࡶࡨࡷࡹࠦࡲࡶࡰࠣࡪࡴࡸࠠࡃࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࠦࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰ࠽ࠤࠧഏ") +  str(error))
    return None, None
def bstack1ll11l1ll1_opy_():
  if os.getenv(bstack1ll_opy_ (u"ࠬࡈࡓࡠࡃ࠴࠵࡞ࡥࡊࡘࡖࠪഐ")) is None:
    return {
        bstack1ll_opy_ (u"࠭ࡳࡵࡣࡷࡹࡸ࠭഑"): bstack1ll_opy_ (u"ࠧࡦࡴࡵࡳࡷ࠭ഒ"),
        bstack1ll_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩഓ"): bstack1ll_opy_ (u"ࠩࡅࡹ࡮ࡲࡤࠡࡥࡵࡩࡦࡺࡩࡰࡰࠣ࡬ࡦࡪࠠࡧࡣ࡬ࡰࡪࡪ࠮ࠨഔ")
    }
  data = {bstack1ll_opy_ (u"ࠪࡩࡳࡪࡔࡪ࡯ࡨࠫക"): bstack1lllll1ll1_opy_()}
  headers = {
      bstack1ll_opy_ (u"ࠫࡆࡻࡴࡩࡱࡵ࡭ࡿࡧࡴࡪࡱࡱࠫഖ"): bstack1ll_opy_ (u"ࠬࡈࡥࡢࡴࡨࡶࠥ࠭ഗ") + os.getenv(bstack1ll_opy_ (u"ࠨࡂࡔࡡࡄ࠵࠶࡟࡟ࡋ࡙ࡗࠦഘ")),
      bstack1ll_opy_ (u"ࠧࡄࡱࡱࡸࡪࡴࡴ࠮ࡖࡼࡴࡪ࠭ങ"): bstack1ll_opy_ (u"ࠨࡣࡳࡴࡱ࡯ࡣࡢࡶ࡬ࡳࡳ࠵ࡪࡴࡱࡱࠫച")
  }
  response = bstack1llll1l11l_opy_(bstack1ll_opy_ (u"ࠩࡓ࡙࡙࠭ഛ"), bstack1l1ll11111_opy_ + bstack1ll_opy_ (u"ࠪ࠳ࡹ࡫ࡳࡵࡡࡵࡹࡳࡹ࠯ࡴࡶࡲࡴࠬജ"), data, { bstack1ll_opy_ (u"ࠫ࡭࡫ࡡࡥࡧࡵࡷࠬഝ"): headers })
  try:
    if response.status_code == 200:
      logger.info(bstack1ll_opy_ (u"ࠧࡈࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࠤࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠡࡖࡨࡷࡹࠦࡒࡶࡰࠣࡱࡦࡸ࡫ࡦࡦࠣࡥࡸࠦࡣࡰ࡯ࡳࡰࡪࡺࡥࡥࠢࡤࡸࠥࠨഞ") + datetime.utcnow().isoformat() + bstack1ll_opy_ (u"࡚࠭ࠨട"))
      return {bstack1ll_opy_ (u"ࠧࡴࡶࡤࡸࡺࡹࠧഠ"): bstack1ll_opy_ (u"ࠨࡵࡸࡧࡨ࡫ࡳࡴࠩഡ"), bstack1ll_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪഢ"): bstack1ll_opy_ (u"ࠪࠫണ")}
    else:
      response.raise_for_status()
  except requests.RequestException as error:
    logger.error(bstack1ll_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡸࡪ࡬ࡰࡪࠦ࡭ࡢࡴ࡮࡭ࡳ࡭ࠠࡤࡱࡰࡴࡱ࡫ࡴࡪࡱࡱࠤࡴ࡬ࠠࡃࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࠦࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰࠣࡘࡪࡹࡴࠡࡔࡸࡲ࠿ࠦࠢത") + str(error))
    return {
        bstack1ll_opy_ (u"ࠬࡹࡴࡢࡶࡸࡷࠬഥ"): bstack1ll_opy_ (u"࠭ࡥࡳࡴࡲࡶࠬദ"),
        bstack1ll_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨധ"): str(error)
    }
def bstack111l11l11_opy_(caps, options):
  try:
    bstack1l1ll11l1l_opy_ = caps.get(bstack1ll_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫࠻ࡱࡳࡸ࡮ࡵ࡮ࡴࠩന"), {}).get(bstack1ll_opy_ (u"ࠩࡧࡩࡻ࡯ࡣࡦࡐࡤࡱࡪ࠭ഩ"), caps.get(bstack1ll_opy_ (u"ࠪࡨࡪࡼࡩࡤࡧࠪപ"), bstack1ll_opy_ (u"ࠫࠬഫ")))
    if bstack1l1ll11l1l_opy_:
      logger.warn(bstack1ll_opy_ (u"ࠧࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠢࡺ࡭ࡱࡲࠠࡳࡷࡱࠤࡴࡴ࡬ࡺࠢࡲࡲࠥࡊࡥࡴ࡭ࡷࡳࡵࠦࡢࡳࡱࡺࡷࡪࡸࡳ࠯ࠤബ"))
      return False
    browser = caps.get(bstack1ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡎࡢ࡯ࡨࠫഭ"), bstack1ll_opy_ (u"ࠧࠨമ")).lower()
    if browser != bstack1ll_opy_ (u"ࠨࡥ࡫ࡶࡴࡳࡥࠨയ"):
      logger.warn(bstack1ll_opy_ (u"ࠤࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࠦࡷࡪ࡮࡯ࠤࡷࡻ࡮ࠡࡱࡱࡰࡾࠦ࡯࡯ࠢࡆ࡬ࡷࡵ࡭ࡦࠢࡥࡶࡴࡽࡳࡦࡴࡶ࠲ࠧര"))
      return False
    browser_version = caps.get(bstack1ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠫറ"), caps.get(bstack1ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡤࡼࡥࡳࡵ࡬ࡳࡳ࠭ല")))
    if browser_version and browser_version != bstack1ll_opy_ (u"ࠬࡲࡡࡵࡧࡶࡸࠬള") and int(browser_version) <= 94:
      logger.warn(bstack1ll_opy_ (u"ࠨࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰࠣࡻ࡮ࡲ࡬ࠡࡴࡸࡲࠥࡵ࡮࡭ࡻࠣࡳࡳࠦࡃࡩࡴࡲࡱࡪࠦࡢࡳࡱࡺࡷࡪࡸࠠࡷࡧࡵࡷ࡮ࡵ࡮ࠡࡩࡵࡩࡦࡺࡥࡳࠢࡷ࡬ࡦࡴࠠ࠺࠶࠱ࠦഴ"))
      return False
    if not options is None:
      bstack1l1l1ll1ll_opy_ = options.to_capabilities().get(bstack1ll_opy_ (u"ࠧࡨࡱࡲ࡫࠿ࡩࡨࡳࡱࡰࡩࡔࡶࡴࡪࡱࡱࡷࠬവ"), {})
      if bstack1ll_opy_ (u"ࠨ࠯࠰࡬ࡪࡧࡤ࡭ࡧࡶࡷࠬശ") in bstack1l1l1ll1ll_opy_.get(bstack1ll_opy_ (u"ࠩࡤࡶ࡬ࡹࠧഷ"), []):
        logger.warn(bstack1ll_opy_ (u"ࠥࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠠࡸ࡫࡯ࡰࠥࡴ࡯ࡵࠢࡵࡹࡳࠦ࡯࡯ࠢ࡯ࡩ࡬ࡧࡣࡺࠢ࡫ࡩࡦࡪ࡬ࡦࡵࡶࠤࡲࡵࡤࡦ࠰ࠣࡗࡼ࡯ࡴࡤࡪࠣࡸࡴࠦ࡮ࡦࡹࠣ࡬ࡪࡧࡤ࡭ࡧࡶࡷࠥࡳ࡯ࡥࡧࠣࡳࡷࠦࡡࡷࡱ࡬ࡨࠥࡻࡳࡪࡰࡪࠤ࡭࡫ࡡࡥ࡮ࡨࡷࡸࠦ࡭ࡰࡦࡨ࠲ࠧസ"))
        return False
    return True
  except Exception as error:
    logger.debug(bstack1ll_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡺࡦࡲࡩࡥࡣࡷࡩࠥࡧ࠱࠲ࡻࠣࡷࡺࡶࡰࡰࡴࡷࠤ࠿ࠨഹ") + str(error))
    return False
def set_capabilities(caps, config):
  try:
    bstack1l1ll1lll1_opy_ = config.get(bstack1ll_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࡔࡶࡴࡪࡱࡱࡷࠬഺ"), {})
    bstack1l1ll1lll1_opy_[bstack1ll_opy_ (u"࠭ࡡࡶࡶ࡫ࡘࡴࡱࡥ࡯഻ࠩ")] = os.getenv(bstack1ll_opy_ (u"ࠧࡃࡕࡢࡅ࠶࠷࡙ࡠࡌ࡚ࡘ഼ࠬ"))
    bstack1l1ll111l1_opy_ = json.loads(os.getenv(bstack1ll_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡤࡇࡃࡄࡇࡖࡗࡎࡈࡉࡍࡋࡗ࡝ࡤࡉࡏࡏࡈࡌࡋ࡚ࡘࡁࡕࡋࡒࡒࡤ࡟ࡍࡍࠩഽ"), bstack1ll_opy_ (u"ࠩࡾࢁࠬാ"))).get(bstack1ll_opy_ (u"ࠪࡷࡨࡧ࡮࡯ࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠫി"))
    caps[bstack1ll_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫീ")] = True
    if bstack1ll_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯࠿ࡵࡰࡵ࡫ࡲࡲࡸ࠭ു") in caps:
      caps[bstack1ll_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡀ࡯ࡱࡶ࡬ࡳࡳࡹࠧൂ")][bstack1ll_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࡏࡱࡶ࡬ࡳࡳࡹࠧൃ")] = bstack1l1ll1lll1_opy_
      caps[bstack1ll_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫࠻ࡱࡳࡸ࡮ࡵ࡮ࡴࠩൄ")][bstack1ll_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࡑࡳࡸ࡮ࡵ࡮ࡴࠩ൅")][bstack1ll_opy_ (u"ࠪࡷࡨࡧ࡮࡯ࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠫെ")] = bstack1l1ll111l1_opy_
    else:
      caps[bstack1ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡒࡴࡹ࡯࡯࡯ࡵࠪേ")] = bstack1l1ll1lll1_opy_
      caps[bstack1ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࡓࡵࡺࡩࡰࡰࡶࠫൈ")][bstack1ll_opy_ (u"࠭ࡳࡤࡣࡱࡲࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠧ൉")] = bstack1l1ll111l1_opy_
  except Exception as error:
    logger.debug(bstack1ll_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣࡻ࡭࡯࡬ࡦࠢࡶࡩࡹࡺࡩ࡯ࡩࠣࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠠࡤࡣࡳࡥࡧ࡯࡬ࡪࡶ࡬ࡩࡸ࠴ࠠࡆࡴࡵࡳࡷࡀࠠࠣൊ") +  str(error))
def bstack1l1ll11l11_opy_(driver, bstack1l1l1ll11l_opy_):
  try:
    session = driver.session_id
    if session:
      bstack1l1ll1llll_opy_ = True
      current_url = driver.current_url
      try:
        url = urlparse(current_url)
      except Exception as e:
        bstack1l1ll1llll_opy_ = False
      bstack1l1ll1llll_opy_ = url.scheme in [bstack1ll_opy_ (u"ࠣࡪࡷࡸࡵࠨോ"), bstack1ll_opy_ (u"ࠤ࡫ࡸࡹࡶࡳࠣൌ")]
      if bstack1l1ll1llll_opy_:
        if bstack1l1l1ll11l_opy_:
          logger.info(bstack1ll_opy_ (u"ࠥࡗࡪࡺࡵࡱࠢࡩࡳࡷࠦࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡴࡦࡵࡷ࡭ࡳ࡭ࠠࡩࡣࡶࠤࡸࡺࡡࡳࡶࡨࡨ࠳ࠦࡁࡶࡶࡲࡱࡦࡺࡥࠡࡶࡨࡷࡹࠦࡣࡢࡵࡨࠤࡪࡾࡥࡤࡷࡷ࡭ࡴࡴࠠࡸ࡫࡯ࡰࠥࡨࡥࡨ࡫ࡱࠤࡲࡵ࡭ࡦࡰࡷࡥࡷ࡯࡬ࡺ࠰്ࠥ"))
          driver.execute_async_script(bstack1ll_opy_ (u"ࠦࠧࠨࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡤࡱࡱࡷࡹࠦࡣࡢ࡮࡯ࡦࡦࡩ࡫ࠡ࠿ࠣࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸࡡࡡࡳࡩࡸࡱࡪࡴࡴࡴ࠰࡯ࡩࡳ࡭ࡴࡩࠢ࠰ࠤ࠶ࡣ࠻ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡥࡲࡲࡸࡺࠠࡧࡰࠣࡁࠥ࠮ࠩࠡ࠿ࡁࠤࢀࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡻ࡮ࡴࡤࡰࡹ࠱ࡥࡩࡪࡅࡷࡧࡱࡸࡑ࡯ࡳࡵࡧࡱࡩࡷ࠮ࠧࡂ࠳࠴࡝ࡤ࡚ࡁࡑࡡࡖࡘࡆࡘࡔࡆࡆࠪ࠰ࠥ࡬࡮࠳ࠫ࠾ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡥࡲࡲࡸࡺࠠࡦࠢࡀࠤࡳ࡫ࡷࠡࡅࡸࡷࡹࡵ࡭ࡆࡸࡨࡲࡹ࠮ࠧࡂ࠳࠴࡝ࡤࡌࡏࡓࡅࡈࡣࡘ࡚ࡁࡓࡖࠪ࠭ࡀࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡻ࡮ࡴࡤࡰࡹ࠱ࡨ࡮ࡹࡰࡢࡶࡦ࡬ࡊࡼࡥ࡯ࡶࠫࡩ࠮ࡁࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡾ࠽ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡧࡴࡴࡳࡵࠢࡩࡲ࠷ࠦ࠽ࠡࠪࠬࠤࡂࡄࠠࡼࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡷࡪࡰࡧࡳࡼ࠴ࡲࡦ࡯ࡲࡺࡪࡋࡶࡦࡰࡷࡐ࡮ࡹࡴࡦࡰࡨࡶ࠭࠭ࡁ࠲࠳࡜ࡣ࡙ࡇࡐࡠࡕࡗࡅࡗ࡚ࡅࡅࠩ࠯ࠤ࡫ࡴࠩ࠼ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡣࡢ࡮࡯ࡦࡦࡩ࡫ࠩࠫ࠾ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࢂࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡦ࡯ࠪࠬ࠿ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠤࠥࠦൎ"))
          logger.info(bstack1ll_opy_ (u"ࠧࡇࡵࡵࡱࡰࡥࡹ࡫ࠠࡵࡧࡶࡸࠥࡩࡡࡴࡧࠣࡩࡽ࡫ࡣࡶࡶ࡬ࡳࡳࠦࡨࡢࡵࠣࡷࡹࡧࡲࡵࡧࡧ࠲ࠧ൏"))
        else:
          driver.execute_script(bstack1ll_opy_ (u"ࠨࠢࠣࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡦࡳࡳࡹࡴࠡࡧࠣࡁࠥࡴࡥࡸࠢࡆࡹࡸࡺ࡯࡮ࡇࡹࡩࡳࡺࠨࠨࡃ࠴࠵࡞ࡥࡆࡐࡔࡆࡉࡤ࡙ࡔࡐࡒࠪ࠭ࡀࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡷࡪࡰࡧࡳࡼ࠴ࡤࡪࡵࡳࡥࡹࡩࡨࡆࡸࡨࡲࡹ࠮ࡥࠪ࠽ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠢࠣࠤ൐"))
      return bstack1l1l1ll11l_opy_
  except Exception as e:
    logger.error(bstack1ll_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡳࡵࡣࡵࡸ࡮ࡴࡧࠡࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡣࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠥࡹࡣࡢࡰࠣࡪࡴࡸࠠࡵࡪ࡬ࡷࠥࡺࡥࡴࡶࠣࡧࡦࡹࡥ࠻ࠢࠥ൑") + str(e))
    return False
def bstack1l1ll1l1ll_opy_(driver, item):
  try:
    bstack1l1l1l1ll1_opy_ = [item.cls.__name__] if not item.cls is None else []
    bstack1l1ll1ll1l_opy_ = {
        bstack1ll_opy_ (u"ࠣࡵࡤࡺࡪࡘࡥࡴࡷ࡯ࡸࡸࠨ൒"): True,
        bstack1ll_opy_ (u"ࠤࡷࡩࡸࡺࡄࡦࡶࡤ࡭ࡱࡹࠢ൓"): {
            bstack1ll_opy_ (u"ࠥࡲࡦࡳࡥࠣൔ"): item.name,
            bstack1ll_opy_ (u"ࠦࡹ࡫ࡳࡵࡔࡸࡲࡎࡪࠢൕ"): os.environ.get(bstack1ll_opy_ (u"ࠬࡈࡓࡠࡃ࠴࠵࡞ࡥࡔࡆࡕࡗࡣࡗ࡛ࡎࡠࡋࡇࠫൖ")),
            bstack1ll_opy_ (u"ࠨࡦࡪ࡮ࡨࡔࡦࡺࡨࠣൗ"): str(item.path),
            bstack1ll_opy_ (u"ࠢࡴࡥࡲࡴࡪࡒࡩࡴࡶࠥ൘"): [item.module.__name__, *bstack1l1l1l1ll1_opy_, item.name],
        },
        bstack1ll_opy_ (u"ࠣࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࠥ൙"): _1l1ll1l11l_opy_(driver)
    }
    driver.execute_async_script(bstack1ll_opy_ (u"ࠤࠥࠦࠏࠦࠠࠡࠢࠣࠤࠥࠦࡣࡰࡰࡶࡸࠥࡩࡡ࡭࡮ࡥࡥࡨࡱࠠ࠾ࠢࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࡠࡧࡲࡨࡷࡰࡩࡳࡺࡳ࠯࡮ࡨࡲ࡬ࡺࡨࠡ࠯ࠣ࠵ࡢࡁࠊࠡࠢࠣࠤࠥࠦࠠࠡࡶ࡫࡭ࡸ࠴ࡲࡦࡵࠣࡁࠥࡴࡵ࡭࡮࠾ࠎࠥࠦࠠࠡࠢࠣࠤࠥ࡯ࡦࠡࠪࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࡠ࠶࡝࠯ࡵࡤࡺࡪࡘࡥࡴࡷ࡯ࡸࡸ࠯ࠠࡼࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡸ࡫ࡱࡨࡴࡽ࠮ࡢࡦࡧࡉࡻ࡫࡮ࡵࡎ࡬ࡷࡹ࡫࡮ࡦࡴࠫࠫࡆ࠷࠱࡚ࡡࡗࡅࡕࡥࡔࡓࡃࡑࡗࡕࡕࡒࡕࡇࡕࠫ࠱ࠦࠨࡦࡸࡨࡲࡹ࠯ࠠ࠾ࡀࠣࡿࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡸ࡫ࡱࡨࡴࡽ࠮ࡵࡣࡳࡘࡷࡧ࡮ࡴࡲࡲࡶࡹ࡫ࡲࡅࡣࡷࡥࠥࡃࠠࡦࡸࡨࡲࡹ࠴ࡤࡦࡶࡤ࡭ࡱࡁࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡷ࡬࡮ࡹ࠮ࡳࡧࡶࠤࡂࠦࡷࡪࡰࡧࡳࡼ࠴ࡴࡢࡲࡗࡶࡦࡴࡳࡱࡱࡵࡸࡪࡸࡄࡢࡶࡤ࠿ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡤࡣ࡯ࡰࡧࡧࡣ࡬ࠪࡷ࡬࡮ࡹ࠮ࡳࡧࡶ࠭ࡀࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࢂ࠯࠻ࠋࠢࠣࠤࠥࠦࠠࠡࠢࢀࠎࠥࠦࠠࠡࠢࠣࠤࠥࡩ࡯࡯ࡵࡷࠤࡪࠦ࠽ࠡࡰࡨࡻࠥࡉࡵࡴࡶࡲࡱࡊࡼࡥ࡯ࡶࠫࠫࡆ࠷࠱࡚ࡡࡗࡉࡘ࡚࡟ࡆࡐࡇࠫ࠱ࠦࡻࠡࡦࡨࡸࡦ࡯࡬࠻ࠢࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࡠ࠶࡝ࠡࡿࠬ࠿ࠏࠦࠠࠡࠢࠣࠤࠥࠦࡷࡪࡰࡧࡳࡼ࠴ࡤࡪࡵࡳࡥࡹࡩࡨࡆࡸࡨࡲࡹ࠮ࡥࠪ࠽ࠍࠤࠥࠦࠠࠡࠢࠣࠤ࡮࡬ࠠࠩࠣࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࡠ࠶࡝࠯ࡵࡤࡺࡪࡘࡥࡴࡷ࡯ࡸࡸ࠯ࠠࡼࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡤࡣ࡯ࡰࡧࡧࡣ࡬ࠪࠬ࠿ࠏࠦࠠࠡࠢࠣࠤࠥࠦࡽࠋࠢࠣࠤࠥࠨࠢࠣ൚"), bstack1l1ll1ll1l_opy_)
    logger.info(bstack1ll_opy_ (u"ࠥࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡸࡪࡹࡴࡪࡰࡪࠤ࡫ࡵࡲࠡࡶ࡫࡭ࡸࠦࡴࡦࡵࡷࠤࡨࡧࡳࡦࠢ࡫ࡥࡸࠦࡥ࡯ࡦࡨࡨ࠳ࠨ൛"))
  except Exception as bstack1l1ll1ll11_opy_:
    logger.error(bstack1ll_opy_ (u"ࠦࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡷ࡫ࡳࡶ࡮ࡷࡷࠥࡩ࡯ࡶ࡮ࡧࠤࡳࡵࡴࠡࡤࡨࠤࡵࡸ࡯ࡤࡧࡶࡷࡪࡪࠠࡧࡱࡵࠤࡹ࡮ࡥࠡࡶࡨࡷࡹࠦࡣࡢࡵࡨ࠾ࠥࠨ൜") + item.path + bstack1ll_opy_ (u"ࠧࠦࡅࡳࡴࡲࡶࠥࡀࠢ൝") + str(bstack1l1ll1ll11_opy_))