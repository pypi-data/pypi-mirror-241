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
import atexit
import os
import signal
import sys
import yaml
import requests
import logging
import threading
import socket
import datetime
import string
import random
import json
import collections.abc
import re
import multiprocessing
import traceback
import copy
from packaging import version
from browserstack.local import Local
from urllib.parse import urlparse
from bstack_utils.constants import *
from bstack_utils.percy import *
import time
import requests
def bstack11l1l111_opy_():
  global CONFIG
  headers = {
        bstack111ll1l_opy_ (u"ࠩࡆࡳࡳࡺࡥ࡯ࡶ࠰ࡸࡾࡶࡥࠨࡵ"): bstack111ll1l_opy_ (u"ࠪࡥࡵࡶ࡬ࡪࡥࡤࡸ࡮ࡵ࡮࠰࡬ࡶࡳࡳ࠭ࡶ"),
      }
  proxies = bstack11ll1l1ll_opy_(CONFIG, bstack1ll1l1l11l_opy_)
  try:
    response = requests.get(bstack1ll1l1l11l_opy_, headers=headers, proxies=proxies, timeout=5)
    if response.json():
      bstack1l1l11l1_opy_ = response.json()[bstack111ll1l_opy_ (u"ࠫ࡭ࡻࡢࡴࠩࡷ")]
      logger.debug(bstack1ll11l1l11_opy_.format(response.json()))
      return bstack1l1l11l1_opy_
    else:
      logger.debug(bstack1lll1l1lll_opy_.format(bstack111ll1l_opy_ (u"ࠧࡘࡥࡴࡲࡲࡲࡸ࡫ࠠࡋࡕࡒࡒࠥࡶࡡࡳࡵࡨࠤࡪࡸࡲࡰࡴࠣࠦࡸ")))
  except Exception as e:
    logger.debug(bstack1lll1l1lll_opy_.format(e))
def bstack1ll1l1ll_opy_(hub_url):
  global CONFIG
  url = bstack111ll1l_opy_ (u"ࠨࡨࡵࡶࡳࡷ࠿࠵࠯ࠣࡹ")+  hub_url + bstack111ll1l_opy_ (u"ࠢ࠰ࡥ࡫ࡩࡨࡱࠢࡺ")
  headers = {
        bstack111ll1l_opy_ (u"ࠨࡅࡲࡲࡹ࡫࡮ࡵ࠯ࡷࡽࡵ࡫ࠧࡻ"): bstack111ll1l_opy_ (u"ࠩࡤࡴࡵࡲࡩࡤࡣࡷ࡭ࡴࡴ࠯࡫ࡵࡲࡲࠬࡼ"),
      }
  proxies = bstack11ll1l1ll_opy_(CONFIG, url)
  try:
    start_time = time.perf_counter()
    requests.get(url, headers=headers, proxies=proxies, timeout=5)
    latency = time.perf_counter() - start_time
    logger.debug(bstack1ll11l1l1l_opy_.format(hub_url, latency))
    return dict(hub_url=hub_url, latency=latency)
  except Exception as e:
    logger.debug(bstack1lll1l1l11_opy_.format(hub_url, e))
def bstack11ll111l1_opy_():
  try:
    global bstack1ll11111_opy_
    bstack1l1l11l1_opy_ = bstack11l1l111_opy_()
    bstack111l111ll_opy_ = []
    results = []
    for bstack1ll11l1111_opy_ in bstack1l1l11l1_opy_:
      bstack111l111ll_opy_.append(bstack111l1111l_opy_(target=bstack1ll1l1ll_opy_,args=(bstack1ll11l1111_opy_,)))
    for t in bstack111l111ll_opy_:
      t.start()
    for t in bstack111l111ll_opy_:
      results.append(t.join())
    bstack11111l11_opy_ = {}
    for item in results:
      hub_url = item[bstack111ll1l_opy_ (u"ࠪ࡬ࡺࡨ࡟ࡶࡴ࡯ࠫࡽ")]
      latency = item[bstack111ll1l_opy_ (u"ࠫࡱࡧࡴࡦࡰࡦࡽࠬࡾ")]
      bstack11111l11_opy_[hub_url] = latency
    bstack1lll111ll_opy_ = min(bstack11111l11_opy_, key= lambda x: bstack11111l11_opy_[x])
    bstack1ll11111_opy_ = bstack1lll111ll_opy_
    logger.debug(bstack1l11ll11l_opy_.format(bstack1lll111ll_opy_))
  except Exception as e:
    logger.debug(bstack1lll11llll_opy_.format(e))
from bstack_utils.messages import *
from bstack_utils.config import Config
from bstack_utils.helper import bstack11111l11l_opy_, bstack11llllll1_opy_, bstack11l11l11_opy_, bstack1ll1111ll_opy_, Notset, bstack1111lll1_opy_, \
  bstack1lll11l11_opy_, bstack1lllll11l_opy_, bstack11l111l1l_opy_, bstack1ll111111_opy_, bstack1lllllllll_opy_, bstack1ll11l11l_opy_, bstack111l11ll_opy_, \
  bstack1l111lll1_opy_
from bstack_utils.bstack1l1111l11_opy_ import bstack1l11lll1l_opy_
from bstack_utils.proxy import bstack1l1l1l111_opy_, bstack11ll1l1ll_opy_, bstack1l1ll11ll_opy_, bstack1l1l1ll11_opy_
import bstack_utils.bstack11ll1111_opy_ as bstack111l1l11l_opy_
from browserstack_sdk.bstack11111ll11_opy_ import *
from browserstack_sdk.bstack1l1l11ll_opy_ import *
from bstack_utils.bstack1ll1l11l11_opy_ import bstack1lll111ll1_opy_
bstack1ll1llll1_opy_ = bstack111ll1l_opy_ (u"ࠬࠦࠠ࠰ࠬࠣࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃࠠࠫ࠱࡟ࡲࠥࠦࡩࡧࠪࡳࡥ࡬࡫ࠠ࠾࠿ࡀࠤࡻࡵࡩࡥࠢ࠳࠭ࠥࢁ࡜࡯ࠢࠣࠤࡹࡸࡹࡼ࡞ࡱࠤࡨࡵ࡮ࡴࡶࠣࡪࡸࠦ࠽ࠡࡴࡨࡵࡺ࡯ࡲࡦࠪ࡟ࠫ࡫ࡹ࡜ࠨࠫ࠾ࡠࡳࠦࠠࠡࠢࠣࡪࡸ࠴ࡡࡱࡲࡨࡲࡩࡌࡩ࡭ࡧࡖࡽࡳࡩࠨࡣࡵࡷࡥࡨࡱ࡟ࡱࡣࡷ࡬࠱ࠦࡊࡔࡑࡑ࠲ࡸࡺࡲࡪࡰࡪ࡭࡫ࡿࠨࡱࡡ࡬ࡲࡩ࡫ࡸࠪࠢ࠮ࠤࠧࡀࠢࠡ࠭ࠣࡎࡘࡕࡎ࠯ࡵࡷࡶ࡮ࡴࡧࡪࡨࡼࠬࡏ࡙ࡏࡏ࠰ࡳࡥࡷࡹࡥࠩࠪࡤࡻࡦ࡯ࡴࠡࡰࡨࡻࡕࡧࡧࡦ࠴࠱ࡩࡻࡧ࡬ࡶࡣࡷࡩ࠭ࠨࠨࠪࠢࡀࡂࠥࢁࡽࠣ࠮ࠣࡠࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࡼࠤࡤࡧࡹ࡯࡯࡯ࠤ࠽ࠤࠧ࡭ࡥࡵࡕࡨࡷࡸ࡯࡯࡯ࡆࡨࡸࡦ࡯࡬ࡴࠤࢀࡠࠬ࠯ࠩࠪ࡝ࠥ࡬ࡦࡹࡨࡦࡦࡢ࡭ࡩࠨ࡝ࠪࠢ࠮ࠤࠧ࠲࡜࡝ࡰࠥ࠭ࡡࡴࠠࠡࠢࠣࢁࡨࡧࡴࡤࡪࠫࡩࡽ࠯ࡻ࡝ࡰࠣࠤࠥࠦࡽ࡝ࡰࠣࠤࢂࡢ࡮ࠡࠢ࠲࠮ࠥࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾ࠢ࠭࠳ࠬࡿ")
bstack1l1lllll_opy_ = bstack111ll1l_opy_ (u"࠭࡜࡯࠱࠭ࠤࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽ࠡࠬ࠲ࡠࡳࡩ࡯࡯ࡵࡷࠤࡧࡹࡴࡢࡥ࡮ࡣࡵࡧࡴࡩࠢࡀࠤࡵࡸ࡯ࡤࡧࡶࡷ࠳ࡧࡲࡨࡸ࡞ࡴࡷࡵࡣࡦࡵࡶ࠲ࡦࡸࡧࡷ࠰࡯ࡩࡳ࡭ࡴࡩࠢ࠰ࠤ࠸ࡣ࡜࡯ࡥࡲࡲࡸࡺࠠࡣࡵࡷࡥࡨࡱ࡟ࡤࡣࡳࡷࠥࡃࠠࡱࡴࡲࡧࡪࡹࡳ࠯ࡣࡵ࡫ࡻࡡࡰࡳࡱࡦࡩࡸࡹ࠮ࡢࡴࡪࡺ࠳ࡲࡥ࡯ࡩࡷ࡬ࠥ࠳ࠠ࠲࡟࡟ࡲࡨࡵ࡮ࡴࡶࠣࡴࡤ࡯࡮ࡥࡧࡻࠤࡂࠦࡰࡳࡱࡦࡩࡸࡹ࠮ࡢࡴࡪࡺࡠࡶࡲࡰࡥࡨࡷࡸ࠴ࡡࡳࡩࡹ࠲ࡱ࡫࡮ࡨࡶ࡫ࠤ࠲ࠦ࠲࡞࡞ࡱࡴࡷࡵࡣࡦࡵࡶ࠲ࡦࡸࡧࡷࠢࡀࠤࡵࡸ࡯ࡤࡧࡶࡷ࠳ࡧࡲࡨࡸ࠱ࡷࡱ࡯ࡣࡦࠪ࠳࠰ࠥࡶࡲࡰࡥࡨࡷࡸ࠴ࡡࡳࡩࡹ࠲ࡱ࡫࡮ࡨࡶ࡫ࠤ࠲ࠦ࠳ࠪ࡞ࡱࡧࡴࡴࡳࡵࠢ࡬ࡱࡵࡵࡲࡵࡡࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹ࠺࡟ࡣࡵࡷࡥࡨࡱࠠ࠾ࠢࡵࡩࡶࡻࡩࡳࡧࠫࠦࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࠣࠫ࠾ࡠࡳ࡯࡭ࡱࡱࡵࡸࡤࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵ࠶ࡢࡦࡸࡺࡡࡤ࡭࠱ࡧ࡭ࡸ࡯࡮࡫ࡸࡱ࠳ࡲࡡࡶࡰࡦ࡬ࠥࡃࠠࡢࡵࡼࡲࡨࠦࠨ࡭ࡣࡸࡲࡨ࡮ࡏࡱࡶ࡬ࡳࡳࡹࠩࠡ࠿ࡁࠤࢀࡢ࡮࡭ࡧࡷࠤࡨࡧࡰࡴ࠽࡟ࡲࡹࡸࡹࠡࡽ࡟ࡲࡨࡧࡰࡴࠢࡀࠤࡏ࡙ࡏࡏ࠰ࡳࡥࡷࡹࡥࠩࡤࡶࡸࡦࡩ࡫ࡠࡥࡤࡴࡸ࠯࡜࡯ࠢࠣࢁࠥࡩࡡࡵࡥ࡫ࠬࡪࡾࠩࠡࡽ࡟ࡲࠥࠦࠠࠡࡿ࡟ࡲࠥࠦࡲࡦࡶࡸࡶࡳࠦࡡࡸࡣ࡬ࡸࠥ࡯࡭ࡱࡱࡵࡸࡤࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵ࠶ࡢࡦࡸࡺࡡࡤ࡭࠱ࡧ࡭ࡸ࡯࡮࡫ࡸࡱ࠳ࡩ࡯࡯ࡰࡨࡧࡹ࠮ࡻ࡝ࡰࠣࠤࠥࠦࡷࡴࡇࡱࡨࡵࡵࡩ࡯ࡶ࠽ࠤࡥࡽࡳࡴ࠼࠲࠳ࡨࡪࡰ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡤࡱࡰ࠳ࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࡀࡥࡤࡴࡸࡃࠤࡼࡧࡱࡧࡴࡪࡥࡖࡔࡌࡇࡴࡳࡰࡰࡰࡨࡲࡹ࠮ࡊࡔࡑࡑ࠲ࡸࡺࡲࡪࡰࡪ࡭࡫ࡿࠨࡤࡣࡳࡷ࠮࠯ࡽࡡ࠮࡟ࡲࠥࠦࠠࠡ࠰࠱࠲ࡱࡧࡵ࡯ࡥ࡫ࡓࡵࡺࡩࡰࡰࡶࡠࡳࠦࠠࡾࠫ࡟ࡲࢂࡢ࡮࠰ࠬࠣࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃࠠࠫ࠱࡟ࡲࠬࢀ")
from ._version import __version__
bstack1ll1ll111_opy_ = None
CONFIG = {}
bstack1ll1lll11_opy_ = {}
bstack1ll1llll11_opy_ = {}
bstack1l1l1l1l1_opy_ = None
bstack11l11ll11_opy_ = None
bstack1111llll1_opy_ = None
bstack1111ll11l_opy_ = -1
bstack11l1ll1ll_opy_ = bstack1llll11111_opy_
bstack1l1111111_opy_ = 1
bstack1l11ll1l_opy_ = False
bstack11111l1l1_opy_ = False
bstack111111lll_opy_ = bstack111ll1l_opy_ (u"ࠧࠨࢁ")
bstack11l11llll_opy_ = bstack111ll1l_opy_ (u"ࠨࠩࢂ")
bstack111l1l1ll_opy_ = False
bstack1l111111l_opy_ = True
bstack1l1l1ll1l_opy_ = bstack111ll1l_opy_ (u"ࠩࠪࢃ")
bstack1lll1l11l1_opy_ = []
bstack1ll11111_opy_ = bstack111ll1l_opy_ (u"ࠪࠫࢄ")
bstack1ll1l1ll1l_opy_ = False
bstack1ll11l11ll_opy_ = None
bstack11lll1ll1_opy_ = None
bstack111lll11l_opy_ = -1
bstack1ll1ll11ll_opy_ = os.path.join(os.path.expanduser(bstack111ll1l_opy_ (u"ࠫࢃ࠭ࢅ")), bstack111ll1l_opy_ (u"ࠬ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠬࢆ"), bstack111ll1l_opy_ (u"࠭࠮ࡳࡱࡥࡳࡹ࠳ࡲࡦࡲࡲࡶࡹ࠳ࡨࡦ࡮ࡳࡩࡷ࠴ࡪࡴࡱࡱࠫࢇ"))
bstack1llll111l1_opy_ = []
bstack1ll111l1l_opy_ = []
bstack11l111l1_opy_ = False
bstack1lll11111l_opy_ = False
bstack11lll1l11_opy_ = None
bstack1ll1l111ll_opy_ = None
bstack1ll11ll11l_opy_ = None
bstack1l111l111_opy_ = None
bstack1lll111l1l_opy_ = None
bstack1ll1l11111_opy_ = None
bstack1l1l111ll_opy_ = None
bstack1l1l1llll_opy_ = None
bstack11lll1l1l_opy_ = None
bstack11l1llll_opy_ = None
bstack1111l1111_opy_ = None
bstack1llllll1l1_opy_ = None
bstack1ll11l1l1_opy_ = None
bstack11l1111ll_opy_ = None
bstack1l1l11ll1_opy_ = None
bstack1l1l1ll1_opy_ = None
bstack1ll1l11l_opy_ = None
bstack1ll1ll1lll_opy_ = None
bstack1lll1ll1ll_opy_ = bstack111ll1l_opy_ (u"ࠢࠣ࢈")
logger = logging.getLogger(__name__)
logging.basicConfig(level=bstack11l1ll1ll_opy_,
                    format=bstack111ll1l_opy_ (u"ࠨ࡞ࡱࠩ࠭ࡧࡳࡤࡶ࡬ࡱࡪ࠯ࡳࠡ࡝ࠨࠬࡳࡧ࡭ࡦࠫࡶࡡࡠࠫࠨ࡭ࡧࡹࡩࡱࡴࡡ࡮ࡧࠬࡷࡢࠦ࠭ࠡࠧࠫࡱࡪࡹࡳࡢࡩࡨ࠭ࡸ࠭ࢉ"),
                    datefmt=bstack111ll1l_opy_ (u"ࠩࠨࡌ࠿ࠫࡍ࠻ࠧࡖࠫࢊ"),
                    stream=sys.stdout)
bstack1ll1l1llll_opy_ = Config.get_instance()
percy = bstack11ll1ll1_opy_()
def bstack1l1l11l1l_opy_():
  global CONFIG
  global bstack11l1ll1ll_opy_
  if bstack111ll1l_opy_ (u"ࠪࡰࡴ࡭ࡌࡦࡸࡨࡰࠬࢋ") in CONFIG:
    bstack11l1ll1ll_opy_ = bstack1lll1ll1_opy_[CONFIG[bstack111ll1l_opy_ (u"ࠫࡱࡵࡧࡍࡧࡹࡩࡱ࠭ࢌ")]]
    logging.getLogger().setLevel(bstack11l1ll1ll_opy_)
def bstack111111l1l_opy_():
  global CONFIG
  global bstack11l111l1_opy_
  bstack1l1lll1ll_opy_ = bstack1l1llll1l_opy_(CONFIG)
  if (bstack111ll1l_opy_ (u"ࠬࡹ࡫ࡪࡲࡖࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠧࢍ") in bstack1l1lll1ll_opy_ and str(bstack1l1lll1ll_opy_[bstack111ll1l_opy_ (u"࠭ࡳ࡬࡫ࡳࡗࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠨࢎ")]).lower() == bstack111ll1l_opy_ (u"ࠧࡵࡴࡸࡩࠬ࢏")):
    bstack11l111l1_opy_ = True
def bstack11l1l1l1l_opy_():
  from appium.version import version as appium_version
  return version.parse(appium_version)
def bstack1lllll1l1l_opy_():
  from selenium import webdriver
  return version.parse(webdriver.__version__)
def bstack11lllll1l_opy_():
  args = sys.argv
  for i in range(len(args)):
    if bstack111ll1l_opy_ (u"ࠣ࠯࠰ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡥࡲࡲ࡫࡯ࡧࡧ࡫࡯ࡩࠧ࢐") == args[i].lower() or bstack111ll1l_opy_ (u"ࠤ࠰࠱ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡧࡴࡴࡦࡪࡩࠥ࢑") == args[i].lower():
      path = args[i + 1]
      sys.argv.remove(args[i])
      sys.argv.remove(path)
      global bstack1l1l1ll1l_opy_
      bstack1l1l1ll1l_opy_ += bstack111ll1l_opy_ (u"ࠪ࠱࠲ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡇࡴࡴࡦࡪࡩࡉ࡭ࡱ࡫ࠠࠨ࢒") + path
      return path
  return None
bstack1llll11ll_opy_ = re.compile(bstack111ll1l_opy_ (u"ࡶࠧ࠴ࠪࡀ࡞ࠧࡿ࠭࠴ࠪࡀࠫࢀ࠲࠯ࡅࠢ࢓"))
def bstack1ll11ll11_opy_(loader, node):
  value = loader.construct_scalar(node)
  for group in bstack1llll11ll_opy_.findall(value):
    if group is not None and os.environ.get(group) is not None:
      value = value.replace(bstack111ll1l_opy_ (u"ࠧࠪࡻࠣ࢔") + group + bstack111ll1l_opy_ (u"ࠨࡽࠣ࢕"), os.environ.get(group))
  return value
def bstack1l1111lll_opy_():
  bstack1l111l1l_opy_ = bstack11lllll1l_opy_()
  if bstack1l111l1l_opy_ and os.path.exists(os.path.abspath(bstack1l111l1l_opy_)):
    fileName = bstack1l111l1l_opy_
  if bstack111ll1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡃࡐࡐࡉࡍࡌࡥࡆࡊࡎࡈࠫ࢖") in os.environ and os.path.exists(
          os.path.abspath(os.environ[bstack111ll1l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡄࡑࡑࡊࡎࡍ࡟ࡇࡋࡏࡉࠬࢗ")])) and not bstack111ll1l_opy_ (u"ࠩࡩ࡭ࡱ࡫ࡎࡢ࡯ࡨࠫ࢘") in locals():
    fileName = os.environ[bstack111ll1l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡆࡓࡓࡌࡉࡈࡡࡉࡍࡑࡋ࢙ࠧ")]
  if bstack111ll1l_opy_ (u"ࠫ࡫࡯࡬ࡦࡐࡤࡱࡪ࢚࠭") in locals():
    bstack1l1ll_opy_ = os.path.abspath(fileName)
  else:
    bstack1l1ll_opy_ = bstack111ll1l_opy_ (u"࢛ࠬ࠭")
  bstack11l111l11_opy_ = os.getcwd()
  bstack1ll1l1l1ll_opy_ = bstack111ll1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡿ࡭࡭ࠩ࢜")
  bstack11ll111l_opy_ = bstack111ll1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡹࡢ࡯࡯ࠫ࢝")
  while (not os.path.exists(bstack1l1ll_opy_)) and bstack11l111l11_opy_ != bstack111ll1l_opy_ (u"ࠣࠤ࢞"):
    bstack1l1ll_opy_ = os.path.join(bstack11l111l11_opy_, bstack1ll1l1l1ll_opy_)
    if not os.path.exists(bstack1l1ll_opy_):
      bstack1l1ll_opy_ = os.path.join(bstack11l111l11_opy_, bstack11ll111l_opy_)
    if bstack11l111l11_opy_ != os.path.dirname(bstack11l111l11_opy_):
      bstack11l111l11_opy_ = os.path.dirname(bstack11l111l11_opy_)
    else:
      bstack11l111l11_opy_ = bstack111ll1l_opy_ (u"ࠤࠥ࢟")
  if not os.path.exists(bstack1l1ll_opy_):
    bstack1ll11l111_opy_(
      bstack1llll1l1l1_opy_.format(os.getcwd()))
  try:
    with open(bstack1l1ll_opy_, bstack111ll1l_opy_ (u"ࠪࡶࠬࢠ")) as stream:
      yaml.add_implicit_resolver(bstack111ll1l_opy_ (u"ࠦࠦࡶࡡࡵࡪࡨࡼࠧࢡ"), bstack1llll11ll_opy_)
      yaml.add_constructor(bstack111ll1l_opy_ (u"ࠧࠧࡰࡢࡶ࡫ࡩࡽࠨࢢ"), bstack1ll11ll11_opy_)
      config = yaml.load(stream, yaml.FullLoader)
      return config
  except:
    with open(bstack1l1ll_opy_, bstack111ll1l_opy_ (u"࠭ࡲࠨࢣ")) as stream:
      try:
        config = yaml.safe_load(stream)
        return config
      except yaml.YAMLError as exc:
        bstack1ll11l111_opy_(bstack1lll1l1l_opy_.format(str(exc)))
def bstack111lll11_opy_(config):
  bstack1ll1lllll1_opy_ = bstack11l11l11l_opy_(config)
  for option in list(bstack1ll1lllll1_opy_):
    if option.lower() in bstack1l1ll1l1_opy_ and option != bstack1l1ll1l1_opy_[option.lower()]:
      bstack1ll1lllll1_opy_[bstack1l1ll1l1_opy_[option.lower()]] = bstack1ll1lllll1_opy_[option]
      del bstack1ll1lllll1_opy_[option]
  return config
def bstack1l11l1ll1_opy_():
  global bstack1ll1llll11_opy_
  for key, bstack1lll111lll_opy_ in bstack111ll1111_opy_.items():
    if isinstance(bstack1lll111lll_opy_, list):
      for var in bstack1lll111lll_opy_:
        if var in os.environ and os.environ[var] and str(os.environ[var]).strip():
          bstack1ll1llll11_opy_[key] = os.environ[var]
          break
    elif bstack1lll111lll_opy_ in os.environ and os.environ[bstack1lll111lll_opy_] and str(os.environ[bstack1lll111lll_opy_]).strip():
      bstack1ll1llll11_opy_[key] = os.environ[bstack1lll111lll_opy_]
  if bstack111ll1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡌࡐࡅࡄࡐࡤࡏࡄࡆࡐࡗࡍࡋࡏࡅࡓࠩࢤ") in os.environ:
    bstack1ll1llll11_opy_[bstack111ll1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࡌࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬࢥ")] = {}
    bstack1ll1llll11_opy_[bstack111ll1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࡍࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭ࢦ")][bstack111ll1l_opy_ (u"ࠪࡰࡴࡩࡡ࡭ࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬࢧ")] = os.environ[bstack111ll1l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡐࡔࡉࡁࡍࡡࡌࡈࡊࡔࡔࡊࡈࡌࡉࡗ࠭ࢨ")]
def bstack1l11l1ll_opy_():
  global bstack1ll1lll11_opy_
  global bstack1l1l1ll1l_opy_
  for idx, val in enumerate(sys.argv):
    if idx < len(sys.argv) and bstack111ll1l_opy_ (u"ࠬ࠳࠭ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴࡬ࡰࡥࡤࡰࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨࢩ").lower() == val.lower():
      bstack1ll1lll11_opy_[bstack111ll1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪࢪ")] = {}
      bstack1ll1lll11_opy_[bstack111ll1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫࢫ")][bstack111ll1l_opy_ (u"ࠨ࡮ࡲࡧࡦࡲࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪࢬ")] = sys.argv[idx + 1]
      del sys.argv[idx:idx + 2]
      break
  for key, bstack1ll1ll1ll1_opy_ in bstack1lllllll1_opy_.items():
    if isinstance(bstack1ll1ll1ll1_opy_, list):
      for idx, val in enumerate(sys.argv):
        for var in bstack1ll1ll1ll1_opy_:
          if idx < len(sys.argv) and bstack111ll1l_opy_ (u"ࠩ࠰࠱ࠬࢭ") + var.lower() == val.lower() and not key in bstack1ll1lll11_opy_:
            bstack1ll1lll11_opy_[key] = sys.argv[idx + 1]
            bstack1l1l1ll1l_opy_ += bstack111ll1l_opy_ (u"ࠪࠤ࠲࠳ࠧࢮ") + var + bstack111ll1l_opy_ (u"ࠫࠥ࠭ࢯ") + sys.argv[idx + 1]
            del sys.argv[idx:idx + 2]
            break
    else:
      for idx, val in enumerate(sys.argv):
        if idx < len(sys.argv) and bstack111ll1l_opy_ (u"ࠬ࠳࠭ࠨࢰ") + bstack1ll1ll1ll1_opy_.lower() == val.lower() and not key in bstack1ll1lll11_opy_:
          bstack1ll1lll11_opy_[key] = sys.argv[idx + 1]
          bstack1l1l1ll1l_opy_ += bstack111ll1l_opy_ (u"࠭ࠠ࠮࠯ࠪࢱ") + bstack1ll1ll1ll1_opy_ + bstack111ll1l_opy_ (u"ࠧࠡࠩࢲ") + sys.argv[idx + 1]
          del sys.argv[idx:idx + 2]
def bstack1ll1l1111l_opy_(config):
  bstack1lllll1l11_opy_ = config.keys()
  for bstack11l1ll11l_opy_, bstack111lll1l1_opy_ in bstack1l1l111l_opy_.items():
    if bstack111lll1l1_opy_ in bstack1lllll1l11_opy_:
      config[bstack11l1ll11l_opy_] = config[bstack111lll1l1_opy_]
      del config[bstack111lll1l1_opy_]
  for bstack11l1ll11l_opy_, bstack111lll1l1_opy_ in bstack11l11ll1_opy_.items():
    if isinstance(bstack111lll1l1_opy_, list):
      for bstack1ll11l1l_opy_ in bstack111lll1l1_opy_:
        if bstack1ll11l1l_opy_ in bstack1lllll1l11_opy_:
          config[bstack11l1ll11l_opy_] = config[bstack1ll11l1l_opy_]
          del config[bstack1ll11l1l_opy_]
          break
    elif bstack111lll1l1_opy_ in bstack1lllll1l11_opy_:
      config[bstack11l1ll11l_opy_] = config[bstack111lll1l1_opy_]
      del config[bstack111lll1l1_opy_]
  for bstack1ll11l1l_opy_ in list(config):
    for bstack1ll1lll1l_opy_ in bstack1111ll1l_opy_:
      if bstack1ll11l1l_opy_.lower() == bstack1ll1lll1l_opy_.lower() and bstack1ll11l1l_opy_ != bstack1ll1lll1l_opy_:
        config[bstack1ll1lll1l_opy_] = config[bstack1ll11l1l_opy_]
        del config[bstack1ll11l1l_opy_]
  bstack1lll1lllll_opy_ = []
  if bstack111ll1l_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫࢳ") in config:
    bstack1lll1lllll_opy_ = config[bstack111ll1l_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬࢴ")]
  for platform in bstack1lll1lllll_opy_:
    for bstack1ll11l1l_opy_ in list(platform):
      for bstack1ll1lll1l_opy_ in bstack1111ll1l_opy_:
        if bstack1ll11l1l_opy_.lower() == bstack1ll1lll1l_opy_.lower() and bstack1ll11l1l_opy_ != bstack1ll1lll1l_opy_:
          platform[bstack1ll1lll1l_opy_] = platform[bstack1ll11l1l_opy_]
          del platform[bstack1ll11l1l_opy_]
  for bstack11l1ll11l_opy_, bstack111lll1l1_opy_ in bstack11l11ll1_opy_.items():
    for platform in bstack1lll1lllll_opy_:
      if isinstance(bstack111lll1l1_opy_, list):
        for bstack1ll11l1l_opy_ in bstack111lll1l1_opy_:
          if bstack1ll11l1l_opy_ in platform:
            platform[bstack11l1ll11l_opy_] = platform[bstack1ll11l1l_opy_]
            del platform[bstack1ll11l1l_opy_]
            break
      elif bstack111lll1l1_opy_ in platform:
        platform[bstack11l1ll11l_opy_] = platform[bstack111lll1l1_opy_]
        del platform[bstack111lll1l1_opy_]
  for bstack111l1lll1_opy_ in bstack11ll111ll_opy_:
    if bstack111l1lll1_opy_ in config:
      if not bstack11ll111ll_opy_[bstack111l1lll1_opy_] in config:
        config[bstack11ll111ll_opy_[bstack111l1lll1_opy_]] = {}
      config[bstack11ll111ll_opy_[bstack111l1lll1_opy_]].update(config[bstack111l1lll1_opy_])
      del config[bstack111l1lll1_opy_]
  for platform in bstack1lll1lllll_opy_:
    for bstack111l1lll1_opy_ in bstack11ll111ll_opy_:
      if bstack111l1lll1_opy_ in list(platform):
        if not bstack11ll111ll_opy_[bstack111l1lll1_opy_] in platform:
          platform[bstack11ll111ll_opy_[bstack111l1lll1_opy_]] = {}
        platform[bstack11ll111ll_opy_[bstack111l1lll1_opy_]].update(platform[bstack111l1lll1_opy_])
        del platform[bstack111l1lll1_opy_]
  config = bstack111lll11_opy_(config)
  return config
def bstack11lllll11_opy_(config):
  global bstack11l11llll_opy_
  if bstack111ll1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࠧࢵ") in config and str(config[bstack111ll1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࠨࢶ")]).lower() != bstack111ll1l_opy_ (u"ࠬ࡬ࡡ࡭ࡵࡨࠫࢷ"):
    if not bstack111ll1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪࢸ") in config:
      config[bstack111ll1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫࢹ")] = {}
    if not bstack111ll1l_opy_ (u"ࠨ࡮ࡲࡧࡦࡲࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪࢺ") in config[bstack111ll1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࡍࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭ࢻ")]:
      bstack1111ll111_opy_ = datetime.datetime.now()
      bstack1ll11lllll_opy_ = bstack1111ll111_opy_.strftime(bstack111ll1l_opy_ (u"ࠪࠩࡩࡥࠥࡣࡡࠨࡌࠪࡓࠧࢼ"))
      hostname = socket.gethostname()
      bstack11ll11111_opy_ = bstack111ll1l_opy_ (u"ࠫࠬࢽ").join(random.choices(string.ascii_lowercase + string.digits, k=4))
      identifier = bstack111ll1l_opy_ (u"ࠬࢁࡽࡠࡽࢀࡣࢀࢃࠧࢾ").format(bstack1ll11lllll_opy_, hostname, bstack11ll11111_opy_)
      config[bstack111ll1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪࢿ")][bstack111ll1l_opy_ (u"ࠧ࡭ࡱࡦࡥࡱࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩࣀ")] = identifier
    bstack11l11llll_opy_ = config[bstack111ll1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࡌࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬࣁ")][bstack111ll1l_opy_ (u"ࠩ࡯ࡳࡨࡧ࡬ࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫࣂ")]
  return config
def bstack11lll1lll_opy_():
  bstack1111l1l1l_opy_ =  bstack1ll111111_opy_()[bstack111ll1l_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠩࣃ")]
  return bstack1111l1l1l_opy_ if bstack1111l1l1l_opy_ else -1
def bstack11l1ll1l_opy_(bstack1111l1l1l_opy_):
  global CONFIG
  if not bstack111ll1l_opy_ (u"ࠫࠩࢁࡂࡖࡋࡏࡈࡤࡔࡕࡎࡄࡈࡖࢂ࠭ࣄ") in CONFIG[bstack111ll1l_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧࣅ")]:
    return
  CONFIG[bstack111ll1l_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨࣆ")] = CONFIG[bstack111ll1l_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩࣇ")].replace(
    bstack111ll1l_opy_ (u"ࠨࠦࡾࡆ࡚ࡏࡌࡅࡡࡑ࡙ࡒࡈࡅࡓࡿࠪࣈ"),
    str(bstack1111l1l1l_opy_)
  )
def bstack1ll1l1l11_opy_():
  global CONFIG
  if not bstack111ll1l_opy_ (u"ࠩࠧࡿࡉࡇࡔࡆࡡࡗࡍࡒࡋࡽࠨࣉ") in CONFIG[bstack111ll1l_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬ࣊")]:
    return
  bstack1111ll111_opy_ = datetime.datetime.now()
  bstack1ll11lllll_opy_ = bstack1111ll111_opy_.strftime(bstack111ll1l_opy_ (u"ࠫࠪࡪ࠭ࠦࡤ࠰ࠩࡍࡀࠥࡎࠩ࣋"))
  CONFIG[bstack111ll1l_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧ࣌")] = CONFIG[bstack111ll1l_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨ࣍")].replace(
    bstack111ll1l_opy_ (u"ࠧࠥࡽࡇࡅ࡙ࡋ࡟ࡕࡋࡐࡉࢂ࠭࣎"),
    bstack1ll11lllll_opy_
  )
def bstack111lll1ll_opy_():
  global CONFIG
  if bstack111ll1l_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴ࣏ࠪ") in CONFIG and not bool(CONFIG[bstack111ll1l_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵ࣐ࠫ")]):
    del CONFIG[bstack111ll1l_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶ࣑ࠬ")]
    return
  if not bstack111ll1l_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࣒࠭") in CONFIG:
    CONFIG[bstack111ll1l_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸ࣓ࠧ")] = bstack111ll1l_opy_ (u"࠭ࠣࠥࡽࡅ࡙ࡎࡒࡄࡠࡐࡘࡑࡇࡋࡒࡾࠩࣔ")
  if bstack111ll1l_opy_ (u"ࠧࠥࡽࡇࡅ࡙ࡋ࡟ࡕࡋࡐࡉࢂ࠭ࣕ") in CONFIG[bstack111ll1l_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪࣖ")]:
    bstack1ll1l1l11_opy_()
    os.environ[bstack111ll1l_opy_ (u"ࠩࡅࡗ࡙ࡇࡃࡌࡡࡆࡓࡒࡈࡉࡏࡇࡇࡣࡇ࡛ࡉࡍࡆࡢࡍࡉ࠭ࣗ")] = CONFIG[bstack111ll1l_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬࣘ")]
  if not bstack111ll1l_opy_ (u"ࠫࠩࢁࡂࡖࡋࡏࡈࡤࡔࡕࡎࡄࡈࡖࢂ࠭ࣙ") in CONFIG[bstack111ll1l_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧࣚ")]:
    return
  bstack1111l1l1l_opy_ = bstack111ll1l_opy_ (u"࠭ࠧࣛ")
  bstack1lll1l1ll_opy_ = bstack11lll1lll_opy_()
  if bstack1lll1l1ll_opy_ != -1:
    bstack1111l1l1l_opy_ = bstack111ll1l_opy_ (u"ࠧࡄࡋࠣࠫࣜ") + str(bstack1lll1l1ll_opy_)
  if bstack1111l1l1l_opy_ == bstack111ll1l_opy_ (u"ࠨࠩࣝ"):
    bstack1111l11ll_opy_ = bstack1lll11l1_opy_(CONFIG[bstack111ll1l_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠬࣞ")])
    if bstack1111l11ll_opy_ != -1:
      bstack1111l1l1l_opy_ = str(bstack1111l11ll_opy_)
  if bstack1111l1l1l_opy_:
    bstack11l1ll1l_opy_(bstack1111l1l1l_opy_)
    os.environ[bstack111ll1l_opy_ (u"ࠪࡆࡘ࡚ࡁࡄࡍࡢࡇࡔࡓࡂࡊࡐࡈࡈࡤࡈࡕࡊࡎࡇࡣࡎࡊࠧࣟ")] = CONFIG[bstack111ll1l_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭࣠")]
def bstack1l1l11lll_opy_(bstack1ll11l1ll1_opy_, bstack1ll1l1ll11_opy_, path):
  bstack1lllll1ll1_opy_ = {
    bstack111ll1l_opy_ (u"ࠬ࡯ࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩ࣡"): bstack1ll1l1ll11_opy_
  }
  if os.path.exists(path):
    bstack111l111l1_opy_ = json.load(open(path, bstack111ll1l_opy_ (u"࠭ࡲࡣࠩ࣢")))
  else:
    bstack111l111l1_opy_ = {}
  bstack111l111l1_opy_[bstack1ll11l1ll1_opy_] = bstack1lllll1ll1_opy_
  with open(path, bstack111ll1l_opy_ (u"ࠢࡸࣣ࠭ࠥ")) as outfile:
    json.dump(bstack111l111l1_opy_, outfile)
def bstack1lll11l1_opy_(bstack1ll11l1ll1_opy_):
  bstack1ll11l1ll1_opy_ = str(bstack1ll11l1ll1_opy_)
  bstack11111111_opy_ = os.path.join(os.path.expanduser(bstack111ll1l_opy_ (u"ࠨࢀࠪࣤ")), bstack111ll1l_opy_ (u"ࠩ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠩࣥ"))
  try:
    if not os.path.exists(bstack11111111_opy_):
      os.makedirs(bstack11111111_opy_)
    file_path = os.path.join(os.path.expanduser(bstack111ll1l_opy_ (u"ࠪࢂࣦࠬ")), bstack111ll1l_opy_ (u"ࠫ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠫࣧ"), bstack111ll1l_opy_ (u"ࠬ࠴ࡢࡶ࡫࡯ࡨ࠲ࡴࡡ࡮ࡧ࠰ࡧࡦࡩࡨࡦ࠰࡭ࡷࡴࡴࠧࣨ"))
    if not os.path.isfile(file_path):
      with open(file_path, bstack111ll1l_opy_ (u"࠭ࡷࠨࣩ")):
        pass
      with open(file_path, bstack111ll1l_opy_ (u"ࠢࡸ࠭ࠥ࣪")) as outfile:
        json.dump({}, outfile)
    with open(file_path, bstack111ll1l_opy_ (u"ࠨࡴࠪ࣫")) as bstack1l11lllll_opy_:
      bstack1l11111l1_opy_ = json.load(bstack1l11lllll_opy_)
    if bstack1ll11l1ll1_opy_ in bstack1l11111l1_opy_:
      bstack1111ll11_opy_ = bstack1l11111l1_opy_[bstack1ll11l1ll1_opy_][bstack111ll1l_opy_ (u"ࠩ࡬ࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭࣬")]
      bstack1l11l11l1_opy_ = int(bstack1111ll11_opy_) + 1
      bstack1l1l11lll_opy_(bstack1ll11l1ll1_opy_, bstack1l11l11l1_opy_, file_path)
      return bstack1l11l11l1_opy_
    else:
      bstack1l1l11lll_opy_(bstack1ll11l1ll1_opy_, 1, file_path)
      return 1
  except Exception as e:
    logger.warn(bstack1ll11ll1l1_opy_.format(str(e)))
    return -1
def bstack11l111ll1_opy_(config):
  if not config[bstack111ll1l_opy_ (u"ࠪࡹࡸ࡫ࡲࡏࡣࡰࡩ࣭ࠬ")] or not config[bstack111ll1l_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶࡏࡪࡿ࣮ࠧ")]:
    return True
  else:
    return False
def bstack1l1l111l1_opy_(config, index=0):
  global bstack111l1l1ll_opy_
  bstack1l1ll111_opy_ = {}
  caps = bstack11l1ll11_opy_ + bstack1llllll11l_opy_
  if bstack111l1l1ll_opy_:
    caps += bstack1ll1111l1_opy_
  for key in config:
    if key in caps + [bstack111ll1l_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ࣯")]:
      continue
    bstack1l1ll111_opy_[key] = config[key]
  if bstack111ll1l_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࣰࠩ") in config:
    for bstack1ll11lll11_opy_ in config[bstack111ll1l_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࣱࠪ")][index]:
      if bstack1ll11lll11_opy_ in caps + [bstack111ll1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡐࡤࡱࡪࣲ࠭"), bstack111ll1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪࣳ")]:
        continue
      bstack1l1ll111_opy_[bstack1ll11lll11_opy_] = config[bstack111ll1l_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ࣴ")][index][bstack1ll11lll11_opy_]
  bstack1l1ll111_opy_[bstack111ll1l_opy_ (u"ࠫ࡭ࡵࡳࡵࡐࡤࡱࡪ࠭ࣵ")] = socket.gethostname()
  if bstack111ll1l_opy_ (u"ࠬࡼࡥࡳࡵ࡬ࡳࡳࣶ࠭") in bstack1l1ll111_opy_:
    del (bstack1l1ll111_opy_[bstack111ll1l_opy_ (u"࠭ࡶࡦࡴࡶ࡭ࡴࡴࠧࣷ")])
  return bstack1l1ll111_opy_
def bstack111ll111_opy_(config):
  global bstack111l1l1ll_opy_
  bstack1l1l1111_opy_ = {}
  caps = bstack1llllll11l_opy_
  if bstack111l1l1ll_opy_:
    caps += bstack1ll1111l1_opy_
  for key in caps:
    if key in config:
      bstack1l1l1111_opy_[key] = config[key]
  return bstack1l1l1111_opy_
def bstack111lll111_opy_(bstack1l1ll111_opy_, bstack1l1l1111_opy_):
  bstack1llllllll_opy_ = {}
  for key in bstack1l1ll111_opy_.keys():
    if key in bstack1l1l111l_opy_:
      bstack1llllllll_opy_[bstack1l1l111l_opy_[key]] = bstack1l1ll111_opy_[key]
    else:
      bstack1llllllll_opy_[key] = bstack1l1ll111_opy_[key]
  for key in bstack1l1l1111_opy_:
    if key in bstack1l1l111l_opy_:
      bstack1llllllll_opy_[bstack1l1l111l_opy_[key]] = bstack1l1l1111_opy_[key]
    else:
      bstack1llllllll_opy_[key] = bstack1l1l1111_opy_[key]
  return bstack1llllllll_opy_
def bstack1lllllll1l_opy_(config, index=0):
  global bstack111l1l1ll_opy_
  config = copy.deepcopy(config)
  caps = {}
  bstack1l1l1111_opy_ = bstack111ll111_opy_(config)
  bstack111ll11l1_opy_ = bstack1llllll11l_opy_
  bstack111ll11l1_opy_ += bstack1ll11lll1l_opy_
  if bstack111l1l1ll_opy_:
    bstack111ll11l1_opy_ += bstack1ll1111l1_opy_
  if bstack111ll1l_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪࣸ") in config:
    if bstack111ll1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡐࡤࡱࡪࣹ࠭") in config[bstack111ll1l_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࣺࠬ")][index]:
      caps[bstack111ll1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡒࡦࡳࡥࠨࣻ")] = config[bstack111ll1l_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧࣼ")][index][bstack111ll1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠪࣽ")]
    if bstack111ll1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠧࣾ") in config[bstack111ll1l_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪࣿ")][index]:
      caps[bstack111ll1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩऀ")] = str(config[bstack111ll1l_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬँ")][index][bstack111ll1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠫं")])
    bstack111l1ll1_opy_ = {}
    for bstack1llll1ll_opy_ in bstack111ll11l1_opy_:
      if bstack1llll1ll_opy_ in config[bstack111ll1l_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧः")][index]:
        if bstack1llll1ll_opy_ == bstack111ll1l_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡖࡦࡴࡶ࡭ࡴࡴࠧऄ"):
          try:
            bstack111l1ll1_opy_[bstack1llll1ll_opy_] = str(config[bstack111ll1l_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩअ")][index][bstack1llll1ll_opy_] * 1.0)
          except:
            bstack111l1ll1_opy_[bstack1llll1ll_opy_] = str(config[bstack111ll1l_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪआ")][index][bstack1llll1ll_opy_])
        else:
          bstack111l1ll1_opy_[bstack1llll1ll_opy_] = config[bstack111ll1l_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫइ")][index][bstack1llll1ll_opy_]
        del (config[bstack111ll1l_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬई")][index][bstack1llll1ll_opy_])
    bstack1l1l1111_opy_ = update(bstack1l1l1111_opy_, bstack111l1ll1_opy_)
  bstack1l1ll111_opy_ = bstack1l1l111l1_opy_(config, index)
  for bstack1ll11l1l_opy_ in bstack1llllll11l_opy_ + [bstack111ll1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡒࡦࡳࡥࠨउ"), bstack111ll1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠬऊ")]:
    if bstack1ll11l1l_opy_ in bstack1l1ll111_opy_:
      bstack1l1l1111_opy_[bstack1ll11l1l_opy_] = bstack1l1ll111_opy_[bstack1ll11l1l_opy_]
      del (bstack1l1ll111_opy_[bstack1ll11l1l_opy_])
  if bstack1111lll1_opy_(config):
    bstack1l1ll111_opy_[bstack111ll1l_opy_ (u"ࠬࡻࡳࡦ࡙࠶ࡇࠬऋ")] = True
    caps.update(bstack1l1l1111_opy_)
    caps[bstack111ll1l_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡀ࡯ࡱࡶ࡬ࡳࡳࡹࠧऌ")] = bstack1l1ll111_opy_
  else:
    bstack1l1ll111_opy_[bstack111ll1l_opy_ (u"ࠧࡶࡵࡨ࡛࠸ࡉࠧऍ")] = False
    caps.update(bstack111lll111_opy_(bstack1l1ll111_opy_, bstack1l1l1111_opy_))
    if bstack111ll1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡐࡤࡱࡪ࠭ऎ") in caps:
      caps[bstack111ll1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࠪए")] = caps[bstack111ll1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡒࡦࡳࡥࠨऐ")]
      del (caps[bstack111ll1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡓࡧ࡭ࡦࠩऑ")])
    if bstack111ll1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ऒ") in caps:
      caps[bstack111ll1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠨओ")] = caps[bstack111ll1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠨऔ")]
      del (caps[bstack111ll1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩक")])
  return caps
def bstack111111111_opy_():
  global bstack1ll11111_opy_
  if bstack1lllll1l1l_opy_() <= version.parse(bstack111ll1l_opy_ (u"ࠩ࠶࠲࠶࠹࠮࠱ࠩख")):
    if bstack1ll11111_opy_ != bstack111ll1l_opy_ (u"ࠪࠫग"):
      return bstack111ll1l_opy_ (u"ࠦ࡭ࡺࡴࡱ࠼࠲࠳ࠧघ") + bstack1ll11111_opy_ + bstack111ll1l_opy_ (u"ࠧࡀ࠸࠱࠱ࡺࡨ࠴࡮ࡵࡣࠤङ")
    return bstack11ll11l1l_opy_
  if bstack1ll11111_opy_ != bstack111ll1l_opy_ (u"࠭ࠧच"):
    return bstack111ll1l_opy_ (u"ࠢࡩࡶࡷࡴࡸࡀ࠯࠰ࠤछ") + bstack1ll11111_opy_ + bstack111ll1l_opy_ (u"ࠣ࠱ࡺࡨ࠴࡮ࡵࡣࠤज")
  return bstack1ll11l1ll_opy_
def bstack11l11l1l1_opy_(options):
  return hasattr(options, bstack111ll1l_opy_ (u"ࠩࡶࡩࡹࡥࡣࡢࡲࡤࡦ࡮ࡲࡩࡵࡻࠪझ"))
def update(d, u):
  for k, v in u.items():
    if isinstance(v, collections.abc.Mapping):
      d[k] = update(d.get(k, {}), v)
    else:
      if isinstance(v, list):
        d[k] = d.get(k, []) + v
      else:
        d[k] = v
  return d
def bstack1ll11l1lll_opy_(options, bstack1lllll1l1_opy_):
  for bstack11111ll1_opy_ in bstack1lllll1l1_opy_:
    if bstack11111ll1_opy_ in [bstack111ll1l_opy_ (u"ࠪࡥࡷ࡭ࡳࠨञ"), bstack111ll1l_opy_ (u"ࠫࡪࡾࡴࡦࡰࡶ࡭ࡴࡴࡳࠨट")]:
      continue
    if bstack11111ll1_opy_ in options._experimental_options:
      options._experimental_options[bstack11111ll1_opy_] = update(options._experimental_options[bstack11111ll1_opy_],
                                                         bstack1lllll1l1_opy_[bstack11111ll1_opy_])
    else:
      options.add_experimental_option(bstack11111ll1_opy_, bstack1lllll1l1_opy_[bstack11111ll1_opy_])
  if bstack111ll1l_opy_ (u"ࠬࡧࡲࡨࡵࠪठ") in bstack1lllll1l1_opy_:
    for arg in bstack1lllll1l1_opy_[bstack111ll1l_opy_ (u"࠭ࡡࡳࡩࡶࠫड")]:
      options.add_argument(arg)
    del (bstack1lllll1l1_opy_[bstack111ll1l_opy_ (u"ࠧࡢࡴࡪࡷࠬढ")])
  if bstack111ll1l_opy_ (u"ࠨࡧࡻࡸࡪࡴࡳࡪࡱࡱࡷࠬण") in bstack1lllll1l1_opy_:
    for ext in bstack1lllll1l1_opy_[bstack111ll1l_opy_ (u"ࠩࡨࡼࡹ࡫࡮ࡴ࡫ࡲࡲࡸ࠭त")]:
      options.add_extension(ext)
    del (bstack1lllll1l1_opy_[bstack111ll1l_opy_ (u"ࠪࡩࡽࡺࡥ࡯ࡵ࡬ࡳࡳࡹࠧथ")])
def bstack1l1lll1l1_opy_(options, bstack1l1lll11_opy_):
  if bstack111ll1l_opy_ (u"ࠫࡵࡸࡥࡧࡵࠪद") in bstack1l1lll11_opy_:
    for bstack11111lll1_opy_ in bstack1l1lll11_opy_[bstack111ll1l_opy_ (u"ࠬࡶࡲࡦࡨࡶࠫध")]:
      if bstack11111lll1_opy_ in options._preferences:
        options._preferences[bstack11111lll1_opy_] = update(options._preferences[bstack11111lll1_opy_], bstack1l1lll11_opy_[bstack111ll1l_opy_ (u"࠭ࡰࡳࡧࡩࡷࠬन")][bstack11111lll1_opy_])
      else:
        options.set_preference(bstack11111lll1_opy_, bstack1l1lll11_opy_[bstack111ll1l_opy_ (u"ࠧࡱࡴࡨࡪࡸ࠭ऩ")][bstack11111lll1_opy_])
  if bstack111ll1l_opy_ (u"ࠨࡣࡵ࡫ࡸ࠭प") in bstack1l1lll11_opy_:
    for arg in bstack1l1lll11_opy_[bstack111ll1l_opy_ (u"ࠩࡤࡶ࡬ࡹࠧफ")]:
      options.add_argument(arg)
def bstack111l1ll1l_opy_(options, bstack1ll11ll1l_opy_):
  if bstack111ll1l_opy_ (u"ࠪࡻࡪࡨࡶࡪࡧࡺࠫब") in bstack1ll11ll1l_opy_:
    options.use_webview(bool(bstack1ll11ll1l_opy_[bstack111ll1l_opy_ (u"ࠫࡼ࡫ࡢࡷ࡫ࡨࡻࠬभ")]))
  bstack1ll11l1lll_opy_(options, bstack1ll11ll1l_opy_)
def bstack1llll1lll_opy_(options, bstack1llll1l1_opy_):
  for bstack1l11l111l_opy_ in bstack1llll1l1_opy_:
    if bstack1l11l111l_opy_ in [bstack111ll1l_opy_ (u"ࠬࡺࡥࡤࡪࡱࡳࡱࡵࡧࡺࡒࡵࡩࡻ࡯ࡥࡸࠩम"), bstack111ll1l_opy_ (u"࠭ࡡࡳࡩࡶࠫय")]:
      continue
    options.set_capability(bstack1l11l111l_opy_, bstack1llll1l1_opy_[bstack1l11l111l_opy_])
  if bstack111ll1l_opy_ (u"ࠧࡢࡴࡪࡷࠬर") in bstack1llll1l1_opy_:
    for arg in bstack1llll1l1_opy_[bstack111ll1l_opy_ (u"ࠨࡣࡵ࡫ࡸ࠭ऱ")]:
      options.add_argument(arg)
  if bstack111ll1l_opy_ (u"ࠩࡷࡩࡨ࡮࡮ࡰ࡮ࡲ࡫ࡾࡖࡲࡦࡸ࡬ࡩࡼ࠭ल") in bstack1llll1l1_opy_:
    options.bstack1ll1lll11l_opy_(bool(bstack1llll1l1_opy_[bstack111ll1l_opy_ (u"ࠪࡸࡪࡩࡨ࡯ࡱ࡯ࡳ࡬ࡿࡐࡳࡧࡹ࡭ࡪࡽࠧळ")]))
def bstack11l1lll1l_opy_(options, bstack1lll1111l1_opy_):
  for bstack1ll1llll_opy_ in bstack1lll1111l1_opy_:
    if bstack1ll1llll_opy_ in [bstack111ll1l_opy_ (u"ࠫࡦࡪࡤࡪࡶ࡬ࡳࡳࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨऴ"), bstack111ll1l_opy_ (u"ࠬࡧࡲࡨࡵࠪव")]:
      continue
    options._options[bstack1ll1llll_opy_] = bstack1lll1111l1_opy_[bstack1ll1llll_opy_]
  if bstack111ll1l_opy_ (u"࠭ࡡࡥࡦ࡬ࡸ࡮ࡵ࡮ࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪश") in bstack1lll1111l1_opy_:
    for bstack1llll1ll1_opy_ in bstack1lll1111l1_opy_[bstack111ll1l_opy_ (u"ࠧࡢࡦࡧ࡭ࡹ࡯࡯࡯ࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫष")]:
      options.bstack1l11l1l1_opy_(
        bstack1llll1ll1_opy_, bstack1lll1111l1_opy_[bstack111ll1l_opy_ (u"ࠨࡣࡧࡨ࡮ࡺࡩࡰࡰࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬस")][bstack1llll1ll1_opy_])
  if bstack111ll1l_opy_ (u"ࠩࡤࡶ࡬ࡹࠧह") in bstack1lll1111l1_opy_:
    for arg in bstack1lll1111l1_opy_[bstack111ll1l_opy_ (u"ࠪࡥࡷ࡭ࡳࠨऺ")]:
      options.add_argument(arg)
def bstack1111ll1ll_opy_(options, caps):
  if not hasattr(options, bstack111ll1l_opy_ (u"ࠫࡐࡋ࡙ࠨऻ")):
    return
  if options.KEY == bstack111ll1l_opy_ (u"ࠬ࡭࡯ࡰࡩ࠽ࡧ࡭ࡸ࡯࡮ࡧࡒࡴࡹ࡯࡯࡯ࡵ़ࠪ") and options.KEY in caps:
    bstack1ll11l1lll_opy_(options, caps[bstack111ll1l_opy_ (u"࠭ࡧࡰࡱࡪ࠾ࡨ࡮ࡲࡰ࡯ࡨࡓࡵࡺࡩࡰࡰࡶࠫऽ")])
  elif options.KEY == bstack111ll1l_opy_ (u"ࠧ࡮ࡱࡽ࠾࡫࡯ࡲࡦࡨࡲࡼࡔࡶࡴࡪࡱࡱࡷࠬा") and options.KEY in caps:
    bstack1l1lll1l1_opy_(options, caps[bstack111ll1l_opy_ (u"ࠨ࡯ࡲࡾ࠿࡬ࡩࡳࡧࡩࡳࡽࡕࡰࡵ࡫ࡲࡲࡸ࠭ि")])
  elif options.KEY == bstack111ll1l_opy_ (u"ࠩࡶࡥ࡫ࡧࡲࡪ࠰ࡲࡴࡹ࡯࡯࡯ࡵࠪी") and options.KEY in caps:
    bstack1llll1lll_opy_(options, caps[bstack111ll1l_opy_ (u"ࠪࡷࡦ࡬ࡡࡳ࡫࠱ࡳࡵࡺࡩࡰࡰࡶࠫु")])
  elif options.KEY == bstack111ll1l_opy_ (u"ࠫࡲࡹ࠺ࡦࡦࡪࡩࡔࡶࡴࡪࡱࡱࡷࠬू") and options.KEY in caps:
    bstack111l1ll1l_opy_(options, caps[bstack111ll1l_opy_ (u"ࠬࡳࡳ࠻ࡧࡧ࡫ࡪࡕࡰࡵ࡫ࡲࡲࡸ࠭ृ")])
  elif options.KEY == bstack111ll1l_opy_ (u"࠭ࡳࡦ࠼࡬ࡩࡔࡶࡴࡪࡱࡱࡷࠬॄ") and options.KEY in caps:
    bstack11l1lll1l_opy_(options, caps[bstack111ll1l_opy_ (u"ࠧࡴࡧ࠽࡭ࡪࡕࡰࡵ࡫ࡲࡲࡸ࠭ॅ")])
def bstack1ll11111l_opy_(caps):
  global bstack111l1l1ll_opy_
  if isinstance(os.environ.get(bstack111ll1l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡊࡕࡢࡅࡕࡖ࡟ࡂࡗࡗࡓࡒࡇࡔࡆࠩॆ")), str):
    bstack111l1l1ll_opy_ = eval(os.getenv(bstack111ll1l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡋࡖࡣࡆࡖࡐࡠࡃࡘࡘࡔࡓࡁࡕࡇࠪे")))
  if bstack111l1l1ll_opy_:
    if bstack11l1l1l1l_opy_() < version.parse(bstack111ll1l_opy_ (u"ࠪ࠶࠳࠹࠮࠱ࠩै")):
      return None
    else:
      from appium.options.common.base import AppiumOptions
      options = AppiumOptions().load_capabilities(caps)
      return options
  else:
    browser = bstack111ll1l_opy_ (u"ࠫࡨ࡮ࡲࡰ࡯ࡨࠫॉ")
    if bstack111ll1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠪॊ") in caps:
      browser = caps[bstack111ll1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡎࡢ࡯ࡨࠫो")]
    elif bstack111ll1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࠨौ") in caps:
      browser = caps[bstack111ll1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳ्ࠩ")]
    browser = str(browser).lower()
    if browser == bstack111ll1l_opy_ (u"ࠩ࡬ࡴ࡭ࡵ࡮ࡦࠩॎ") or browser == bstack111ll1l_opy_ (u"ࠪ࡭ࡵࡧࡤࠨॏ"):
      browser = bstack111ll1l_opy_ (u"ࠫࡸࡧࡦࡢࡴ࡬ࠫॐ")
    if browser == bstack111ll1l_opy_ (u"ࠬࡹࡡ࡮ࡵࡸࡲ࡬࠭॑"):
      browser = bstack111ll1l_opy_ (u"࠭ࡣࡩࡴࡲࡱࡪ॒࠭")
    if browser not in [bstack111ll1l_opy_ (u"ࠧࡤࡪࡵࡳࡲ࡫ࠧ॓"), bstack111ll1l_opy_ (u"ࠨࡧࡧ࡫ࡪ࠭॔"), bstack111ll1l_opy_ (u"ࠩ࡬ࡩࠬॕ"), bstack111ll1l_opy_ (u"ࠪࡷࡦ࡬ࡡࡳ࡫ࠪॖ"), bstack111ll1l_opy_ (u"ࠫ࡫࡯ࡲࡦࡨࡲࡼࠬॗ")]:
      return None
    try:
      package = bstack111ll1l_opy_ (u"ࠬࡹࡥ࡭ࡧࡱ࡭ࡺࡳ࠮ࡸࡧࡥࡨࡷ࡯ࡶࡦࡴ࠱ࡿࢂ࠴࡯ࡱࡶ࡬ࡳࡳࡹࠧक़").format(browser)
      name = bstack111ll1l_opy_ (u"࠭ࡏࡱࡶ࡬ࡳࡳࡹࠧख़")
      browser_options = getattr(__import__(package, fromlist=[name]), name)
      options = browser_options()
      if not bstack11l11l1l1_opy_(options):
        return None
      for bstack1ll11l1l_opy_ in caps.keys():
        options.set_capability(bstack1ll11l1l_opy_, caps[bstack1ll11l1l_opy_])
      bstack1111ll1ll_opy_(options, caps)
      return options
    except Exception as e:
      logger.debug(str(e))
      return None
def bstack1lll1111_opy_(options, bstack1llll1111l_opy_):
  if not bstack11l11l1l1_opy_(options):
    return
  for bstack1ll11l1l_opy_ in bstack1llll1111l_opy_.keys():
    if bstack1ll11l1l_opy_ in bstack1ll11lll1l_opy_:
      continue
    if bstack1ll11l1l_opy_ in options._caps and type(options._caps[bstack1ll11l1l_opy_]) in [dict, list]:
      options._caps[bstack1ll11l1l_opy_] = update(options._caps[bstack1ll11l1l_opy_], bstack1llll1111l_opy_[bstack1ll11l1l_opy_])
    else:
      options.set_capability(bstack1ll11l1l_opy_, bstack1llll1111l_opy_[bstack1ll11l1l_opy_])
  bstack1111ll1ll_opy_(options, bstack1llll1111l_opy_)
  if bstack111ll1l_opy_ (u"ࠧ࡮ࡱࡽ࠾ࡩ࡫ࡢࡶࡩࡪࡩࡷࡇࡤࡥࡴࡨࡷࡸ࠭ग़") in options._caps:
    if options._caps[bstack111ll1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡐࡤࡱࡪ࠭ज़")] and options._caps[bstack111ll1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡑࡥࡲ࡫ࠧड़")].lower() != bstack111ll1l_opy_ (u"ࠪࡪ࡮ࡸࡥࡧࡱࡻࠫढ़"):
      del options._caps[bstack111ll1l_opy_ (u"ࠫࡲࡵࡺ࠻ࡦࡨࡦࡺ࡭ࡧࡦࡴࡄࡨࡩࡸࡥࡴࡵࠪफ़")]
def bstack1ll1llll1l_opy_(proxy_config):
  if bstack111ll1l_opy_ (u"ࠬ࡮ࡴࡵࡲࡶࡔࡷࡵࡸࡺࠩय़") in proxy_config:
    proxy_config[bstack111ll1l_opy_ (u"࠭ࡳࡴ࡮ࡓࡶࡴࡾࡹࠨॠ")] = proxy_config[bstack111ll1l_opy_ (u"ࠧࡩࡶࡷࡴࡸࡖࡲࡰࡺࡼࠫॡ")]
    del (proxy_config[bstack111ll1l_opy_ (u"ࠨࡪࡷࡸࡵࡹࡐࡳࡱࡻࡽࠬॢ")])
  if bstack111ll1l_opy_ (u"ࠩࡳࡶࡴࡾࡹࡕࡻࡳࡩࠬॣ") in proxy_config and proxy_config[bstack111ll1l_opy_ (u"ࠪࡴࡷࡵࡸࡺࡖࡼࡴࡪ࠭।")].lower() != bstack111ll1l_opy_ (u"ࠫࡩ࡯ࡲࡦࡥࡷࠫ॥"):
    proxy_config[bstack111ll1l_opy_ (u"ࠬࡶࡲࡰࡺࡼࡘࡾࡶࡥࠨ०")] = bstack111ll1l_opy_ (u"࠭࡭ࡢࡰࡸࡥࡱ࠭१")
  if bstack111ll1l_opy_ (u"ࠧࡱࡴࡲࡼࡾࡇࡵࡵࡱࡦࡳࡳ࡬ࡩࡨࡗࡵࡰࠬ२") in proxy_config:
    proxy_config[bstack111ll1l_opy_ (u"ࠨࡲࡵࡳࡽࡿࡔࡺࡲࡨࠫ३")] = bstack111ll1l_opy_ (u"ࠩࡳࡥࡨ࠭४")
  return proxy_config
def bstack111l1lll_opy_(config, proxy):
  from selenium.webdriver.common.proxy import Proxy
  if not bstack111ll1l_opy_ (u"ࠪࡴࡷࡵࡸࡺࠩ५") in config:
    return proxy
  config[bstack111ll1l_opy_ (u"ࠫࡵࡸ࡯ࡹࡻࠪ६")] = bstack1ll1llll1l_opy_(config[bstack111ll1l_opy_ (u"ࠬࡶࡲࡰࡺࡼࠫ७")])
  if proxy == None:
    proxy = Proxy(config[bstack111ll1l_opy_ (u"࠭ࡰࡳࡱࡻࡽࠬ८")])
  return proxy
def bstack1l11l111_opy_(self):
  global CONFIG
  global bstack1111l1111_opy_
  try:
    proxy = bstack1l1ll11ll_opy_(CONFIG)
    if proxy:
      if proxy.endswith(bstack111ll1l_opy_ (u"ࠧ࠯ࡲࡤࡧࠬ९")):
        proxies = bstack1l1l1l111_opy_(proxy, bstack111111111_opy_())
        if len(proxies) > 0:
          protocol, bstack1lllll1111_opy_ = proxies.popitem()
          if bstack111ll1l_opy_ (u"ࠣ࠼࠲࠳ࠧ॰") in bstack1lllll1111_opy_:
            return bstack1lllll1111_opy_
          else:
            return bstack111ll1l_opy_ (u"ࠤ࡫ࡸࡹࡶ࠺࠰࠱ࠥॱ") + bstack1lllll1111_opy_
      else:
        return proxy
  except Exception as e:
    logger.error(bstack111ll1l_opy_ (u"ࠥࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥࡹࡥࡵࡶ࡬ࡲ࡬ࠦࡰࡳࡱࡻࡽࠥࡻࡲ࡭ࠢ࠽ࠤࢀࢃࠢॲ").format(str(e)))
  return bstack1111l1111_opy_(self)
def bstack1l1l1l1l_opy_():
  global CONFIG
  return bstack1l1l1ll11_opy_(CONFIG) and bstack1ll11l11l_opy_() and bstack1lllll1l1l_opy_() >= version.parse(bstack1llll11l1l_opy_)
def bstack1ll1ll11l_opy_():
  global CONFIG
  return (bstack111ll1l_opy_ (u"ࠫ࡭ࡺࡴࡱࡒࡵࡳࡽࡿࠧॳ") in CONFIG or bstack111ll1l_opy_ (u"ࠬ࡮ࡴࡵࡲࡶࡔࡷࡵࡸࡺࠩॴ") in CONFIG) and bstack111l11ll_opy_()
def bstack11l11l11l_opy_(config):
  bstack1ll1lllll1_opy_ = {}
  if bstack111ll1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪॵ") in config:
    bstack1ll1lllll1_opy_ = config[bstack111ll1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫॶ")]
  if bstack111ll1l_opy_ (u"ࠨ࡮ࡲࡧࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧॷ") in config:
    bstack1ll1lllll1_opy_ = config[bstack111ll1l_opy_ (u"ࠩ࡯ࡳࡨࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨॸ")]
  proxy = bstack1l1ll11ll_opy_(config)
  if proxy:
    if proxy.endswith(bstack111ll1l_opy_ (u"ࠪ࠲ࡵࡧࡣࠨॹ")) and os.path.isfile(proxy):
      bstack1ll1lllll1_opy_[bstack111ll1l_opy_ (u"ࠫ࠲ࡶࡡࡤ࠯ࡩ࡭ࡱ࡫ࠧॺ")] = proxy
    else:
      parsed_url = None
      if proxy.endswith(bstack111ll1l_opy_ (u"ࠬ࠴ࡰࡢࡥࠪॻ")):
        proxies = bstack11ll1l1ll_opy_(config, bstack111111111_opy_())
        if len(proxies) > 0:
          protocol, bstack1lllll1111_opy_ = proxies.popitem()
          if bstack111ll1l_opy_ (u"ࠨ࠺࠰࠱ࠥॼ") in bstack1lllll1111_opy_:
            parsed_url = urlparse(bstack1lllll1111_opy_)
          else:
            parsed_url = urlparse(protocol + bstack111ll1l_opy_ (u"ࠢ࠻࠱࠲ࠦॽ") + bstack1lllll1111_opy_)
      else:
        parsed_url = urlparse(proxy)
      if parsed_url and parsed_url.hostname: bstack1ll1lllll1_opy_[bstack111ll1l_opy_ (u"ࠨࡲࡵࡳࡽࡿࡈࡰࡵࡷࠫॾ")] = str(parsed_url.hostname)
      if parsed_url and parsed_url.port: bstack1ll1lllll1_opy_[bstack111ll1l_opy_ (u"ࠩࡳࡶࡴࡾࡹࡑࡱࡵࡸࠬॿ")] = str(parsed_url.port)
      if parsed_url and parsed_url.username: bstack1ll1lllll1_opy_[bstack111ll1l_opy_ (u"ࠪࡴࡷࡵࡸࡺࡗࡶࡩࡷ࠭ঀ")] = str(parsed_url.username)
      if parsed_url and parsed_url.password: bstack1ll1lllll1_opy_[bstack111ll1l_opy_ (u"ࠫࡵࡸ࡯ࡹࡻࡓࡥࡸࡹࠧঁ")] = str(parsed_url.password)
  return bstack1ll1lllll1_opy_
def bstack1l1llll1l_opy_(config):
  if bstack111ll1l_opy_ (u"ࠬࡺࡥࡴࡶࡆࡳࡳࡺࡥࡹࡶࡒࡴࡹ࡯࡯࡯ࡵࠪং") in config:
    return config[bstack111ll1l_opy_ (u"࠭ࡴࡦࡵࡷࡇࡴࡴࡴࡦࡺࡷࡓࡵࡺࡩࡰࡰࡶࠫঃ")]
  return {}
def bstack11l11111l_opy_(caps):
  global bstack11l11llll_opy_
  if bstack111ll1l_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࠺ࡰࡲࡷ࡭ࡴࡴࡳࠨ঄") in caps:
    caps[bstack111ll1l_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫࠻ࡱࡳࡸ࡮ࡵ࡮ࡴࠩঅ")][bstack111ll1l_opy_ (u"ࠩ࡯ࡳࡨࡧ࡬ࠨআ")] = True
    if bstack11l11llll_opy_:
      caps[bstack111ll1l_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭࠽ࡳࡵࡺࡩࡰࡰࡶࠫই")][bstack111ll1l_opy_ (u"ࠫࡱࡵࡣࡢ࡮ࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭ঈ")] = bstack11l11llll_opy_
  else:
    caps[bstack111ll1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡱࡵࡣࡢ࡮ࠪউ")] = True
    if bstack11l11llll_opy_:
      caps[bstack111ll1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡲ࡯ࡤࡣ࡯ࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧঊ")] = bstack11l11llll_opy_
def bstack1ll1l1l1_opy_():
  global CONFIG
  if bstack111ll1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࠫঋ") in CONFIG and CONFIG[bstack111ll1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡌࡰࡥࡤࡰࠬঌ")]:
    bstack1ll1lllll1_opy_ = bstack11l11l11l_opy_(CONFIG)
    bstack11ll11lll_opy_(CONFIG[bstack111ll1l_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴࡍࡨࡽࠬ঍")], bstack1ll1lllll1_opy_)
def bstack11ll11lll_opy_(key, bstack1ll1lllll1_opy_):
  global bstack1ll1ll111_opy_
  logger.info(bstack1l11ll1l1_opy_)
  try:
    bstack1ll1ll111_opy_ = Local()
    bstack11ll1llll_opy_ = {bstack111ll1l_opy_ (u"ࠪ࡯ࡪࡿࠧ঎"): key}
    bstack11ll1llll_opy_.update(bstack1ll1lllll1_opy_)
    logger.debug(bstack111ll11ll_opy_.format(str(bstack11ll1llll_opy_)))
    bstack1ll1ll111_opy_.start(**bstack11ll1llll_opy_)
    if bstack1ll1ll111_opy_.isRunning():
      logger.info(bstack1lll1llll_opy_)
  except Exception as e:
    bstack1ll11l111_opy_(bstack1111l1l1_opy_.format(str(e)))
def bstack1llll1l11_opy_():
  global bstack1ll1ll111_opy_
  if bstack1ll1ll111_opy_.isRunning():
    logger.info(bstack11111l111_opy_)
    bstack1ll1ll111_opy_.stop()
  bstack1ll1ll111_opy_ = None
def bstack1llll111l_opy_(bstack111llllll_opy_=[]):
  global CONFIG
  bstack1llll11l1_opy_ = []
  bstack1ll11l11_opy_ = [bstack111ll1l_opy_ (u"ࠫࡴࡹࠧএ"), bstack111ll1l_opy_ (u"ࠬࡵࡳࡗࡧࡵࡷ࡮ࡵ࡮ࠨঐ"), bstack111ll1l_opy_ (u"࠭ࡤࡦࡸ࡬ࡧࡪࡔࡡ࡮ࡧࠪ঑"), bstack111ll1l_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡘࡨࡶࡸ࡯࡯࡯ࠩ঒"), bstack111ll1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡐࡤࡱࡪ࠭ও"), bstack111ll1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪঔ")]
  try:
    for err in bstack111llllll_opy_:
      bstack111l111l_opy_ = {}
      for k in bstack1ll11l11_opy_:
        val = CONFIG[bstack111ll1l_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ক")][int(err[bstack111ll1l_opy_ (u"ࠫ࡮ࡴࡤࡦࡺࠪখ")])].get(k)
        if val:
          bstack111l111l_opy_[k] = val
      bstack111l111l_opy_[bstack111ll1l_opy_ (u"ࠬࡺࡥࡴࡶࡶࠫগ")] = {
        err[bstack111ll1l_opy_ (u"࠭࡮ࡢ࡯ࡨࠫঘ")]: err[bstack111ll1l_opy_ (u"ࠧࡦࡴࡵࡳࡷ࠭ঙ")]
      }
      bstack1llll11l1_opy_.append(bstack111l111l_opy_)
  except Exception as e:
    logger.debug(bstack111ll1l_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡪࡰࠣࡪࡴࡸ࡭ࡢࡶࡷ࡭ࡳ࡭ࠠࡥࡣࡷࡥࠥ࡬࡯ࡳࠢࡨࡺࡪࡴࡴ࠻ࠢࠪচ") + str(e))
  finally:
    return bstack1llll11l1_opy_
def bstack11l11lll1_opy_():
  global bstack1lll1ll1ll_opy_
  global bstack1lll1l11l1_opy_
  global bstack1llll111l1_opy_
  percy.shutdown()
  if bstack1lll1ll1ll_opy_:
    logger.warning(bstack111l11111_opy_.format(str(bstack1lll1ll1ll_opy_)))
  else:
    try:
      bstack111l111l1_opy_ = bstack1lll11l11_opy_(bstack111ll1l_opy_ (u"ࠩ࠱ࡦࡸࡺࡡࡤ࡭࠰ࡧࡴࡴࡦࡪࡩ࠱࡮ࡸࡵ࡮ࠨছ"), logger)
      if bstack111l111l1_opy_.get(bstack111ll1l_opy_ (u"ࠪࡲࡺࡪࡧࡦࡡ࡯ࡳࡨࡧ࡬ࠨজ")) and bstack111l111l1_opy_.get(bstack111ll1l_opy_ (u"ࠫࡳࡻࡤࡨࡧࡢࡰࡴࡩࡡ࡭ࠩঝ")).get(bstack111ll1l_opy_ (u"ࠬ࡮࡯ࡴࡶࡱࡥࡲ࡫ࠧঞ")):
        logger.warning(bstack111l11111_opy_.format(str(bstack111l111l1_opy_[bstack111ll1l_opy_ (u"࠭࡮ࡶࡦࡪࡩࡤࡲ࡯ࡤࡣ࡯ࠫট")][bstack111ll1l_opy_ (u"ࠧࡩࡱࡶࡸࡳࡧ࡭ࡦࠩঠ")])))
    except Exception as e:
      logger.error(e)
  logger.info(bstack11lll111l_opy_)
  global bstack1ll1ll111_opy_
  if bstack1ll1ll111_opy_:
    bstack1llll1l11_opy_()
  try:
    for driver in bstack1lll1l11l1_opy_:
      driver.quit()
  except Exception as e:
    pass
  logger.info(bstack1111l11l_opy_)
  bstack1lllll111l_opy_()
  if len(bstack1llll111l1_opy_) > 0:
    message = bstack1llll111l_opy_(bstack1llll111l1_opy_)
    bstack1lllll111l_opy_(message)
  else:
    bstack1lllll111l_opy_()
  bstack1lllll11l_opy_(bstack11lll11ll_opy_, logger)
def bstack1l1ll11l_opy_(self, *args):
  logger.error(bstack11ll11l1_opy_)
  bstack11l11lll1_opy_()
  sys.exit(1)
def bstack1ll11l111_opy_(err):
  logger.critical(bstack11lll1111_opy_.format(str(err)))
  bstack1lllll111l_opy_(bstack11lll1111_opy_.format(str(err)))
  atexit.unregister(bstack11l11lll1_opy_)
  sys.exit(1)
def bstack1l1lll111_opy_(error, message):
  logger.critical(str(error))
  logger.critical(message)
  bstack1lllll111l_opy_(message)
  atexit.unregister(bstack11l11lll1_opy_)
  sys.exit(1)
def bstack1l1llllll_opy_():
  global CONFIG
  global bstack1ll1lll11_opy_
  global bstack1ll1llll11_opy_
  global bstack1l111111l_opy_
  CONFIG = bstack1l1111lll_opy_()
  bstack1l11l1ll1_opy_()
  bstack1l11l1ll_opy_()
  CONFIG = bstack1ll1l1111l_opy_(CONFIG)
  update(CONFIG, bstack1ll1llll11_opy_)
  update(CONFIG, bstack1ll1lll11_opy_)
  CONFIG = bstack11lllll11_opy_(CONFIG)
  bstack1l111111l_opy_ = bstack1ll1111ll_opy_(CONFIG)
  bstack1ll1l1llll_opy_.bstack1ll1lll111_opy_(bstack111ll1l_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡠࡵࡨࡷࡸ࡯࡯࡯ࠩড"), bstack1l111111l_opy_)
  if (bstack111ll1l_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠬঢ") in CONFIG and bstack111ll1l_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡐࡤࡱࡪ࠭ণ") in bstack1ll1lll11_opy_) or (
          bstack111ll1l_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧত") in CONFIG and bstack111ll1l_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡒࡦࡳࡥࠨথ") not in bstack1ll1llll11_opy_):
    if os.getenv(bstack111ll1l_opy_ (u"࠭ࡂࡔࡖࡄࡇࡐࡥࡃࡐࡏࡅࡍࡓࡋࡄࡠࡄࡘࡍࡑࡊ࡟ࡊࡆࠪদ")):
      CONFIG[bstack111ll1l_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩধ")] = os.getenv(bstack111ll1l_opy_ (u"ࠨࡄࡖࡘࡆࡉࡋࡠࡅࡒࡑࡇࡏࡎࡆࡆࡢࡆ࡚ࡏࡌࡅࡡࡌࡈࠬন"))
    else:
      bstack111lll1ll_opy_()
  elif (bstack111ll1l_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠬ঩") not in CONFIG and bstack111ll1l_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬপ") in CONFIG) or (
          bstack111ll1l_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧফ") in bstack1ll1llll11_opy_ and bstack111ll1l_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡒࡦࡳࡥࠨব") not in bstack1ll1lll11_opy_):
    del (CONFIG[bstack111ll1l_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨভ")])
  if bstack11l111ll1_opy_(CONFIG):
    bstack1ll11l111_opy_(bstack1111ll1l1_opy_)
  bstack1l111l11_opy_()
  bstack111llll1l_opy_()
  if bstack111l1l1ll_opy_:
    CONFIG[bstack111ll1l_opy_ (u"ࠧࡢࡲࡳࠫম")] = bstack1111l1lll_opy_(CONFIG)
    logger.info(bstack11l1l111l_opy_.format(CONFIG[bstack111ll1l_opy_ (u"ࠨࡣࡳࡴࠬয")]))
def bstack1llll1l11l_opy_(config, bstack11l1ll111_opy_):
  global CONFIG
  global bstack111l1l1ll_opy_
  CONFIG = config
  bstack111l1l1ll_opy_ = bstack11l1ll111_opy_
def bstack111llll1l_opy_():
  global CONFIG
  global bstack111l1l1ll_opy_
  if bstack111ll1l_opy_ (u"ࠩࡤࡴࡵ࠭র") in CONFIG:
    try:
      from appium import version
    except Exception as e:
      bstack1l1lll111_opy_(e, bstack1llll11l11_opy_)
    bstack111l1l1ll_opy_ = True
    bstack1ll1l1llll_opy_.bstack1ll1lll111_opy_(bstack111ll1l_opy_ (u"ࠪࡥࡵࡶ࡟ࡢࡷࡷࡳࡲࡧࡴࡦࠩ঱"), True)
def bstack1111l1lll_opy_(config):
  bstack1llll1llll_opy_ = bstack111ll1l_opy_ (u"ࠫࠬল")
  app = config[bstack111ll1l_opy_ (u"ࠬࡧࡰࡱࠩ঳")]
  if isinstance(app, str):
    if os.path.splitext(app)[1] in bstack1lllll11l1_opy_:
      if os.path.exists(app):
        bstack1llll1llll_opy_ = bstack1ll111ll1_opy_(config, app)
      elif bstack1lll11111_opy_(app):
        bstack1llll1llll_opy_ = app
      else:
        bstack1ll11l111_opy_(bstack1llll11ll1_opy_.format(app))
    else:
      if bstack1lll11111_opy_(app):
        bstack1llll1llll_opy_ = app
      elif os.path.exists(app):
        bstack1llll1llll_opy_ = bstack1ll111ll1_opy_(app)
      else:
        bstack1ll11l111_opy_(bstack11111l1l_opy_)
  else:
    if len(app) > 2:
      bstack1ll11l111_opy_(bstack1lll11l1ll_opy_)
    elif len(app) == 2:
      if bstack111ll1l_opy_ (u"࠭ࡰࡢࡶ࡫ࠫ঴") in app and bstack111ll1l_opy_ (u"ࠧࡤࡷࡶࡸࡴࡳ࡟ࡪࡦࠪ঵") in app:
        if os.path.exists(app[bstack111ll1l_opy_ (u"ࠨࡲࡤࡸ࡭࠭শ")]):
          bstack1llll1llll_opy_ = bstack1ll111ll1_opy_(config, app[bstack111ll1l_opy_ (u"ࠩࡳࡥࡹ࡮ࠧষ")], app[bstack111ll1l_opy_ (u"ࠪࡧࡺࡹࡴࡰ࡯ࡢ࡭ࡩ࠭স")])
        else:
          bstack1ll11l111_opy_(bstack1llll11ll1_opy_.format(app))
      else:
        bstack1ll11l111_opy_(bstack1lll11l1ll_opy_)
    else:
      for key in app:
        if key in bstack11l11111_opy_:
          if key == bstack111ll1l_opy_ (u"ࠫࡵࡧࡴࡩࠩহ"):
            if os.path.exists(app[key]):
              bstack1llll1llll_opy_ = bstack1ll111ll1_opy_(config, app[key])
            else:
              bstack1ll11l111_opy_(bstack1llll11ll1_opy_.format(app))
          else:
            bstack1llll1llll_opy_ = app[key]
        else:
          bstack1ll11l111_opy_(bstack1l1l1111l_opy_)
  return bstack1llll1llll_opy_
def bstack1lll11111_opy_(bstack1llll1llll_opy_):
  import re
  bstack1l111lll_opy_ = re.compile(bstack111ll1l_opy_ (u"ࡷࠨ࡞࡜ࡣ࠰ࡾࡆ࠳࡚࠱࠯࠼ࡠࡤ࠴࡜࠮࡟࠭ࠨࠧ঺"))
  bstack1111l11l1_opy_ = re.compile(bstack111ll1l_opy_ (u"ࡸࠢ࡟࡝ࡤ࠱ࡿࡇ࡛࠭࠲࠰࠽ࡡࡥ࠮࡝࠯ࡠ࠮࠴ࡡࡡ࠮ࡼࡄ࠱࡟࠶࠭࠺࡞ࡢ࠲ࡡ࠳࡝ࠫࠦࠥ঻"))
  if bstack111ll1l_opy_ (u"ࠧࡣࡵ࠽࠳࠴়࠭") in bstack1llll1llll_opy_ or re.fullmatch(bstack1l111lll_opy_, bstack1llll1llll_opy_) or re.fullmatch(bstack1111l11l1_opy_, bstack1llll1llll_opy_):
    return True
  else:
    return False
def bstack1ll111ll1_opy_(config, path, bstack1l111llll_opy_=None):
  import requests
  from requests_toolbelt.multipart.encoder import MultipartEncoder
  import hashlib
  md5_hash = hashlib.md5(open(os.path.abspath(path), bstack111ll1l_opy_ (u"ࠨࡴࡥࠫঽ")).read()).hexdigest()
  bstack1ll1l11ll_opy_ = bstack1lll11ll1l_opy_(md5_hash)
  bstack1llll1llll_opy_ = None
  if bstack1ll1l11ll_opy_:
    logger.info(bstack1ll1ll1ll_opy_.format(bstack1ll1l11ll_opy_, md5_hash))
    return bstack1ll1l11ll_opy_
  bstack1ll11ll111_opy_ = MultipartEncoder(
    fields={
      bstack111ll1l_opy_ (u"ࠩࡩ࡭ࡱ࡫ࠧা"): (os.path.basename(path), open(os.path.abspath(path), bstack111ll1l_opy_ (u"ࠪࡶࡧ࠭ি")), bstack111ll1l_opy_ (u"ࠫࡹ࡫ࡸࡵ࠱ࡳࡰࡦ࡯࡮ࠨী")),
      bstack111ll1l_opy_ (u"ࠬࡩࡵࡴࡶࡲࡱࡤ࡯ࡤࠨু"): bstack1l111llll_opy_
    }
  )
  response = requests.post(bstack1lll111l1_opy_, data=bstack1ll11ll111_opy_,
                           headers={bstack111ll1l_opy_ (u"࠭ࡃࡰࡰࡷࡩࡳࡺ࠭ࡕࡻࡳࡩࠬূ"): bstack1ll11ll111_opy_.content_type},
                           auth=(config[bstack111ll1l_opy_ (u"ࠧࡶࡵࡨࡶࡓࡧ࡭ࡦࠩৃ")], config[bstack111ll1l_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡌࡧࡼࠫৄ")]))
  try:
    res = json.loads(response.text)
    bstack1llll1llll_opy_ = res[bstack111ll1l_opy_ (u"ࠩࡤࡴࡵࡥࡵࡳ࡮ࠪ৅")]
    logger.info(bstack1lll1l1l1l_opy_.format(bstack1llll1llll_opy_))
    bstack1lll1ll11l_opy_(md5_hash, bstack1llll1llll_opy_)
  except ValueError as err:
    bstack1ll11l111_opy_(bstack1111lll11_opy_.format(str(err)))
  return bstack1llll1llll_opy_
def bstack1l111l11_opy_():
  global CONFIG
  global bstack1l1111111_opy_
  bstack1ll1lllll_opy_ = 0
  bstack111111ll1_opy_ = 1
  if bstack111ll1l_opy_ (u"ࠪࡴࡦࡸࡡ࡭࡮ࡨࡰࡸࡖࡥࡳࡒ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪ৆") in CONFIG:
    bstack111111ll1_opy_ = CONFIG[bstack111ll1l_opy_ (u"ࠫࡵࡧࡲࡢ࡮࡯ࡩࡱࡹࡐࡦࡴࡓࡰࡦࡺࡦࡰࡴࡰࠫে")]
  if bstack111ll1l_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨৈ") in CONFIG:
    bstack1ll1lllll_opy_ = len(CONFIG[bstack111ll1l_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ৉")])
  bstack1l1111111_opy_ = int(bstack111111ll1_opy_) * int(bstack1ll1lllll_opy_)
def bstack1lll11ll1l_opy_(md5_hash):
  bstack1lll1lll1l_opy_ = os.path.join(os.path.expanduser(bstack111ll1l_opy_ (u"ࠧࡿࠩ৊")), bstack111ll1l_opy_ (u"ࠨ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠨো"), bstack111ll1l_opy_ (u"ࠩࡤࡴࡵ࡛ࡰ࡭ࡱࡤࡨࡒࡊ࠵ࡉࡣࡶ࡬࠳ࡰࡳࡰࡰࠪৌ"))
  if os.path.exists(bstack1lll1lll1l_opy_):
    bstack1ll1l1l1l1_opy_ = json.load(open(bstack1lll1lll1l_opy_, bstack111ll1l_opy_ (u"ࠪࡶࡧ্࠭")))
    if md5_hash in bstack1ll1l1l1l1_opy_:
      bstack11l1lllll_opy_ = bstack1ll1l1l1l1_opy_[md5_hash]
      bstack11l1l1l11_opy_ = datetime.datetime.now()
      bstack1ll1l11lll_opy_ = datetime.datetime.strptime(bstack11l1lllll_opy_[bstack111ll1l_opy_ (u"ࠫࡹ࡯࡭ࡦࡵࡷࡥࡲࡶࠧৎ")], bstack111ll1l_opy_ (u"ࠬࠫࡤ࠰ࠧࡰ࠳ࠪ࡟ࠠࠦࡊ࠽ࠩࡒࡀࠥࡔࠩ৏"))
      if (bstack11l1l1l11_opy_ - bstack1ll1l11lll_opy_).days > 30:
        return None
      elif version.parse(str(__version__)) > version.parse(bstack11l1lllll_opy_[bstack111ll1l_opy_ (u"࠭ࡳࡥ࡭ࡢࡺࡪࡸࡳࡪࡱࡱࠫ৐")]):
        return None
      return bstack11l1lllll_opy_[bstack111ll1l_opy_ (u"ࠧࡪࡦࠪ৑")]
  else:
    return None
def bstack1lll1ll11l_opy_(md5_hash, bstack1llll1llll_opy_):
  bstack11111111_opy_ = os.path.join(os.path.expanduser(bstack111ll1l_opy_ (u"ࠨࢀࠪ৒")), bstack111ll1l_opy_ (u"ࠩ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠩ৓"))
  if not os.path.exists(bstack11111111_opy_):
    os.makedirs(bstack11111111_opy_)
  bstack1lll1lll1l_opy_ = os.path.join(os.path.expanduser(bstack111ll1l_opy_ (u"ࠪࢂࠬ৔")), bstack111ll1l_opy_ (u"ࠫ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠫ৕"), bstack111ll1l_opy_ (u"ࠬࡧࡰࡱࡗࡳࡰࡴࡧࡤࡎࡆ࠸ࡌࡦࡹࡨ࠯࡬ࡶࡳࡳ࠭৖"))
  bstack1lllllll11_opy_ = {
    bstack111ll1l_opy_ (u"࠭ࡩࡥࠩৗ"): bstack1llll1llll_opy_,
    bstack111ll1l_opy_ (u"ࠧࡵ࡫ࡰࡩࡸࡺࡡ࡮ࡲࠪ৘"): datetime.datetime.strftime(datetime.datetime.now(), bstack111ll1l_opy_ (u"ࠨࠧࡧ࠳ࠪࡳ࠯࡛ࠦࠣࠩࡍࡀࠥࡎ࠼ࠨࡗࠬ৙")),
    bstack111ll1l_opy_ (u"ࠩࡶࡨࡰࡥࡶࡦࡴࡶ࡭ࡴࡴࠧ৚"): str(__version__)
  }
  if os.path.exists(bstack1lll1lll1l_opy_):
    bstack1ll1l1l1l1_opy_ = json.load(open(bstack1lll1lll1l_opy_, bstack111ll1l_opy_ (u"ࠪࡶࡧ࠭৛")))
  else:
    bstack1ll1l1l1l1_opy_ = {}
  bstack1ll1l1l1l1_opy_[md5_hash] = bstack1lllllll11_opy_
  with open(bstack1lll1lll1l_opy_, bstack111ll1l_opy_ (u"ࠦࡼ࠱ࠢড়")) as outfile:
    json.dump(bstack1ll1l1l1l1_opy_, outfile)
def bstack11l1l11l1_opy_(self):
  return
def bstack11l111ll_opy_(self):
  return
def bstack11l1l1ll_opy_(self):
  from selenium.webdriver.remote.webdriver import WebDriver
  WebDriver.quit(self)
def bstack11l1l11ll_opy_(self):
  global bstack111111lll_opy_
  global bstack1l1l1l1l1_opy_
  global bstack1ll1l111ll_opy_
  try:
    if bstack111ll1l_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬঢ়") in bstack111111lll_opy_ and self.session_id != None and bstack11l11l11_opy_(threading.current_thread(), bstack111ll1l_opy_ (u"࠭ࡴࡦࡵࡷࡗࡹࡧࡴࡶࡵࠪ৞"), bstack111ll1l_opy_ (u"ࠧࠨয়")) != bstack111ll1l_opy_ (u"ࠨࡵ࡮࡭ࡵࡶࡥࡥࠩৠ"):
      bstack111l11l1l_opy_ = bstack111ll1l_opy_ (u"ࠩࡳࡥࡸࡹࡥࡥࠩৡ") if len(threading.current_thread().bstackTestErrorMessages) == 0 else bstack111ll1l_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪৢ")
      bstack11ll11ll_opy_ = bstack1l1ll1111_opy_(bstack111ll1l_opy_ (u"ࠫࡸ࡫ࡴࡔࡧࡶࡷ࡮ࡵ࡮ࡔࡶࡤࡸࡺࡹࠧৣ"), bstack111ll1l_opy_ (u"ࠬ࠭৤"), bstack111l11l1l_opy_, bstack111ll1l_opy_ (u"࠭ࠬࠡࠩ৥").join(
        threading.current_thread().bstackTestErrorMessages), bstack111ll1l_opy_ (u"ࠧࠨ০"), bstack111ll1l_opy_ (u"ࠨࠩ১"))
      if self != None:
        self.execute_script(bstack11ll11ll_opy_)
  except Exception as e:
    logger.debug(bstack111ll1l_opy_ (u"ࠤࡈࡶࡷࡵࡲࠡࡹ࡫࡭ࡱ࡫ࠠ࡮ࡣࡵ࡯࡮ࡴࡧࠡࡵࡷࡥࡹࡻࡳ࠻ࠢࠥ২") + str(e))
  bstack1ll1l111ll_opy_(self)
  self.session_id = None
def bstack11ll11l11_opy_(self, *args, **kwargs):
  bstack1111llll_opy_ = bstack11lll1l11_opy_(self, *args, **kwargs)
  bstack1l11lll1l_opy_.bstack1lll1111l_opy_(self)
  return bstack1111llll_opy_
def bstack11lll1l1_opy_(self, command_executor,
             desired_capabilities=None, browser_profile=None, proxy=None,
             keep_alive=True, file_detector=None, options=None):
  global CONFIG
  global bstack1l1l1l1l1_opy_
  global bstack1111ll11l_opy_
  global bstack1111llll1_opy_
  global bstack1l11ll1l_opy_
  global bstack11111l1l1_opy_
  global bstack111111lll_opy_
  global bstack11lll1l11_opy_
  global bstack1lll1l11l1_opy_
  global bstack111lll11l_opy_
  CONFIG[bstack111ll1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡕࡇࡏࠬ৩")] = str(bstack111111lll_opy_) + str(__version__)
  command_executor = bstack111111111_opy_()
  logger.debug(bstack11ll1l11_opy_.format(command_executor))
  proxy = bstack111l1lll_opy_(CONFIG, proxy)
  bstack1lll1l11l_opy_ = 0 if bstack1111ll11l_opy_ < 0 else bstack1111ll11l_opy_
  try:
    if bstack1l11ll1l_opy_ is True:
      bstack1lll1l11l_opy_ = int(multiprocessing.current_process().name)
    elif bstack11111l1l1_opy_ is True:
      bstack1lll1l11l_opy_ = int(threading.current_thread().name)
  except:
    bstack1lll1l11l_opy_ = 0
  bstack1llll1111l_opy_ = bstack1lllllll1l_opy_(CONFIG, bstack1lll1l11l_opy_)
  logger.debug(bstack1ll1ll1l1_opy_.format(str(bstack1llll1111l_opy_)))
  if bstack111ll1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࠨ৪") in CONFIG and CONFIG[bstack111ll1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࠩ৫")]:
    bstack11l11111l_opy_(bstack1llll1111l_opy_)
  if desired_capabilities:
    bstack1lll1lll_opy_ = bstack1ll1l1111l_opy_(desired_capabilities)
    bstack1lll1lll_opy_[bstack111ll1l_opy_ (u"࠭ࡵࡴࡧ࡚࠷ࡈ࠭৬")] = bstack1111lll1_opy_(CONFIG)
    bstack111ll111l_opy_ = bstack1lllllll1l_opy_(bstack1lll1lll_opy_)
    if bstack111ll111l_opy_:
      bstack1llll1111l_opy_ = update(bstack111ll111l_opy_, bstack1llll1111l_opy_)
    desired_capabilities = None
  if options:
    bstack1lll1111_opy_(options, bstack1llll1111l_opy_)
  if not options:
    options = bstack1ll11111l_opy_(bstack1llll1111l_opy_)
  if bstack111l1l11l_opy_.bstack1lll1l11_opy_(CONFIG, bstack1lll1l11l_opy_) and bstack111l1l11l_opy_.bstack1ll1ll1l_opy_(bstack1llll1111l_opy_, options):
    bstack111l1l11l_opy_.set_capabilities(bstack1llll1111l_opy_, CONFIG)
  if proxy and bstack1lllll1l1l_opy_() >= version.parse(bstack111ll1l_opy_ (u"ࠧ࠵࠰࠴࠴࠳࠶ࠧ৭")):
    options.proxy(proxy)
  if options and bstack1lllll1l1l_opy_() >= version.parse(bstack111ll1l_opy_ (u"ࠨ࠵࠱࠼࠳࠶ࠧ৮")):
    desired_capabilities = None
  if (
          not options and not desired_capabilities
  ) or (
          bstack1lllll1l1l_opy_() < version.parse(bstack111ll1l_opy_ (u"ࠩ࠶࠲࠽࠴࠰ࠨ৯")) and not desired_capabilities
  ):
    desired_capabilities = {}
    desired_capabilities.update(bstack1llll1111l_opy_)
  logger.info(bstack1lll1l1l1_opy_)
  if bstack1lllll1l1l_opy_() >= version.parse(bstack111ll1l_opy_ (u"ࠪ࠸࠳࠷࠰࠯࠲ࠪৰ")):
    bstack11lll1l11_opy_(self, command_executor=command_executor,
              options=options, keep_alive=keep_alive, file_detector=file_detector)
  elif bstack1lllll1l1l_opy_() >= version.parse(bstack111ll1l_opy_ (u"ࠫ࠸࠴࠸࠯࠲ࠪৱ")):
    bstack11lll1l11_opy_(self, command_executor=command_executor,
              desired_capabilities=desired_capabilities, options=options,
              browser_profile=browser_profile, proxy=proxy,
              keep_alive=keep_alive, file_detector=file_detector)
  elif bstack1lllll1l1l_opy_() >= version.parse(bstack111ll1l_opy_ (u"ࠬ࠸࠮࠶࠵࠱࠴ࠬ৲")):
    bstack11lll1l11_opy_(self, command_executor=command_executor,
              desired_capabilities=desired_capabilities,
              browser_profile=browser_profile, proxy=proxy,
              keep_alive=keep_alive, file_detector=file_detector)
  else:
    bstack11lll1l11_opy_(self, command_executor=command_executor,
              desired_capabilities=desired_capabilities,
              browser_profile=browser_profile, proxy=proxy,
              keep_alive=keep_alive)
  try:
    bstack11ll1111l_opy_ = bstack111ll1l_opy_ (u"࠭ࠧ৳")
    if bstack1lllll1l1l_opy_() >= version.parse(bstack111ll1l_opy_ (u"ࠧ࠵࠰࠳࠲࠵ࡨ࠱ࠨ৴")):
      bstack11ll1111l_opy_ = self.caps.get(bstack111ll1l_opy_ (u"ࠣࡱࡳࡸ࡮ࡳࡡ࡭ࡊࡸࡦ࡚ࡸ࡬ࠣ৵"))
    else:
      bstack11ll1111l_opy_ = self.capabilities.get(bstack111ll1l_opy_ (u"ࠤࡲࡴࡹ࡯࡭ࡢ࡮ࡋࡹࡧ࡛ࡲ࡭ࠤ৶"))
    if bstack11ll1111l_opy_:
      if bstack1lllll1l1l_opy_() <= version.parse(bstack111ll1l_opy_ (u"ࠪ࠷࠳࠷࠳࠯࠲ࠪ৷")):
        self.command_executor._url = bstack111ll1l_opy_ (u"ࠦ࡭ࡺࡴࡱ࠼࠲࠳ࠧ৸") + bstack1ll11111_opy_ + bstack111ll1l_opy_ (u"ࠧࡀ࠸࠱࠱ࡺࡨ࠴࡮ࡵࡣࠤ৹")
      else:
        self.command_executor._url = bstack111ll1l_opy_ (u"ࠨࡨࡵࡶࡳࡷ࠿࠵࠯ࠣ৺") + bstack11ll1111l_opy_ + bstack111ll1l_opy_ (u"ࠢ࠰ࡹࡧ࠳࡭ࡻࡢࠣ৻")
      logger.debug(bstack111l11ll1_opy_.format(bstack11ll1111l_opy_))
    else:
      logger.debug(bstack1ll1l11l1_opy_.format(bstack111ll1l_opy_ (u"ࠣࡑࡳࡸ࡮ࡳࡡ࡭ࠢࡋࡹࡧࠦ࡮ࡰࡶࠣࡪࡴࡻ࡮ࡥࠤৼ")))
  except Exception as e:
    logger.debug(bstack1ll1l11l1_opy_.format(e))
  if bstack111ll1l_opy_ (u"ࠩࡵࡳࡧࡵࡴࠨ৽") in bstack111111lll_opy_:
    bstack1lll111l11_opy_(bstack1111ll11l_opy_, bstack111lll11l_opy_)
  bstack1l1l1l1l1_opy_ = self.session_id
  if bstack111ll1l_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࠪ৾") in bstack111111lll_opy_ or bstack111ll1l_opy_ (u"ࠫࡧ࡫ࡨࡢࡸࡨࠫ৿") in bstack111111lll_opy_:
    threading.current_thread().bstack111l1111_opy_ = self.session_id
    threading.current_thread().bstackSessionDriver = self
    threading.current_thread().bstackTestErrorMessages = []
    bstack1l11lll1l_opy_.bstack1lll1111l_opy_(self)
  bstack1lll1l11l1_opy_.append(self)
  if bstack111ll1l_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ਀") in CONFIG and bstack111ll1l_opy_ (u"࠭ࡳࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠫਁ") in CONFIG[bstack111ll1l_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪਂ")][bstack1lll1l11l_opy_]:
    bstack1111llll1_opy_ = CONFIG[bstack111ll1l_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫਃ")][bstack1lll1l11l_opy_][bstack111ll1l_opy_ (u"ࠩࡶࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠧ਄")]
  logger.debug(bstack11lll11l_opy_.format(bstack1l1l1l1l1_opy_))
try:
  try:
    import Browser
    from subprocess import Popen
    def bstack1l1llll11_opy_(self, args, bufsize=-1, executable=None,
              stdin=None, stdout=None, stderr=None,
              preexec_fn=None, close_fds=True,
              shell=False, cwd=None, env=None, universal_newlines=None,
              startupinfo=None, creationflags=0,
              restore_signals=True, start_new_session=False,
              pass_fds=(), *, user=None, group=None, extra_groups=None,
              encoding=None, errors=None, text=None, umask=-1, pipesize=-1):
      global CONFIG
      global bstack1ll1l1ll1l_opy_
      if(bstack111ll1l_opy_ (u"ࠥ࡭ࡳࡪࡥࡹ࠰࡭ࡷࠧਅ") in args[1]):
        with open(os.path.join(os.path.expanduser(bstack111ll1l_opy_ (u"ࠫࢃ࠭ਆ")), bstack111ll1l_opy_ (u"ࠬ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠬਇ"), bstack111ll1l_opy_ (u"࠭࠮ࡴࡧࡶࡷ࡮ࡵ࡮ࡪࡦࡶ࠲ࡹࡾࡴࠨਈ")), bstack111ll1l_opy_ (u"ࠧࡸࠩਉ")) as fp:
          fp.write(bstack111ll1l_opy_ (u"ࠣࠤਊ"))
        if(not os.path.exists(os.path.join(os.path.dirname(args[1]), bstack111ll1l_opy_ (u"ࠤ࡬ࡲࡩ࡫ࡸࡠࡤࡶࡸࡦࡩ࡫࠯࡬ࡶࠦ਋")))):
          with open(args[1], bstack111ll1l_opy_ (u"ࠪࡶࠬ਌")) as f:
            lines = f.readlines()
            index = next((i for i, line in enumerate(lines) if bstack111ll1l_opy_ (u"ࠫࡦࡹࡹ࡯ࡥࠣࡪࡺࡴࡣࡵ࡫ࡲࡲࠥࡥ࡮ࡦࡹࡓࡥ࡬࡫ࠨࡤࡱࡱࡸࡪࡾࡴ࠭ࠢࡳࡥ࡬࡫ࠠ࠾ࠢࡹࡳ࡮ࡪࠠ࠱ࠫࠪ਍") in line), None)
            if index is not None:
                lines.insert(index+2, bstack1ll1llll1_opy_)
            lines.insert(1, bstack1l1lllll_opy_)
            f.seek(0)
            with open(os.path.join(os.path.dirname(args[1]), bstack111ll1l_opy_ (u"ࠧ࡯࡮ࡥࡧࡻࡣࡧࡹࡴࡢࡥ࡮࠲࡯ࡹࠢ਎")), bstack111ll1l_opy_ (u"࠭ࡷࠨਏ")) as bstack1l11llll1_opy_:
              bstack1l11llll1_opy_.writelines(lines)
        CONFIG[bstack111ll1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࡙ࡄࡌࠩਐ")] = str(bstack111111lll_opy_) + str(__version__)
        bstack1lll1l11l_opy_ = 0 if bstack1111ll11l_opy_ < 0 else bstack1111ll11l_opy_
        try:
          if bstack1l11ll1l_opy_ is True:
            bstack1lll1l11l_opy_ = int(multiprocessing.current_process().name)
          elif bstack11111l1l1_opy_ is True:
            bstack1lll1l11l_opy_ = int(threading.current_thread().name)
        except:
          bstack1lll1l11l_opy_ = 0
        CONFIG[bstack111ll1l_opy_ (u"ࠣࡷࡶࡩ࡜࠹ࡃࠣ਑")] = False
        CONFIG[bstack111ll1l_opy_ (u"ࠤ࡬ࡷࡕࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࠣ਒")] = True
        bstack1llll1111l_opy_ = bstack1lllllll1l_opy_(CONFIG, bstack1lll1l11l_opy_)
        logger.debug(bstack1ll1ll1l1_opy_.format(str(bstack1llll1111l_opy_)))
        if CONFIG.get(bstack111ll1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࠧਓ")):
          bstack11l11111l_opy_(bstack1llll1111l_opy_)
        if bstack111ll1l_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧਔ") in CONFIG and bstack111ll1l_opy_ (u"ࠬࡹࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠪਕ") in CONFIG[bstack111ll1l_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩਖ")][bstack1lll1l11l_opy_]:
          bstack1111llll1_opy_ = CONFIG[bstack111ll1l_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪਗ")][bstack1lll1l11l_opy_][bstack111ll1l_opy_ (u"ࠨࡵࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪ࠭ਘ")]
        args.append(os.path.join(os.path.expanduser(bstack111ll1l_opy_ (u"ࠩࢁࠫਙ")), bstack111ll1l_opy_ (u"ࠪ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠪਚ"), bstack111ll1l_opy_ (u"ࠫ࠳ࡹࡥࡴࡵ࡬ࡳࡳ࡯ࡤࡴ࠰ࡷࡼࡹ࠭ਛ")))
        args.append(str(threading.get_ident()))
        args.append(json.dumps(bstack1llll1111l_opy_))
        args[1] = os.path.join(os.path.dirname(args[1]), bstack111ll1l_opy_ (u"ࠧ࡯࡮ࡥࡧࡻࡣࡧࡹࡴࡢࡥ࡮࠲࡯ࡹࠢਜ"))
      bstack1ll1l1ll1l_opy_ = True
      return bstack11l1111ll_opy_(self, args, bufsize=bufsize, executable=executable,
                    stdin=stdin, stdout=stdout, stderr=stderr,
                    preexec_fn=preexec_fn, close_fds=close_fds,
                    shell=shell, cwd=cwd, env=env, universal_newlines=universal_newlines,
                    startupinfo=startupinfo, creationflags=creationflags,
                    restore_signals=restore_signals, start_new_session=start_new_session,
                    pass_fds=pass_fds, user=user, group=group, extra_groups=extra_groups,
                    encoding=encoding, errors=errors, text=text, umask=umask, pipesize=pipesize)
  except Exception as e:
    pass
  import playwright._impl._api_structures
  import playwright._impl._helper
  def bstack11ll11ll1_opy_(self,
        executablePath = None,
        channel = None,
        args = None,
        ignoreDefaultArgs = None,
        handleSIGINT = None,
        handleSIGTERM = None,
        handleSIGHUP = None,
        timeout = None,
        env = None,
        headless = None,
        devtools = None,
        proxy = None,
        downloadsPath = None,
        slowMo = None,
        tracesDir = None,
        chromiumSandbox = None,
        firefoxUserPrefs = None
        ):
    global CONFIG
    global bstack1111ll11l_opy_
    global bstack1111llll1_opy_
    global bstack1l11ll1l_opy_
    global bstack11111l1l1_opy_
    global bstack111111lll_opy_
    CONFIG[bstack111ll1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡘࡊࡋࠨਝ")] = str(bstack111111lll_opy_) + str(__version__)
    bstack1lll1l11l_opy_ = 0 if bstack1111ll11l_opy_ < 0 else bstack1111ll11l_opy_
    try:
      if bstack1l11ll1l_opy_ is True:
        bstack1lll1l11l_opy_ = int(multiprocessing.current_process().name)
      elif bstack11111l1l1_opy_ is True:
        bstack1lll1l11l_opy_ = int(threading.current_thread().name)
    except:
      bstack1lll1l11l_opy_ = 0
    CONFIG[bstack111ll1l_opy_ (u"ࠢࡪࡵࡓࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹࠨਞ")] = True
    bstack1llll1111l_opy_ = bstack1lllllll1l_opy_(CONFIG, bstack1lll1l11l_opy_)
    logger.debug(bstack1ll1ll1l1_opy_.format(str(bstack1llll1111l_opy_)))
    if CONFIG.get(bstack111ll1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡌࡰࡥࡤࡰࠬਟ")):
      bstack11l11111l_opy_(bstack1llll1111l_opy_)
    if bstack111ll1l_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬਠ") in CONFIG and bstack111ll1l_opy_ (u"ࠪࡷࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠨਡ") in CONFIG[bstack111ll1l_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧਢ")][bstack1lll1l11l_opy_]:
      bstack1111llll1_opy_ = CONFIG[bstack111ll1l_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨਣ")][bstack1lll1l11l_opy_][bstack111ll1l_opy_ (u"࠭ࡳࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠫਤ")]
    import urllib
    import json
    bstack1ll1l111l1_opy_ = bstack111ll1l_opy_ (u"ࠧࡸࡵࡶ࠾࠴࠵ࡣࡥࡲ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡦࡳࡲ࠵ࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࡂࡧࡦࡶࡳ࠾ࠩਥ") + urllib.parse.quote(json.dumps(bstack1llll1111l_opy_))
    browser = self.connect(bstack1ll1l111l1_opy_)
    return browser
except Exception as e:
    pass
def bstack1lll1l111l_opy_():
    global bstack1ll1l1ll1l_opy_
    try:
        from playwright._impl._browser_type import BrowserType
        BrowserType.launch = bstack11ll11ll1_opy_
        bstack1ll1l1ll1l_opy_ = True
    except Exception as e:
        pass
    try:
      import Browser
      from subprocess import Popen
      Popen.__init__ = bstack1l1llll11_opy_
      bstack1ll1l1ll1l_opy_ = True
    except Exception as e:
      pass
def bstack1l1ll11l1_opy_(context, bstack1llll1l1ll_opy_):
  try:
    context.page.evaluate(bstack111ll1l_opy_ (u"ࠣࡡࠣࡁࡃࠦࡻࡾࠤਦ"), bstack111ll1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࠨࡡࡤࡶ࡬ࡳࡳࠨ࠺ࠡࠤࡶࡩࡹ࡙ࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠥ࠰ࠥࠨࡡࡳࡩࡸࡱࡪࡴࡴࡴࠤ࠽ࠤࢀࠨ࡮ࡢ࡯ࡨࠦ࠿࠭ਧ")+ json.dumps(bstack1llll1l1ll_opy_) + bstack111ll1l_opy_ (u"ࠥࢁࢂࠨਨ"))
  except Exception as e:
    logger.debug(bstack111ll1l_opy_ (u"ࠦࡪࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡴࡱࡧࡹࡸࡴ࡬࡫࡭ࡺࠠࡴࡧࡶࡷ࡮ࡵ࡮ࠡࡰࡤࡱࡪࠦࡻࡾࠤ਩"), e)
def bstack1l11ll1ll_opy_(context, message, level):
  try:
    context.page.evaluate(bstack111ll1l_opy_ (u"ࠧࡥࠠ࠾ࡀࠣࡿࢂࠨਪ"), bstack111ll1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࠥࡥࡨࡺࡩࡰࡰࠥ࠾ࠥࠨࡡ࡯ࡰࡲࡸࡦࡺࡥࠣ࠮ࠣࠦࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠢ࠻ࠢࡾࠦࡩࡧࡴࡢࠤ࠽ࠫਫ") + json.dumps(message) + bstack111ll1l_opy_ (u"ࠧ࠭ࠤ࡯ࡩࡻ࡫࡬ࠣ࠼ࠪਬ") + json.dumps(level) + bstack111ll1l_opy_ (u"ࠨࡿࢀࠫਭ"))
  except Exception as e:
    logger.debug(bstack111ll1l_opy_ (u"ࠤࡨࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࠥࡧ࡮࡯ࡱࡷࡥࡹ࡯࡯࡯ࠢࡾࢁࠧਮ"), e)
def bstack1l1lll1l_opy_(context, status, message = bstack111ll1l_opy_ (u"ࠥࠦਯ")):
  try:
    if(status == bstack111ll1l_opy_ (u"ࠦ࡫ࡧࡩ࡭ࡧࡧࠦਰ")):
      context.page.evaluate(bstack111ll1l_opy_ (u"ࠧࡥࠠ࠾ࡀࠣࡿࢂࠨ਱"), bstack111ll1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࠥࡥࡨࡺࡩࡰࡰࠥ࠾ࠥࠨࡳࡦࡶࡖࡩࡸࡹࡩࡰࡰࡖࡸࡦࡺࡵࡴࠤ࠯ࠤࠧࡧࡲࡨࡷࡰࡩࡳࡺࡳࠣ࠼ࠣࡿࠧࡸࡥࡢࡵࡲࡲࠧࡀࠧਲ") + json.dumps(bstack111ll1l_opy_ (u"ࠢࡔࡥࡨࡲࡦࡸࡩࡰࠢࡩࡥ࡮ࡲࡥࡥࠢࡺ࡭ࡹ࡮࠺ࠡࠤਲ਼") + str(message)) + bstack111ll1l_opy_ (u"ࠨ࠮ࠥࡷࡹࡧࡴࡶࡵࠥ࠾ࠬ਴") + json.dumps(status) + bstack111ll1l_opy_ (u"ࠤࢀࢁࠧਵ"))
    else:
      context.page.evaluate(bstack111ll1l_opy_ (u"ࠥࡣࠥࡃ࠾ࠡࡽࢀࠦਸ਼"), bstack111ll1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻࠣࡣࡦࡸ࡮ࡵ࡮ࠣ࠼ࠣࠦࡸ࡫ࡴࡔࡧࡶࡷ࡮ࡵ࡮ࡔࡶࡤࡸࡺࡹࠢ࠭ࠢࠥࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸࠨ࠺ࠡࡽࠥࡷࡹࡧࡴࡶࡵࠥ࠾ࠬ਷") + json.dumps(status) + bstack111ll1l_opy_ (u"ࠧࢃࡽࠣਸ"))
  except Exception as e:
    logger.debug(bstack111ll1l_opy_ (u"ࠨࡥࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠢࡶࡩࡹࠦࡳࡦࡵࡶ࡭ࡴࡴࠠࡴࡶࡤࡸࡺࡹࠠࡼࡿࠥਹ"), e)
def bstack11ll1l111_opy_(self, url):
  global bstack1ll11l1l1_opy_
  try:
    bstack1ll1l1l111_opy_(url)
  except Exception as err:
    logger.debug(bstack111llll1_opy_.format(str(err)))
  try:
    bstack1ll11l1l1_opy_(self, url)
  except Exception as e:
    try:
      bstack11lll11l1_opy_ = str(e)
      if any(err_msg in bstack11lll11l1_opy_ for err_msg in bstack1lll1llll1_opy_):
        bstack1ll1l1l111_opy_(url, True)
    except Exception as err:
      logger.debug(bstack111llll1_opy_.format(str(err)))
    raise e
def bstack11ll1l1l_opy_(self):
  global bstack11lll1ll1_opy_
  bstack11lll1ll1_opy_ = self
  return
def bstack1l1llll1_opy_(self):
  global bstack1ll11l11ll_opy_
  bstack1ll11l11ll_opy_ = self
  return
def bstack1l1111ll1_opy_(self, test):
  global CONFIG
  global bstack1ll11l11ll_opy_
  global bstack11lll1ll1_opy_
  global bstack1l1l1l1l1_opy_
  global bstack11l11ll11_opy_
  global bstack1111llll1_opy_
  global bstack1ll11ll11l_opy_
  global bstack1l111l111_opy_
  global bstack1lll111l1l_opy_
  global bstack1lll1l11l1_opy_
  try:
    if not bstack1l1l1l1l1_opy_:
      with open(os.path.join(os.path.expanduser(bstack111ll1l_opy_ (u"ࠧࡿࠩ਺")), bstack111ll1l_opy_ (u"ࠨ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠨ਻"), bstack111ll1l_opy_ (u"ࠩ࠱ࡷࡪࡹࡳࡪࡱࡱ࡭ࡩࡹ࠮ࡵࡺࡷ਼ࠫ"))) as f:
        bstack1lllll11ll_opy_ = json.loads(bstack111ll1l_opy_ (u"ࠥࡿࠧ਽") + f.read().strip() + bstack111ll1l_opy_ (u"ࠫࠧࡾࠢ࠻ࠢࠥࡽࠧ࠭ਾ") + bstack111ll1l_opy_ (u"ࠧࢃࠢਿ"))
        bstack1l1l1l1l1_opy_ = bstack1lllll11ll_opy_[str(threading.get_ident())]
  except:
    pass
  if bstack1lll1l11l1_opy_:
    for driver in bstack1lll1l11l1_opy_:
      if bstack1l1l1l1l1_opy_ == driver.session_id:
        if test:
          bstack1ll1ll11_opy_ = str(test.data)
        if not bstack11l111l1_opy_ and bstack1ll1ll11_opy_:
          bstack1l1ll111l_opy_ = {
            bstack111ll1l_opy_ (u"࠭ࡡࡤࡶ࡬ࡳࡳ࠭ੀ"): bstack111ll1l_opy_ (u"ࠧࡴࡧࡷࡗࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠨੁ"),
            bstack111ll1l_opy_ (u"ࠨࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠫੂ"): {
              bstack111ll1l_opy_ (u"ࠩࡱࡥࡲ࡫ࠧ੃"): bstack1ll1ll11_opy_
            }
          }
          bstack1lll1ll111_opy_ = bstack111ll1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁࡽࠨ੄").format(json.dumps(bstack1l1ll111l_opy_))
          driver.execute_script(bstack1lll1ll111_opy_)
        if bstack11l11ll11_opy_:
          bstack1111l111_opy_ = {
            bstack111ll1l_opy_ (u"ࠫࡦࡩࡴࡪࡱࡱࠫ੅"): bstack111ll1l_opy_ (u"ࠬࡧ࡮࡯ࡱࡷࡥࡹ࡫ࠧ੆"),
            bstack111ll1l_opy_ (u"࠭ࡡࡳࡩࡸࡱࡪࡴࡴࡴࠩੇ"): {
              bstack111ll1l_opy_ (u"ࠧࡥࡣࡷࡥࠬੈ"): bstack1ll1ll11_opy_ + bstack111ll1l_opy_ (u"ࠨࠢࡳࡥࡸࡹࡥࡥࠣࠪ੉"),
              bstack111ll1l_opy_ (u"ࠩ࡯ࡩࡻ࡫࡬ࠨ੊"): bstack111ll1l_opy_ (u"ࠪ࡭ࡳ࡬࡯ࠨੋ")
            }
          }
          bstack1l1ll111l_opy_ = {
            bstack111ll1l_opy_ (u"ࠫࡦࡩࡴࡪࡱࡱࠫੌ"): bstack111ll1l_opy_ (u"ࠬࡹࡥࡵࡕࡨࡷࡸ࡯࡯࡯ࡕࡷࡥࡹࡻࡳࠨ੍"),
            bstack111ll1l_opy_ (u"࠭ࡡࡳࡩࡸࡱࡪࡴࡴࡴࠩ੎"): {
              bstack111ll1l_opy_ (u"ࠧࡴࡶࡤࡸࡺࡹࠧ੏"): bstack111ll1l_opy_ (u"ࠨࡲࡤࡷࡸ࡫ࡤࠨ੐")
            }
          }
          if bstack11l11ll11_opy_.status == bstack111ll1l_opy_ (u"ࠩࡓࡅࡘ࡙ࠧੑ"):
            bstack1llllll11_opy_ = bstack111ll1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁࡽࠨ੒").format(json.dumps(bstack1111l111_opy_))
            driver.execute_script(bstack1llllll11_opy_)
            bstack1lll1ll111_opy_ = bstack111ll1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻࡾࠩ੓").format(json.dumps(bstack1l1ll111l_opy_))
            driver.execute_script(bstack1lll1ll111_opy_)
          elif bstack11l11ll11_opy_.status == bstack111ll1l_opy_ (u"ࠬࡌࡁࡊࡎࠪ੔"):
            reason = bstack111ll1l_opy_ (u"ࠨࠢ੕")
            bstack1l1111l1_opy_ = bstack1ll1ll11_opy_ + bstack111ll1l_opy_ (u"ࠧࠡࡨࡤ࡭ࡱ࡫ࡤࠨ੖")
            if bstack11l11ll11_opy_.message:
              reason = str(bstack11l11ll11_opy_.message)
              bstack1l1111l1_opy_ = bstack1l1111l1_opy_ + bstack111ll1l_opy_ (u"ࠨࠢࡺ࡭ࡹ࡮ࠠࡦࡴࡵࡳࡷࡀࠠࠨ੗") + reason
            bstack1111l111_opy_[bstack111ll1l_opy_ (u"ࠩࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠬ੘")] = {
              bstack111ll1l_opy_ (u"ࠪࡰࡪࡼࡥ࡭ࠩਖ਼"): bstack111ll1l_opy_ (u"ࠫࡪࡸࡲࡰࡴࠪਗ਼"),
              bstack111ll1l_opy_ (u"ࠬࡪࡡࡵࡣࠪਜ਼"): bstack1l1111l1_opy_
            }
            bstack1l1ll111l_opy_[bstack111ll1l_opy_ (u"࠭ࡡࡳࡩࡸࡱࡪࡴࡴࡴࠩੜ")] = {
              bstack111ll1l_opy_ (u"ࠧࡴࡶࡤࡸࡺࡹࠧ੝"): bstack111ll1l_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨਫ਼"),
              bstack111ll1l_opy_ (u"ࠩࡵࡩࡦࡹ࡯࡯ࠩ੟"): reason
            }
            bstack1llllll11_opy_ = bstack111ll1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁࡽࠨ੠").format(json.dumps(bstack1111l111_opy_))
            driver.execute_script(bstack1llllll11_opy_)
            bstack1lll1ll111_opy_ = bstack111ll1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻࡾࠩ੡").format(json.dumps(bstack1l1ll111l_opy_))
            driver.execute_script(bstack1lll1ll111_opy_)
  elif bstack1l1l1l1l1_opy_:
    try:
      data = {}
      bstack1ll1ll11_opy_ = None
      if test:
        bstack1ll1ll11_opy_ = str(test.data)
      if not bstack11l111l1_opy_ and bstack1ll1ll11_opy_:
        data[bstack111ll1l_opy_ (u"ࠬࡴࡡ࡮ࡧࠪ੢")] = bstack1ll1ll11_opy_
      if bstack11l11ll11_opy_:
        if bstack11l11ll11_opy_.status == bstack111ll1l_opy_ (u"࠭ࡐࡂࡕࡖࠫ੣"):
          data[bstack111ll1l_opy_ (u"ࠧࡴࡶࡤࡸࡺࡹࠧ੤")] = bstack111ll1l_opy_ (u"ࠨࡲࡤࡷࡸ࡫ࡤࠨ੥")
        elif bstack11l11ll11_opy_.status == bstack111ll1l_opy_ (u"ࠩࡉࡅࡎࡒࠧ੦"):
          data[bstack111ll1l_opy_ (u"ࠪࡷࡹࡧࡴࡶࡵࠪ੧")] = bstack111ll1l_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫ੨")
          if bstack11l11ll11_opy_.message:
            data[bstack111ll1l_opy_ (u"ࠬࡸࡥࡢࡵࡲࡲࠬ੩")] = str(bstack11l11ll11_opy_.message)
      user = CONFIG[bstack111ll1l_opy_ (u"࠭ࡵࡴࡧࡵࡒࡦࡳࡥࠨ੪")]
      key = CONFIG[bstack111ll1l_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡋࡦࡻࠪ੫")]
      url = bstack111ll1l_opy_ (u"ࠨࡪࡷࡸࡵࡹ࠺࠰࠱ࡾࢁ࠿ࢁࡽࡁࡣࡳ࡭࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡨࡵ࡭࠰ࡣࡸࡸࡴࡳࡡࡵࡧ࠲ࡷࡪࡹࡳࡪࡱࡱࡷ࠴ࢁࡽ࠯࡬ࡶࡳࡳ࠭੬").format(user, key, bstack1l1l1l1l1_opy_)
      headers = {
        bstack111ll1l_opy_ (u"ࠩࡆࡳࡳࡺࡥ࡯ࡶ࠰ࡸࡾࡶࡥࠨ੭"): bstack111ll1l_opy_ (u"ࠪࡥࡵࡶ࡬ࡪࡥࡤࡸ࡮ࡵ࡮࠰࡬ࡶࡳࡳ࠭੮"),
      }
      if bool(data):
        requests.put(url, json=data, headers=headers)
    except Exception as e:
      logger.error(bstack111ll1l11_opy_.format(str(e)))
  if bstack1ll11l11ll_opy_:
    bstack1l111l111_opy_(bstack1ll11l11ll_opy_)
  if bstack11lll1ll1_opy_:
    bstack1lll111l1l_opy_(bstack11lll1ll1_opy_)
  bstack1ll11ll11l_opy_(self, test)
def bstack1lll11l1l1_opy_(self, parent, test, skip_on_failure=None, rpa=False):
  global bstack1ll1l11111_opy_
  bstack1ll1l11111_opy_(self, parent, test, skip_on_failure=skip_on_failure, rpa=rpa)
  global bstack11l11ll11_opy_
  bstack11l11ll11_opy_ = self._test
def bstack1ll11l11l1_opy_():
  global bstack1ll1ll11ll_opy_
  try:
    if os.path.exists(bstack1ll1ll11ll_opy_):
      os.remove(bstack1ll1ll11ll_opy_)
  except Exception as e:
    logger.debug(bstack111ll1l_opy_ (u"ࠫࡊࡸࡲࡰࡴࠣ࡭ࡳࠦࡤࡦ࡮ࡨࡸ࡮ࡴࡧࠡࡴࡲࡦࡴࡺࠠࡳࡧࡳࡳࡷࡺࠠࡧ࡫࡯ࡩ࠿ࠦࠧ੯") + str(e))
def bstack1ll1lll1_opy_():
  global bstack1ll1ll11ll_opy_
  bstack111l111l1_opy_ = {}
  try:
    if not os.path.isfile(bstack1ll1ll11ll_opy_):
      with open(bstack1ll1ll11ll_opy_, bstack111ll1l_opy_ (u"ࠬࡽࠧੰ")):
        pass
      with open(bstack1ll1ll11ll_opy_, bstack111ll1l_opy_ (u"ࠨࡷࠬࠤੱ")) as outfile:
        json.dump({}, outfile)
    if os.path.exists(bstack1ll1ll11ll_opy_):
      bstack111l111l1_opy_ = json.load(open(bstack1ll1ll11ll_opy_, bstack111ll1l_opy_ (u"ࠧࡳࡤࠪੲ")))
  except Exception as e:
    logger.debug(bstack111ll1l_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡪࡰࠣࡶࡪࡧࡤࡪࡰࡪࠤࡷࡵࡢࡰࡶࠣࡶࡪࡶ࡯ࡳࡶࠣࡪ࡮ࡲࡥ࠻ࠢࠪੳ") + str(e))
  finally:
    return bstack111l111l1_opy_
def bstack1lll111l11_opy_(platform_index, item_index):
  global bstack1ll1ll11ll_opy_
  try:
    bstack111l111l1_opy_ = bstack1ll1lll1_opy_()
    bstack111l111l1_opy_[item_index] = platform_index
    with open(bstack1ll1ll11ll_opy_, bstack111ll1l_opy_ (u"ࠤࡺ࠯ࠧੴ")) as outfile:
      json.dump(bstack111l111l1_opy_, outfile)
  except Exception as e:
    logger.debug(bstack111ll1l_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥࡽࡲࡪࡶ࡬ࡲ࡬ࠦࡴࡰࠢࡵࡳࡧࡵࡴࠡࡴࡨࡴࡴࡸࡴࠡࡨ࡬ࡰࡪࡀࠠࠨੵ") + str(e))
def bstack1l111l11l_opy_(bstack1llllll1l_opy_):
  global CONFIG
  bstack1l11llll_opy_ = bstack111ll1l_opy_ (u"ࠫࠬ੶")
  if not bstack111ll1l_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ੷") in CONFIG:
    logger.info(bstack111ll1l_opy_ (u"࠭ࡎࡰࠢࡳࡰࡦࡺࡦࡰࡴࡰࡷࠥࡶࡡࡴࡵࡨࡨࠥࡻ࡮ࡢࡤ࡯ࡩࠥࡺ࡯ࠡࡩࡨࡲࡪࡸࡡࡵࡧࠣࡶࡪࡶ࡯ࡳࡶࠣࡪࡴࡸࠠࡓࡱࡥࡳࡹࠦࡲࡶࡰࠪ੸"))
  try:
    platform = CONFIG[bstack111ll1l_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪ੹")][bstack1llllll1l_opy_]
    if bstack111ll1l_opy_ (u"ࠨࡱࡶࠫ੺") in platform:
      bstack1l11llll_opy_ += str(platform[bstack111ll1l_opy_ (u"ࠩࡲࡷࠬ੻")]) + bstack111ll1l_opy_ (u"ࠪ࠰ࠥ࠭੼")
    if bstack111ll1l_opy_ (u"ࠫࡴࡹࡖࡦࡴࡶ࡭ࡴࡴࠧ੽") in platform:
      bstack1l11llll_opy_ += str(platform[bstack111ll1l_opy_ (u"ࠬࡵࡳࡗࡧࡵࡷ࡮ࡵ࡮ࠨ੾")]) + bstack111ll1l_opy_ (u"࠭ࠬࠡࠩ੿")
    if bstack111ll1l_opy_ (u"ࠧࡥࡧࡹ࡭ࡨ࡫ࡎࡢ࡯ࡨࠫ઀") in platform:
      bstack1l11llll_opy_ += str(platform[bstack111ll1l_opy_ (u"ࠨࡦࡨࡺ࡮ࡩࡥࡏࡣࡰࡩࠬઁ")]) + bstack111ll1l_opy_ (u"ࠩ࠯ࠤࠬં")
    if bstack111ll1l_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱ࡛࡫ࡲࡴ࡫ࡲࡲࠬઃ") in platform:
      bstack1l11llll_opy_ += str(platform[bstack111ll1l_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲ࡜ࡥࡳࡵ࡬ࡳࡳ࠭઄")]) + bstack111ll1l_opy_ (u"ࠬ࠲ࠠࠨઅ")
    if bstack111ll1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡎࡢ࡯ࡨࠫઆ") in platform:
      bstack1l11llll_opy_ += str(platform[bstack111ll1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡏࡣࡰࡩࠬઇ")]) + bstack111ll1l_opy_ (u"ࠨ࠮ࠣࠫઈ")
    if bstack111ll1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪઉ") in platform:
      bstack1l11llll_opy_ += str(platform[bstack111ll1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠫઊ")]) + bstack111ll1l_opy_ (u"ࠫ࠱ࠦࠧઋ")
  except Exception as e:
    logger.debug(bstack111ll1l_opy_ (u"࡙ࠬ࡯࡮ࡧࠣࡩࡷࡸ࡯ࡳࠢ࡬ࡲࠥ࡭ࡥ࡯ࡧࡵࡥࡹ࡯࡮ࡨࠢࡳࡰࡦࡺࡦࡰࡴࡰࠤࡸࡺࡲࡪࡰࡪࠤ࡫ࡵࡲࠡࡴࡨࡴࡴࡸࡴࠡࡩࡨࡲࡪࡸࡡࡵ࡫ࡲࡲࠬઌ") + str(e))
  finally:
    if bstack1l11llll_opy_[len(bstack1l11llll_opy_) - 2:] == bstack111ll1l_opy_ (u"࠭ࠬࠡࠩઍ"):
      bstack1l11llll_opy_ = bstack1l11llll_opy_[:-2]
    return bstack1l11llll_opy_
def bstack1l111ll11_opy_(path, bstack1l11llll_opy_):
  try:
    import xml.etree.ElementTree as ET
    bstack1l1ll1l1l_opy_ = ET.parse(path)
    bstack111llll11_opy_ = bstack1l1ll1l1l_opy_.getroot()
    bstack1l1l1l11_opy_ = None
    for suite in bstack111llll11_opy_.iter(bstack111ll1l_opy_ (u"ࠧࡴࡷ࡬ࡸࡪ࠭઎")):
      if bstack111ll1l_opy_ (u"ࠨࡵࡲࡹࡷࡩࡥࠨએ") in suite.attrib:
        suite.attrib[bstack111ll1l_opy_ (u"ࠩࡱࡥࡲ࡫ࠧઐ")] += bstack111ll1l_opy_ (u"ࠪࠤࠬઑ") + bstack1l11llll_opy_
        bstack1l1l1l11_opy_ = suite
    bstack111ll1lll_opy_ = None
    for robot in bstack111llll11_opy_.iter(bstack111ll1l_opy_ (u"ࠫࡷࡵࡢࡰࡶࠪ઒")):
      bstack111ll1lll_opy_ = robot
    bstack111111l1_opy_ = len(bstack111ll1lll_opy_.findall(bstack111ll1l_opy_ (u"ࠬࡹࡵࡪࡶࡨࠫઓ")))
    if bstack111111l1_opy_ == 1:
      bstack111ll1lll_opy_.remove(bstack111ll1lll_opy_.findall(bstack111ll1l_opy_ (u"࠭ࡳࡶ࡫ࡷࡩࠬઔ"))[0])
      bstack1lll11lll1_opy_ = ET.Element(bstack111ll1l_opy_ (u"ࠧࡴࡷ࡬ࡸࡪ࠭ક"), attrib={bstack111ll1l_opy_ (u"ࠨࡰࡤࡱࡪ࠭ખ"): bstack111ll1l_opy_ (u"ࠩࡖࡹ࡮ࡺࡥࡴࠩગ"), bstack111ll1l_opy_ (u"ࠪ࡭ࡩ࠭ઘ"): bstack111ll1l_opy_ (u"ࠫࡸ࠶ࠧઙ")})
      bstack111ll1lll_opy_.insert(1, bstack1lll11lll1_opy_)
      bstack1l11lll11_opy_ = None
      for suite in bstack111ll1lll_opy_.iter(bstack111ll1l_opy_ (u"ࠬࡹࡵࡪࡶࡨࠫચ")):
        bstack1l11lll11_opy_ = suite
      bstack1l11lll11_opy_.append(bstack1l1l1l11_opy_)
      bstack11l1ll1l1_opy_ = None
      for status in bstack1l1l1l11_opy_.iter(bstack111ll1l_opy_ (u"࠭ࡳࡵࡣࡷࡹࡸ࠭છ")):
        bstack11l1ll1l1_opy_ = status
      bstack1l11lll11_opy_.append(bstack11l1ll1l1_opy_)
    bstack1l1ll1l1l_opy_.write(path)
  except Exception as e:
    logger.debug(bstack111ll1l_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡳࡥࡷࡹࡩ࡯ࡩࠣࡻ࡭࡯࡬ࡦࠢࡪࡩࡳ࡫ࡲࡢࡶ࡬ࡲ࡬ࠦࡲࡰࡤࡲࡸࠥࡸࡥࡱࡱࡵࡸࠬજ") + str(e))
def bstack1ll11ll1_opy_(outs_dir, pabot_args, options, start_time_string, tests_root_name):
  global bstack1ll1l11l_opy_
  global CONFIG
  if bstack111ll1l_opy_ (u"ࠣࡲࡼࡸ࡭ࡵ࡮ࡱࡣࡷ࡬ࠧઝ") in options:
    del options[bstack111ll1l_opy_ (u"ࠤࡳࡽࡹ࡮࡯࡯ࡲࡤࡸ࡭ࠨઞ")]
  bstack1lllll1ll1_opy_ = bstack1ll1lll1_opy_()
  for bstack1lll1ll11_opy_ in bstack1lllll1ll1_opy_.keys():
    path = os.path.join(os.getcwd(), bstack111ll1l_opy_ (u"ࠪࡴࡦࡨ࡯ࡵࡡࡵࡩࡸࡻ࡬ࡵࡵࠪટ"), str(bstack1lll1ll11_opy_), bstack111ll1l_opy_ (u"ࠫࡴࡻࡴࡱࡷࡷ࠲ࡽࡳ࡬ࠨઠ"))
    bstack1l111ll11_opy_(path, bstack1l111l11l_opy_(bstack1lllll1ll1_opy_[bstack1lll1ll11_opy_]))
  bstack1ll11l11l1_opy_()
  return bstack1ll1l11l_opy_(outs_dir, pabot_args, options, start_time_string, tests_root_name)
def bstack111l1ll11_opy_(self, ff_profile_dir):
  global bstack1l1l111ll_opy_
  if not ff_profile_dir:
    return None
  return bstack1l1l111ll_opy_(self, ff_profile_dir)
def bstack111lllll1_opy_(datasources, opts_for_run, outs_dir, pabot_args, suite_group):
  from pabot.pabot import QueueItem
  global CONFIG
  global bstack11l11llll_opy_
  bstack1lll1l1111_opy_ = []
  if bstack111ll1l_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨડ") in CONFIG:
    bstack1lll1l1111_opy_ = CONFIG[bstack111ll1l_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩઢ")]
  return [
    QueueItem(
      datasources,
      outs_dir,
      opts_for_run,
      suite,
      pabot_args[bstack111ll1l_opy_ (u"ࠢࡤࡱࡰࡱࡦࡴࡤࠣણ")],
      pabot_args[bstack111ll1l_opy_ (u"ࠣࡸࡨࡶࡧࡵࡳࡦࠤત")],
      argfile,
      pabot_args.get(bstack111ll1l_opy_ (u"ࠤ࡫࡭ࡻ࡫ࠢથ")),
      pabot_args[bstack111ll1l_opy_ (u"ࠥࡴࡷࡵࡣࡦࡵࡶࡩࡸࠨદ")],
      platform[0],
      bstack11l11llll_opy_
    )
    for suite in suite_group
    for argfile in pabot_args[bstack111ll1l_opy_ (u"ࠦࡦࡸࡧࡶ࡯ࡨࡲࡹ࡬ࡩ࡭ࡧࡶࠦધ")] or [(bstack111ll1l_opy_ (u"ࠧࠨન"), None)]
    for platform in enumerate(bstack1lll1l1111_opy_)
  ]
def bstack1ll111ll_opy_(self, datasources, outs_dir, options,
                        execution_item, command, verbose, argfile,
                        hive=None, processes=0, platform_index=0, bstack1llll1ll1l_opy_=bstack111ll1l_opy_ (u"࠭ࠧ઩")):
  global bstack11lll1l1l_opy_
  self.platform_index = platform_index
  self.bstack1lll11ll11_opy_ = bstack1llll1ll1l_opy_
  bstack11lll1l1l_opy_(self, datasources, outs_dir, options,
                      execution_item, command, verbose, argfile, hive, processes)
def bstack11llll1l1_opy_(caller_id, datasources, is_last, item, outs_dir):
  global bstack11l1llll_opy_
  global bstack1l1l1ll1l_opy_
  if not bstack111ll1l_opy_ (u"ࠧࡷࡣࡵ࡭ࡦࡨ࡬ࡦࠩપ") in item.options:
    item.options[bstack111ll1l_opy_ (u"ࠨࡸࡤࡶ࡮ࡧࡢ࡭ࡧࠪફ")] = []
  for v in item.options[bstack111ll1l_opy_ (u"ࠩࡹࡥࡷ࡯ࡡࡣ࡮ࡨࠫબ")]:
    if bstack111ll1l_opy_ (u"ࠪࡆࡘ࡚ࡁࡄࡍࡓࡐࡆ࡚ࡆࡐࡔࡐࡍࡓࡊࡅ࡙ࠩભ") in v:
      item.options[bstack111ll1l_opy_ (u"ࠫࡻࡧࡲࡪࡣࡥࡰࡪ࠭મ")].remove(v)
    if bstack111ll1l_opy_ (u"ࠬࡈࡓࡕࡃࡆࡏࡈࡒࡉࡂࡔࡊࡗࠬય") in v:
      item.options[bstack111ll1l_opy_ (u"࠭ࡶࡢࡴ࡬ࡥࡧࡲࡥࠨર")].remove(v)
  item.options[bstack111ll1l_opy_ (u"ࠧࡷࡣࡵ࡭ࡦࡨ࡬ࡦࠩ઱")].insert(0, bstack111ll1l_opy_ (u"ࠨࡄࡖࡘࡆࡉࡋࡑࡎࡄࡘࡋࡕࡒࡎࡋࡑࡈࡊ࡞࠺ࡼࡿࠪલ").format(item.platform_index))
  item.options[bstack111ll1l_opy_ (u"ࠩࡹࡥࡷ࡯ࡡࡣ࡮ࡨࠫળ")].insert(0, bstack111ll1l_opy_ (u"ࠪࡆࡘ࡚ࡁࡄࡍࡇࡉࡋࡒࡏࡄࡃࡏࡍࡉࡋࡎࡕࡋࡉࡍࡊࡘ࠺ࡼࡿࠪ઴").format(item.bstack1lll11ll11_opy_))
  if bstack1l1l1ll1l_opy_:
    item.options[bstack111ll1l_opy_ (u"ࠫࡻࡧࡲࡪࡣࡥࡰࡪ࠭વ")].insert(0, bstack111ll1l_opy_ (u"ࠬࡈࡓࡕࡃࡆࡏࡈࡒࡉࡂࡔࡊࡗ࠿ࢁࡽࠨશ").format(bstack1l1l1ll1l_opy_))
  return bstack11l1llll_opy_(caller_id, datasources, is_last, item, outs_dir)
def bstack1l11ll111_opy_(command, item_index):
  global bstack1l1l1ll1l_opy_
  if bstack1l1l1ll1l_opy_:
    command[0] = command[0].replace(bstack111ll1l_opy_ (u"࠭ࡲࡰࡤࡲࡸࠬષ"), bstack111ll1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠳ࡳࡥ࡭ࠣࡶࡴࡨ࡯ࡵ࠯࡬ࡲࡹ࡫ࡲ࡯ࡣ࡯ࠤ࠲࠳ࡢࡴࡶࡤࡧࡰࡥࡩࡵࡧࡰࡣ࡮ࡴࡤࡦࡺࠣࠫસ") + str(
      item_index) + bstack111ll1l_opy_ (u"ࠨࠢࠪહ") + bstack1l1l1ll1l_opy_, 1)
  else:
    command[0] = command[0].replace(bstack111ll1l_opy_ (u"ࠩࡵࡳࡧࡵࡴࠨ઺"),
                                    bstack111ll1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠯ࡶࡨࡰࠦࡲࡰࡤࡲࡸ࠲࡯࡮ࡵࡧࡵࡲࡦࡲࠠ࠮࠯ࡥࡷࡹࡧࡣ࡬ࡡ࡬ࡸࡪࡳ࡟ࡪࡰࡧࡩࡽࠦࠧ઻") + str(item_index), 1)
def bstack1l1l1l1ll_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index):
  global bstack1l1l1llll_opy_
  bstack1l11ll111_opy_(command, item_index)
  return bstack1l1l1llll_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index)
def bstack11llll11l_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir):
  global bstack1l1l1llll_opy_
  bstack1l11ll111_opy_(command, item_index)
  return bstack1l1l1llll_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir)
def bstack11l1l1ll1_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout):
  global bstack1l1l1llll_opy_
  bstack1l11ll111_opy_(command, item_index)
  return bstack1l1l1llll_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout)
def bstack1l11111ll_opy_(self, runner, quiet=False, capture=True):
  global bstack1ll111l1_opy_
  bstack1llll11l_opy_ = bstack1ll111l1_opy_(self, runner, quiet=False, capture=True)
  if self.exception:
    if not hasattr(runner, bstack111ll1l_opy_ (u"ࠫࡪࡾࡣࡦࡲࡷ࡭ࡴࡴ࡟ࡢࡴࡵ઼ࠫ")):
      runner.exception_arr = []
    if not hasattr(runner, bstack111ll1l_opy_ (u"ࠬ࡫ࡸࡤࡡࡷࡶࡦࡩࡥࡣࡣࡦ࡯ࡤࡧࡲࡳࠩઽ")):
      runner.exc_traceback_arr = []
    runner.exception = self.exception
    runner.exc_traceback = self.exc_traceback
    runner.exception_arr.append(self.exception)
    runner.exc_traceback_arr.append(self.exc_traceback)
  return bstack1llll11l_opy_
def bstack1111l111l_opy_(self, name, context, *args):
  global bstack1l11l11l_opy_
  if name == bstack111ll1l_opy_ (u"࠭ࡢࡦࡨࡲࡶࡪࡥࡦࡦࡣࡷࡹࡷ࡫ࠧા"):
    bstack1l11l11l_opy_(self, name, context, *args)
    try:
      if not bstack11l111l1_opy_:
        bstack1l111111_opy_ = threading.current_thread().bstackSessionDriver if bstack1llllll1ll_opy_(bstack111ll1l_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱࡓࡦࡵࡶ࡭ࡴࡴࡄࡳ࡫ࡹࡩࡷ࠭િ")) else context.browser
        bstack1llll1l1ll_opy_ = str(self.feature.name)
        bstack1l1ll11l1_opy_(context, bstack1llll1l1ll_opy_)
        bstack1l111111_opy_.execute_script(bstack111ll1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࡿࠧࡧࡣࡵ࡫ࡲࡲࠧࡀࠠࠣࡵࡨࡸࡘ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠤ࠯ࠤࠧࡧࡲࡨࡷࡰࡩࡳࡺࡳࠣ࠼ࠣࡿࠧࡴࡡ࡮ࡧࠥ࠾ࠥ࠭ી") + json.dumps(bstack1llll1l1ll_opy_) + bstack111ll1l_opy_ (u"ࠩࢀࢁࠬુ"))
      self.driver_before_scenario = False
    except Exception as e:
      logger.debug(bstack111ll1l_opy_ (u"ࠪࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡳࡦࡶࠣࡷࡪࡹࡳࡪࡱࡱࠤࡳࡧ࡭ࡦࠢ࡬ࡲࠥࡨࡥࡧࡱࡵࡩࠥ࡬ࡥࡢࡶࡸࡶࡪࡀࠠࡼࡿࠪૂ").format(str(e)))
  elif name == bstack111ll1l_opy_ (u"ࠫࡧ࡫ࡦࡰࡴࡨࡣࡸࡩࡥ࡯ࡣࡵ࡭ࡴ࠭ૃ"):
    bstack1l11l11l_opy_(self, name, context, *args)
    try:
      if not hasattr(self, bstack111ll1l_opy_ (u"ࠬࡪࡲࡪࡸࡨࡶࡤࡨࡥࡧࡱࡵࡩࡤࡹࡣࡦࡰࡤࡶ࡮ࡵࠧૄ")):
        self.driver_before_scenario = True
      if (not bstack11l111l1_opy_):
        scenario_name = args[0].name
        feature_name = bstack1llll1l1ll_opy_ = str(self.feature.name)
        bstack1llll1l1ll_opy_ = feature_name + bstack111ll1l_opy_ (u"࠭ࠠ࠮ࠢࠪૅ") + scenario_name
        bstack1l111111_opy_ = threading.current_thread().bstackSessionDriver if bstack1llllll1ll_opy_(bstack111ll1l_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱࡓࡦࡵࡶ࡭ࡴࡴࡄࡳ࡫ࡹࡩࡷ࠭૆")) else context.browser
        if self.driver_before_scenario:
          bstack1l1ll11l1_opy_(context, bstack1llll1l1ll_opy_)
          bstack1l111111_opy_.execute_script(bstack111ll1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࡿࠧࡧࡣࡵ࡫ࡲࡲࠧࡀࠠࠣࡵࡨࡸࡘ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠤ࠯ࠤࠧࡧࡲࡨࡷࡰࡩࡳࡺࡳࠣ࠼ࠣࡿࠧࡴࡡ࡮ࡧࠥ࠾ࠥ࠭ે") + json.dumps(bstack1llll1l1ll_opy_) + bstack111ll1l_opy_ (u"ࠩࢀࢁࠬૈ"))
    except Exception as e:
      logger.debug(bstack111ll1l_opy_ (u"ࠪࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡳࡦࡶࠣࡷࡪࡹࡳࡪࡱࡱࠤࡳࡧ࡭ࡦࠢ࡬ࡲࠥࡨࡥࡧࡱࡵࡩࠥࡹࡣࡦࡰࡤࡶ࡮ࡵ࠺ࠡࡽࢀࠫૉ").format(str(e)))
  elif name == bstack111ll1l_opy_ (u"ࠫࡦ࡬ࡴࡦࡴࡢࡷࡨ࡫࡮ࡢࡴ࡬ࡳࠬ૊"):
    try:
      bstack1lll11lll_opy_ = args[0].status.name
      bstack1l111111_opy_ = threading.current_thread().bstackSessionDriver if bstack111ll1l_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯ࡘ࡫ࡳࡴ࡫ࡲࡲࡉࡸࡩࡷࡧࡵࠫો") in threading.current_thread().__dict__.keys() else context.browser
      if str(bstack1lll11lll_opy_).lower() == bstack111ll1l_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭ૌ"):
        bstack1l111l1ll_opy_ = bstack111ll1l_opy_ (u"ࠧࠨ્")
        bstack1llll111_opy_ = bstack111ll1l_opy_ (u"ࠨࠩ૎")
        bstack1l1l11l11_opy_ = bstack111ll1l_opy_ (u"ࠩࠪ૏")
        try:
          import traceback
          bstack1l111l1ll_opy_ = self.exception.__class__.__name__
          bstack1llll1lll1_opy_ = traceback.format_tb(self.exc_traceback)
          bstack1llll111_opy_ = bstack111ll1l_opy_ (u"ࠪࠤࠬૐ").join(bstack1llll1lll1_opy_)
          bstack1l1l11l11_opy_ = bstack1llll1lll1_opy_[-1]
        except Exception as e:
          logger.debug(bstack1111l1ll_opy_.format(str(e)))
        bstack1l111l1ll_opy_ += bstack1l1l11l11_opy_
        bstack1l11ll1ll_opy_(context, json.dumps(str(args[0].name) + bstack111ll1l_opy_ (u"ࠦࠥ࠳ࠠࡇࡣ࡬ࡰࡪࡪࠡ࡝ࡰࠥ૑") + str(bstack1llll111_opy_)),
                            bstack111ll1l_opy_ (u"ࠧ࡫ࡲࡳࡱࡵࠦ૒"))
        if self.driver_before_scenario:
          bstack1l1lll1l_opy_(context, bstack111ll1l_opy_ (u"ࠨࡦࡢ࡫࡯ࡩࡩࠨ૓"), bstack1l111l1ll_opy_)
          bstack1l111111_opy_.execute_script(bstack111ll1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࡾࠦࡦࡩࡴࡪࡱࡱࠦ࠿ࠦࠢࡢࡰࡱࡳࡹࡧࡴࡦࠤ࠯ࠤࠧࡧࡲࡨࡷࡰࡩࡳࡺࡳࠣ࠼ࠣࡿࠧࡪࡡࡵࡣࠥ࠾ࠬ૔") + json.dumps(str(args[0].name) + bstack111ll1l_opy_ (u"ࠣࠢ࠰ࠤࡋࡧࡩ࡭ࡧࡧࠥࡡࡴࠢ૕") + str(bstack1llll111_opy_)) + bstack111ll1l_opy_ (u"ࠩ࠯ࠤࠧࡲࡥࡷࡧ࡯ࠦ࠿ࠦࠢࡦࡴࡵࡳࡷࠨࡽࡾࠩ૖"))
        if self.driver_before_scenario:
          bstack1l111111_opy_.execute_script(bstack111ll1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁࠢࡢࡥࡷ࡭ࡴࡴࠢ࠻ࠢࠥࡷࡪࡺࡓࡦࡵࡶ࡭ࡴࡴࡓࡵࡣࡷࡹࡸࠨࠬࠡࠤࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠧࡀࠠࡼࠤࡶࡸࡦࡺࡵࡴࠤ࠽ࠦ࡫ࡧࡩ࡭ࡧࡧࠦ࠱ࠦࠢࡳࡧࡤࡷࡴࡴࠢ࠻ࠢࠪ૗") + json.dumps(bstack111ll1l_opy_ (u"ࠦࡘࡩࡥ࡯ࡣࡵ࡭ࡴࠦࡦࡢ࡫࡯ࡩࡩࠦࡷࡪࡶ࡫࠾ࠥࡢ࡮ࠣ૘") + str(bstack1l111l1ll_opy_)) + bstack111ll1l_opy_ (u"ࠬࢃࡽࠨ૙"))
      else:
        bstack1l11ll1ll_opy_(context, bstack111ll1l_opy_ (u"ࠨࡐࡢࡵࡶࡩࡩࠧࠢ૚"), bstack111ll1l_opy_ (u"ࠢࡪࡰࡩࡳࠧ૛"))
        if self.driver_before_scenario:
          bstack1l1lll1l_opy_(context, bstack111ll1l_opy_ (u"ࠣࡲࡤࡷࡸ࡫ࡤࠣ૜"))
        bstack1l111111_opy_.execute_script(bstack111ll1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࠨࡡࡤࡶ࡬ࡳࡳࠨ࠺ࠡࠤࡤࡲࡳࡵࡴࡢࡶࡨࠦ࠱ࠦࠢࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠥ࠾ࠥࢁࠢࡥࡣࡷࡥࠧࡀࠧ૝") + json.dumps(str(args[0].name) + bstack111ll1l_opy_ (u"ࠥࠤ࠲ࠦࡐࡢࡵࡶࡩࡩࠧࠢ૞")) + bstack111ll1l_opy_ (u"ࠫ࠱ࠦࠢ࡭ࡧࡹࡩࡱࠨ࠺ࠡࠤ࡬ࡲ࡫ࡵࠢࡾࡿࠪ૟"))
        if self.driver_before_scenario:
          bstack1l111111_opy_.execute_script(bstack111ll1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࡼࠤࡤࡧࡹ࡯࡯࡯ࠤ࠽ࠤࠧࡹࡥࡵࡕࡨࡷࡸ࡯࡯࡯ࡕࡷࡥࡹࡻࡳࠣ࠮ࠣࠦࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠢ࠻ࠢࡾࠦࡸࡺࡡࡵࡷࡶࠦ࠿ࠨࡰࡢࡵࡶࡩࡩࠨࡽࡾࠩૠ"))
    except Exception as e:
      logger.debug(bstack111ll1l_opy_ (u"࠭ࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡰࡥࡷࡱࠠࡴࡧࡶࡷ࡮ࡵ࡮ࠡࡵࡷࡥࡹࡻࡳࠡ࡫ࡱࠤࡦ࡬ࡴࡦࡴࠣࡪࡪࡧࡴࡶࡴࡨ࠾ࠥࢁࡽࠨૡ").format(str(e)))
  elif name == bstack111ll1l_opy_ (u"ࠧࡢࡨࡷࡩࡷࡥࡦࡦࡣࡷࡹࡷ࡫ࠧૢ"):
    try:
      bstack1l111111_opy_ = threading.current_thread().bstackSessionDriver if bstack1llllll1ll_opy_(bstack111ll1l_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡔࡧࡶࡷ࡮ࡵ࡮ࡅࡴ࡬ࡺࡪࡸࠧૣ")) else context.browser
      if context.failed is True:
        bstack1ll11lll_opy_ = []
        bstack1l11l1l1l_opy_ = []
        bstack11llll11_opy_ = []
        bstack1l11lll1_opy_ = bstack111ll1l_opy_ (u"ࠩࠪ૤")
        try:
          import traceback
          for exc in self.exception_arr:
            bstack1ll11lll_opy_.append(exc.__class__.__name__)
          for exc_tb in self.exc_traceback_arr:
            bstack1llll1lll1_opy_ = traceback.format_tb(exc_tb)
            bstack1l1111ll_opy_ = bstack111ll1l_opy_ (u"ࠪࠤࠬ૥").join(bstack1llll1lll1_opy_)
            bstack1l11l1l1l_opy_.append(bstack1l1111ll_opy_)
            bstack11llll11_opy_.append(bstack1llll1lll1_opy_[-1])
        except Exception as e:
          logger.debug(bstack1111l1ll_opy_.format(str(e)))
        bstack1l111l1ll_opy_ = bstack111ll1l_opy_ (u"ࠫࠬ૦")
        for i in range(len(bstack1ll11lll_opy_)):
          bstack1l111l1ll_opy_ += bstack1ll11lll_opy_[i] + bstack11llll11_opy_[i] + bstack111ll1l_opy_ (u"ࠬࡢ࡮ࠨ૧")
        bstack1l11lll1_opy_ = bstack111ll1l_opy_ (u"࠭ࠠࠨ૨").join(bstack1l11l1l1l_opy_)
        if not self.driver_before_scenario:
          bstack1l11ll1ll_opy_(context, bstack1l11lll1_opy_, bstack111ll1l_opy_ (u"ࠢࡦࡴࡵࡳࡷࠨ૩"))
          bstack1l1lll1l_opy_(context, bstack111ll1l_opy_ (u"ࠣࡨࡤ࡭ࡱ࡫ࡤࠣ૪"), bstack1l111l1ll_opy_)
          bstack1l111111_opy_.execute_script(bstack111ll1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࠨࡡࡤࡶ࡬ࡳࡳࠨ࠺ࠡࠤࡤࡲࡳࡵࡴࡢࡶࡨࠦ࠱ࠦࠢࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠥ࠾ࠥࢁࠢࡥࡣࡷࡥࠧࡀࠧ૫") + json.dumps(bstack1l11lll1_opy_) + bstack111ll1l_opy_ (u"ࠪ࠰ࠥࠨ࡬ࡦࡸࡨࡰࠧࡀࠠࠣࡧࡵࡶࡴࡸࠢࡾࡿࠪ૬"))
          bstack1l111111_opy_.execute_script(bstack111ll1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻࠣࡣࡦࡸ࡮ࡵ࡮ࠣ࠼ࠣࠦࡸ࡫ࡴࡔࡧࡶࡷ࡮ࡵ࡮ࡔࡶࡤࡸࡺࡹࠢ࠭ࠢࠥࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸࠨ࠺ࠡࡽࠥࡷࡹࡧࡴࡶࡵࠥ࠾ࠧ࡬ࡡࡪ࡮ࡨࡨࠧ࠲ࠠࠣࡴࡨࡥࡸࡵ࡮ࠣ࠼ࠣࠫ૭") + json.dumps(bstack111ll1l_opy_ (u"࡙ࠧ࡯࡮ࡧࠣࡷࡨ࡫࡮ࡢࡴ࡬ࡳࡸࠦࡦࡢ࡫࡯ࡩࡩࡀࠠ࡝ࡰࠥ૮") + str(bstack1l111l1ll_opy_)) + bstack111ll1l_opy_ (u"࠭ࡽࡾࠩ૯"))
      else:
        if not self.driver_before_scenario:
          bstack1l11ll1ll_opy_(context, bstack111ll1l_opy_ (u"ࠢࡇࡧࡤࡸࡺࡸࡥ࠻ࠢࠥ૰") + str(self.feature.name) + bstack111ll1l_opy_ (u"ࠣࠢࡳࡥࡸࡹࡥࡥࠣࠥ૱"), bstack111ll1l_opy_ (u"ࠤ࡬ࡲ࡫ࡵࠢ૲"))
          bstack1l1lll1l_opy_(context, bstack111ll1l_opy_ (u"ࠥࡴࡦࡹࡳࡦࡦࠥ૳"))
          bstack1l111111_opy_.execute_script(bstack111ll1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻࠣࡣࡦࡸ࡮ࡵ࡮ࠣ࠼ࠣࠦࡦࡴ࡮ࡰࡶࡤࡸࡪࠨࠬࠡࠤࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠧࡀࠠࡼࠤࡧࡥࡹࡧࠢ࠻ࠩ૴") + json.dumps(bstack111ll1l_opy_ (u"ࠧࡌࡥࡢࡶࡸࡶࡪࡀࠠࠣ૵") + str(self.feature.name) + bstack111ll1l_opy_ (u"ࠨࠠࡱࡣࡶࡷࡪࡪࠡࠣ૶")) + bstack111ll1l_opy_ (u"ࠧ࠭ࠢࠥࡰࡪࡼࡥ࡭ࠤ࠽ࠤࠧ࡯࡮ࡧࡱࠥࢁࢂ࠭૷"))
          bstack1l111111_opy_.execute_script(bstack111ll1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࡿࠧࡧࡣࡵ࡫ࡲࡲࠧࡀࠠࠣࡵࡨࡸࡘ࡫ࡳࡴ࡫ࡲࡲࡘࡺࡡࡵࡷࡶࠦ࠱ࠦࠢࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠥ࠾ࠥࢁࠢࡴࡶࡤࡸࡺࡹࠢ࠻ࠤࡳࡥࡸࡹࡥࡥࠤࢀࢁࠬ૸"))
    except Exception as e:
      logger.debug(bstack111ll1l_opy_ (u"ࠩࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡳࡡࡳ࡭ࠣࡷࡪࡹࡳࡪࡱࡱࠤࡸࡺࡡࡵࡷࡶࠤ࡮ࡴࠠࡢࡨࡷࡩࡷࠦࡦࡦࡣࡷࡹࡷ࡫࠺ࠡࡽࢀࠫૹ").format(str(e)))
  else:
    bstack1l11l11l_opy_(self, name, context, *args)
  if name in [bstack111ll1l_opy_ (u"ࠪࡥ࡫ࡺࡥࡳࡡࡩࡩࡦࡺࡵࡳࡧࠪૺ"), bstack111ll1l_opy_ (u"ࠫࡦ࡬ࡴࡦࡴࡢࡷࡨ࡫࡮ࡢࡴ࡬ࡳࠬૻ")]:
    bstack1l11l11l_opy_(self, name, context, *args)
    if (name == bstack111ll1l_opy_ (u"ࠬࡧࡦࡵࡧࡵࡣࡸࡩࡥ࡯ࡣࡵ࡭ࡴ࠭ૼ") and self.driver_before_scenario) or (
            name == bstack111ll1l_opy_ (u"࠭ࡡࡧࡶࡨࡶࡤ࡬ࡥࡢࡶࡸࡶࡪ࠭૽") and not self.driver_before_scenario):
      try:
        bstack1l111111_opy_ = threading.current_thread().bstackSessionDriver if bstack1llllll1ll_opy_(bstack111ll1l_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱࡓࡦࡵࡶ࡭ࡴࡴࡄࡳ࡫ࡹࡩࡷ࠭૾")) else context.browser
        bstack1l111111_opy_.quit()
      except Exception:
        pass
def bstack1111lllll_opy_(config, startdir):
  return bstack111ll1l_opy_ (u"ࠣࡦࡵ࡭ࡻ࡫ࡲ࠻ࠢࡾ࠴ࢂࠨ૿").format(bstack111ll1l_opy_ (u"ࠤࡅࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࠣ଀"))
notset = Notset()
def bstack1l11111l_opy_(self, name: str, default=notset, skip: bool = False):
  global bstack1l1l11ll1_opy_
  if str(name).lower() == bstack111ll1l_opy_ (u"ࠪࡨࡷ࡯ࡶࡦࡴࠪଁ"):
    return bstack111ll1l_opy_ (u"ࠦࡇࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࠥଂ")
  else:
    return bstack1l1l11ll1_opy_(self, name, default, skip)
def bstack1lll11ll_opy_(item, when):
  global bstack1l1l1ll1_opy_
  try:
    bstack1l1l1ll1_opy_(item, when)
  except Exception as e:
    pass
def bstack111l11lll_opy_():
  return
def bstack1l1ll1111_opy_(type, name, status, reason, bstack1ll11l111l_opy_, bstack11l111111_opy_):
  bstack1l1ll111l_opy_ = {
    bstack111ll1l_opy_ (u"ࠬࡧࡣࡵ࡫ࡲࡲࠬଃ"): type,
    bstack111ll1l_opy_ (u"࠭ࡡࡳࡩࡸࡱࡪࡴࡴࡴࠩ଄"): {}
  }
  if type == bstack111ll1l_opy_ (u"ࠧࡢࡰࡱࡳࡹࡧࡴࡦࠩଅ"):
    bstack1l1ll111l_opy_[bstack111ll1l_opy_ (u"ࠨࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠫଆ")][bstack111ll1l_opy_ (u"ࠩ࡯ࡩࡻ࡫࡬ࠨଇ")] = bstack1ll11l111l_opy_
    bstack1l1ll111l_opy_[bstack111ll1l_opy_ (u"ࠪࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸ࠭ଈ")][bstack111ll1l_opy_ (u"ࠫࡩࡧࡴࡢࠩଉ")] = json.dumps(str(bstack11l111111_opy_))
  if type == bstack111ll1l_opy_ (u"ࠬࡹࡥࡵࡕࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪ࠭ଊ"):
    bstack1l1ll111l_opy_[bstack111ll1l_opy_ (u"࠭ࡡࡳࡩࡸࡱࡪࡴࡴࡴࠩଋ")][bstack111ll1l_opy_ (u"ࠧ࡯ࡣࡰࡩࠬଌ")] = name
  if type == bstack111ll1l_opy_ (u"ࠨࡵࡨࡸࡘ࡫ࡳࡴ࡫ࡲࡲࡘࡺࡡࡵࡷࡶࠫ଍"):
    bstack1l1ll111l_opy_[bstack111ll1l_opy_ (u"ࠩࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠬ଎")][bstack111ll1l_opy_ (u"ࠪࡷࡹࡧࡴࡶࡵࠪଏ")] = status
    if status == bstack111ll1l_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫଐ"):
      bstack1l1ll111l_opy_[bstack111ll1l_opy_ (u"ࠬࡧࡲࡨࡷࡰࡩࡳࡺࡳࠨ଑")][bstack111ll1l_opy_ (u"࠭ࡲࡦࡣࡶࡳࡳ࠭଒")] = json.dumps(str(reason))
  bstack1lll1ll111_opy_ = bstack111ll1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࡾࢁࠬଓ").format(json.dumps(bstack1l1ll111l_opy_))
  return bstack1lll1ll111_opy_
def bstack1l11l1111_opy_(item, call, rep):
  global bstack1ll1ll1lll_opy_
  global bstack1lll1l11l1_opy_
  global bstack11l111l1_opy_
  name = bstack111ll1l_opy_ (u"ࠨࠩଔ")
  try:
    if rep.when == bstack111ll1l_opy_ (u"ࠩࡦࡥࡱࡲࠧକ"):
      bstack1l1l1l1l1_opy_ = threading.current_thread().bstack111l1111_opy_
      try:
        if not bstack11l111l1_opy_:
          name = str(rep.nodeid)
          bstack11ll11ll_opy_ = bstack1l1ll1111_opy_(bstack111ll1l_opy_ (u"ࠪࡷࡪࡺࡓࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠫଖ"), name, bstack111ll1l_opy_ (u"ࠫࠬଗ"), bstack111ll1l_opy_ (u"ࠬ࠭ଘ"), bstack111ll1l_opy_ (u"࠭ࠧଙ"), bstack111ll1l_opy_ (u"ࠧࠨଚ"))
          for driver in bstack1lll1l11l1_opy_:
            if bstack1l1l1l1l1_opy_ == driver.session_id:
              driver.execute_script(bstack11ll11ll_opy_)
      except Exception as e:
        logger.debug(bstack111ll1l_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡪࡰࠣࡷࡪࡺࡴࡪࡰࡪࠤࡸ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠢࡩࡳࡷࠦࡰࡺࡶࡨࡷࡹ࠳ࡢࡥࡦࠣࡷࡪࡹࡳࡪࡱࡱ࠾ࠥࢁࡽࠨଛ").format(str(e)))
      try:
        bstack1lll111ll1_opy_(rep.outcome.lower())
        if rep.outcome.lower() != bstack111ll1l_opy_ (u"ࠩࡶ࡯࡮ࡶࡰࡦࡦࠪଜ"):
          status = bstack111ll1l_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪଝ") if rep.outcome.lower() == bstack111ll1l_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫଞ") else bstack111ll1l_opy_ (u"ࠬࡶࡡࡴࡵࡨࡨࠬଟ")
          reason = bstack111ll1l_opy_ (u"࠭ࠧଠ")
          if status == bstack111ll1l_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧଡ"):
            reason = rep.longrepr.reprcrash.message
            if (not threading.current_thread().bstackTestErrorMessages):
              threading.current_thread().bstackTestErrorMessages = []
            threading.current_thread().bstackTestErrorMessages.append(reason)
          level = bstack111ll1l_opy_ (u"ࠨ࡫ࡱࡪࡴ࠭ଢ") if status == bstack111ll1l_opy_ (u"ࠩࡳࡥࡸࡹࡥࡥࠩଣ") else bstack111ll1l_opy_ (u"ࠪࡩࡷࡸ࡯ࡳࠩତ")
          data = name + bstack111ll1l_opy_ (u"ࠫࠥࡶࡡࡴࡵࡨࡨࠦ࠭ଥ") if status == bstack111ll1l_opy_ (u"ࠬࡶࡡࡴࡵࡨࡨࠬଦ") else name + bstack111ll1l_opy_ (u"࠭ࠠࡧࡣ࡬ࡰࡪࡪࠡࠡࠩଧ") + reason
          bstack1lll11l11l_opy_ = bstack1l1ll1111_opy_(bstack111ll1l_opy_ (u"ࠧࡢࡰࡱࡳࡹࡧࡴࡦࠩନ"), bstack111ll1l_opy_ (u"ࠨࠩ଩"), bstack111ll1l_opy_ (u"ࠩࠪପ"), bstack111ll1l_opy_ (u"ࠪࠫଫ"), level, data)
          for driver in bstack1lll1l11l1_opy_:
            if bstack1l1l1l1l1_opy_ == driver.session_id:
              driver.execute_script(bstack1lll11l11l_opy_)
      except Exception as e:
        logger.debug(bstack111ll1l_opy_ (u"ࠫࡊࡸࡲࡰࡴࠣ࡭ࡳࠦࡳࡦࡶࡷ࡭ࡳ࡭ࠠࡴࡧࡶࡷ࡮ࡵ࡮ࠡࡥࡲࡲࡹ࡫ࡸࡵࠢࡩࡳࡷࠦࡰࡺࡶࡨࡷࡹ࠳ࡢࡥࡦࠣࡷࡪࡹࡳࡪࡱࡱ࠾ࠥࢁࡽࠨବ").format(str(e)))
  except Exception as e:
    logger.debug(bstack111ll1l_opy_ (u"ࠬࡋࡲࡳࡱࡵࠤ࡮ࡴࠠࡨࡧࡷࡸ࡮ࡴࡧࠡࡵࡷࡥࡹ࡫ࠠࡪࡰࠣࡴࡾࡺࡥࡴࡶ࠰ࡦࡩࡪࠠࡵࡧࡶࡸࠥࡹࡴࡢࡶࡸࡷ࠿ࠦࡻࡾࠩଭ").format(str(e)))
  bstack1ll1ll1lll_opy_(item, call, rep)
def bstack111ll1ll1_opy_(framework_name):
  global bstack111111lll_opy_
  global bstack1ll1l1ll1l_opy_
  global bstack1lll11111l_opy_
  bstack111111lll_opy_ = framework_name
  logger.info(bstack1l111ll1l_opy_.format(bstack111111lll_opy_.split(bstack111ll1l_opy_ (u"࠭࠭ࠨମ"))[0]))
  try:
    from selenium import webdriver
    from selenium.webdriver.common.service import Service
    from selenium.webdriver.remote.webdriver import WebDriver
    if bstack1l111111l_opy_:
      Service.start = bstack11l1l11l1_opy_
      Service.stop = bstack11l111ll_opy_
      webdriver.Remote.get = bstack11ll1l111_opy_
      WebDriver.close = bstack11l1l1ll_opy_
      WebDriver.quit = bstack11l1l11ll_opy_
      webdriver.Remote.__init__ = bstack11lll1l1_opy_
      WebDriver.getAccessibilityResults = getAccessibilityResults
      WebDriver.getAccessibilityResultsSummary = getAccessibilityResultsSummary
    if not bstack1l111111l_opy_ and bstack1l11lll1l_opy_.on():
      webdriver.Remote.__init__ = bstack11ll11l11_opy_
    bstack1ll1l1ll1l_opy_ = True
  except Exception as e:
    pass
  bstack1lll1l111l_opy_()
  if not bstack1ll1l1ll1l_opy_:
    bstack1l1lll111_opy_(bstack111ll1l_opy_ (u"ࠢࡑࡣࡦ࡯ࡦ࡭ࡥࡴࠢࡱࡳࡹࠦࡩ࡯ࡵࡷࡥࡱࡲࡥࡥࠤଯ"), bstack11111llll_opy_)
  if bstack1l1l1l1l_opy_():
    try:
      from selenium.webdriver.remote.remote_connection import RemoteConnection
      RemoteConnection._get_proxy_url = bstack1l11l111_opy_
    except Exception as e:
      logger.error(bstack1ll1l1ll1_opy_.format(str(e)))
  if bstack1ll1ll11l_opy_():
    bstack1l111lll1_opy_(CONFIG, logger)
  if (bstack111ll1l_opy_ (u"ࠨࡴࡲࡦࡴࡺࠧର") in str(framework_name).lower()):
    try:
      from robot import run_cli
      from robot.output import Output
      from robot.running.status import TestStatus
      from pabot.pabot import QueueItem
      from pabot import pabot
      try:
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCreator
        WebDriverCreator._get_ff_profile = bstack111l1ll11_opy_
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCache
        WebDriverCache.close = bstack1l1llll1_opy_
      except Exception as e:
        logger.warn(bstack11ll1ll1l_opy_ + str(e))
      try:
        from AppiumLibrary.utils.applicationcache import ApplicationCache
        ApplicationCache.close = bstack11ll1l1l_opy_
      except Exception as e:
        logger.debug(bstack11llll111_opy_ + str(e))
    except Exception as e:
      bstack1l1lll111_opy_(e, bstack11ll1ll1l_opy_)
    Output.end_test = bstack1l1111ll1_opy_
    TestStatus.__init__ = bstack1lll11l1l1_opy_
    QueueItem.__init__ = bstack1ll111ll_opy_
    pabot._create_items = bstack111lllll1_opy_
    try:
      from pabot import __version__ as bstack1ll1l11ll1_opy_
      if version.parse(bstack1ll1l11ll1_opy_) >= version.parse(bstack111ll1l_opy_ (u"ࠩ࠵࠲࠶࠻࠮࠱ࠩ଱")):
        pabot._run = bstack11l1l1ll1_opy_
      elif version.parse(bstack1ll1l11ll1_opy_) >= version.parse(bstack111ll1l_opy_ (u"ࠪ࠶࠳࠷࠳࠯࠲ࠪଲ")):
        pabot._run = bstack11llll11l_opy_
      else:
        pabot._run = bstack1l1l1l1ll_opy_
    except Exception as e:
      pabot._run = bstack1l1l1l1ll_opy_
    pabot._create_command_for_execution = bstack11llll1l1_opy_
    pabot._report_results = bstack1ll11ll1_opy_
  if bstack111ll1l_opy_ (u"ࠫࡧ࡫ࡨࡢࡸࡨࠫଳ") in str(framework_name).lower():
    try:
      from behave.runner import Runner
      from behave.model import Step
    except Exception as e:
      bstack1l1lll111_opy_(e, bstack1l1l1lll_opy_)
    Runner.run_hook = bstack1111l111l_opy_
    Step.run = bstack1l11111ll_opy_
  if bstack111ll1l_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬ଴") in str(framework_name).lower():
    if not bstack1l111111l_opy_:
      return
    try:
      from pytest_selenium import pytest_selenium
      from _pytest.config import Config
      pytest_selenium.pytest_report_header = bstack1111lllll_opy_
      from pytest_selenium.drivers import browserstack
      browserstack.pytest_selenium_runtest_makereport = bstack111l11lll_opy_
      Config.getoption = bstack1l11111l_opy_
    except Exception as e:
      pass
    try:
      from pytest_bdd import reporting
      reporting.runtest_makereport = bstack1l11l1111_opy_
    except Exception as e:
      pass
def bstack1lll1l11ll_opy_():
  global CONFIG
  if bstack111ll1l_opy_ (u"࠭ࡰࡢࡴࡤࡰࡱ࡫࡬ࡴࡒࡨࡶࡕࡲࡡࡵࡨࡲࡶࡲ࠭ଵ") in CONFIG and int(CONFIG[bstack111ll1l_opy_ (u"ࠧࡱࡣࡵࡥࡱࡲࡥ࡭ࡵࡓࡩࡷࡖ࡬ࡢࡶࡩࡳࡷࡳࠧଶ")]) > 1:
    logger.warn(bstack1lll1l111_opy_)
def bstack1l1lllll1_opy_(arg, bstack11lllllll_opy_):
  global CONFIG
  global bstack1ll11111_opy_
  global bstack111l1l1ll_opy_
  global bstack1l111111l_opy_
  global bstack1ll1l1llll_opy_
  bstack1ll11ll1ll_opy_ = bstack111ll1l_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࠨଷ")
  if bstack11lllllll_opy_ and isinstance(bstack11lllllll_opy_, str):
    bstack11lllllll_opy_ = eval(bstack11lllllll_opy_)
  CONFIG = bstack11lllllll_opy_[bstack111ll1l_opy_ (u"ࠩࡆࡓࡓࡌࡉࡈࠩସ")]
  bstack1ll11111_opy_ = bstack11lllllll_opy_[bstack111ll1l_opy_ (u"ࠪࡌ࡚ࡈ࡟ࡖࡔࡏࠫହ")]
  bstack111l1l1ll_opy_ = bstack11lllllll_opy_[bstack111ll1l_opy_ (u"ࠫࡎ࡙࡟ࡂࡒࡓࡣࡆ࡛ࡔࡐࡏࡄࡘࡊ࠭଺")]
  bstack1l111111l_opy_ = bstack11lllllll_opy_[bstack111ll1l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡆ࡛ࡔࡐࡏࡄࡘࡎࡕࡎࠨ଻")]
  bstack1ll1l1llll_opy_.bstack1ll1lll111_opy_(bstack111ll1l_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡥࡳࡦࡵࡶ࡭ࡴࡴ଼ࠧ"), bstack1l111111l_opy_)
  os.environ[bstack111ll1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡆࡓࡃࡐࡉ࡜ࡕࡒࡌࠩଽ")] = bstack1ll11ll1ll_opy_
  os.environ[bstack111ll1l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡄࡑࡑࡊࡎࡍࠧା")] = json.dumps(CONFIG)
  os.environ[bstack111ll1l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡊࡘࡆࡤ࡛ࡒࡍࠩି")] = bstack1ll11111_opy_
  os.environ[bstack111ll1l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡌࡗࡤࡇࡐࡑࡡࡄ࡙࡙ࡕࡍࡂࡖࡈࠫୀ")] = str(bstack111l1l1ll_opy_)
  os.environ[bstack111ll1l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡔ࡞࡚ࡅࡔࡖࡢࡔࡑ࡛ࡇࡊࡐࠪୁ")] = str(True)
  if bstack11l111l1l_opy_(arg, [bstack111ll1l_opy_ (u"ࠬ࠳࡮ࠨୂ"), bstack111ll1l_opy_ (u"࠭࠭࠮ࡰࡸࡱࡵࡸ࡯ࡤࡧࡶࡷࡪࡹࠧୃ")]) != -1:
    os.environ[bstack111ll1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡐ࡚ࡖࡈࡗ࡙ࡥࡐࡂࡔࡄࡐࡑࡋࡌࠨୄ")] = str(True)
  if len(sys.argv) <= 1:
    logger.critical(bstack1111111l1_opy_)
    return
  bstack1lllll11_opy_()
  global bstack1l1111111_opy_
  global bstack1111ll11l_opy_
  global bstack11l11llll_opy_
  global bstack1l1l1ll1l_opy_
  global bstack1ll111l1l_opy_
  global bstack1lll11111l_opy_
  global bstack1l11ll1l_opy_
  arg.append(bstack111ll1l_opy_ (u"ࠣ࠯࡚ࠦ୅"))
  arg.append(bstack111ll1l_opy_ (u"ࠤ࡬࡫ࡳࡵࡲࡦ࠼ࡐࡳࡩࡻ࡬ࡦࠢࡤࡰࡷ࡫ࡡࡥࡻࠣ࡭ࡲࡶ࡯ࡳࡶࡨࡨ࠿ࡶࡹࡵࡧࡶࡸ࠳ࡖࡹࡵࡧࡶࡸ࡜ࡧࡲ࡯࡫ࡱ࡫ࠧ୆"))
  arg.append(bstack111ll1l_opy_ (u"ࠥ࠱࡜ࠨେ"))
  arg.append(bstack111ll1l_opy_ (u"ࠦ࡮࡭࡮ࡰࡴࡨ࠾࡙࡮ࡥࠡࡪࡲࡳࡰ࡯࡭ࡱ࡮ࠥୈ"))
  global bstack11lll1l11_opy_
  global bstack1ll1l111ll_opy_
  global bstack1ll1l11111_opy_
  global bstack1l1l111ll_opy_
  global bstack11lll1l1l_opy_
  global bstack11l1llll_opy_
  global bstack1llllll1l1_opy_
  global bstack1ll11l1l1_opy_
  global bstack1111l1111_opy_
  global bstack1l1l11ll1_opy_
  global bstack1l1l1ll1_opy_
  global bstack1ll1ll1lll_opy_
  try:
    from selenium import webdriver
    from selenium.webdriver.remote.webdriver import WebDriver
    bstack11lll1l11_opy_ = webdriver.Remote.__init__
    bstack1ll1l111ll_opy_ = WebDriver.quit
    bstack1llllll1l1_opy_ = WebDriver.close
    bstack1ll11l1l1_opy_ = WebDriver.get
  except Exception as e:
    pass
  if bstack1l1l1ll11_opy_(CONFIG) and bstack1ll11l11l_opy_():
    if bstack1lllll1l1l_opy_() < version.parse(bstack1llll11l1l_opy_):
      logger.error(bstack1ll1lll1l1_opy_.format(bstack1lllll1l1l_opy_()))
    else:
      try:
        from selenium.webdriver.remote.remote_connection import RemoteConnection
        bstack1111l1111_opy_ = RemoteConnection._get_proxy_url
      except Exception as e:
        logger.error(bstack1ll1l1ll1_opy_.format(str(e)))
  try:
    from _pytest.config import Config
    bstack1l1l11ll1_opy_ = Config.getoption
    from _pytest import runner
    bstack1l1l1ll1_opy_ = runner._update_current_test_var
  except Exception as e:
    logger.warn(e, bstack11l11l1ll_opy_)
  try:
    from pytest_bdd import reporting
    bstack1ll1ll1lll_opy_ = reporting.runtest_makereport
  except Exception as e:
    logger.debug(bstack111ll1l_opy_ (u"ࠬࡖ࡬ࡦࡣࡶࡩࠥ࡯࡮ࡴࡶࡤࡰࡱࠦࡰࡺࡶࡨࡷࡹ࠳ࡢࡥࡦࠣࡸࡴࠦࡲࡶࡰࠣࡴࡾࡺࡥࡴࡶ࠰ࡦࡩࡪࠠࡵࡧࡶࡸࡸ࠭୉"))
  bstack11l11llll_opy_ = CONFIG.get(bstack111ll1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪ୊"), {}).get(bstack111ll1l_opy_ (u"ࠧ࡭ࡱࡦࡥࡱࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩୋ"))
  bstack1l11ll1l_opy_ = True
  bstack111ll1ll1_opy_(bstack11llllll_opy_)
  os.environ[bstack111ll1l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡖࡕࡈࡖࡓࡇࡍࡆࠩୌ")] = CONFIG[bstack111ll1l_opy_ (u"ࠩࡸࡷࡪࡸࡎࡢ࡯ࡨ୍ࠫ")]
  os.environ[bstack111ll1l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡄࡇࡈࡋࡓࡔࡡࡎࡉ࡞࠭୎")] = CONFIG[bstack111ll1l_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶࡏࡪࡿࠧ୏")]
  os.environ[bstack111ll1l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡆ࡛ࡔࡐࡏࡄࡘࡎࡕࡎࠨ୐")] = bstack1l111111l_opy_.__str__()
  from _pytest.config import main as bstack1ll11lll1_opy_
  bstack1ll11lll1_opy_(arg)
def bstack1l11l1l11_opy_(arg):
  bstack111ll1ll1_opy_(bstack1lll11l1l_opy_)
  from behave.__main__ import main as bstack11l1111l_opy_
  bstack11l1111l_opy_(arg)
def bstack111ll1l1_opy_():
  logger.info(bstack11111111l_opy_)
  import argparse
  parser = argparse.ArgumentParser()
  parser.add_argument(bstack111ll1l_opy_ (u"࠭ࡳࡦࡶࡸࡴࠬ୑"), help=bstack111ll1l_opy_ (u"ࠧࡈࡧࡱࡩࡷࡧࡴࡦࠢࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠡࡥࡲࡲ࡫࡯ࡧࠨ୒"))
  parser.add_argument(bstack111ll1l_opy_ (u"ࠨ࠯ࡸࠫ୓"), bstack111ll1l_opy_ (u"ࠩ࠰࠱ࡺࡹࡥࡳࡰࡤࡱࡪ࠭୔"), help=bstack111ll1l_opy_ (u"ࠪ࡝ࡴࡻࡲࠡࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠠࡶࡵࡨࡶࡳࡧ࡭ࡦࠩ୕"))
  parser.add_argument(bstack111ll1l_opy_ (u"ࠫ࠲ࡱࠧୖ"), bstack111ll1l_opy_ (u"ࠬ࠳࠭࡬ࡧࡼࠫୗ"), help=bstack111ll1l_opy_ (u"࡙࠭ࡰࡷࡵࠤࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠣࡥࡨࡩࡥࡴࡵࠣ࡯ࡪࡿࠧ୘"))
  parser.add_argument(bstack111ll1l_opy_ (u"ࠧ࠮ࡨࠪ୙"), bstack111ll1l_opy_ (u"ࠨ࠯࠰ࡪࡷࡧ࡭ࡦࡹࡲࡶࡰ࠭୚"), help=bstack111ll1l_opy_ (u"ࠩ࡜ࡳࡺࡸࠠࡵࡧࡶࡸࠥ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࠨ୛"))
  bstack1l11ll11_opy_ = parser.parse_args()
  try:
    bstack111l1l1l1_opy_ = bstack111ll1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡪࡩࡳ࡫ࡲࡪࡥ࠱ࡽࡲࡲ࠮ࡴࡣࡰࡴࡱ࡫ࠧଡ଼")
    if bstack1l11ll11_opy_.framework and bstack1l11ll11_opy_.framework not in (bstack111ll1l_opy_ (u"ࠫࡵࡿࡴࡩࡱࡱࠫଢ଼"), bstack111ll1l_opy_ (u"ࠬࡶࡹࡵࡪࡲࡲ࠸࠭୞")):
      bstack111l1l1l1_opy_ = bstack111ll1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫࠯ࡻࡰࡰ࠳ࡹࡡ࡮ࡲ࡯ࡩࠬୟ")
    bstack1ll111lll_opy_ = os.path.join(os.path.dirname(os.path.realpath(__file__)), bstack111l1l1l1_opy_)
    bstack11111l1ll_opy_ = open(bstack1ll111lll_opy_, bstack111ll1l_opy_ (u"ࠧࡳࠩୠ"))
    bstack1lllll111_opy_ = bstack11111l1ll_opy_.read()
    bstack11111l1ll_opy_.close()
    if bstack1l11ll11_opy_.username:
      bstack1lllll111_opy_ = bstack1lllll111_opy_.replace(bstack111ll1l_opy_ (u"ࠨ࡛ࡒ࡙ࡗࡥࡕࡔࡇࡕࡒࡆࡓࡅࠨୡ"), bstack1l11ll11_opy_.username)
    if bstack1l11ll11_opy_.key:
      bstack1lllll111_opy_ = bstack1lllll111_opy_.replace(bstack111ll1l_opy_ (u"ࠩ࡜ࡓ࡚ࡘ࡟ࡂࡅࡆࡉࡘ࡙࡟ࡌࡇ࡜ࠫୢ"), bstack1l11ll11_opy_.key)
    if bstack1l11ll11_opy_.framework:
      bstack1lllll111_opy_ = bstack1lllll111_opy_.replace(bstack111ll1l_opy_ (u"ࠪ࡝ࡔ࡛ࡒࡠࡈࡕࡅࡒࡋࡗࡐࡔࡎࠫୣ"), bstack1l11ll11_opy_.framework)
    file_name = bstack111ll1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡽࡲࡲࠧ୤")
    file_path = os.path.abspath(file_name)
    bstack11l1l11l_opy_ = open(file_path, bstack111ll1l_opy_ (u"ࠬࡽࠧ୥"))
    bstack11l1l11l_opy_.write(bstack1lllll111_opy_)
    bstack11l1l11l_opy_.close()
    logger.info(bstack11l11ll1l_opy_)
    try:
      os.environ[bstack111ll1l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡌࡒࡂࡏࡈ࡛ࡔࡘࡋࠨ୦")] = bstack1l11ll11_opy_.framework if bstack1l11ll11_opy_.framework != None else bstack111ll1l_opy_ (u"ࠢࠣ୧")
      config = yaml.safe_load(bstack1lllll111_opy_)
      config[bstack111ll1l_opy_ (u"ࠨࡵࡲࡹࡷࡩࡥࠨ୨")] = bstack111ll1l_opy_ (u"ࠩࡳࡽࡹ࡮࡯࡯࠯ࡶࡩࡹࡻࡰࠨ୩")
      bstack11ll1l1l1_opy_(bstack1ll1ll1l11_opy_, config)
    except Exception as e:
      logger.debug(bstack11l11lll_opy_.format(str(e)))
  except Exception as e:
    logger.error(bstack1l1lll11l_opy_.format(str(e)))
def bstack11ll1l1l1_opy_(bstack111l11l1_opy_, config, bstack1ll1ll111l_opy_={}):
  global bstack1l111111l_opy_
  if not config:
    return
  bstack1ll1llllll_opy_ = bstack1l111l1l1_opy_ if not bstack1l111111l_opy_ else (
    bstack11ll1lll_opy_ if bstack111ll1l_opy_ (u"ࠪࡥࡵࡶࠧ୪") in config else bstack1ll11llll_opy_)
  data = {
    bstack111ll1l_opy_ (u"ࠫࡺࡹࡥࡳࡐࡤࡱࡪ࠭୫"): config[bstack111ll1l_opy_ (u"ࠬࡻࡳࡦࡴࡑࡥࡲ࡫ࠧ୬")],
    bstack111ll1l_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸࡑࡥࡺࠩ୭"): config[bstack111ll1l_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡋࡦࡻࠪ୮")],
    bstack111ll1l_opy_ (u"ࠨࡧࡹࡩࡳࡺ࡟ࡵࡻࡳࡩࠬ୯"): bstack111l11l1_opy_,
    bstack111ll1l_opy_ (u"ࠩࡨࡺࡪࡴࡴࡠࡲࡵࡳࡵ࡫ࡲࡵ࡫ࡨࡷࠬ୰"): {
      bstack111ll1l_opy_ (u"ࠪࡰࡦࡴࡧࡶࡣࡪࡩࡤ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࠨୱ"): str(config[bstack111ll1l_opy_ (u"ࠫࡸࡵࡵࡳࡥࡨࠫ୲")]) if bstack111ll1l_opy_ (u"ࠬࡹ࡯ࡶࡴࡦࡩࠬ୳") in config else bstack111ll1l_opy_ (u"ࠨࡵ࡯࡭ࡱࡳࡼࡴࠢ୴"),
      bstack111ll1l_opy_ (u"ࠧࡳࡧࡩࡩࡷࡸࡥࡳࠩ୵"): bstack11l11l111_opy_(os.getenv(bstack111ll1l_opy_ (u"ࠣࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡇࡔࡄࡑࡊ࡝ࡏࡓࡍࠥ୶"), bstack111ll1l_opy_ (u"ࠤࠥ୷"))),
      bstack111ll1l_opy_ (u"ࠪࡰࡦࡴࡧࡶࡣࡪࡩࠬ୸"): bstack111ll1l_opy_ (u"ࠫࡵࡿࡴࡩࡱࡱࠫ୹"),
      bstack111ll1l_opy_ (u"ࠬࡶࡲࡰࡦࡸࡧࡹ࠭୺"): bstack1ll1llllll_opy_,
      bstack111ll1l_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡓࡧ࡭ࡦࠩ୻"): config[bstack111ll1l_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡔࡡ࡮ࡧࠪ୼")] if config[bstack111ll1l_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡎࡢ࡯ࡨࠫ୽")] else bstack111ll1l_opy_ (u"ࠤࡸࡲࡰࡴ࡯ࡸࡰࠥ୾"),
      bstack111ll1l_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬ୿"): str(config[bstack111ll1l_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭஀")]) if bstack111ll1l_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧ஁") in config else bstack111ll1l_opy_ (u"ࠨࡵ࡯࡭ࡱࡳࡼࡴࠢஂ"),
      bstack111ll1l_opy_ (u"ࠧࡰࡵࠪஃ"): sys.platform,
      bstack111ll1l_opy_ (u"ࠨࡪࡲࡷࡹࡴࡡ࡮ࡧࠪ஄"): socket.gethostname()
    }
  }
  update(data[bstack111ll1l_opy_ (u"ࠩࡨࡺࡪࡴࡴࡠࡲࡵࡳࡵ࡫ࡲࡵ࡫ࡨࡷࠬஅ")], bstack1ll1ll111l_opy_)
  try:
    response = bstack11111l11l_opy_(bstack111ll1l_opy_ (u"ࠪࡔࡔ࡙ࡔࠨஆ"), bstack11llllll1_opy_(bstack1l1111l1l_opy_), data, {
      bstack111ll1l_opy_ (u"ࠫࡦࡻࡴࡩࠩஇ"): (config[bstack111ll1l_opy_ (u"ࠬࡻࡳࡦࡴࡑࡥࡲ࡫ࠧஈ")], config[bstack111ll1l_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸࡑࡥࡺࠩஉ")])
    })
    if response:
      logger.debug(bstack1l11l11ll_opy_.format(bstack111l11l1_opy_, str(response.json())))
  except Exception as e:
    logger.debug(bstack1llll1l111_opy_.format(str(e)))
def bstack11l11l111_opy_(framework):
  return bstack111ll1l_opy_ (u"ࠢࡼࡿ࠰ࡴࡾࡺࡨࡰࡰࡤ࡫ࡪࡴࡴ࠰ࡽࢀࠦஊ").format(str(framework), __version__) if framework else bstack111ll1l_opy_ (u"ࠣࡲࡼࡸ࡭ࡵ࡮ࡢࡩࡨࡲࡹ࠵ࡻࡾࠤ஋").format(
    __version__)
def bstack1lllll11_opy_():
  global CONFIG
  if bool(CONFIG):
    return
  try:
    bstack1l1llllll_opy_()
    logger.debug(bstack11ll1l11l_opy_.format(str(CONFIG)))
    bstack1l1l11l1l_opy_()
    bstack111111l1l_opy_()
  except Exception as e:
    logger.error(bstack111ll1l_opy_ (u"ࠤࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡹࡥࡵࡷࡳ࠰ࠥ࡫ࡲࡳࡱࡵ࠾ࠥࠨ஌") + str(e))
    sys.exit(1)
  sys.excepthook = bstack1lll1lll1_opy_
  atexit.register(bstack11l11lll1_opy_)
  signal.signal(signal.SIGINT, bstack1l1ll11l_opy_)
  signal.signal(signal.SIGTERM, bstack1l1ll11l_opy_)
def bstack1lll1lll1_opy_(exctype, value, traceback):
  global bstack1lll1l11l1_opy_
  try:
    for driver in bstack1lll1l11l1_opy_:
      driver.execute_script(
        bstack111ll1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁࠢࡢࡥࡷ࡭ࡴࡴࠢ࠻ࠢࠥࡷࡪࡺࡓࡦࡵࡶ࡭ࡴࡴࡓࡵࡣࡷࡹࡸࠨࠬࠡࠤࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠧࡀࠠࡼࠤࡶࡸࡦࡺࡵࡴࠤ࠽ࠦ࡫ࡧࡩ࡭ࡧࡧࠦ࠱ࠦࠢࡳࡧࡤࡷࡴࡴࠢ࠻ࠢࠪ஍") + json.dumps(
          bstack111ll1l_opy_ (u"ࠦࡘ࡫ࡳࡴ࡫ࡲࡲࠥ࡬ࡡࡪ࡮ࡨࡨࠥࡽࡩࡵࡪ࠽ࠤࡡࡴࠢஎ") + str(value)) + bstack111ll1l_opy_ (u"ࠬࢃࡽࠨஏ"))
  except Exception:
    pass
  bstack1lllll111l_opy_(value)
  sys.__excepthook__(exctype, value, traceback)
  sys.exit(1)
def bstack1lllll111l_opy_(message=bstack111ll1l_opy_ (u"࠭ࠧஐ")):
  global CONFIG
  try:
    if message:
      bstack1ll1ll111l_opy_ = {
        bstack111ll1l_opy_ (u"ࠧࡦࡴࡵࡳࡷ࠭஑"): str(message)
      }
      bstack11ll1l1l1_opy_(bstack111ll1l1l_opy_, CONFIG, bstack1ll1ll111l_opy_)
    else:
      bstack11ll1l1l1_opy_(bstack111ll1l1l_opy_, CONFIG)
  except Exception as e:
    logger.debug(bstack1111111l_opy_.format(str(e)))
def bstack1llllll111_opy_(bstack1ll1l111l_opy_, size):
  bstack1ll1lll1ll_opy_ = []
  while len(bstack1ll1l111l_opy_) > size:
    bstack11lllll1_opy_ = bstack1ll1l111l_opy_[:size]
    bstack1ll1lll1ll_opy_.append(bstack11lllll1_opy_)
    bstack1ll1l111l_opy_ = bstack1ll1l111l_opy_[size:]
  bstack1ll1lll1ll_opy_.append(bstack1ll1l111l_opy_)
  return bstack1ll1lll1ll_opy_
def bstack1ll1111l_opy_(args):
  if bstack111ll1l_opy_ (u"ࠨ࠯ࡰࠫஒ") in args and bstack111ll1l_opy_ (u"ࠩࡳࡨࡧ࠭ஓ") in args:
    return True
  return False
def run_on_browserstack(bstack111lll1l_opy_=None, bstack1llll11lll_opy_=None, bstack1lllll1ll_opy_=False):
  global CONFIG
  global bstack1ll11111_opy_
  global bstack111l1l1ll_opy_
  bstack1ll11ll1ll_opy_ = bstack111ll1l_opy_ (u"ࠪࠫஔ")
  bstack1lllll11l_opy_(bstack11lll11ll_opy_, logger)
  if bstack111lll1l_opy_ and isinstance(bstack111lll1l_opy_, str):
    bstack111lll1l_opy_ = eval(bstack111lll1l_opy_)
  if bstack111lll1l_opy_:
    CONFIG = bstack111lll1l_opy_[bstack111ll1l_opy_ (u"ࠫࡈࡕࡎࡇࡋࡊࠫக")]
    bstack1ll11111_opy_ = bstack111lll1l_opy_[bstack111ll1l_opy_ (u"ࠬࡎࡕࡃࡡࡘࡖࡑ࠭஖")]
    bstack111l1l1ll_opy_ = bstack111lll1l_opy_[bstack111ll1l_opy_ (u"࠭ࡉࡔࡡࡄࡔࡕࡥࡁࡖࡖࡒࡑࡆ࡚ࡅࠨ஗")]
    bstack1ll1l1llll_opy_.bstack1ll1lll111_opy_(bstack111ll1l_opy_ (u"ࠧࡊࡕࡢࡅࡕࡖ࡟ࡂࡗࡗࡓࡒࡇࡔࡆࠩ஘"), bstack111l1l1ll_opy_)
    bstack1ll11ll1ll_opy_ = bstack111ll1l_opy_ (u"ࠨࡲࡼࡸ࡭ࡵ࡮ࠨங")
  if not bstack1lllll1ll_opy_:
    if len(sys.argv) <= 1:
      logger.critical(bstack1111111l1_opy_)
      return
    if sys.argv[1] == bstack111ll1l_opy_ (u"ࠩ࠰࠱ࡻ࡫ࡲࡴ࡫ࡲࡲࠬச") or sys.argv[1] == bstack111ll1l_opy_ (u"ࠪ࠱ࡻ࠭஛"):
      logger.info(bstack111ll1l_opy_ (u"ࠫࡇࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠣࡔࡾࡺࡨࡰࡰࠣࡗࡉࡑࠠࡷࡽࢀࠫஜ").format(__version__))
      return
    if sys.argv[1] == bstack111ll1l_opy_ (u"ࠬࡹࡥࡵࡷࡳࠫ஝"):
      bstack111ll1l1_opy_()
      return
  args = sys.argv
  bstack1lllll11_opy_()
  global bstack1l1111111_opy_
  global bstack1l11ll1l_opy_
  global bstack11111l1l1_opy_
  global bstack1111ll11l_opy_
  global bstack11l11llll_opy_
  global bstack1l1l1ll1l_opy_
  global bstack1llll111l1_opy_
  global bstack1ll111l1l_opy_
  global bstack1lll11111l_opy_
  if not bstack1ll11ll1ll_opy_:
    if args[1] == bstack111ll1l_opy_ (u"࠭ࡰࡺࡶ࡫ࡳࡳ࠭ஞ") or args[1] == bstack111ll1l_opy_ (u"ࠧࡱࡻࡷ࡬ࡴࡴ࠳ࠨட"):
      bstack1ll11ll1ll_opy_ = bstack111ll1l_opy_ (u"ࠨࡲࡼࡸ࡭ࡵ࡮ࠨ஠")
      args = args[2:]
    elif args[1] == bstack111ll1l_opy_ (u"ࠩࡵࡳࡧࡵࡴࠨ஡"):
      bstack1ll11ll1ll_opy_ = bstack111ll1l_opy_ (u"ࠪࡶࡴࡨ࡯ࡵࠩ஢")
      args = args[2:]
    elif args[1] == bstack111ll1l_opy_ (u"ࠫࡵࡧࡢࡰࡶࠪண"):
      bstack1ll11ll1ll_opy_ = bstack111ll1l_opy_ (u"ࠬࡶࡡࡣࡱࡷࠫத")
      args = args[2:]
    elif args[1] == bstack111ll1l_opy_ (u"࠭ࡲࡰࡤࡲࡸ࠲࡯࡮ࡵࡧࡵࡲࡦࡲࠧ஥"):
      bstack1ll11ll1ll_opy_ = bstack111ll1l_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠳ࡩ࡯ࡶࡨࡶࡳࡧ࡬ࠨ஦")
      args = args[2:]
    elif args[1] == bstack111ll1l_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࠨ஧"):
      bstack1ll11ll1ll_opy_ = bstack111ll1l_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࠩந")
      args = args[2:]
    elif args[1] == bstack111ll1l_opy_ (u"ࠪࡦࡪ࡮ࡡࡷࡧࠪன"):
      bstack1ll11ll1ll_opy_ = bstack111ll1l_opy_ (u"ࠫࡧ࡫ࡨࡢࡸࡨࠫப")
      args = args[2:]
    else:
      if not bstack111ll1l_opy_ (u"ࠬ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࠨ஫") in CONFIG or str(CONFIG[bstack111ll1l_opy_ (u"࠭ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࠩ஬")]).lower() in [bstack111ll1l_opy_ (u"ࠧࡱࡻࡷ࡬ࡴࡴࠧ஭"), bstack111ll1l_opy_ (u"ࠨࡲࡼࡸ࡭ࡵ࡮࠴ࠩம")]:
        bstack1ll11ll1ll_opy_ = bstack111ll1l_opy_ (u"ࠩࡳࡽࡹ࡮࡯࡯ࠩய")
        args = args[1:]
      elif str(CONFIG[bstack111ll1l_opy_ (u"ࠪࡪࡷࡧ࡭ࡦࡹࡲࡶࡰ࠭ர")]).lower() == bstack111ll1l_opy_ (u"ࠫࡷࡵࡢࡰࡶࠪற"):
        bstack1ll11ll1ll_opy_ = bstack111ll1l_opy_ (u"ࠬࡸ࡯ࡣࡱࡷࠫல")
        args = args[1:]
      elif str(CONFIG[bstack111ll1l_opy_ (u"࠭ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࠩள")]).lower() == bstack111ll1l_opy_ (u"ࠧࡱࡣࡥࡳࡹ࠭ழ"):
        bstack1ll11ll1ll_opy_ = bstack111ll1l_opy_ (u"ࠨࡲࡤࡦࡴࡺࠧவ")
        args = args[1:]
      elif str(CONFIG[bstack111ll1l_opy_ (u"ࠩࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࠬஶ")]).lower() == bstack111ll1l_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࠪஷ"):
        bstack1ll11ll1ll_opy_ = bstack111ll1l_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࠫஸ")
        args = args[1:]
      elif str(CONFIG[bstack111ll1l_opy_ (u"ࠬ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࠨஹ")]).lower() == bstack111ll1l_opy_ (u"࠭ࡢࡦࡪࡤࡺࡪ࠭஺"):
        bstack1ll11ll1ll_opy_ = bstack111ll1l_opy_ (u"ࠧࡣࡧ࡫ࡥࡻ࡫ࠧ஻")
        args = args[1:]
      else:
        os.environ[bstack111ll1l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡇࡔࡄࡑࡊ࡝ࡏࡓࡍࠪ஼")] = bstack1ll11ll1ll_opy_
        bstack1ll11l111_opy_(bstack1ll1ll1111_opy_)
  global bstack11l1111ll_opy_
  if bstack111lll1l_opy_:
    try:
      os.environ[bstack111ll1l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡈࡕࡅࡒࡋࡗࡐࡔࡎࠫ஽")] = bstack1ll11ll1ll_opy_
      bstack11ll1l1l1_opy_(bstack1ll1ll11l1_opy_, CONFIG)
    except Exception as e:
      logger.debug(bstack1111111l_opy_.format(str(e)))
  global bstack11lll1l11_opy_
  global bstack1ll1l111ll_opy_
  global bstack1ll11ll11l_opy_
  global bstack1lll111l1l_opy_
  global bstack1l111l111_opy_
  global bstack1ll1l11111_opy_
  global bstack1l1l111ll_opy_
  global bstack1l1l1llll_opy_
  global bstack11lll1l1l_opy_
  global bstack11l1llll_opy_
  global bstack1llllll1l1_opy_
  global bstack1l11l11l_opy_
  global bstack1ll111l1_opy_
  global bstack1ll11l1l1_opy_
  global bstack1111l1111_opy_
  global bstack1l1l11ll1_opy_
  global bstack1l1l1ll1_opy_
  global bstack1ll1l11l_opy_
  global bstack1ll1ll1lll_opy_
  try:
    from selenium import webdriver
    from selenium.webdriver.remote.webdriver import WebDriver
    bstack11lll1l11_opy_ = webdriver.Remote.__init__
    bstack1ll1l111ll_opy_ = WebDriver.quit
    bstack1llllll1l1_opy_ = WebDriver.close
    bstack1ll11l1l1_opy_ = WebDriver.get
  except Exception as e:
    pass
  try:
    import Browser
    from subprocess import Popen
    bstack11l1111ll_opy_ = Popen.__init__
  except Exception as e:
    pass
  if bstack1l1l1ll11_opy_(CONFIG) and bstack1ll11l11l_opy_():
    if bstack1lllll1l1l_opy_() < version.parse(bstack1llll11l1l_opy_):
      logger.error(bstack1ll1lll1l1_opy_.format(bstack1lllll1l1l_opy_()))
    else:
      try:
        from selenium.webdriver.remote.remote_connection import RemoteConnection
        bstack1111l1111_opy_ = RemoteConnection._get_proxy_url
      except Exception as e:
        logger.error(bstack1ll1l1ll1_opy_.format(str(e)))
  if bstack1ll11ll1ll_opy_ != bstack111ll1l_opy_ (u"ࠪࡴࡾࡺࡨࡰࡰࠪா") or (bstack1ll11ll1ll_opy_ == bstack111ll1l_opy_ (u"ࠫࡵࡿࡴࡩࡱࡱࠫி") and not bstack111lll1l_opy_):
    bstack11ll111l1_opy_()
  if (bstack1ll11ll1ll_opy_ in [bstack111ll1l_opy_ (u"ࠬࡶࡡࡣࡱࡷࠫீ"), bstack111ll1l_opy_ (u"࠭ࡲࡰࡤࡲࡸࠬு"), bstack111ll1l_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠳ࡩ࡯ࡶࡨࡶࡳࡧ࡬ࠨூ")]):
    try:
      from robot import run_cli
      from robot.output import Output
      from robot.running.status import TestStatus
      from pabot.pabot import QueueItem
      from pabot import pabot
      try:
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCreator
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCache
        WebDriverCreator._get_ff_profile = bstack111l1ll11_opy_
        bstack1l111l111_opy_ = WebDriverCache.close
      except Exception as e:
        logger.warn(bstack11ll1ll1l_opy_ + str(e))
      try:
        from AppiumLibrary.utils.applicationcache import ApplicationCache
        bstack1lll111l1l_opy_ = ApplicationCache.close
      except Exception as e:
        logger.debug(bstack11llll111_opy_ + str(e))
    except Exception as e:
      bstack1l1lll111_opy_(e, bstack11ll1ll1l_opy_)
    if bstack1ll11ll1ll_opy_ != bstack111ll1l_opy_ (u"ࠨࡴࡲࡦࡴࡺ࠭ࡪࡰࡷࡩࡷࡴࡡ࡭ࠩ௃"):
      bstack1ll11l11l1_opy_()
    bstack1ll11ll11l_opy_ = Output.end_test
    bstack1ll1l11111_opy_ = TestStatus.__init__
    bstack1l1l1llll_opy_ = pabot._run
    bstack11lll1l1l_opy_ = QueueItem.__init__
    bstack11l1llll_opy_ = pabot._create_command_for_execution
    bstack1ll1l11l_opy_ = pabot._report_results
  if bstack1ll11ll1ll_opy_ == bstack111ll1l_opy_ (u"ࠩࡥࡩ࡭ࡧࡶࡦࠩ௄"):
    try:
      from behave.runner import Runner
      from behave.model import Step
    except Exception as e:
      bstack1l1lll111_opy_(e, bstack1l1l1lll_opy_)
    bstack1l11l11l_opy_ = Runner.run_hook
    bstack1ll111l1_opy_ = Step.run
  if bstack111ll1l_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡒࡴࡹ࡯࡯࡯ࡵࠪ௅") in CONFIG:
    os.environ[bstack111ll1l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡠࡃࡆࡇࡊ࡙ࡓࡊࡄࡌࡐࡎ࡚࡙ࡠࡅࡒࡒࡋࡏࡇࡖࡔࡄࡘࡎࡕࡎࡠ࡛ࡐࡐࠬெ")] = json.dumps(CONFIG[bstack111ll1l_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࡔࡶࡴࡪࡱࡱࡷࠬே")])
    CONFIG[bstack111ll1l_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࡕࡰࡵ࡫ࡲࡲࡸ࠭ை")].pop(bstack111ll1l_opy_ (u"ࠧࡪࡰࡦࡰࡺࡪࡥࡕࡣࡪࡷࡎࡴࡔࡦࡵࡷ࡭ࡳ࡭ࡓࡤࡱࡳࡩࠬ௉"), None)
    CONFIG[bstack111ll1l_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࡐࡲࡷ࡭ࡴࡴࡳࠨொ")].pop(bstack111ll1l_opy_ (u"ࠩࡨࡼࡨࡲࡵࡥࡧࡗࡥ࡬ࡹࡉ࡯ࡖࡨࡷࡹ࡯࡮ࡨࡕࡦࡳࡵ࡫ࠧோ"), None)
  if bstack1ll11ll1ll_opy_ == bstack111ll1l_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࠪௌ"):
    try:
      bstack1l11lll1l_opy_.launch(CONFIG, {
        bstack111ll1l_opy_ (u"ࠫ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟࡯ࡣࡰࡩ்ࠬ"): bstack111ll1l_opy_ (u"ࠬࡖࡹࡵࡧࡶࡸ࠲ࡩࡵࡤࡷࡰࡦࡪࡸࠧ௎") if bstack1lllllllll_opy_() else bstack111ll1l_opy_ (u"࠭ࡐࡺࡶࡨࡷࡹ࠭௏"),
        bstack111ll1l_opy_ (u"ࠧࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡺࡪࡸࡳࡪࡱࡱࠫௐ"): bstack1l1ll1lll_opy_.version(),
        bstack111ll1l_opy_ (u"ࠨࡵࡧ࡯ࡤࡼࡥࡳࡵ࡬ࡳࡳ࠭௑"): __version__
      })
      if bstack1l111111l_opy_ and bstack111l1l11l_opy_.bstack1l1ll1ll1_opy_(CONFIG):
        bstack11l1lll11_opy_, bstack111l1l11_opy_ = bstack111l1l11l_opy_.bstack11111lll_opy_(CONFIG, bstack1ll11ll1ll_opy_, bstack1l1ll1lll_opy_.version());
        if not bstack11l1lll11_opy_ is None:
          os.environ[bstack111ll1l_opy_ (u"ࠩࡅࡗࡤࡇ࠱࠲࡛ࡢࡎ࡜࡚ࠧ௒")] = bstack11l1lll11_opy_;
          os.environ[bstack111ll1l_opy_ (u"ࠪࡆࡘࡥࡁ࠲࠳࡜ࡣ࡙ࡋࡓࡕࡡࡕ࡙ࡓࡥࡉࡅࠩ௓")] = str(bstack111l1l11_opy_);
      from _pytest.config import Config
      bstack1l1l11ll1_opy_ = Config.getoption
      from _pytest import runner
      bstack1l1l1ll1_opy_ = runner._update_current_test_var
    except Exception as e:
      logger.warn(e, bstack11l11l1ll_opy_)
    try:
      from pytest_bdd import reporting
      bstack1ll1ll1lll_opy_ = reporting.runtest_makereport
    except Exception as e:
      logger.debug(bstack111ll1l_opy_ (u"ࠫࡕࡲࡥࡢࡵࡨࠤ࡮ࡴࡳࡵࡣ࡯ࡰࠥࡶࡹࡵࡧࡶࡸ࠲ࡨࡤࡥࠢࡷࡳࠥࡸࡵ࡯ࠢࡳࡽࡹ࡫ࡳࡵ࠯ࡥࡨࡩࠦࡴࡦࡵࡷࡷࠬ௔"))
  if bstack1ll11ll1ll_opy_ == bstack111ll1l_opy_ (u"ࠬࡶࡹࡵࡪࡲࡲࠬ௕"):
    bstack1l11ll1l_opy_ = True
    if bstack111lll1l_opy_ and bstack1lllll1ll_opy_:
      bstack11l11llll_opy_ = CONFIG.get(bstack111ll1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪ௖"), {}).get(bstack111ll1l_opy_ (u"ࠧ࡭ࡱࡦࡥࡱࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩௗ"))
      bstack111ll1ll1_opy_(bstack1111l1ll1_opy_)
    elif bstack111lll1l_opy_:
      bstack11l11llll_opy_ = CONFIG.get(bstack111ll1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࡌࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬ௘"), {}).get(bstack111ll1l_opy_ (u"ࠩ࡯ࡳࡨࡧ࡬ࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫ௙"))
      global bstack1lll1l11l1_opy_
      try:
        if bstack1ll1111l_opy_(bstack111lll1l_opy_[bstack111ll1l_opy_ (u"ࠪࡪ࡮ࡲࡥࡠࡰࡤࡱࡪ࠭௚")]) and multiprocessing.current_process().name == bstack111ll1l_opy_ (u"ࠫ࠵࠭௛"):
          bstack111lll1l_opy_[bstack111ll1l_opy_ (u"ࠬ࡬ࡩ࡭ࡧࡢࡲࡦࡳࡥࠨ௜")].remove(bstack111ll1l_opy_ (u"࠭࠭࡮ࠩ௝"))
          bstack111lll1l_opy_[bstack111ll1l_opy_ (u"ࠧࡧ࡫࡯ࡩࡤࡴࡡ࡮ࡧࠪ௞")].remove(bstack111ll1l_opy_ (u"ࠨࡲࡧࡦࠬ௟"))
          bstack111lll1l_opy_[bstack111ll1l_opy_ (u"ࠩࡩ࡭ࡱ࡫࡟࡯ࡣࡰࡩࠬ௠")] = bstack111lll1l_opy_[bstack111ll1l_opy_ (u"ࠪࡪ࡮ࡲࡥࡠࡰࡤࡱࡪ࠭௡")][0]
          with open(bstack111lll1l_opy_[bstack111ll1l_opy_ (u"ࠫ࡫࡯࡬ࡦࡡࡱࡥࡲ࡫ࠧ௢")], bstack111ll1l_opy_ (u"ࠬࡸࠧ௣")) as f:
            bstack11llll1l_opy_ = f.read()
          bstack111l1l1l_opy_ = bstack111ll1l_opy_ (u"ࠨࠢࠣࡨࡵࡳࡲࠦࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤࡹࡤ࡬ࠢ࡬ࡱࡵࡵࡲࡵࠢࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠ࡫ࡱ࡭ࡹ࡯ࡡ࡭࡫ࡽࡩࡀࠦࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡯࡮ࡪࡶ࡬ࡥࡱ࡯ࡺࡦࠪࡾࢁ࠮ࡁࠠࡧࡴࡲࡱࠥࡶࡤࡣࠢ࡬ࡱࡵࡵࡲࡵࠢࡓࡨࡧࡁࠠࡰࡩࡢࡨࡧࠦ࠽ࠡࡒࡧࡦ࠳ࡪ࡯ࡠࡤࡵࡩࡦࡱ࠻ࠋࡦࡨࡪࠥࡳ࡯ࡥࡡࡥࡶࡪࡧ࡫ࠩࡵࡨࡰ࡫࠲ࠠࡢࡴࡪ࠰ࠥࡺࡥ࡮ࡲࡲࡶࡦࡸࡹࠡ࠿ࠣ࠴࠮ࡀࠊࠡࠢࡷࡶࡾࡀࠊࠡࠢࠣࠤࡦࡸࡧࠡ࠿ࠣࡷࡹࡸࠨࡪࡰࡷࠬࡦࡸࡧࠪ࠭࠴࠴࠮ࠐࠠࠡࡧࡻࡧࡪࡶࡴࠡࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤࡦࡹࠠࡦ࠼ࠍࠤࠥࠦࠠࡱࡣࡶࡷࠏࠦࠠࡰࡩࡢࡨࡧ࠮ࡳࡦ࡮ࡩ࠰ࡦࡸࡧ࠭ࡶࡨࡱࡵࡵࡲࡢࡴࡼ࠭ࠏࡖࡤࡣ࠰ࡧࡳࡤࡨࠠ࠾ࠢࡰࡳࡩࡥࡢࡳࡧࡤ࡯ࠏࡖࡤࡣ࠰ࡧࡳࡤࡨࡲࡦࡣ࡮ࠤࡂࠦ࡭ࡰࡦࡢࡦࡷ࡫ࡡ࡬ࠌࡓࡨࡧ࠮ࠩ࠯ࡵࡨࡸࡤࡺࡲࡢࡥࡨࠬ࠮ࡢ࡮ࠣࠤࠥ௤").format(str(bstack111lll1l_opy_))
          bstack1llllllll1_opy_ = bstack111l1l1l_opy_ + bstack11llll1l_opy_
          bstack111l1llll_opy_ = bstack111lll1l_opy_[bstack111ll1l_opy_ (u"ࠧࡧ࡫࡯ࡩࡤࡴࡡ࡮ࡧࠪ௥")] + bstack111ll1l_opy_ (u"ࠨࡡࡥࡷࡹࡧࡣ࡬ࡡࡷࡩࡲࡶ࠮ࡱࡻࠪ௦")
          with open(bstack111l1llll_opy_, bstack111ll1l_opy_ (u"ࠩࡺࠫ௧")):
            pass
          with open(bstack111l1llll_opy_, bstack111ll1l_opy_ (u"ࠥࡻ࠰ࠨ௨")) as f:
            f.write(bstack1llllllll1_opy_)
          import subprocess
          bstack1ll11llll1_opy_ = subprocess.run([bstack111ll1l_opy_ (u"ࠦࡵࡿࡴࡩࡱࡱࠦ௩"), bstack111l1llll_opy_])
          if os.path.exists(bstack111l1llll_opy_):
            os.unlink(bstack111l1llll_opy_)
          os._exit(bstack1ll11llll1_opy_.returncode)
        else:
          if bstack1ll1111l_opy_(bstack111lll1l_opy_[bstack111ll1l_opy_ (u"ࠬ࡬ࡩ࡭ࡧࡢࡲࡦࡳࡥࠨ௪")]):
            bstack111lll1l_opy_[bstack111ll1l_opy_ (u"࠭ࡦࡪ࡮ࡨࡣࡳࡧ࡭ࡦࠩ௫")].remove(bstack111ll1l_opy_ (u"ࠧ࠮࡯ࠪ௬"))
            bstack111lll1l_opy_[bstack111ll1l_opy_ (u"ࠨࡨ࡬ࡰࡪࡥ࡮ࡢ࡯ࡨࠫ௭")].remove(bstack111ll1l_opy_ (u"ࠩࡳࡨࡧ࠭௮"))
            bstack111lll1l_opy_[bstack111ll1l_opy_ (u"ࠪࡪ࡮ࡲࡥࡠࡰࡤࡱࡪ࠭௯")] = bstack111lll1l_opy_[bstack111ll1l_opy_ (u"ࠫ࡫࡯࡬ࡦࡡࡱࡥࡲ࡫ࠧ௰")][0]
          bstack111ll1ll1_opy_(bstack1111l1ll1_opy_)
          sys.path.append(os.path.dirname(os.path.abspath(bstack111lll1l_opy_[bstack111ll1l_opy_ (u"ࠬ࡬ࡩ࡭ࡧࡢࡲࡦࡳࡥࠨ௱")])))
          sys.argv = sys.argv[2:]
          mod_globals = globals()
          mod_globals[bstack111ll1l_opy_ (u"࠭࡟ࡠࡰࡤࡱࡪࡥ࡟ࠨ௲")] = bstack111ll1l_opy_ (u"ࠧࡠࡡࡰࡥ࡮ࡴ࡟ࡠࠩ௳")
          mod_globals[bstack111ll1l_opy_ (u"ࠨࡡࡢࡪ࡮ࡲࡥࡠࡡࠪ௴")] = os.path.abspath(bstack111lll1l_opy_[bstack111ll1l_opy_ (u"ࠩࡩ࡭ࡱ࡫࡟࡯ࡣࡰࡩࠬ௵")])
          exec(open(bstack111lll1l_opy_[bstack111ll1l_opy_ (u"ࠪࡪ࡮ࡲࡥࡠࡰࡤࡱࡪ࠭௶")]).read(), mod_globals)
      except BaseException as e:
        try:
          traceback.print_exc()
          logger.error(bstack111ll1l_opy_ (u"ࠫࡈࡧࡵࡨࡪࡷࠤࡊࡾࡣࡦࡲࡷ࡭ࡴࡴ࠺ࠡࡽࢀࠫ௷").format(str(e)))
          for driver in bstack1lll1l11l1_opy_:
            bstack1llll11lll_opy_.append({
              bstack111ll1l_opy_ (u"ࠬࡴࡡ࡮ࡧࠪ௸"): bstack111lll1l_opy_[bstack111ll1l_opy_ (u"࠭ࡦࡪ࡮ࡨࡣࡳࡧ࡭ࡦࠩ௹")],
              bstack111ll1l_opy_ (u"ࠧࡦࡴࡵࡳࡷ࠭௺"): str(e),
              bstack111ll1l_opy_ (u"ࠨ࡫ࡱࡨࡪࡾࠧ௻"): multiprocessing.current_process().name
            })
            driver.execute_script(
              bstack111ll1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࠨࡡࡤࡶ࡬ࡳࡳࠨ࠺ࠡࠤࡶࡩࡹ࡙ࡥࡴࡵ࡬ࡳࡳ࡙ࡴࡢࡶࡸࡷࠧ࠲ࠠࠣࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠦ࠿ࠦࡻࠣࡵࡷࡥࡹࡻࡳࠣ࠼ࠥࡪࡦ࡯࡬ࡦࡦࠥ࠰ࠥࠨࡲࡦࡣࡶࡳࡳࠨ࠺ࠡࠩ௼") + json.dumps(
                bstack111ll1l_opy_ (u"ࠥࡗࡪࡹࡳࡪࡱࡱࠤ࡫ࡧࡩ࡭ࡧࡧࠤࡼ࡯ࡴࡩ࠼ࠣࡠࡳࠨ௽") + str(e)) + bstack111ll1l_opy_ (u"ࠫࢂࢃࠧ௾"))
        except Exception:
          pass
      finally:
        try:
          for driver in bstack1lll1l11l1_opy_:
            driver.quit()
        except Exception as e:
          pass
    else:
      percy.init(bstack111l1l1ll_opy_, CONFIG, logger)
      bstack1ll1l1l1_opy_()
      bstack1lll1l11ll_opy_()
      bstack11lllllll_opy_ = {
        bstack111ll1l_opy_ (u"ࠬ࡬ࡩ࡭ࡧࡢࡲࡦࡳࡥࠨ௿"): args[0],
        bstack111ll1l_opy_ (u"࠭ࡃࡐࡐࡉࡍࡌ࠭ఀ"): CONFIG,
        bstack111ll1l_opy_ (u"ࠧࡉࡗࡅࡣ࡚ࡘࡌࠨఁ"): bstack1ll11111_opy_,
        bstack111ll1l_opy_ (u"ࠨࡋࡖࡣࡆࡖࡐࡠࡃࡘࡘࡔࡓࡁࡕࡇࠪం"): bstack111l1l1ll_opy_
      }
      percy.bstack1ll1l111_opy_()
      if bstack111ll1l_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬః") in CONFIG:
        bstack11l11l1l_opy_ = []
        manager = multiprocessing.Manager()
        bstack111111ll_opy_ = manager.list()
        if bstack1ll1111l_opy_(args):
          for index, platform in enumerate(CONFIG[bstack111ll1l_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ఄ")]):
            if index == 0:
              bstack11lllllll_opy_[bstack111ll1l_opy_ (u"ࠫ࡫࡯࡬ࡦࡡࡱࡥࡲ࡫ࠧఅ")] = args
            bstack11l11l1l_opy_.append(multiprocessing.Process(name=str(index),
                                                       target=run_on_browserstack,
                                                       args=(bstack11lllllll_opy_, bstack111111ll_opy_)))
        else:
          for index, platform in enumerate(CONFIG[bstack111ll1l_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨఆ")]):
            bstack11l11l1l_opy_.append(multiprocessing.Process(name=str(index),
                                                       target=run_on_browserstack,
                                                       args=(bstack11lllllll_opy_, bstack111111ll_opy_)))
        for t in bstack11l11l1l_opy_:
          t.start()
        for t in bstack11l11l1l_opy_:
          t.join()
        bstack1llll111l1_opy_ = list(bstack111111ll_opy_)
      else:
        if bstack1ll1111l_opy_(args):
          bstack11lllllll_opy_[bstack111ll1l_opy_ (u"࠭ࡦࡪ࡮ࡨࡣࡳࡧ࡭ࡦࠩఇ")] = args
          test = multiprocessing.Process(name=str(0),
                                         target=run_on_browserstack, args=(bstack11lllllll_opy_,))
          test.start()
          test.join()
        else:
          bstack111ll1ll1_opy_(bstack1111l1ll1_opy_)
          sys.path.append(os.path.dirname(os.path.abspath(args[0])))
          mod_globals = globals()
          mod_globals[bstack111ll1l_opy_ (u"ࠧࡠࡡࡱࡥࡲ࡫࡟ࡠࠩఈ")] = bstack111ll1l_opy_ (u"ࠨࡡࡢࡱࡦ࡯࡮ࡠࡡࠪఉ")
          mod_globals[bstack111ll1l_opy_ (u"ࠩࡢࡣ࡫࡯࡬ࡦࡡࡢࠫఊ")] = os.path.abspath(args[0])
          sys.argv = sys.argv[2:]
          exec(open(args[0]).read(), mod_globals)
  elif bstack1ll11ll1ll_opy_ == bstack111ll1l_opy_ (u"ࠪࡴࡦࡨ࡯ࡵࠩఋ") or bstack1ll11ll1ll_opy_ == bstack111ll1l_opy_ (u"ࠫࡷࡵࡢࡰࡶࠪఌ"):
    try:
      from pabot import pabot
    except Exception as e:
      bstack1l1lll111_opy_(e, bstack11ll1ll1l_opy_)
    bstack1ll1l1l1_opy_()
    bstack111ll1ll1_opy_(bstack111111l11_opy_)
    if bstack111ll1l_opy_ (u"ࠬ࠳࠭ࡱࡴࡲࡧࡪࡹࡳࡦࡵࠪ఍") in args:
      i = args.index(bstack111ll1l_opy_ (u"࠭࠭࠮ࡲࡵࡳࡨ࡫ࡳࡴࡧࡶࠫఎ"))
      args.pop(i)
      args.pop(i)
    args.insert(0, str(bstack1l1111111_opy_))
    args.insert(0, str(bstack111ll1l_opy_ (u"ࠧ࠮࠯ࡳࡶࡴࡩࡥࡴࡵࡨࡷࠬఏ")))
    pabot.main(args)
  elif bstack1ll11ll1ll_opy_ == bstack111ll1l_opy_ (u"ࠨࡴࡲࡦࡴࡺ࠭ࡪࡰࡷࡩࡷࡴࡡ࡭ࠩఐ"):
    try:
      from robot import run_cli
    except Exception as e:
      bstack1l1lll111_opy_(e, bstack11ll1ll1l_opy_)
    for a in args:
      if bstack111ll1l_opy_ (u"ࠩࡅࡗ࡙ࡇࡃࡌࡒࡏࡅ࡙ࡌࡏࡓࡏࡌࡒࡉࡋࡘࠨ఑") in a:
        bstack1111ll11l_opy_ = int(a.split(bstack111ll1l_opy_ (u"ࠪ࠾ࠬఒ"))[1])
      if bstack111ll1l_opy_ (u"ࠫࡇ࡙ࡔࡂࡅࡎࡈࡊࡌࡌࡐࡅࡄࡐࡎࡊࡅࡏࡖࡌࡊࡎࡋࡒࠨఓ") in a:
        bstack11l11llll_opy_ = str(a.split(bstack111ll1l_opy_ (u"ࠬࡀࠧఔ"))[1])
      if bstack111ll1l_opy_ (u"࠭ࡂࡔࡖࡄࡇࡐࡉࡌࡊࡃࡕࡋࡘ࠭క") in a:
        bstack1l1l1ll1l_opy_ = str(a.split(bstack111ll1l_opy_ (u"ࠧ࠻ࠩఖ"))[1])
    bstack1lll1ll1l1_opy_ = None
    if bstack111ll1l_opy_ (u"ࠨ࠯࠰ࡦࡸࡺࡡࡤ࡭ࡢ࡭ࡹ࡫࡭ࡠ࡫ࡱࡨࡪࡾࠧగ") in args:
      i = args.index(bstack111ll1l_opy_ (u"ࠩ࠰࠱ࡧࡹࡴࡢࡥ࡮ࡣ࡮ࡺࡥ࡮ࡡ࡬ࡲࡩ࡫ࡸࠨఘ"))
      args.pop(i)
      bstack1lll1ll1l1_opy_ = args.pop(i)
    if bstack1lll1ll1l1_opy_ is not None:
      global bstack111lll11l_opy_
      bstack111lll11l_opy_ = bstack1lll1ll1l1_opy_
    bstack111ll1ll1_opy_(bstack111111l11_opy_)
    run_cli(args)
  elif bstack1ll11ll1ll_opy_ == bstack111ll1l_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࠪఙ"):
    bstack1llll1111_opy_ = bstack1l1ll1lll_opy_(args, logger, CONFIG, bstack1l111111l_opy_)
    bstack1llll1111_opy_.bstack1ll1l1lll_opy_()
    bstack1ll1l1l1_opy_()
    bstack11111l1l1_opy_ = True
    bstack1lll11111l_opy_ = bstack1llll1111_opy_.bstack1lll111111_opy_()
    bstack1llll1111_opy_.bstack11lllllll_opy_(bstack11l111l1_opy_)
    bstack1ll111l1l_opy_ = bstack1llll1111_opy_.bstack1lll111l_opy_(bstack1l1lllll1_opy_, {
      bstack111ll1l_opy_ (u"ࠫࡍ࡛ࡂࡠࡗࡕࡐࠬచ"): bstack1ll11111_opy_,
      bstack111ll1l_opy_ (u"ࠬࡏࡓࡠࡃࡓࡔࡤࡇࡕࡕࡑࡐࡅ࡙ࡋࠧఛ"): bstack111l1l1ll_opy_,
      bstack111ll1l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡇࡕࡕࡑࡐࡅ࡙ࡏࡏࡏࠩజ"): bstack1l111111l_opy_
    })
  elif bstack1ll11ll1ll_opy_ == bstack111ll1l_opy_ (u"ࠧࡣࡧ࡫ࡥࡻ࡫ࠧఝ"):
    try:
      from behave.__main__ import main as bstack11l1111l_opy_
      from behave.configuration import Configuration
    except Exception as e:
      bstack1l1lll111_opy_(e, bstack1l1l1lll_opy_)
    bstack1ll1l1l1_opy_()
    bstack11111l1l1_opy_ = True
    bstack1l111ll1_opy_ = 1
    if bstack111ll1l_opy_ (u"ࠨࡲࡤࡶࡦࡲ࡬ࡦ࡮ࡶࡔࡪࡸࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨఞ") in CONFIG:
      bstack1l111ll1_opy_ = CONFIG[bstack111ll1l_opy_ (u"ࠩࡳࡥࡷࡧ࡬࡭ࡧ࡯ࡷࡕ࡫ࡲࡑ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩట")]
    bstack1lll11ll1_opy_ = int(bstack1l111ll1_opy_) * int(len(CONFIG[bstack111ll1l_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ఠ")]))
    config = Configuration(args)
    bstack1lll11l111_opy_ = config.paths
    if len(bstack1lll11l111_opy_) == 0:
      import glob
      pattern = bstack111ll1l_opy_ (u"ࠫ࠯࠰࠯ࠫ࠰ࡩࡩࡦࡺࡵࡳࡧࠪడ")
      bstack1llll1ll11_opy_ = glob.glob(pattern, recursive=True)
      args.extend(bstack1llll1ll11_opy_)
      config = Configuration(args)
      bstack1lll11l111_opy_ = config.paths
    bstack1l11l1lll_opy_ = [os.path.normpath(item) for item in bstack1lll11l111_opy_]
    bstack1lllll1lll_opy_ = [os.path.normpath(item) for item in args]
    bstack1l1l11111_opy_ = [item for item in bstack1lllll1lll_opy_ if item not in bstack1l11l1lll_opy_]
    import platform as pf
    if pf.system().lower() == bstack111ll1l_opy_ (u"ࠬࡽࡩ࡯ࡦࡲࡻࡸ࠭ఢ"):
      from pathlib import PureWindowsPath, PurePosixPath
      bstack1l11l1lll_opy_ = [str(PurePosixPath(PureWindowsPath(bstack1lll1lll11_opy_)))
                    for bstack1lll1lll11_opy_ in bstack1l11l1lll_opy_]
    bstack1l1l1l11l_opy_ = []
    for spec in bstack1l11l1lll_opy_:
      bstack1lll1111ll_opy_ = []
      bstack1lll1111ll_opy_ += bstack1l1l11111_opy_
      bstack1lll1111ll_opy_.append(spec)
      bstack1l1l1l11l_opy_.append(bstack1lll1111ll_opy_)
    execution_items = []
    for bstack1lll1111ll_opy_ in bstack1l1l1l11l_opy_:
      for index, _ in enumerate(CONFIG[bstack111ll1l_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩణ")]):
        item = {}
        item[bstack111ll1l_opy_ (u"ࠧࡢࡴࡪࠫత")] = bstack111ll1l_opy_ (u"ࠨࠢࠪథ").join(bstack1lll1111ll_opy_)
        item[bstack111ll1l_opy_ (u"ࠩ࡬ࡲࡩ࡫ࡸࠨద")] = index
        execution_items.append(item)
    bstack11l1111l1_opy_ = bstack1llllll111_opy_(execution_items, bstack1lll11ll1_opy_)
    for execution_item in bstack11l1111l1_opy_:
      bstack11l11l1l_opy_ = []
      for item in execution_item:
        bstack11l11l1l_opy_.append(bstack111l1111l_opy_(name=str(item[bstack111ll1l_opy_ (u"ࠪ࡭ࡳࡪࡥࡹࠩధ")]),
                                             target=bstack1l11l1l11_opy_,
                                             args=(item[bstack111ll1l_opy_ (u"ࠫࡦࡸࡧࠨన")],)))
      for t in bstack11l11l1l_opy_:
        t.start()
      for t in bstack11l11l1l_opy_:
        t.join()
  else:
    bstack1ll11l111_opy_(bstack1ll1ll1111_opy_)
  if not bstack111lll1l_opy_:
    bstack1lll1ll1l_opy_()
def browserstack_initialize(bstack1ll1ll1l1l_opy_=None):
  run_on_browserstack(bstack1ll1ll1l1l_opy_, None, True)
def bstack1lll1ll1l_opy_():
  global CONFIG
  bstack1l11lll1l_opy_.stop()
  bstack1l11lll1l_opy_.bstack111l11l11_opy_()
  if bstack111l1l11l_opy_.bstack1l1ll1ll1_opy_(CONFIG):
    bstack111l1l11l_opy_.bstack1lll1l1ll1_opy_()
  [bstack1ll1l1lll1_opy_, bstack1111lll1l_opy_] = bstack111ll11l_opy_()
  if bstack1ll1l1lll1_opy_ is not None and bstack11lll1lll_opy_() != -1:
    sessions = bstack11l1lll1_opy_(bstack1ll1l1lll1_opy_)
    bstack1111111ll_opy_(sessions, bstack1111lll1l_opy_)
def bstack1llll1l1l_opy_(bstack1ll1l11l1l_opy_):
  if bstack1ll1l11l1l_opy_:
    return bstack1ll1l11l1l_opy_.capitalize()
  else:
    return bstack1ll1l11l1l_opy_
def bstack11ll1lll1_opy_(bstack11llll1ll_opy_):
  if bstack111ll1l_opy_ (u"ࠬࡴࡡ࡮ࡧࠪ఩") in bstack11llll1ll_opy_ and bstack11llll1ll_opy_[bstack111ll1l_opy_ (u"࠭࡮ࡢ࡯ࡨࠫప")] != bstack111ll1l_opy_ (u"ࠧࠨఫ"):
    return bstack11llll1ll_opy_[bstack111ll1l_opy_ (u"ࠨࡰࡤࡱࡪ࠭బ")]
  else:
    bstack1ll1ll11_opy_ = bstack111ll1l_opy_ (u"ࠤࠥభ")
    if bstack111ll1l_opy_ (u"ࠪࡨࡪࡼࡩࡤࡧࠪమ") in bstack11llll1ll_opy_ and bstack11llll1ll_opy_[bstack111ll1l_opy_ (u"ࠫࡩ࡫ࡶࡪࡥࡨࠫయ")] != None:
      bstack1ll1ll11_opy_ += bstack11llll1ll_opy_[bstack111ll1l_opy_ (u"ࠬࡪࡥࡷ࡫ࡦࡩࠬర")] + bstack111ll1l_opy_ (u"ࠨࠬࠡࠤఱ")
      if bstack11llll1ll_opy_[bstack111ll1l_opy_ (u"ࠧࡰࡵࠪల")] == bstack111ll1l_opy_ (u"ࠣ࡫ࡲࡷࠧళ"):
        bstack1ll1ll11_opy_ += bstack111ll1l_opy_ (u"ࠤ࡬ࡓࡘࠦࠢఴ")
      bstack1ll1ll11_opy_ += (bstack11llll1ll_opy_[bstack111ll1l_opy_ (u"ࠪࡳࡸࡥࡶࡦࡴࡶ࡭ࡴࡴࠧవ")] or bstack111ll1l_opy_ (u"ࠫࠬశ"))
      return bstack1ll1ll11_opy_
    else:
      bstack1ll1ll11_opy_ += bstack1llll1l1l_opy_(bstack11llll1ll_opy_[bstack111ll1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࠭ష")]) + bstack111ll1l_opy_ (u"ࠨࠠࠣస") + (
              bstack11llll1ll_opy_[bstack111ll1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡠࡸࡨࡶࡸ࡯࡯࡯ࠩహ")] or bstack111ll1l_opy_ (u"ࠨࠩ఺")) + bstack111ll1l_opy_ (u"ࠤ࠯ࠤࠧ఻")
      if bstack11llll1ll_opy_[bstack111ll1l_opy_ (u"ࠪࡳࡸ఼࠭")] == bstack111ll1l_opy_ (u"ࠦ࡜࡯࡮ࡥࡱࡺࡷࠧఽ"):
        bstack1ll1ll11_opy_ += bstack111ll1l_opy_ (u"ࠧ࡝ࡩ࡯ࠢࠥా")
      bstack1ll1ll11_opy_ += bstack11llll1ll_opy_[bstack111ll1l_opy_ (u"࠭࡯ࡴࡡࡹࡩࡷࡹࡩࡰࡰࠪి")] or bstack111ll1l_opy_ (u"ࠧࠨీ")
      return bstack1ll1ll11_opy_
def bstack1l1ll1l11_opy_(bstack1l1ll1ll_opy_):
  if bstack1l1ll1ll_opy_ == bstack111ll1l_opy_ (u"ࠣࡦࡲࡲࡪࠨు"):
    return bstack111ll1l_opy_ (u"ࠩ࠿ࡸࡩࠦࡣ࡭ࡣࡶࡷࡂࠨࡢࡴࡶࡤࡧࡰ࠳ࡤࡢࡶࡤࠦࠥࡹࡴࡺ࡮ࡨࡁࠧࡩ࡯࡭ࡱࡵ࠾࡬ࡸࡥࡦࡰ࠾ࠦࡃࡂࡦࡰࡰࡷࠤࡨࡵ࡬ࡰࡴࡀࠦ࡬ࡸࡥࡦࡰࠥࡂࡈࡵ࡭ࡱ࡮ࡨࡸࡪࡪ࠼࠰ࡨࡲࡲࡹࡄ࠼࠰ࡶࡧࡂࠬూ")
  elif bstack1l1ll1ll_opy_ == bstack111ll1l_opy_ (u"ࠥࡪࡦ࡯࡬ࡦࡦࠥృ"):
    return bstack111ll1l_opy_ (u"ࠫࡁࡺࡤࠡࡥ࡯ࡥࡸࡹ࠽ࠣࡤࡶࡸࡦࡩ࡫࠮ࡦࡤࡸࡦࠨࠠࡴࡶࡼࡰࡪࡃࠢࡤࡱ࡯ࡳࡷࡀࡲࡦࡦ࠾ࠦࡃࡂࡦࡰࡰࡷࠤࡨࡵ࡬ࡰࡴࡀࠦࡷ࡫ࡤࠣࡀࡉࡥ࡮ࡲࡥࡥ࠾࠲ࡪࡴࡴࡴ࠿࠾࠲ࡸࡩࡄࠧౄ")
  elif bstack1l1ll1ll_opy_ == bstack111ll1l_opy_ (u"ࠧࡶࡡࡴࡵࡨࡨࠧ౅"):
    return bstack111ll1l_opy_ (u"࠭࠼ࡵࡦࠣࡧࡱࡧࡳࡴ࠿ࠥࡦࡸࡺࡡࡤ࡭࠰ࡨࡦࡺࡡࠣࠢࡶࡸࡾࡲࡥ࠾ࠤࡦࡳࡱࡵࡲ࠻ࡩࡵࡩࡪࡴ࠻ࠣࡀ࠿ࡪࡴࡴࡴࠡࡥࡲࡰࡴࡸ࠽ࠣࡩࡵࡩࡪࡴࠢ࠿ࡒࡤࡷࡸ࡫ࡤ࠽࠱ࡩࡳࡳࡺ࠾࠽࠱ࡷࡨࡃ࠭ె")
  elif bstack1l1ll1ll_opy_ == bstack111ll1l_opy_ (u"ࠢࡦࡴࡵࡳࡷࠨే"):
    return bstack111ll1l_opy_ (u"ࠨ࠾ࡷࡨࠥࡩ࡬ࡢࡵࡶࡁࠧࡨࡳࡵࡣࡦ࡯࠲ࡪࡡࡵࡣࠥࠤࡸࡺࡹ࡭ࡧࡀࠦࡨࡵ࡬ࡰࡴ࠽ࡶࡪࡪ࠻ࠣࡀ࠿ࡪࡴࡴࡴࠡࡥࡲࡰࡴࡸ࠽ࠣࡴࡨࡨࠧࡄࡅࡳࡴࡲࡶࡁ࠵ࡦࡰࡰࡷࡂࡁ࠵ࡴࡥࡀࠪై")
  elif bstack1l1ll1ll_opy_ == bstack111ll1l_opy_ (u"ࠤࡷ࡭ࡲ࡫࡯ࡶࡶࠥ౉"):
    return bstack111ll1l_opy_ (u"ࠪࡀࡹࡪࠠࡤ࡮ࡤࡷࡸࡃࠢࡣࡵࡷࡥࡨࡱ࠭ࡥࡣࡷࡥࠧࠦࡳࡵࡻ࡯ࡩࡂࠨࡣࡰ࡮ࡲࡶ࠿ࠩࡥࡦࡣ࠶࠶࠻ࡁࠢ࠿࠾ࡩࡳࡳࡺࠠࡤࡱ࡯ࡳࡷࡃࠢࠤࡧࡨࡥ࠸࠸࠶ࠣࡀࡗ࡭ࡲ࡫࡯ࡶࡶ࠿࠳࡫ࡵ࡮ࡵࡀ࠿࠳ࡹࡪ࠾ࠨొ")
  elif bstack1l1ll1ll_opy_ == bstack111ll1l_opy_ (u"ࠦࡷࡻ࡮࡯࡫ࡱ࡫ࠧో"):
    return bstack111ll1l_opy_ (u"ࠬࡂࡴࡥࠢࡦࡰࡦࡹࡳ࠾ࠤࡥࡷࡹࡧࡣ࡬࠯ࡧࡥࡹࡧࠢࠡࡵࡷࡽࡱ࡫࠽ࠣࡥࡲࡰࡴࡸ࠺ࡣ࡮ࡤࡧࡰࡁࠢ࠿࠾ࡩࡳࡳࡺࠠࡤࡱ࡯ࡳࡷࡃࠢࡣ࡮ࡤࡧࡰࠨ࠾ࡓࡷࡱࡲ࡮ࡴࡧ࠽࠱ࡩࡳࡳࡺ࠾࠽࠱ࡷࡨࡃ࠭ౌ")
  else:
    return bstack111ll1l_opy_ (u"࠭࠼ࡵࡦࠣࡥࡱ࡯ࡧ࡯࠿ࠥࡧࡪࡴࡴࡦࡴࠥࠤࡨࡲࡡࡴࡵࡀࠦࡧࡹࡴࡢࡥ࡮࠱ࡩࡧࡴࡢࠤࠣࡷࡹࡿ࡬ࡦ࠿ࠥࡧࡴࡲ࡯ࡳ࠼ࡥࡰࡦࡩ࡫࠼ࠤࡁࡀ࡫ࡵ࡮ࡵࠢࡦࡳࡱࡵࡲ࠾ࠤࡥࡰࡦࡩ࡫ࠣࡀ్ࠪ") + bstack1llll1l1l_opy_(
      bstack1l1ll1ll_opy_) + bstack111ll1l_opy_ (u"ࠧ࠽࠱ࡩࡳࡳࡺ࠾࠽࠱ࡷࡨࡃ࠭౎")
def bstack11l1l1111_opy_(session):
  return bstack111ll1l_opy_ (u"ࠨ࠾ࡷࡶࠥࡩ࡬ࡢࡵࡶࡁࠧࡨࡳࡵࡣࡦ࡯࠲ࡸ࡯ࡸࠤࡁࡀࡹࡪࠠࡤ࡮ࡤࡷࡸࡃࠢࡣࡵࡷࡥࡨࡱ࠭ࡥࡣࡷࡥࠥࡹࡥࡴࡵ࡬ࡳࡳ࠳࡮ࡢ࡯ࡨࠦࡃࡂࡡࠡࡪࡵࡩ࡫ࡃࠢࡼࡿࠥࠤࡹࡧࡲࡨࡧࡷࡁࠧࡥࡢ࡭ࡣࡱ࡯ࠧࡄࡻࡾ࠾࠲ࡥࡃࡂ࠯ࡵࡦࡁࡿࢂࢁࡽ࠽ࡶࡧࠤࡦࡲࡩࡨࡰࡀࠦࡨ࡫࡮ࡵࡧࡵࠦࠥࡩ࡬ࡢࡵࡶࡁࠧࡨࡳࡵࡣࡦ࡯࠲ࡪࡡࡵࡣࠥࡂࢀࢃ࠼࠰ࡶࡧࡂࡁࡺࡤࠡࡣ࡯࡭࡬ࡴ࠽ࠣࡥࡨࡲࡹ࡫ࡲࠣࠢࡦࡰࡦࡹࡳ࠾ࠤࡥࡷࡹࡧࡣ࡬࠯ࡧࡥࡹࡧࠢ࠿ࡽࢀࡀ࠴ࡺࡤ࠿࠾ࡷࡨࠥࡧ࡬ࡪࡩࡱࡁࠧࡩࡥ࡯ࡶࡨࡶࠧࠦࡣ࡭ࡣࡶࡷࡂࠨࡢࡴࡶࡤࡧࡰ࠳ࡤࡢࡶࡤࠦࡃࢁࡽ࠽࠱ࡷࡨࡃࡂࡴࡥࠢࡤࡰ࡮࡭࡮࠾ࠤࡦࡩࡳࡺࡥࡳࠤࠣࡧࡱࡧࡳࡴ࠿ࠥࡦࡸࡺࡡࡤ࡭࠰ࡨࡦࡺࡡࠣࡀࡾࢁࡁ࠵ࡴࡥࡀ࠿࠳ࡹࡸ࠾ࠨ౏").format(
    session[bstack111ll1l_opy_ (u"ࠩࡳࡹࡧࡲࡩࡤࡡࡸࡶࡱ࠭౐")], bstack11ll1lll1_opy_(session), bstack1l1ll1l11_opy_(session[bstack111ll1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡶࡸࡦࡺࡵࡴࠩ౑")]),
    bstack1l1ll1l11_opy_(session[bstack111ll1l_opy_ (u"ࠫࡸࡺࡡࡵࡷࡶࠫ౒")]),
    bstack1llll1l1l_opy_(session[bstack111ll1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࠭౓")] or session[bstack111ll1l_opy_ (u"࠭ࡤࡦࡸ࡬ࡧࡪ࠭౔")] or bstack111ll1l_opy_ (u"ࠧࠨౕ")) + bstack111ll1l_opy_ (u"ౖࠣࠢࠥ") + (session[bstack111ll1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡢࡺࡪࡸࡳࡪࡱࡱࠫ౗")] or bstack111ll1l_opy_ (u"ࠪࠫౘ")),
    session[bstack111ll1l_opy_ (u"ࠫࡴࡹࠧౙ")] + bstack111ll1l_opy_ (u"ࠧࠦࠢౚ") + session[bstack111ll1l_opy_ (u"࠭࡯ࡴࡡࡹࡩࡷࡹࡩࡰࡰࠪ౛")], session[bstack111ll1l_opy_ (u"ࠧࡥࡷࡵࡥࡹ࡯࡯࡯ࠩ౜")] or bstack111ll1l_opy_ (u"ࠨࠩౝ"),
    session[bstack111ll1l_opy_ (u"ࠩࡦࡶࡪࡧࡴࡦࡦࡢࡥࡹ࠭౞")] if session[bstack111ll1l_opy_ (u"ࠪࡧࡷ࡫ࡡࡵࡧࡧࡣࡦࡺࠧ౟")] else bstack111ll1l_opy_ (u"ࠫࠬౠ"))
def bstack1111111ll_opy_(sessions, bstack1111lll1l_opy_):
  try:
    bstack11l1l1l1_opy_ = bstack111ll1l_opy_ (u"ࠧࠨౡ")
    if not os.path.exists(bstack11lll1ll_opy_):
      os.mkdir(bstack11lll1ll_opy_)
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), bstack111ll1l_opy_ (u"࠭ࡡࡴࡵࡨࡸࡸ࠵ࡲࡦࡲࡲࡶࡹ࠴ࡨࡵ࡯࡯ࠫౢ")), bstack111ll1l_opy_ (u"ࠧࡳࠩౣ")) as f:
      bstack11l1l1l1_opy_ = f.read()
    bstack11l1l1l1_opy_ = bstack11l1l1l1_opy_.replace(bstack111ll1l_opy_ (u"ࠨࡽࠨࡖࡊ࡙ࡕࡍࡖࡖࡣࡈࡕࡕࡏࡖࠨࢁࠬ౤"), str(len(sessions)))
    bstack11l1l1l1_opy_ = bstack11l1l1l1_opy_.replace(bstack111ll1l_opy_ (u"ࠩࡾࠩࡇ࡛ࡉࡍࡆࡢ࡙ࡗࡒࠥࡾࠩ౥"), bstack1111lll1l_opy_)
    bstack11l1l1l1_opy_ = bstack11l1l1l1_opy_.replace(bstack111ll1l_opy_ (u"ࠪࡿࠪࡈࡕࡊࡎࡇࡣࡓࡇࡍࡆࠧࢀࠫ౦"),
                                              sessions[0].get(bstack111ll1l_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡢࡲࡦࡳࡥࠨ౧")) if sessions[0] else bstack111ll1l_opy_ (u"ࠬ࠭౨"))
    with open(os.path.join(bstack11lll1ll_opy_, bstack111ll1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠲ࡸࡥࡱࡱࡵࡸ࠳࡮ࡴ࡮࡮ࠪ౩")), bstack111ll1l_opy_ (u"ࠧࡸࠩ౪")) as stream:
      stream.write(bstack11l1l1l1_opy_.split(bstack111ll1l_opy_ (u"ࠨࡽࠨࡗࡊ࡙ࡓࡊࡑࡑࡗࡤࡊࡁࡕࡃࠨࢁࠬ౫"))[0])
      for session in sessions:
        stream.write(bstack11l1l1111_opy_(session))
      stream.write(bstack11l1l1l1_opy_.split(bstack111ll1l_opy_ (u"ࠩࡾࠩࡘࡋࡓࡔࡋࡒࡒࡘࡥࡄࡂࡖࡄࠩࢂ࠭౬"))[1])
    logger.info(bstack111ll1l_opy_ (u"ࠪࡋࡪࡴࡥࡳࡣࡷࡩࡩࠦࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠥࡨࡵࡪ࡮ࡧࠤࡦࡸࡴࡪࡨࡤࡧࡹࡹࠠࡢࡶࠣࡿࢂ࠭౭").format(bstack11lll1ll_opy_));
  except Exception as e:
    logger.debug(bstack11lll111_opy_.format(str(e)))
def bstack11l1lll1_opy_(bstack1ll1l1lll1_opy_):
  global CONFIG
  try:
    host = bstack111ll1l_opy_ (u"ࠫࡦࡶࡩ࠮ࡥ࡯ࡳࡺࡪࠧ౮") if bstack111ll1l_opy_ (u"ࠬࡧࡰࡱࠩ౯") in CONFIG else bstack111ll1l_opy_ (u"࠭ࡡࡱ࡫ࠪ౰")
    user = CONFIG[bstack111ll1l_opy_ (u"ࠧࡶࡵࡨࡶࡓࡧ࡭ࡦࠩ౱")]
    key = CONFIG[bstack111ll1l_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡌࡧࡼࠫ౲")]
    bstack11111ll1l_opy_ = bstack111ll1l_opy_ (u"ࠩࡤࡴࡵ࠳ࡡࡶࡶࡲࡱࡦࡺࡥࠨ౳") if bstack111ll1l_opy_ (u"ࠪࡥࡵࡶࠧ౴") in CONFIG else bstack111ll1l_opy_ (u"ࠫࡦࡻࡴࡰ࡯ࡤࡸࡪ࠭౵")
    url = bstack111ll1l_opy_ (u"ࠬ࡮ࡴࡵࡲࡶ࠾࠴࠵ࡻࡾ࠼ࡾࢁࡅࢁࡽ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡤࡱࡰ࠳ࢀࢃ࠯ࡣࡷ࡬ࡰࡩࡹ࠯ࡼࡿ࠲ࡷࡪࡹࡳࡪࡱࡱࡷ࠳ࡰࡳࡰࡰࠪ౶").format(user, key, host, bstack11111ll1l_opy_,
                                                                                bstack1ll1l1lll1_opy_)
    headers = {
      bstack111ll1l_opy_ (u"࠭ࡃࡰࡰࡷࡩࡳࡺ࠭ࡵࡻࡳࡩࠬ౷"): bstack111ll1l_opy_ (u"ࠧࡢࡲࡳࡰ࡮ࡩࡡࡵ࡫ࡲࡲ࠴ࡰࡳࡰࡰࠪ౸"),
    }
    proxies = bstack11ll1l1ll_opy_(CONFIG, url)
    response = requests.get(url, headers=headers, proxies=proxies)
    if response.json():
      return list(map(lambda session: session[bstack111ll1l_opy_ (u"ࠨࡣࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࡤࡹࡥࡴࡵ࡬ࡳࡳ࠭౹")], response.json()))
  except Exception as e:
    logger.debug(bstack1ll1l1111_opy_.format(str(e)))
def bstack111ll11l_opy_():
  global CONFIG
  try:
    if bstack111ll1l_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠬ౺") in CONFIG:
      host = bstack111ll1l_opy_ (u"ࠪࡥࡵ࡯࠭ࡤ࡮ࡲࡹࡩ࠭౻") if bstack111ll1l_opy_ (u"ࠫࡦࡶࡰࠨ౼") in CONFIG else bstack111ll1l_opy_ (u"ࠬࡧࡰࡪࠩ౽")
      user = CONFIG[bstack111ll1l_opy_ (u"࠭ࡵࡴࡧࡵࡒࡦࡳࡥࠨ౾")]
      key = CONFIG[bstack111ll1l_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡋࡦࡻࠪ౿")]
      bstack11111ll1l_opy_ = bstack111ll1l_opy_ (u"ࠨࡣࡳࡴ࠲ࡧࡵࡵࡱࡰࡥࡹ࡫ࠧಀ") if bstack111ll1l_opy_ (u"ࠩࡤࡴࡵ࠭ಁ") in CONFIG else bstack111ll1l_opy_ (u"ࠪࡥࡺࡺ࡯࡮ࡣࡷࡩࠬಂ")
      url = bstack111ll1l_opy_ (u"ࠫ࡭ࡺࡴࡱࡵ࠽࠳࠴ࢁࡽ࠻ࡽࢀࡄࢀࢃ࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡣࡰ࡯࠲ࡿࢂ࠵ࡢࡶ࡫࡯ࡨࡸ࠴ࡪࡴࡱࡱࠫಃ").format(user, key, host, bstack11111ll1l_opy_)
      headers = {
        bstack111ll1l_opy_ (u"ࠬࡉ࡯࡯ࡶࡨࡲࡹ࠳ࡴࡺࡲࡨࠫ಄"): bstack111ll1l_opy_ (u"࠭ࡡࡱࡲ࡯࡭ࡨࡧࡴࡪࡱࡱ࠳࡯ࡹ࡯࡯ࠩಅ"),
      }
      if bstack111ll1l_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩಆ") in CONFIG:
        params = {bstack111ll1l_opy_ (u"ࠨࡰࡤࡱࡪ࠭ಇ"): CONFIG[bstack111ll1l_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠬಈ")], bstack111ll1l_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡡ࡬ࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭ಉ"): CONFIG[bstack111ll1l_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭ಊ")]}
      else:
        params = {bstack111ll1l_opy_ (u"ࠬࡴࡡ࡮ࡧࠪಋ"): CONFIG[bstack111ll1l_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡓࡧ࡭ࡦࠩಌ")]}
      proxies = bstack11ll1l1ll_opy_(CONFIG, url)
      response = requests.get(url, params=params, headers=headers, proxies=proxies)
      if response.json():
        bstack1l1l1lll1_opy_ = response.json()[0][bstack111ll1l_opy_ (u"ࠧࡢࡷࡷࡳࡲࡧࡴࡪࡱࡱࡣࡧࡻࡩ࡭ࡦࠪ಍")]
        if bstack1l1l1lll1_opy_:
          bstack1111lll1l_opy_ = bstack1l1l1lll1_opy_[bstack111ll1l_opy_ (u"ࠨࡲࡸࡦࡱ࡯ࡣࡠࡷࡵࡰࠬಎ")].split(bstack111ll1l_opy_ (u"ࠩࡳࡹࡧࡲࡩࡤ࠯ࡥࡹ࡮ࡲࡤࠨಏ"))[0] + bstack111ll1l_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡵ࠲ࠫಐ") + bstack1l1l1lll1_opy_[
            bstack111ll1l_opy_ (u"ࠫ࡭ࡧࡳࡩࡧࡧࡣ࡮ࡪࠧ಑")]
          logger.info(bstack111l1l111_opy_.format(bstack1111lll1l_opy_))
          bstack111ll1ll_opy_ = CONFIG[bstack111ll1l_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡒࡦࡳࡥࠨಒ")]
          if bstack111ll1l_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨಓ") in CONFIG:
            bstack111ll1ll_opy_ += bstack111ll1l_opy_ (u"ࠧࠡࠩಔ") + CONFIG[bstack111ll1l_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪಕ")]
          if bstack111ll1ll_opy_ != bstack1l1l1lll1_opy_[bstack111ll1l_opy_ (u"ࠩࡱࡥࡲ࡫ࠧಖ")]:
            logger.debug(bstack1ll111l11_opy_.format(bstack1l1l1lll1_opy_[bstack111ll1l_opy_ (u"ࠪࡲࡦࡳࡥࠨಗ")], bstack111ll1ll_opy_))
          return [bstack1l1l1lll1_opy_[bstack111ll1l_opy_ (u"ࠫ࡭ࡧࡳࡩࡧࡧࡣ࡮ࡪࠧಘ")], bstack1111lll1l_opy_]
    else:
      logger.warn(bstack1llll111ll_opy_)
  except Exception as e:
    logger.debug(bstack11ll1ll11_opy_.format(str(e)))
  return [None, None]
def bstack1ll1l1l111_opy_(url, bstack11l1l1lll_opy_=False):
  global CONFIG
  global bstack1lll1ll1ll_opy_
  if not bstack1lll1ll1ll_opy_:
    hostname = bstack11l1llll1_opy_(url)
    is_private = bstack11l111lll_opy_(hostname)
    if (bstack111ll1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࠩಙ") in CONFIG and not CONFIG[bstack111ll1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࠪಚ")]) and (is_private or bstack11l1l1lll_opy_):
      bstack1lll1ll1ll_opy_ = hostname
def bstack11l1llll1_opy_(url):
  return urlparse(url).hostname
def bstack11l111lll_opy_(hostname):
  for bstack1111l1l11_opy_ in bstack1ll1l1l1l_opy_:
    regex = re.compile(bstack1111l1l11_opy_)
    if regex.match(hostname):
      return True
  return False
def bstack1llllll1ll_opy_(key_name):
  return True if key_name in threading.current_thread().__dict__.keys() else False
def getAccessibilityResults(driver):
  global CONFIG
  global bstack1111ll11l_opy_
  if not bstack111l1l11l_opy_.bstack1lll1l11_opy_(CONFIG, bstack1111ll11l_opy_):
    logger.warning(bstack111ll1l_opy_ (u"ࠢࡏࡱࡷࠤࡦࡴࠠࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠤࡸ࡫ࡳࡴ࡫ࡲࡲ࠱ࠦࡣࡢࡰࡱࡳࡹࠦࡲࡦࡶࡵ࡭ࡪࡼࡥࠡࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡴࡨࡷࡺࡲࡴࡴ࠰ࠥಛ"))
    return {}
  try:
    results = driver.execute_script(bstack111ll1l_opy_ (u"ࠣࠤࠥࠎࠥࠦࠠࠡࠢࠣࠤࠥࡸࡥࡵࡷࡵࡲࠥࡴࡥࡸࠢࡓࡶࡴࡳࡩࡴࡧࠫࡪࡺࡴࡣࡵ࡫ࡲࡲࠥ࠮ࡲࡦࡵࡲࡰࡻ࡫ࠬࠡࡴࡨ࡮ࡪࡩࡴࠪࠢࡾࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡷࡶࡾࠦࡻࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡧࡴࡴࡳࡵࠢࡨࡺࡪࡴࡴࠡ࠿ࠣࡲࡪࡽࠠࡄࡷࡶࡸࡴࡳࡅࡷࡧࡱࡸ࠭࠭ࡁ࠲࠳࡜ࡣ࡙ࡇࡐࡠࡉࡈࡘࡤࡘࡅࡔࡗࡏࡘࡘ࠭ࠩ࠼ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡨࡵ࡮ࡴࡶࠣࡪࡳࠦ࠽ࠡࡨࡸࡲࡨࡺࡩࡰࡰࠣࠬࡪࡼࡥ࡯ࡶࠬࠤࢀࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࡽࡩ࡯ࡦࡲࡻ࠳ࡸࡥ࡮ࡱࡹࡩࡊࡼࡥ࡯ࡶࡏ࡭ࡸࡺࡥ࡯ࡧࡵࠬࠬࡇ࠱࠲࡛ࡢࡖࡊ࡙ࡕࡍࡖࡖࡣࡗࡋࡓࡑࡑࡑࡗࡊ࠭ࠬࠡࡨࡱ࠭ࡀࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࡸࡥࡴࡱ࡯ࡺࡪ࠮ࡥࡷࡧࡱࡸ࠳ࡪࡥࡵࡣ࡬ࡰ࠳ࡪࡡࡵࡣࠬ࠿ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡾ࠽ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࡽࡩ࡯ࡦࡲࡻ࠳ࡧࡤࡥࡇࡹࡩࡳࡺࡌࡪࡵࡷࡩࡳ࡫ࡲࠩࠩࡄ࠵࠶࡟࡟ࡓࡇࡖ࡙ࡑ࡚ࡓࡠࡔࡈࡗࡕࡕࡎࡔࡇࠪ࠰ࠥ࡬࡮ࠪ࠽ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࡽࡩ࡯ࡦࡲࡻ࠳ࡪࡩࡴࡲࡤࡸࡨ࡮ࡅࡷࡧࡱࡸ࠭࡫ࡶࡦࡰࡷ࠭ࡀࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࢂࠦࡣࡢࡶࡦ࡬ࠥࢁࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡵࡩ࡯࡫ࡣࡵࠪࠬ࠿ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࢁࠏࠦࠠࠡࠢࠣࠤࠥࠦࡽࠪ࠽ࠍࠤࠥࠦࠠࠣࠤࠥಜ"))
    return results
  except Exception:
    logger.error(bstack111ll1l_opy_ (u"ࠤࡑࡳࠥࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡸࡥࡴࡷ࡯ࡸࡸࠦࡷࡦࡴࡨࠤ࡫ࡵࡵ࡯ࡦ࠱ࠦಝ"))
    return {}
def getAccessibilityResultsSummary(driver):
  global CONFIG
  global bstack1111ll11l_opy_
  if not bstack111l1l11l_opy_.bstack1lll1l11_opy_(CONFIG, bstack1111ll11l_opy_):
    logger.warning(bstack111ll1l_opy_ (u"ࠥࡒࡴࡺࠠࡢࡰࠣࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠠࡴࡧࡶࡷ࡮ࡵ࡮࠭ࠢࡦࡥࡳࡴ࡯ࡵࠢࡵࡩࡹࡸࡩࡦࡸࡨࠤࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡷ࡫ࡳࡶ࡮ࡷࡷࠥࡹࡵ࡮࡯ࡤࡶࡾ࠴ࠢಞ"))
    return {}
  try:
    bstack111lllll_opy_ = driver.execute_script(bstack111ll1l_opy_ (u"ࠦࠧࠨࠊࠡࠢࠣࠤࠥࠦࠠࠡࡴࡨࡸࡺࡸ࡮ࠡࡰࡨࡻࠥࡖࡲࡰ࡯࡬ࡷࡪ࠮ࡦࡶࡰࡦࡸ࡮ࡵ࡮ࠡࠪࡵࡩࡸࡵ࡬ࡷࡧ࠯ࠤࡷ࡫ࡪࡦࡥࡷ࠭ࠥࢁࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࡺࡲࡺࠢࡾࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡣࡰࡰࡶࡸࠥ࡫ࡶࡦࡰࡷࠤࡂࠦ࡮ࡦࡹࠣࡇࡺࡹࡴࡰ࡯ࡈࡺࡪࡴࡴࠩࠩࡄ࠵࠶࡟࡟ࡕࡃࡓࡣࡌࡋࡔࡠࡔࡈࡗ࡚ࡒࡔࡔࡡࡖ࡙ࡒࡓࡁࡓ࡛ࠪ࠭ࡀࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡥࡲࡲࡸࡺࠠࡧࡰࠣࡁࠥ࡬ࡵ࡯ࡥࡷ࡭ࡴࡴࠠࠩࡧࡹࡩࡳࡺࠩࠡࡽࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡺ࡭ࡳࡪ࡯ࡸ࠰ࡵࡩࡲࡵࡶࡦࡇࡹࡩࡳࡺࡌࡪࡵࡷࡩࡳ࡫ࡲࠩࠩࡄ࠵࠶࡟࡟ࡓࡇࡖ࡙ࡑ࡚ࡓࡠࡕࡘࡑࡒࡇࡒ࡚ࡡࡕࡉࡘࡖࡏࡏࡕࡈࠫ࠱ࠦࡦ࡯ࠫ࠾ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡶࡪࡹ࡯࡭ࡸࡨࠬࡪࡼࡥ࡯ࡶ࠱ࡨࡪࡺࡡࡪ࡮࠱ࡷࡺࡳ࡭ࡢࡴࡼ࠭ࡀࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡿ࠾ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡷࡪࡰࡧࡳࡼ࠴ࡡࡥࡦࡈࡺࡪࡴࡴࡍ࡫ࡶࡸࡪࡴࡥࡳࠪࠪࡅ࠶࠷࡙ࡠࡔࡈࡗ࡚ࡒࡔࡔࡡࡖ࡙ࡒࡓࡁࡓ࡛ࡢࡖࡊ࡙ࡐࡐࡐࡖࡉࠬ࠲ࠠࡧࡰࠬ࠿ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡸ࡫ࡱࡨࡴࡽ࠮ࡥ࡫ࡶࡴࡦࡺࡣࡩࡇࡹࡩࡳࡺࠨࡦࡸࡨࡲࡹ࠯࠻ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡽࠡࡥࡤࡸࡨ࡮ࠠࡼࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡷ࡫ࡪࡦࡥࡷࠬ࠮ࡁࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࢃࠊࠡࠢࠣࠤࠥࠦࠠࠡࡿࠬ࠿ࠏࠦࠠࠡࠢࠥࠦࠧಟ"))
    return bstack111lllll_opy_
  except Exception:
    logger.error(bstack111ll1l_opy_ (u"ࠧࡔ࡯ࠡࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡵࡸࡱࡲࡧࡲࡺࠢࡺࡥࡸࠦࡦࡰࡷࡱࡨ࠳ࠨಠ"))
    return {}