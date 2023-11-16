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
import os
from uuid import uuid4
from bstack_utils.helper import bstack1111ll111_opy_, bstack1l11lll1l1_opy_
from bstack_utils.bstack1ll1l11l11_opy_ import bstack11ll1ll1l1_opy_
class bstack11l1l11ll1_opy_:
    def __init__(self, name=None, code=None, uuid=None, file_path=None, bstack11l1l11lll_opy_=None, framework=None, tags=[], scope=[], bstack11l1lll111_opy_=None, bstack11l1ll1lll_opy_=True, bstack11l1l111ll_opy_=None, bstack111l11l1_opy_=None, result=None, duration=None, meta={}):
        self.name = name
        self.code = code
        self.file_path = file_path
        self.uuid = uuid
        if not self.uuid and bstack11l1ll1lll_opy_:
            self.uuid = uuid4().__str__()
        self.bstack11l1l11lll_opy_ = bstack11l1l11lll_opy_
        self.framework = framework
        self.tags = tags
        self.scope = scope
        self.bstack11l1lll111_opy_ = bstack11l1lll111_opy_
        self.bstack11l1l111ll_opy_ = bstack11l1l111ll_opy_
        self.bstack111l11l1_opy_ = bstack111l11l1_opy_
        self.result = result
        self.duration = duration
        self.meta = meta
    def bstack11l1l1111l_opy_(self):
        if self.uuid:
            return self.uuid
        self.uuid = uuid4().__str__()
        return self.uuid
    def bstack11l1l1l1ll_opy_(self):
        bstack11l1l1ll11_opy_ = os.path.relpath(self.file_path, start=os.getcwd())
        return {
            bstack111ll1l_opy_ (u"ࠨࡨ࡬ࡰࡪࡥ࡮ࡢ࡯ࡨࠫቓ"): bstack11l1l1ll11_opy_,
            bstack111ll1l_opy_ (u"ࠩ࡯ࡳࡨࡧࡴࡪࡱࡱࠫቔ"): bstack11l1l1ll11_opy_,
            bstack111ll1l_opy_ (u"ࠪࡺࡨࡥࡦࡪ࡮ࡨࡴࡦࡺࡨࠨቕ"): bstack11l1l1ll11_opy_
        }
    def set(self, **kwargs):
        for key, val in kwargs.items():
            if not hasattr(self, key):
                raise TypeError(bstack111ll1l_opy_ (u"࡚ࠦࡴࡥࡹࡲࡨࡧࡹ࡫ࡤࠡࡣࡵ࡫ࡺࡳࡥ࡯ࡶ࠽ࠤࠧቖ") + key)
            setattr(self, key, val)
    def bstack11l1ll111l_opy_(self):
        return {
            bstack111ll1l_opy_ (u"ࠬࡴࡡ࡮ࡧࠪ቗"): self.name,
            bstack111ll1l_opy_ (u"࠭ࡢࡰࡦࡼࠫቘ"): {
                bstack111ll1l_opy_ (u"ࠧ࡭ࡣࡱ࡫ࠬ቙"): bstack111ll1l_opy_ (u"ࠨࡲࡼࡸ࡭ࡵ࡮ࠨቚ"),
                bstack111ll1l_opy_ (u"ࠩࡦࡳࡩ࡫ࠧቛ"): self.code
            },
            bstack111ll1l_opy_ (u"ࠪࡷࡨࡵࡰࡦࡵࠪቜ"): self.scope,
            bstack111ll1l_opy_ (u"ࠫࡹࡧࡧࡴࠩቝ"): self.tags,
            bstack111ll1l_opy_ (u"ࠬ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࠨ቞"): self.framework,
            bstack111ll1l_opy_ (u"࠭ࡳࡵࡣࡵࡸࡪࡪ࡟ࡢࡶࠪ቟"): self.bstack11l1l11lll_opy_
        }
    def bstack11l1ll1111_opy_(self):
        return {
         bstack111ll1l_opy_ (u"ࠧ࡮ࡧࡷࡥࠬበ"): self.meta
        }
    def bstack11l1ll1l11_opy_(self):
        return {
            bstack111ll1l_opy_ (u"ࠨࡥࡸࡷࡹࡵ࡭ࡓࡧࡵࡹࡳࡖࡡࡳࡣࡰࠫቡ"): {
                bstack111ll1l_opy_ (u"ࠩࡵࡩࡷࡻ࡮ࡠࡰࡤࡱࡪ࠭ቢ"): self.bstack11l1lll111_opy_
            }
        }
    def bstack11l1l1lll1_opy_(self, bstack11l1l1ll1l_opy_, details):
        step = next(filter(lambda st: st[bstack111ll1l_opy_ (u"ࠪ࡭ࡩ࠭ባ")] == bstack11l1l1ll1l_opy_, self.meta[bstack111ll1l_opy_ (u"ࠫࡸࡺࡥࡱࡵࠪቤ")]), None)
        step.update(details)
    def bstack11l1ll11l1_opy_(self, bstack11l1l1ll1l_opy_):
        step = next(filter(lambda st: st[bstack111ll1l_opy_ (u"ࠬ࡯ࡤࠨብ")] == bstack11l1l1ll1l_opy_, self.meta[bstack111ll1l_opy_ (u"࠭ࡳࡵࡧࡳࡷࠬቦ")]), None)
        step.update({
            bstack111ll1l_opy_ (u"ࠧࡴࡶࡤࡶࡹ࡫ࡤࡠࡣࡷࠫቧ"): bstack1111ll111_opy_()
        })
    def bstack11l1l111l1_opy_(self, bstack11l1l1ll1l_opy_, result):
        bstack11l1l111ll_opy_ = bstack1111ll111_opy_()
        step = next(filter(lambda st: st[bstack111ll1l_opy_ (u"ࠨ࡫ࡧࠫቨ")] == bstack11l1l1ll1l_opy_, self.meta[bstack111ll1l_opy_ (u"ࠩࡶࡸࡪࡶࡳࠨቩ")]), None)
        step.update({
            bstack111ll1l_opy_ (u"ࠪࡪ࡮ࡴࡩࡴࡪࡨࡨࡤࡧࡴࠨቪ"): bstack11l1l111ll_opy_,
            bstack111ll1l_opy_ (u"ࠫࡩࡻࡲࡢࡶ࡬ࡳࡳ࠭ቫ"): bstack1l11lll1l1_opy_(step[bstack111ll1l_opy_ (u"ࠬࡹࡴࡢࡴࡷࡩࡩࡥࡡࡵࠩቬ")], bstack11l1l111ll_opy_),
            bstack111ll1l_opy_ (u"࠭ࡲࡦࡵࡸࡰࡹ࠭ቭ"): result.result,
            bstack111ll1l_opy_ (u"ࠧࡧࡣ࡬ࡰࡺࡸࡥࠨቮ"): str(result.exception) if result.exception else None
        })
    def bstack11l1l1llll_opy_(self):
        return {
            bstack111ll1l_opy_ (u"ࠨࡷࡸ࡭ࡩ࠭ቯ"): self.bstack11l1l1111l_opy_(),
            **self.bstack11l1ll111l_opy_(),
            **self.bstack11l1l1l1ll_opy_(),
            **self.bstack11l1ll1111_opy_()
        }
    def bstack11l1ll1ll1_opy_(self):
        data = {
            bstack111ll1l_opy_ (u"ࠩࡩ࡭ࡳ࡯ࡳࡩࡧࡧࡣࡦࡺࠧተ"): self.bstack11l1l111ll_opy_,
            bstack111ll1l_opy_ (u"ࠪࡨࡺࡸࡡࡵ࡫ࡲࡲࡤ࡯࡮ࡠ࡯ࡶࠫቱ"): self.duration,
            bstack111ll1l_opy_ (u"ࠫࡷ࡫ࡳࡶ࡮ࡷࠫቲ"): self.result.result
        }
        if data[bstack111ll1l_opy_ (u"ࠬࡸࡥࡴࡷ࡯ࡸࠬታ")] == bstack111ll1l_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭ቴ"):
            data[bstack111ll1l_opy_ (u"ࠧࡧࡣ࡬ࡰࡺࡸࡥࡠࡶࡼࡴࡪ࠭ት")] = self.result.bstack1l11ll1l1l_opy_()
            data[bstack111ll1l_opy_ (u"ࠨࡨࡤ࡭ࡱࡻࡲࡦࠩቶ")] = [{bstack111ll1l_opy_ (u"ࠩࡥࡥࡨࡱࡴࡳࡣࡦࡩࠬቷ"): self.result.bstack1l11ll111l_opy_()}]
        return data
    def bstack11l1ll11ll_opy_(self):
        return {
            bstack111ll1l_opy_ (u"ࠪࡹࡺ࡯ࡤࠨቸ"): self.bstack11l1l1111l_opy_(),
            **self.bstack11l1ll111l_opy_(),
            **self.bstack11l1l1l1ll_opy_(),
            **self.bstack11l1ll1ll1_opy_(),
            **self.bstack11l1ll1111_opy_()
        }
    def bstack11l1l1l1l1_opy_(self, event, result=None):
        if result:
            self.result = result
        if event == bstack111ll1l_opy_ (u"࡙ࠫ࡫ࡳࡵࡔࡸࡲࡘࡺࡡࡳࡶࡨࡨࠬቹ"):
            return self.bstack11l1l1llll_opy_()
        elif event == bstack111ll1l_opy_ (u"࡚ࠬࡥࡴࡶࡕࡹࡳࡌࡩ࡯࡫ࡶ࡬ࡪࡪࠧቺ"):
            return self.bstack11l1ll11ll_opy_()
    def bstack11l1l11l1l_opy_(self):
        pass
    def stop(self, time=None, duration=None, result=None):
        self.bstack11l1l111ll_opy_ = time if time else bstack1111ll111_opy_()
        self.duration = duration if duration else bstack1l11lll1l1_opy_(self.bstack11l1l11lll_opy_, self.bstack11l1l111ll_opy_)
        if result:
            self.result = result
class bstack11l1l1l111_opy_(bstack11l1l11ll1_opy_):
    def __init__(self, *args, hooks=[], **kwargs):
        self.hooks = hooks
        super().__init__(*args, **kwargs, bstack111l11l1_opy_=bstack111ll1l_opy_ (u"࠭ࡴࡦࡵࡷࠫቻ"))
    @classmethod
    def bstack11l1l1l11l_opy_(cls, scenario, feature, test, **kwargs):
        steps = []
        for step in scenario.steps:
            steps.append({
                bstack111ll1l_opy_ (u"ࠧࡪࡦࠪቼ"): id(step),
                bstack111ll1l_opy_ (u"ࠨࡶࡨࡼࡹ࠭ች"): step.name,
                bstack111ll1l_opy_ (u"ࠩ࡮ࡩࡾࡽ࡯ࡳࡦࠪቾ"): step.keyword,
            })
        return bstack11l1l1l111_opy_(
            **kwargs,
            meta={
                bstack111ll1l_opy_ (u"ࠪࡪࡪࡧࡴࡶࡴࡨࠫቿ"): {
                    bstack111ll1l_opy_ (u"ࠫࡳࡧ࡭ࡦࠩኀ"): feature.name,
                    bstack111ll1l_opy_ (u"ࠬࡶࡡࡵࡪࠪኁ"): feature.filename,
                    bstack111ll1l_opy_ (u"࠭ࡤࡦࡵࡦࡶ࡮ࡶࡴࡪࡱࡱࠫኂ"): feature.description
                },
                bstack111ll1l_opy_ (u"ࠧࡴࡥࡨࡲࡦࡸࡩࡰࠩኃ"): {
                    bstack111ll1l_opy_ (u"ࠨࡰࡤࡱࡪ࠭ኄ"): scenario.name
                },
                bstack111ll1l_opy_ (u"ࠩࡶࡸࡪࡶࡳࠨኅ"): steps,
                bstack111ll1l_opy_ (u"ࠪࡩࡽࡧ࡭ࡱ࡮ࡨࡷࠬኆ"): bstack11ll1ll1l1_opy_(test)
            }
        )
    def bstack11l1ll1l1l_opy_(self):
        return {
            bstack111ll1l_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡵࠪኇ"): self.hooks
        }
    def bstack11l1ll11ll_opy_(self):
        return {
            **super().bstack11l1ll11ll_opy_(),
            **self.bstack11l1ll1l1l_opy_()
        }
    def bstack11l1l11l1l_opy_(self):
        return bstack111ll1l_opy_ (u"ࠬࡺࡥࡴࡶࡢࡶࡺࡴࠧኈ")