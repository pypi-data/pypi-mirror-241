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
class bstack11l1l1l1l1_opy_:
    def __init__(self, handler):
        self._11l1l11ll1_opy_ = None
        self.handler = handler
        self._11l1l11lll_opy_ = self.bstack11l1l1l111_opy_()
        self.patch()
    def patch(self):
        self._11l1l11ll1_opy_ = self._11l1l11lll_opy_.execute
        self._11l1l11lll_opy_.execute = self.bstack11l1l1l11l_opy_()
    def bstack11l1l1l11l_opy_(self):
        def execute(this, driver_command, *args, **kwargs):
            response = self._11l1l11ll1_opy_(this, driver_command, *args, **kwargs)
            self.handler(driver_command, response)
            return response
        return execute
    def reset(self):
        self._11l1l11lll_opy_.execute = self._11l1l11ll1_opy_
    @staticmethod
    def bstack11l1l1l111_opy_():
        from selenium.webdriver.remote.webdriver import WebDriver
        return WebDriver