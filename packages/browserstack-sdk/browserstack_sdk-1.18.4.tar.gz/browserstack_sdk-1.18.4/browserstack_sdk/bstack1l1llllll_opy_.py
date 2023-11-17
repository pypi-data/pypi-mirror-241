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
import multiprocessing
import os
from browserstack_sdk.bstack1ll1ll11l_opy_ import *
from bstack_utils.helper import bstack11ll111ll_opy_
from bstack_utils.messages import bstack1ll1lll1_opy_
from bstack_utils.constants import bstack111ll11l_opy_
class bstack1ll1l1l1l_opy_:
    def __init__(self, args, logger, bstack1l1lll1lll_opy_, bstack1l1llll111_opy_):
        self.args = args
        self.logger = logger
        self.bstack1l1lll1lll_opy_ = bstack1l1lll1lll_opy_
        self.bstack1l1llll111_opy_ = bstack1l1llll111_opy_
        self._prepareconfig = None
        self.Config = None
        self.runner = None
        self.bstack1lll111ll1_opy_ = []
        self.bstack1l1lll1ll1_opy_ = None
        self.bstack1lll1ll11_opy_ = []
        self.bstack1l1lllll1l_opy_ = self.bstack111l11l1l_opy_()
        self.bstack1l1l1lll_opy_ = -1
    def bstack1111ll11l_opy_(self, bstack1l1llll11l_opy_):
        self.parse_args()
        self.bstack1l1lll11ll_opy_()
        self.bstack1l1llll1ll_opy_(bstack1l1llll11l_opy_)
    @staticmethod
    def version():
        import pytest
        return pytest.__version__
    def bstack1l1lllll11_opy_(self, arg):
        if arg in self.args:
            i = self.args.index(arg)
            self.args.pop(i + 1)
            self.args.pop(i)
    def parse_args(self):
        self.bstack1l1l1lll_opy_ = -1
        if bstack1ll_opy_ (u"ࠩࡳࡥࡷࡧ࡬࡭ࡧ࡯ࡷࡕ࡫ࡲࡑ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩಲ") in self.bstack1l1lll1lll_opy_:
            self.bstack1l1l1lll_opy_ = self.bstack1l1lll1lll_opy_[bstack1ll_opy_ (u"ࠪࡴࡦࡸࡡ࡭࡮ࡨࡰࡸࡖࡥࡳࡒ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪಳ")]
        try:
            bstack1l1lll1l1l_opy_ = [bstack1ll_opy_ (u"ࠫ࠲࠳ࡤࡳ࡫ࡹࡩࡷ࠭಴"), bstack1ll_opy_ (u"ࠬ࠳࠭ࡱ࡮ࡸ࡫࡮ࡴࡳࠨವ"), bstack1ll_opy_ (u"࠭࠭ࡱࠩಶ")]
            if self.bstack1l1l1lll_opy_ >= 0:
                bstack1l1lll1l1l_opy_.extend([bstack1ll_opy_ (u"ࠧ࠮࠯ࡱࡹࡲࡶࡲࡰࡥࡨࡷࡸ࡫ࡳࠨಷ"), bstack1ll_opy_ (u"ࠨ࠯ࡱࠫಸ")])
            for arg in bstack1l1lll1l1l_opy_:
                self.bstack1l1lllll11_opy_(arg)
        except Exception as exc:
            self.logger.error(str(exc))
    def get_args(self):
        return self.args
    def bstack1l1lll11ll_opy_(self):
        bstack1l1lll1ll1_opy_ = [os.path.normpath(item) for item in self.args]
        self.bstack1l1lll1ll1_opy_ = bstack1l1lll1ll1_opy_
        return bstack1l1lll1ll1_opy_
    def bstack1l1l111l1_opy_(self):
        try:
            from _pytest.config import _prepareconfig
            from _pytest.config import Config
            from _pytest import runner
            import importlib
            bstack1l1lll1l11_opy_ = importlib.find_loader(bstack1ll_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࡡࡶࡩࡱ࡫࡮ࡪࡷࡰࠫಹ"))
            self._prepareconfig = _prepareconfig
            self.Config = Config
            self.runner = runner
        except Exception as e:
            self.logger.warn(e, bstack1ll1lll1_opy_)
    def bstack1l1llll1ll_opy_(self, bstack1l1llll11l_opy_):
        if bstack1l1llll11l_opy_:
            self.bstack1l1lll1ll1_opy_.append(bstack1ll_opy_ (u"ࠪ࠱࠲ࡹ࡫ࡪࡲࡖࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠧ಺"))
            self.bstack1l1lll1ll1_opy_.append(bstack1ll_opy_ (u"࡙ࠫࡸࡵࡦࠩ಻"))
        self.bstack1l1lll1ll1_opy_.append(bstack1ll_opy_ (u"ࠬ࠳ࡰࠨ಼"))
        self.bstack1l1lll1ll1_opy_.append(bstack1ll_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹࡥࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡵࡲࡵࡨ࡫ࡱࠫಽ"))
        self.bstack1l1lll1ll1_opy_.append(bstack1ll_opy_ (u"ࠧ࠮࠯ࡧࡶ࡮ࡼࡥࡳࠩಾ"))
        self.bstack1l1lll1ll1_opy_.append(bstack1ll_opy_ (u"ࠨࡥ࡫ࡶࡴࡳࡥࠨಿ"))
        if self.bstack1l1l1lll_opy_ > 1:
            self.bstack1l1lll1ll1_opy_.append(bstack1ll_opy_ (u"ࠩ࠰ࡲࠬೀ"))
            self.bstack1l1lll1ll1_opy_.append(str(self.bstack1l1l1lll_opy_))
    def bstack1l1llllll1_opy_(self):
        bstack1lll1ll11_opy_ = []
        for spec in self.bstack1lll111ll1_opy_:
            bstack1l1ll11l1_opy_ = [spec]
            bstack1l1ll11l1_opy_ += self.bstack1l1lll1ll1_opy_
            bstack1lll1ll11_opy_.append(bstack1l1ll11l1_opy_)
        self.bstack1lll1ll11_opy_ = bstack1lll1ll11_opy_
        return bstack1lll1ll11_opy_
    def bstack111l11l1l_opy_(self):
        try:
            from pytest_bdd import reporting
            self.bstack1l1lllll1l_opy_ = True
            return True
        except Exception as e:
            self.bstack1l1lllll1l_opy_ = False
        return self.bstack1l1lllll1l_opy_
    def bstack1111lllll_opy_(self, bstack1l1llll1l1_opy_, bstack1111ll11l_opy_):
        bstack1111ll11l_opy_[bstack1ll_opy_ (u"ࠪࡇࡔࡔࡆࡊࡉࠪು")] = self.bstack1l1lll1lll_opy_
        multiprocessing.set_start_method(bstack1ll_opy_ (u"ࠫࡸࡶࡡࡸࡰࠪೂ"))
        if bstack1ll_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨೃ") in self.bstack1l1lll1lll_opy_:
            bstack11l111111_opy_ = []
            manager = multiprocessing.Manager()
            bstack1l1ll1ll_opy_ = manager.list()
            for index, platform in enumerate(self.bstack1l1lll1lll_opy_[bstack1ll_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩೄ")]):
                bstack11l111111_opy_.append(multiprocessing.Process(name=str(index),
                                                           target=bstack1l1llll1l1_opy_,
                                                           args=(self.bstack1l1lll1ll1_opy_, bstack1111ll11l_opy_, bstack1l1ll1ll_opy_)))
            i = 0
            for t in bstack11l111111_opy_:
                os.environ[bstack1ll_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡐࡍࡃࡗࡊࡔࡘࡍࡠࡋࡑࡈࡊ࡞ࠧ೅")] = str(i)
                i += 1
                t.start()
            for t in bstack11l111111_opy_:
                t.join()
            return list(bstack1l1ll1ll_opy_)