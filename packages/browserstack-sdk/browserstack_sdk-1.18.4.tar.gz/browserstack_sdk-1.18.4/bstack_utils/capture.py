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
import sys
class bstack1l1l1l11ll_opy_:
    def __init__(self, handler):
        self._1l1l1l11l1_opy_ = sys.stdout.write
        self._1l1l1l111l_opy_ = sys.stderr.write
        self.handler = handler
        self._started = False
    def start(self):
        if self._started:
            return
        self._started = True
        sys.stdout.write = self.bstack1l1l1l1l1l_opy_
        sys.stdout.error = self.bstack1l1l1l1l11_opy_
    def bstack1l1l1l1l1l_opy_(self, _str):
        self._1l1l1l11l1_opy_(_str)
        if self.handler:
            self.handler({bstack1ll_opy_ (u"࠭࡬ࡦࡸࡨࡰࠬ൞"): bstack1ll_opy_ (u"ࠧࡊࡐࡉࡓࠬൟ"), bstack1ll_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩൠ"): _str})
    def bstack1l1l1l1l11_opy_(self, _str):
        self._1l1l1l111l_opy_(_str)
        if self.handler:
            self.handler({bstack1ll_opy_ (u"ࠩ࡯ࡩࡻ࡫࡬ࠨൡ"): bstack1ll_opy_ (u"ࠪࡉࡗࡘࡏࡓࠩൢ"), bstack1ll_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬൣ"): _str})
    def reset(self):
        if not self._started:
            return
        self._started = False
        sys.stdout.write = self._1l1l1l11l1_opy_
        sys.stderr.write = self._1l1l1l111l_opy_