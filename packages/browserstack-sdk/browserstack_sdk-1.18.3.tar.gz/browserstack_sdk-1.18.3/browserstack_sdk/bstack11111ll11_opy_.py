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
import multiprocessing
import os
from browserstack_sdk.bstack1l1l11ll_opy_ import *
from bstack_utils.helper import bstack1llllll111_opy_
from bstack_utils.messages import bstack11l11l1ll_opy_
from bstack_utils.constants import bstack11llllll_opy_
class bstack1l1ll1lll_opy_:
    def __init__(self, args, logger, bstack1ll111l111_opy_, bstack1ll1111l11_opy_):
        self.args = args
        self.logger = logger
        self.bstack1ll111l111_opy_ = bstack1ll111l111_opy_
        self.bstack1ll1111l11_opy_ = bstack1ll1111l11_opy_
        self._prepareconfig = None
        self.Config = None
        self.runner = None
        self.bstack1l11l1lll_opy_ = []
        self.bstack1ll111l11l_opy_ = None
        self.bstack1l1l1l11l_opy_ = []
        self.bstack1ll111l1l1_opy_ = self.bstack1lll111111_opy_()
        self.bstack1l111ll1_opy_ = -1
    def bstack11lllllll_opy_(self, bstack1ll111lll1_opy_):
        self.parse_args()
        self.bstack1ll1111l1l_opy_()
        self.bstack1ll111llll_opy_(bstack1ll111lll1_opy_)
    @staticmethod
    def version():
        import pytest
        return pytest.__version__
    def bstack1ll1111ll1_opy_(self, arg):
        if arg in self.args:
            i = self.args.index(arg)
            self.args.pop(i + 1)
            self.args.pop(i)
    def parse_args(self):
        self.bstack1l111ll1_opy_ = -1
        if bstack111ll1l_opy_ (u"࠭ࡰࡢࡴࡤࡰࡱ࡫࡬ࡴࡒࡨࡶࡕࡲࡡࡵࡨࡲࡶࡲ࠭ಡ") in self.bstack1ll111l111_opy_:
            self.bstack1l111ll1_opy_ = self.bstack1ll111l111_opy_[bstack111ll1l_opy_ (u"ࠧࡱࡣࡵࡥࡱࡲࡥ࡭ࡵࡓࡩࡷࡖ࡬ࡢࡶࡩࡳࡷࡳࠧಢ")]
        try:
            bstack1ll1111lll_opy_ = [bstack111ll1l_opy_ (u"ࠨ࠯࠰ࡨࡷ࡯ࡶࡦࡴࠪಣ"), bstack111ll1l_opy_ (u"ࠩ࠰࠱ࡵࡲࡵࡨ࡫ࡱࡷࠬತ"), bstack111ll1l_opy_ (u"ࠪ࠱ࡵ࠭ಥ")]
            if self.bstack1l111ll1_opy_ >= 0:
                bstack1ll1111lll_opy_.extend([bstack111ll1l_opy_ (u"ࠫ࠲࠳࡮ࡶ࡯ࡳࡶࡴࡩࡥࡴࡵࡨࡷࠬದ"), bstack111ll1l_opy_ (u"ࠬ࠳࡮ࠨಧ")])
            for arg in bstack1ll1111lll_opy_:
                self.bstack1ll1111ll1_opy_(arg)
        except Exception as exc:
            self.logger.error(str(exc))
    def get_args(self):
        return self.args
    def bstack1ll1111l1l_opy_(self):
        bstack1ll111l11l_opy_ = [os.path.normpath(item) for item in self.args]
        self.bstack1ll111l11l_opy_ = bstack1ll111l11l_opy_
        return bstack1ll111l11l_opy_
    def bstack1ll1l1lll_opy_(self):
        try:
            from _pytest.config import _prepareconfig
            from _pytest.config import Config
            from _pytest import runner
            import importlib
            bstack1ll111ll1l_opy_ = importlib.find_loader(bstack111ll1l_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹࡥࡳࡦ࡮ࡨࡲ࡮ࡻ࡭ࠨನ"))
            self._prepareconfig = _prepareconfig
            self.Config = Config
            self.runner = runner
        except Exception as e:
            self.logger.warn(e, bstack11l11l1ll_opy_)
    def bstack1ll111llll_opy_(self, bstack1ll111lll1_opy_):
        if bstack1ll111lll1_opy_:
            self.bstack1ll111l11l_opy_.append(bstack111ll1l_opy_ (u"ࠧ࠮࠯ࡶ࡯࡮ࡶࡓࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠫ಩"))
            self.bstack1ll111l11l_opy_.append(bstack111ll1l_opy_ (u"ࠨࡖࡵࡹࡪ࠭ಪ"))
        self.bstack1ll111l11l_opy_.append(bstack111ll1l_opy_ (u"ࠩ࠰ࡴࠬಫ"))
        self.bstack1ll111l11l_opy_.append(bstack111ll1l_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࡢࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡲ࡯ࡹ࡬࡯࡮ࠨಬ"))
        self.bstack1ll111l11l_opy_.append(bstack111ll1l_opy_ (u"ࠫ࠲࠳ࡤࡳ࡫ࡹࡩࡷ࠭ಭ"))
        self.bstack1ll111l11l_opy_.append(bstack111ll1l_opy_ (u"ࠬࡩࡨࡳࡱࡰࡩࠬಮ"))
        if self.bstack1l111ll1_opy_ > 1:
            self.bstack1ll111l11l_opy_.append(bstack111ll1l_opy_ (u"࠭࠭࡯ࠩಯ"))
            self.bstack1ll111l11l_opy_.append(str(self.bstack1l111ll1_opy_))
    def bstack1ll111l1ll_opy_(self):
        bstack1l1l1l11l_opy_ = []
        for spec in self.bstack1l11l1lll_opy_:
            bstack1lll1111ll_opy_ = [spec]
            bstack1lll1111ll_opy_ += self.bstack1ll111l11l_opy_
            bstack1l1l1l11l_opy_.append(bstack1lll1111ll_opy_)
        self.bstack1l1l1l11l_opy_ = bstack1l1l1l11l_opy_
        return bstack1l1l1l11l_opy_
    def bstack1lll111111_opy_(self):
        try:
            from pytest_bdd import reporting
            self.bstack1ll111l1l1_opy_ = True
            return True
        except Exception as e:
            self.bstack1ll111l1l1_opy_ = False
        return self.bstack1ll111l1l1_opy_
    def bstack1lll111l_opy_(self, bstack1ll111ll11_opy_, bstack11lllllll_opy_):
        bstack11lllllll_opy_[bstack111ll1l_opy_ (u"ࠧࡄࡑࡑࡊࡎࡍࠧರ")] = self.bstack1ll111l111_opy_
        multiprocessing.set_start_method(bstack111ll1l_opy_ (u"ࠨࡵࡳࡥࡼࡴࠧಱ"))
        if bstack111ll1l_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬಲ") in self.bstack1ll111l111_opy_:
            bstack11l11l1l_opy_ = []
            manager = multiprocessing.Manager()
            bstack111111ll_opy_ = manager.list()
            for index, platform in enumerate(self.bstack1ll111l111_opy_[bstack111ll1l_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ಳ")]):
                bstack11l11l1l_opy_.append(multiprocessing.Process(name=str(index),
                                                           target=bstack1ll111ll11_opy_,
                                                           args=(self.bstack1ll111l11l_opy_, bstack11lllllll_opy_)))
            i = 0
            for t in bstack11l11l1l_opy_:
                os.environ[bstack111ll1l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡔࡑࡇࡔࡇࡑࡕࡑࡤࡏࡎࡅࡇ࡛ࠫ಴")] = str(i)
                i += 1
                t.start()
            for t in bstack11l11l1l_opy_:
                t.join()
            return bstack111111ll_opy_