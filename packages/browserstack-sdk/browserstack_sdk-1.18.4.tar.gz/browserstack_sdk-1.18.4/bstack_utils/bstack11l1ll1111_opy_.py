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
import threading
bstack11l1ll11l1_opy_ = 1000
bstack11l1l1l1ll_opy_ = 5
bstack11l1ll1l11_opy_ = 30
bstack11l1ll11ll_opy_ = 2
class bstack11l1ll1l1l_opy_:
    def __init__(self, handler, bstack11l1l1ll11_opy_=bstack11l1ll11l1_opy_, bstack11l1ll1ll1_opy_=bstack11l1l1l1ll_opy_):
        self.queue = []
        self.handler = handler
        self.bstack11l1l1ll11_opy_ = bstack11l1l1ll11_opy_
        self.bstack11l1ll1ll1_opy_ = bstack11l1ll1ll1_opy_
        self.lock = threading.Lock()
        self.timer = None
    def start(self):
        if not self.timer:
            self.bstack11l1l1ll1l_opy_()
    def bstack11l1l1ll1l_opy_(self):
        self.timer = threading.Timer(self.bstack11l1ll1ll1_opy_, self.bstack11l1l1llll_opy_)
        self.timer.start()
    def bstack11l1l1lll1_opy_(self):
        self.timer.cancel()
    def bstack11l1ll111l_opy_(self):
        self.bstack11l1l1lll1_opy_()
        self.bstack11l1l1ll1l_opy_()
    def add(self, event):
        with self.lock:
            self.queue.append(event)
            if len(self.queue) >= self.bstack11l1l1ll11_opy_:
                t = threading.Thread(target=self.bstack11l1l1llll_opy_)
                t.start()
                self.bstack11l1ll111l_opy_()
    def bstack11l1l1llll_opy_(self):
        if len(self.queue) <= 0:
            return
        data = self.queue[:self.bstack11l1l1ll11_opy_]
        del self.queue[:self.bstack11l1l1ll11_opy_]
        self.handler(data)
    def shutdown(self):
        self.bstack11l1l1lll1_opy_()
        while len(self.queue) > 0:
            self.bstack11l1l1llll_opy_()