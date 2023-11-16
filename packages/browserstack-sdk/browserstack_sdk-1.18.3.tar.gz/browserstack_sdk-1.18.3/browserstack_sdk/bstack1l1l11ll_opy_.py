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
import threading
class bstack111l1111l_opy_(threading.Thread):
    def run(self):
        self.exc = None
        try:
            self.ret = self._target(*self._args, **self._kwargs)
        except Exception as e:
            self.exc = e
    def join(self, timeout=None):
        super(bstack111l1111l_opy_, self).join(timeout)
        if self.exc:
            raise self.exc
        return self.ret