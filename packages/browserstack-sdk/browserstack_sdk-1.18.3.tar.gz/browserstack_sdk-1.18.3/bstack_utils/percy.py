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
import re
import sys
import json
import time
import shutil
import tempfile
import requests
import subprocess
from threading import Thread
from os.path import expanduser
from bstack_utils.constants import *
from requests.auth import HTTPBasicAuth
from bstack_utils.helper import bstack11llllll1_opy_, bstack11111l11l_opy_
class bstack11ll1ll1_opy_:
  working_dir = os.getcwd()
  bstack11l1ll111_opy_ = False
  config = {}
  binary_path = bstack111ll1l_opy_ (u"ࠩࠪᅴ")
  bstack11llllllll_opy_ = bstack111ll1l_opy_ (u"ࠪࠫᅵ")
  bstack1l11111ll1_opy_ = False
  bstack11llll1111_opy_ = None
  bstack1l111111ll_opy_ = {}
  bstack11lll1ll11_opy_ = 300
  bstack1l11111111_opy_ = False
  logger = None
  bstack1l1111111l_opy_ = False
  bstack11lll1l1l1_opy_ = bstack111ll1l_opy_ (u"ࠫࠬᅶ")
  bstack1l11111l11_opy_ = {
    bstack111ll1l_opy_ (u"ࠬࡩࡨࡳࡱࡰࡩࠬᅷ") : 1,
    bstack111ll1l_opy_ (u"࠭ࡦࡪࡴࡨࡪࡴࡾࠧᅸ") : 2,
    bstack111ll1l_opy_ (u"ࠧࡦࡦࡪࡩࠬᅹ") : 3,
    bstack111ll1l_opy_ (u"ࠨࡵࡤࡪࡦࡸࡩࠨᅺ") : 4
  }
  def __init__(self) -> None: pass
  def bstack1l1111ll11_opy_(self):
    bstack1l1111l111_opy_ = bstack111ll1l_opy_ (u"ࠩࠪᅻ")
    bstack11lll1ll1l_opy_ = sys.platform
    bstack11llll111l_opy_ = bstack111ll1l_opy_ (u"ࠪࡴࡪࡸࡣࡺࠩᅼ")
    if re.match(bstack111ll1l_opy_ (u"ࠦࡩࡧࡲࡸ࡫ࡱࢀࡲࡧࡣࠡࡱࡶࠦᅽ"), bstack11lll1ll1l_opy_) != None:
      bstack1l1111l111_opy_ = bstack1l1l1ll1ll_opy_ + bstack111ll1l_opy_ (u"ࠧ࠵ࡰࡦࡴࡦࡽ࠲ࡵࡳࡹ࠰ࡽ࡭ࡵࠨᅾ")
      self.bstack11lll1l1l1_opy_ = bstack111ll1l_opy_ (u"࠭࡭ࡢࡥࠪᅿ")
    elif re.match(bstack111ll1l_opy_ (u"ࠢ࡮ࡵࡺ࡭ࡳࢂ࡭ࡴࡻࡶࢀࡲ࡯࡮ࡨࡹࡿࡧࡾ࡭ࡷࡪࡰࡿࡦࡨࡩࡷࡪࡰࡿࡻ࡮ࡴࡣࡦࡾࡨࡱࡨࢂࡷࡪࡰ࠶࠶ࠧᆀ"), bstack11lll1ll1l_opy_) != None:
      bstack1l1111l111_opy_ = bstack1l1l1ll1ll_opy_ + bstack111ll1l_opy_ (u"ࠣ࠱ࡳࡩࡷࡩࡹ࠮ࡹ࡬ࡲ࠳ࢀࡩࡱࠤᆁ")
      bstack11llll111l_opy_ = bstack111ll1l_opy_ (u"ࠤࡳࡩࡷࡩࡹ࠯ࡧࡻࡩࠧᆂ")
      self.bstack11lll1l1l1_opy_ = bstack111ll1l_opy_ (u"ࠪࡻ࡮ࡴࠧᆃ")
    else:
      bstack1l1111l111_opy_ = bstack1l1l1ll1ll_opy_ + bstack111ll1l_opy_ (u"ࠦ࠴ࡶࡥࡳࡥࡼ࠱ࡱ࡯࡮ࡶࡺ࠱ࡾ࡮ࡶࠢᆄ")
      self.bstack11lll1l1l1_opy_ = bstack111ll1l_opy_ (u"ࠬࡲࡩ࡯ࡷࡻࠫᆅ")
    return bstack1l1111l111_opy_, bstack11llll111l_opy_
  def bstack11lll1lll1_opy_(self):
    try:
      bstack11lllll1ll_opy_ = [os.path.join(expanduser(bstack111ll1l_opy_ (u"ࠨࡾࠣᆆ")), bstack111ll1l_opy_ (u"ࠧ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠧᆇ")), self.working_dir, tempfile.gettempdir()]
      for path in bstack11lllll1ll_opy_:
        if(self.bstack11lll1l1ll_opy_(path)):
          return path
      raise bstack111ll1l_opy_ (u"ࠣࡗࡱࡥࡱࡨࡥࠡࡶࡲࠤࡩࡵࡷ࡯࡮ࡲࡥࡩࠦࡰࡦࡴࡦࡽࠥࡨࡩ࡯ࡣࡵࡽࠧᆈ")
    except Exception as e:
      self.logger.error(bstack111ll1l_opy_ (u"ࠤࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥ࡬ࡩ࡯ࡦࠣࡥࡻࡧࡩ࡭ࡣࡥࡰࡪࠦࡰࡢࡶ࡫ࠤ࡫ࡵࡲࠡࡲࡨࡶࡨࡿࠠࡥࡱࡺࡲࡱࡵࡡࡥ࠮ࠣࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦ࠭ࠡࡽࢀࠦᆉ").format(e))
  def bstack11lll1l1ll_opy_(self, path):
    try:
      if not os.path.exists(path):
        os.makedirs(path)
      return True
    except:
      return False
  def bstack1l111l111l_opy_(self, bstack1l1111l111_opy_, bstack11llll111l_opy_):
    try:
      bstack11lll1l111_opy_ = self.bstack11lll1lll1_opy_()
      bstack1l1111l11l_opy_ = os.path.join(bstack11lll1l111_opy_, bstack111ll1l_opy_ (u"ࠪࡴࡪࡸࡣࡺ࠰ࡽ࡭ࡵ࠭ᆊ"))
      bstack1l1111l1l1_opy_ = os.path.join(bstack11lll1l111_opy_, bstack11llll111l_opy_)
      if os.path.exists(bstack1l1111l1l1_opy_):
        self.logger.info(bstack111ll1l_opy_ (u"ࠦࡕ࡫ࡲࡤࡻࠣࡦ࡮ࡴࡡࡳࡻࠣࡪࡴࡻ࡮ࡥࠢ࡬ࡲࠥࢁࡽ࠭ࠢࡶ࡯࡮ࡶࡰࡪࡰࡪࠤࡩࡵࡷ࡯࡮ࡲࡥࡩࠨᆋ").format(bstack1l1111l1l1_opy_))
        return bstack1l1111l1l1_opy_
      if os.path.exists(bstack1l1111l11l_opy_):
        self.logger.info(bstack111ll1l_opy_ (u"ࠧࡖࡥࡳࡥࡼࠤࡿ࡯ࡰࠡࡨࡲࡹࡳࡪࠠࡪࡰࠣࡿࢂ࠲ࠠࡶࡰࡽ࡭ࡵࡶࡩ࡯ࡩࠥᆌ").format(bstack1l1111l11l_opy_))
        return self.bstack11lll11ll1_opy_(bstack1l1111l11l_opy_, bstack11llll111l_opy_)
      self.logger.info(bstack111ll1l_opy_ (u"ࠨࡄࡰࡹࡱࡰࡴࡧࡤࡪࡰࡪࠤࡵ࡫ࡲࡤࡻࠣࡦ࡮ࡴࡡࡳࡻࠣࡪࡷࡵ࡭ࠡࡽࢀࠦᆍ").format(bstack1l1111l111_opy_))
      response = bstack11111l11l_opy_(bstack111ll1l_opy_ (u"ࠧࡈࡇࡗࠫᆎ"), bstack1l1111l111_opy_, {}, {})
      if response.status_code == 200:
        with open(bstack1l1111l11l_opy_, bstack111ll1l_opy_ (u"ࠨࡹࡥࠫᆏ")) as file:
          file.write(response.content)
        self.logger.info(bstack1l111111l1_opy_ (u"ࠤࡇࡳࡼࡴ࡬ࡰࡣࡧࡩࡩࠦࡰࡦࡴࡦࡽࠥࡨࡩ࡯ࡣࡵࡽࠥࡧ࡮ࡥࠢࡶࡥࡻ࡫ࡤࠡࡣࡷࠤࢀࡨࡩ࡯ࡣࡵࡽࡤࢀࡩࡱࡡࡳࡥࡹ࡮ࡽࠣᆐ"))
        return self.bstack11lll11ll1_opy_(bstack1l1111l11l_opy_, bstack11llll111l_opy_)
      else:
        raise(bstack1l111111l1_opy_ (u"ࠥࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡤࡰࡹࡱࡰࡴࡧࡤࠡࡶ࡫ࡩࠥ࡬ࡩ࡭ࡧ࠱ࠤࡘࡺࡡࡵࡷࡶࠤࡨࡵࡤࡦ࠼ࠣࡿࡷ࡫ࡳࡱࡱࡱࡷࡪ࠴ࡳࡵࡣࡷࡹࡸࡥࡣࡰࡦࡨࢁࠧᆑ"))
    except:
      self.logger.error(bstack111ll1l_opy_ (u"࡚ࠦࡴࡡࡣ࡮ࡨࠤࡹࡵࠠࡥࡱࡺࡲࡱࡵࡡࡥࠢࡳࡩࡷࡩࡹࠡࡤ࡬ࡲࡦࡸࡹࠣᆒ"))
  def bstack1l111l1l1l_opy_(self, bstack1l1111l111_opy_, bstack11llll111l_opy_):
    try:
      bstack1l1111l1l1_opy_ = self.bstack1l111l111l_opy_(bstack1l1111l111_opy_, bstack11llll111l_opy_)
      bstack1l111l1111_opy_ = self.bstack1l111l1lll_opy_(bstack1l1111l111_opy_, bstack11llll111l_opy_, bstack1l1111l1l1_opy_)
      return bstack1l1111l1l1_opy_, bstack1l111l1111_opy_
    except Exception as e:
      self.logger.error(bstack111ll1l_opy_ (u"࡛ࠧ࡮ࡢࡤ࡯ࡩࠥࡺ࡯ࠡࡩࡨࡸࠥࡶࡥࡳࡥࡼࠤࡧ࡯࡮ࡢࡴࡼࠤࡵࡧࡴࡩࠤᆓ").format(e))
    return bstack1l1111l1l1_opy_, False
  def bstack1l111l1lll_opy_(self, bstack1l1111l111_opy_, bstack11llll111l_opy_, bstack1l1111l1l1_opy_, bstack11llll1l11_opy_ = 0):
    if bstack11llll1l11_opy_ > 1:
      return False
    if bstack1l1111l1l1_opy_ == None or os.path.exists(bstack1l1111l1l1_opy_) == False:
      self.logger.warn(bstack111ll1l_opy_ (u"ࠨࡐࡦࡴࡦࡽࠥࡶࡡࡵࡪࠣࡲࡴࡺࠠࡧࡱࡸࡲࡩ࠲ࠠࡳࡧࡷࡶࡾ࡯࡮ࡨࠢࡧࡳࡼࡴ࡬ࡰࡣࡧࠦᆔ"))
      bstack1l1111l1l1_opy_ = self.bstack1l111l111l_opy_(bstack1l1111l111_opy_, bstack11llll111l_opy_)
      self.bstack1l111l1lll_opy_(bstack1l1111l111_opy_, bstack11llll111l_opy_, bstack1l1111l1l1_opy_, bstack11llll1l11_opy_+1)
    bstack11llll1l1l_opy_ = bstack111ll1l_opy_ (u"ࠢ࡟࠰࠭ࡄࡵ࡫ࡲࡤࡻ࡟࠳ࡨࡲࡩࠡ࡞ࡧ࠲ࡡࡪࠫ࠯࡞ࡧ࠯ࠧᆕ")
    command = bstack111ll1l_opy_ (u"ࠨࡽࢀࠤ࠲࠳ࡶࡦࡴࡶ࡭ࡴࡴࠧᆖ").format(bstack1l1111l1l1_opy_)
    bstack1l1111lll1_opy_ = subprocess.check_output(command, shell=True, text=True)
    if re.match(bstack11llll1l1l_opy_, bstack1l1111lll1_opy_) != None:
      return True
    else:
      self.logger.error(bstack111ll1l_opy_ (u"ࠤࡓࡩࡷࡩࡹࠡࡸࡨࡶࡸ࡯࡯࡯ࠢࡦ࡬ࡪࡩ࡫ࠡࡨࡤ࡭ࡱ࡫ࡤࠣᆗ"))
      bstack1l1111l1l1_opy_ = self.bstack1l111l111l_opy_(bstack1l1111l111_opy_, bstack11llll111l_opy_)
      self.bstack1l111l1lll_opy_(bstack1l1111l111_opy_, bstack11llll111l_opy_, bstack1l1111l1l1_opy_, bstack11llll1l11_opy_+1)
  def bstack11lll11ll1_opy_(self, bstack1l1111l11l_opy_, bstack11llll111l_opy_):
    try:
      working_dir = os.path.dirname(bstack1l1111l11l_opy_)
      shutil.unpack_archive(bstack1l1111l11l_opy_, working_dir)
      bstack1l1111l1l1_opy_ = os.path.join(working_dir, bstack11llll111l_opy_)
      os.chmod(bstack1l1111l1l1_opy_, 0o755)
      return bstack1l1111l1l1_opy_
    except Exception as e:
      self.logger.error(bstack111ll1l_opy_ (u"࡙ࠥࡳࡧࡢ࡭ࡧࠣࡸࡴࠦࡵ࡯ࡼ࡬ࡴࠥࡶࡥࡳࡥࡼࠤࡧ࡯࡮ࡢࡴࡼࠦᆘ"))
  def bstack11lllll111_opy_(self):
    try:
      percy = str(self.config.get(bstack111ll1l_opy_ (u"ࠫࡵ࡫ࡲࡤࡻࠪᆙ"), bstack111ll1l_opy_ (u"ࠧ࡬ࡡ࡭ࡵࡨࠦᆚ"))).lower()
      if percy != bstack111ll1l_opy_ (u"ࠨࡴࡳࡷࡨࠦᆛ"):
        return False
      self.bstack1l11111ll1_opy_ = True
      return True
    except Exception as e:
      self.logger.error(bstack111ll1l_opy_ (u"ࠢࡖࡰࡤࡦࡱ࡫ࠠࡵࡱࠣࡨࡪࡺࡥࡤࡶࠣࡴࡪࡸࡣࡺ࠮ࠣࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡻࡾࠤᆜ").format(e))
  def init(self, bstack11l1ll111_opy_, config, logger):
    self.bstack11l1ll111_opy_ = bstack11l1ll111_opy_
    self.config = config
    self.logger = logger
    if not self.bstack11lllll111_opy_():
      return
    self.bstack1l111111ll_opy_ = config.get(bstack111ll1l_opy_ (u"ࠨࡲࡨࡶࡨࡿࡏࡱࡶ࡬ࡳࡳࡹࠧᆝ"), {})
    try:
      bstack1l1111l111_opy_, bstack11llll111l_opy_ = self.bstack1l1111ll11_opy_()
      bstack1l1111l1l1_opy_, bstack1l111l1111_opy_ = self.bstack1l111l1l1l_opy_(bstack1l1111l111_opy_, bstack11llll111l_opy_)
      if bstack1l111l1111_opy_:
        self.binary_path = bstack1l1111l1l1_opy_
        thread = Thread(target=self.bstack11llllll11_opy_)
        thread.start()
      else:
        self.bstack1l1111111l_opy_ = True
        self.logger.error(bstack111ll1l_opy_ (u"ࠤࡌࡲࡻࡧ࡬ࡪࡦࠣࡴࡪࡸࡣࡺࠢࡳࡥࡹ࡮ࠠࡧࡱࡸࡲࡩࠦ࠭ࠡࡽࢀ࠰࡛ࠥ࡮ࡢࡤ࡯ࡩࠥࡺ࡯ࠡࡵࡷࡥࡷࡺࠠࡑࡧࡵࡧࡾࠨᆞ").format(bstack1l1111l1l1_opy_))
    except Exception as e:
      self.logger.error(bstack111ll1l_opy_ (u"࡙ࠥࡳࡧࡢ࡭ࡧࠣࡸࡴࠦࡳࡵࡣࡵࡸࠥࡶࡥࡳࡥࡼ࠰ࠥࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡࡽࢀࠦᆟ").format(e))
  def bstack11lllllll1_opy_(self):
    try:
      logfile = os.path.join(self.working_dir, bstack111ll1l_opy_ (u"ࠫࡱࡵࡧࠨᆠ"), bstack111ll1l_opy_ (u"ࠬࡶࡥࡳࡥࡼ࠲ࡱࡵࡧࠨᆡ"))
      os.makedirs(os.path.dirname(logfile)) if not os.path.exists(os.path.dirname(logfile)) else None
      self.logger.debug(bstack111ll1l_opy_ (u"ࠨࡐࡶࡵ࡫࡭ࡳ࡭ࠠࡱࡧࡵࡧࡾࠦ࡬ࡰࡩࡶࠤࡦࡺࠠࡼࡿࠥᆢ").format(logfile))
      self.bstack11llllllll_opy_ = logfile
    except Exception as e:
      self.logger.error(bstack111ll1l_opy_ (u"ࠢࡖࡰࡤࡦࡱ࡫ࠠࡵࡱࠣࡷࡪࡺࠠࡱࡧࡵࡧࡾࠦ࡬ࡰࡩࠣࡴࡦࡺࡨ࠭ࠢࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥࢁࡽࠣᆣ").format(e))
  def bstack11llllll11_opy_(self):
    bstack1l111l11ll_opy_ = self.bstack11llll1ll1_opy_()
    if bstack1l111l11ll_opy_ == None:
      self.bstack1l1111111l_opy_ = True
      self.logger.error(bstack111ll1l_opy_ (u"ࠣࡒࡨࡶࡨࡿࠠࡵࡱ࡮ࡩࡳࠦ࡮ࡰࡶࠣࡪࡴࡻ࡮ࡥ࠮ࠣࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡳࡵࡣࡵࡸࠥࡶࡥࡳࡥࡼࠦᆤ"))
      return False
    command_args = [bstack111ll1l_opy_ (u"ࠤࡤࡴࡵࡀࡥࡹࡧࡦ࠾ࡸࡺࡡࡳࡶࠥᆥ") if self.bstack11l1ll111_opy_ else bstack111ll1l_opy_ (u"ࠪࡩࡽ࡫ࡣ࠻ࡵࡷࡥࡷࡺࠧᆦ")]
    bstack1l111ll111_opy_ = self.bstack1l111l1l11_opy_()
    if bstack1l111ll111_opy_ != None:
      command_args.append(bstack111ll1l_opy_ (u"ࠦ࠲ࡩࠠࡼࡿࠥᆧ").format(bstack1l111ll111_opy_))
    env = os.environ.copy()
    env[bstack111ll1l_opy_ (u"ࠧࡖࡅࡓࡅ࡜ࡣ࡙ࡕࡋࡆࡐࠥᆨ")] = bstack1l111l11ll_opy_
    bstack11llll1lll_opy_ = [self.binary_path]
    self.bstack11lllllll1_opy_()
    self.bstack11llll1111_opy_ = self.bstack1l11111l1l_opy_(bstack11llll1lll_opy_ + command_args, env)
    self.logger.debug(bstack111ll1l_opy_ (u"ࠨࡓࡵࡣࡵࡸ࡮ࡴࡧࠡࡊࡨࡥࡱࡺࡨࠡࡅ࡫ࡩࡨࡱࠢᆩ"))
    bstack11llll1l11_opy_ = 0
    while self.bstack11llll1111_opy_.poll() == None:
      bstack1l1111l1ll_opy_ = self.bstack1l1111ll1l_opy_()
      if bstack1l1111l1ll_opy_:
        self.logger.debug(bstack111ll1l_opy_ (u"ࠢࡉࡧࡤࡰࡹ࡮ࠠࡄࡪࡨࡧࡰࠦࡳࡶࡥࡦࡩࡸࡹࡦࡶ࡮ࠥᆪ"))
        self.bstack1l11111111_opy_ = True
        return True
      bstack11llll1l11_opy_ += 1
      self.logger.debug(bstack111ll1l_opy_ (u"ࠣࡊࡨࡥࡱࡺࡨࠡࡅ࡫ࡩࡨࡱࠠࡓࡧࡷࡶࡾࠦ࠭ࠡࡽࢀࠦᆫ").format(bstack11llll1l11_opy_))
      time.sleep(2)
    self.logger.error(bstack111ll1l_opy_ (u"ࠤࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡹࡴࡢࡴࡷࠤࡵ࡫ࡲࡤࡻ࠯ࠤࡍ࡫ࡡ࡭ࡶ࡫ࠤࡈ࡮ࡥࡤ࡭ࠣࡊࡦ࡯࡬ࡦࡦࠣࡥ࡫ࡺࡥࡳࠢࡾࢁࠥࡧࡴࡵࡧࡰࡴࡹࡹࠢᆬ").format(bstack11llll1l11_opy_))
    self.bstack1l1111111l_opy_ = True
    return False
  def bstack1l1111ll1l_opy_(self, bstack11llll1l11_opy_ = 0):
    try:
      if bstack11llll1l11_opy_ > 10:
        return False
      bstack1l111ll11l_opy_ = os.environ.get(bstack111ll1l_opy_ (u"ࠪࡔࡊࡘࡃ࡚ࡡࡖࡉࡗ࡜ࡅࡓࡡࡄࡈࡉࡘࡅࡔࡕࠪᆭ"), bstack111ll1l_opy_ (u"ࠫ࡭ࡺࡴࡱ࠼࠲࠳ࡱࡵࡣࡢ࡮࡫ࡳࡸࡺ࠺࠶࠵࠶࠼ࠬᆮ"))
      bstack11lll11lll_opy_ = bstack1l111ll11l_opy_ + bstack1l1l1lllll_opy_
      response = requests.get(bstack11lll11lll_opy_)
      return True if response.json() else False
    except:
      return False
  def bstack11llll1ll1_opy_(self):
    bstack11lll1l11l_opy_ = bstack111ll1l_opy_ (u"ࠬࡧࡰࡱࠩᆯ") if self.bstack11l1ll111_opy_ else bstack111ll1l_opy_ (u"࠭ࡡࡶࡶࡲࡱࡦࡺࡥࠨᆰ")
    bstack1l11lllll1_opy_ = bstack111ll1l_opy_ (u"ࠢࡢࡲ࡬࠳ࡦࡶࡰࡠࡲࡨࡶࡨࡿ࠯ࡨࡧࡷࡣࡵࡸ࡯࡫ࡧࡦࡸࡤࡺ࡯࡬ࡧࡱࡃࡳࡧ࡭ࡦ࠿ࡾࢁࠫࡺࡹࡱࡧࡀࡿࢂࠨᆱ").format(self.config[bstack111ll1l_opy_ (u"ࠨࡲࡵࡳ࡯࡫ࡣࡵࡐࡤࡱࡪ࠭ᆲ")], bstack11lll1l11l_opy_)
    uri = bstack11llllll1_opy_(bstack1l11lllll1_opy_)
    try:
      response = bstack11111l11l_opy_(bstack111ll1l_opy_ (u"ࠩࡊࡉ࡙࠭ᆳ"), uri, {}, {bstack111ll1l_opy_ (u"ࠪࡥࡺࡺࡨࠨᆴ"): (self.config[bstack111ll1l_opy_ (u"ࠫࡺࡹࡥࡳࡐࡤࡱࡪ࠭ᆵ")], self.config[bstack111ll1l_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷࡐ࡫ࡹࠨᆶ")])})
      if response.status_code == 200:
        bstack1l111l11l1_opy_ = response.json()
        if bstack111ll1l_opy_ (u"ࠨࡴࡰ࡭ࡨࡲࠧᆷ") in bstack1l111l11l1_opy_:
          return bstack1l111l11l1_opy_[bstack111ll1l_opy_ (u"ࠢࡵࡱ࡮ࡩࡳࠨᆸ")]
        else:
          raise bstack111ll1l_opy_ (u"ࠨࡖࡲ࡯ࡪࡴࠠࡏࡱࡷࠤࡋࡵࡵ࡯ࡦࠣ࠱ࠥࢁࡽࠨᆹ").format(bstack1l111l11l1_opy_)
      else:
        raise bstack111ll1l_opy_ (u"ࠤࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥ࡬ࡥࡵࡥ࡫ࠤࡵ࡫ࡲࡤࡻࠣࡸࡴࡱࡥ࡯࠮ࠣࡖࡪࡹࡰࡰࡰࡶࡩࠥࡹࡴࡢࡶࡸࡷࠥ࠳ࠠࡼࡿ࠯ࠤࡗ࡫ࡳࡱࡱࡱࡷࡪࠦࡂࡰࡦࡼࠤ࠲ࠦࡻࡾࠤᆺ").format(response.status_code, response.json())
    except Exception as e:
      self.logger.error(bstack111ll1l_opy_ (u"ࠥࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡦࡶࡪࡧࡴࡪࡰࡪࠤࡵ࡫ࡲࡤࡻࠣࡴࡷࡵࡪࡦࡥࡷࠦᆻ").format(e))
  def bstack1l111l1l11_opy_(self):
    bstack11lll1llll_opy_ = os.path.join(tempfile.gettempdir(), bstack111ll1l_opy_ (u"ࠦࡵ࡫ࡲࡤࡻࡆࡳࡳ࡬ࡩࡨ࠰࡭ࡷࡴࡴࠢᆼ"))
    try:
      if bstack111ll1l_opy_ (u"ࠬࡼࡥࡳࡵ࡬ࡳࡳ࠭ᆽ") not in self.bstack1l111111ll_opy_:
        self.bstack1l111111ll_opy_[bstack111ll1l_opy_ (u"࠭ࡶࡦࡴࡶ࡭ࡴࡴࠧᆾ")] = 2
      with open(bstack11lll1llll_opy_, bstack111ll1l_opy_ (u"ࠧࡸࠩᆿ")) as fp:
        json.dump(self.bstack1l111111ll_opy_, fp)
      return bstack11lll1llll_opy_
    except Exception as e:
      self.logger.error(bstack111ll1l_opy_ (u"ࠣࡗࡱࡥࡧࡲࡥࠡࡶࡲࠤࡨࡸࡥࡢࡶࡨࠤࡵ࡫ࡲࡤࡻࠣࡧࡴࡴࡦ࠭ࠢࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥࢁࡽࠣᇀ").format(e))
  def bstack1l11111l1l_opy_(self, cmd, env = os.environ.copy()):
    try:
      if self.bstack11lll1l1l1_opy_ == bstack111ll1l_opy_ (u"ࠩࡺ࡭ࡳ࠭ᇁ"):
        bstack1l11111lll_opy_ = [bstack111ll1l_opy_ (u"ࠪࡧࡲࡪ࠮ࡦࡺࡨࠫᇂ"), bstack111ll1l_opy_ (u"ࠫ࠴ࡩࠧᇃ")]
        cmd = bstack1l11111lll_opy_ + cmd
      cmd = bstack111ll1l_opy_ (u"ࠬࠦࠧᇄ").join(cmd)
      self.logger.debug(bstack111ll1l_opy_ (u"ࠨࡒࡶࡰࡱ࡭ࡳ࡭ࠠࡼࡿࠥᇅ").format(cmd))
      with open(self.bstack11llllllll_opy_, bstack111ll1l_opy_ (u"ࠢࡢࠤᇆ")) as bstack11llll11ll_opy_:
        process = subprocess.Popen(cmd, shell=True, stdout=bstack11llll11ll_opy_, text=True, stderr=bstack11llll11ll_opy_, env=env, universal_newlines=True)
      return process
    except Exception as e:
      self.bstack1l1111111l_opy_ = True
      self.logger.error(bstack111ll1l_opy_ (u"ࠣࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡸࡺࡡࡳࡶࠣࡴࡪࡸࡣࡺࠢࡺ࡭ࡹ࡮ࠠࡤ࡯ࡧࠤ࠲ࠦࡻࡾ࠮ࠣࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࡀࠠࡼࡿࠥᇇ").format(cmd, e))
  def shutdown(self):
    try:
      if self.bstack1l11111111_opy_:
        self.logger.info(bstack111ll1l_opy_ (u"ࠤࡖࡸࡴࡶࡰࡪࡰࡪࠤࡕ࡫ࡲࡤࡻࠥᇈ"))
        cmd = [self.binary_path, bstack111ll1l_opy_ (u"ࠥࡩࡽ࡫ࡣ࠻ࡵࡷࡳࡵࠨᇉ")]
        self.bstack1l11111l1l_opy_(cmd)
        self.bstack1l11111111_opy_ = False
    except Exception as e:
      self.logger.error(bstack111ll1l_opy_ (u"ࠦࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡴࡶࡲࡴࠥࡹࡥࡴࡵ࡬ࡳࡳࠦࡷࡪࡶ࡫ࠤࡨࡵ࡭࡮ࡣࡱࡨࠥ࠳ࠠࡼࡿ࠯ࠤࡊࡾࡣࡦࡲࡷ࡭ࡴࡴ࠺ࠡࡽࢀࠦᇊ").format(cmd, e))
  def bstack1ll1l111_opy_(self):
    if not self.bstack1l11111ll1_opy_:
      return
    try:
      bstack11lllll1l1_opy_ = 0
      while not self.bstack1l11111111_opy_ and bstack11lllll1l1_opy_ < self.bstack11lll1ll11_opy_:
        if self.bstack1l1111111l_opy_:
          self.logger.info(bstack111ll1l_opy_ (u"ࠧࡖࡥࡳࡥࡼࠤࡸ࡫ࡴࡶࡲࠣࡪࡦ࡯࡬ࡦࡦࠥᇋ"))
          return
        time.sleep(1)
        bstack11lllll1l1_opy_ += 1
      os.environ[bstack111ll1l_opy_ (u"࠭ࡐࡆࡔࡆ࡝ࡤࡈࡅࡔࡖࡢࡔࡑࡇࡔࡇࡑࡕࡑࠬᇌ")] = str(self.bstack11llll11l1_opy_())
      self.logger.info(bstack111ll1l_opy_ (u"ࠢࡑࡧࡵࡧࡾࠦࡳࡦࡶࡸࡴࠥࡩ࡯࡮ࡲ࡯ࡩࡹ࡫ࡤࠣᇍ"))
    except Exception as e:
      self.logger.error(bstack111ll1l_opy_ (u"ࠣࡗࡱࡥࡧࡲࡥࠡࡶࡲࠤࡸ࡫ࡴࡶࡲࠣࡴࡪࡸࡣࡺ࠮ࠣࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡻࡾࠤᇎ").format(e))
  def bstack11llll11l1_opy_(self):
    if self.bstack11l1ll111_opy_:
      return
    try:
      bstack11lllll11l_opy_ = [platform[bstack111ll1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡑࡥࡲ࡫ࠧᇏ")].lower() for platform in self.config.get(bstack111ll1l_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ᇐ"), [])]
      bstack11llllll1l_opy_ = sys.maxsize
      bstack1l1111llll_opy_ = bstack111ll1l_opy_ (u"ࠫࠬᇑ")
      for browser in bstack11lllll11l_opy_:
        if browser in self.bstack1l11111l11_opy_:
          bstack1l111l1ll1_opy_ = self.bstack1l11111l11_opy_[browser]
        if bstack1l111l1ll1_opy_ < bstack11llllll1l_opy_:
          bstack11llllll1l_opy_ = bstack1l111l1ll1_opy_
          bstack1l1111llll_opy_ = browser
      return bstack1l1111llll_opy_
    except Exception as e:
      self.logger.error(bstack111ll1l_opy_ (u"࡛ࠧ࡮ࡢࡤ࡯ࡩࠥࡺ࡯ࠡࡨ࡬ࡲࡩࠦࡢࡦࡵࡷࠤࡵࡲࡡࡵࡨࡲࡶࡲ࠲ࠠࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣࡿࢂࠨᇒ").format(e))