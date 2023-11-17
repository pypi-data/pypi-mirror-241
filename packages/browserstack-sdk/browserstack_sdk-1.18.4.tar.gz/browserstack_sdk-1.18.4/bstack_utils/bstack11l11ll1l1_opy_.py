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
from uuid import uuid4
from bstack_utils.helper import bstack1lllll1ll1_opy_, bstack1l11l1l1ll_opy_
from bstack_utils.bstack1lll1l11_opy_ import bstack11l1llllll_opy_
class bstack11l11ll1ll_opy_:
    def __init__(self, name=None, code=None, uuid=None, file_path=None, bstack11l111llll_opy_=None, framework=None, tags=[], scope=[], bstack11l11llll1_opy_=None, bstack11l111l111_opy_=True, bstack11l111ll1l_opy_=None, bstack1l1l11ll_opy_=None, result=None, duration=None, meta={}):
        self.name = name
        self.code = code
        self.file_path = file_path
        self.uuid = uuid
        if not self.uuid and bstack11l111l111_opy_:
            self.uuid = uuid4().__str__()
        self.bstack11l111llll_opy_ = bstack11l111llll_opy_
        self.framework = framework
        self.tags = tags
        self.scope = scope
        self.bstack11l11llll1_opy_ = bstack11l11llll1_opy_
        self.bstack11l111ll1l_opy_ = bstack11l111ll1l_opy_
        self.bstack1l1l11ll_opy_ = bstack1l1l11ll_opy_
        self.result = result
        self.duration = duration
        self.meta = meta
    def bstack11l111lll1_opy_(self):
        if self.uuid:
            return self.uuid
        self.uuid = uuid4().__str__()
        return self.uuid
    def bstack11l11lll11_opy_(self):
        bstack11l11l11l1_opy_ = os.path.relpath(self.file_path, start=os.getcwd())
        return {
            bstack1ll_opy_ (u"ࠧࡧ࡫࡯ࡩࡤࡴࡡ࡮ࡧࠪኃ"): bstack11l11l11l1_opy_,
            bstack1ll_opy_ (u"ࠨ࡮ࡲࡧࡦࡺࡩࡰࡰࠪኄ"): bstack11l11l11l1_opy_,
            bstack1ll_opy_ (u"ࠩࡹࡧࡤ࡬ࡩ࡭ࡧࡳࡥࡹ࡮ࠧኅ"): bstack11l11l11l1_opy_
        }
    def set(self, **kwargs):
        for key, val in kwargs.items():
            if not hasattr(self, key):
                raise TypeError(bstack1ll_opy_ (u"࡙ࠥࡳ࡫ࡸࡱࡧࡦࡸࡪࡪࠠࡢࡴࡪࡹࡲ࡫࡮ࡵ࠼ࠣࠦኆ") + key)
            setattr(self, key, val)
    def bstack11l11l1lll_opy_(self):
        return {
            bstack1ll_opy_ (u"ࠫࡳࡧ࡭ࡦࠩኇ"): self.name,
            bstack1ll_opy_ (u"ࠬࡨ࡯ࡥࡻࠪኈ"): {
                bstack1ll_opy_ (u"࠭࡬ࡢࡰࡪࠫ኉"): bstack1ll_opy_ (u"ࠧࡱࡻࡷ࡬ࡴࡴࠧኊ"),
                bstack1ll_opy_ (u"ࠨࡥࡲࡨࡪ࠭ኋ"): self.code
            },
            bstack1ll_opy_ (u"ࠩࡶࡧࡴࡶࡥࡴࠩኌ"): self.scope,
            bstack1ll_opy_ (u"ࠪࡸࡦ࡭ࡳࠨኍ"): self.tags,
            bstack1ll_opy_ (u"ࠫ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱࠧ኎"): self.framework,
            bstack1ll_opy_ (u"ࠬࡹࡴࡢࡴࡷࡩࡩࡥࡡࡵࠩ኏"): self.bstack11l111llll_opy_
        }
    def bstack11l11ll11l_opy_(self):
        return {
         bstack1ll_opy_ (u"࠭࡭ࡦࡶࡤࠫነ"): self.meta
        }
    def bstack11l11l1ll1_opy_(self):
        return {
            bstack1ll_opy_ (u"ࠧࡤࡷࡶࡸࡴࡳࡒࡦࡴࡸࡲࡕࡧࡲࡢ࡯ࠪኑ"): {
                bstack1ll_opy_ (u"ࠨࡴࡨࡶࡺࡴ࡟࡯ࡣࡰࡩࠬኒ"): self.bstack11l11llll1_opy_
            }
        }
    def bstack11l11lll1l_opy_(self, bstack11l11lllll_opy_, details):
        step = next(filter(lambda st: st[bstack1ll_opy_ (u"ࠩ࡬ࡨࠬና")] == bstack11l11lllll_opy_, self.meta[bstack1ll_opy_ (u"ࠪࡷࡹ࡫ࡰࡴࠩኔ")]), None)
        step.update(details)
    def bstack11l11l1l1l_opy_(self, bstack11l11lllll_opy_):
        step = next(filter(lambda st: st[bstack1ll_opy_ (u"ࠫ࡮ࡪࠧን")] == bstack11l11lllll_opy_, self.meta[bstack1ll_opy_ (u"ࠬࡹࡴࡦࡲࡶࠫኖ")]), None)
        step.update({
            bstack1ll_opy_ (u"࠭ࡳࡵࡣࡵࡸࡪࡪ࡟ࡢࡶࠪኗ"): bstack1lllll1ll1_opy_()
        })
    def bstack11l11l111l_opy_(self, bstack11l11lllll_opy_, result):
        bstack11l111ll1l_opy_ = bstack1lllll1ll1_opy_()
        step = next(filter(lambda st: st[bstack1ll_opy_ (u"ࠧࡪࡦࠪኘ")] == bstack11l11lllll_opy_, self.meta[bstack1ll_opy_ (u"ࠨࡵࡷࡩࡵࡹࠧኙ")]), None)
        step.update({
            bstack1ll_opy_ (u"ࠩࡩ࡭ࡳ࡯ࡳࡩࡧࡧࡣࡦࡺࠧኚ"): bstack11l111ll1l_opy_,
            bstack1ll_opy_ (u"ࠪࡨࡺࡸࡡࡵ࡫ࡲࡲࠬኛ"): bstack1l11l1l1ll_opy_(step[bstack1ll_opy_ (u"ࠫࡸࡺࡡࡳࡶࡨࡨࡤࡧࡴࠨኜ")], bstack11l111ll1l_opy_),
            bstack1ll_opy_ (u"ࠬࡸࡥࡴࡷ࡯ࡸࠬኝ"): result.result,
            bstack1ll_opy_ (u"࠭ࡦࡢ࡫࡯ࡹࡷ࡫ࠧኞ"): str(result.exception) if result.exception else None
        })
    def bstack11l11l11ll_opy_(self):
        return {
            bstack1ll_opy_ (u"ࠧࡶࡷ࡬ࡨࠬኟ"): self.bstack11l111lll1_opy_(),
            **self.bstack11l11l1lll_opy_(),
            **self.bstack11l11lll11_opy_(),
            **self.bstack11l11ll11l_opy_()
        }
    def bstack11l111l1ll_opy_(self):
        data = {
            bstack1ll_opy_ (u"ࠨࡨ࡬ࡲ࡮ࡹࡨࡦࡦࡢࡥࡹ࠭አ"): self.bstack11l111ll1l_opy_,
            bstack1ll_opy_ (u"ࠩࡧࡹࡷࡧࡴࡪࡱࡱࡣ࡮ࡴ࡟࡮ࡵࠪኡ"): self.duration,
            bstack1ll_opy_ (u"ࠪࡶࡪࡹࡵ࡭ࡶࠪኢ"): self.result.result
        }
        if data[bstack1ll_opy_ (u"ࠫࡷ࡫ࡳࡶ࡮ࡷࠫኣ")] == bstack1ll_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬኤ"):
            data[bstack1ll_opy_ (u"࠭ࡦࡢ࡫࡯ࡹࡷ࡫࡟ࡵࡻࡳࡩࠬእ")] = self.result.bstack1l11l111l1_opy_()
            data[bstack1ll_opy_ (u"ࠧࡧࡣ࡬ࡰࡺࡸࡥࠨኦ")] = [{bstack1ll_opy_ (u"ࠨࡤࡤࡧࡰࡺࡲࡢࡥࡨࠫኧ"): self.result.bstack1l1l111l11_opy_()}]
        return data
    def bstack11l11l1l11_opy_(self):
        return {
            bstack1ll_opy_ (u"ࠩࡸࡹ࡮ࡪࠧከ"): self.bstack11l111lll1_opy_(),
            **self.bstack11l11l1lll_opy_(),
            **self.bstack11l11lll11_opy_(),
            **self.bstack11l111l1ll_opy_(),
            **self.bstack11l11ll11l_opy_()
        }
    def bstack11l11l1111_opy_(self, event, result=None):
        if result:
            self.result = result
        if event == bstack1ll_opy_ (u"ࠪࡘࡪࡹࡴࡓࡷࡱࡗࡹࡧࡲࡵࡧࡧࠫኩ"):
            return self.bstack11l11l11ll_opy_()
        elif event == bstack1ll_opy_ (u"࡙ࠫ࡫ࡳࡵࡔࡸࡲࡋ࡯࡮ࡪࡵ࡫ࡩࡩ࠭ኪ"):
            return self.bstack11l11l1l11_opy_()
    def bstack11l111l1l1_opy_(self):
        pass
    def stop(self, time=None, duration=None, result=None):
        self.bstack11l111ll1l_opy_ = time if time else bstack1lllll1ll1_opy_()
        self.duration = duration if duration else bstack1l11l1l1ll_opy_(self.bstack11l111llll_opy_, self.bstack11l111ll1l_opy_)
        if result:
            self.result = result
class bstack11l11ll111_opy_(bstack11l11ll1ll_opy_):
    def __init__(self, *args, hooks=[], **kwargs):
        self.hooks = hooks
        super().__init__(*args, **kwargs, bstack1l1l11ll_opy_=bstack1ll_opy_ (u"ࠬࡺࡥࡴࡶࠪካ"))
    @classmethod
    def bstack11l111ll11_opy_(cls, scenario, feature, test, **kwargs):
        steps = []
        for step in scenario.steps:
            steps.append({
                bstack1ll_opy_ (u"࠭ࡩࡥࠩኬ"): id(step),
                bstack1ll_opy_ (u"ࠧࡵࡧࡻࡸࠬክ"): step.name,
                bstack1ll_opy_ (u"ࠨ࡭ࡨࡽࡼࡵࡲࡥࠩኮ"): step.keyword,
            })
        return bstack11l11ll111_opy_(
            **kwargs,
            meta={
                bstack1ll_opy_ (u"ࠩࡩࡩࡦࡺࡵࡳࡧࠪኯ"): {
                    bstack1ll_opy_ (u"ࠪࡲࡦࡳࡥࠨኰ"): feature.name,
                    bstack1ll_opy_ (u"ࠫࡵࡧࡴࡩࠩ኱"): feature.filename,
                    bstack1ll_opy_ (u"ࠬࡪࡥࡴࡥࡵ࡭ࡵࡺࡩࡰࡰࠪኲ"): feature.description
                },
                bstack1ll_opy_ (u"࠭ࡳࡤࡧࡱࡥࡷ࡯࡯ࠨኳ"): {
                    bstack1ll_opy_ (u"ࠧ࡯ࡣࡰࡩࠬኴ"): scenario.name
                },
                bstack1ll_opy_ (u"ࠨࡵࡷࡩࡵࡹࠧኵ"): steps,
                bstack1ll_opy_ (u"ࠩࡨࡼࡦࡳࡰ࡭ࡧࡶࠫ኶"): bstack11l1llllll_opy_(test)
            }
        )
    def bstack11l111l11l_opy_(self):
        return {
            bstack1ll_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡴࠩ኷"): self.hooks
        }
    def bstack11l11l1l11_opy_(self):
        return {
            **super().bstack11l11l1l11_opy_(),
            **self.bstack11l111l11l_opy_()
        }
    def bstack11l111l1l1_opy_(self):
        return bstack1ll_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳ࠭ኸ")