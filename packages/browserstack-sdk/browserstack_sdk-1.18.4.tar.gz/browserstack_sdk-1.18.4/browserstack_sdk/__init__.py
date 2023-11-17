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
import tempfile
from packaging import version
from browserstack.local import Local
from urllib.parse import urlparse
from bstack_utils.constants import *
from bstack_utils.percy import *
import time
import requests
def bstack1ll1lllll_opy_():
  global CONFIG
  headers = {
        bstack1ll_opy_ (u"ࠩࡆࡳࡳࡺࡥ࡯ࡶ࠰ࡸࡾࡶࡥࠨࡵ"): bstack1ll_opy_ (u"ࠪࡥࡵࡶ࡬ࡪࡥࡤࡸ࡮ࡵ࡮࠰࡬ࡶࡳࡳ࠭ࡶ"),
      }
  proxies = bstack1llll1111_opy_(CONFIG, bstack1lll1ll1l_opy_)
  try:
    response = requests.get(bstack1lll1ll1l_opy_, headers=headers, proxies=proxies, timeout=5)
    if response.json():
      bstack1ll1l1l11_opy_ = response.json()[bstack1ll_opy_ (u"ࠫ࡭ࡻࡢࡴࠩࡷ")]
      logger.debug(bstack1111l111l_opy_.format(response.json()))
      return bstack1ll1l1l11_opy_
    else:
      logger.debug(bstack1l1ll11ll_opy_.format(bstack1ll_opy_ (u"ࠧࡘࡥࡴࡲࡲࡲࡸ࡫ࠠࡋࡕࡒࡒࠥࡶࡡࡳࡵࡨࠤࡪࡸࡲࡰࡴࠣࠦࡸ")))
  except Exception as e:
    logger.debug(bstack1l1ll11ll_opy_.format(e))
def bstack1llll1l11_opy_(hub_url):
  global CONFIG
  url = bstack1ll_opy_ (u"ࠨࡨࡵࡶࡳࡷ࠿࠵࠯ࠣࡹ")+  hub_url + bstack1ll_opy_ (u"ࠢ࠰ࡥ࡫ࡩࡨࡱࠢࡺ")
  headers = {
        bstack1ll_opy_ (u"ࠨࡅࡲࡲࡹ࡫࡮ࡵ࠯ࡷࡽࡵ࡫ࠧࡻ"): bstack1ll_opy_ (u"ࠩࡤࡴࡵࡲࡩࡤࡣࡷ࡭ࡴࡴ࠯࡫ࡵࡲࡲࠬࡼ"),
      }
  proxies = bstack1llll1111_opy_(CONFIG, url)
  try:
    start_time = time.perf_counter()
    requests.get(url, headers=headers, proxies=proxies, timeout=5)
    latency = time.perf_counter() - start_time
    logger.debug(bstack11l1ll11_opy_.format(hub_url, latency))
    return dict(hub_url=hub_url, latency=latency)
  except Exception as e:
    logger.debug(bstack1lll1l1l11_opy_.format(hub_url, e))
def bstack1ll11l11ll_opy_():
  try:
    global bstack1l111l111_opy_
    bstack1ll1l1l11_opy_ = bstack1ll1lllll_opy_()
    bstack1ll1111111_opy_ = []
    results = []
    for bstack1llll11lll_opy_ in bstack1ll1l1l11_opy_:
      bstack1ll1111111_opy_.append(bstack11lll1111_opy_(target=bstack1llll1l11_opy_,args=(bstack1llll11lll_opy_,)))
    for t in bstack1ll1111111_opy_:
      t.start()
    for t in bstack1ll1111111_opy_:
      results.append(t.join())
    bstack1lllll1l11_opy_ = {}
    for item in results:
      hub_url = item[bstack1ll_opy_ (u"ࠪ࡬ࡺࡨ࡟ࡶࡴ࡯ࠫࡽ")]
      latency = item[bstack1ll_opy_ (u"ࠫࡱࡧࡴࡦࡰࡦࡽࠬࡾ")]
      bstack1lllll1l11_opy_[hub_url] = latency
    bstack1l1lll11l_opy_ = min(bstack1lllll1l11_opy_, key= lambda x: bstack1lllll1l11_opy_[x])
    bstack1l111l111_opy_ = bstack1l1lll11l_opy_
    logger.debug(bstack1l11llll1_opy_.format(bstack1l1lll11l_opy_))
  except Exception as e:
    logger.debug(bstack1ll1l11l1_opy_.format(e))
from bstack_utils.messages import *
from bstack_utils.config import Config
from bstack_utils.helper import bstack1llll1l11l_opy_, bstack1lll1ll1l1_opy_, bstack1llll11l_opy_, bstack1l111lll1_opy_, Notset, bstack111lll111_opy_, \
  bstack1l1ll1ll1_opy_, bstack11111l11l_opy_, bstack1ll11ll111_opy_, bstack11l111ll_opy_, bstack1ll1ll11l1_opy_, bstack111ll111l_opy_, bstack1lll11ll1l_opy_, \
  bstack1ll11l1lll_opy_, bstack11llll11l_opy_, bstack1lll11l1_opy_, bstack1l11l1ll1_opy_, bstack1ll11ll11_opy_, bstack1ll111ll1_opy_
from bstack_utils.bstack1ll11l1l11_opy_ import bstack11l1l1l1_opy_
from bstack_utils.proxy import bstack11llllll_opy_, bstack1llll1111_opy_, bstack1l111ll11_opy_, bstack1lll11lll_opy_
import bstack_utils.bstack1l1l1l1l1_opy_ as bstack1lll1ll1_opy_
from browserstack_sdk.bstack1l1llllll_opy_ import *
from browserstack_sdk.bstack1ll1ll11l_opy_ import *
from bstack_utils.bstack1lll1l11_opy_ import bstack1ll11l11_opy_
bstack1llll1l1_opy_ = bstack1ll_opy_ (u"ࠬࠦࠠ࠰ࠬࠣࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃࠠࠫ࠱࡟ࡲࠥࠦࡩࡧࠪࡳࡥ࡬࡫ࠠ࠾࠿ࡀࠤࡻࡵࡩࡥࠢ࠳࠭ࠥࢁ࡜࡯ࠢࠣࠤࡹࡸࡹࡼ࡞ࡱࠤࡨࡵ࡮ࡴࡶࠣࡪࡸࠦ࠽ࠡࡴࡨࡵࡺ࡯ࡲࡦࠪ࡟ࠫ࡫ࡹ࡜ࠨࠫ࠾ࡠࡳࠦࠠࠡࠢࠣࡪࡸ࠴ࡡࡱࡲࡨࡲࡩࡌࡩ࡭ࡧࡖࡽࡳࡩࠨࡣࡵࡷࡥࡨࡱ࡟ࡱࡣࡷ࡬࠱ࠦࡊࡔࡑࡑ࠲ࡸࡺࡲࡪࡰࡪ࡭࡫ࡿࠨࡱࡡ࡬ࡲࡩ࡫ࡸࠪࠢ࠮ࠤࠧࡀࠢࠡ࠭ࠣࡎࡘࡕࡎ࠯ࡵࡷࡶ࡮ࡴࡧࡪࡨࡼࠬࡏ࡙ࡏࡏ࠰ࡳࡥࡷࡹࡥࠩࠪࡤࡻࡦ࡯ࡴࠡࡰࡨࡻࡕࡧࡧࡦ࠴࠱ࡩࡻࡧ࡬ࡶࡣࡷࡩ࠭ࠨࠨࠪࠢࡀࡂࠥࢁࡽࠣ࠮ࠣࡠࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࡼࠤࡤࡧࡹ࡯࡯࡯ࠤ࠽ࠤࠧ࡭ࡥࡵࡕࡨࡷࡸ࡯࡯࡯ࡆࡨࡸࡦ࡯࡬ࡴࠤࢀࡠࠬ࠯ࠩࠪ࡝ࠥ࡬ࡦࡹࡨࡦࡦࡢ࡭ࡩࠨ࡝ࠪࠢ࠮ࠤࠧ࠲࡜࡝ࡰࠥ࠭ࡡࡴࠠࠡࠢࠣࢁࡨࡧࡴࡤࡪࠫࡩࡽ࠯ࡻ࡝ࡰࠣࠤࠥࠦࡽ࡝ࡰࠣࠤࢂࡢ࡮ࠡࠢ࠲࠮ࠥࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾ࠢ࠭࠳ࠬࡿ")
bstack1llll1ll1l_opy_ = bstack1ll_opy_ (u"࠭࡜࡯࠱࠭ࠤࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽ࠡࠬ࠲ࡠࡳࡩ࡯࡯ࡵࡷࠤࡧࡹࡴࡢࡥ࡮ࡣࡵࡧࡴࡩࠢࡀࠤࡵࡸ࡯ࡤࡧࡶࡷ࠳ࡧࡲࡨࡸ࡞ࡴࡷࡵࡣࡦࡵࡶ࠲ࡦࡸࡧࡷ࠰࡯ࡩࡳ࡭ࡴࡩࠢ࠰ࠤ࠸ࡣ࡜࡯ࡥࡲࡲࡸࡺࠠࡣࡵࡷࡥࡨࡱ࡟ࡤࡣࡳࡷࠥࡃࠠࡱࡴࡲࡧࡪࡹࡳ࠯ࡣࡵ࡫ࡻࡡࡰࡳࡱࡦࡩࡸࡹ࠮ࡢࡴࡪࡺ࠳ࡲࡥ࡯ࡩࡷ࡬ࠥ࠳ࠠ࠲࡟࡟ࡲࡨࡵ࡮ࡴࡶࠣࡴࡤ࡯࡮ࡥࡧࡻࠤࡂࠦࡰࡳࡱࡦࡩࡸࡹ࠮ࡢࡴࡪࡺࡠࡶࡲࡰࡥࡨࡷࡸ࠴ࡡࡳࡩࡹ࠲ࡱ࡫࡮ࡨࡶ࡫ࠤ࠲ࠦ࠲࡞࡞ࡱࡴࡷࡵࡣࡦࡵࡶ࠲ࡦࡸࡧࡷࠢࡀࠤࡵࡸ࡯ࡤࡧࡶࡷ࠳ࡧࡲࡨࡸ࠱ࡷࡱ࡯ࡣࡦࠪ࠳࠰ࠥࡶࡲࡰࡥࡨࡷࡸ࠴ࡡࡳࡩࡹ࠲ࡱ࡫࡮ࡨࡶ࡫ࠤ࠲ࠦ࠳ࠪ࡞ࡱࡧࡴࡴࡳࡵࠢ࡬ࡱࡵࡵࡲࡵࡡࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹ࠺࡟ࡣࡵࡷࡥࡨࡱࠠ࠾ࠢࡵࡩࡶࡻࡩࡳࡧࠫࠦࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࠣࠫ࠾ࡠࡳ࡯࡭ࡱࡱࡵࡸࡤࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵ࠶ࡢࡦࡸࡺࡡࡤ࡭࠱ࡧ࡭ࡸ࡯࡮࡫ࡸࡱ࠳ࡲࡡࡶࡰࡦ࡬ࠥࡃࠠࡢࡵࡼࡲࡨࠦࠨ࡭ࡣࡸࡲࡨ࡮ࡏࡱࡶ࡬ࡳࡳࡹࠩࠡ࠿ࡁࠤࢀࡢ࡮࡭ࡧࡷࠤࡨࡧࡰࡴ࠽࡟ࡲࡹࡸࡹࠡࡽ࡟ࡲࡨࡧࡰࡴࠢࡀࠤࡏ࡙ࡏࡏ࠰ࡳࡥࡷࡹࡥࠩࡤࡶࡸࡦࡩ࡫ࡠࡥࡤࡴࡸ࠯࡜࡯ࠢࠣࢁࠥࡩࡡࡵࡥ࡫ࠬࡪࡾࠩࠡࡽ࡟ࡲࠥࠦࠠࠡࡿ࡟ࡲࠥࠦࡲࡦࡶࡸࡶࡳࠦࡡࡸࡣ࡬ࡸࠥ࡯࡭ࡱࡱࡵࡸࡤࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵ࠶ࡢࡦࡸࡺࡡࡤ࡭࠱ࡧ࡭ࡸ࡯࡮࡫ࡸࡱ࠳ࡩ࡯࡯ࡰࡨࡧࡹ࠮ࡻ࡝ࡰࠣࠤࠥࠦࡷࡴࡇࡱࡨࡵࡵࡩ࡯ࡶ࠽ࠤࡥࡽࡳࡴ࠼࠲࠳ࡨࡪࡰ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡤࡱࡰ࠳ࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࡀࡥࡤࡴࡸࡃࠤࡼࡧࡱࡧࡴࡪࡥࡖࡔࡌࡇࡴࡳࡰࡰࡰࡨࡲࡹ࠮ࡊࡔࡑࡑ࠲ࡸࡺࡲࡪࡰࡪ࡭࡫ࡿࠨࡤࡣࡳࡷ࠮࠯ࡽࡡ࠮࡟ࡲࠥࠦࠠࠡ࠰࠱࠲ࡱࡧࡵ࡯ࡥ࡫ࡓࡵࡺࡩࡰࡰࡶࡠࡳࠦࠠࡾࠫ࡟ࡲࢂࡢ࡮࠰ࠬࠣࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃࠠࠫ࠱࡟ࡲࠬࢀ")
from ._version import __version__
bstack1ll1l1ll_opy_ = None
CONFIG = {}
bstack1ll1l1111_opy_ = {}
bstack1l1ll1l1l_opy_ = {}
bstack1ll11l1ll_opy_ = None
bstack111111l1l_opy_ = None
bstack1lll1l111l_opy_ = None
bstack1l1lllll1_opy_ = -1
bstack1l1l11l11_opy_ = bstack11l1ll1ll_opy_
bstack11lllll1l_opy_ = 1
bstack111111ll_opy_ = False
bstack1lllllll11_opy_ = False
bstack1lll11l11l_opy_ = bstack1ll_opy_ (u"ࠧࠨࢁ")
bstack1l1111ll_opy_ = bstack1ll_opy_ (u"ࠨࠩࢂ")
bstack1l11l11ll_opy_ = False
bstack1lll1l11l_opy_ = True
bstack11ll1l1l_opy_ = bstack1ll_opy_ (u"ࠩࠪࢃ")
bstack11l1l1l1l_opy_ = []
bstack1l111l111_opy_ = bstack1ll_opy_ (u"ࠪࠫࢄ")
bstack11lll1lll_opy_ = False
bstack1lll1lll_opy_ = None
bstack1ll1l1l11l_opy_ = None
bstack11llll1l_opy_ = -1
bstack1lll11ll_opy_ = os.path.join(os.path.expanduser(bstack1ll_opy_ (u"ࠫࢃ࠭ࢅ")), bstack1ll_opy_ (u"ࠬ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠬࢆ"), bstack1ll_opy_ (u"࠭࠮ࡳࡱࡥࡳࡹ࠳ࡲࡦࡲࡲࡶࡹ࠳ࡨࡦ࡮ࡳࡩࡷ࠴ࡪࡴࡱࡱࠫࢇ"))
bstack11lllllll_opy_ = []
bstack11l1l1111_opy_ = []
bstack1lllllll1l_opy_ = []
bstack1ll1llll_opy_ = []
bstack11ll1l111_opy_ = bstack1ll_opy_ (u"ࠧࠨ࢈")
bstack11111l1ll_opy_ = bstack1ll_opy_ (u"ࠨࠩࢉ")
bstack1llll1l111_opy_ = False
bstack1l111l11l_opy_ = False
bstack11ll11ll1_opy_ = None
bstack111ll1ll_opy_ = None
bstack1l111111_opy_ = None
bstack1ll1l1llll_opy_ = None
bstack1ll1l1l1_opy_ = None
bstack1lll1l1ll1_opy_ = None
bstack1lll111l1_opy_ = None
bstack111l1l111_opy_ = None
bstack11lll11ll_opy_ = None
bstack1ll111l11l_opy_ = None
bstack1ll1111l1_opy_ = None
bstack1l1l11ll1_opy_ = None
bstack1l1111lll_opy_ = None
bstack1ll11ll1ll_opy_ = None
bstack1llllll111_opy_ = None
bstack11l111lll_opy_ = None
bstack1ll111l1l1_opy_ = None
bstack11111111l_opy_ = None
bstack1l11lllll_opy_ = bstack1ll_opy_ (u"ࠤࠥࢊ")
logger = logging.getLogger(__name__)
logging.basicConfig(level=bstack1l1l11l11_opy_,
                    format=bstack1ll_opy_ (u"ࠪࡠࡳࠫࠨࡢࡵࡦࡸ࡮ࡳࡥࠪࡵࠣ࡟ࠪ࠮࡮ࡢ࡯ࡨ࠭ࡸࡣ࡛ࠦࠪ࡯ࡩࡻ࡫࡬࡯ࡣࡰࡩ࠮ࡹ࡝ࠡ࠯ࠣࠩ࠭ࡳࡥࡴࡵࡤ࡫ࡪ࠯ࡳࠨࢋ"),
                    datefmt=bstack1ll_opy_ (u"ࠫࠪࡎ࠺ࠦࡏ࠽ࠩࡘ࠭ࢌ"),
                    stream=sys.stdout)
bstack1lll1l1lll_opy_ = Config.get_instance()
percy = bstack111111lll_opy_()
def bstack1llll11l11_opy_():
  global CONFIG
  global bstack1l1l11l11_opy_
  if bstack1ll_opy_ (u"ࠬࡲ࡯ࡨࡎࡨࡺࡪࡲࠧࢍ") in CONFIG:
    bstack1l1l11l11_opy_ = bstack1l1llll1_opy_[CONFIG[bstack1ll_opy_ (u"࠭࡬ࡰࡩࡏࡩࡻ࡫࡬ࠨࢎ")]]
    logging.getLogger().setLevel(bstack1l1l11l11_opy_)
def bstack11l1lll11_opy_():
  global CONFIG
  global bstack1llll1l111_opy_
  bstack11l1l11ll_opy_ = bstack111l1111l_opy_(CONFIG)
  if (bstack1ll_opy_ (u"ࠧࡴ࡭࡬ࡴࡘ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠩ࢏") in bstack11l1l11ll_opy_ and str(bstack11l1l11ll_opy_[bstack1ll_opy_ (u"ࠨࡵ࡮࡭ࡵ࡙ࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠪ࢐")]).lower() == bstack1ll_opy_ (u"ࠩࡷࡶࡺ࡫ࠧ࢑")):
    bstack1llll1l111_opy_ = True
def bstack1l1ll1l1_opy_():
  from appium.version import version as appium_version
  return version.parse(appium_version)
def bstack1l1lllllll_opy_():
  from selenium import webdriver
  return version.parse(webdriver.__version__)
def bstack111llll1l_opy_():
  args = sys.argv
  for i in range(len(args)):
    if bstack1ll_opy_ (u"ࠥ࠱࠲ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡧࡴࡴࡦࡪࡩࡩ࡭ࡱ࡫ࠢ࢒") == args[i].lower() or bstack1ll_opy_ (u"ࠦ࠲࠳ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡩ࡯࡯ࡨ࡬࡫ࠧ࢓") == args[i].lower():
      path = args[i + 1]
      sys.argv.remove(args[i])
      sys.argv.remove(path)
      global bstack11ll1l1l_opy_
      bstack11ll1l1l_opy_ += bstack1ll_opy_ (u"ࠬ࠳࠭ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡉ࡯࡯ࡨ࡬࡫ࡋ࡯࡬ࡦࠢࠪ࢔") + path
      return path
  return None
bstack111l1l11_opy_ = re.compile(bstack1ll_opy_ (u"ࡸࠢ࠯ࠬࡂࡠࠩࢁࠨ࠯ࠬࡂ࠭ࢂ࠴ࠪࡀࠤ࢕"))
def bstack1111ll1l1_opy_(loader, node):
  value = loader.construct_scalar(node)
  for group in bstack111l1l11_opy_.findall(value):
    if group is not None and os.environ.get(group) is not None:
      value = value.replace(bstack1ll_opy_ (u"ࠢࠥࡽࠥ࢖") + group + bstack1ll_opy_ (u"ࠣࡿࠥࢗ"), os.environ.get(group))
  return value
def bstack111l1ll1_opy_():
  bstack1lllll1l1_opy_ = bstack111llll1l_opy_()
  if bstack1lllll1l1_opy_ and os.path.exists(os.path.abspath(bstack1lllll1l1_opy_)):
    fileName = bstack1lllll1l1_opy_
  if bstack1ll_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡅࡒࡒࡋࡏࡇࡠࡈࡌࡐࡊ࠭࢘") in os.environ and os.path.exists(
          os.path.abspath(os.environ[bstack1ll_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡆࡓࡓࡌࡉࡈࡡࡉࡍࡑࡋ࢙ࠧ")])) and not bstack1ll_opy_ (u"ࠫ࡫࡯࡬ࡦࡐࡤࡱࡪ࢚࠭") in locals():
    fileName = os.environ[bstack1ll_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡈࡕࡎࡇࡋࡊࡣࡋࡏࡌࡆ࢛ࠩ")]
  if bstack1ll_opy_ (u"࠭ࡦࡪ࡮ࡨࡒࡦࡳࡥࠨ࢜") in locals():
    bstack11lll1_opy_ = os.path.abspath(fileName)
  else:
    bstack11lll1_opy_ = bstack1ll_opy_ (u"ࠧࠨ࢝")
  bstack1l1lll1l_opy_ = os.getcwd()
  bstack1ll11l1l1_opy_ = bstack1ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡺ࡯࡯ࠫ࢞")
  bstack1l1l1111l_opy_ = bstack1ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡻࡤࡱࡱ࠭࢟")
  while (not os.path.exists(bstack11lll1_opy_)) and bstack1l1lll1l_opy_ != bstack1ll_opy_ (u"ࠥࠦࢠ"):
    bstack11lll1_opy_ = os.path.join(bstack1l1lll1l_opy_, bstack1ll11l1l1_opy_)
    if not os.path.exists(bstack11lll1_opy_):
      bstack11lll1_opy_ = os.path.join(bstack1l1lll1l_opy_, bstack1l1l1111l_opy_)
    if bstack1l1lll1l_opy_ != os.path.dirname(bstack1l1lll1l_opy_):
      bstack1l1lll1l_opy_ = os.path.dirname(bstack1l1lll1l_opy_)
    else:
      bstack1l1lll1l_opy_ = bstack1ll_opy_ (u"ࠦࠧࢡ")
  if not os.path.exists(bstack11lll1_opy_):
    bstack11l1l1l11_opy_(
      bstack11l1ll1l_opy_.format(os.getcwd()))
  try:
    with open(bstack11lll1_opy_, bstack1ll_opy_ (u"ࠬࡸࠧࢢ")) as stream:
      yaml.add_implicit_resolver(bstack1ll_opy_ (u"ࠨࠡࡱࡣࡷ࡬ࡪࡾࠢࢣ"), bstack111l1l11_opy_)
      yaml.add_constructor(bstack1ll_opy_ (u"ࠢࠢࡲࡤࡸ࡭࡫ࡸࠣࢤ"), bstack1111ll1l1_opy_)
      config = yaml.load(stream, yaml.FullLoader)
      return config
  except:
    with open(bstack11lll1_opy_, bstack1ll_opy_ (u"ࠨࡴࠪࢥ")) as stream:
      try:
        config = yaml.safe_load(stream)
        return config
      except yaml.YAMLError as exc:
        bstack11l1l1l11_opy_(bstack1ll11l11l1_opy_.format(str(exc)))
def bstack1111l11l1_opy_(config):
  bstack111lll1ll_opy_ = bstack1ll11l1111_opy_(config)
  for option in list(bstack111lll1ll_opy_):
    if option.lower() in bstack11l1l111l_opy_ and option != bstack11l1l111l_opy_[option.lower()]:
      bstack111lll1ll_opy_[bstack11l1l111l_opy_[option.lower()]] = bstack111lll1ll_opy_[option]
      del bstack111lll1ll_opy_[option]
  return config
def bstack11llll1l1_opy_():
  global bstack1l1ll1l1l_opy_
  for key, bstack1ll1lll11l_opy_ in bstack1ll11l1l1l_opy_.items():
    if isinstance(bstack1ll1lll11l_opy_, list):
      for var in bstack1ll1lll11l_opy_:
        if var in os.environ and os.environ[var] and str(os.environ[var]).strip():
          bstack1l1ll1l1l_opy_[key] = os.environ[var]
          break
    elif bstack1ll1lll11l_opy_ in os.environ and os.environ[bstack1ll1lll11l_opy_] and str(os.environ[bstack1ll1lll11l_opy_]).strip():
      bstack1l1ll1l1l_opy_[key] = os.environ[bstack1ll1lll11l_opy_]
  if bstack1ll_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡎࡒࡇࡆࡒ࡟ࡊࡆࡈࡒ࡙ࡏࡆࡊࡇࡕࠫࢦ") in os.environ:
    bstack1l1ll1l1l_opy_[bstack1ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧࢧ")] = {}
    bstack1l1ll1l1l_opy_[bstack1ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨࢨ")][bstack1ll_opy_ (u"ࠬࡲ࡯ࡤࡣ࡯ࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧࢩ")] = os.environ[bstack1ll_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡒࡏࡄࡃࡏࡣࡎࡊࡅࡏࡖࡌࡊࡎࡋࡒࠨࢪ")]
def bstack1l11l111_opy_():
  global bstack1ll1l1111_opy_
  global bstack11ll1l1l_opy_
  for idx, val in enumerate(sys.argv):
    if idx < len(sys.argv) and bstack1ll_opy_ (u"ࠧ࠮࠯ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯࡮ࡲࡧࡦࡲࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪࢫ").lower() == val.lower():
      bstack1ll1l1111_opy_[bstack1ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࡌࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬࢬ")] = {}
      bstack1ll1l1111_opy_[bstack1ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࡍࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭ࢭ")][bstack1ll_opy_ (u"ࠪࡰࡴࡩࡡ࡭ࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬࢮ")] = sys.argv[idx + 1]
      del sys.argv[idx:idx + 2]
      break
  for key, bstack11111111_opy_ in bstack11l1l11l_opy_.items():
    if isinstance(bstack11111111_opy_, list):
      for idx, val in enumerate(sys.argv):
        for var in bstack11111111_opy_:
          if idx < len(sys.argv) and bstack1ll_opy_ (u"ࠫ࠲࠳ࠧࢯ") + var.lower() == val.lower() and not key in bstack1ll1l1111_opy_:
            bstack1ll1l1111_opy_[key] = sys.argv[idx + 1]
            bstack11ll1l1l_opy_ += bstack1ll_opy_ (u"ࠬࠦ࠭࠮ࠩࢰ") + var + bstack1ll_opy_ (u"࠭ࠠࠨࢱ") + sys.argv[idx + 1]
            del sys.argv[idx:idx + 2]
            break
    else:
      for idx, val in enumerate(sys.argv):
        if idx < len(sys.argv) and bstack1ll_opy_ (u"ࠧ࠮࠯ࠪࢲ") + bstack11111111_opy_.lower() == val.lower() and not key in bstack1ll1l1111_opy_:
          bstack1ll1l1111_opy_[key] = sys.argv[idx + 1]
          bstack11ll1l1l_opy_ += bstack1ll_opy_ (u"ࠨࠢ࠰࠱ࠬࢳ") + bstack11111111_opy_ + bstack1ll_opy_ (u"ࠩࠣࠫࢴ") + sys.argv[idx + 1]
          del sys.argv[idx:idx + 2]
def bstack1lll11lll1_opy_(config):
  bstack11ll11l11_opy_ = config.keys()
  for bstack1ll111lll1_opy_, bstack1l1ll1lll_opy_ in bstack1lll11111_opy_.items():
    if bstack1l1ll1lll_opy_ in bstack11ll11l11_opy_:
      config[bstack1ll111lll1_opy_] = config[bstack1l1ll1lll_opy_]
      del config[bstack1l1ll1lll_opy_]
  for bstack1ll111lll1_opy_, bstack1l1ll1lll_opy_ in bstack1llll1l1l1_opy_.items():
    if isinstance(bstack1l1ll1lll_opy_, list):
      for bstack111ll1lll_opy_ in bstack1l1ll1lll_opy_:
        if bstack111ll1lll_opy_ in bstack11ll11l11_opy_:
          config[bstack1ll111lll1_opy_] = config[bstack111ll1lll_opy_]
          del config[bstack111ll1lll_opy_]
          break
    elif bstack1l1ll1lll_opy_ in bstack11ll11l11_opy_:
      config[bstack1ll111lll1_opy_] = config[bstack1l1ll1lll_opy_]
      del config[bstack1l1ll1lll_opy_]
  for bstack111ll1lll_opy_ in list(config):
    for bstack11111ll1l_opy_ in bstack1ll1ll1111_opy_:
      if bstack111ll1lll_opy_.lower() == bstack11111ll1l_opy_.lower() and bstack111ll1lll_opy_ != bstack11111ll1l_opy_:
        config[bstack11111ll1l_opy_] = config[bstack111ll1lll_opy_]
        del config[bstack111ll1lll_opy_]
  bstack111l1l1l_opy_ = []
  if bstack1ll_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ࢵ") in config:
    bstack111l1l1l_opy_ = config[bstack1ll_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧࢶ")]
  for platform in bstack111l1l1l_opy_:
    for bstack111ll1lll_opy_ in list(platform):
      for bstack11111ll1l_opy_ in bstack1ll1ll1111_opy_:
        if bstack111ll1lll_opy_.lower() == bstack11111ll1l_opy_.lower() and bstack111ll1lll_opy_ != bstack11111ll1l_opy_:
          platform[bstack11111ll1l_opy_] = platform[bstack111ll1lll_opy_]
          del platform[bstack111ll1lll_opy_]
  for bstack1ll111lll1_opy_, bstack1l1ll1lll_opy_ in bstack1llll1l1l1_opy_.items():
    for platform in bstack111l1l1l_opy_:
      if isinstance(bstack1l1ll1lll_opy_, list):
        for bstack111ll1lll_opy_ in bstack1l1ll1lll_opy_:
          if bstack111ll1lll_opy_ in platform:
            platform[bstack1ll111lll1_opy_] = platform[bstack111ll1lll_opy_]
            del platform[bstack111ll1lll_opy_]
            break
      elif bstack1l1ll1lll_opy_ in platform:
        platform[bstack1ll111lll1_opy_] = platform[bstack1l1ll1lll_opy_]
        del platform[bstack1l1ll1lll_opy_]
  for bstack1lll1111l_opy_ in bstack1llll11ll_opy_:
    if bstack1lll1111l_opy_ in config:
      if not bstack1llll11ll_opy_[bstack1lll1111l_opy_] in config:
        config[bstack1llll11ll_opy_[bstack1lll1111l_opy_]] = {}
      config[bstack1llll11ll_opy_[bstack1lll1111l_opy_]].update(config[bstack1lll1111l_opy_])
      del config[bstack1lll1111l_opy_]
  for platform in bstack111l1l1l_opy_:
    for bstack1lll1111l_opy_ in bstack1llll11ll_opy_:
      if bstack1lll1111l_opy_ in list(platform):
        if not bstack1llll11ll_opy_[bstack1lll1111l_opy_] in platform:
          platform[bstack1llll11ll_opy_[bstack1lll1111l_opy_]] = {}
        platform[bstack1llll11ll_opy_[bstack1lll1111l_opy_]].update(platform[bstack1lll1111l_opy_])
        del platform[bstack1lll1111l_opy_]
  config = bstack1111l11l1_opy_(config)
  return config
def bstack11ll11l1_opy_(config):
  global bstack1l1111ll_opy_
  if bstack1ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࠩࢷ") in config and str(config[bstack1ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࠪࢸ")]).lower() != bstack1ll_opy_ (u"ࠧࡧࡣ࡯ࡷࡪ࠭ࢹ"):
    if not bstack1ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࡌࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬࢺ") in config:
      config[bstack1ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࡍࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭ࢻ")] = {}
    if not bstack1ll_opy_ (u"ࠪࡰࡴࡩࡡ࡭ࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬࢼ") in config[bstack1ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨࢽ")]:
      bstack1lllll1ll1_opy_ = datetime.datetime.now()
      bstack1ll11l111l_opy_ = bstack1lllll1ll1_opy_.strftime(bstack1ll_opy_ (u"ࠬࠫࡤࡠࠧࡥࡣࠪࡎࠥࡎࠩࢾ"))
      hostname = socket.gethostname()
      bstack11l11ll1l_opy_ = bstack1ll_opy_ (u"࠭ࠧࢿ").join(random.choices(string.ascii_lowercase + string.digits, k=4))
      identifier = bstack1ll_opy_ (u"ࠧࡼࡿࡢࡿࢂࡥࡻࡾࠩࣀ").format(bstack1ll11l111l_opy_, hostname, bstack11l11ll1l_opy_)
      config[bstack1ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࡌࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬࣁ")][bstack1ll_opy_ (u"ࠩ࡯ࡳࡨࡧ࡬ࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫࣂ")] = identifier
    bstack1l1111ll_opy_ = config[bstack1ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧࣃ")][bstack1ll_opy_ (u"ࠫࡱࡵࡣࡢ࡮ࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭ࣄ")]
  return config
def bstack1ll1l1l1l1_opy_():
  bstack1111llll_opy_ =  bstack11l111ll_opy_()[bstack1ll_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠫࣅ")]
  return bstack1111llll_opy_ if bstack1111llll_opy_ else -1
def bstack1lll1llll_opy_(bstack1111llll_opy_):
  global CONFIG
  if not bstack1ll_opy_ (u"࠭ࠤࡼࡄࡘࡍࡑࡊ࡟ࡏࡗࡐࡆࡊࡘࡽࠨࣆ") in CONFIG[bstack1ll_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩࣇ")]:
    return
  CONFIG[bstack1ll_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪࣈ")] = CONFIG[bstack1ll_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫࣉ")].replace(
    bstack1ll_opy_ (u"ࠪࠨࢀࡈࡕࡊࡎࡇࡣࡓ࡛ࡍࡃࡇࡕࢁࠬ࣊"),
    str(bstack1111llll_opy_)
  )
def bstack1ll11l1l_opy_():
  global CONFIG
  if not bstack1ll_opy_ (u"ࠫࠩࢁࡄࡂࡖࡈࡣ࡙ࡏࡍࡆࡿࠪ࣋") in CONFIG[bstack1ll_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧ࣌")]:
    return
  bstack1lllll1ll1_opy_ = datetime.datetime.now()
  bstack1ll11l111l_opy_ = bstack1lllll1ll1_opy_.strftime(bstack1ll_opy_ (u"࠭ࠥࡥ࠯ࠨࡦ࠲ࠫࡈ࠻ࠧࡐࠫ࣍"))
  CONFIG[bstack1ll_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩ࣎")] = CONFIG[bstack1ll_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴ࣏ࠪ")].replace(
    bstack1ll_opy_ (u"ࠩࠧࡿࡉࡇࡔࡆࡡࡗࡍࡒࡋࡽࠨ࣐"),
    bstack1ll11l111l_opy_
  )
def bstack1ll1ll1ll_opy_():
  global CONFIG
  if bstack1ll_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶ࣑ࠬ") in CONFIG and not bool(CONFIG[bstack1ll_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࣒࠭")]):
    del CONFIG[bstack1ll_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸ࣓ࠧ")]
    return
  if not bstack1ll_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨࣔ") in CONFIG:
    CONFIG[bstack1ll_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩࣕ")] = bstack1ll_opy_ (u"ࠨࠥࠧࡿࡇ࡛ࡉࡍࡆࡢࡒ࡚ࡓࡂࡆࡔࢀࠫࣖ")
  if bstack1ll_opy_ (u"ࠩࠧࡿࡉࡇࡔࡆࡡࡗࡍࡒࡋࡽࠨࣗ") in CONFIG[bstack1ll_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬࣘ")]:
    bstack1ll11l1l_opy_()
    os.environ[bstack1ll_opy_ (u"ࠫࡇ࡙ࡔࡂࡅࡎࡣࡈࡕࡍࡃࡋࡑࡉࡉࡥࡂࡖࡋࡏࡈࡤࡏࡄࠨࣙ")] = CONFIG[bstack1ll_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧࣚ")]
  if not bstack1ll_opy_ (u"࠭ࠤࡼࡄࡘࡍࡑࡊ࡟ࡏࡗࡐࡆࡊࡘࡽࠨࣛ") in CONFIG[bstack1ll_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩࣜ")]:
    return
  bstack1111llll_opy_ = bstack1ll_opy_ (u"ࠨࠩࣝ")
  bstack1llllll1l_opy_ = bstack1ll1l1l1l1_opy_()
  if bstack1llllll1l_opy_ != -1:
    bstack1111llll_opy_ = bstack1ll_opy_ (u"ࠩࡆࡍࠥ࠭ࣞ") + str(bstack1llllll1l_opy_)
  if bstack1111llll_opy_ == bstack1ll_opy_ (u"ࠪࠫࣟ"):
    bstack1ll111111l_opy_ = bstack1111ll1l_opy_(CONFIG[bstack1ll_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧ࣠")])
    if bstack1ll111111l_opy_ != -1:
      bstack1111llll_opy_ = str(bstack1ll111111l_opy_)
  if bstack1111llll_opy_:
    bstack1lll1llll_opy_(bstack1111llll_opy_)
    os.environ[bstack1ll_opy_ (u"ࠬࡈࡓࡕࡃࡆࡏࡤࡉࡏࡎࡄࡌࡒࡊࡊ࡟ࡃࡗࡌࡐࡉࡥࡉࡅࠩ࣡")] = CONFIG[bstack1ll_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨ࣢")]
def bstack1lllll111_opy_(bstack1111l1111_opy_, bstack11111l111_opy_, path):
  bstack11lll1ll_opy_ = {
    bstack1ll_opy_ (u"ࠧࡪࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࣣࠫ"): bstack11111l111_opy_
  }
  if os.path.exists(path):
    bstack11lllll1_opy_ = json.load(open(path, bstack1ll_opy_ (u"ࠨࡴࡥࠫࣤ")))
  else:
    bstack11lllll1_opy_ = {}
  bstack11lllll1_opy_[bstack1111l1111_opy_] = bstack11lll1ll_opy_
  with open(path, bstack1ll_opy_ (u"ࠤࡺ࠯ࠧࣥ")) as outfile:
    json.dump(bstack11lllll1_opy_, outfile)
def bstack1111ll1l_opy_(bstack1111l1111_opy_):
  bstack1111l1111_opy_ = str(bstack1111l1111_opy_)
  bstack1l11ll1ll_opy_ = os.path.join(os.path.expanduser(bstack1ll_opy_ (u"ࠪࢂࣦࠬ")), bstack1ll_opy_ (u"ࠫ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠫࣧ"))
  try:
    if not os.path.exists(bstack1l11ll1ll_opy_):
      os.makedirs(bstack1l11ll1ll_opy_)
    file_path = os.path.join(os.path.expanduser(bstack1ll_opy_ (u"ࠬࢄࠧࣨ")), bstack1ll_opy_ (u"࠭࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࣩ࠭"), bstack1ll_opy_ (u"ࠧ࠯ࡤࡸ࡭ࡱࡪ࠭࡯ࡣࡰࡩ࠲ࡩࡡࡤࡪࡨ࠲࡯ࡹ࡯࡯ࠩ࣪"))
    if not os.path.isfile(file_path):
      with open(file_path, bstack1ll_opy_ (u"ࠨࡹࠪ࣫")):
        pass
      with open(file_path, bstack1ll_opy_ (u"ࠤࡺ࠯ࠧ࣬")) as outfile:
        json.dump({}, outfile)
    with open(file_path, bstack1ll_opy_ (u"ࠪࡶ࣭ࠬ")) as bstack1llllllll_opy_:
      bstack1lll111lll_opy_ = json.load(bstack1llllllll_opy_)
    if bstack1111l1111_opy_ in bstack1lll111lll_opy_:
      bstack1ll11lll1_opy_ = bstack1lll111lll_opy_[bstack1111l1111_opy_][bstack1ll_opy_ (u"ࠫ࡮ࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨ࣮")]
      bstack1ll1llllll_opy_ = int(bstack1ll11lll1_opy_) + 1
      bstack1lllll111_opy_(bstack1111l1111_opy_, bstack1ll1llllll_opy_, file_path)
      return bstack1ll1llllll_opy_
    else:
      bstack1lllll111_opy_(bstack1111l1111_opy_, 1, file_path)
      return 1
  except Exception as e:
    logger.warn(bstack1l1l1l11_opy_.format(str(e)))
    return -1
def bstack1l1111l1l_opy_(config):
  if not config[bstack1ll_opy_ (u"ࠬࡻࡳࡦࡴࡑࡥࡲ࡫࣯ࠧ")] or not config[bstack1ll_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸࡑࡥࡺࣰࠩ")]:
    return True
  else:
    return False
def bstack1l1111l1_opy_(config, index=0):
  global bstack1l11l11ll_opy_
  bstack1lllll11_opy_ = {}
  caps = bstack1l111ll1_opy_ + bstack1l1lll111_opy_
  if bstack1l11l11ll_opy_:
    caps += bstack11l11l111_opy_
  for key in config:
    if key in caps + [bstack1ll_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࣱࠪ")]:
      continue
    bstack1lllll11_opy_[key] = config[key]
  if bstack1ll_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࣲࠫ") in config:
    for bstack111111l1_opy_ in config[bstack1ll_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬࣳ")][index]:
      if bstack111111l1_opy_ in caps + [bstack1ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡒࡦࡳࡥࠨࣴ"), bstack1ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠬࣵ")]:
        continue
      bstack1lllll11_opy_[bstack111111l1_opy_] = config[bstack1ll_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨࣶ")][index][bstack111111l1_opy_]
  bstack1lllll11_opy_[bstack1ll_opy_ (u"࠭ࡨࡰࡵࡷࡒࡦࡳࡥࠨࣷ")] = socket.gethostname()
  if bstack1ll_opy_ (u"ࠧࡷࡧࡵࡷ࡮ࡵ࡮ࠨࣸ") in bstack1lllll11_opy_:
    del (bstack1lllll11_opy_[bstack1ll_opy_ (u"ࠨࡸࡨࡶࡸ࡯࡯࡯ࣹࠩ")])
  return bstack1lllll11_opy_
def bstack11111l1l1_opy_(config):
  global bstack1l11l11ll_opy_
  bstack11l11ll11_opy_ = {}
  caps = bstack1l1lll111_opy_
  if bstack1l11l11ll_opy_:
    caps += bstack11l11l111_opy_
  for key in caps:
    if key in config:
      bstack11l11ll11_opy_[key] = config[key]
  return bstack11l11ll11_opy_
def bstack1lll1lll1l_opy_(bstack1lllll11_opy_, bstack11l11ll11_opy_):
  bstack1lllll1l1l_opy_ = {}
  for key in bstack1lllll11_opy_.keys():
    if key in bstack1lll11111_opy_:
      bstack1lllll1l1l_opy_[bstack1lll11111_opy_[key]] = bstack1lllll11_opy_[key]
    else:
      bstack1lllll1l1l_opy_[key] = bstack1lllll11_opy_[key]
  for key in bstack11l11ll11_opy_:
    if key in bstack1lll11111_opy_:
      bstack1lllll1l1l_opy_[bstack1lll11111_opy_[key]] = bstack11l11ll11_opy_[key]
    else:
      bstack1lllll1l1l_opy_[key] = bstack11l11ll11_opy_[key]
  return bstack1lllll1l1l_opy_
def bstack111l11lll_opy_(config, index=0):
  global bstack1l11l11ll_opy_
  config = copy.deepcopy(config)
  caps = {}
  bstack11l11ll11_opy_ = bstack11111l1l1_opy_(config)
  bstack1llll111_opy_ = bstack1l1lll111_opy_
  bstack1llll111_opy_ += bstack11lllll11_opy_
  if bstack1l11l11ll_opy_:
    bstack1llll111_opy_ += bstack11l11l111_opy_
  if bstack1ll_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࣺࠬ") in config:
    if bstack1ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡒࡦࡳࡥࠨࣻ") in config[bstack1ll_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧࣼ")][index]:
      caps[bstack1ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠪࣽ")] = config[bstack1ll_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩࣾ")][index][bstack1ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡏࡣࡰࡩࠬࣿ")]
    if bstack1ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩऀ") in config[bstack1ll_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬँ")][index]:
      caps[bstack1ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠫं")] = str(config[bstack1ll_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧः")][index][bstack1ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ऄ")])
    bstack1l11ll11l_opy_ = {}
    for bstack1l11l1111_opy_ in bstack1llll111_opy_:
      if bstack1l11l1111_opy_ in config[bstack1ll_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩअ")][index]:
        if bstack1l11l1111_opy_ == bstack1ll_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡘࡨࡶࡸ࡯࡯࡯ࠩआ"):
          try:
            bstack1l11ll11l_opy_[bstack1l11l1111_opy_] = str(config[bstack1ll_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫइ")][index][bstack1l11l1111_opy_] * 1.0)
          except:
            bstack1l11ll11l_opy_[bstack1l11l1111_opy_] = str(config[bstack1ll_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬई")][index][bstack1l11l1111_opy_])
        else:
          bstack1l11ll11l_opy_[bstack1l11l1111_opy_] = config[bstack1ll_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭उ")][index][bstack1l11l1111_opy_]
        del (config[bstack1ll_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧऊ")][index][bstack1l11l1111_opy_])
    bstack11l11ll11_opy_ = update(bstack11l11ll11_opy_, bstack1l11ll11l_opy_)
  bstack1lllll11_opy_ = bstack1l1111l1_opy_(config, index)
  for bstack111ll1lll_opy_ in bstack1l1lll111_opy_ + [bstack1ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠪऋ"), bstack1ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠧऌ")]:
    if bstack111ll1lll_opy_ in bstack1lllll11_opy_:
      bstack11l11ll11_opy_[bstack111ll1lll_opy_] = bstack1lllll11_opy_[bstack111ll1lll_opy_]
      del (bstack1lllll11_opy_[bstack111ll1lll_opy_])
  if bstack111lll111_opy_(config):
    bstack1lllll11_opy_[bstack1ll_opy_ (u"ࠧࡶࡵࡨ࡛࠸ࡉࠧऍ")] = True
    caps.update(bstack11l11ll11_opy_)
    caps[bstack1ll_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫࠻ࡱࡳࡸ࡮ࡵ࡮ࡴࠩऎ")] = bstack1lllll11_opy_
  else:
    bstack1lllll11_opy_[bstack1ll_opy_ (u"ࠩࡸࡷࡪ࡝࠳ࡄࠩए")] = False
    caps.update(bstack1lll1lll1l_opy_(bstack1lllll11_opy_, bstack11l11ll11_opy_))
    if bstack1ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡒࡦࡳࡥࠨऐ") in caps:
      caps[bstack1ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࠬऑ")] = caps[bstack1ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠪऒ")]
      del (caps[bstack1ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡎࡢ࡯ࡨࠫओ")])
    if bstack1ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠨऔ") in caps:
      caps[bstack1ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡡࡹࡩࡷࡹࡩࡰࡰࠪक")] = caps[bstack1ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪख")]
      del (caps[bstack1ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠫग")])
  return caps
def bstack1l1l1ll11_opy_():
  global bstack1l111l111_opy_
  if bstack1l1lllllll_opy_() <= version.parse(bstack1ll_opy_ (u"ࠫ࠸࠴࠱࠴࠰࠳ࠫघ")):
    if bstack1l111l111_opy_ != bstack1ll_opy_ (u"ࠬ࠭ङ"):
      return bstack1ll_opy_ (u"ࠨࡨࡵࡶࡳ࠾࠴࠵ࠢच") + bstack1l111l111_opy_ + bstack1ll_opy_ (u"ࠢ࠻࠺࠳࠳ࡼࡪ࠯ࡩࡷࡥࠦछ")
    return bstack1ll1l11l11_opy_
  if bstack1l111l111_opy_ != bstack1ll_opy_ (u"ࠨࠩज"):
    return bstack1ll_opy_ (u"ࠤ࡫ࡸࡹࡶࡳ࠻࠱࠲ࠦझ") + bstack1l111l111_opy_ + bstack1ll_opy_ (u"ࠥ࠳ࡼࡪ࠯ࡩࡷࡥࠦञ")
  return bstack1llllll1ll_opy_
def bstack1lllllllll_opy_(options):
  return hasattr(options, bstack1ll_opy_ (u"ࠫࡸ࡫ࡴࡠࡥࡤࡴࡦࡨࡩ࡭࡫ࡷࡽࠬट"))
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
def bstack1ll1ll11ll_opy_(options, bstack1ll1l11l_opy_):
  for bstack1llll1ll11_opy_ in bstack1ll1l11l_opy_:
    if bstack1llll1ll11_opy_ in [bstack1ll_opy_ (u"ࠬࡧࡲࡨࡵࠪठ"), bstack1ll_opy_ (u"࠭ࡥࡹࡶࡨࡲࡸ࡯࡯࡯ࡵࠪड")]:
      continue
    if bstack1llll1ll11_opy_ in options._experimental_options:
      options._experimental_options[bstack1llll1ll11_opy_] = update(options._experimental_options[bstack1llll1ll11_opy_],
                                                         bstack1ll1l11l_opy_[bstack1llll1ll11_opy_])
    else:
      options.add_experimental_option(bstack1llll1ll11_opy_, bstack1ll1l11l_opy_[bstack1llll1ll11_opy_])
  if bstack1ll_opy_ (u"ࠧࡢࡴࡪࡷࠬढ") in bstack1ll1l11l_opy_:
    for arg in bstack1ll1l11l_opy_[bstack1ll_opy_ (u"ࠨࡣࡵ࡫ࡸ࠭ण")]:
      options.add_argument(arg)
    del (bstack1ll1l11l_opy_[bstack1ll_opy_ (u"ࠩࡤࡶ࡬ࡹࠧत")])
  if bstack1ll_opy_ (u"ࠪࡩࡽࡺࡥ࡯ࡵ࡬ࡳࡳࡹࠧथ") in bstack1ll1l11l_opy_:
    for ext in bstack1ll1l11l_opy_[bstack1ll_opy_ (u"ࠫࡪࡾࡴࡦࡰࡶ࡭ࡴࡴࡳࠨद")]:
      options.add_extension(ext)
    del (bstack1ll1l11l_opy_[bstack1ll_opy_ (u"ࠬ࡫ࡸࡵࡧࡱࡷ࡮ࡵ࡮ࡴࠩध")])
def bstack1ll1ll1ll1_opy_(options, bstack111l11111_opy_):
  if bstack1ll_opy_ (u"࠭ࡰࡳࡧࡩࡷࠬन") in bstack111l11111_opy_:
    for bstack1ll1ll1l1l_opy_ in bstack111l11111_opy_[bstack1ll_opy_ (u"ࠧࡱࡴࡨࡪࡸ࠭ऩ")]:
      if bstack1ll1ll1l1l_opy_ in options._preferences:
        options._preferences[bstack1ll1ll1l1l_opy_] = update(options._preferences[bstack1ll1ll1l1l_opy_], bstack111l11111_opy_[bstack1ll_opy_ (u"ࠨࡲࡵࡩ࡫ࡹࠧप")][bstack1ll1ll1l1l_opy_])
      else:
        options.set_preference(bstack1ll1ll1l1l_opy_, bstack111l11111_opy_[bstack1ll_opy_ (u"ࠩࡳࡶࡪ࡬ࡳࠨफ")][bstack1ll1ll1l1l_opy_])
  if bstack1ll_opy_ (u"ࠪࡥࡷ࡭ࡳࠨब") in bstack111l11111_opy_:
    for arg in bstack111l11111_opy_[bstack1ll_opy_ (u"ࠫࡦࡸࡧࡴࠩभ")]:
      options.add_argument(arg)
def bstack11l1lll1_opy_(options, bstack1ll111l1l_opy_):
  if bstack1ll_opy_ (u"ࠬࡽࡥࡣࡸ࡬ࡩࡼ࠭म") in bstack1ll111l1l_opy_:
    options.use_webview(bool(bstack1ll111l1l_opy_[bstack1ll_opy_ (u"࠭ࡷࡦࡤࡹ࡭ࡪࡽࠧय")]))
  bstack1ll1ll11ll_opy_(options, bstack1ll111l1l_opy_)
def bstack111111l11_opy_(options, bstack1ll111lll_opy_):
  for bstack111ll1l1_opy_ in bstack1ll111lll_opy_:
    if bstack111ll1l1_opy_ in [bstack1ll_opy_ (u"ࠧࡵࡧࡦ࡬ࡳࡵ࡬ࡰࡩࡼࡔࡷ࡫ࡶࡪࡧࡺࠫर"), bstack1ll_opy_ (u"ࠨࡣࡵ࡫ࡸ࠭ऱ")]:
      continue
    options.set_capability(bstack111ll1l1_opy_, bstack1ll111lll_opy_[bstack111ll1l1_opy_])
  if bstack1ll_opy_ (u"ࠩࡤࡶ࡬ࡹࠧल") in bstack1ll111lll_opy_:
    for arg in bstack1ll111lll_opy_[bstack1ll_opy_ (u"ࠪࡥࡷ࡭ࡳࠨळ")]:
      options.add_argument(arg)
  if bstack1ll_opy_ (u"ࠫࡹ࡫ࡣࡩࡰࡲࡰࡴ࡭ࡹࡑࡴࡨࡺ࡮࡫ࡷࠨऴ") in bstack1ll111lll_opy_:
    options.bstack1111llll1_opy_(bool(bstack1ll111lll_opy_[bstack1ll_opy_ (u"ࠬࡺࡥࡤࡪࡱࡳࡱࡵࡧࡺࡒࡵࡩࡻ࡯ࡥࡸࠩव")]))
def bstack11l11l11_opy_(options, bstack111lll11l_opy_):
  for bstack1lllll1111_opy_ in bstack111lll11l_opy_:
    if bstack1lllll1111_opy_ in [bstack1ll_opy_ (u"࠭ࡡࡥࡦ࡬ࡸ࡮ࡵ࡮ࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪश"), bstack1ll_opy_ (u"ࠧࡢࡴࡪࡷࠬष")]:
      continue
    options._options[bstack1lllll1111_opy_] = bstack111lll11l_opy_[bstack1lllll1111_opy_]
  if bstack1ll_opy_ (u"ࠨࡣࡧࡨ࡮ࡺࡩࡰࡰࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬस") in bstack111lll11l_opy_:
    for bstack1ll11lll_opy_ in bstack111lll11l_opy_[bstack1ll_opy_ (u"ࠩࡤࡨࡩ࡯ࡴࡪࡱࡱࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭ह")]:
      options.bstack1lll11111l_opy_(
        bstack1ll11lll_opy_, bstack111lll11l_opy_[bstack1ll_opy_ (u"ࠪࡥࡩࡪࡩࡵ࡫ࡲࡲࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧऺ")][bstack1ll11lll_opy_])
  if bstack1ll_opy_ (u"ࠫࡦࡸࡧࡴࠩऻ") in bstack111lll11l_opy_:
    for arg in bstack111lll11l_opy_[bstack1ll_opy_ (u"ࠬࡧࡲࡨࡵ़ࠪ")]:
      options.add_argument(arg)
def bstack1l1111ll1_opy_(options, caps):
  if not hasattr(options, bstack1ll_opy_ (u"࠭ࡋࡆ࡛ࠪऽ")):
    return
  if options.KEY == bstack1ll_opy_ (u"ࠧࡨࡱࡲ࡫࠿ࡩࡨࡳࡱࡰࡩࡔࡶࡴࡪࡱࡱࡷࠬा") and options.KEY in caps:
    bstack1ll1ll11ll_opy_(options, caps[bstack1ll_opy_ (u"ࠨࡩࡲࡳ࡬ࡀࡣࡩࡴࡲࡱࡪࡕࡰࡵ࡫ࡲࡲࡸ࠭ि")])
  elif options.KEY == bstack1ll_opy_ (u"ࠩࡰࡳࡿࡀࡦࡪࡴࡨࡪࡴࡾࡏࡱࡶ࡬ࡳࡳࡹࠧी") and options.KEY in caps:
    bstack1ll1ll1ll1_opy_(options, caps[bstack1ll_opy_ (u"ࠪࡱࡴࢀ࠺ࡧ࡫ࡵࡩ࡫ࡵࡸࡐࡲࡷ࡭ࡴࡴࡳࠨु")])
  elif options.KEY == bstack1ll_opy_ (u"ࠫࡸࡧࡦࡢࡴ࡬࠲ࡴࡶࡴࡪࡱࡱࡷࠬू") and options.KEY in caps:
    bstack111111l11_opy_(options, caps[bstack1ll_opy_ (u"ࠬࡹࡡࡧࡣࡵ࡭࠳ࡵࡰࡵ࡫ࡲࡲࡸ࠭ृ")])
  elif options.KEY == bstack1ll_opy_ (u"࠭࡭ࡴ࠼ࡨࡨ࡬࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧॄ") and options.KEY in caps:
    bstack11l1lll1_opy_(options, caps[bstack1ll_opy_ (u"ࠧ࡮ࡵ࠽ࡩࡩ࡭ࡥࡐࡲࡷ࡭ࡴࡴࡳࠨॅ")])
  elif options.KEY == bstack1ll_opy_ (u"ࠨࡵࡨ࠾࡮࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧॆ") and options.KEY in caps:
    bstack11l11l11_opy_(options, caps[bstack1ll_opy_ (u"ࠩࡶࡩ࠿࡯ࡥࡐࡲࡷ࡭ࡴࡴࡳࠨे")])
def bstack1111l1l11_opy_(caps):
  global bstack1l11l11ll_opy_
  if isinstance(os.environ.get(bstack1ll_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡌࡗࡤࡇࡐࡑࡡࡄ࡙࡙ࡕࡍࡂࡖࡈࠫै")), str):
    bstack1l11l11ll_opy_ = eval(os.getenv(bstack1ll_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡍࡘࡥࡁࡑࡒࡢࡅ࡚࡚ࡏࡎࡃࡗࡉࠬॉ")))
  if bstack1l11l11ll_opy_:
    if bstack1l1ll1l1_opy_() < version.parse(bstack1ll_opy_ (u"ࠬ࠸࠮࠴࠰࠳ࠫॊ")):
      return None
    else:
      from appium.options.common.base import AppiumOptions
      options = AppiumOptions().load_capabilities(caps)
      return options
  else:
    browser = bstack1ll_opy_ (u"࠭ࡣࡩࡴࡲࡱࡪ࠭ो")
    if bstack1ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡏࡣࡰࡩࠬौ") in caps:
      browser = caps[bstack1ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡐࡤࡱࡪ्࠭")]
    elif bstack1ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࠪॎ") in caps:
      browser = caps[bstack1ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࠫॏ")]
    browser = str(browser).lower()
    if browser == bstack1ll_opy_ (u"ࠫ࡮ࡶࡨࡰࡰࡨࠫॐ") or browser == bstack1ll_opy_ (u"ࠬ࡯ࡰࡢࡦࠪ॑"):
      browser = bstack1ll_opy_ (u"࠭ࡳࡢࡨࡤࡶ࡮॒࠭")
    if browser == bstack1ll_opy_ (u"ࠧࡴࡣࡰࡷࡺࡴࡧࠨ॓"):
      browser = bstack1ll_opy_ (u"ࠨࡥ࡫ࡶࡴࡳࡥࠨ॔")
    if browser not in [bstack1ll_opy_ (u"ࠩࡦ࡬ࡷࡵ࡭ࡦࠩॕ"), bstack1ll_opy_ (u"ࠪࡩࡩ࡭ࡥࠨॖ"), bstack1ll_opy_ (u"ࠫ࡮࡫ࠧॗ"), bstack1ll_opy_ (u"ࠬࡹࡡࡧࡣࡵ࡭ࠬक़"), bstack1ll_opy_ (u"࠭ࡦࡪࡴࡨࡪࡴࡾࠧख़")]:
      return None
    try:
      package = bstack1ll_opy_ (u"ࠧࡴࡧ࡯ࡩࡳ࡯ࡵ࡮࠰ࡺࡩࡧࡪࡲࡪࡸࡨࡶ࠳ࢁࡽ࠯ࡱࡳࡸ࡮ࡵ࡮ࡴࠩग़").format(browser)
      name = bstack1ll_opy_ (u"ࠨࡑࡳࡸ࡮ࡵ࡮ࡴࠩज़")
      browser_options = getattr(__import__(package, fromlist=[name]), name)
      options = browser_options()
      if not bstack1lllllllll_opy_(options):
        return None
      for bstack111ll1lll_opy_ in caps.keys():
        options.set_capability(bstack111ll1lll_opy_, caps[bstack111ll1lll_opy_])
      bstack1l1111ll1_opy_(options, caps)
      return options
    except Exception as e:
      logger.debug(str(e))
      return None
def bstack11l111l11_opy_(options, bstack1l1l1111_opy_):
  if not bstack1lllllllll_opy_(options):
    return
  for bstack111ll1lll_opy_ in bstack1l1l1111_opy_.keys():
    if bstack111ll1lll_opy_ in bstack11lllll11_opy_:
      continue
    if bstack111ll1lll_opy_ in options._caps and type(options._caps[bstack111ll1lll_opy_]) in [dict, list]:
      options._caps[bstack111ll1lll_opy_] = update(options._caps[bstack111ll1lll_opy_], bstack1l1l1111_opy_[bstack111ll1lll_opy_])
    else:
      options.set_capability(bstack111ll1lll_opy_, bstack1l1l1111_opy_[bstack111ll1lll_opy_])
  bstack1l1111ll1_opy_(options, bstack1l1l1111_opy_)
  if bstack1ll_opy_ (u"ࠩࡰࡳࡿࡀࡤࡦࡤࡸ࡫࡬࡫ࡲࡂࡦࡧࡶࡪࡹࡳࠨड़") in options._caps:
    if options._caps[bstack1ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡒࡦࡳࡥࠨढ़")] and options._caps[bstack1ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡓࡧ࡭ࡦࠩफ़")].lower() != bstack1ll_opy_ (u"ࠬ࡬ࡩࡳࡧࡩࡳࡽ࠭य़"):
      del options._caps[bstack1ll_opy_ (u"࠭࡭ࡰࡼ࠽ࡨࡪࡨࡵࡨࡩࡨࡶࡆࡪࡤࡳࡧࡶࡷࠬॠ")]
def bstack1ll1lllll1_opy_(proxy_config):
  if bstack1ll_opy_ (u"ࠧࡩࡶࡷࡴࡸࡖࡲࡰࡺࡼࠫॡ") in proxy_config:
    proxy_config[bstack1ll_opy_ (u"ࠨࡵࡶࡰࡕࡸ࡯ࡹࡻࠪॢ")] = proxy_config[bstack1ll_opy_ (u"ࠩ࡫ࡸࡹࡶࡳࡑࡴࡲࡼࡾ࠭ॣ")]
    del (proxy_config[bstack1ll_opy_ (u"ࠪ࡬ࡹࡺࡰࡴࡒࡵࡳࡽࡿࠧ।")])
  if bstack1ll_opy_ (u"ࠫࡵࡸ࡯ࡹࡻࡗࡽࡵ࡫ࠧ॥") in proxy_config and proxy_config[bstack1ll_opy_ (u"ࠬࡶࡲࡰࡺࡼࡘࡾࡶࡥࠨ०")].lower() != bstack1ll_opy_ (u"࠭ࡤࡪࡴࡨࡧࡹ࠭१"):
    proxy_config[bstack1ll_opy_ (u"ࠧࡱࡴࡲࡼࡾ࡚ࡹࡱࡧࠪ२")] = bstack1ll_opy_ (u"ࠨ࡯ࡤࡲࡺࡧ࡬ࠨ३")
  if bstack1ll_opy_ (u"ࠩࡳࡶࡴࡾࡹࡂࡷࡷࡳࡨࡵ࡮ࡧ࡫ࡪ࡙ࡷࡲࠧ४") in proxy_config:
    proxy_config[bstack1ll_opy_ (u"ࠪࡴࡷࡵࡸࡺࡖࡼࡴࡪ࠭५")] = bstack1ll_opy_ (u"ࠫࡵࡧࡣࠨ६")
  return proxy_config
def bstack1ll11111l_opy_(config, proxy):
  from selenium.webdriver.common.proxy import Proxy
  if not bstack1ll_opy_ (u"ࠬࡶࡲࡰࡺࡼࠫ७") in config:
    return proxy
  config[bstack1ll_opy_ (u"࠭ࡰࡳࡱࡻࡽࠬ८")] = bstack1ll1lllll1_opy_(config[bstack1ll_opy_ (u"ࠧࡱࡴࡲࡼࡾ࠭९")])
  if proxy == None:
    proxy = Proxy(config[bstack1ll_opy_ (u"ࠨࡲࡵࡳࡽࡿࠧ॰")])
  return proxy
def bstack1l1lll11_opy_(self):
  global CONFIG
  global bstack1ll1111l1_opy_
  try:
    proxy = bstack1l111ll11_opy_(CONFIG)
    if proxy:
      if proxy.endswith(bstack1ll_opy_ (u"ࠩ࠱ࡴࡦࡩࠧॱ")):
        proxies = bstack11llllll_opy_(proxy, bstack1l1l1ll11_opy_())
        if len(proxies) > 0:
          protocol, bstack1l1llll11_opy_ = proxies.popitem()
          if bstack1ll_opy_ (u"ࠥ࠾࠴࠵ࠢॲ") in bstack1l1llll11_opy_:
            return bstack1l1llll11_opy_
          else:
            return bstack1ll_opy_ (u"ࠦ࡭ࡺࡴࡱ࠼࠲࠳ࠧॳ") + bstack1l1llll11_opy_
      else:
        return proxy
  except Exception as e:
    logger.error(bstack1ll_opy_ (u"ࠧࡋࡲࡳࡱࡵࠤ࡮ࡴࠠࡴࡧࡷࡸ࡮ࡴࡧࠡࡲࡵࡳࡽࡿࠠࡶࡴ࡯ࠤ࠿ࠦࡻࡾࠤॴ").format(str(e)))
  return bstack1ll1111l1_opy_(self)
def bstack111l1l1l1_opy_():
  global CONFIG
  return bstack1lll11lll_opy_(CONFIG) and bstack111ll111l_opy_() and bstack1l1lllllll_opy_() >= version.parse(bstack11l1111l_opy_)
def bstack11llll111_opy_():
  global CONFIG
  return (bstack1ll_opy_ (u"࠭ࡨࡵࡶࡳࡔࡷࡵࡸࡺࠩॵ") in CONFIG or bstack1ll_opy_ (u"ࠧࡩࡶࡷࡴࡸࡖࡲࡰࡺࡼࠫॶ") in CONFIG) and bstack1lll11ll1l_opy_()
def bstack1ll11l1111_opy_(config):
  bstack111lll1ll_opy_ = {}
  if bstack1ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࡌࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬॷ") in config:
    bstack111lll1ll_opy_ = config[bstack1ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࡍࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭ॸ")]
  if bstack1ll_opy_ (u"ࠪࡰࡴࡩࡡ࡭ࡑࡳࡸ࡮ࡵ࡮ࡴࠩॹ") in config:
    bstack111lll1ll_opy_ = config[bstack1ll_opy_ (u"ࠫࡱࡵࡣࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪॺ")]
  proxy = bstack1l111ll11_opy_(config)
  if proxy:
    if proxy.endswith(bstack1ll_opy_ (u"ࠬ࠴ࡰࡢࡥࠪॻ")) and os.path.isfile(proxy):
      bstack111lll1ll_opy_[bstack1ll_opy_ (u"࠭࠭ࡱࡣࡦ࠱࡫࡯࡬ࡦࠩॼ")] = proxy
    else:
      parsed_url = None
      if proxy.endswith(bstack1ll_opy_ (u"ࠧ࠯ࡲࡤࡧࠬॽ")):
        proxies = bstack1llll1111_opy_(config, bstack1l1l1ll11_opy_())
        if len(proxies) > 0:
          protocol, bstack1l1llll11_opy_ = proxies.popitem()
          if bstack1ll_opy_ (u"ࠣ࠼࠲࠳ࠧॾ") in bstack1l1llll11_opy_:
            parsed_url = urlparse(bstack1l1llll11_opy_)
          else:
            parsed_url = urlparse(protocol + bstack1ll_opy_ (u"ࠤ࠽࠳࠴ࠨॿ") + bstack1l1llll11_opy_)
      else:
        parsed_url = urlparse(proxy)
      if parsed_url and parsed_url.hostname: bstack111lll1ll_opy_[bstack1ll_opy_ (u"ࠪࡴࡷࡵࡸࡺࡊࡲࡷࡹ࠭ঀ")] = str(parsed_url.hostname)
      if parsed_url and parsed_url.port: bstack111lll1ll_opy_[bstack1ll_opy_ (u"ࠫࡵࡸ࡯ࡹࡻࡓࡳࡷࡺࠧঁ")] = str(parsed_url.port)
      if parsed_url and parsed_url.username: bstack111lll1ll_opy_[bstack1ll_opy_ (u"ࠬࡶࡲࡰࡺࡼ࡙ࡸ࡫ࡲࠨং")] = str(parsed_url.username)
      if parsed_url and parsed_url.password: bstack111lll1ll_opy_[bstack1ll_opy_ (u"࠭ࡰࡳࡱࡻࡽࡕࡧࡳࡴࠩঃ")] = str(parsed_url.password)
  return bstack111lll1ll_opy_
def bstack111l1111l_opy_(config):
  if bstack1ll_opy_ (u"ࠧࡵࡧࡶࡸࡈࡵ࡮ࡵࡧࡻࡸࡔࡶࡴࡪࡱࡱࡷࠬ঄") in config:
    return config[bstack1ll_opy_ (u"ࠨࡶࡨࡷࡹࡉ࡯࡯ࡶࡨࡼࡹࡕࡰࡵ࡫ࡲࡲࡸ࠭অ")]
  return {}
def bstack1ll1llll11_opy_(caps):
  global bstack1l1111ll_opy_
  if bstack1ll_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬࠼ࡲࡴࡹ࡯࡯࡯ࡵࠪআ") in caps:
    caps[bstack1ll_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭࠽ࡳࡵࡺࡩࡰࡰࡶࠫই")][bstack1ll_opy_ (u"ࠫࡱࡵࡣࡢ࡮ࠪঈ")] = True
    if bstack1l1111ll_opy_:
      caps[bstack1ll_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯࠿ࡵࡰࡵ࡫ࡲࡲࡸ࠭উ")][bstack1ll_opy_ (u"࠭࡬ࡰࡥࡤࡰࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨঊ")] = bstack1l1111ll_opy_
  else:
    caps[bstack1ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴࡬ࡰࡥࡤࡰࠬঋ")] = True
    if bstack1l1111ll_opy_:
      caps[bstack1ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮࡭ࡱࡦࡥࡱࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩঌ")] = bstack1l1111ll_opy_
def bstack11l1l11l1_opy_():
  global CONFIG
  if bstack1ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡍࡱࡦࡥࡱ࠭঍") in CONFIG and CONFIG[bstack1ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࠧ঎")]:
    bstack111lll1ll_opy_ = bstack1ll11l1111_opy_(CONFIG)
    bstack111l1111_opy_(CONFIG[bstack1ll_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶࡏࡪࡿࠧএ")], bstack111lll1ll_opy_)
def bstack111l1111_opy_(key, bstack111lll1ll_opy_):
  global bstack1ll1l1ll_opy_
  logger.info(bstack1l1ll111_opy_)
  try:
    bstack1ll1l1ll_opy_ = Local()
    bstack1lllllll1_opy_ = {bstack1ll_opy_ (u"ࠬࡱࡥࡺࠩঐ"): key}
    bstack1lllllll1_opy_.update(bstack111lll1ll_opy_)
    logger.debug(bstack1ll1l111l_opy_.format(str(bstack1lllllll1_opy_)))
    bstack1ll1l1ll_opy_.start(**bstack1lllllll1_opy_)
    if bstack1ll1l1ll_opy_.isRunning():
      logger.info(bstack1ll1111l11_opy_)
  except Exception as e:
    bstack11l1l1l11_opy_(bstack1llll111ll_opy_.format(str(e)))
def bstack1ll1lll111_opy_():
  global bstack1ll1l1ll_opy_
  if bstack1ll1l1ll_opy_.isRunning():
    logger.info(bstack1ll1l1ll11_opy_)
    bstack1ll1l1ll_opy_.stop()
  bstack1ll1l1ll_opy_ = None
def bstack111lllll1_opy_(bstack111111ll1_opy_=[]):
  global CONFIG
  bstack11lll11l_opy_ = []
  bstack1llll111l1_opy_ = [bstack1ll_opy_ (u"࠭࡯ࡴࠩ঑"), bstack1ll_opy_ (u"ࠧࡰࡵ࡙ࡩࡷࡹࡩࡰࡰࠪ঒"), bstack1ll_opy_ (u"ࠨࡦࡨࡺ࡮ࡩࡥࡏࡣࡰࡩࠬও"), bstack1ll_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰ࡚ࡪࡸࡳࡪࡱࡱࠫঔ"), bstack1ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡒࡦࡳࡥࠨক"), bstack1ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠬখ")]
  try:
    for err in bstack111111ll1_opy_:
      bstack1111l11l_opy_ = {}
      for k in bstack1llll111l1_opy_:
        val = CONFIG[bstack1ll_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨগ")][int(err[bstack1ll_opy_ (u"࠭ࡩ࡯ࡦࡨࡼࠬঘ")])].get(k)
        if val:
          bstack1111l11l_opy_[k] = val
      bstack1111l11l_opy_[bstack1ll_opy_ (u"ࠧࡵࡧࡶࡸࡸ࠭ঙ")] = {
        err[bstack1ll_opy_ (u"ࠨࡰࡤࡱࡪ࠭চ")]: err[bstack1ll_opy_ (u"ࠩࡨࡶࡷࡵࡲࠨছ")]
      }
      bstack11lll11l_opy_.append(bstack1111l11l_opy_)
  except Exception as e:
    logger.debug(bstack1ll_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥ࡬࡯ࡳ࡯ࡤࡸࡹ࡯࡮ࡨࠢࡧࡥࡹࡧࠠࡧࡱࡵࠤࡪࡼࡥ࡯ࡶ࠽ࠤࠬজ") + str(e))
  finally:
    return bstack11lll11l_opy_
def bstack1l11ll1l1_opy_(file_name):
  bstack1l11l1l11_opy_ = []
  try:
    bstack11l111l1_opy_ = os.path.join(tempfile.gettempdir(), file_name)
    if os.path.exists(bstack11l111l1_opy_):
      with open(bstack11l111l1_opy_) as f:
        bstack1llll11111_opy_ = json.load(f)
        bstack1l11l1l11_opy_ = bstack1llll11111_opy_
      os.remove(bstack11l111l1_opy_)
    return bstack1l11l1l11_opy_
  except Exception as e:
    logger.debug(bstack1ll_opy_ (u"ࠫࡊࡸࡲࡰࡴࠣ࡭ࡳࠦࡦࡪࡰࡧ࡭ࡳ࡭ࠠࡦࡴࡵࡳࡷࠦ࡬ࡪࡵࡷ࠾ࠥ࠭ঝ") + str(e))
def bstack1ll1l1ll1l_opy_():
  global bstack1l11lllll_opy_
  global bstack11l1l1l1l_opy_
  global bstack11lllllll_opy_
  global bstack11l1l1111_opy_
  global bstack1lllllll1l_opy_
  global bstack11111l1ll_opy_
  percy.shutdown()
  if bstack1l11lllll_opy_:
    logger.warning(bstack1l111l11_opy_.format(str(bstack1l11lllll_opy_)))
  else:
    try:
      bstack11lllll1_opy_ = bstack1l1ll1ll1_opy_(bstack1ll_opy_ (u"ࠬ࠴ࡢࡴࡶࡤࡧࡰ࠳ࡣࡰࡰࡩ࡭࡬࠴ࡪࡴࡱࡱࠫঞ"), logger)
      if bstack11lllll1_opy_.get(bstack1ll_opy_ (u"࠭࡮ࡶࡦࡪࡩࡤࡲ࡯ࡤࡣ࡯ࠫট")) and bstack11lllll1_opy_.get(bstack1ll_opy_ (u"ࠧ࡯ࡷࡧ࡫ࡪࡥ࡬ࡰࡥࡤࡰࠬঠ")).get(bstack1ll_opy_ (u"ࠨࡪࡲࡷࡹࡴࡡ࡮ࡧࠪড")):
        logger.warning(bstack1l111l11_opy_.format(str(bstack11lllll1_opy_[bstack1ll_opy_ (u"ࠩࡱࡹࡩ࡭ࡥࡠ࡮ࡲࡧࡦࡲࠧঢ")][bstack1ll_opy_ (u"ࠪ࡬ࡴࡹࡴ࡯ࡣࡰࡩࠬণ")])))
    except Exception as e:
      logger.error(e)
  logger.info(bstack1l1l11lll_opy_)
  global bstack1ll1l1ll_opy_
  if bstack1ll1l1ll_opy_:
    bstack1ll1lll111_opy_()
  try:
    for driver in bstack11l1l1l1l_opy_:
      driver.quit()
  except Exception as e:
    pass
  logger.info(bstack111l11l1_opy_)
  if bstack11111l1ll_opy_ == bstack1ll_opy_ (u"ࠫࡷࡵࡢࡰࡶࠪত"):
    bstack1lllllll1l_opy_ = bstack1l11ll1l1_opy_(bstack1ll_opy_ (u"ࠬࡸ࡯ࡣࡱࡷࡣࡪࡸࡲࡰࡴࡢࡰ࡮ࡹࡴ࠯࡬ࡶࡳࡳ࠭থ"))
  if bstack11111l1ll_opy_ == bstack1ll_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭দ") and len(bstack11l1l1111_opy_) == 0:
    bstack11l1l1111_opy_ = bstack1l11ll1l1_opy_(bstack1ll_opy_ (u"ࠧࡱࡹࡢࡴࡾࡺࡥࡴࡶࡢࡩࡷࡸ࡯ࡳࡡ࡯࡭ࡸࡺ࠮࡫ࡵࡲࡲࠬধ"))
    if len(bstack11l1l1111_opy_) == 0:
      bstack11l1l1111_opy_ = bstack1l11ll1l1_opy_(bstack1ll_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࡠࡲࡳࡴࡤ࡫ࡲࡳࡱࡵࡣࡱ࡯ࡳࡵ࠰࡭ࡷࡴࡴࠧন"))
  bstack11lll1l11_opy_ = bstack1ll_opy_ (u"ࠩࠪ঩")
  if len(bstack11lllllll_opy_) > 0:
    bstack11lll1l11_opy_ = bstack111lllll1_opy_(bstack11lllllll_opy_)
  elif len(bstack11l1l1111_opy_) > 0:
    bstack11lll1l11_opy_ = bstack111lllll1_opy_(bstack11l1l1111_opy_)
  elif len(bstack1lllllll1l_opy_) > 0:
    bstack11lll1l11_opy_ = bstack111lllll1_opy_(bstack1lllllll1l_opy_)
  elif len(bstack1ll1llll_opy_) > 0:
    bstack11lll1l11_opy_ = bstack111lllll1_opy_(bstack1ll1llll_opy_)
  if bool(bstack11lll1l11_opy_):
    bstack1l1ll1l11_opy_(bstack11lll1l11_opy_)
  else:
    bstack1l1ll1l11_opy_()
  bstack11111l11l_opy_(bstack1llll1111l_opy_, logger)
def bstack1lllll1lll_opy_(self, *args):
  logger.error(bstack1lll1lll11_opy_)
  bstack1ll1l1ll1l_opy_()
  sys.exit(1)
def bstack11l1l1l11_opy_(err):
  logger.critical(bstack1ll11ll1l_opy_.format(str(err)))
  bstack1l1ll1l11_opy_(bstack1ll11ll1l_opy_.format(str(err)))
  atexit.unregister(bstack1ll1l1ll1l_opy_)
  sys.exit(1)
def bstack11111l1l_opy_(error, message):
  logger.critical(str(error))
  logger.critical(message)
  bstack1l1ll1l11_opy_(message)
  atexit.unregister(bstack1ll1l1ll1l_opy_)
  sys.exit(1)
def bstack1l11lll1l_opy_():
  global CONFIG
  global bstack1ll1l1111_opy_
  global bstack1l1ll1l1l_opy_
  global bstack1lll1l11l_opy_
  CONFIG = bstack111l1ll1_opy_()
  bstack11llll1l1_opy_()
  bstack1l11l111_opy_()
  CONFIG = bstack1lll11lll1_opy_(CONFIG)
  update(CONFIG, bstack1l1ll1l1l_opy_)
  update(CONFIG, bstack1ll1l1111_opy_)
  CONFIG = bstack11ll11l1_opy_(CONFIG)
  bstack1lll1l11l_opy_ = bstack1l111lll1_opy_(CONFIG)
  bstack1lll1l1lll_opy_.bstack1l1l111ll_opy_(bstack1ll_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡢࡷࡪࡹࡳࡪࡱࡱࠫপ"), bstack1lll1l11l_opy_)
  if (bstack1ll_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧফ") in CONFIG and bstack1ll_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡒࡦࡳࡥࠨব") in bstack1ll1l1111_opy_) or (
          bstack1ll_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡓࡧ࡭ࡦࠩভ") in CONFIG and bstack1ll_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡔࡡ࡮ࡧࠪম") not in bstack1l1ll1l1l_opy_):
    if os.getenv(bstack1ll_opy_ (u"ࠨࡄࡖࡘࡆࡉࡋࡠࡅࡒࡑࡇࡏࡎࡆࡆࡢࡆ࡚ࡏࡌࡅࡡࡌࡈࠬয")):
      CONFIG[bstack1ll_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫর")] = os.getenv(bstack1ll_opy_ (u"ࠪࡆࡘ࡚ࡁࡄࡍࡢࡇࡔࡓࡂࡊࡐࡈࡈࡤࡈࡕࡊࡎࡇࡣࡎࡊࠧ঱"))
    else:
      bstack1ll1ll1ll_opy_()
  elif (bstack1ll_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧল") not in CONFIG and bstack1ll_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧ঳") in CONFIG) or (
          bstack1ll_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡓࡧ࡭ࡦࠩ঴") in bstack1l1ll1l1l_opy_ and bstack1ll_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡔࡡ࡮ࡧࠪ঵") not in bstack1ll1l1111_opy_):
    del (CONFIG[bstack1ll_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪশ")])
  if bstack1l1111l1l_opy_(CONFIG):
    bstack11l1l1l11_opy_(bstack1lllll1ll_opy_)
  bstack11l11ll1_opy_()
  bstack1l1111l11_opy_()
  if bstack1l11l11ll_opy_:
    CONFIG[bstack1ll_opy_ (u"ࠩࡤࡴࡵ࠭ষ")] = bstack1ll1l1ll1_opy_(CONFIG)
    logger.info(bstack1111l1ll1_opy_.format(CONFIG[bstack1ll_opy_ (u"ࠪࡥࡵࡶࠧস")]))
def bstack11ll1ll1l_opy_(config, bstack11l1l1ll_opy_):
  global CONFIG
  global bstack1l11l11ll_opy_
  CONFIG = config
  bstack1l11l11ll_opy_ = bstack11l1l1ll_opy_
def bstack1l1111l11_opy_():
  global CONFIG
  global bstack1l11l11ll_opy_
  if bstack1ll_opy_ (u"ࠫࡦࡶࡰࠨহ") in CONFIG:
    try:
      from appium import version
    except Exception as e:
      bstack11111l1l_opy_(e, bstack1ll1lll1l_opy_)
    bstack1l11l11ll_opy_ = True
    bstack1lll1l1lll_opy_.bstack1l1l111ll_opy_(bstack1ll_opy_ (u"ࠬࡧࡰࡱࡡࡤࡹࡹࡵ࡭ࡢࡶࡨࠫ঺"), True)
def bstack1ll1l1ll1_opy_(config):
  bstack1ll111l1_opy_ = bstack1ll_opy_ (u"࠭ࠧ঻")
  app = config[bstack1ll_opy_ (u"ࠧࡢࡲࡳ়ࠫ")]
  if isinstance(app, str):
    if os.path.splitext(app)[1] in bstack1llll11l1l_opy_:
      if os.path.exists(app):
        bstack1ll111l1_opy_ = bstack1lll111l_opy_(config, app)
      elif bstack11l1111l1_opy_(app):
        bstack1ll111l1_opy_ = app
      else:
        bstack11l1l1l11_opy_(bstack1ll11lll1l_opy_.format(app))
    else:
      if bstack11l1111l1_opy_(app):
        bstack1ll111l1_opy_ = app
      elif os.path.exists(app):
        bstack1ll111l1_opy_ = bstack1lll111l_opy_(app)
      else:
        bstack11l1l1l11_opy_(bstack1lll1ll11l_opy_)
  else:
    if len(app) > 2:
      bstack11l1l1l11_opy_(bstack1ll1lll11_opy_)
    elif len(app) == 2:
      if bstack1ll_opy_ (u"ࠨࡲࡤࡸ࡭࠭ঽ") in app and bstack1ll_opy_ (u"ࠩࡦࡹࡸࡺ࡯࡮ࡡ࡬ࡨࠬা") in app:
        if os.path.exists(app[bstack1ll_opy_ (u"ࠪࡴࡦࡺࡨࠨি")]):
          bstack1ll111l1_opy_ = bstack1lll111l_opy_(config, app[bstack1ll_opy_ (u"ࠫࡵࡧࡴࡩࠩী")], app[bstack1ll_opy_ (u"ࠬࡩࡵࡴࡶࡲࡱࡤ࡯ࡤࠨু")])
        else:
          bstack11l1l1l11_opy_(bstack1ll11lll1l_opy_.format(app))
      else:
        bstack11l1l1l11_opy_(bstack1ll1lll11_opy_)
    else:
      for key in app:
        if key in bstack111l111l_opy_:
          if key == bstack1ll_opy_ (u"࠭ࡰࡢࡶ࡫ࠫূ"):
            if os.path.exists(app[key]):
              bstack1ll111l1_opy_ = bstack1lll111l_opy_(config, app[key])
            else:
              bstack11l1l1l11_opy_(bstack1ll11lll1l_opy_.format(app))
          else:
            bstack1ll111l1_opy_ = app[key]
        else:
          bstack11l1l1l11_opy_(bstack1lll111l11_opy_)
  return bstack1ll111l1_opy_
def bstack11l1111l1_opy_(bstack1ll111l1_opy_):
  import re
  bstack11lll11l1_opy_ = re.compile(bstack1ll_opy_ (u"ࡲࠣࡠ࡞ࡥ࠲ࢀࡁ࠮࡜࠳࠱࠾ࡢ࡟࠯࡞࠰ࡡ࠯ࠪࠢৃ"))
  bstack1ll1l11111_opy_ = re.compile(bstack1ll_opy_ (u"ࡳࠤࡡ࡟ࡦ࠳ࡺࡂ࠯࡝࠴࠲࠿࡜ࡠ࠰࡟࠱ࡢ࠰࠯࡜ࡣ࠰ࡾࡆ࠳࡚࠱࠯࠼ࡠࡤ࠴࡜࠮࡟࠭ࠨࠧৄ"))
  if bstack1ll_opy_ (u"ࠩࡥࡷ࠿࠵࠯ࠨ৅") in bstack1ll111l1_opy_ or re.fullmatch(bstack11lll11l1_opy_, bstack1ll111l1_opy_) or re.fullmatch(bstack1ll1l11111_opy_, bstack1ll111l1_opy_):
    return True
  else:
    return False
def bstack1lll111l_opy_(config, path, bstack1l1l1lll1_opy_=None):
  import requests
  from requests_toolbelt.multipart.encoder import MultipartEncoder
  import hashlib
  md5_hash = hashlib.md5(open(os.path.abspath(path), bstack1ll_opy_ (u"ࠪࡶࡧ࠭৆")).read()).hexdigest()
  bstack111llllll_opy_ = bstack1111111l1_opy_(md5_hash)
  bstack1ll111l1_opy_ = None
  if bstack111llllll_opy_:
    logger.info(bstack11l11l1l1_opy_.format(bstack111llllll_opy_, md5_hash))
    return bstack111llllll_opy_
  bstack1lllll11l1_opy_ = MultipartEncoder(
    fields={
      bstack1ll_opy_ (u"ࠫ࡫࡯࡬ࡦࠩে"): (os.path.basename(path), open(os.path.abspath(path), bstack1ll_opy_ (u"ࠬࡸࡢࠨৈ")), bstack1ll_opy_ (u"࠭ࡴࡦࡺࡷ࠳ࡵࡲࡡࡪࡰࠪ৉")),
      bstack1ll_opy_ (u"ࠧࡤࡷࡶࡸࡴࡳ࡟ࡪࡦࠪ৊"): bstack1l1l1lll1_opy_
    }
  )
  response = requests.post(bstack1ll1ll1lll_opy_, data=bstack1lllll11l1_opy_,
                           headers={bstack1ll_opy_ (u"ࠨࡅࡲࡲࡹ࡫࡮ࡵ࠯ࡗࡽࡵ࡫ࠧো"): bstack1lllll11l1_opy_.content_type},
                           auth=(config[bstack1ll_opy_ (u"ࠩࡸࡷࡪࡸࡎࡢ࡯ࡨࠫৌ")], config[bstack1ll_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵࡎࡩࡾ্࠭")]))
  try:
    res = json.loads(response.text)
    bstack1ll111l1_opy_ = res[bstack1ll_opy_ (u"ࠫࡦࡶࡰࡠࡷࡵࡰࠬৎ")]
    logger.info(bstack1ll11ll1l1_opy_.format(bstack1ll111l1_opy_))
    bstack1lll1l1ll_opy_(md5_hash, bstack1ll111l1_opy_)
  except ValueError as err:
    bstack11l1l1l11_opy_(bstack111l111ll_opy_.format(str(err)))
  return bstack1ll111l1_opy_
def bstack11l11ll1_opy_():
  global CONFIG
  global bstack11lllll1l_opy_
  bstack11l1l1lll_opy_ = 0
  bstack111lll1l1_opy_ = 1
  if bstack1ll_opy_ (u"ࠬࡶࡡࡳࡣ࡯ࡰࡪࡲࡳࡑࡧࡵࡔࡱࡧࡴࡧࡱࡵࡱࠬ৏") in CONFIG:
    bstack111lll1l1_opy_ = CONFIG[bstack1ll_opy_ (u"࠭ࡰࡢࡴࡤࡰࡱ࡫࡬ࡴࡒࡨࡶࡕࡲࡡࡵࡨࡲࡶࡲ࠭৐")]
  if bstack1ll_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪ৑") in CONFIG:
    bstack11l1l1lll_opy_ = len(CONFIG[bstack1ll_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ৒")])
  bstack11lllll1l_opy_ = int(bstack111lll1l1_opy_) * int(bstack11l1l1lll_opy_)
def bstack1111111l1_opy_(md5_hash):
  bstack1llll111l_opy_ = os.path.join(os.path.expanduser(bstack1ll_opy_ (u"ࠩࢁࠫ৓")), bstack1ll_opy_ (u"ࠪ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠪ৔"), bstack1ll_opy_ (u"ࠫࡦࡶࡰࡖࡲ࡯ࡳࡦࡪࡍࡅ࠷ࡋࡥࡸ࡮࠮࡫ࡵࡲࡲࠬ৕"))
  if os.path.exists(bstack1llll111l_opy_):
    bstack111l11ll_opy_ = json.load(open(bstack1llll111l_opy_, bstack1ll_opy_ (u"ࠬࡸࡢࠨ৖")))
    if md5_hash in bstack111l11ll_opy_:
      bstack1l1l11111_opy_ = bstack111l11ll_opy_[md5_hash]
      bstack1ll111l11_opy_ = datetime.datetime.now()
      bstack1l1lll1ll_opy_ = datetime.datetime.strptime(bstack1l1l11111_opy_[bstack1ll_opy_ (u"࠭ࡴࡪ࡯ࡨࡷࡹࡧ࡭ࡱࠩৗ")], bstack1ll_opy_ (u"ࠧࠦࡦ࠲ࠩࡲ࠵࡚ࠥࠢࠨࡌ࠿ࠫࡍ࠻ࠧࡖࠫ৘"))
      if (bstack1ll111l11_opy_ - bstack1l1lll1ll_opy_).days > 30:
        return None
      elif version.parse(str(__version__)) > version.parse(bstack1l1l11111_opy_[bstack1ll_opy_ (u"ࠨࡵࡧ࡯ࡤࡼࡥࡳࡵ࡬ࡳࡳ࠭৙")]):
        return None
      return bstack1l1l11111_opy_[bstack1ll_opy_ (u"ࠩ࡬ࡨࠬ৚")]
  else:
    return None
def bstack1lll1l1ll_opy_(md5_hash, bstack1ll111l1_opy_):
  bstack1l11ll1ll_opy_ = os.path.join(os.path.expanduser(bstack1ll_opy_ (u"ࠪࢂࠬ৛")), bstack1ll_opy_ (u"ࠫ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠫড়"))
  if not os.path.exists(bstack1l11ll1ll_opy_):
    os.makedirs(bstack1l11ll1ll_opy_)
  bstack1llll111l_opy_ = os.path.join(os.path.expanduser(bstack1ll_opy_ (u"ࠬࢄࠧঢ়")), bstack1ll_opy_ (u"࠭࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠭৞"), bstack1ll_opy_ (u"ࠧࡢࡲࡳ࡙ࡵࡲ࡯ࡢࡦࡐࡈ࠺ࡎࡡࡴࡪ࠱࡮ࡸࡵ࡮ࠨয়"))
  bstack11l1111ll_opy_ = {
    bstack1ll_opy_ (u"ࠨ࡫ࡧࠫৠ"): bstack1ll111l1_opy_,
    bstack1ll_opy_ (u"ࠩࡷ࡭ࡲ࡫ࡳࡵࡣࡰࡴࠬৡ"): datetime.datetime.strftime(datetime.datetime.now(), bstack1ll_opy_ (u"ࠪࠩࡩ࠵ࠥ࡮࠱ࠨ࡝ࠥࠫࡈ࠻ࠧࡐ࠾࡙ࠪࠧৢ")),
    bstack1ll_opy_ (u"ࠫࡸࡪ࡫ࡠࡸࡨࡶࡸ࡯࡯࡯ࠩৣ"): str(__version__)
  }
  if os.path.exists(bstack1llll111l_opy_):
    bstack111l11ll_opy_ = json.load(open(bstack1llll111l_opy_, bstack1ll_opy_ (u"ࠬࡸࡢࠨ৤")))
  else:
    bstack111l11ll_opy_ = {}
  bstack111l11ll_opy_[md5_hash] = bstack11l1111ll_opy_
  with open(bstack1llll111l_opy_, bstack1ll_opy_ (u"ࠨࡷࠬࠤ৥")) as outfile:
    json.dump(bstack111l11ll_opy_, outfile)
def bstack1lll1l11l1_opy_(self):
  return
def bstack1ll11lll11_opy_(self):
  return
def bstack11ll11111_opy_(self):
  from selenium.webdriver.remote.webdriver import WebDriver
  WebDriver.quit(self)
def bstack1lll1lll1_opy_(self):
  global bstack1lll11l11l_opy_
  global bstack1ll11l1ll_opy_
  global bstack111ll1ll_opy_
  try:
    if bstack1ll_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺࠧ০") in bstack1lll11l11l_opy_ and self.session_id != None and bstack1llll11l_opy_(threading.current_thread(), bstack1ll_opy_ (u"ࠨࡶࡨࡷࡹ࡙ࡴࡢࡶࡸࡷࠬ১"), bstack1ll_opy_ (u"ࠩࠪ২")) != bstack1ll_opy_ (u"ࠪࡷࡰ࡯ࡰࡱࡧࡧࠫ৩"):
      bstack1ll1l1lll_opy_ = bstack1ll_opy_ (u"ࠫࡵࡧࡳࡴࡧࡧࠫ৪") if len(threading.current_thread().bstackTestErrorMessages) == 0 else bstack1ll_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬ৫")
      bstack11ll11l1l_opy_ = bstack11ll1111_opy_(bstack1ll_opy_ (u"࠭ࡳࡦࡶࡖࡩࡸࡹࡩࡰࡰࡖࡸࡦࡺࡵࡴࠩ৬"), bstack1ll_opy_ (u"ࠧࠨ৭"), bstack1ll1l1lll_opy_, bstack1ll_opy_ (u"ࠨ࠮ࠣࠫ৮").join(
        threading.current_thread().bstackTestErrorMessages), bstack1ll_opy_ (u"ࠩࠪ৯"), bstack1ll_opy_ (u"ࠪࠫৰ"))
      if bstack1ll1l1lll_opy_ == bstack1ll_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫৱ"):
        bstack1ll11ll11_opy_(logger)
      if self != None:
        self.execute_script(bstack11ll11l1l_opy_)
  except Exception as e:
    logger.debug(bstack1ll_opy_ (u"ࠧࡋࡲࡳࡱࡵࠤࡼ࡮ࡩ࡭ࡧࠣࡱࡦࡸ࡫ࡪࡰࡪࠤࡸࡺࡡࡵࡷࡶ࠾ࠥࠨ৲") + str(e))
  bstack111ll1ll_opy_(self)
  self.session_id = None
def bstack11111ll1_opy_(self, *args, **kwargs):
  bstack1lll1111ll_opy_ = bstack11ll11ll1_opy_(self, *args, **kwargs)
  bstack11l1l1l1_opy_.bstack1l11ll111_opy_(self)
  return bstack1lll1111ll_opy_
def bstack1lllll11l_opy_(self, command_executor,
             desired_capabilities=None, browser_profile=None, proxy=None,
             keep_alive=True, file_detector=None, options=None):
  global CONFIG
  global bstack1ll11l1ll_opy_
  global bstack1l1lllll1_opy_
  global bstack1lll1l111l_opy_
  global bstack111111ll_opy_
  global bstack1lllllll11_opy_
  global bstack1lll11l11l_opy_
  global bstack11ll11ll1_opy_
  global bstack11l1l1l1l_opy_
  global bstack11llll1l_opy_
  CONFIG[bstack1ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡘࡊࡋࠨ৳")] = str(bstack1lll11l11l_opy_) + str(__version__)
  command_executor = bstack1l1l1ll11_opy_()
  logger.debug(bstack1ll1l111_opy_.format(command_executor))
  proxy = bstack1ll11111l_opy_(CONFIG, proxy)
  bstack1l1l1l1l_opy_ = 0 if bstack1l1lllll1_opy_ < 0 else bstack1l1lllll1_opy_
  try:
    if bstack111111ll_opy_ is True:
      bstack1l1l1l1l_opy_ = int(multiprocessing.current_process().name)
    elif bstack1lllllll11_opy_ is True:
      bstack1l1l1l1l_opy_ = int(threading.current_thread().name)
  except:
    bstack1l1l1l1l_opy_ = 0
  bstack1l1l1111_opy_ = bstack111l11lll_opy_(CONFIG, bstack1l1l1l1l_opy_)
  logger.debug(bstack11ll1l11_opy_.format(str(bstack1l1l1111_opy_)))
  if bstack1ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࠫ৴") in CONFIG and CONFIG[bstack1ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡌࡰࡥࡤࡰࠬ৵")]:
    bstack1ll1llll11_opy_(bstack1l1l1111_opy_)
  if desired_capabilities:
    bstack11l1l1ll1_opy_ = bstack1lll11lll1_opy_(desired_capabilities)
    bstack11l1l1ll1_opy_[bstack1ll_opy_ (u"ࠩࡸࡷࡪ࡝࠳ࡄࠩ৶")] = bstack111lll111_opy_(CONFIG)
    bstack1111111ll_opy_ = bstack111l11lll_opy_(bstack11l1l1ll1_opy_)
    if bstack1111111ll_opy_:
      bstack1l1l1111_opy_ = update(bstack1111111ll_opy_, bstack1l1l1111_opy_)
    desired_capabilities = None
  if options:
    bstack11l111l11_opy_(options, bstack1l1l1111_opy_)
  if not options:
    options = bstack1111l1l11_opy_(bstack1l1l1111_opy_)
  if bstack1lll1ll1_opy_.bstack11l11lll1_opy_(CONFIG, bstack1l1l1l1l_opy_) and bstack1lll1ll1_opy_.bstack111l11l11_opy_(bstack1l1l1111_opy_, options):
    bstack1lll1ll1_opy_.set_capabilities(bstack1l1l1111_opy_, CONFIG)
  if proxy and bstack1l1lllllll_opy_() >= version.parse(bstack1ll_opy_ (u"ࠪ࠸࠳࠷࠰࠯࠲ࠪ৷")):
    options.proxy(proxy)
  if options and bstack1l1lllllll_opy_() >= version.parse(bstack1ll_opy_ (u"ࠫ࠸࠴࠸࠯࠲ࠪ৸")):
    desired_capabilities = None
  if (
          not options and not desired_capabilities
  ) or (
          bstack1l1lllllll_opy_() < version.parse(bstack1ll_opy_ (u"ࠬ࠹࠮࠹࠰࠳ࠫ৹")) and not desired_capabilities
  ):
    desired_capabilities = {}
    desired_capabilities.update(bstack1l1l1111_opy_)
  logger.info(bstack1lll1l1l_opy_)
  if bstack1l1lllllll_opy_() >= version.parse(bstack1ll_opy_ (u"࠭࠴࠯࠳࠳࠲࠵࠭৺")):
    bstack11ll11ll1_opy_(self, command_executor=command_executor,
              options=options, keep_alive=keep_alive, file_detector=file_detector)
  elif bstack1l1lllllll_opy_() >= version.parse(bstack1ll_opy_ (u"ࠧ࠴࠰࠻࠲࠵࠭৻")):
    bstack11ll11ll1_opy_(self, command_executor=command_executor,
              desired_capabilities=desired_capabilities, options=options,
              browser_profile=browser_profile, proxy=proxy,
              keep_alive=keep_alive, file_detector=file_detector)
  elif bstack1l1lllllll_opy_() >= version.parse(bstack1ll_opy_ (u"ࠨ࠴࠱࠹࠸࠴࠰ࠨৼ")):
    bstack11ll11ll1_opy_(self, command_executor=command_executor,
              desired_capabilities=desired_capabilities,
              browser_profile=browser_profile, proxy=proxy,
              keep_alive=keep_alive, file_detector=file_detector)
  else:
    bstack11ll11ll1_opy_(self, command_executor=command_executor,
              desired_capabilities=desired_capabilities,
              browser_profile=browser_profile, proxy=proxy,
              keep_alive=keep_alive)
  try:
    bstack111l111l1_opy_ = bstack1ll_opy_ (u"ࠩࠪ৽")
    if bstack1l1lllllll_opy_() >= version.parse(bstack1ll_opy_ (u"ࠪ࠸࠳࠶࠮࠱ࡤ࠴ࠫ৾")):
      bstack111l111l1_opy_ = self.caps.get(bstack1ll_opy_ (u"ࠦࡴࡶࡴࡪ࡯ࡤࡰࡍࡻࡢࡖࡴ࡯ࠦ৿"))
    else:
      bstack111l111l1_opy_ = self.capabilities.get(bstack1ll_opy_ (u"ࠧࡵࡰࡵ࡫ࡰࡥࡱࡎࡵࡣࡗࡵࡰࠧ਀"))
    if bstack111l111l1_opy_:
      bstack1lll11l1_opy_(bstack111l111l1_opy_)
      if bstack1l1lllllll_opy_() <= version.parse(bstack1ll_opy_ (u"࠭࠳࠯࠳࠶࠲࠵࠭ਁ")):
        self.command_executor._url = bstack1ll_opy_ (u"ࠢࡩࡶࡷࡴ࠿࠵࠯ࠣਂ") + bstack1l111l111_opy_ + bstack1ll_opy_ (u"ࠣ࠼࠻࠴࠴ࡽࡤ࠰ࡪࡸࡦࠧਃ")
      else:
        self.command_executor._url = bstack1ll_opy_ (u"ࠤ࡫ࡸࡹࡶࡳ࠻࠱࠲ࠦ਄") + bstack111l111l1_opy_ + bstack1ll_opy_ (u"ࠥ࠳ࡼࡪ࠯ࡩࡷࡥࠦਅ")
      logger.debug(bstack1l11l111l_opy_.format(bstack111l111l1_opy_))
    else:
      logger.debug(bstack1111ll111_opy_.format(bstack1ll_opy_ (u"ࠦࡔࡶࡴࡪ࡯ࡤࡰࠥࡎࡵࡣࠢࡱࡳࡹࠦࡦࡰࡷࡱࡨࠧਆ")))
  except Exception as e:
    logger.debug(bstack1111ll111_opy_.format(e))
  if bstack1ll_opy_ (u"ࠬࡸ࡯ࡣࡱࡷࠫਇ") in bstack1lll11l11l_opy_:
    bstack1lll1ll1ll_opy_(bstack1l1lllll1_opy_, bstack11llll1l_opy_)
  bstack1ll11l1ll_opy_ = self.session_id
  if bstack1ll_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭ਈ") in bstack1lll11l11l_opy_ or bstack1ll_opy_ (u"ࠧࡣࡧ࡫ࡥࡻ࡫ࠧਉ") in bstack1lll11l11l_opy_:
    threading.current_thread().bstack111ll11l1_opy_ = self.session_id
    threading.current_thread().bstackSessionDriver = self
    threading.current_thread().bstackTestErrorMessages = []
    bstack11l1l1l1_opy_.bstack1l11ll111_opy_(self)
  bstack11l1l1l1l_opy_.append(self)
  if bstack1ll_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫਊ") in CONFIG and bstack1ll_opy_ (u"ࠩࡶࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠧ਋") in CONFIG[bstack1ll_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭਌")][bstack1l1l1l1l_opy_]:
    bstack1lll1l111l_opy_ = CONFIG[bstack1ll_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧ਍")][bstack1l1l1l1l_opy_][bstack1ll_opy_ (u"ࠬࡹࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠪ਎")]
  logger.debug(bstack1llll11ll1_opy_.format(bstack1ll11l1ll_opy_))
try:
  try:
    import Browser
    from subprocess import Popen
    def bstack1111lll1_opy_(self, args, bufsize=-1, executable=None,
              stdin=None, stdout=None, stderr=None,
              preexec_fn=None, close_fds=True,
              shell=False, cwd=None, env=None, universal_newlines=None,
              startupinfo=None, creationflags=0,
              restore_signals=True, start_new_session=False,
              pass_fds=(), *, user=None, group=None, extra_groups=None,
              encoding=None, errors=None, text=None, umask=-1, pipesize=-1):
      global CONFIG
      global bstack11lll1lll_opy_
      if(bstack1ll_opy_ (u"ࠨࡩ࡯ࡦࡨࡼ࠳ࡰࡳࠣਏ") in args[1]):
        with open(os.path.join(os.path.expanduser(bstack1ll_opy_ (u"ࠧࡿࠩਐ")), bstack1ll_opy_ (u"ࠨ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠨ਑"), bstack1ll_opy_ (u"ࠩ࠱ࡷࡪࡹࡳࡪࡱࡱ࡭ࡩࡹ࠮ࡵࡺࡷࠫ਒")), bstack1ll_opy_ (u"ࠪࡻࠬਓ")) as fp:
          fp.write(bstack1ll_opy_ (u"ࠦࠧਔ"))
        if(not os.path.exists(os.path.join(os.path.dirname(args[1]), bstack1ll_opy_ (u"ࠧ࡯࡮ࡥࡧࡻࡣࡧࡹࡴࡢࡥ࡮࠲࡯ࡹࠢਕ")))):
          with open(args[1], bstack1ll_opy_ (u"࠭ࡲࠨਖ")) as f:
            lines = f.readlines()
            index = next((i for i, line in enumerate(lines) if bstack1ll_opy_ (u"ࠧࡢࡵࡼࡲࡨࠦࡦࡶࡰࡦࡸ࡮ࡵ࡮ࠡࡡࡱࡩࡼࡖࡡࡨࡧࠫࡧࡴࡴࡴࡦࡺࡷ࠰ࠥࡶࡡࡨࡧࠣࡁࠥࡼ࡯ࡪࡦࠣ࠴࠮࠭ਗ") in line), None)
            if index is not None:
                lines.insert(index+2, bstack1llll1l1_opy_)
            lines.insert(1, bstack1llll1ll1l_opy_)
            f.seek(0)
            with open(os.path.join(os.path.dirname(args[1]), bstack1ll_opy_ (u"ࠣ࡫ࡱࡨࡪࡾ࡟ࡣࡵࡷࡥࡨࡱ࠮࡫ࡵࠥਘ")), bstack1ll_opy_ (u"ࠩࡺࠫਙ")) as bstack111l1lll1_opy_:
              bstack111l1lll1_opy_.writelines(lines)
        CONFIG[bstack1ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡕࡇࡏࠬਚ")] = str(bstack1lll11l11l_opy_) + str(__version__)
        bstack1l1l1l1l_opy_ = 0 if bstack1l1lllll1_opy_ < 0 else bstack1l1lllll1_opy_
        try:
          if bstack111111ll_opy_ is True:
            bstack1l1l1l1l_opy_ = int(multiprocessing.current_process().name)
          elif bstack1lllllll11_opy_ is True:
            bstack1l1l1l1l_opy_ = int(threading.current_thread().name)
        except:
          bstack1l1l1l1l_opy_ = 0
        CONFIG[bstack1ll_opy_ (u"ࠦࡺࡹࡥࡘ࠵ࡆࠦਛ")] = False
        CONFIG[bstack1ll_opy_ (u"ࠧ࡯ࡳࡑ࡮ࡤࡽࡼࡸࡩࡨࡪࡷࠦਜ")] = True
        bstack1l1l1111_opy_ = bstack111l11lll_opy_(CONFIG, bstack1l1l1l1l_opy_)
        logger.debug(bstack11ll1l11_opy_.format(str(bstack1l1l1111_opy_)))
        if CONFIG.get(bstack1ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࠪਝ")):
          bstack1ll1llll11_opy_(bstack1l1l1111_opy_)
        if bstack1ll_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪਞ") in CONFIG and bstack1ll_opy_ (u"ࠨࡵࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪ࠭ਟ") in CONFIG[bstack1ll_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬਠ")][bstack1l1l1l1l_opy_]:
          bstack1lll1l111l_opy_ = CONFIG[bstack1ll_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ਡ")][bstack1l1l1l1l_opy_][bstack1ll_opy_ (u"ࠫࡸ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠩਢ")]
        args.append(os.path.join(os.path.expanduser(bstack1ll_opy_ (u"ࠬࢄࠧਣ")), bstack1ll_opy_ (u"࠭࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠭ਤ"), bstack1ll_opy_ (u"ࠧ࠯ࡵࡨࡷࡸ࡯࡯࡯࡫ࡧࡷ࠳ࡺࡸࡵࠩਥ")))
        args.append(str(threading.get_ident()))
        args.append(json.dumps(bstack1l1l1111_opy_))
        args[1] = os.path.join(os.path.dirname(args[1]), bstack1ll_opy_ (u"ࠣ࡫ࡱࡨࡪࡾ࡟ࡣࡵࡷࡥࡨࡱ࠮࡫ࡵࠥਦ"))
      bstack11lll1lll_opy_ = True
      return bstack1ll11ll1ll_opy_(self, args, bufsize=bufsize, executable=executable,
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
  def bstack1l11llll_opy_(self,
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
    global bstack1l1lllll1_opy_
    global bstack1lll1l111l_opy_
    global bstack111111ll_opy_
    global bstack1lllllll11_opy_
    global bstack1lll11l11l_opy_
    CONFIG[bstack1ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡔࡆࡎࠫਧ")] = str(bstack1lll11l11l_opy_) + str(__version__)
    bstack1l1l1l1l_opy_ = 0 if bstack1l1lllll1_opy_ < 0 else bstack1l1lllll1_opy_
    try:
      if bstack111111ll_opy_ is True:
        bstack1l1l1l1l_opy_ = int(multiprocessing.current_process().name)
      elif bstack1lllllll11_opy_ is True:
        bstack1l1l1l1l_opy_ = int(threading.current_thread().name)
    except:
      bstack1l1l1l1l_opy_ = 0
    CONFIG[bstack1ll_opy_ (u"ࠥ࡭ࡸࡖ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠤਨ")] = True
    bstack1l1l1111_opy_ = bstack111l11lll_opy_(CONFIG, bstack1l1l1l1l_opy_)
    logger.debug(bstack11ll1l11_opy_.format(str(bstack1l1l1111_opy_)))
    if CONFIG.get(bstack1ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࠨ਩")):
      bstack1ll1llll11_opy_(bstack1l1l1111_opy_)
    if bstack1ll_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨਪ") in CONFIG and bstack1ll_opy_ (u"࠭ࡳࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠫਫ") in CONFIG[bstack1ll_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪਬ")][bstack1l1l1l1l_opy_]:
      bstack1lll1l111l_opy_ = CONFIG[bstack1ll_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫਭ")][bstack1l1l1l1l_opy_][bstack1ll_opy_ (u"ࠩࡶࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠧਮ")]
    import urllib
    import json
    bstack1ll11ll1_opy_ = bstack1ll_opy_ (u"ࠪࡻࡸࡹ࠺࠰࠱ࡦࡨࡵ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡩ࡯࡮࠱ࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹࡅࡣࡢࡲࡶࡁࠬਯ") + urllib.parse.quote(json.dumps(bstack1l1l1111_opy_))
    browser = self.connect(bstack1ll11ll1_opy_)
    return browser
except Exception as e:
    pass
def bstack1lllll111l_opy_():
    global bstack11lll1lll_opy_
    try:
        from playwright._impl._browser_type import BrowserType
        BrowserType.launch = bstack1l11llll_opy_
        bstack11lll1lll_opy_ = True
    except Exception as e:
        pass
    try:
      import Browser
      from subprocess import Popen
      Popen.__init__ = bstack1111lll1_opy_
      bstack11lll1lll_opy_ = True
    except Exception as e:
      pass
def bstack1ll1l11ll1_opy_(context, bstack1llll1lll_opy_):
  try:
    context.page.evaluate(bstack1ll_opy_ (u"ࠦࡤࠦ࠽࠿ࠢࡾࢁࠧਰ"), bstack1ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࡼࠤࡤࡧࡹ࡯࡯࡯ࠤ࠽ࠤࠧࡹࡥࡵࡕࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪࠨࠬࠡࠤࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠧࡀࠠࡼࠤࡱࡥࡲ࡫ࠢ࠻ࠩ਱")+ json.dumps(bstack1llll1lll_opy_) + bstack1ll_opy_ (u"ࠨࡽࡾࠤਲ"))
  except Exception as e:
    logger.debug(bstack1ll_opy_ (u"ࠢࡦࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࠣࡷࡪࡹࡳࡪࡱࡱࠤࡳࡧ࡭ࡦࠢࡾࢁࠧਲ਼"), e)
def bstack1lll11l111_opy_(context, message, level):
  try:
    context.page.evaluate(bstack1ll_opy_ (u"ࠣࡡࠣࡁࡃࠦࡻࡾࠤ਴"), bstack1ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࠨࡡࡤࡶ࡬ࡳࡳࠨ࠺ࠡࠤࡤࡲࡳࡵࡴࡢࡶࡨࠦ࠱ࠦࠢࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠥ࠾ࠥࢁࠢࡥࡣࡷࡥࠧࡀࠧਵ") + json.dumps(message) + bstack1ll_opy_ (u"ࠪ࠰ࠧࡲࡥࡷࡧ࡯ࠦ࠿࠭ਸ਼") + json.dumps(level) + bstack1ll_opy_ (u"ࠫࢂࢃࠧ਷"))
  except Exception as e:
    logger.debug(bstack1ll_opy_ (u"ࠧ࡫ࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࠡࡣࡱࡲࡴࡺࡡࡵ࡫ࡲࡲࠥࢁࡽࠣਸ"), e)
def bstack11lll111_opy_(context, status, message = bstack1ll_opy_ (u"ࠨࠢਹ")):
  try:
    if(status == bstack1ll_opy_ (u"ࠢࡧࡣ࡬ࡰࡪࡪࠢ਺")):
      context.page.evaluate(bstack1ll_opy_ (u"ࠣࡡࠣࡁࡃࠦࡻࡾࠤ਻"), bstack1ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࠨࡡࡤࡶ࡬ࡳࡳࠨ࠺ࠡࠤࡶࡩࡹ࡙ࡥࡴࡵ࡬ࡳࡳ࡙ࡴࡢࡶࡸࡷࠧ࠲ࠠࠣࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠦ࠿ࠦࡻࠣࡴࡨࡥࡸࡵ࡮ࠣ࠼਼ࠪ") + json.dumps(bstack1ll_opy_ (u"ࠥࡗࡨ࡫࡮ࡢࡴ࡬ࡳࠥ࡬ࡡࡪ࡮ࡨࡨࠥࡽࡩࡵࡪ࠽ࠤࠧ਽") + str(message)) + bstack1ll_opy_ (u"ࠫ࠱ࠨࡳࡵࡣࡷࡹࡸࠨ࠺ࠨਾ") + json.dumps(status) + bstack1ll_opy_ (u"ࠧࢃࡽࠣਿ"))
    else:
      context.page.evaluate(bstack1ll_opy_ (u"ࠨ࡟ࠡ࠿ࡁࠤࢀࢃࠢੀ"), bstack1ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࡾࠦࡦࡩࡴࡪࡱࡱࠦ࠿ࠦࠢࡴࡧࡷࡗࡪࡹࡳࡪࡱࡱࡗࡹࡧࡴࡶࡵࠥ࠰ࠥࠨࡡࡳࡩࡸࡱࡪࡴࡴࡴࠤ࠽ࠤࢀࠨࡳࡵࡣࡷࡹࡸࠨ࠺ࠨੁ") + json.dumps(status) + bstack1ll_opy_ (u"ࠣࡿࢀࠦੂ"))
  except Exception as e:
    logger.debug(bstack1ll_opy_ (u"ࠤࡨࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࠥࡹࡥࡵࠢࡶࡩࡸࡹࡩࡰࡰࠣࡷࡹࡧࡴࡶࡵࠣࡿࢂࠨ੃"), e)
def bstack111l1ll11_opy_(self, url):
  global bstack1l1111lll_opy_
  try:
    bstack1llllll1l1_opy_(url)
  except Exception as err:
    logger.debug(bstack11ll1l1l1_opy_.format(str(err)))
  try:
    bstack1l1111lll_opy_(self, url)
  except Exception as e:
    try:
      bstack11111lll_opy_ = str(e)
      if any(err_msg in bstack11111lll_opy_ for err_msg in bstack1111ll1ll_opy_):
        bstack1llllll1l1_opy_(url, True)
    except Exception as err:
      logger.debug(bstack11ll1l1l1_opy_.format(str(err)))
    raise e
def bstack1ll1l111ll_opy_(self):
  global bstack1ll1l1l11l_opy_
  bstack1ll1l1l11l_opy_ = self
  return
def bstack11l11llll_opy_(self):
  global bstack1lll1lll_opy_
  bstack1lll1lll_opy_ = self
  return
def bstack1l11lll11_opy_(self, test):
  global CONFIG
  global bstack1lll1lll_opy_
  global bstack1ll1l1l11l_opy_
  global bstack1ll11l1ll_opy_
  global bstack111111l1l_opy_
  global bstack1lll1l111l_opy_
  global bstack1l111111_opy_
  global bstack1ll1l1llll_opy_
  global bstack1ll1l1l1_opy_
  global bstack11l1l1l1l_opy_
  try:
    if not bstack1ll11l1ll_opy_:
      with open(os.path.join(os.path.expanduser(bstack1ll_opy_ (u"ࠪࢂࠬ੄")), bstack1ll_opy_ (u"ࠫ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠫ੅"), bstack1ll_opy_ (u"ࠬ࠴ࡳࡦࡵࡶ࡭ࡴࡴࡩࡥࡵ࠱ࡸࡽࡺࠧ੆"))) as f:
        bstack11l11111_opy_ = json.loads(bstack1ll_opy_ (u"ࠨࡻࠣੇ") + f.read().strip() + bstack1ll_opy_ (u"ࠧࠣࡺࠥ࠾ࠥࠨࡹࠣࠩੈ") + bstack1ll_opy_ (u"ࠣࡿࠥ੉"))
        bstack1ll11l1ll_opy_ = bstack11l11111_opy_[str(threading.get_ident())]
  except:
    pass
  if bstack11l1l1l1l_opy_:
    for driver in bstack11l1l1l1l_opy_:
      if bstack1ll11l1ll_opy_ == driver.session_id:
        if test:
          bstack1lll11ll1_opy_ = str(test.data)
        if not bstack1llll1l111_opy_ and bstack1lll11ll1_opy_:
          bstack1llll1l1l_opy_ = {
            bstack1ll_opy_ (u"ࠩࡤࡧࡹ࡯࡯࡯ࠩ੊"): bstack1ll_opy_ (u"ࠪࡷࡪࡺࡓࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠫੋ"),
            bstack1ll_opy_ (u"ࠫࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠧੌ"): {
              bstack1ll_opy_ (u"ࠬࡴࡡ࡮ࡧ੍ࠪ"): bstack1lll11ll1_opy_
            }
          }
          bstack11l1ll11l_opy_ = bstack1ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࢀࠫ੎").format(json.dumps(bstack1llll1l1l_opy_))
          driver.execute_script(bstack11l1ll11l_opy_)
        if bstack111111l1l_opy_:
          bstack1llllll11l_opy_ = {
            bstack1ll_opy_ (u"ࠧࡢࡥࡷ࡭ࡴࡴࠧ੏"): bstack1ll_opy_ (u"ࠨࡣࡱࡲࡴࡺࡡࡵࡧࠪ੐"),
            bstack1ll_opy_ (u"ࠩࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠬੑ"): {
              bstack1ll_opy_ (u"ࠪࡨࡦࡺࡡࠨ੒"): bstack1lll11ll1_opy_ + bstack1ll_opy_ (u"ࠫࠥࡶࡡࡴࡵࡨࡨࠦ࠭੓"),
              bstack1ll_opy_ (u"ࠬࡲࡥࡷࡧ࡯ࠫ੔"): bstack1ll_opy_ (u"࠭ࡩ࡯ࡨࡲࠫ੕")
            }
          }
          bstack1llll1l1l_opy_ = {
            bstack1ll_opy_ (u"ࠧࡢࡥࡷ࡭ࡴࡴࠧ੖"): bstack1ll_opy_ (u"ࠨࡵࡨࡸࡘ࡫ࡳࡴ࡫ࡲࡲࡘࡺࡡࡵࡷࡶࠫ੗"),
            bstack1ll_opy_ (u"ࠩࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠬ੘"): {
              bstack1ll_opy_ (u"ࠪࡷࡹࡧࡴࡶࡵࠪਖ਼"): bstack1ll_opy_ (u"ࠫࡵࡧࡳࡴࡧࡧࠫਗ਼")
            }
          }
          if bstack111111l1l_opy_.status == bstack1ll_opy_ (u"ࠬࡖࡁࡔࡕࠪਜ਼"):
            bstack1111111l_opy_ = bstack1ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࢀࠫੜ").format(json.dumps(bstack1llllll11l_opy_))
            driver.execute_script(bstack1111111l_opy_)
            bstack11l1ll11l_opy_ = bstack1ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࡾࢁࠬ੝").format(json.dumps(bstack1llll1l1l_opy_))
            driver.execute_script(bstack11l1ll11l_opy_)
          elif bstack111111l1l_opy_.status == bstack1ll_opy_ (u"ࠨࡈࡄࡍࡑ࠭ਫ਼"):
            reason = bstack1ll_opy_ (u"ࠤࠥ੟")
            bstack1lll11l11_opy_ = bstack1lll11ll1_opy_ + bstack1ll_opy_ (u"ࠪࠤ࡫ࡧࡩ࡭ࡧࡧࠫ੠")
            if bstack111111l1l_opy_.message:
              reason = str(bstack111111l1l_opy_.message)
              bstack1lll11l11_opy_ = bstack1lll11l11_opy_ + bstack1ll_opy_ (u"ࠫࠥࡽࡩࡵࡪࠣࡩࡷࡸ࡯ࡳ࠼ࠣࠫ੡") + reason
            bstack1llllll11l_opy_[bstack1ll_opy_ (u"ࠬࡧࡲࡨࡷࡰࡩࡳࡺࡳࠨ੢")] = {
              bstack1ll_opy_ (u"࠭࡬ࡦࡸࡨࡰࠬ੣"): bstack1ll_opy_ (u"ࠧࡦࡴࡵࡳࡷ࠭੤"),
              bstack1ll_opy_ (u"ࠨࡦࡤࡸࡦ࠭੥"): bstack1lll11l11_opy_
            }
            bstack1llll1l1l_opy_[bstack1ll_opy_ (u"ࠩࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠬ੦")] = {
              bstack1ll_opy_ (u"ࠪࡷࡹࡧࡴࡶࡵࠪ੧"): bstack1ll_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫ੨"),
              bstack1ll_opy_ (u"ࠬࡸࡥࡢࡵࡲࡲࠬ੩"): reason
            }
            bstack1111111l_opy_ = bstack1ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࢀࠫ੪").format(json.dumps(bstack1llllll11l_opy_))
            driver.execute_script(bstack1111111l_opy_)
            bstack11l1ll11l_opy_ = bstack1ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࡾࢁࠬ੫").format(json.dumps(bstack1llll1l1l_opy_))
            driver.execute_script(bstack11l1ll11l_opy_)
            bstack1ll111ll1_opy_(reason, str(bstack111111l1l_opy_), str(bstack1l1lllll1_opy_), logger)
  elif bstack1ll11l1ll_opy_:
    try:
      data = {}
      bstack1lll11ll1_opy_ = None
      if test:
        bstack1lll11ll1_opy_ = str(test.data)
      if not bstack1llll1l111_opy_ and bstack1lll11ll1_opy_:
        data[bstack1ll_opy_ (u"ࠨࡰࡤࡱࡪ࠭੬")] = bstack1lll11ll1_opy_
      if bstack111111l1l_opy_:
        if bstack111111l1l_opy_.status == bstack1ll_opy_ (u"ࠩࡓࡅࡘ࡙ࠧ੭"):
          data[bstack1ll_opy_ (u"ࠪࡷࡹࡧࡴࡶࡵࠪ੮")] = bstack1ll_opy_ (u"ࠫࡵࡧࡳࡴࡧࡧࠫ੯")
        elif bstack111111l1l_opy_.status == bstack1ll_opy_ (u"ࠬࡌࡁࡊࡎࠪੰ"):
          data[bstack1ll_opy_ (u"࠭ࡳࡵࡣࡷࡹࡸ࠭ੱ")] = bstack1ll_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧੲ")
          if bstack111111l1l_opy_.message:
            data[bstack1ll_opy_ (u"ࠨࡴࡨࡥࡸࡵ࡮ࠨੳ")] = str(bstack111111l1l_opy_.message)
      user = CONFIG[bstack1ll_opy_ (u"ࠩࡸࡷࡪࡸࡎࡢ࡯ࡨࠫੴ")]
      key = CONFIG[bstack1ll_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵࡎࡩࡾ࠭ੵ")]
      url = bstack1ll_opy_ (u"ࠫ࡭ࡺࡴࡱࡵ࠽࠳࠴ࢁࡽ࠻ࡽࢀࡄࡦࡶࡩ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡤࡱࡰ࠳ࡦࡻࡴࡰ࡯ࡤࡸࡪ࠵ࡳࡦࡵࡶ࡭ࡴࡴࡳ࠰ࡽࢀ࠲࡯ࡹ࡯࡯ࠩ੶").format(user, key, bstack1ll11l1ll_opy_)
      headers = {
        bstack1ll_opy_ (u"ࠬࡉ࡯࡯ࡶࡨࡲࡹ࠳ࡴࡺࡲࡨࠫ੷"): bstack1ll_opy_ (u"࠭ࡡࡱࡲ࡯࡭ࡨࡧࡴࡪࡱࡱ࠳࡯ࡹ࡯࡯ࠩ੸"),
      }
      if bool(data):
        requests.put(url, json=data, headers=headers)
    except Exception as e:
      logger.error(bstack1ll1ll1l1_opy_.format(str(e)))
  if bstack1lll1lll_opy_:
    bstack1ll1l1llll_opy_(bstack1lll1lll_opy_)
  if bstack1ll1l1l11l_opy_:
    bstack1ll1l1l1_opy_(bstack1ll1l1l11l_opy_)
  bstack1l111111_opy_(self, test)
def bstack1111lll1l_opy_(self, parent, test, skip_on_failure=None, rpa=False):
  global bstack1lll1l1ll1_opy_
  bstack1lll1l1ll1_opy_(self, parent, test, skip_on_failure=skip_on_failure, rpa=rpa)
  global bstack111111l1l_opy_
  bstack111111l1l_opy_ = self._test
def bstack1ll111111_opy_():
  global bstack1lll11ll_opy_
  try:
    if os.path.exists(bstack1lll11ll_opy_):
      os.remove(bstack1lll11ll_opy_)
  except Exception as e:
    logger.debug(bstack1ll_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡧࡩࡱ࡫ࡴࡪࡰࡪࠤࡷࡵࡢࡰࡶࠣࡶࡪࡶ࡯ࡳࡶࠣࡪ࡮ࡲࡥ࠻ࠢࠪ੹") + str(e))
def bstack1ll11l11l_opy_():
  global bstack1lll11ll_opy_
  bstack11lllll1_opy_ = {}
  try:
    if not os.path.isfile(bstack1lll11ll_opy_):
      with open(bstack1lll11ll_opy_, bstack1ll_opy_ (u"ࠨࡹࠪ੺")):
        pass
      with open(bstack1lll11ll_opy_, bstack1ll_opy_ (u"ࠤࡺ࠯ࠧ੻")) as outfile:
        json.dump({}, outfile)
    if os.path.exists(bstack1lll11ll_opy_):
      bstack11lllll1_opy_ = json.load(open(bstack1lll11ll_opy_, bstack1ll_opy_ (u"ࠪࡶࡧ࠭੼")))
  except Exception as e:
    logger.debug(bstack1ll_opy_ (u"ࠫࡊࡸࡲࡰࡴࠣ࡭ࡳࠦࡲࡦࡣࡧ࡭ࡳ࡭ࠠࡳࡱࡥࡳࡹࠦࡲࡦࡲࡲࡶࡹࠦࡦࡪ࡮ࡨ࠾ࠥ࠭੽") + str(e))
  finally:
    return bstack11lllll1_opy_
def bstack1lll1ll1ll_opy_(platform_index, item_index):
  global bstack1lll11ll_opy_
  try:
    bstack11lllll1_opy_ = bstack1ll11l11l_opy_()
    bstack11lllll1_opy_[item_index] = platform_index
    with open(bstack1lll11ll_opy_, bstack1ll_opy_ (u"ࠧࡽࠫࠣ੾")) as outfile:
      json.dump(bstack11lllll1_opy_, outfile)
  except Exception as e:
    logger.debug(bstack1ll_opy_ (u"࠭ࡅࡳࡴࡲࡶࠥ࡯࡮ࠡࡹࡵ࡭ࡹ࡯࡮ࡨࠢࡷࡳࠥࡸ࡯ࡣࡱࡷࠤࡷ࡫ࡰࡰࡴࡷࠤ࡫࡯࡬ࡦ࠼ࠣࠫ੿") + str(e))
def bstack1l11l1l1_opy_(bstack1ll1lll1l1_opy_):
  global CONFIG
  bstack11111lll1_opy_ = bstack1ll_opy_ (u"ࠧࠨ઀")
  if not bstack1ll_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫઁ") in CONFIG:
    logger.info(bstack1ll_opy_ (u"ࠩࡑࡳࠥࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠡࡲࡤࡷࡸ࡫ࡤࠡࡷࡱࡥࡧࡲࡥࠡࡶࡲࠤ࡬࡫࡮ࡦࡴࡤࡸࡪࠦࡲࡦࡲࡲࡶࡹࠦࡦࡰࡴࠣࡖࡴࡨ࡯ࡵࠢࡵࡹࡳ࠭ં"))
  try:
    platform = CONFIG[bstack1ll_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ઃ")][bstack1ll1lll1l1_opy_]
    if bstack1ll_opy_ (u"ࠫࡴࡹࠧ઄") in platform:
      bstack11111lll1_opy_ += str(platform[bstack1ll_opy_ (u"ࠬࡵࡳࠨઅ")]) + bstack1ll_opy_ (u"࠭ࠬࠡࠩઆ")
    if bstack1ll_opy_ (u"ࠧࡰࡵ࡙ࡩࡷࡹࡩࡰࡰࠪઇ") in platform:
      bstack11111lll1_opy_ += str(platform[bstack1ll_opy_ (u"ࠨࡱࡶ࡚ࡪࡸࡳࡪࡱࡱࠫઈ")]) + bstack1ll_opy_ (u"ࠩ࠯ࠤࠬઉ")
    if bstack1ll_opy_ (u"ࠪࡨࡪࡼࡩࡤࡧࡑࡥࡲ࡫ࠧઊ") in platform:
      bstack11111lll1_opy_ += str(platform[bstack1ll_opy_ (u"ࠫࡩ࡫ࡶࡪࡥࡨࡒࡦࡳࡥࠨઋ")]) + bstack1ll_opy_ (u"ࠬ࠲ࠠࠨઌ")
    if bstack1ll_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡗࡧࡵࡷ࡮ࡵ࡮ࠨઍ") in platform:
      bstack11111lll1_opy_ += str(platform[bstack1ll_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡘࡨࡶࡸ࡯࡯࡯ࠩ઎")]) + bstack1ll_opy_ (u"ࠨ࠮ࠣࠫએ")
    if bstack1ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡑࡥࡲ࡫ࠧઐ") in platform:
      bstack11111lll1_opy_ += str(platform[bstack1ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡒࡦࡳࡥࠨઑ")]) + bstack1ll_opy_ (u"ࠫ࠱ࠦࠧ઒")
    if bstack1ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ઓ") in platform:
      bstack11111lll1_opy_ += str(platform[bstack1ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠧઔ")]) + bstack1ll_opy_ (u"ࠧ࠭ࠢࠪક")
  except Exception as e:
    logger.debug(bstack1ll_opy_ (u"ࠨࡕࡲࡱࡪࠦࡥࡳࡴࡲࡶࠥ࡯࡮ࠡࡩࡨࡲࡪࡸࡡࡵ࡫ࡱ࡫ࠥࡶ࡬ࡢࡶࡩࡳࡷࡳࠠࡴࡶࡵ࡭ࡳ࡭ࠠࡧࡱࡵࠤࡷ࡫ࡰࡰࡴࡷࠤ࡬࡫࡮ࡦࡴࡤࡸ࡮ࡵ࡮ࠨખ") + str(e))
  finally:
    if bstack11111lll1_opy_[len(bstack11111lll1_opy_) - 2:] == bstack1ll_opy_ (u"ࠩ࠯ࠤࠬગ"):
      bstack11111lll1_opy_ = bstack11111lll1_opy_[:-2]
    return bstack11111lll1_opy_
def bstack1ll11llll_opy_(path, bstack11111lll1_opy_):
  try:
    import xml.etree.ElementTree as ET
    bstack1ll1ll1l11_opy_ = ET.parse(path)
    bstack1l11111l1_opy_ = bstack1ll1ll1l11_opy_.getroot()
    bstack11l1l111_opy_ = None
    for suite in bstack1l11111l1_opy_.iter(bstack1ll_opy_ (u"ࠪࡷࡺ࡯ࡴࡦࠩઘ")):
      if bstack1ll_opy_ (u"ࠫࡸࡵࡵࡳࡥࡨࠫઙ") in suite.attrib:
        suite.attrib[bstack1ll_opy_ (u"ࠬࡴࡡ࡮ࡧࠪચ")] += bstack1ll_opy_ (u"࠭ࠠࠨછ") + bstack11111lll1_opy_
        bstack11l1l111_opy_ = suite
    bstack11ll1llll_opy_ = None
    for robot in bstack1l11111l1_opy_.iter(bstack1ll_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠭જ")):
      bstack11ll1llll_opy_ = robot
    bstack1l1l1l111_opy_ = len(bstack11ll1llll_opy_.findall(bstack1ll_opy_ (u"ࠨࡵࡸ࡭ࡹ࡫ࠧઝ")))
    if bstack1l1l1l111_opy_ == 1:
      bstack11ll1llll_opy_.remove(bstack11ll1llll_opy_.findall(bstack1ll_opy_ (u"ࠩࡶࡹ࡮ࡺࡥࠨઞ"))[0])
      bstack11lll1l1l_opy_ = ET.Element(bstack1ll_opy_ (u"ࠪࡷࡺ࡯ࡴࡦࠩટ"), attrib={bstack1ll_opy_ (u"ࠫࡳࡧ࡭ࡦࠩઠ"): bstack1ll_opy_ (u"࡙ࠬࡵࡪࡶࡨࡷࠬડ"), bstack1ll_opy_ (u"࠭ࡩࡥࠩઢ"): bstack1ll_opy_ (u"ࠧࡴ࠲ࠪણ")})
      bstack11ll1llll_opy_.insert(1, bstack11lll1l1l_opy_)
      bstack1111l1lll_opy_ = None
      for suite in bstack11ll1llll_opy_.iter(bstack1ll_opy_ (u"ࠨࡵࡸ࡭ࡹ࡫ࠧત")):
        bstack1111l1lll_opy_ = suite
      bstack1111l1lll_opy_.append(bstack11l1l111_opy_)
      bstack1llllll11_opy_ = None
      for status in bstack11l1l111_opy_.iter(bstack1ll_opy_ (u"ࠩࡶࡸࡦࡺࡵࡴࠩથ")):
        bstack1llllll11_opy_ = status
      bstack1111l1lll_opy_.append(bstack1llllll11_opy_)
    bstack1ll1ll1l11_opy_.write(path)
  except Exception as e:
    logger.debug(bstack1ll_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥࡶࡡࡳࡵ࡬ࡲ࡬ࠦࡷࡩ࡫࡯ࡩࠥ࡭ࡥ࡯ࡧࡵࡥࡹ࡯࡮ࡨࠢࡵࡳࡧࡵࡴࠡࡴࡨࡴࡴࡸࡴࠨદ") + str(e))
def bstack111l1l1ll_opy_(outs_dir, pabot_args, options, start_time_string, tests_root_name):
  global bstack1ll111l1l1_opy_
  global CONFIG
  if bstack1ll_opy_ (u"ࠦࡵࡿࡴࡩࡱࡱࡴࡦࡺࡨࠣધ") in options:
    del options[bstack1ll_opy_ (u"ࠧࡶࡹࡵࡪࡲࡲࡵࡧࡴࡩࠤન")]
  bstack11lll1ll_opy_ = bstack1ll11l11l_opy_()
  for bstack1l111111l_opy_ in bstack11lll1ll_opy_.keys():
    path = os.path.join(os.getcwd(), bstack1ll_opy_ (u"࠭ࡰࡢࡤࡲࡸࡤࡸࡥࡴࡷ࡯ࡸࡸ࠭઩"), str(bstack1l111111l_opy_), bstack1ll_opy_ (u"ࠧࡰࡷࡷࡴࡺࡺ࠮ࡹ࡯࡯ࠫપ"))
    bstack1ll11llll_opy_(path, bstack1l11l1l1_opy_(bstack11lll1ll_opy_[bstack1l111111l_opy_]))
  bstack1ll111111_opy_()
  return bstack1ll111l1l1_opy_(outs_dir, pabot_args, options, start_time_string, tests_root_name)
def bstack1ll111l1ll_opy_(self, ff_profile_dir):
  global bstack1lll111l1_opy_
  if not ff_profile_dir:
    return None
  return bstack1lll111l1_opy_(self, ff_profile_dir)
def bstack11ll11lll_opy_(datasources, opts_for_run, outs_dir, pabot_args, suite_group):
  from pabot.pabot import QueueItem
  global CONFIG
  global bstack1l1111ll_opy_
  bstack1lll1ll111_opy_ = []
  if bstack1ll_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫફ") in CONFIG:
    bstack1lll1ll111_opy_ = CONFIG[bstack1ll_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬબ")]
  return [
    QueueItem(
      datasources,
      outs_dir,
      opts_for_run,
      suite,
      pabot_args[bstack1ll_opy_ (u"ࠥࡧࡴࡳ࡭ࡢࡰࡧࠦભ")],
      pabot_args[bstack1ll_opy_ (u"ࠦࡻ࡫ࡲࡣࡱࡶࡩࠧમ")],
      argfile,
      pabot_args.get(bstack1ll_opy_ (u"ࠧ࡮ࡩࡷࡧࠥય")),
      pabot_args[bstack1ll_opy_ (u"ࠨࡰࡳࡱࡦࡩࡸࡹࡥࡴࠤર")],
      platform[0],
      bstack1l1111ll_opy_
    )
    for suite in suite_group
    for argfile in pabot_args[bstack1ll_opy_ (u"ࠢࡢࡴࡪࡹࡲ࡫࡮ࡵࡨ࡬ࡰࡪࡹࠢ઱")] or [(bstack1ll_opy_ (u"ࠣࠤલ"), None)]
    for platform in enumerate(bstack1lll1ll111_opy_)
  ]
def bstack1ll1111ll_opy_(self, datasources, outs_dir, options,
                        execution_item, command, verbose, argfile,
                        hive=None, processes=0, platform_index=0, bstack1l1ll11l_opy_=bstack1ll_opy_ (u"ࠩࠪળ")):
  global bstack11lll11ll_opy_
  self.platform_index = platform_index
  self.bstack11llll11_opy_ = bstack1l1ll11l_opy_
  bstack11lll11ll_opy_(self, datasources, outs_dir, options,
                      execution_item, command, verbose, argfile, hive, processes)
def bstack11ll111l1_opy_(caller_id, datasources, is_last, item, outs_dir):
  global bstack1ll111l11l_opy_
  global bstack11ll1l1l_opy_
  if not bstack1ll_opy_ (u"ࠪࡺࡦࡸࡩࡢࡤ࡯ࡩࠬ઴") in item.options:
    item.options[bstack1ll_opy_ (u"ࠫࡻࡧࡲࡪࡣࡥࡰࡪ࠭વ")] = []
  for v in item.options[bstack1ll_opy_ (u"ࠬࡼࡡࡳ࡫ࡤࡦࡱ࡫ࠧશ")]:
    if bstack1ll_opy_ (u"࠭ࡂࡔࡖࡄࡇࡐࡖࡌࡂࡖࡉࡓࡗࡓࡉࡏࡆࡈ࡜ࠬષ") in v:
      item.options[bstack1ll_opy_ (u"ࠧࡷࡣࡵ࡭ࡦࡨ࡬ࡦࠩસ")].remove(v)
    if bstack1ll_opy_ (u"ࠨࡄࡖࡘࡆࡉࡋࡄࡎࡌࡅࡗࡍࡓࠨહ") in v:
      item.options[bstack1ll_opy_ (u"ࠩࡹࡥࡷ࡯ࡡࡣ࡮ࡨࠫ઺")].remove(v)
  item.options[bstack1ll_opy_ (u"ࠪࡺࡦࡸࡩࡢࡤ࡯ࡩࠬ઻")].insert(0, bstack1ll_opy_ (u"ࠫࡇ࡙ࡔࡂࡅࡎࡔࡑࡇࡔࡇࡑࡕࡑࡎࡔࡄࡆ࡚࠽ࡿࢂ઼࠭").format(item.platform_index))
  item.options[bstack1ll_opy_ (u"ࠬࡼࡡࡳ࡫ࡤࡦࡱ࡫ࠧઽ")].insert(0, bstack1ll_opy_ (u"࠭ࡂࡔࡖࡄࡇࡐࡊࡅࡇࡎࡒࡇࡆࡒࡉࡅࡇࡑࡘࡎࡌࡉࡆࡔ࠽ࡿࢂ࠭ા").format(item.bstack11llll11_opy_))
  if bstack11ll1l1l_opy_:
    item.options[bstack1ll_opy_ (u"ࠧࡷࡣࡵ࡭ࡦࡨ࡬ࡦࠩિ")].insert(0, bstack1ll_opy_ (u"ࠨࡄࡖࡘࡆࡉࡋࡄࡎࡌࡅࡗࡍࡓ࠻ࡽࢀࠫી").format(bstack11ll1l1l_opy_))
  return bstack1ll111l11l_opy_(caller_id, datasources, is_last, item, outs_dir)
def bstack11l11l1l_opy_(command, item_index):
  global bstack11ll1l1l_opy_
  if bstack11ll1l1l_opy_:
    command[0] = command[0].replace(bstack1ll_opy_ (u"ࠩࡵࡳࡧࡵࡴࠨુ"), bstack1ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠯ࡶࡨࡰࠦࡲࡰࡤࡲࡸ࠲࡯࡮ࡵࡧࡵࡲࡦࡲࠠ࠮࠯ࡥࡷࡹࡧࡣ࡬ࡡ࡬ࡸࡪࡳ࡟ࡪࡰࡧࡩࡽࠦࠧૂ") + str(
      item_index) + bstack1ll_opy_ (u"ࠫࠥ࠭ૃ") + bstack11ll1l1l_opy_, 1)
  else:
    command[0] = command[0].replace(bstack1ll_opy_ (u"ࠬࡸ࡯ࡣࡱࡷࠫૄ"),
                                    bstack1ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠲ࡹࡤ࡬ࠢࡵࡳࡧࡵࡴ࠮࡫ࡱࡸࡪࡸ࡮ࡢ࡮ࠣ࠱࠲ࡨࡳࡵࡣࡦ࡯ࡤ࡯ࡴࡦ࡯ࡢ࡭ࡳࡪࡥࡹࠢࠪૅ") + str(item_index), 1)
def bstack1l111l1ll_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index):
  global bstack111l1l111_opy_
  bstack11l11l1l_opy_(command, item_index)
  return bstack111l1l111_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index)
def bstack1l111llll_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir):
  global bstack111l1l111_opy_
  bstack11l11l1l_opy_(command, item_index)
  return bstack111l1l111_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir)
def bstack1ll1l11ll_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout):
  global bstack111l1l111_opy_
  bstack11l11l1l_opy_(command, item_index)
  return bstack111l1l111_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout)
def bstack1lll1111_opy_(self, runner, quiet=False, capture=True):
  global bstack11ll11ll_opy_
  bstack11l11l1ll_opy_ = bstack11ll11ll_opy_(self, runner, quiet=False, capture=True)
  if self.exception:
    if not hasattr(runner, bstack1ll_opy_ (u"ࠧࡦࡺࡦࡩࡵࡺࡩࡰࡰࡢࡥࡷࡸࠧ૆")):
      runner.exception_arr = []
    if not hasattr(runner, bstack1ll_opy_ (u"ࠨࡧࡻࡧࡤࡺࡲࡢࡥࡨࡦࡦࡩ࡫ࡠࡣࡵࡶࠬે")):
      runner.exc_traceback_arr = []
    runner.exception = self.exception
    runner.exc_traceback = self.exc_traceback
    runner.exception_arr.append(self.exception)
    runner.exc_traceback_arr.append(self.exc_traceback)
  return bstack11l11l1ll_opy_
def bstack1lll1l1l1l_opy_(self, name, context, *args):
  global bstack1llll1ll_opy_
  if name == bstack1ll_opy_ (u"ࠩࡥࡩ࡫ࡵࡲࡦࡡࡩࡩࡦࡺࡵࡳࡧࠪૈ"):
    bstack1llll1ll_opy_(self, name, context, *args)
    try:
      if not bstack1llll1l111_opy_:
        bstack1111l1l1l_opy_ = threading.current_thread().bstackSessionDriver if bstack1lll111111_opy_(bstack1ll_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡖࡩࡸࡹࡩࡰࡰࡇࡶ࡮ࡼࡥࡳࠩૉ")) else context.browser
        bstack1llll1lll_opy_ = str(self.feature.name)
        bstack1ll1l11ll1_opy_(context, bstack1llll1lll_opy_)
        bstack1111l1l1l_opy_.execute_script(bstack1ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻࠣࡣࡦࡸ࡮ࡵ࡮ࠣ࠼ࠣࠦࡸ࡫ࡴࡔࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠧ࠲ࠠࠣࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠦ࠿ࠦࡻࠣࡰࡤࡱࡪࠨ࠺ࠡࠩ૊") + json.dumps(bstack1llll1lll_opy_) + bstack1ll_opy_ (u"ࠬࢃࡽࠨો"))
      self.driver_before_scenario = False
    except Exception as e:
      logger.debug(bstack1ll_opy_ (u"࠭ࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡶࡩࡹࠦࡳࡦࡵࡶ࡭ࡴࡴࠠ࡯ࡣࡰࡩࠥ࡯࡮ࠡࡤࡨࡪࡴࡸࡥࠡࡨࡨࡥࡹࡻࡲࡦ࠼ࠣࡿࢂ࠭ૌ").format(str(e)))
  elif name == bstack1ll_opy_ (u"ࠧࡣࡧࡩࡳࡷ࡫࡟ࡴࡥࡨࡲࡦࡸࡩࡰ્ࠩ"):
    bstack1llll1ll_opy_(self, name, context, *args)
    try:
      if not hasattr(self, bstack1ll_opy_ (u"ࠨࡦࡵ࡭ࡻ࡫ࡲࡠࡤࡨࡪࡴࡸࡥࡠࡵࡦࡩࡳࡧࡲࡪࡱࠪ૎")):
        self.driver_before_scenario = True
      if (not bstack1llll1l111_opy_):
        scenario_name = args[0].name
        feature_name = bstack1llll1lll_opy_ = str(self.feature.name)
        bstack1llll1lll_opy_ = feature_name + bstack1ll_opy_ (u"ࠩࠣ࠱ࠥ࠭૏") + scenario_name
        bstack1111l1l1l_opy_ = threading.current_thread().bstackSessionDriver if bstack1lll111111_opy_(bstack1ll_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡖࡩࡸࡹࡩࡰࡰࡇࡶ࡮ࡼࡥࡳࠩૐ")) else context.browser
        if self.driver_before_scenario:
          bstack1ll1l11ll1_opy_(context, bstack1llll1lll_opy_)
          bstack1111l1l1l_opy_.execute_script(bstack1ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻࠣࡣࡦࡸ࡮ࡵ࡮ࠣ࠼ࠣࠦࡸ࡫ࡴࡔࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠧ࠲ࠠࠣࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠦ࠿ࠦࡻࠣࡰࡤࡱࡪࠨ࠺ࠡࠩ૑") + json.dumps(bstack1llll1lll_opy_) + bstack1ll_opy_ (u"ࠬࢃࡽࠨ૒"))
    except Exception as e:
      logger.debug(bstack1ll_opy_ (u"࠭ࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡶࡩࡹࠦࡳࡦࡵࡶ࡭ࡴࡴࠠ࡯ࡣࡰࡩࠥ࡯࡮ࠡࡤࡨࡪࡴࡸࡥࠡࡵࡦࡩࡳࡧࡲࡪࡱ࠽ࠤࢀࢃࠧ૓").format(str(e)))
  elif name == bstack1ll_opy_ (u"ࠧࡢࡨࡷࡩࡷࡥࡳࡤࡧࡱࡥࡷ࡯࡯ࠨ૔"):
    try:
      bstack1l111l1l1_opy_ = args[0].status.name
      bstack1111l1l1l_opy_ = threading.current_thread().bstackSessionDriver if bstack1ll_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡔࡧࡶࡷ࡮ࡵ࡮ࡅࡴ࡬ࡺࡪࡸࠧ૕") in threading.current_thread().__dict__.keys() else context.browser
      if str(bstack1l111l1l1_opy_).lower() == bstack1ll_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩ૖"):
        bstack1lll111ll_opy_ = bstack1ll_opy_ (u"ࠪࠫ૗")
        bstack1ll1111l_opy_ = bstack1ll_opy_ (u"ࠫࠬ૘")
        bstack111lllll_opy_ = bstack1ll_opy_ (u"ࠬ࠭૙")
        try:
          import traceback
          bstack1lll111ll_opy_ = self.exception.__class__.__name__
          bstack1ll1l11l1l_opy_ = traceback.format_tb(self.exc_traceback)
          bstack1ll1111l_opy_ = bstack1ll_opy_ (u"࠭ࠠࠨ૚").join(bstack1ll1l11l1l_opy_)
          bstack111lllll_opy_ = bstack1ll1l11l1l_opy_[-1]
        except Exception as e:
          logger.debug(bstack1lllll11ll_opy_.format(str(e)))
        bstack1lll111ll_opy_ += bstack111lllll_opy_
        bstack1lll11l111_opy_(context, json.dumps(str(args[0].name) + bstack1ll_opy_ (u"ࠢࠡ࠯ࠣࡊࡦ࡯࡬ࡦࡦࠤࡠࡳࠨ૛") + str(bstack1ll1111l_opy_)),
                            bstack1ll_opy_ (u"ࠣࡧࡵࡶࡴࡸࠢ૜"))
        if self.driver_before_scenario:
          bstack11lll111_opy_(context, bstack1ll_opy_ (u"ࠤࡩࡥ࡮ࡲࡥࡥࠤ૝"), bstack1lll111ll_opy_)
          bstack1111l1l1l_opy_.execute_script(bstack1ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁࠢࡢࡥࡷ࡭ࡴࡴࠢ࠻ࠢࠥࡥࡳࡴ࡯ࡵࡣࡷࡩࠧ࠲ࠠࠣࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠦ࠿ࠦࡻࠣࡦࡤࡸࡦࠨ࠺ࠨ૞") + json.dumps(str(args[0].name) + bstack1ll_opy_ (u"ࠦࠥ࠳ࠠࡇࡣ࡬ࡰࡪࡪࠡ࡝ࡰࠥ૟") + str(bstack1ll1111l_opy_)) + bstack1ll_opy_ (u"ࠬ࠲ࠠࠣ࡮ࡨࡺࡪࡲࠢ࠻ࠢࠥࡩࡷࡸ࡯ࡳࠤࢀࢁࠬૠ"))
        if self.driver_before_scenario:
          bstack1111l1l1l_opy_.execute_script(bstack1ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࠥࡥࡨࡺࡩࡰࡰࠥ࠾ࠥࠨࡳࡦࡶࡖࡩࡸࡹࡩࡰࡰࡖࡸࡦࡺࡵࡴࠤ࠯ࠤࠧࡧࡲࡨࡷࡰࡩࡳࡺࡳࠣ࠼ࠣࡿࠧࡹࡴࡢࡶࡸࡷࠧࡀࠢࡧࡣ࡬ࡰࡪࡪࠢ࠭ࠢࠥࡶࡪࡧࡳࡰࡰࠥ࠾ࠥ࠭ૡ") + json.dumps(bstack1ll_opy_ (u"ࠢࡔࡥࡨࡲࡦࡸࡩࡰࠢࡩࡥ࡮ࡲࡥࡥࠢࡺ࡭ࡹ࡮࠺ࠡ࡞ࡱࠦૢ") + str(bstack1lll111ll_opy_)) + bstack1ll_opy_ (u"ࠨࡿࢀࠫૣ"))
      else:
        bstack1lll11l111_opy_(context, bstack1ll_opy_ (u"ࠤࡓࡥࡸࡹࡥࡥࠣࠥ૤"), bstack1ll_opy_ (u"ࠥ࡭ࡳ࡬࡯ࠣ૥"))
        if self.driver_before_scenario:
          bstack11lll111_opy_(context, bstack1ll_opy_ (u"ࠦࡵࡧࡳࡴࡧࡧࠦ૦"))
        bstack1111l1l1l_opy_.execute_script(bstack1ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࡼࠤࡤࡧࡹ࡯࡯࡯ࠤ࠽ࠤࠧࡧ࡮࡯ࡱࡷࡥࡹ࡫ࠢ࠭ࠢࠥࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸࠨ࠺ࠡࡽࠥࡨࡦࡺࡡࠣ࠼ࠪ૧") + json.dumps(str(args[0].name) + bstack1ll_opy_ (u"ࠨࠠ࠮ࠢࡓࡥࡸࡹࡥࡥࠣࠥ૨")) + bstack1ll_opy_ (u"ࠧ࠭ࠢࠥࡰࡪࡼࡥ࡭ࠤ࠽ࠤࠧ࡯࡮ࡧࡱࠥࢁࢂ࠭૩"))
        if self.driver_before_scenario:
          bstack1111l1l1l_opy_.execute_script(bstack1ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࡿࠧࡧࡣࡵ࡫ࡲࡲࠧࡀࠠࠣࡵࡨࡸࡘ࡫ࡳࡴ࡫ࡲࡲࡘࡺࡡࡵࡷࡶࠦ࠱ࠦࠢࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠥ࠾ࠥࢁࠢࡴࡶࡤࡸࡺࡹࠢ࠻ࠤࡳࡥࡸࡹࡥࡥࠤࢀࢁࠬ૪"))
    except Exception as e:
      logger.debug(bstack1ll_opy_ (u"ࠩࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡳࡡࡳ࡭ࠣࡷࡪࡹࡳࡪࡱࡱࠤࡸࡺࡡࡵࡷࡶࠤ࡮ࡴࠠࡢࡨࡷࡩࡷࠦࡦࡦࡣࡷࡹࡷ࡫࠺ࠡࡽࢀࠫ૫").format(str(e)))
  elif name == bstack1ll_opy_ (u"ࠪࡥ࡫ࡺࡥࡳࡡࡩࡩࡦࡺࡵࡳࡧࠪ૬"):
    try:
      bstack1111l1l1l_opy_ = threading.current_thread().bstackSessionDriver if bstack1lll111111_opy_(bstack1ll_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡗࡪࡹࡳࡪࡱࡱࡈࡷ࡯ࡶࡦࡴࠪ૭")) else context.browser
      if context.failed is True:
        bstack111llll1_opy_ = []
        bstack11ll1ll11_opy_ = []
        bstack11ll1lll_opy_ = []
        bstack1ll1lll1ll_opy_ = bstack1ll_opy_ (u"ࠬ࠭૮")
        try:
          import traceback
          for exc in self.exception_arr:
            bstack111llll1_opy_.append(exc.__class__.__name__)
          for exc_tb in self.exc_traceback_arr:
            bstack1ll1l11l1l_opy_ = traceback.format_tb(exc_tb)
            bstack1ll1111l1l_opy_ = bstack1ll_opy_ (u"࠭ࠠࠨ૯").join(bstack1ll1l11l1l_opy_)
            bstack11ll1ll11_opy_.append(bstack1ll1111l1l_opy_)
            bstack11ll1lll_opy_.append(bstack1ll1l11l1l_opy_[-1])
        except Exception as e:
          logger.debug(bstack1lllll11ll_opy_.format(str(e)))
        bstack1lll111ll_opy_ = bstack1ll_opy_ (u"ࠧࠨ૰")
        for i in range(len(bstack111llll1_opy_)):
          bstack1lll111ll_opy_ += bstack111llll1_opy_[i] + bstack11ll1lll_opy_[i] + bstack1ll_opy_ (u"ࠨ࡞ࡱࠫ૱")
        bstack1ll1lll1ll_opy_ = bstack1ll_opy_ (u"ࠩࠣࠫ૲").join(bstack11ll1ll11_opy_)
        if not self.driver_before_scenario:
          bstack1lll11l111_opy_(context, bstack1ll1lll1ll_opy_, bstack1ll_opy_ (u"ࠥࡩࡷࡸ࡯ࡳࠤ૳"))
          bstack11lll111_opy_(context, bstack1ll_opy_ (u"ࠦ࡫ࡧࡩ࡭ࡧࡧࠦ૴"), bstack1lll111ll_opy_)
          bstack1111l1l1l_opy_.execute_script(bstack1ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࡼࠤࡤࡧࡹ࡯࡯࡯ࠤ࠽ࠤࠧࡧ࡮࡯ࡱࡷࡥࡹ࡫ࠢ࠭ࠢࠥࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸࠨ࠺ࠡࡽࠥࡨࡦࡺࡡࠣ࠼ࠪ૵") + json.dumps(bstack1ll1lll1ll_opy_) + bstack1ll_opy_ (u"࠭ࠬࠡࠤ࡯ࡩࡻ࡫࡬ࠣ࠼ࠣࠦࡪࡸࡲࡰࡴࠥࢁࢂ࠭૶"))
          bstack1111l1l1l_opy_.execute_script(bstack1ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࡾࠦࡦࡩࡴࡪࡱࡱࠦ࠿ࠦࠢࡴࡧࡷࡗࡪࡹࡳࡪࡱࡱࡗࡹࡧࡴࡶࡵࠥ࠰ࠥࠨࡡࡳࡩࡸࡱࡪࡴࡴࡴࠤ࠽ࠤࢀࠨࡳࡵࡣࡷࡹࡸࠨ࠺ࠣࡨࡤ࡭ࡱ࡫ࡤࠣ࠮ࠣࠦࡷ࡫ࡡࡴࡱࡱࠦ࠿ࠦࠧ૷") + json.dumps(bstack1ll_opy_ (u"ࠣࡕࡲࡱࡪࠦࡳࡤࡧࡱࡥࡷ࡯࡯ࡴࠢࡩࡥ࡮ࡲࡥࡥ࠼ࠣࡠࡳࠨ૸") + str(bstack1lll111ll_opy_)) + bstack1ll_opy_ (u"ࠩࢀࢁࠬૹ"))
          bstack1ll1l1l1ll_opy_ = bstack1l11l1ll1_opy_(bstack1ll1lll1ll_opy_, self.feature.name, logger)
          if (bstack1ll1l1l1ll_opy_ != None):
            bstack1ll1llll_opy_.append(bstack1ll1l1l1ll_opy_)
      else:
        if not self.driver_before_scenario:
          bstack1lll11l111_opy_(context, bstack1ll_opy_ (u"ࠥࡊࡪࡧࡴࡶࡴࡨ࠾ࠥࠨૺ") + str(self.feature.name) + bstack1ll_opy_ (u"ࠦࠥࡶࡡࡴࡵࡨࡨࠦࠨૻ"), bstack1ll_opy_ (u"ࠧ࡯࡮ࡧࡱࠥૼ"))
          bstack11lll111_opy_(context, bstack1ll_opy_ (u"ࠨࡰࡢࡵࡶࡩࡩࠨ૽"))
          bstack1111l1l1l_opy_.execute_script(bstack1ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࡾࠦࡦࡩࡴࡪࡱࡱࠦ࠿ࠦࠢࡢࡰࡱࡳࡹࡧࡴࡦࠤ࠯ࠤࠧࡧࡲࡨࡷࡰࡩࡳࡺࡳࠣ࠼ࠣࡿࠧࡪࡡࡵࡣࠥ࠾ࠬ૾") + json.dumps(bstack1ll_opy_ (u"ࠣࡈࡨࡥࡹࡻࡲࡦ࠼ࠣࠦ૿") + str(self.feature.name) + bstack1ll_opy_ (u"ࠤࠣࡴࡦࡹࡳࡦࡦࠤࠦ଀")) + bstack1ll_opy_ (u"ࠪ࠰ࠥࠨ࡬ࡦࡸࡨࡰࠧࡀࠠࠣ࡫ࡱࡪࡴࠨࡽࡾࠩଁ"))
          bstack1111l1l1l_opy_.execute_script(bstack1ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻࠣࡣࡦࡸ࡮ࡵ࡮ࠣ࠼ࠣࠦࡸ࡫ࡴࡔࡧࡶࡷ࡮ࡵ࡮ࡔࡶࡤࡸࡺࡹࠢ࠭ࠢࠥࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸࠨ࠺ࠡࡽࠥࡷࡹࡧࡴࡶࡵࠥ࠾ࠧࡶࡡࡴࡵࡨࡨࠧࢃࡽࠨଂ"))
          bstack1ll1l1l1ll_opy_ = bstack1l11l1ll1_opy_(bstack1ll1lll1ll_opy_, self.feature.name, logger)
          if (bstack1ll1l1l1ll_opy_ != None):
            bstack1ll1llll_opy_.append(bstack1ll1l1l1ll_opy_)
    except Exception as e:
      logger.debug(bstack1ll_opy_ (u"ࠬࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡ࡯ࡤࡶࡰࠦࡳࡦࡵࡶ࡭ࡴࡴࠠࡴࡶࡤࡸࡺࡹࠠࡪࡰࠣࡥ࡫ࡺࡥࡳࠢࡩࡩࡦࡺࡵࡳࡧ࠽ࠤࢀࢃࠧଃ").format(str(e)))
  else:
    bstack1llll1ll_opy_(self, name, context, *args)
  if name in [bstack1ll_opy_ (u"࠭ࡡࡧࡶࡨࡶࡤ࡬ࡥࡢࡶࡸࡶࡪ࠭଄"), bstack1ll_opy_ (u"ࠧࡢࡨࡷࡩࡷࡥࡳࡤࡧࡱࡥࡷ࡯࡯ࠨଅ")]:
    bstack1llll1ll_opy_(self, name, context, *args)
    if (name == bstack1ll_opy_ (u"ࠨࡣࡩࡸࡪࡸ࡟ࡴࡥࡨࡲࡦࡸࡩࡰࠩଆ") and self.driver_before_scenario) or (
            name == bstack1ll_opy_ (u"ࠩࡤࡪࡹ࡫ࡲࡠࡨࡨࡥࡹࡻࡲࡦࠩଇ") and not self.driver_before_scenario):
      try:
        bstack1111l1l1l_opy_ = threading.current_thread().bstackSessionDriver if bstack1lll111111_opy_(bstack1ll_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡖࡩࡸࡹࡩࡰࡰࡇࡶ࡮ࡼࡥࡳࠩଈ")) else context.browser
        bstack1111l1l1l_opy_.quit()
      except Exception:
        pass
def bstack111ll111_opy_(config, startdir):
  return bstack1ll_opy_ (u"ࠦࡩࡸࡩࡷࡧࡵ࠾ࠥࢁ࠰ࡾࠤଉ").format(bstack1ll_opy_ (u"ࠧࡈࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࠦଊ"))
notset = Notset()
def bstack1ll11l111_opy_(self, name: str, default=notset, skip: bool = False):
  global bstack1llllll111_opy_
  if str(name).lower() == bstack1ll_opy_ (u"࠭ࡤࡳ࡫ࡹࡩࡷ࠭ଋ"):
    return bstack1ll_opy_ (u"ࠢࡃࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࠨଌ")
  else:
    return bstack1llllll111_opy_(self, name, default, skip)
def bstack1ll11llll1_opy_(item, when):
  global bstack11l111lll_opy_
  try:
    bstack11l111lll_opy_(item, when)
  except Exception as e:
    pass
def bstack11111llll_opy_():
  return
def bstack11ll1111_opy_(type, name, status, reason, bstack11l1llll_opy_, bstack1lll11ll11_opy_):
  bstack1llll1l1l_opy_ = {
    bstack1ll_opy_ (u"ࠨࡣࡦࡸ࡮ࡵ࡮ࠨ଍"): type,
    bstack1ll_opy_ (u"ࠩࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠬ଎"): {}
  }
  if type == bstack1ll_opy_ (u"ࠪࡥࡳࡴ࡯ࡵࡣࡷࡩࠬଏ"):
    bstack1llll1l1l_opy_[bstack1ll_opy_ (u"ࠫࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠧଐ")][bstack1ll_opy_ (u"ࠬࡲࡥࡷࡧ࡯ࠫ଑")] = bstack11l1llll_opy_
    bstack1llll1l1l_opy_[bstack1ll_opy_ (u"࠭ࡡࡳࡩࡸࡱࡪࡴࡴࡴࠩ଒")][bstack1ll_opy_ (u"ࠧࡥࡣࡷࡥࠬଓ")] = json.dumps(str(bstack1lll11ll11_opy_))
  if type == bstack1ll_opy_ (u"ࠨࡵࡨࡸࡘ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠩଔ"):
    bstack1llll1l1l_opy_[bstack1ll_opy_ (u"ࠩࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠬକ")][bstack1ll_opy_ (u"ࠪࡲࡦࡳࡥࠨଖ")] = name
  if type == bstack1ll_opy_ (u"ࠫࡸ࡫ࡴࡔࡧࡶࡷ࡮ࡵ࡮ࡔࡶࡤࡸࡺࡹࠧଗ"):
    bstack1llll1l1l_opy_[bstack1ll_opy_ (u"ࠬࡧࡲࡨࡷࡰࡩࡳࡺࡳࠨଘ")][bstack1ll_opy_ (u"࠭ࡳࡵࡣࡷࡹࡸ࠭ଙ")] = status
    if status == bstack1ll_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧଚ"):
      bstack1llll1l1l_opy_[bstack1ll_opy_ (u"ࠨࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠫଛ")][bstack1ll_opy_ (u"ࠩࡵࡩࡦࡹ࡯࡯ࠩଜ")] = json.dumps(str(reason))
  bstack11l1ll11l_opy_ = bstack1ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁࡽࠨଝ").format(json.dumps(bstack1llll1l1l_opy_))
  return bstack11l1ll11l_opy_
def bstack1l11111l_opy_(item, call, rep):
  global bstack11111111l_opy_
  global bstack11l1l1l1l_opy_
  global bstack1llll1l111_opy_
  name = bstack1ll_opy_ (u"ࠫࠬଞ")
  try:
    if rep.when == bstack1ll_opy_ (u"ࠬࡩࡡ࡭࡮ࠪଟ"):
      bstack1ll11l1ll_opy_ = threading.current_thread().bstack111ll11l1_opy_
      try:
        if not bstack1llll1l111_opy_:
          name = str(rep.nodeid)
          bstack11ll11l1l_opy_ = bstack11ll1111_opy_(bstack1ll_opy_ (u"࠭ࡳࡦࡶࡖࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠧଠ"), name, bstack1ll_opy_ (u"ࠧࠨଡ"), bstack1ll_opy_ (u"ࠨࠩଢ"), bstack1ll_opy_ (u"ࠩࠪଣ"), bstack1ll_opy_ (u"ࠪࠫତ"))
          threading.current_thread().bstack1111l111_opy_ = name
          for driver in bstack11l1l1l1l_opy_:
            if bstack1ll11l1ll_opy_ == driver.session_id:
              driver.execute_script(bstack11ll11l1l_opy_)
      except Exception as e:
        logger.debug(bstack1ll_opy_ (u"ࠫࡊࡸࡲࡰࡴࠣ࡭ࡳࠦࡳࡦࡶࡷ࡭ࡳ࡭ࠠࡴࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠥ࡬࡯ࡳࠢࡳࡽࡹ࡫ࡳࡵ࠯ࡥࡨࡩࠦࡳࡦࡵࡶ࡭ࡴࡴ࠺ࠡࡽࢀࠫଥ").format(str(e)))
      try:
        bstack1ll11l11_opy_(rep.outcome.lower())
        if rep.outcome.lower() != bstack1ll_opy_ (u"ࠬࡹ࡫ࡪࡲࡳࡩࡩ࠭ଦ"):
          status = bstack1ll_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭ଧ") if rep.outcome.lower() == bstack1ll_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧନ") else bstack1ll_opy_ (u"ࠨࡲࡤࡷࡸ࡫ࡤࠨ଩")
          reason = bstack1ll_opy_ (u"ࠩࠪପ")
          if status == bstack1ll_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪଫ"):
            reason = rep.longrepr.reprcrash.message
            if (not threading.current_thread().bstackTestErrorMessages):
              threading.current_thread().bstackTestErrorMessages = []
            threading.current_thread().bstackTestErrorMessages.append(reason)
          level = bstack1ll_opy_ (u"ࠫ࡮ࡴࡦࡰࠩବ") if status == bstack1ll_opy_ (u"ࠬࡶࡡࡴࡵࡨࡨࠬଭ") else bstack1ll_opy_ (u"࠭ࡥࡳࡴࡲࡶࠬମ")
          data = name + bstack1ll_opy_ (u"ࠧࠡࡲࡤࡷࡸ࡫ࡤࠢࠩଯ") if status == bstack1ll_opy_ (u"ࠨࡲࡤࡷࡸ࡫ࡤࠨର") else name + bstack1ll_opy_ (u"ࠩࠣࡪࡦ࡯࡬ࡦࡦࠤࠤࠬ଱") + reason
          bstack1l11l1lll_opy_ = bstack11ll1111_opy_(bstack1ll_opy_ (u"ࠪࡥࡳࡴ࡯ࡵࡣࡷࡩࠬଲ"), bstack1ll_opy_ (u"ࠫࠬଳ"), bstack1ll_opy_ (u"ࠬ࠭଴"), bstack1ll_opy_ (u"࠭ࠧଵ"), level, data)
          for driver in bstack11l1l1l1l_opy_:
            if bstack1ll11l1ll_opy_ == driver.session_id:
              driver.execute_script(bstack1l11l1lll_opy_)
      except Exception as e:
        logger.debug(bstack1ll_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡶࡩࡹࡺࡩ࡯ࡩࠣࡷࡪࡹࡳࡪࡱࡱࠤࡨࡵ࡮ࡵࡧࡻࡸࠥ࡬࡯ࡳࠢࡳࡽࡹ࡫ࡳࡵ࠯ࡥࡨࡩࠦࡳࡦࡵࡶ࡭ࡴࡴ࠺ࠡࡽࢀࠫଶ").format(str(e)))
  except Exception as e:
    logger.debug(bstack1ll_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡪࡰࠣ࡫ࡪࡺࡴࡪࡰࡪࠤࡸࡺࡡࡵࡧࠣ࡭ࡳࠦࡰࡺࡶࡨࡷࡹ࠳ࡢࡥࡦࠣࡸࡪࡹࡴࠡࡵࡷࡥࡹࡻࡳ࠻ࠢࡾࢁࠬଷ").format(str(e)))
  bstack11111111l_opy_(item, call, rep)
def bstack1ll111ll11_opy_(framework_name):
  global bstack1lll11l11l_opy_
  global bstack11lll1lll_opy_
  global bstack1l111l11l_opy_
  bstack1lll11l11l_opy_ = framework_name
  logger.info(bstack1ll1111lll_opy_.format(bstack1lll11l11l_opy_.split(bstack1ll_opy_ (u"ࠩ࠰ࠫସ"))[0]))
  try:
    from selenium import webdriver
    from selenium.webdriver.common.service import Service
    from selenium.webdriver.remote.webdriver import WebDriver
    if bstack1lll1l11l_opy_:
      Service.start = bstack1lll1l11l1_opy_
      Service.stop = bstack1ll11lll11_opy_
      webdriver.Remote.get = bstack111l1ll11_opy_
      WebDriver.close = bstack11ll11111_opy_
      WebDriver.quit = bstack1lll1lll1_opy_
      webdriver.Remote.__init__ = bstack1lllll11l_opy_
      WebDriver.getAccessibilityResults = getAccessibilityResults
      WebDriver.getAccessibilityResultsSummary = getAccessibilityResultsSummary
    if not bstack1lll1l11l_opy_ and bstack11l1l1l1_opy_.on():
      webdriver.Remote.__init__ = bstack11111ll1_opy_
    bstack11lll1lll_opy_ = True
  except Exception as e:
    pass
  bstack1lllll111l_opy_()
  if not bstack11lll1lll_opy_:
    bstack11111l1l_opy_(bstack1ll_opy_ (u"ࠥࡔࡦࡩ࡫ࡢࡩࡨࡷࠥࡴ࡯ࡵࠢ࡬ࡲࡸࡺࡡ࡭࡮ࡨࡨࠧହ"), bstack1l1l1ll1l_opy_)
  if bstack111l1l1l1_opy_():
    try:
      from selenium.webdriver.remote.remote_connection import RemoteConnection
      RemoteConnection._get_proxy_url = bstack1l1lll11_opy_
    except Exception as e:
      logger.error(bstack111l1llll_opy_.format(str(e)))
  if bstack11llll111_opy_():
    bstack1ll11l1lll_opy_(CONFIG, logger)
  if (bstack1ll_opy_ (u"ࠫࡷࡵࡢࡰࡶࠪ଺") in str(framework_name).lower()):
    try:
      from robot import run_cli
      from robot.output import Output
      from robot.running.status import TestStatus
      from pabot.pabot import QueueItem
      from pabot import pabot
      try:
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCreator
        WebDriverCreator._get_ff_profile = bstack1ll111l1ll_opy_
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCache
        WebDriverCache.close = bstack11l11llll_opy_
      except Exception as e:
        logger.warn(bstack111ll1l1l_opy_ + str(e))
      try:
        from AppiumLibrary.utils.applicationcache import ApplicationCache
        ApplicationCache.close = bstack1ll1l111ll_opy_
      except Exception as e:
        logger.debug(bstack111lll11_opy_ + str(e))
    except Exception as e:
      bstack11111l1l_opy_(e, bstack111ll1l1l_opy_)
    Output.end_test = bstack1l11lll11_opy_
    TestStatus.__init__ = bstack1111lll1l_opy_
    QueueItem.__init__ = bstack1ll1111ll_opy_
    pabot._create_items = bstack11ll11lll_opy_
    try:
      from pabot import __version__ as bstack1ll11ll11l_opy_
      if version.parse(bstack1ll11ll11l_opy_) >= version.parse(bstack1ll_opy_ (u"ࠬ࠸࠮࠲࠷࠱࠴ࠬ଻")):
        pabot._run = bstack1ll1l11ll_opy_
      elif version.parse(bstack1ll11ll11l_opy_) >= version.parse(bstack1ll_opy_ (u"࠭࠲࠯࠳࠶࠲࠵଼࠭")):
        pabot._run = bstack1l111llll_opy_
      else:
        pabot._run = bstack1l111l1ll_opy_
    except Exception as e:
      pabot._run = bstack1l111l1ll_opy_
    pabot._create_command_for_execution = bstack11ll111l1_opy_
    pabot._report_results = bstack111l1l1ll_opy_
  if bstack1ll_opy_ (u"ࠧࡣࡧ࡫ࡥࡻ࡫ࠧଽ") in str(framework_name).lower():
    try:
      from behave.runner import Runner
      from behave.model import Step
    except Exception as e:
      bstack11111l1l_opy_(e, bstack1ll1l1111l_opy_)
    Runner.run_hook = bstack1lll1l1l1l_opy_
    Step.run = bstack1lll1111_opy_
  if bstack1ll_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࠨା") in str(framework_name).lower():
    if not bstack1lll1l11l_opy_:
      return
    try:
      from pytest_selenium import pytest_selenium
      from _pytest.config import Config
      pytest_selenium.pytest_report_header = bstack111ll111_opy_
      from pytest_selenium.drivers import browserstack
      browserstack.pytest_selenium_runtest_makereport = bstack11111llll_opy_
      Config.getoption = bstack1ll11l111_opy_
    except Exception as e:
      pass
    try:
      from pytest_bdd import reporting
      reporting.runtest_makereport = bstack1l11111l_opy_
    except Exception as e:
      pass
def bstack111lll1l_opy_():
  global CONFIG
  if bstack1ll_opy_ (u"ࠩࡳࡥࡷࡧ࡬࡭ࡧ࡯ࡷࡕ࡫ࡲࡑ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩି") in CONFIG and int(CONFIG[bstack1ll_opy_ (u"ࠪࡴࡦࡸࡡ࡭࡮ࡨࡰࡸࡖࡥࡳࡒ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪୀ")]) > 1:
    logger.warn(bstack11l1lllll_opy_)
def bstack1ll1llll1_opy_(arg, bstack1111ll11l_opy_, bstack1l11l1l11_opy_=None):
  global CONFIG
  global bstack1l111l111_opy_
  global bstack1l11l11ll_opy_
  global bstack1lll1l11l_opy_
  global bstack1lll1l1lll_opy_
  bstack1111l1ll_opy_ = bstack1ll_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࠫୁ")
  if bstack1111ll11l_opy_ and isinstance(bstack1111ll11l_opy_, str):
    bstack1111ll11l_opy_ = eval(bstack1111ll11l_opy_)
  CONFIG = bstack1111ll11l_opy_[bstack1ll_opy_ (u"ࠬࡉࡏࡏࡈࡌࡋࠬୂ")]
  bstack1l111l111_opy_ = bstack1111ll11l_opy_[bstack1ll_opy_ (u"࠭ࡈࡖࡄࡢ࡙ࡗࡒࠧୃ")]
  bstack1l11l11ll_opy_ = bstack1111ll11l_opy_[bstack1ll_opy_ (u"ࠧࡊࡕࡢࡅࡕࡖ࡟ࡂࡗࡗࡓࡒࡇࡔࡆࠩୄ")]
  bstack1lll1l11l_opy_ = bstack1111ll11l_opy_[bstack1ll_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡂࡗࡗࡓࡒࡇࡔࡊࡑࡑࠫ୅")]
  bstack1lll1l1lll_opy_.bstack1l1l111ll_opy_(bstack1ll_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡡࡶࡩࡸࡹࡩࡰࡰࠪ୆"), bstack1lll1l11l_opy_)
  os.environ[bstack1ll_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡉࡖࡆࡓࡅࡘࡑࡕࡏࠬେ")] = bstack1111l1ll_opy_
  os.environ[bstack1ll_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡇࡔࡔࡆࡊࡉࠪୈ")] = json.dumps(CONFIG)
  os.environ[bstack1ll_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡍ࡛ࡂࡠࡗࡕࡐࠬ୉")] = bstack1l111l111_opy_
  os.environ[bstack1ll_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡏࡓࡠࡃࡓࡔࡤࡇࡕࡕࡑࡐࡅ࡙ࡋࠧ୊")] = str(bstack1l11l11ll_opy_)
  os.environ[bstack1ll_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡐ࡚ࡖࡈࡗ࡙ࡥࡐࡍࡗࡊࡍࡓ࠭ୋ")] = str(True)
  if bstack1ll11ll111_opy_(arg, [bstack1ll_opy_ (u"ࠨ࠯ࡱࠫୌ"), bstack1ll_opy_ (u"ࠩ࠰࠱ࡳࡻ࡭ࡱࡴࡲࡧࡪࡹࡳࡦࡵ୍ࠪ")]) != -1:
    os.environ[bstack1ll_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡓ࡝࡙ࡋࡓࡕࡡࡓࡅࡗࡇࡌࡍࡇࡏࠫ୎")] = str(True)
  if len(sys.argv) <= 1:
    logger.critical(bstack1l11lll1_opy_)
    return
  bstack1ll1ll111l_opy_()
  global bstack11lllll1l_opy_
  global bstack1l1lllll1_opy_
  global bstack1l1111ll_opy_
  global bstack11ll1l1l_opy_
  global bstack11l1l1111_opy_
  global bstack1l111l11l_opy_
  global bstack111111ll_opy_
  arg.append(bstack1ll_opy_ (u"ࠦ࠲࡝ࠢ୏"))
  arg.append(bstack1ll_opy_ (u"ࠧ࡯ࡧ࡯ࡱࡵࡩ࠿ࡓ࡯ࡥࡷ࡯ࡩࠥࡧ࡬ࡳࡧࡤࡨࡾࠦࡩ࡮ࡲࡲࡶࡹ࡫ࡤ࠻ࡲࡼࡸࡪࡹࡴ࠯ࡒࡼࡸࡪࡹࡴࡘࡣࡵࡲ࡮ࡴࡧࠣ୐"))
  arg.append(bstack1ll_opy_ (u"ࠨ࠭ࡘࠤ୑"))
  arg.append(bstack1ll_opy_ (u"ࠢࡪࡩࡱࡳࡷ࡫࠺ࡕࡪࡨࠤ࡭ࡵ࡯࡬࡫ࡰࡴࡱࠨ୒"))
  global bstack11ll11ll1_opy_
  global bstack111ll1ll_opy_
  global bstack1lll1l1ll1_opy_
  global bstack1lll111l1_opy_
  global bstack11lll11ll_opy_
  global bstack1ll111l11l_opy_
  global bstack1l1l11ll1_opy_
  global bstack1l1111lll_opy_
  global bstack1ll1111l1_opy_
  global bstack1llllll111_opy_
  global bstack11l111lll_opy_
  global bstack11111111l_opy_
  try:
    from selenium import webdriver
    from selenium.webdriver.remote.webdriver import WebDriver
    bstack11ll11ll1_opy_ = webdriver.Remote.__init__
    bstack111ll1ll_opy_ = WebDriver.quit
    bstack1l1l11ll1_opy_ = WebDriver.close
    bstack1l1111lll_opy_ = WebDriver.get
  except Exception as e:
    pass
  if bstack1lll11lll_opy_(CONFIG) and bstack111ll111l_opy_():
    if bstack1l1lllllll_opy_() < version.parse(bstack11l1111l_opy_):
      logger.error(bstack11ll1111l_opy_.format(bstack1l1lllllll_opy_()))
    else:
      try:
        from selenium.webdriver.remote.remote_connection import RemoteConnection
        bstack1ll1111l1_opy_ = RemoteConnection._get_proxy_url
      except Exception as e:
        logger.error(bstack111l1llll_opy_.format(str(e)))
  try:
    from _pytest.config import Config
    bstack1llllll111_opy_ = Config.getoption
    from _pytest import runner
    bstack11l111lll_opy_ = runner._update_current_test_var
  except Exception as e:
    logger.warn(e, bstack1ll1lll1_opy_)
  try:
    from pytest_bdd import reporting
    bstack11111111l_opy_ = reporting.runtest_makereport
  except Exception as e:
    logger.debug(bstack1ll_opy_ (u"ࠨࡒ࡯ࡩࡦࡹࡥࠡ࡫ࡱࡷࡹࡧ࡬࡭ࠢࡳࡽࡹ࡫ࡳࡵ࠯ࡥࡨࡩࠦࡴࡰࠢࡵࡹࡳࠦࡰࡺࡶࡨࡷࡹ࠳ࡢࡥࡦࠣࡸࡪࡹࡴࡴࠩ୓"))
  bstack1l1111ll_opy_ = CONFIG.get(bstack1ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࡍࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭୔"), {}).get(bstack1ll_opy_ (u"ࠪࡰࡴࡩࡡ࡭ࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬ୕"))
  bstack111111ll_opy_ = True
  bstack1ll111ll11_opy_(bstack111ll11l_opy_)
  os.environ[bstack1ll_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢ࡙ࡘࡋࡒࡏࡃࡐࡉࠬୖ")] = CONFIG[bstack1ll_opy_ (u"ࠬࡻࡳࡦࡴࡑࡥࡲ࡫ࠧୗ")]
  os.environ[bstack1ll_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡇࡃࡄࡇࡖࡗࡤࡑࡅ࡚ࠩ୘")] = CONFIG[bstack1ll_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡋࡦࡻࠪ୙")]
  os.environ[bstack1ll_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡂࡗࡗࡓࡒࡇࡔࡊࡑࡑࠫ୚")] = bstack1lll1l11l_opy_.__str__()
  from _pytest.config import main as bstack1l1ll111l_opy_
  bstack1l1ll111l_opy_(arg)
  if bstack1ll_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡡࡨࡶࡷࡵࡲࡠ࡮࡬ࡷࡹ࠭୛") in multiprocessing.current_process().__dict__.keys():
    for bstack11l11lll_opy_ in multiprocessing.current_process().bstack1ll1ll111_opy_:
      bstack1l11l1l11_opy_.append(bstack11l11lll_opy_)
def bstack11l11111l_opy_(arg):
  bstack1ll111ll11_opy_(bstack1l111ll1l_opy_)
  from behave.__main__ import main as bstack11111ll11_opy_
  bstack11111ll11_opy_(arg)
def bstack1ll11111_opy_():
  logger.info(bstack1111l11ll_opy_)
  import argparse
  parser = argparse.ArgumentParser()
  parser.add_argument(bstack1ll_opy_ (u"ࠪࡷࡪࡺࡵࡱࠩଡ଼"), help=bstack1ll_opy_ (u"ࠫࡌ࡫࡮ࡦࡴࡤࡸࡪࠦࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠥࡩ࡯࡯ࡨ࡬࡫ࠬଢ଼"))
  parser.add_argument(bstack1ll_opy_ (u"ࠬ࠳ࡵࠨ୞"), bstack1ll_opy_ (u"࠭࠭࠮ࡷࡶࡩࡷࡴࡡ࡮ࡧࠪୟ"), help=bstack1ll_opy_ (u"࡚ࠧࡱࡸࡶࠥࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠤࡺࡹࡥࡳࡰࡤࡱࡪ࠭ୠ"))
  parser.add_argument(bstack1ll_opy_ (u"ࠨ࠯࡮ࠫୡ"), bstack1ll_opy_ (u"ࠩ࠰࠱ࡰ࡫ࡹࠨୢ"), help=bstack1ll_opy_ (u"ࠪ࡝ࡴࡻࡲࠡࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠠࡢࡥࡦࡩࡸࡹࠠ࡬ࡧࡼࠫୣ"))
  parser.add_argument(bstack1ll_opy_ (u"ࠫ࠲࡬ࠧ୤"), bstack1ll_opy_ (u"ࠬ࠳࠭ࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࠪ୥"), help=bstack1ll_opy_ (u"࡙࠭ࡰࡷࡵࠤࡹ࡫ࡳࡵࠢࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࠬ୦"))
  bstack1llll11l1_opy_ = parser.parse_args()
  try:
    bstack111l11ll1_opy_ = bstack1ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡧࡦࡰࡨࡶ࡮ࡩ࠮ࡺ࡯࡯࠲ࡸࡧ࡭ࡱ࡮ࡨࠫ୧")
    if bstack1llll11l1_opy_.framework and bstack1llll11l1_opy_.framework not in (bstack1ll_opy_ (u"ࠨࡲࡼࡸ࡭ࡵ࡮ࠨ୨"), bstack1ll_opy_ (u"ࠩࡳࡽࡹ࡮࡯࡯࠵ࠪ୩")):
      bstack111l11ll1_opy_ = bstack1ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡩࡶࡦࡳࡥࡸࡱࡵ࡯࠳ࡿ࡭࡭࠰ࡶࡥࡲࡶ࡬ࡦࠩ୪")
    bstack11ll1lll1_opy_ = os.path.join(os.path.dirname(os.path.realpath(__file__)), bstack111l11ll1_opy_)
    bstack1lll1lllll_opy_ = open(bstack11ll1lll1_opy_, bstack1ll_opy_ (u"ࠫࡷ࠭୫"))
    bstack1l1l11l1_opy_ = bstack1lll1lllll_opy_.read()
    bstack1lll1lllll_opy_.close()
    if bstack1llll11l1_opy_.username:
      bstack1l1l11l1_opy_ = bstack1l1l11l1_opy_.replace(bstack1ll_opy_ (u"ࠬ࡟ࡏࡖࡔࡢ࡙ࡘࡋࡒࡏࡃࡐࡉࠬ୬"), bstack1llll11l1_opy_.username)
    if bstack1llll11l1_opy_.key:
      bstack1l1l11l1_opy_ = bstack1l1l11l1_opy_.replace(bstack1ll_opy_ (u"࡙࠭ࡐࡗࡕࡣࡆࡉࡃࡆࡕࡖࡣࡐࡋ࡙ࠨ୭"), bstack1llll11l1_opy_.key)
    if bstack1llll11l1_opy_.framework:
      bstack1l1l11l1_opy_ = bstack1l1l11l1_opy_.replace(bstack1ll_opy_ (u"࡚ࠧࡑࡘࡖࡤࡌࡒࡂࡏࡈ࡛ࡔࡘࡋࠨ୮"), bstack1llll11l1_opy_.framework)
    file_name = bstack1ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡺ࡯࡯ࠫ୯")
    file_path = os.path.abspath(file_name)
    bstack1l111lll_opy_ = open(file_path, bstack1ll_opy_ (u"ࠩࡺࠫ୰"))
    bstack1l111lll_opy_.write(bstack1l1l11l1_opy_)
    bstack1l111lll_opy_.close()
    logger.info(bstack111ll1l11_opy_)
    try:
      os.environ[bstack1ll_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡉࡖࡆࡓࡅࡘࡑࡕࡏࠬୱ")] = bstack1llll11l1_opy_.framework if bstack1llll11l1_opy_.framework != None else bstack1ll_opy_ (u"ࠦࠧ୲")
      config = yaml.safe_load(bstack1l1l11l1_opy_)
      config[bstack1ll_opy_ (u"ࠬࡹ࡯ࡶࡴࡦࡩࠬ୳")] = bstack1ll_opy_ (u"࠭ࡰࡺࡶ࡫ࡳࡳ࠳ࡳࡦࡶࡸࡴࠬ୴")
      bstack111llll11_opy_(bstack111111111_opy_, config)
    except Exception as e:
      logger.debug(bstack1ll1l11lll_opy_.format(str(e)))
  except Exception as e:
    logger.error(bstack11l1ll111_opy_.format(str(e)))
def bstack111llll11_opy_(bstack1l1l11ll_opy_, config, bstack1ll1l111l1_opy_={}):
  global bstack1lll1l11l_opy_
  global bstack11111l1ll_opy_
  if not config:
    return
  bstack1ll1111ll1_opy_ = bstack1ll111llll_opy_ if not bstack1lll1l11l_opy_ else (
    bstack1l11ll1l_opy_ if bstack1ll_opy_ (u"ࠧࡢࡲࡳࠫ୵") in config else bstack1l1llll1l_opy_)
  data = {
    bstack1ll_opy_ (u"ࠨࡷࡶࡩࡷࡔࡡ࡮ࡧࠪ୶"): config[bstack1ll_opy_ (u"ࠩࡸࡷࡪࡸࡎࡢ࡯ࡨࠫ୷")],
    bstack1ll_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵࡎࡩࡾ࠭୸"): config[bstack1ll_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶࡏࡪࡿࠧ୹")],
    bstack1ll_opy_ (u"ࠬ࡫ࡶࡦࡰࡷࡣࡹࡿࡰࡦࠩ୺"): bstack1l1l11ll_opy_,
    bstack1ll_opy_ (u"࠭ࡤࡦࡶࡨࡧࡹ࡫ࡤࡇࡴࡤࡱࡪࡽ࡯ࡳ࡭ࠪ୻"): os.environ.get(bstack1ll_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡆࡓࡃࡐࡉ࡜ࡕࡒࡌࠩ୼"), bstack11111l1ll_opy_),
    bstack1ll_opy_ (u"ࠨࡤࡸ࡭ࡱࡪ࡟ࡩࡣࡶ࡬ࡪࡪ࡟ࡪࡦࠪ୽"): bstack11ll1l111_opy_,
    bstack1ll_opy_ (u"ࠩࡲࡴࡹ࡯࡭ࡢ࡮ࡢ࡬ࡺࡨ࡟ࡶࡴ࡯ࠫ୾"): bstack11llll11l_opy_(),
    bstack1ll_opy_ (u"ࠪࡩࡻ࡫࡮ࡵࡡࡳࡶࡴࡶࡥࡳࡶ࡬ࡩࡸ࠭୿"): {
      bstack1ll_opy_ (u"ࠫࡱࡧ࡮ࡨࡷࡤ࡫ࡪࡥࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࠩ஀"): str(config[bstack1ll_opy_ (u"ࠬࡹ࡯ࡶࡴࡦࡩࠬ஁")]) if bstack1ll_opy_ (u"࠭ࡳࡰࡷࡵࡧࡪ࠭ஂ") in config else bstack1ll_opy_ (u"ࠢࡶࡰ࡮ࡲࡴࡽ࡮ࠣஃ"),
      bstack1ll_opy_ (u"ࠨࡴࡨࡪࡪࡸࡲࡦࡴࠪ஄"): bstack1ll11111ll_opy_(os.getenv(bstack1ll_opy_ (u"ࠤࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡈࡕࡅࡒࡋࡗࡐࡔࡎࠦஅ"), bstack1ll_opy_ (u"ࠥࠦஆ"))),
      bstack1ll_opy_ (u"ࠫࡱࡧ࡮ࡨࡷࡤ࡫ࡪ࠭இ"): bstack1ll_opy_ (u"ࠬࡶࡹࡵࡪࡲࡲࠬஈ"),
      bstack1ll_opy_ (u"࠭ࡰࡳࡱࡧࡹࡨࡺࠧஉ"): bstack1ll1111ll1_opy_,
      bstack1ll_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡔࡡ࡮ࡧࠪஊ"): config[bstack1ll_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡎࡢ࡯ࡨࠫ஋")] if config[bstack1ll_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠬ஌")] else bstack1ll_opy_ (u"ࠥࡹࡳࡱ࡮ࡰࡹࡱࠦ஍"),
      bstack1ll_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭எ"): str(config[bstack1ll_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧஏ")]) if bstack1ll_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨஐ") in config else bstack1ll_opy_ (u"ࠢࡶࡰ࡮ࡲࡴࡽ࡮ࠣ஑"),
      bstack1ll_opy_ (u"ࠨࡱࡶࠫஒ"): sys.platform,
      bstack1ll_opy_ (u"ࠩ࡫ࡳࡸࡺ࡮ࡢ࡯ࡨࠫஓ"): socket.gethostname()
    }
  }
  update(data[bstack1ll_opy_ (u"ࠪࡩࡻ࡫࡮ࡵࡡࡳࡶࡴࡶࡥࡳࡶ࡬ࡩࡸ࠭ஔ")], bstack1ll1l111l1_opy_)
  try:
    response = bstack1llll1l11l_opy_(bstack1ll_opy_ (u"ࠫࡕࡕࡓࡕࠩக"), bstack1lll1ll1l1_opy_(bstack1l1l1l11l_opy_), data, {
      bstack1ll_opy_ (u"ࠬࡧࡵࡵࡪࠪ஖"): (config[bstack1ll_opy_ (u"࠭ࡵࡴࡧࡵࡒࡦࡳࡥࠨ஗")], config[bstack1ll_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡋࡦࡻࠪ஘")])
    })
    if response:
      logger.debug(bstack1lll1l1l1_opy_.format(bstack1l1l11ll_opy_, str(response.json())))
  except Exception as e:
    logger.debug(bstack1l1l1l1ll_opy_.format(str(e)))
def bstack1ll11111ll_opy_(framework):
  return bstack1ll_opy_ (u"ࠣࡽࢀ࠱ࡵࡿࡴࡩࡱࡱࡥ࡬࡫࡮ࡵ࠱ࡾࢁࠧங").format(str(framework), __version__) if framework else bstack1ll_opy_ (u"ࠤࡳࡽࡹ࡮࡯࡯ࡣࡪࡩࡳࡺ࠯ࡼࡿࠥச").format(
    __version__)
def bstack1ll1ll111l_opy_():
  global CONFIG
  if bool(CONFIG):
    return
  try:
    bstack1l11lll1l_opy_()
    logger.debug(bstack1l1ll1111_opy_.format(str(CONFIG)))
    bstack1llll11l11_opy_()
    bstack11l1lll11_opy_()
  except Exception as e:
    logger.error(bstack1ll_opy_ (u"ࠥࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡳࡦࡶࡸࡴ࠱ࠦࡥࡳࡴࡲࡶ࠿ࠦࠢ஛") + str(e))
    sys.exit(1)
  sys.excepthook = bstack1l111l1l_opy_
  atexit.register(bstack1ll1l1ll1l_opy_)
  signal.signal(signal.SIGINT, bstack1lllll1lll_opy_)
  signal.signal(signal.SIGTERM, bstack1lllll1lll_opy_)
def bstack1l111l1l_opy_(exctype, value, traceback):
  global bstack11l1l1l1l_opy_
  try:
    for driver in bstack11l1l1l1l_opy_:
      driver.execute_script(
        bstack1ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻࠣࡣࡦࡸ࡮ࡵ࡮ࠣ࠼ࠣࠦࡸ࡫ࡴࡔࡧࡶࡷ࡮ࡵ࡮ࡔࡶࡤࡸࡺࡹࠢ࠭ࠢࠥࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸࠨ࠺ࠡࡽࠥࡷࡹࡧࡴࡶࡵࠥ࠾ࠧ࡬ࡡࡪ࡮ࡨࡨࠧ࠲ࠠࠣࡴࡨࡥࡸࡵ࡮ࠣ࠼ࠣࠫஜ") + json.dumps(
          bstack1ll_opy_ (u"࡙ࠧࡥࡴࡵ࡬ࡳࡳࠦࡦࡢ࡫࡯ࡩࡩࠦࡷࡪࡶ࡫࠾ࠥࡢ࡮ࠣ஝") + str(value)) + bstack1ll_opy_ (u"࠭ࡽࡾࠩஞ"))
  except Exception:
    pass
  bstack1l1ll1l11_opy_(value)
  sys.__excepthook__(exctype, value, traceback)
  sys.exit(1)
def bstack1l1ll1l11_opy_(message=bstack1ll_opy_ (u"ࠧࠨட")):
  global CONFIG
  try:
    if message:
      bstack1ll1l111l1_opy_ = {
        bstack1ll_opy_ (u"ࠨࡧࡵࡶࡴࡸࠧ஠"): str(message)
      }
      bstack111llll11_opy_(bstack1lll11l1ll_opy_, CONFIG, bstack1ll1l111l1_opy_)
    else:
      bstack111llll11_opy_(bstack1lll11l1ll_opy_, CONFIG)
  except Exception as e:
    logger.debug(bstack1ll1llll1l_opy_.format(str(e)))
def bstack11ll111ll_opy_(bstack1ll1l1l111_opy_, size):
  bstack1ll1ll1l_opy_ = []
  while len(bstack1ll1l1l111_opy_) > size:
    bstack11111l11_opy_ = bstack1ll1l1l111_opy_[:size]
    bstack1ll1ll1l_opy_.append(bstack11111l11_opy_)
    bstack1ll1l1l111_opy_ = bstack1ll1l1l111_opy_[size:]
  bstack1ll1ll1l_opy_.append(bstack1ll1l1l111_opy_)
  return bstack1ll1ll1l_opy_
def bstack1lll1llll1_opy_(args):
  if bstack1ll_opy_ (u"ࠩ࠰ࡱࠬ஡") in args and bstack1ll_opy_ (u"ࠪࡴࡩࡨࠧ஢") in args:
    return True
  return False
def run_on_browserstack(bstack1llll1lll1_opy_=None, bstack1l11l1l11_opy_=None, bstack111ll11ll_opy_=False):
  global CONFIG
  global bstack1l111l111_opy_
  global bstack1l11l11ll_opy_
  global bstack11111l1ll_opy_
  bstack1111l1ll_opy_ = bstack1ll_opy_ (u"ࠫࠬண")
  bstack11111l11l_opy_(bstack1llll1111l_opy_, logger)
  if bstack1llll1lll1_opy_ and isinstance(bstack1llll1lll1_opy_, str):
    bstack1llll1lll1_opy_ = eval(bstack1llll1lll1_opy_)
  if bstack1llll1lll1_opy_:
    CONFIG = bstack1llll1lll1_opy_[bstack1ll_opy_ (u"ࠬࡉࡏࡏࡈࡌࡋࠬத")]
    bstack1l111l111_opy_ = bstack1llll1lll1_opy_[bstack1ll_opy_ (u"࠭ࡈࡖࡄࡢ࡙ࡗࡒࠧ஥")]
    bstack1l11l11ll_opy_ = bstack1llll1lll1_opy_[bstack1ll_opy_ (u"ࠧࡊࡕࡢࡅࡕࡖ࡟ࡂࡗࡗࡓࡒࡇࡔࡆࠩ஦")]
    bstack1lll1l1lll_opy_.bstack1l1l111ll_opy_(bstack1ll_opy_ (u"ࠨࡋࡖࡣࡆࡖࡐࡠࡃࡘࡘࡔࡓࡁࡕࡇࠪ஧"), bstack1l11l11ll_opy_)
    bstack1111l1ll_opy_ = bstack1ll_opy_ (u"ࠩࡳࡽࡹ࡮࡯࡯ࠩந")
  if not bstack111ll11ll_opy_:
    if len(sys.argv) <= 1:
      logger.critical(bstack1l11lll1_opy_)
      return
    if sys.argv[1] == bstack1ll_opy_ (u"ࠪ࠱࠲ࡼࡥࡳࡵ࡬ࡳࡳ࠭ன") or sys.argv[1] == bstack1ll_opy_ (u"ࠫ࠲ࡼࠧப"):
      logger.info(bstack1ll_opy_ (u"ࠬࡈࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠤࡕࡿࡴࡩࡱࡱࠤࡘࡊࡋࠡࡸࡾࢁࠬ஫").format(__version__))
      return
    if sys.argv[1] == bstack1ll_opy_ (u"࠭ࡳࡦࡶࡸࡴࠬ஬"):
      bstack1ll11111_opy_()
      return
  args = sys.argv
  bstack1ll1ll111l_opy_()
  global bstack11lllll1l_opy_
  global bstack111111ll_opy_
  global bstack1lllllll11_opy_
  global bstack1l1lllll1_opy_
  global bstack1l1111ll_opy_
  global bstack11ll1l1l_opy_
  global bstack11lllllll_opy_
  global bstack11l1l1111_opy_
  global bstack1l111l11l_opy_
  if not bstack1111l1ll_opy_:
    if args[1] == bstack1ll_opy_ (u"ࠧࡱࡻࡷ࡬ࡴࡴࠧ஭") or args[1] == bstack1ll_opy_ (u"ࠨࡲࡼࡸ࡭ࡵ࡮࠴ࠩம"):
      bstack1111l1ll_opy_ = bstack1ll_opy_ (u"ࠩࡳࡽࡹ࡮࡯࡯ࠩய")
      args = args[2:]
    elif args[1] == bstack1ll_opy_ (u"ࠪࡶࡴࡨ࡯ࡵࠩர"):
      bstack1111l1ll_opy_ = bstack1ll_opy_ (u"ࠫࡷࡵࡢࡰࡶࠪற")
      args = args[2:]
    elif args[1] == bstack1ll_opy_ (u"ࠬࡶࡡࡣࡱࡷࠫல"):
      bstack1111l1ll_opy_ = bstack1ll_opy_ (u"࠭ࡰࡢࡤࡲࡸࠬள")
      args = args[2:]
    elif args[1] == bstack1ll_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠳ࡩ࡯ࡶࡨࡶࡳࡧ࡬ࠨழ"):
      bstack1111l1ll_opy_ = bstack1ll_opy_ (u"ࠨࡴࡲࡦࡴࡺ࠭ࡪࡰࡷࡩࡷࡴࡡ࡭ࠩவ")
      args = args[2:]
    elif args[1] == bstack1ll_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࠩஶ"):
      bstack1111l1ll_opy_ = bstack1ll_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࠪஷ")
      args = args[2:]
    elif args[1] == bstack1ll_opy_ (u"ࠫࡧ࡫ࡨࡢࡸࡨࠫஸ"):
      bstack1111l1ll_opy_ = bstack1ll_opy_ (u"ࠬࡨࡥࡩࡣࡹࡩࠬஹ")
      args = args[2:]
    else:
      if not bstack1ll_opy_ (u"࠭ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࠩ஺") in CONFIG or str(CONFIG[bstack1ll_opy_ (u"ࠧࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࠪ஻")]).lower() in [bstack1ll_opy_ (u"ࠨࡲࡼࡸ࡭ࡵ࡮ࠨ஼"), bstack1ll_opy_ (u"ࠩࡳࡽࡹ࡮࡯࡯࠵ࠪ஽")]:
        bstack1111l1ll_opy_ = bstack1ll_opy_ (u"ࠪࡴࡾࡺࡨࡰࡰࠪா")
        args = args[1:]
      elif str(CONFIG[bstack1ll_opy_ (u"ࠫ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱࠧி")]).lower() == bstack1ll_opy_ (u"ࠬࡸ࡯ࡣࡱࡷࠫீ"):
        bstack1111l1ll_opy_ = bstack1ll_opy_ (u"࠭ࡲࡰࡤࡲࡸࠬு")
        args = args[1:]
      elif str(CONFIG[bstack1ll_opy_ (u"ࠧࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࠪூ")]).lower() == bstack1ll_opy_ (u"ࠨࡲࡤࡦࡴࡺࠧ௃"):
        bstack1111l1ll_opy_ = bstack1ll_opy_ (u"ࠩࡳࡥࡧࡵࡴࠨ௄")
        args = args[1:]
      elif str(CONFIG[bstack1ll_opy_ (u"ࠪࡪࡷࡧ࡭ࡦࡹࡲࡶࡰ࠭௅")]).lower() == bstack1ll_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࠫெ"):
        bstack1111l1ll_opy_ = bstack1ll_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬே")
        args = args[1:]
      elif str(CONFIG[bstack1ll_opy_ (u"࠭ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࠩை")]).lower() == bstack1ll_opy_ (u"ࠧࡣࡧ࡫ࡥࡻ࡫ࠧ௉"):
        bstack1111l1ll_opy_ = bstack1ll_opy_ (u"ࠨࡤࡨ࡬ࡦࡼࡥࠨொ")
        args = args[1:]
      else:
        os.environ[bstack1ll_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡈࡕࡅࡒࡋࡗࡐࡔࡎࠫோ")] = bstack1111l1ll_opy_
        bstack11l1l1l11_opy_(bstack1lll1l111_opy_)
  bstack11111l1ll_opy_ = bstack1111l1ll_opy_
  global bstack1ll11ll1ll_opy_
  if bstack1llll1lll1_opy_:
    try:
      os.environ[bstack1ll_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡉࡖࡆࡓࡅࡘࡑࡕࡏࠬௌ")] = bstack1111l1ll_opy_
      bstack111llll11_opy_(bstack1ll1ll11_opy_, CONFIG)
    except Exception as e:
      logger.debug(bstack1ll1llll1l_opy_.format(str(e)))
  global bstack11ll11ll1_opy_
  global bstack111ll1ll_opy_
  global bstack1l111111_opy_
  global bstack1ll1l1l1_opy_
  global bstack1ll1l1llll_opy_
  global bstack1lll1l1ll1_opy_
  global bstack1lll111l1_opy_
  global bstack111l1l111_opy_
  global bstack11lll11ll_opy_
  global bstack1ll111l11l_opy_
  global bstack1l1l11ll1_opy_
  global bstack1llll1ll_opy_
  global bstack11ll11ll_opy_
  global bstack1l1111lll_opy_
  global bstack1ll1111l1_opy_
  global bstack1llllll111_opy_
  global bstack11l111lll_opy_
  global bstack1ll111l1l1_opy_
  global bstack11111111l_opy_
  try:
    from selenium import webdriver
    from selenium.webdriver.remote.webdriver import WebDriver
    bstack11ll11ll1_opy_ = webdriver.Remote.__init__
    bstack111ll1ll_opy_ = WebDriver.quit
    bstack1l1l11ll1_opy_ = WebDriver.close
    bstack1l1111lll_opy_ = WebDriver.get
  except Exception as e:
    pass
  try:
    import Browser
    from subprocess import Popen
    bstack1ll11ll1ll_opy_ = Popen.__init__
  except Exception as e:
    pass
  if bstack1lll11lll_opy_(CONFIG) and bstack111ll111l_opy_():
    if bstack1l1lllllll_opy_() < version.parse(bstack11l1111l_opy_):
      logger.error(bstack11ll1111l_opy_.format(bstack1l1lllllll_opy_()))
    else:
      try:
        from selenium.webdriver.remote.remote_connection import RemoteConnection
        bstack1ll1111l1_opy_ = RemoteConnection._get_proxy_url
      except Exception as e:
        logger.error(bstack111l1llll_opy_.format(str(e)))
  if bstack1111l1ll_opy_ != bstack1ll_opy_ (u"ࠫࡵࡿࡴࡩࡱࡱ்ࠫ") or (bstack1111l1ll_opy_ == bstack1ll_opy_ (u"ࠬࡶࡹࡵࡪࡲࡲࠬ௎") and not bstack1llll1lll1_opy_):
    bstack1ll11l11ll_opy_()
  if (bstack1111l1ll_opy_ in [bstack1ll_opy_ (u"࠭ࡰࡢࡤࡲࡸࠬ௏"), bstack1ll_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠭ௐ"), bstack1ll_opy_ (u"ࠨࡴࡲࡦࡴࡺ࠭ࡪࡰࡷࡩࡷࡴࡡ࡭ࠩ௑")]):
    try:
      from robot import run_cli
      from robot.output import Output
      from robot.running.status import TestStatus
      from pabot.pabot import QueueItem
      from pabot import pabot
      try:
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCreator
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCache
        WebDriverCreator._get_ff_profile = bstack1ll111l1ll_opy_
        bstack1ll1l1llll_opy_ = WebDriverCache.close
      except Exception as e:
        logger.warn(bstack111ll1l1l_opy_ + str(e))
      try:
        from AppiumLibrary.utils.applicationcache import ApplicationCache
        bstack1ll1l1l1_opy_ = ApplicationCache.close
      except Exception as e:
        logger.debug(bstack111lll11_opy_ + str(e))
    except Exception as e:
      bstack11111l1l_opy_(e, bstack111ll1l1l_opy_)
    if bstack1111l1ll_opy_ != bstack1ll_opy_ (u"ࠩࡵࡳࡧࡵࡴ࠮࡫ࡱࡸࡪࡸ࡮ࡢ࡮ࠪ௒"):
      bstack1ll111111_opy_()
    bstack1l111111_opy_ = Output.end_test
    bstack1lll1l1ll1_opy_ = TestStatus.__init__
    bstack111l1l111_opy_ = pabot._run
    bstack11lll11ll_opy_ = QueueItem.__init__
    bstack1ll111l11l_opy_ = pabot._create_command_for_execution
    bstack1ll111l1l1_opy_ = pabot._report_results
  if bstack1111l1ll_opy_ == bstack1ll_opy_ (u"ࠪࡦࡪ࡮ࡡࡷࡧࠪ௓"):
    try:
      from behave.runner import Runner
      from behave.model import Step
    except Exception as e:
      bstack11111l1l_opy_(e, bstack1ll1l1111l_opy_)
    bstack1llll1ll_opy_ = Runner.run_hook
    bstack11ll11ll_opy_ = Step.run
  if bstack1ll_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࡓࡵࡺࡩࡰࡰࡶࠫ௔") in CONFIG:
    os.environ[bstack1ll_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡡࡄࡇࡈࡋࡓࡔࡋࡅࡍࡑࡏࡔ࡚ࡡࡆࡓࡓࡌࡉࡈࡗࡕࡅ࡙ࡏࡏࡏࡡ࡜ࡑࡑ࠭௕")] = json.dumps(CONFIG[bstack1ll_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࡕࡰࡵ࡫ࡲࡲࡸ࠭௖")])
    CONFIG[bstack1ll_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࡏࡱࡶ࡬ࡳࡳࡹࠧௗ")].pop(bstack1ll_opy_ (u"ࠨ࡫ࡱࡧࡱࡻࡤࡦࡖࡤ࡫ࡸࡏ࡮ࡕࡧࡶࡸ࡮ࡴࡧࡔࡥࡲࡴࡪ࠭௘"), None)
    CONFIG[bstack1ll_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࡑࡳࡸ࡮ࡵ࡮ࡴࠩ௙")].pop(bstack1ll_opy_ (u"ࠪࡩࡽࡩ࡬ࡶࡦࡨࡘࡦ࡭ࡳࡊࡰࡗࡩࡸࡺࡩ࡯ࡩࡖࡧࡴࡶࡥࠨ௚"), None)
  if bstack1111l1ll_opy_ == bstack1ll_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࠫ௛"):
    try:
      bstack11l1l1l1_opy_.launch(CONFIG, {
        bstack1ll_opy_ (u"ࠬ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡰࡤࡱࡪ࠭௜"): bstack1ll_opy_ (u"࠭ࡐࡺࡶࡨࡷࡹ࠳ࡣࡶࡥࡸࡱࡧ࡫ࡲࠨ௝") if bstack1ll1ll11l1_opy_() else bstack1ll_opy_ (u"ࠧࡑࡻࡷࡩࡸࡺࠧ௞"),
        bstack1ll_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬ௟"): bstack1ll1l1l1l_opy_.version(),
        bstack1ll_opy_ (u"ࠩࡶࡨࡰࡥࡶࡦࡴࡶ࡭ࡴࡴࠧ௠"): __version__
      })
      if bstack1lll1l11l_opy_ and bstack1lll1ll1_opy_.bstack1l1lll1l1_opy_(CONFIG):
        bstack11lll111l_opy_, bstack1llll1l1ll_opy_ = bstack1lll1ll1_opy_.bstack1l1l1llll_opy_(CONFIG, bstack1111l1ll_opy_, bstack1ll1l1l1l_opy_.version());
        if not bstack11lll111l_opy_ is None:
          os.environ[bstack1ll_opy_ (u"ࠪࡆࡘࡥࡁ࠲࠳࡜ࡣࡏ࡝ࡔࠨ௡")] = bstack11lll111l_opy_;
          os.environ[bstack1ll_opy_ (u"ࠫࡇ࡙࡟ࡂ࠳࠴࡝ࡤ࡚ࡅࡔࡖࡢࡖ࡚ࡔ࡟ࡊࡆࠪ௢")] = str(bstack1llll1l1ll_opy_);
      from _pytest.config import Config
      bstack1llllll111_opy_ = Config.getoption
      from _pytest import runner
      bstack11l111lll_opy_ = runner._update_current_test_var
    except Exception as e:
      logger.warn(e, bstack1ll1lll1_opy_)
    try:
      from pytest_bdd import reporting
      bstack11111111l_opy_ = reporting.runtest_makereport
    except Exception as e:
      logger.debug(bstack1ll_opy_ (u"ࠬࡖ࡬ࡦࡣࡶࡩࠥ࡯࡮ࡴࡶࡤࡰࡱࠦࡰࡺࡶࡨࡷࡹ࠳ࡢࡥࡦࠣࡸࡴࠦࡲࡶࡰࠣࡴࡾࡺࡥࡴࡶ࠰ࡦࡩࡪࠠࡵࡧࡶࡸࡸ࠭௣"))
  if bstack1111l1ll_opy_ == bstack1ll_opy_ (u"࠭ࡰࡺࡶ࡫ࡳࡳ࠭௤"):
    bstack111111ll_opy_ = True
    if bstack1llll1lll1_opy_ and bstack111ll11ll_opy_:
      bstack1l1111ll_opy_ = CONFIG.get(bstack1ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫ௥"), {}).get(bstack1ll_opy_ (u"ࠨ࡮ࡲࡧࡦࡲࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪ௦"))
      bstack1ll111ll11_opy_(bstack1l1lllll_opy_)
    elif bstack1llll1lll1_opy_:
      bstack1l1111ll_opy_ = CONFIG.get(bstack1ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࡍࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭௧"), {}).get(bstack1ll_opy_ (u"ࠪࡰࡴࡩࡡ࡭ࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬ௨"))
      global bstack11l1l1l1l_opy_
      try:
        if bstack1lll1llll1_opy_(bstack1llll1lll1_opy_[bstack1ll_opy_ (u"ࠫ࡫࡯࡬ࡦࡡࡱࡥࡲ࡫ࠧ௩")]) and multiprocessing.current_process().name == bstack1ll_opy_ (u"ࠬ࠶ࠧ௪"):
          bstack1llll1lll1_opy_[bstack1ll_opy_ (u"࠭ࡦࡪ࡮ࡨࡣࡳࡧ࡭ࡦࠩ௫")].remove(bstack1ll_opy_ (u"ࠧ࠮࡯ࠪ௬"))
          bstack1llll1lll1_opy_[bstack1ll_opy_ (u"ࠨࡨ࡬ࡰࡪࡥ࡮ࡢ࡯ࡨࠫ௭")].remove(bstack1ll_opy_ (u"ࠩࡳࡨࡧ࠭௮"))
          bstack1llll1lll1_opy_[bstack1ll_opy_ (u"ࠪࡪ࡮ࡲࡥࡠࡰࡤࡱࡪ࠭௯")] = bstack1llll1lll1_opy_[bstack1ll_opy_ (u"ࠫ࡫࡯࡬ࡦࡡࡱࡥࡲ࡫ࠧ௰")][0]
          with open(bstack1llll1lll1_opy_[bstack1ll_opy_ (u"ࠬ࡬ࡩ࡭ࡧࡢࡲࡦࡳࡥࠨ௱")], bstack1ll_opy_ (u"࠭ࡲࠨ௲")) as f:
            bstack1l11ll11_opy_ = f.read()
          bstack1lll1l1111_opy_ = bstack1ll_opy_ (u"ࠢࠣࠤࡩࡶࡴࡳࠠࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡳࡥ࡭ࠣ࡭ࡲࡶ࡯ࡳࡶࠣࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡ࡬ࡲ࡮ࡺࡩࡢ࡮࡬ࡾࡪࡁࠠࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡩ࡯࡫ࡷ࡭ࡦࡲࡩࡻࡧࠫࡿࢂ࠯࠻ࠡࡨࡵࡳࡲࠦࡰࡥࡤࠣ࡭ࡲࡶ࡯ࡳࡶࠣࡔࡩࡨ࠻ࠡࡱࡪࡣࡩࡨࠠ࠾ࠢࡓࡨࡧ࠴ࡤࡰࡡࡥࡶࡪࡧ࡫࠼ࠌࡧࡩ࡫ࠦ࡭ࡰࡦࡢࡦࡷ࡫ࡡ࡬ࠪࡶࡩࡱ࡬ࠬࠡࡣࡵ࡫࠱ࠦࡴࡦ࡯ࡳࡳࡷࡧࡲࡺࠢࡀࠤ࠵࠯࠺ࠋࠢࠣࡸࡷࡿ࠺ࠋࠢࠣࠤࠥࡧࡲࡨࠢࡀࠤࡸࡺࡲࠩ࡫ࡱࡸ࠭ࡧࡲࡨࠫ࠮࠵࠵࠯ࠊࠡࠢࡨࡼࡨ࡫ࡰࡵࠢࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥࡧࡳࠡࡧ࠽ࠎࠥࠦࠠࠡࡲࡤࡷࡸࠐࠠࠡࡱࡪࡣࡩࡨࠨࡴࡧ࡯ࡪ࠱ࡧࡲࡨ࠮ࡷࡩࡲࡶ࡯ࡳࡣࡵࡽ࠮ࠐࡐࡥࡤ࠱ࡨࡴࡥࡢࠡ࠿ࠣࡱࡴࡪ࡟ࡣࡴࡨࡥࡰࠐࡐࡥࡤ࠱ࡨࡴࡥࡢࡳࡧࡤ࡯ࠥࡃࠠ࡮ࡱࡧࡣࡧࡸࡥࡢ࡭ࠍࡔࡩࡨࠨࠪ࠰ࡶࡩࡹࡥࡴࡳࡣࡦࡩ࠭࠯࡜࡯ࠤࠥࠦ௳").format(str(bstack1llll1lll1_opy_))
          bstack11ll111l_opy_ = bstack1lll1l1111_opy_ + bstack1l11ll11_opy_
          bstack1lll1l11ll_opy_ = bstack1llll1lll1_opy_[bstack1ll_opy_ (u"ࠨࡨ࡬ࡰࡪࡥ࡮ࡢ࡯ࡨࠫ௴")] + bstack1ll_opy_ (u"ࠩࡢࡦࡸࡺࡡࡤ࡭ࡢࡸࡪࡳࡰ࠯ࡲࡼࠫ௵")
          with open(bstack1lll1l11ll_opy_, bstack1ll_opy_ (u"ࠪࡻࠬ௶")):
            pass
          with open(bstack1lll1l11ll_opy_, bstack1ll_opy_ (u"ࠦࡼ࠱ࠢ௷")) as f:
            f.write(bstack11ll111l_opy_)
          import subprocess
          bstack1l1111111_opy_ = subprocess.run([bstack1ll_opy_ (u"ࠧࡶࡹࡵࡪࡲࡲࠧ௸"), bstack1lll1l11ll_opy_])
          if os.path.exists(bstack1lll1l11ll_opy_):
            os.unlink(bstack1lll1l11ll_opy_)
          os._exit(bstack1l1111111_opy_.returncode)
        else:
          if bstack1lll1llll1_opy_(bstack1llll1lll1_opy_[bstack1ll_opy_ (u"࠭ࡦࡪ࡮ࡨࡣࡳࡧ࡭ࡦࠩ௹")]):
            bstack1llll1lll1_opy_[bstack1ll_opy_ (u"ࠧࡧ࡫࡯ࡩࡤࡴࡡ࡮ࡧࠪ௺")].remove(bstack1ll_opy_ (u"ࠨ࠯ࡰࠫ௻"))
            bstack1llll1lll1_opy_[bstack1ll_opy_ (u"ࠩࡩ࡭ࡱ࡫࡟࡯ࡣࡰࡩࠬ௼")].remove(bstack1ll_opy_ (u"ࠪࡴࡩࡨࠧ௽"))
            bstack1llll1lll1_opy_[bstack1ll_opy_ (u"ࠫ࡫࡯࡬ࡦࡡࡱࡥࡲ࡫ࠧ௾")] = bstack1llll1lll1_opy_[bstack1ll_opy_ (u"ࠬ࡬ࡩ࡭ࡧࡢࡲࡦࡳࡥࠨ௿")][0]
          bstack1ll111ll11_opy_(bstack1l1lllll_opy_)
          sys.path.append(os.path.dirname(os.path.abspath(bstack1llll1lll1_opy_[bstack1ll_opy_ (u"࠭ࡦࡪ࡮ࡨࡣࡳࡧ࡭ࡦࠩఀ")])))
          sys.argv = sys.argv[2:]
          mod_globals = globals()
          mod_globals[bstack1ll_opy_ (u"ࠧࡠࡡࡱࡥࡲ࡫࡟ࡠࠩఁ")] = bstack1ll_opy_ (u"ࠨࡡࡢࡱࡦ࡯࡮ࡠࡡࠪం")
          mod_globals[bstack1ll_opy_ (u"ࠩࡢࡣ࡫࡯࡬ࡦࡡࡢࠫః")] = os.path.abspath(bstack1llll1lll1_opy_[bstack1ll_opy_ (u"ࠪࡪ࡮ࡲࡥࡠࡰࡤࡱࡪ࠭ఄ")])
          exec(open(bstack1llll1lll1_opy_[bstack1ll_opy_ (u"ࠫ࡫࡯࡬ࡦࡡࡱࡥࡲ࡫ࠧఅ")]).read(), mod_globals)
      except BaseException as e:
        try:
          traceback.print_exc()
          logger.error(bstack1ll_opy_ (u"ࠬࡉࡡࡶࡩ࡫ࡸࠥࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮࠻ࠢࡾࢁࠬఆ").format(str(e)))
          for driver in bstack11l1l1l1l_opy_:
            bstack1l11l1l11_opy_.append({
              bstack1ll_opy_ (u"࠭࡮ࡢ࡯ࡨࠫఇ"): bstack1llll1lll1_opy_[bstack1ll_opy_ (u"ࠧࡧ࡫࡯ࡩࡤࡴࡡ࡮ࡧࠪఈ")],
              bstack1ll_opy_ (u"ࠨࡧࡵࡶࡴࡸࠧఉ"): str(e),
              bstack1ll_opy_ (u"ࠩ࡬ࡲࡩ࡫ࡸࠨఊ"): multiprocessing.current_process().name
            })
            driver.execute_script(
              bstack1ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁࠢࡢࡥࡷ࡭ࡴࡴࠢ࠻ࠢࠥࡷࡪࡺࡓࡦࡵࡶ࡭ࡴࡴࡓࡵࡣࡷࡹࡸࠨࠬࠡࠤࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠧࡀࠠࡼࠤࡶࡸࡦࡺࡵࡴࠤ࠽ࠦ࡫ࡧࡩ࡭ࡧࡧࠦ࠱ࠦࠢࡳࡧࡤࡷࡴࡴࠢ࠻ࠢࠪఋ") + json.dumps(
                bstack1ll_opy_ (u"ࠦࡘ࡫ࡳࡴ࡫ࡲࡲࠥ࡬ࡡࡪ࡮ࡨࡨࠥࡽࡩࡵࡪ࠽ࠤࡡࡴࠢఌ") + str(e)) + bstack1ll_opy_ (u"ࠬࢃࡽࠨ఍"))
        except Exception:
          pass
      finally:
        try:
          for driver in bstack11l1l1l1l_opy_:
            driver.quit()
        except Exception as e:
          pass
    else:
      percy.init(bstack1l11l11ll_opy_, CONFIG, logger)
      bstack11l1l11l1_opy_()
      bstack111lll1l_opy_()
      bstack1111ll11l_opy_ = {
        bstack1ll_opy_ (u"࠭ࡦࡪ࡮ࡨࡣࡳࡧ࡭ࡦࠩఎ"): args[0],
        bstack1ll_opy_ (u"ࠧࡄࡑࡑࡊࡎࡍࠧఏ"): CONFIG,
        bstack1ll_opy_ (u"ࠨࡊࡘࡆࡤ࡛ࡒࡍࠩఐ"): bstack1l111l111_opy_,
        bstack1ll_opy_ (u"ࠩࡌࡗࡤࡇࡐࡑࡡࡄ࡙࡙ࡕࡍࡂࡖࡈࠫ఑"): bstack1l11l11ll_opy_
      }
      percy.bstack1111ll11_opy_()
      if bstack1ll_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ఒ") in CONFIG:
        bstack11l111111_opy_ = []
        manager = multiprocessing.Manager()
        bstack1l1ll1ll_opy_ = manager.list()
        if bstack1lll1llll1_opy_(args):
          for index, platform in enumerate(CONFIG[bstack1ll_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧఓ")]):
            if index == 0:
              bstack1111ll11l_opy_[bstack1ll_opy_ (u"ࠬ࡬ࡩ࡭ࡧࡢࡲࡦࡳࡥࠨఔ")] = args
            bstack11l111111_opy_.append(multiprocessing.Process(name=str(index),
                                                       target=run_on_browserstack,
                                                       args=(bstack1111ll11l_opy_, bstack1l1ll1ll_opy_)))
        else:
          for index, platform in enumerate(CONFIG[bstack1ll_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩక")]):
            bstack11l111111_opy_.append(multiprocessing.Process(name=str(index),
                                                       target=run_on_browserstack,
                                                       args=(bstack1111ll11l_opy_, bstack1l1ll1ll_opy_)))
        for t in bstack11l111111_opy_:
          t.start()
        for t in bstack11l111111_opy_:
          t.join()
        bstack11lllllll_opy_ = list(bstack1l1ll1ll_opy_)
      else:
        if bstack1lll1llll1_opy_(args):
          bstack1111ll11l_opy_[bstack1ll_opy_ (u"ࠧࡧ࡫࡯ࡩࡤࡴࡡ࡮ࡧࠪఖ")] = args
          test = multiprocessing.Process(name=str(0),
                                         target=run_on_browserstack, args=(bstack1111ll11l_opy_,))
          test.start()
          test.join()
        else:
          bstack1ll111ll11_opy_(bstack1l1lllll_opy_)
          sys.path.append(os.path.dirname(os.path.abspath(args[0])))
          mod_globals = globals()
          mod_globals[bstack1ll_opy_ (u"ࠨࡡࡢࡲࡦࡳࡥࡠࡡࠪగ")] = bstack1ll_opy_ (u"ࠩࡢࡣࡲࡧࡩ࡯ࡡࡢࠫఘ")
          mod_globals[bstack1ll_opy_ (u"ࠪࡣࡤ࡬ࡩ࡭ࡧࡢࡣࠬఙ")] = os.path.abspath(args[0])
          sys.argv = sys.argv[2:]
          exec(open(args[0]).read(), mod_globals)
  elif bstack1111l1ll_opy_ == bstack1ll_opy_ (u"ࠫࡵࡧࡢࡰࡶࠪచ") or bstack1111l1ll_opy_ == bstack1ll_opy_ (u"ࠬࡸ࡯ࡣࡱࡷࠫఛ"):
    try:
      from pabot import pabot
    except Exception as e:
      bstack11111l1l_opy_(e, bstack111ll1l1l_opy_)
    bstack11l1l11l1_opy_()
    bstack1ll111ll11_opy_(bstack1l11111ll_opy_)
    if bstack1ll_opy_ (u"࠭࠭࠮ࡲࡵࡳࡨ࡫ࡳࡴࡧࡶࠫజ") in args:
      i = args.index(bstack1ll_opy_ (u"ࠧ࠮࠯ࡳࡶࡴࡩࡥࡴࡵࡨࡷࠬఝ"))
      args.pop(i)
      args.pop(i)
    args.insert(0, str(bstack11lllll1l_opy_))
    args.insert(0, str(bstack1ll_opy_ (u"ࠨ࠯࠰ࡴࡷࡵࡣࡦࡵࡶࡩࡸ࠭ఞ")))
    pabot.main(args)
  elif bstack1111l1ll_opy_ == bstack1ll_opy_ (u"ࠩࡵࡳࡧࡵࡴ࠮࡫ࡱࡸࡪࡸ࡮ࡢ࡮ࠪట"):
    try:
      from robot import run_cli
    except Exception as e:
      bstack11111l1l_opy_(e, bstack111ll1l1l_opy_)
    for a in args:
      if bstack1ll_opy_ (u"ࠪࡆࡘ࡚ࡁࡄࡍࡓࡐࡆ࡚ࡆࡐࡔࡐࡍࡓࡊࡅ࡙ࠩఠ") in a:
        bstack1l1lllll1_opy_ = int(a.split(bstack1ll_opy_ (u"ࠫ࠿࠭డ"))[1])
      if bstack1ll_opy_ (u"ࠬࡈࡓࡕࡃࡆࡏࡉࡋࡆࡍࡑࡆࡅࡑࡏࡄࡆࡐࡗࡍࡋࡏࡅࡓࠩఢ") in a:
        bstack1l1111ll_opy_ = str(a.split(bstack1ll_opy_ (u"࠭࠺ࠨణ"))[1])
      if bstack1ll_opy_ (u"ࠧࡃࡕࡗࡅࡈࡑࡃࡍࡋࡄࡖࡌ࡙ࠧత") in a:
        bstack11ll1l1l_opy_ = str(a.split(bstack1ll_opy_ (u"ࠨ࠼ࠪథ"))[1])
    bstack11ll1l1ll_opy_ = None
    if bstack1ll_opy_ (u"ࠩ࠰࠱ࡧࡹࡴࡢࡥ࡮ࡣ࡮ࡺࡥ࡮ࡡ࡬ࡲࡩ࡫ࡸࠨద") in args:
      i = args.index(bstack1ll_opy_ (u"ࠪ࠱࠲ࡨࡳࡵࡣࡦ࡯ࡤ࡯ࡴࡦ࡯ࡢ࡭ࡳࡪࡥࡹࠩధ"))
      args.pop(i)
      bstack11ll1l1ll_opy_ = args.pop(i)
    if bstack11ll1l1ll_opy_ is not None:
      global bstack11llll1l_opy_
      bstack11llll1l_opy_ = bstack11ll1l1ll_opy_
    bstack1ll111ll11_opy_(bstack1l11111ll_opy_)
    run_cli(args)
    if bstack1ll_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡣࡪࡸࡲࡰࡴࡢࡰ࡮ࡹࡴࠨన") in multiprocessing.current_process().__dict__.keys():
      for bstack11l11lll_opy_ in multiprocessing.current_process().bstack1ll1ll111_opy_:
        bstack1l11l1l11_opy_.append(bstack11l11lll_opy_)
  elif bstack1111l1ll_opy_ == bstack1ll_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬ఩"):
    bstack11lll1l1_opy_ = bstack1ll1l1l1l_opy_(args, logger, CONFIG, bstack1lll1l11l_opy_)
    bstack11lll1l1_opy_.bstack1l1l111l1_opy_()
    bstack11l1l11l1_opy_()
    bstack1lllllll11_opy_ = True
    bstack1l111l11l_opy_ = bstack11lll1l1_opy_.bstack111l11l1l_opy_()
    bstack11lll1l1_opy_.bstack1111ll11l_opy_(bstack1llll1l111_opy_)
    bstack11l1l1111_opy_ = bstack11lll1l1_opy_.bstack1111lllll_opy_(bstack1ll1llll1_opy_, {
      bstack1ll_opy_ (u"࠭ࡈࡖࡄࡢ࡙ࡗࡒࠧప"): bstack1l111l111_opy_,
      bstack1ll_opy_ (u"ࠧࡊࡕࡢࡅࡕࡖ࡟ࡂࡗࡗࡓࡒࡇࡔࡆࠩఫ"): bstack1l11l11ll_opy_,
      bstack1ll_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡂࡗࡗࡓࡒࡇࡔࡊࡑࡑࠫబ"): bstack1lll1l11l_opy_
    })
  elif bstack1111l1ll_opy_ == bstack1ll_opy_ (u"ࠩࡥࡩ࡭ࡧࡶࡦࠩభ"):
    try:
      from behave.__main__ import main as bstack11111ll11_opy_
      from behave.configuration import Configuration
    except Exception as e:
      bstack11111l1l_opy_(e, bstack1ll1l1111l_opy_)
    bstack11l1l11l1_opy_()
    bstack1lllllll11_opy_ = True
    bstack1l1l1lll_opy_ = 1
    if bstack1ll_opy_ (u"ࠪࡴࡦࡸࡡ࡭࡮ࡨࡰࡸࡖࡥࡳࡒ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪమ") in CONFIG:
      bstack1l1l1lll_opy_ = CONFIG[bstack1ll_opy_ (u"ࠫࡵࡧࡲࡢ࡮࡯ࡩࡱࡹࡐࡦࡴࡓࡰࡦࡺࡦࡰࡴࡰࠫయ")]
    bstack11ll1ll1_opy_ = int(bstack1l1l1lll_opy_) * int(len(CONFIG[bstack1ll_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨర")]))
    config = Configuration(args)
    bstack1llllllll1_opy_ = config.paths
    if len(bstack1llllllll1_opy_) == 0:
      import glob
      pattern = bstack1ll_opy_ (u"࠭ࠪࠫ࠱࠭࠲࡫࡫ࡡࡵࡷࡵࡩࠬఱ")
      bstack1lll111l1l_opy_ = glob.glob(pattern, recursive=True)
      args.extend(bstack1lll111l1l_opy_)
      config = Configuration(args)
      bstack1llllllll1_opy_ = config.paths
    bstack1lll111ll1_opy_ = [os.path.normpath(item) for item in bstack1llllllll1_opy_]
    bstack1lll11l1l_opy_ = [os.path.normpath(item) for item in args]
    bstack11llll1ll_opy_ = [item for item in bstack1lll11l1l_opy_ if item not in bstack1lll111ll1_opy_]
    import platform as pf
    if pf.system().lower() == bstack1ll_opy_ (u"ࠧࡸ࡫ࡱࡨࡴࡽࡳࠨల"):
      from pathlib import PureWindowsPath, PurePosixPath
      bstack1lll111ll1_opy_ = [str(PurePosixPath(PureWindowsPath(bstack11l1lll1l_opy_)))
                    for bstack11l1lll1l_opy_ in bstack1lll111ll1_opy_]
    bstack1lll1ll11_opy_ = []
    for spec in bstack1lll111ll1_opy_:
      bstack1l1ll11l1_opy_ = []
      bstack1l1ll11l1_opy_ += bstack11llll1ll_opy_
      bstack1l1ll11l1_opy_.append(spec)
      bstack1lll1ll11_opy_.append(bstack1l1ll11l1_opy_)
    execution_items = []
    for bstack1l1ll11l1_opy_ in bstack1lll1ll11_opy_:
      for index, _ in enumerate(CONFIG[bstack1ll_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫళ")]):
        item = {}
        item[bstack1ll_opy_ (u"ࠩࡤࡶ࡬࠭ఴ")] = bstack1ll_opy_ (u"ࠪࠤࠬవ").join(bstack1l1ll11l1_opy_)
        item[bstack1ll_opy_ (u"ࠫ࡮ࡴࡤࡦࡺࠪశ")] = index
        execution_items.append(item)
    bstack1llll1ll1_opy_ = bstack11ll111ll_opy_(execution_items, bstack11ll1ll1_opy_)
    for execution_item in bstack1llll1ll1_opy_:
      bstack11l111111_opy_ = []
      for item in execution_item:
        bstack11l111111_opy_.append(bstack11lll1111_opy_(name=str(item[bstack1ll_opy_ (u"ࠬ࡯࡮ࡥࡧࡻࠫష")]),
                                             target=bstack11l11111l_opy_,
                                             args=(item[bstack1ll_opy_ (u"࠭ࡡࡳࡩࠪస")],)))
      for t in bstack11l111111_opy_:
        t.start()
      for t in bstack11l111111_opy_:
        t.join()
  else:
    bstack11l1l1l11_opy_(bstack1lll1l111_opy_)
  if not bstack1llll1lll1_opy_:
    bstack11ll1l11l_opy_()
def browserstack_initialize(bstack1llll1llll_opy_=None):
  run_on_browserstack(bstack1llll1llll_opy_, None, True)
def bstack11ll1l11l_opy_():
  global CONFIG
  bstack11l1l1l1_opy_.stop()
  bstack11l1l1l1_opy_.bstack1ll1l1lll1_opy_()
  if bstack1lll1ll1_opy_.bstack1l1lll1l1_opy_(CONFIG):
    bstack1lll1ll1_opy_.bstack1ll11l1ll1_opy_()
  [bstack11l11l11l_opy_, bstack1ll111l111_opy_] = bstack1ll111ll1l_opy_()
  if bstack11l11l11l_opy_ is not None and bstack1ll1l1l1l1_opy_() != -1:
    sessions = bstack111ll1ll1_opy_(bstack11l11l11l_opy_)
    bstack111l1lll_opy_(sessions, bstack1ll111l111_opy_)
def bstack1l11l1l1l_opy_(bstack1111l1l1_opy_):
  if bstack1111l1l1_opy_:
    return bstack1111l1l1_opy_.capitalize()
  else:
    return bstack1111l1l1_opy_
def bstack1l1l1ll1_opy_(bstack11l1ll1l1_opy_):
  if bstack1ll_opy_ (u"ࠧ࡯ࡣࡰࡩࠬహ") in bstack11l1ll1l1_opy_ and bstack11l1ll1l1_opy_[bstack1ll_opy_ (u"ࠨࡰࡤࡱࡪ࠭఺")] != bstack1ll_opy_ (u"ࠩࠪ఻"):
    return bstack11l1ll1l1_opy_[bstack1ll_opy_ (u"ࠪࡲࡦࡳࡥࠨ఼")]
  else:
    bstack1lll11ll1_opy_ = bstack1ll_opy_ (u"ࠦࠧఽ")
    if bstack1ll_opy_ (u"ࠬࡪࡥࡷ࡫ࡦࡩࠬా") in bstack11l1ll1l1_opy_ and bstack11l1ll1l1_opy_[bstack1ll_opy_ (u"࠭ࡤࡦࡸ࡬ࡧࡪ࠭ి")] != None:
      bstack1lll11ll1_opy_ += bstack11l1ll1l1_opy_[bstack1ll_opy_ (u"ࠧࡥࡧࡹ࡭ࡨ࡫ࠧీ")] + bstack1ll_opy_ (u"ࠣ࠮ࠣࠦు")
      if bstack11l1ll1l1_opy_[bstack1ll_opy_ (u"ࠩࡲࡷࠬూ")] == bstack1ll_opy_ (u"ࠥ࡭ࡴࡹࠢృ"):
        bstack1lll11ll1_opy_ += bstack1ll_opy_ (u"ࠦ࡮ࡕࡓࠡࠤౄ")
      bstack1lll11ll1_opy_ += (bstack11l1ll1l1_opy_[bstack1ll_opy_ (u"ࠬࡵࡳࡠࡸࡨࡶࡸ࡯࡯࡯ࠩ౅")] or bstack1ll_opy_ (u"࠭ࠧె"))
      return bstack1lll11ll1_opy_
    else:
      bstack1lll11ll1_opy_ += bstack1l11l1l1l_opy_(bstack11l1ll1l1_opy_[bstack1ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࠨే")]) + bstack1ll_opy_ (u"ࠣࠢࠥై") + (
              bstack11l1ll1l1_opy_[bstack1ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡢࡺࡪࡸࡳࡪࡱࡱࠫ౉")] or bstack1ll_opy_ (u"ࠪࠫొ")) + bstack1ll_opy_ (u"ࠦ࠱ࠦࠢో")
      if bstack11l1ll1l1_opy_[bstack1ll_opy_ (u"ࠬࡵࡳࠨౌ")] == bstack1ll_opy_ (u"ࠨࡗࡪࡰࡧࡳࡼࡹ్ࠢ"):
        bstack1lll11ll1_opy_ += bstack1ll_opy_ (u"ࠢࡘ࡫ࡱࠤࠧ౎")
      bstack1lll11ll1_opy_ += bstack11l1ll1l1_opy_[bstack1ll_opy_ (u"ࠨࡱࡶࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬ౏")] or bstack1ll_opy_ (u"ࠩࠪ౐")
      return bstack1lll11ll1_opy_
def bstack1ll11111l1_opy_(bstack11l111l1l_opy_):
  if bstack11l111l1l_opy_ == bstack1ll_opy_ (u"ࠥࡨࡴࡴࡥࠣ౑"):
    return bstack1ll_opy_ (u"ࠫࡁࡺࡤࠡࡥ࡯ࡥࡸࡹ࠽ࠣࡤࡶࡸࡦࡩ࡫࠮ࡦࡤࡸࡦࠨࠠࡴࡶࡼࡰࡪࡃࠢࡤࡱ࡯ࡳࡷࡀࡧࡳࡧࡨࡲࡀࠨ࠾࠽ࡨࡲࡲࡹࠦࡣࡰ࡮ࡲࡶࡂࠨࡧࡳࡧࡨࡲࠧࡄࡃࡰ࡯ࡳࡰࡪࡺࡥࡥ࠾࠲ࡪࡴࡴࡴ࠿࠾࠲ࡸࡩࡄࠧ౒")
  elif bstack11l111l1l_opy_ == bstack1ll_opy_ (u"ࠧ࡬ࡡࡪ࡮ࡨࡨࠧ౓"):
    return bstack1ll_opy_ (u"࠭࠼ࡵࡦࠣࡧࡱࡧࡳࡴ࠿ࠥࡦࡸࡺࡡࡤ࡭࠰ࡨࡦࡺࡡࠣࠢࡶࡸࡾࡲࡥ࠾ࠤࡦࡳࡱࡵࡲ࠻ࡴࡨࡨࡀࠨ࠾࠽ࡨࡲࡲࡹࠦࡣࡰ࡮ࡲࡶࡂࠨࡲࡦࡦࠥࡂࡋࡧࡩ࡭ࡧࡧࡀ࠴࡬࡯࡯ࡶࡁࡀ࠴ࡺࡤ࠿ࠩ౔")
  elif bstack11l111l1l_opy_ == bstack1ll_opy_ (u"ࠢࡱࡣࡶࡷࡪࡪౕࠢ"):
    return bstack1ll_opy_ (u"ࠨ࠾ࡷࡨࠥࡩ࡬ࡢࡵࡶࡁࠧࡨࡳࡵࡣࡦ࡯࠲ࡪࡡࡵࡣࠥࠤࡸࡺࡹ࡭ࡧࡀࠦࡨࡵ࡬ࡰࡴ࠽࡫ࡷ࡫ࡥ࡯࠽ࠥࡂࡁ࡬࡯࡯ࡶࠣࡧࡴࡲ࡯ࡳ࠿ࠥ࡫ࡷ࡫ࡥ࡯ࠤࡁࡔࡦࡹࡳࡦࡦ࠿࠳࡫ࡵ࡮ࡵࡀ࠿࠳ࡹࡪ࠾ࠨౖ")
  elif bstack11l111l1l_opy_ == bstack1ll_opy_ (u"ࠤࡨࡶࡷࡵࡲࠣ౗"):
    return bstack1ll_opy_ (u"ࠪࡀࡹࡪࠠࡤ࡮ࡤࡷࡸࡃࠢࡣࡵࡷࡥࡨࡱ࠭ࡥࡣࡷࡥࠧࠦࡳࡵࡻ࡯ࡩࡂࠨࡣࡰ࡮ࡲࡶ࠿ࡸࡥࡥ࠽ࠥࡂࡁ࡬࡯࡯ࡶࠣࡧࡴࡲ࡯ࡳ࠿ࠥࡶࡪࡪࠢ࠿ࡇࡵࡶࡴࡸ࠼࠰ࡨࡲࡲࡹࡄ࠼࠰ࡶࡧࡂࠬౘ")
  elif bstack11l111l1l_opy_ == bstack1ll_opy_ (u"ࠦࡹ࡯࡭ࡦࡱࡸࡸࠧౙ"):
    return bstack1ll_opy_ (u"ࠬࡂࡴࡥࠢࡦࡰࡦࡹࡳ࠾ࠤࡥࡷࡹࡧࡣ࡬࠯ࡧࡥࡹࡧࠢࠡࡵࡷࡽࡱ࡫࠽ࠣࡥࡲࡰࡴࡸ࠺ࠤࡧࡨࡥ࠸࠸࠶࠼ࠤࡁࡀ࡫ࡵ࡮ࡵࠢࡦࡳࡱࡵࡲ࠾ࠤࠦࡩࡪࡧ࠳࠳࠸ࠥࡂ࡙࡯࡭ࡦࡱࡸࡸࡁ࠵ࡦࡰࡰࡷࡂࡁ࠵ࡴࡥࡀࠪౚ")
  elif bstack11l111l1l_opy_ == bstack1ll_opy_ (u"ࠨࡲࡶࡰࡱ࡭ࡳ࡭ࠢ౛"):
    return bstack1ll_opy_ (u"ࠧ࠽ࡶࡧࠤࡨࡲࡡࡴࡵࡀࠦࡧࡹࡴࡢࡥ࡮࠱ࡩࡧࡴࡢࠤࠣࡷࡹࡿ࡬ࡦ࠿ࠥࡧࡴࡲ࡯ࡳ࠼ࡥࡰࡦࡩ࡫࠼ࠤࡁࡀ࡫ࡵ࡮ࡵࠢࡦࡳࡱࡵࡲ࠾ࠤࡥࡰࡦࡩ࡫ࠣࡀࡕࡹࡳࡴࡩ࡯ࡩ࠿࠳࡫ࡵ࡮ࡵࡀ࠿࠳ࡹࡪ࠾ࠨ౜")
  else:
    return bstack1ll_opy_ (u"ࠨ࠾ࡷࡨࠥࡧ࡬ࡪࡩࡱࡁࠧࡩࡥ࡯ࡶࡨࡶࠧࠦࡣ࡭ࡣࡶࡷࡂࠨࡢࡴࡶࡤࡧࡰ࠳ࡤࡢࡶࡤࠦࠥࡹࡴࡺ࡮ࡨࡁࠧࡩ࡯࡭ࡱࡵ࠾ࡧࡲࡡࡤ࡭࠾ࠦࡃࡂࡦࡰࡰࡷࠤࡨࡵ࡬ࡰࡴࡀࠦࡧࡲࡡࡤ࡭ࠥࡂࠬౝ") + bstack1l11l1l1l_opy_(
      bstack11l111l1l_opy_) + bstack1ll_opy_ (u"ࠩ࠿࠳࡫ࡵ࡮ࡵࡀ࠿࠳ࡹࡪ࠾ࠨ౞")
def bstack1l11l11l_opy_(session):
  return bstack1ll_opy_ (u"ࠪࡀࡹࡸࠠࡤ࡮ࡤࡷࡸࡃࠢࡣࡵࡷࡥࡨࡱ࠭ࡳࡱࡺࠦࡃࡂࡴࡥࠢࡦࡰࡦࡹࡳ࠾ࠤࡥࡷࡹࡧࡣ࡬࠯ࡧࡥࡹࡧࠠࡴࡧࡶࡷ࡮ࡵ࡮࠮ࡰࡤࡱࡪࠨ࠾࠽ࡣࠣ࡬ࡷ࡫ࡦ࠾ࠤࡾࢁࠧࠦࡴࡢࡴࡪࡩࡹࡃࠢࡠࡤ࡯ࡥࡳࡱࠢ࠿ࡽࢀࡀ࠴ࡧ࠾࠽࠱ࡷࡨࡃࢁࡽࡼࡿ࠿ࡸࡩࠦࡡ࡭࡫ࡪࡲࡂࠨࡣࡦࡰࡷࡩࡷࠨࠠࡤ࡮ࡤࡷࡸࡃࠢࡣࡵࡷࡥࡨࡱ࠭ࡥࡣࡷࡥࠧࡄࡻࡾ࠾࠲ࡸࡩࡄ࠼ࡵࡦࠣࡥࡱ࡯ࡧ࡯࠿ࠥࡧࡪࡴࡴࡦࡴࠥࠤࡨࡲࡡࡴࡵࡀࠦࡧࡹࡴࡢࡥ࡮࠱ࡩࡧࡴࡢࠤࡁࡿࢂࡂ࠯ࡵࡦࡁࡀࡹࡪࠠࡢ࡮࡬࡫ࡳࡃࠢࡤࡧࡱࡸࡪࡸࠢࠡࡥ࡯ࡥࡸࡹ࠽ࠣࡤࡶࡸࡦࡩ࡫࠮ࡦࡤࡸࡦࠨ࠾ࡼࡿ࠿࠳ࡹࡪ࠾࠽ࡶࡧࠤࡦࡲࡩࡨࡰࡀࠦࡨ࡫࡮ࡵࡧࡵࠦࠥࡩ࡬ࡢࡵࡶࡁࠧࡨࡳࡵࡣࡦ࡯࠲ࡪࡡࡵࡣࠥࡂࢀࢃ࠼࠰ࡶࡧࡂࡁ࠵ࡴࡳࡀࠪ౟").format(
    session[bstack1ll_opy_ (u"ࠫࡵࡻࡢ࡭࡫ࡦࡣࡺࡸ࡬ࠨౠ")], bstack1l1l1ll1_opy_(session), bstack1ll11111l1_opy_(session[bstack1ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡸࡺࡡࡵࡷࡶࠫౡ")]),
    bstack1ll11111l1_opy_(session[bstack1ll_opy_ (u"࠭ࡳࡵࡣࡷࡹࡸ࠭ౢ")]),
    bstack1l11l1l1l_opy_(session[bstack1ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࠨౣ")] or session[bstack1ll_opy_ (u"ࠨࡦࡨࡺ࡮ࡩࡥࠨ౤")] or bstack1ll_opy_ (u"ࠩࠪ౥")) + bstack1ll_opy_ (u"ࠥࠤࠧ౦") + (session[bstack1ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡤࡼࡥࡳࡵ࡬ࡳࡳ࠭౧")] or bstack1ll_opy_ (u"ࠬ࠭౨")),
    session[bstack1ll_opy_ (u"࠭࡯ࡴࠩ౩")] + bstack1ll_opy_ (u"ࠢࠡࠤ౪") + session[bstack1ll_opy_ (u"ࠨࡱࡶࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬ౫")], session[bstack1ll_opy_ (u"ࠩࡧࡹࡷࡧࡴࡪࡱࡱࠫ౬")] or bstack1ll_opy_ (u"ࠪࠫ౭"),
    session[bstack1ll_opy_ (u"ࠫࡨࡸࡥࡢࡶࡨࡨࡤࡧࡴࠨ౮")] if session[bstack1ll_opy_ (u"ࠬࡩࡲࡦࡣࡷࡩࡩࡥࡡࡵࠩ౯")] else bstack1ll_opy_ (u"࠭ࠧ౰"))
def bstack111l1lll_opy_(sessions, bstack1ll111l111_opy_):
  try:
    bstack1l1l111l_opy_ = bstack1ll_opy_ (u"ࠢࠣ౱")
    if not os.path.exists(bstack1lll11llll_opy_):
      os.mkdir(bstack1lll11llll_opy_)
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), bstack1ll_opy_ (u"ࠨࡣࡶࡷࡪࡺࡳ࠰ࡴࡨࡴࡴࡸࡴ࠯ࡪࡷࡱࡱ࠭౲")), bstack1ll_opy_ (u"ࠩࡵࠫ౳")) as f:
      bstack1l1l111l_opy_ = f.read()
    bstack1l1l111l_opy_ = bstack1l1l111l_opy_.replace(bstack1ll_opy_ (u"ࠪࡿࠪࡘࡅࡔࡗࡏࡘࡘࡥࡃࡐࡗࡑࡘࠪࢃࠧ౴"), str(len(sessions)))
    bstack1l1l111l_opy_ = bstack1l1l111l_opy_.replace(bstack1ll_opy_ (u"ࠫࢀࠫࡂࡖࡋࡏࡈࡤ࡛ࡒࡍࠧࢀࠫ౵"), bstack1ll111l111_opy_)
    bstack1l1l111l_opy_ = bstack1l1l111l_opy_.replace(bstack1ll_opy_ (u"ࠬࢁࠥࡃࡗࡌࡐࡉࡥࡎࡂࡏࡈࠩࢂ࠭౶"),
                                              sessions[0].get(bstack1ll_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡤࡴࡡ࡮ࡧࠪ౷")) if sessions[0] else bstack1ll_opy_ (u"ࠧࠨ౸"))
    with open(os.path.join(bstack1lll11llll_opy_, bstack1ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠭ࡳࡧࡳࡳࡷࡺ࠮ࡩࡶࡰࡰࠬ౹")), bstack1ll_opy_ (u"ࠩࡺࠫ౺")) as stream:
      stream.write(bstack1l1l111l_opy_.split(bstack1ll_opy_ (u"ࠪࡿ࡙ࠪࡅࡔࡕࡌࡓࡓ࡙࡟ࡅࡃࡗࡅࠪࢃࠧ౻"))[0])
      for session in sessions:
        stream.write(bstack1l11l11l_opy_(session))
      stream.write(bstack1l1l111l_opy_.split(bstack1ll_opy_ (u"ࠫࢀࠫࡓࡆࡕࡖࡍࡔࡔࡓࡠࡆࡄࡘࡆࠫࡽࠨ౼"))[1])
    logger.info(bstack1ll_opy_ (u"ࠬࡍࡥ࡯ࡧࡵࡥࡹ࡫ࡤࠡࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠠࡣࡷ࡬ࡰࡩࠦࡡࡳࡶ࡬ࡪࡦࡩࡴࡴࠢࡤࡸࠥࢁࡽࠨ౽").format(bstack1lll11llll_opy_));
  except Exception as e:
    logger.debug(bstack11llllll1_opy_.format(str(e)))
def bstack111ll1ll1_opy_(bstack11l11l11l_opy_):
  global CONFIG
  try:
    host = bstack1ll_opy_ (u"࠭ࡡࡱ࡫࠰ࡧࡱࡵࡵࡥࠩ౾") if bstack1ll_opy_ (u"ࠧࡢࡲࡳࠫ౿") in CONFIG else bstack1ll_opy_ (u"ࠨࡣࡳ࡭ࠬಀ")
    user = CONFIG[bstack1ll_opy_ (u"ࠩࡸࡷࡪࡸࡎࡢ࡯ࡨࠫಁ")]
    key = CONFIG[bstack1ll_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵࡎࡩࡾ࠭ಂ")]
    bstack1lll11l1l1_opy_ = bstack1ll_opy_ (u"ࠫࡦࡶࡰ࠮ࡣࡸࡸࡴࡳࡡࡵࡧࠪಃ") if bstack1ll_opy_ (u"ࠬࡧࡰࡱࠩ಄") in CONFIG else bstack1ll_opy_ (u"࠭ࡡࡶࡶࡲࡱࡦࡺࡥࠨಅ")
    url = bstack1ll_opy_ (u"ࠧࡩࡶࡷࡴࡸࡀ࠯࠰ࡽࢀ࠾ࢀࢃࡀࡼࡿ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡦࡳࡲ࠵ࡻࡾ࠱ࡥࡹ࡮ࡲࡤࡴ࠱ࡾࢁ࠴ࡹࡥࡴࡵ࡬ࡳࡳࡹ࠮࡫ࡵࡲࡲࠬಆ").format(user, key, host, bstack1lll11l1l1_opy_,
                                                                                bstack11l11l11l_opy_)
    headers = {
      bstack1ll_opy_ (u"ࠨࡅࡲࡲࡹ࡫࡮ࡵ࠯ࡷࡽࡵ࡫ࠧಇ"): bstack1ll_opy_ (u"ࠩࡤࡴࡵࡲࡩࡤࡣࡷ࡭ࡴࡴ࠯࡫ࡵࡲࡲࠬಈ"),
    }
    proxies = bstack1llll1111_opy_(CONFIG, url)
    response = requests.get(url, headers=headers, proxies=proxies)
    if response.json():
      return list(map(lambda session: session[bstack1ll_opy_ (u"ࠪࡥࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴ࡟ࡴࡧࡶࡷ࡮ࡵ࡮ࠨಉ")], response.json()))
  except Exception as e:
    logger.debug(bstack1l11l1ll_opy_.format(str(e)))
def bstack1ll111ll1l_opy_():
  global CONFIG
  global bstack11ll1l111_opy_
  try:
    if bstack1ll_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧಊ") in CONFIG:
      host = bstack1ll_opy_ (u"ࠬࡧࡰࡪ࠯ࡦࡰࡴࡻࡤࠨಋ") if bstack1ll_opy_ (u"࠭ࡡࡱࡲࠪಌ") in CONFIG else bstack1ll_opy_ (u"ࠧࡢࡲ࡬ࠫ಍")
      user = CONFIG[bstack1ll_opy_ (u"ࠨࡷࡶࡩࡷࡔࡡ࡮ࡧࠪಎ")]
      key = CONFIG[bstack1ll_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴࡍࡨࡽࠬಏ")]
      bstack1lll11l1l1_opy_ = bstack1ll_opy_ (u"ࠪࡥࡵࡶ࠭ࡢࡷࡷࡳࡲࡧࡴࡦࠩಐ") if bstack1ll_opy_ (u"ࠫࡦࡶࡰࠨ಑") in CONFIG else bstack1ll_opy_ (u"ࠬࡧࡵࡵࡱࡰࡥࡹ࡫ࠧಒ")
      url = bstack1ll_opy_ (u"࠭ࡨࡵࡶࡳࡷ࠿࠵࠯ࡼࡿ࠽ࡿࢂࡆࡻࡾ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡥࡲࡱ࠴ࢁࡽ࠰ࡤࡸ࡭ࡱࡪࡳ࠯࡬ࡶࡳࡳ࠭ಓ").format(user, key, host, bstack1lll11l1l1_opy_)
      headers = {
        bstack1ll_opy_ (u"ࠧࡄࡱࡱࡸࡪࡴࡴ࠮ࡶࡼࡴࡪ࠭ಔ"): bstack1ll_opy_ (u"ࠨࡣࡳࡴࡱ࡯ࡣࡢࡶ࡬ࡳࡳ࠵ࡪࡴࡱࡱࠫಕ"),
      }
      if bstack1ll_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫಖ") in CONFIG:
        params = {bstack1ll_opy_ (u"ࠪࡲࡦࡳࡥࠨಗ"): CONFIG[bstack1ll_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧಘ")], bstack1ll_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡣ࡮ࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨಙ"): CONFIG[bstack1ll_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨಚ")]}
      else:
        params = {bstack1ll_opy_ (u"ࠧ࡯ࡣࡰࡩࠬಛ"): CONFIG[bstack1ll_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡎࡢ࡯ࡨࠫಜ")]}
      proxies = bstack1llll1111_opy_(CONFIG, url)
      response = requests.get(url, params=params, headers=headers, proxies=proxies)
      if response.json():
        bstack111l1ll1l_opy_ = response.json()[0][bstack1ll_opy_ (u"ࠩࡤࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࡥࡢࡶ࡫࡯ࡨࠬಝ")]
        if bstack111l1ll1l_opy_:
          bstack1ll111l111_opy_ = bstack111l1ll1l_opy_[bstack1ll_opy_ (u"ࠪࡴࡺࡨ࡬ࡪࡥࡢࡹࡷࡲࠧಞ")].split(bstack1ll_opy_ (u"ࠫࡵࡻࡢ࡭࡫ࡦ࠱ࡧࡻࡩ࡭ࡦࠪಟ"))[0] + bstack1ll_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡷ࠴࠭ಠ") + bstack111l1ll1l_opy_[
            bstack1ll_opy_ (u"࠭ࡨࡢࡵ࡫ࡩࡩࡥࡩࡥࠩಡ")]
          logger.info(bstack11l1llll1_opy_.format(bstack1ll111l111_opy_))
          bstack11ll1l111_opy_ = bstack111l1ll1l_opy_[bstack1ll_opy_ (u"ࠧࡩࡣࡶ࡬ࡪࡪ࡟ࡪࡦࠪಢ")]
          bstack111ll1111_opy_ = CONFIG[bstack1ll_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡎࡢ࡯ࡨࠫಣ")]
          if bstack1ll_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫತ") in CONFIG:
            bstack111ll1111_opy_ += bstack1ll_opy_ (u"ࠪࠤࠬಥ") + CONFIG[bstack1ll_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭ದ")]
          if bstack111ll1111_opy_ != bstack111l1ll1l_opy_[bstack1ll_opy_ (u"ࠬࡴࡡ࡮ࡧࠪಧ")]:
            logger.debug(bstack1ll11lllll_opy_.format(bstack111l1ll1l_opy_[bstack1ll_opy_ (u"࠭࡮ࡢ࡯ࡨࠫನ")], bstack111ll1111_opy_))
          return [bstack111l1ll1l_opy_[bstack1ll_opy_ (u"ࠧࡩࡣࡶ࡬ࡪࡪ࡟ࡪࡦࠪ಩")], bstack1ll111l111_opy_]
    else:
      logger.warn(bstack11l111ll1_opy_)
  except Exception as e:
    logger.debug(bstack1111lll11_opy_.format(str(e)))
  return [None, None]
def bstack1llllll1l1_opy_(url, bstack1l1l11l1l_opy_=False):
  global CONFIG
  global bstack1l11lllll_opy_
  if not bstack1l11lllll_opy_:
    hostname = bstack1ll111ll_opy_(url)
    is_private = bstack1l11l11l1_opy_(hostname)
    if (bstack1ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡌࡰࡥࡤࡰࠬಪ") in CONFIG and not CONFIG[bstack1ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡍࡱࡦࡥࡱ࠭ಫ")]) and (is_private or bstack1l1l11l1l_opy_):
      bstack1l11lllll_opy_ = hostname
def bstack1ll111ll_opy_(url):
  return urlparse(url).hostname
def bstack1l11l11l1_opy_(hostname):
  for bstack1lll1111l1_opy_ in bstack111l1l11l_opy_:
    regex = re.compile(bstack1lll1111l1_opy_)
    if regex.match(hostname):
      return True
  return False
def bstack1lll111111_opy_(key_name):
  return True if key_name in threading.current_thread().__dict__.keys() else False
def getAccessibilityResults(driver):
  global CONFIG
  global bstack1l1lllll1_opy_
  if not bstack1lll1ll1_opy_.bstack11l11lll1_opy_(CONFIG, bstack1l1lllll1_opy_):
    logger.warning(bstack1ll_opy_ (u"ࠥࡒࡴࡺࠠࡢࡰࠣࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠠࡴࡧࡶࡷ࡮ࡵ࡮࠭ࠢࡦࡥࡳࡴ࡯ࡵࠢࡵࡩࡹࡸࡩࡦࡸࡨࠤࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡷ࡫ࡳࡶ࡮ࡷࡷ࠳ࠨಬ"))
    return {}
  try:
    results = driver.execute_script(bstack1ll_opy_ (u"ࠦࠧࠨࠊࠡࠢࠣࠤࠥࠦࠠࠡࡴࡨࡸࡺࡸ࡮ࠡࡰࡨࡻࠥࡖࡲࡰ࡯࡬ࡷࡪ࠮ࡦࡶࡰࡦࡸ࡮ࡵ࡮ࠡࠪࡵࡩࡸࡵ࡬ࡷࡧ࠯ࠤࡷ࡫ࡪࡦࡥࡷ࠭ࠥࢁࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࡺࡲࡺࠢࡾࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡣࡰࡰࡶࡸࠥ࡫ࡶࡦࡰࡷࠤࡂࠦ࡮ࡦࡹࠣࡇࡺࡹࡴࡰ࡯ࡈࡺࡪࡴࡴࠩࠩࡄ࠵࠶࡟࡟ࡕࡃࡓࡣࡌࡋࡔࡠࡔࡈࡗ࡚ࡒࡔࡔࠩࠬ࠿ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡤࡱࡱࡷࡹࠦࡦ࡯ࠢࡀࠤ࡫ࡻ࡮ࡤࡶ࡬ࡳࡳࠦࠨࡦࡸࡨࡲࡹ࠯ࠠࡼࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡹ࡬ࡲࡩࡵࡷ࠯ࡴࡨࡱࡴࡼࡥࡆࡸࡨࡲࡹࡒࡩࡴࡶࡨࡲࡪࡸࠨࠨࡃ࠴࠵࡞ࡥࡒࡆࡕࡘࡐ࡙࡙࡟ࡓࡇࡖࡔࡔࡔࡓࡆࠩ࠯ࠤ࡫ࡴࠩ࠼ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡴࡨࡷࡴࡲࡶࡦࠪࡨࡺࡪࡴࡴ࠯ࡦࡨࡸࡦ࡯࡬࠯ࡦࡤࡸࡦ࠯࠻ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࢁࡀࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡹ࡬ࡲࡩࡵࡷ࠯ࡣࡧࡨࡊࡼࡥ࡯ࡶࡏ࡭ࡸࡺࡥ࡯ࡧࡵࠬࠬࡇ࠱࠲࡛ࡢࡖࡊ࡙ࡕࡍࡖࡖࡣࡗࡋࡓࡑࡑࡑࡗࡊ࠭ࠬࠡࡨࡱ࠭ࡀࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡹ࡬ࡲࡩࡵࡷ࠯ࡦ࡬ࡷࡵࡧࡴࡤࡪࡈࡺࡪࡴࡴࠩࡧࡹࡩࡳࡺࠩ࠼ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡾࠢࡦࡥࡹࡩࡨࠡࡽࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࡸࡥ࡫ࡧࡦࡸ࠭࠯࠻ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡽࠋࠢࠣࠤࠥࠦࠠࠡࠢࢀ࠭ࡀࠐࠠࠡࠢࠣࠦࠧࠨಭ"))
    return results
  except Exception:
    logger.error(bstack1ll_opy_ (u"ࠧࡔ࡯ࠡࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡴࡨࡷࡺࡲࡴࡴࠢࡺࡩࡷ࡫ࠠࡧࡱࡸࡲࡩ࠴ࠢಮ"))
    return {}
def getAccessibilityResultsSummary(driver):
  global CONFIG
  global bstack1l1lllll1_opy_
  if not bstack1lll1ll1_opy_.bstack11l11lll1_opy_(CONFIG, bstack1l1lllll1_opy_):
    logger.warning(bstack1ll_opy_ (u"ࠨࡎࡰࡶࠣࡥࡳࠦࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰࠣࡷࡪࡹࡳࡪࡱࡱ࠰ࠥࡩࡡ࡯ࡰࡲࡸࠥࡸࡥࡵࡴ࡬ࡩࡻ࡫ࠠࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡳࡧࡶࡹࡱࡺࡳࠡࡵࡸࡱࡲࡧࡲࡺ࠰ࠥಯ"))
    return {}
  try:
    bstack11lll1ll1_opy_ = driver.execute_script(bstack1ll_opy_ (u"ࠢࠣࠤࠍࠤࠥࠦࠠࠡࠢࠣࠤࡷ࡫ࡴࡶࡴࡱࠤࡳ࡫ࡷࠡࡒࡵࡳࡲ࡯ࡳࡦࠪࡩࡹࡳࡩࡴࡪࡱࡱࠤ࠭ࡸࡥࡴࡱ࡯ࡺࡪ࠲ࠠࡳࡧ࡭ࡩࡨࡺࠩࠡࡽࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡶࡵࡽࠥࢁࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡦࡳࡳࡹࡴࠡࡧࡹࡩࡳࡺࠠ࠾ࠢࡱࡩࡼࠦࡃࡶࡵࡷࡳࡲࡋࡶࡦࡰࡷࠬࠬࡇ࠱࠲࡛ࡢࡘࡆࡖ࡟ࡈࡇࡗࡣࡗࡋࡓࡖࡎࡗࡗࡤ࡙ࡕࡎࡏࡄࡖ࡞࠭ࠩ࠼ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡨࡵ࡮ࡴࡶࠣࡪࡳࠦ࠽ࠡࡨࡸࡲࡨࡺࡩࡰࡰࠣࠬࡪࡼࡥ࡯ࡶࠬࠤࢀࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࡽࡩ࡯ࡦࡲࡻ࠳ࡸࡥ࡮ࡱࡹࡩࡊࡼࡥ࡯ࡶࡏ࡭ࡸࡺࡥ࡯ࡧࡵࠬࠬࡇ࠱࠲࡛ࡢࡖࡊ࡙ࡕࡍࡖࡖࡣࡘ࡛ࡍࡎࡃࡕ࡝ࡤࡘࡅࡔࡒࡒࡒࡘࡋࠧ࠭ࠢࡩࡲ࠮ࡁࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡲࡦࡵࡲࡰࡻ࡫ࠨࡦࡸࡨࡲࡹ࠴ࡤࡦࡶࡤ࡭ࡱ࠴ࡳࡶ࡯ࡰࡥࡷࡿࠩ࠼ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࢂࡁࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡺ࡭ࡳࡪ࡯ࡸ࠰ࡤࡨࡩࡋࡶࡦࡰࡷࡐ࡮ࡹࡴࡦࡰࡨࡶ࠭࠭ࡁ࠲࠳࡜ࡣࡗࡋࡓࡖࡎࡗࡗࡤ࡙ࡕࡎࡏࡄࡖ࡞ࡥࡒࡆࡕࡓࡓࡓ࡙ࡅࠨ࠮ࠣࡪࡳ࠯࠻ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡻ࡮ࡴࡤࡰࡹ࠱ࡨ࡮ࡹࡰࡢࡶࡦ࡬ࡊࡼࡥ࡯ࡶࠫࡩࡻ࡫࡮ࡵࠫ࠾ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࢀࠤࡨࡧࡴࡤࡪࠣࡿࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡳࡧ࡭ࡩࡨࡺࠨࠪ࠽ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡿࠍࠤࠥࠦࠠࠡࠢࠣࠤࢂ࠯࠻ࠋࠢࠣࠤࠥࠨࠢࠣರ"))
    return bstack11lll1ll1_opy_
  except Exception:
    logger.error(bstack1ll_opy_ (u"ࠣࡐࡲࠤࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡸࡻ࡭࡮ࡣࡵࡽࠥࡽࡡࡴࠢࡩࡳࡺࡴࡤ࠯ࠤಱ"))
    return {}