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
import sys
class bstack1l1ll11l1l_opy_:
    def __init__(self, handler):
        self._1l1ll11l11_opy_ = sys.stdout.write
        self._1l1ll11ll1_opy_ = sys.stderr.write
        self.handler = handler
        self._started = False
    def start(self):
        if self._started:
            return
        self._started = True
        sys.stdout.write = self.bstack1l1ll111ll_opy_
        sys.stdout.error = self.bstack1l1ll111l1_opy_
    def bstack1l1ll111ll_opy_(self, _str):
        self._1l1ll11l11_opy_(_str)
        if self.handler:
            self.handler({bstack111ll1l_opy_ (u"ࠪࡰࡪࡼࡥ࡭്ࠩ"): bstack111ll1l_opy_ (u"ࠫࡎࡔࡆࡐࠩൎ"), bstack111ll1l_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ࠭൏"): _str})
    def bstack1l1ll111l1_opy_(self, _str):
        self._1l1ll11ll1_opy_(_str)
        if self.handler:
            self.handler({bstack111ll1l_opy_ (u"࠭࡬ࡦࡸࡨࡰࠬ൐"): bstack111ll1l_opy_ (u"ࠧࡆࡔࡕࡓࡗ࠭൑"), bstack111ll1l_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩ൒"): _str})
    def reset(self):
        if not self._started:
            return
        self._started = False
        sys.stdout.write = self._1l1ll11l11_opy_
        sys.stderr.write = self._1l1ll11ll1_opy_