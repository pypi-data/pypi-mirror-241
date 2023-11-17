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
from bstack_utils.helper import bstack1lll1ll1l1_opy_, bstack1llll1l11l_opy_
class bstack111111lll_opy_:
  working_dir = os.getcwd()
  bstack11l1l1ll_opy_ = False
  config = {}
  binary_path = bstack1ll_opy_ (u"ࠨࠩᆤ")
  bstack11llll1l11_opy_ = bstack1ll_opy_ (u"ࠩࠪᆥ")
  bstack11lll11ll1_opy_ = False
  bstack11ll1l1ll1_opy_ = None
  bstack11ll1l111l_opy_ = {}
  bstack11lllll11l_opy_ = 300
  bstack11lll1l11l_opy_ = False
  logger = None
  bstack11llll1ll1_opy_ = False
  bstack11llllll1l_opy_ = bstack1ll_opy_ (u"ࠪࠫᆦ")
  bstack11ll1ll1l1_opy_ = {
    bstack1ll_opy_ (u"ࠫࡨ࡮ࡲࡰ࡯ࡨࠫᆧ") : 1,
    bstack1ll_opy_ (u"ࠬ࡬ࡩࡳࡧࡩࡳࡽ࠭ᆨ") : 2,
    bstack1ll_opy_ (u"࠭ࡥࡥࡩࡨࠫᆩ") : 3,
    bstack1ll_opy_ (u"ࠧࡴࡣࡩࡥࡷ࡯ࠧᆪ") : 4
  }
  def __init__(self) -> None: pass
  def bstack11lll1ll11_opy_(self):
    bstack11llllll11_opy_ = bstack1ll_opy_ (u"ࠨࠩᆫ")
    bstack11lll1l111_opy_ = sys.platform
    bstack11llll1l1l_opy_ = bstack1ll_opy_ (u"ࠩࡳࡩࡷࡩࡹࠨᆬ")
    if re.match(bstack1ll_opy_ (u"ࠥࡨࡦࡸࡷࡪࡰࡿࡱࡦࡩࠠࡰࡵࠥᆭ"), bstack11lll1l111_opy_) != None:
      bstack11llllll11_opy_ = bstack1l1l11l1l1_opy_ + bstack1ll_opy_ (u"ࠦ࠴ࡶࡥࡳࡥࡼ࠱ࡴࡹࡸ࠯ࡼ࡬ࡴࠧᆮ")
      self.bstack11llllll1l_opy_ = bstack1ll_opy_ (u"ࠬࡳࡡࡤࠩᆯ")
    elif re.match(bstack1ll_opy_ (u"ࠨ࡭ࡴࡹ࡬ࡲࢁࡳࡳࡺࡵࡿࡱ࡮ࡴࡧࡸࡾࡦࡽ࡬ࡽࡩ࡯ࡾࡥࡧࡨࡽࡩ࡯ࡾࡺ࡭ࡳࡩࡥࡽࡧࡰࡧࢁࡽࡩ࡯࠵࠵ࠦᆰ"), bstack11lll1l111_opy_) != None:
      bstack11llllll11_opy_ = bstack1l1l11l1l1_opy_ + bstack1ll_opy_ (u"ࠢ࠰ࡲࡨࡶࡨࡿ࠭ࡸ࡫ࡱ࠲ࡿ࡯ࡰࠣᆱ")
      bstack11llll1l1l_opy_ = bstack1ll_opy_ (u"ࠣࡲࡨࡶࡨࡿ࠮ࡦࡺࡨࠦᆲ")
      self.bstack11llllll1l_opy_ = bstack1ll_opy_ (u"ࠩࡺ࡭ࡳ࠭ᆳ")
    else:
      bstack11llllll11_opy_ = bstack1l1l11l1l1_opy_ + bstack1ll_opy_ (u"ࠥ࠳ࡵ࡫ࡲࡤࡻ࠰ࡰ࡮ࡴࡵࡹ࠰ࡽ࡭ࡵࠨᆴ")
      self.bstack11llllll1l_opy_ = bstack1ll_opy_ (u"ࠫࡱ࡯࡮ࡶࡺࠪᆵ")
    return bstack11llllll11_opy_, bstack11llll1l1l_opy_
  def bstack11lllllll1_opy_(self):
    try:
      bstack11ll1l11l1_opy_ = [os.path.join(expanduser(bstack1ll_opy_ (u"ࠧࢄࠢᆶ")), bstack1ll_opy_ (u"࠭࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠭ᆷ")), self.working_dir, tempfile.gettempdir()]
      for path in bstack11ll1l11l1_opy_:
        if(self.bstack11lllll1ll_opy_(path)):
          return path
      raise bstack1ll_opy_ (u"ࠢࡖࡰࡤࡰࡧ࡫ࠠࡵࡱࠣࡨࡴࡽ࡮࡭ࡱࡤࡨࠥࡶࡥࡳࡥࡼࠤࡧ࡯࡮ࡢࡴࡼࠦᆸ")
    except Exception as e:
      self.logger.error(bstack1ll_opy_ (u"ࠣࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤ࡫࡯࡮ࡥࠢࡤࡺࡦ࡯࡬ࡢࡤ࡯ࡩࠥࡶࡡࡵࡪࠣࡪࡴࡸࠠࡱࡧࡵࡧࡾࠦࡤࡰࡹࡱࡰࡴࡧࡤ࠭ࠢࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࠳ࠠࡼࡿࠥᆹ").format(e))
  def bstack11lllll1ll_opy_(self, path):
    try:
      if not os.path.exists(path):
        os.makedirs(path)
      return True
    except:
      return False
  def bstack1l11111111_opy_(self, bstack11llllll11_opy_, bstack11llll1l1l_opy_):
    try:
      bstack11lll1l1l1_opy_ = self.bstack11lllllll1_opy_()
      bstack11lllll1l1_opy_ = os.path.join(bstack11lll1l1l1_opy_, bstack1ll_opy_ (u"ࠩࡳࡩࡷࡩࡹ࠯ࡼ࡬ࡴࠬᆺ"))
      bstack11llll1111_opy_ = os.path.join(bstack11lll1l1l1_opy_, bstack11llll1l1l_opy_)
      if os.path.exists(bstack11llll1111_opy_):
        self.logger.info(bstack1ll_opy_ (u"ࠥࡔࡪࡸࡣࡺࠢࡥ࡭ࡳࡧࡲࡺࠢࡩࡳࡺࡴࡤࠡ࡫ࡱࠤࢀࢃࠬࠡࡵ࡮࡭ࡵࡶࡩ࡯ࡩࠣࡨࡴࡽ࡮࡭ࡱࡤࡨࠧᆻ").format(bstack11llll1111_opy_))
        return bstack11llll1111_opy_
      if os.path.exists(bstack11lllll1l1_opy_):
        self.logger.info(bstack1ll_opy_ (u"ࠦࡕ࡫ࡲࡤࡻࠣࡾ࡮ࡶࠠࡧࡱࡸࡲࡩࠦࡩ࡯ࠢࡾࢁ࠱ࠦࡵ࡯ࡼ࡬ࡴࡵ࡯࡮ࡨࠤᆼ").format(bstack11lllll1l1_opy_))
        return self.bstack11ll1ll11l_opy_(bstack11lllll1l1_opy_, bstack11llll1l1l_opy_)
      self.logger.info(bstack1ll_opy_ (u"ࠧࡊ࡯ࡸࡰ࡯ࡳࡦࡪࡩ࡯ࡩࠣࡴࡪࡸࡣࡺࠢࡥ࡭ࡳࡧࡲࡺࠢࡩࡶࡴࡳࠠࡼࡿࠥᆽ").format(bstack11llllll11_opy_))
      response = bstack1llll1l11l_opy_(bstack1ll_opy_ (u"࠭ࡇࡆࡖࠪᆾ"), bstack11llllll11_opy_, {}, {})
      if response.status_code == 200:
        with open(bstack11lllll1l1_opy_, bstack1ll_opy_ (u"ࠧࡸࡤࠪᆿ")) as file:
          file.write(response.content)
        self.logger.info(bstack11lll11l11_opy_ (u"ࠣࡆࡲࡻࡳࡲ࡯ࡢࡦࡨࡨࠥࡶࡥࡳࡥࡼࠤࡧ࡯࡮ࡢࡴࡼࠤࡦࡴࡤࠡࡵࡤࡺࡪࡪࠠࡢࡶࠣࡿࡧ࡯࡮ࡢࡴࡼࡣࡿ࡯ࡰࡠࡲࡤࡸ࡭ࢃࠢᇀ"))
        return self.bstack11ll1ll11l_opy_(bstack11lllll1l1_opy_, bstack11llll1l1l_opy_)
      else:
        raise(bstack11lll11l11_opy_ (u"ࠤࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡪ࡯ࡸࡰ࡯ࡳࡦࡪࠠࡵࡪࡨࠤ࡫࡯࡬ࡦ࠰ࠣࡗࡹࡧࡴࡶࡵࠣࡧࡴࡪࡥ࠻ࠢࡾࡶࡪࡹࡰࡰࡰࡶࡩ࠳ࡹࡴࡢࡶࡸࡷࡤࡩ࡯ࡥࡧࢀࠦᇁ"))
    except:
      self.logger.error(bstack1ll_opy_ (u"࡙ࠥࡳࡧࡢ࡭ࡧࠣࡸࡴࠦࡤࡰࡹࡱࡰࡴࡧࡤࠡࡲࡨࡶࡨࡿࠠࡣ࡫ࡱࡥࡷࡿࠢᇂ"))
  def bstack11lll111ll_opy_(self, bstack11llllll11_opy_, bstack11llll1l1l_opy_):
    try:
      bstack11llll1111_opy_ = self.bstack1l11111111_opy_(bstack11llllll11_opy_, bstack11llll1l1l_opy_)
      bstack11lll11lll_opy_ = self.bstack11lll1llll_opy_(bstack11llllll11_opy_, bstack11llll1l1l_opy_, bstack11llll1111_opy_)
      return bstack11llll1111_opy_, bstack11lll11lll_opy_
    except Exception as e:
      self.logger.error(bstack1ll_opy_ (u"࡚ࠦࡴࡡࡣ࡮ࡨࠤࡹࡵࠠࡨࡧࡷࠤࡵ࡫ࡲࡤࡻࠣࡦ࡮ࡴࡡࡳࡻࠣࡴࡦࡺࡨࠣᇃ").format(e))
    return bstack11llll1111_opy_, False
  def bstack11lll1llll_opy_(self, bstack11llllll11_opy_, bstack11llll1l1l_opy_, bstack11llll1111_opy_, bstack11ll1llll1_opy_ = 0):
    if bstack11ll1llll1_opy_ > 1:
      return False
    if bstack11llll1111_opy_ == None or os.path.exists(bstack11llll1111_opy_) == False:
      self.logger.warn(bstack1ll_opy_ (u"ࠧࡖࡥࡳࡥࡼࠤࡵࡧࡴࡩࠢࡱࡳࡹࠦࡦࡰࡷࡱࡨ࠱ࠦࡲࡦࡶࡵࡽ࡮ࡴࡧࠡࡦࡲࡻࡳࡲ࡯ࡢࡦࠥᇄ"))
      bstack11llll1111_opy_ = self.bstack1l11111111_opy_(bstack11llllll11_opy_, bstack11llll1l1l_opy_)
      self.bstack11lll1llll_opy_(bstack11llllll11_opy_, bstack11llll1l1l_opy_, bstack11llll1111_opy_, bstack11ll1llll1_opy_+1)
    bstack11ll11lll1_opy_ = bstack1ll_opy_ (u"ࠨ࡞࠯ࠬࡃࡴࡪࡸࡣࡺ࡞࠲ࡧࡱ࡯ࠠ࡝ࡦ࠱ࡠࡩ࠱࠮࡝ࡦ࠮ࠦᇅ")
    command = bstack1ll_opy_ (u"ࠧࡼࡿࠣ࠱࠲ࡼࡥࡳࡵ࡬ࡳࡳ࠭ᇆ").format(bstack11llll1111_opy_)
    bstack11lll1l1ll_opy_ = subprocess.check_output(command, shell=True, text=True)
    if re.match(bstack11ll11lll1_opy_, bstack11lll1l1ll_opy_) != None:
      return True
    else:
      self.logger.error(bstack1ll_opy_ (u"ࠣࡒࡨࡶࡨࡿࠠࡷࡧࡵࡷ࡮ࡵ࡮ࠡࡥ࡫ࡩࡨࡱࠠࡧࡣ࡬ࡰࡪࡪࠢᇇ"))
      bstack11llll1111_opy_ = self.bstack1l11111111_opy_(bstack11llllll11_opy_, bstack11llll1l1l_opy_)
      self.bstack11lll1llll_opy_(bstack11llllll11_opy_, bstack11llll1l1l_opy_, bstack11llll1111_opy_, bstack11ll1llll1_opy_+1)
  def bstack11ll1ll11l_opy_(self, bstack11lllll1l1_opy_, bstack11llll1l1l_opy_):
    try:
      working_dir = os.path.dirname(bstack11lllll1l1_opy_)
      shutil.unpack_archive(bstack11lllll1l1_opy_, working_dir)
      bstack11llll1111_opy_ = os.path.join(working_dir, bstack11llll1l1l_opy_)
      os.chmod(bstack11llll1111_opy_, 0o755)
      return bstack11llll1111_opy_
    except Exception as e:
      self.logger.error(bstack1ll_opy_ (u"ࠤࡘࡲࡦࡨ࡬ࡦࠢࡷࡳࠥࡻ࡮ࡻ࡫ࡳࠤࡵ࡫ࡲࡤࡻࠣࡦ࡮ࡴࡡࡳࡻࠥᇈ"))
  def bstack11ll1lll1l_opy_(self):
    try:
      percy = str(self.config.get(bstack1ll_opy_ (u"ࠪࡴࡪࡸࡣࡺࠩᇉ"), bstack1ll_opy_ (u"ࠦ࡫ࡧ࡬ࡴࡧࠥᇊ"))).lower()
      if percy != bstack1ll_opy_ (u"ࠧࡺࡲࡶࡧࠥᇋ"):
        return False
      self.bstack11lll11ll1_opy_ = True
      return True
    except Exception as e:
      self.logger.error(bstack1ll_opy_ (u"ࠨࡕ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡧࡩࡹ࡫ࡣࡵࠢࡳࡩࡷࡩࡹ࠭ࠢࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥࢁࡽࠣᇌ").format(e))
  def init(self, bstack11l1l1ll_opy_, config, logger):
    self.bstack11l1l1ll_opy_ = bstack11l1l1ll_opy_
    self.config = config
    self.logger = logger
    if not self.bstack11ll1lll1l_opy_():
      return
    self.bstack11ll1l111l_opy_ = config.get(bstack1ll_opy_ (u"ࠧࡱࡧࡵࡧࡾࡕࡰࡵ࡫ࡲࡲࡸ࠭ᇍ"), {})
    try:
      bstack11llllll11_opy_, bstack11llll1l1l_opy_ = self.bstack11lll1ll11_opy_()
      bstack11llll1111_opy_, bstack11lll11lll_opy_ = self.bstack11lll111ll_opy_(bstack11llllll11_opy_, bstack11llll1l1l_opy_)
      if bstack11lll11lll_opy_:
        self.binary_path = bstack11llll1111_opy_
        thread = Thread(target=self.bstack11lll1111l_opy_)
        thread.start()
      else:
        self.bstack11llll1ll1_opy_ = True
        self.logger.error(bstack1ll_opy_ (u"ࠣࡋࡱࡺࡦࡲࡩࡥࠢࡳࡩࡷࡩࡹࠡࡲࡤࡸ࡭ࠦࡦࡰࡷࡱࡨࠥ࠳ࠠࡼࡿ࠯ࠤ࡚ࡴࡡࡣ࡮ࡨࠤࡹࡵࠠࡴࡶࡤࡶࡹࠦࡐࡦࡴࡦࡽࠧᇎ").format(bstack11llll1111_opy_))
    except Exception as e:
      self.logger.error(bstack1ll_opy_ (u"ࠤࡘࡲࡦࡨ࡬ࡦࠢࡷࡳࠥࡹࡴࡢࡴࡷࠤࡵ࡫ࡲࡤࡻ࠯ࠤࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡼࡿࠥᇏ").format(e))
  def bstack11ll11llll_opy_(self):
    try:
      logfile = os.path.join(self.working_dir, bstack1ll_opy_ (u"ࠪࡰࡴ࡭ࠧᇐ"), bstack1ll_opy_ (u"ࠫࡵ࡫ࡲࡤࡻ࠱ࡰࡴ࡭ࠧᇑ"))
      os.makedirs(os.path.dirname(logfile)) if not os.path.exists(os.path.dirname(logfile)) else None
      self.logger.debug(bstack1ll_opy_ (u"ࠧࡖࡵࡴࡪ࡬ࡲ࡬ࠦࡰࡦࡴࡦࡽࠥࡲ࡯ࡨࡵࠣࡥࡹࠦࡻࡾࠤᇒ").format(logfile))
      self.bstack11llll1l11_opy_ = logfile
    except Exception as e:
      self.logger.error(bstack1ll_opy_ (u"ࠨࡕ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡶࡩࡹࠦࡰࡦࡴࡦࡽࠥࡲ࡯ࡨࠢࡳࡥࡹ࡮ࠬࠡࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤࢀࢃࠢᇓ").format(e))
  def bstack11lll1111l_opy_(self):
    bstack11lll11111_opy_ = self.bstack11lll1ll1l_opy_()
    if bstack11lll11111_opy_ == None:
      self.bstack11llll1ll1_opy_ = True
      self.logger.error(bstack1ll_opy_ (u"ࠢࡑࡧࡵࡧࡾࠦࡴࡰ࡭ࡨࡲࠥࡴ࡯ࡵࠢࡩࡳࡺࡴࡤ࠭ࠢࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡹࡴࡢࡴࡷࠤࡵ࡫ࡲࡤࡻࠥᇔ"))
      return False
    command_args = [bstack1ll_opy_ (u"ࠣࡣࡳࡴ࠿࡫ࡸࡦࡥ࠽ࡷࡹࡧࡲࡵࠤᇕ") if self.bstack11l1l1ll_opy_ else bstack1ll_opy_ (u"ࠩࡨࡼࡪࡩ࠺ࡴࡶࡤࡶࡹ࠭ᇖ")]
    bstack11ll11ll1l_opy_ = self.bstack11llll11l1_opy_()
    if bstack11ll11ll1l_opy_ != None:
      command_args.append(bstack1ll_opy_ (u"ࠥ࠱ࡨࠦࡻࡾࠤᇗ").format(bstack11ll11ll1l_opy_))
    env = os.environ.copy()
    env[bstack1ll_opy_ (u"ࠦࡕࡋࡒࡄ࡛ࡢࡘࡔࡑࡅࡏࠤᇘ")] = bstack11lll11111_opy_
    bstack11llll1lll_opy_ = [self.binary_path]
    self.bstack11ll11llll_opy_()
    self.bstack11ll1l1ll1_opy_ = self.bstack11lll11l1l_opy_(bstack11llll1lll_opy_ + command_args, env)
    self.logger.debug(bstack1ll_opy_ (u"࡙ࠧࡴࡢࡴࡷ࡭ࡳ࡭ࠠࡉࡧࡤࡰࡹ࡮ࠠࡄࡪࡨࡧࡰࠨᇙ"))
    bstack11ll1llll1_opy_ = 0
    while self.bstack11ll1l1ll1_opy_.poll() == None:
      bstack11ll1ll1ll_opy_ = self.bstack11llllllll_opy_()
      if bstack11ll1ll1ll_opy_:
        self.logger.debug(bstack1ll_opy_ (u"ࠨࡈࡦࡣ࡯ࡸ࡭ࠦࡃࡩࡧࡦ࡯ࠥࡹࡵࡤࡥࡨࡷࡸ࡬ࡵ࡭ࠤᇚ"))
        self.bstack11lll1l11l_opy_ = True
        return True
      bstack11ll1llll1_opy_ += 1
      self.logger.debug(bstack1ll_opy_ (u"ࠢࡉࡧࡤࡰࡹ࡮ࠠࡄࡪࡨࡧࡰࠦࡒࡦࡶࡵࡽࠥ࠳ࠠࡼࡿࠥᇛ").format(bstack11ll1llll1_opy_))
      time.sleep(2)
    self.logger.error(bstack1ll_opy_ (u"ࠣࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡸࡺࡡࡳࡶࠣࡴࡪࡸࡣࡺ࠮ࠣࡌࡪࡧ࡬ࡵࡪࠣࡇ࡭࡫ࡣ࡬ࠢࡉࡥ࡮ࡲࡥࡥࠢࡤࡪࡹ࡫ࡲࠡࡽࢀࠤࡦࡺࡴࡦ࡯ࡳࡸࡸࠨᇜ").format(bstack11ll1llll1_opy_))
    self.bstack11llll1ll1_opy_ = True
    return False
  def bstack11llllllll_opy_(self, bstack11ll1llll1_opy_ = 0):
    try:
      if bstack11ll1llll1_opy_ > 10:
        return False
      bstack11llll11ll_opy_ = os.environ.get(bstack1ll_opy_ (u"ࠩࡓࡉࡗࡉ࡙ࡠࡕࡈࡖ࡛ࡋࡒࡠࡃࡇࡈࡗࡋࡓࡔࠩᇝ"), bstack1ll_opy_ (u"ࠪ࡬ࡹࡺࡰ࠻࠱࠲ࡰࡴࡩࡡ࡭ࡪࡲࡷࡹࡀ࠵࠴࠵࠻ࠫᇞ"))
      bstack11ll1l1l11_opy_ = bstack11llll11ll_opy_ + bstack1l1l11ll11_opy_
      response = requests.get(bstack11ll1l1l11_opy_)
      return True if response.json() else False
    except:
      return False
  def bstack11lll1ll1l_opy_(self):
    bstack11ll1l1111_opy_ = bstack1ll_opy_ (u"ࠫࡦࡶࡰࠨᇟ") if self.bstack11l1l1ll_opy_ else bstack1ll_opy_ (u"ࠬࡧࡵࡵࡱࡰࡥࡹ࡫ࠧᇠ")
    bstack1l11llllll_opy_ = bstack1ll_opy_ (u"ࠨࡡࡱ࡫࠲ࡥࡵࡶ࡟ࡱࡧࡵࡧࡾ࠵ࡧࡦࡶࡢࡴࡷࡵࡪࡦࡥࡷࡣࡹࡵ࡫ࡦࡰࡂࡲࡦࡳࡥ࠾ࡽࢀࠪࡹࡿࡰࡦ࠿ࡾࢁࠧᇡ").format(self.config[bstack1ll_opy_ (u"ࠧࡱࡴࡲ࡮ࡪࡩࡴࡏࡣࡰࡩࠬᇢ")], bstack11ll1l1111_opy_)
    uri = bstack1lll1ll1l1_opy_(bstack1l11llllll_opy_)
    try:
      response = bstack1llll1l11l_opy_(bstack1ll_opy_ (u"ࠨࡉࡈࡘࠬᇣ"), uri, {}, {bstack1ll_opy_ (u"ࠩࡤࡹࡹ࡮ࠧᇤ"): (self.config[bstack1ll_opy_ (u"ࠪࡹࡸ࡫ࡲࡏࡣࡰࡩࠬᇥ")], self.config[bstack1ll_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶࡏࡪࡿࠧᇦ")])})
      if response.status_code == 200:
        bstack11ll1l1l1l_opy_ = response.json()
        if bstack1ll_opy_ (u"ࠧࡺ࡯࡬ࡧࡱࠦᇧ") in bstack11ll1l1l1l_opy_:
          return bstack11ll1l1l1l_opy_[bstack1ll_opy_ (u"ࠨࡴࡰ࡭ࡨࡲࠧᇨ")]
        else:
          raise bstack1ll_opy_ (u"ࠧࡕࡱ࡮ࡩࡳࠦࡎࡰࡶࠣࡊࡴࡻ࡮ࡥࠢ࠰ࠤࢀࢃࠧᇩ").format(bstack11ll1l1l1l_opy_)
      else:
        raise bstack1ll_opy_ (u"ࠣࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤ࡫࡫ࡴࡤࡪࠣࡴࡪࡸࡣࡺࠢࡷࡳࡰ࡫࡮࠭ࠢࡕࡩࡸࡶ࡯࡯ࡵࡨࠤࡸࡺࡡࡵࡷࡶࠤ࠲ࠦࡻࡾ࠮ࠣࡖࡪࡹࡰࡰࡰࡶࡩࠥࡈ࡯ࡥࡻࠣ࠱ࠥࢁࡽࠣᇪ").format(response.status_code, response.json())
    except Exception as e:
      self.logger.error(bstack1ll_opy_ (u"ࠤࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡥࡵࡩࡦࡺࡩ࡯ࡩࠣࡴࡪࡸࡣࡺࠢࡳࡶࡴࡰࡥࡤࡶࠥᇫ").format(e))
  def bstack11llll11l1_opy_(self):
    bstack11llll111l_opy_ = os.path.join(tempfile.gettempdir(), bstack1ll_opy_ (u"ࠥࡴࡪࡸࡣࡺࡅࡲࡲ࡫࡯ࡧ࠯࡬ࡶࡳࡳࠨᇬ"))
    try:
      if bstack1ll_opy_ (u"ࠫࡻ࡫ࡲࡴ࡫ࡲࡲࠬᇭ") not in self.bstack11ll1l111l_opy_:
        self.bstack11ll1l111l_opy_[bstack1ll_opy_ (u"ࠬࡼࡥࡳࡵ࡬ࡳࡳ࠭ᇮ")] = 2
      with open(bstack11llll111l_opy_, bstack1ll_opy_ (u"࠭ࡷࠨᇯ")) as fp:
        json.dump(self.bstack11ll1l111l_opy_, fp)
      return bstack11llll111l_opy_
    except Exception as e:
      self.logger.error(bstack1ll_opy_ (u"ࠢࡖࡰࡤࡦࡱ࡫ࠠࡵࡱࠣࡧࡷ࡫ࡡࡵࡧࠣࡴࡪࡸࡣࡺࠢࡦࡳࡳ࡬ࠬࠡࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤࢀࢃࠢᇰ").format(e))
  def bstack11lll11l1l_opy_(self, cmd, env = os.environ.copy()):
    try:
      if self.bstack11llllll1l_opy_ == bstack1ll_opy_ (u"ࠨࡹ࡬ࡲࠬᇱ"):
        bstack11ll1l11ll_opy_ = [bstack1ll_opy_ (u"ࠩࡦࡱࡩ࠴ࡥࡹࡧࠪᇲ"), bstack1ll_opy_ (u"ࠪ࠳ࡨ࠭ᇳ")]
        cmd = bstack11ll1l11ll_opy_ + cmd
      cmd = bstack1ll_opy_ (u"ࠫࠥ࠭ᇴ").join(cmd)
      self.logger.debug(bstack1ll_opy_ (u"ࠧࡘࡵ࡯ࡰ࡬ࡲ࡬ࠦࡻࡾࠤᇵ").format(cmd))
      with open(self.bstack11llll1l11_opy_, bstack1ll_opy_ (u"ࠨࡡࠣᇶ")) as bstack11lll111l1_opy_:
        process = subprocess.Popen(cmd, shell=True, stdout=bstack11lll111l1_opy_, text=True, stderr=bstack11lll111l1_opy_, env=env, universal_newlines=True)
      return process
    except Exception as e:
      self.bstack11llll1ll1_opy_ = True
      self.logger.error(bstack1ll_opy_ (u"ࠢࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡷࡹࡧࡲࡵࠢࡳࡩࡷࡩࡹࠡࡹ࡬ࡸ࡭ࠦࡣ࡮ࡦࠣ࠱ࠥࢁࡽ࠭ࠢࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲ࠿ࠦࡻࡾࠤᇷ").format(cmd, e))
  def shutdown(self):
    try:
      if self.bstack11lll1l11l_opy_:
        self.logger.info(bstack1ll_opy_ (u"ࠣࡕࡷࡳࡵࡶࡩ࡯ࡩࠣࡔࡪࡸࡣࡺࠤᇸ"))
        cmd = [self.binary_path, bstack1ll_opy_ (u"ࠤࡨࡼࡪࡩ࠺ࡴࡶࡲࡴࠧᇹ")]
        self.bstack11lll11l1l_opy_(cmd)
        self.bstack11lll1l11l_opy_ = False
    except Exception as e:
      self.logger.error(bstack1ll_opy_ (u"ࠥࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡳࡵࡱࡳࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠥࡽࡩࡵࡪࠣࡧࡴࡳ࡭ࡢࡰࡧࠤ࠲ࠦࡻࡾ࠮ࠣࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࡀࠠࡼࡿࠥᇺ").format(cmd, e))
  def bstack1111ll11_opy_(self):
    if not self.bstack11lll11ll1_opy_:
      return
    try:
      bstack11ll1l1lll_opy_ = 0
      while not self.bstack11lll1l11l_opy_ and bstack11ll1l1lll_opy_ < self.bstack11lllll11l_opy_:
        if self.bstack11llll1ll1_opy_:
          self.logger.info(bstack1ll_opy_ (u"ࠦࡕ࡫ࡲࡤࡻࠣࡷࡪࡺࡵࡱࠢࡩࡥ࡮ࡲࡥࡥࠤᇻ"))
          return
        time.sleep(1)
        bstack11ll1l1lll_opy_ += 1
      os.environ[bstack1ll_opy_ (u"ࠬࡖࡅࡓࡅ࡜ࡣࡇࡋࡓࡕࡡࡓࡐࡆ࡚ࡆࡐࡔࡐࠫᇼ")] = str(self.bstack11lll1lll1_opy_())
      self.logger.info(bstack1ll_opy_ (u"ࠨࡐࡦࡴࡦࡽࠥࡹࡥࡵࡷࡳࠤࡨࡵ࡭ࡱ࡮ࡨࡸࡪࡪࠢᇽ"))
    except Exception as e:
      self.logger.error(bstack1ll_opy_ (u"ࠢࡖࡰࡤࡦࡱ࡫ࠠࡵࡱࠣࡷࡪࡺࡵࡱࠢࡳࡩࡷࡩࡹ࠭ࠢࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥࢁࡽࠣᇾ").format(e))
  def bstack11lll1lll1_opy_(self):
    if self.bstack11l1l1ll_opy_:
      return
    try:
      bstack11ll1lll11_opy_ = [platform[bstack1ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡐࡤࡱࡪ࠭ᇿ")].lower() for platform in self.config.get(bstack1ll_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬሀ"), [])]
      bstack11ll1lllll_opy_ = sys.maxsize
      bstack11ll1ll111_opy_ = bstack1ll_opy_ (u"ࠪࠫሁ")
      for browser in bstack11ll1lll11_opy_:
        if browser in self.bstack11ll1ll1l1_opy_:
          bstack11lllll111_opy_ = self.bstack11ll1ll1l1_opy_[browser]
        if bstack11lllll111_opy_ < bstack11ll1lllll_opy_:
          bstack11ll1lllll_opy_ = bstack11lllll111_opy_
          bstack11ll1ll111_opy_ = browser
      return bstack11ll1ll111_opy_
    except Exception as e:
      self.logger.error(bstack1ll_opy_ (u"࡚ࠦࡴࡡࡣ࡮ࡨࠤࡹࡵࠠࡧ࡫ࡱࡨࠥࡨࡥࡴࡶࠣࡴࡱࡧࡴࡧࡱࡵࡱ࠱ࠦࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢࡾࢁࠧሂ").format(e))