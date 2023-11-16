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
class bstack11ll1111l1_opy_:
    def __init__(self, handler):
        self._11ll1111ll_opy_ = None
        self.handler = handler
        self._11ll111111_opy_ = self.bstack11l1llllll_opy_()
        self.patch()
    def patch(self):
        self._11ll1111ll_opy_ = self._11ll111111_opy_.execute
        self._11ll111111_opy_.execute = self.bstack11l1lllll1_opy_()
    def bstack11l1lllll1_opy_(self):
        def execute(this, driver_command, *args, **kwargs):
            response = self._11ll1111ll_opy_(this, driver_command, *args, **kwargs)
            self.handler(driver_command, response)
            return response
        return execute
    def reset(self):
        self._11ll111111_opy_.execute = self._11ll1111ll_opy_
    @staticmethod
    def bstack11l1llllll_opy_():
        from selenium.webdriver.remote.webdriver import WebDriver
        return WebDriver