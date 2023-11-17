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
from _pytest import fixtures
from _pytest.python import _call_with_optional_argument
from pytest import Module, Class
from bstack_utils.helper import Result
def _1l1111l1l1_opy_(method, this, arg):
    arg_count = method.__code__.co_argcount
    if arg_count > 1:
        method(this, arg)
    else:
        method(this)
class bstack1l111l11ll_opy_:
    def __init__(self, handler):
        self._1l111l1l1l_opy_ = {}
        self._1l111l1111_opy_ = {}
        self.handler = handler
        self.patch()
        pass
    def patch(self):
        self._1l111l1l1l_opy_[bstack1ll_opy_ (u"ࠪࡪࡺࡴࡣࡵ࡫ࡲࡲࡤ࡬ࡩࡹࡶࡸࡶࡪ࠭ᄽ")] = Module._inject_setup_function_fixture
        self._1l111l1l1l_opy_[bstack1ll_opy_ (u"ࠫࡲࡵࡤࡶ࡮ࡨࡣ࡫࡯ࡸࡵࡷࡵࡩࠬᄾ")] = Module._inject_setup_module_fixture
        self._1l111l1l1l_opy_[bstack1ll_opy_ (u"ࠬࡩ࡬ࡢࡵࡶࡣ࡫࡯ࡸࡵࡷࡵࡩࠬᄿ")] = Class._inject_setup_class_fixture
        self._1l111l1l1l_opy_[bstack1ll_opy_ (u"࠭࡭ࡦࡶ࡫ࡳࡩࡥࡦࡪࡺࡷࡹࡷ࡫ࠧᅀ")] = Class._inject_setup_method_fixture
        Module._inject_setup_function_fixture = self.bstack1l1111lll1_opy_(bstack1ll_opy_ (u"ࠧࡧࡷࡱࡧࡹ࡯࡯࡯ࡡࡩ࡭ࡽࡺࡵࡳࡧࠪᅁ"))
        Module._inject_setup_module_fixture = self.bstack1l1111lll1_opy_(bstack1ll_opy_ (u"ࠨ࡯ࡲࡨࡺࡲࡥࡠࡨ࡬ࡼࡹࡻࡲࡦࠩᅂ"))
        Class._inject_setup_class_fixture = self.bstack1l1111lll1_opy_(bstack1ll_opy_ (u"ࠩࡦࡰࡦࡹࡳࡠࡨ࡬ࡼࡹࡻࡲࡦࠩᅃ"))
        Class._inject_setup_method_fixture = self.bstack1l1111lll1_opy_(bstack1ll_opy_ (u"ࠪࡱࡪࡺࡨࡰࡦࡢࡪ࡮ࡾࡴࡶࡴࡨࠫᅄ"))
    def bstack1l1111ll11_opy_(self, bstack1l1111l1ll_opy_, hook_type):
        meth = getattr(bstack1l1111l1ll_opy_, hook_type, None)
        if meth is not None and fixtures.getfixturemarker(meth) is None:
            self._1l111l1111_opy_[hook_type] = meth
            setattr(bstack1l1111l1ll_opy_, hook_type, self.bstack1l1111l11l_opy_(hook_type))
    def bstack1l11111lll_opy_(self, instance, bstack1l111l111l_opy_):
        if bstack1l111l111l_opy_ == bstack1ll_opy_ (u"ࠦ࡫ࡻ࡮ࡤࡶ࡬ࡳࡳࡥࡦࡪࡺࡷࡹࡷ࡫ࠢᅅ"):
            self.bstack1l1111ll11_opy_(instance.obj, bstack1ll_opy_ (u"ࠧࡹࡥࡵࡷࡳࡣ࡫ࡻ࡮ࡤࡶ࡬ࡳࡳࠨᅆ"))
            self.bstack1l1111ll11_opy_(instance.obj, bstack1ll_opy_ (u"ࠨࡴࡦࡣࡵࡨࡴࡽ࡮ࡠࡨࡸࡲࡨࡺࡩࡰࡰࠥᅇ"))
        if bstack1l111l111l_opy_ == bstack1ll_opy_ (u"ࠢ࡮ࡱࡧࡹࡱ࡫࡟ࡧ࡫ࡻࡸࡺࡸࡥࠣᅈ"):
            self.bstack1l1111ll11_opy_(instance.obj, bstack1ll_opy_ (u"ࠣࡵࡨࡸࡺࡶ࡟࡮ࡱࡧࡹࡱ࡫ࠢᅉ"))
            self.bstack1l1111ll11_opy_(instance.obj, bstack1ll_opy_ (u"ࠤࡷࡩࡦࡸࡤࡰࡹࡱࡣࡲࡵࡤࡶ࡮ࡨࠦᅊ"))
        if bstack1l111l111l_opy_ == bstack1ll_opy_ (u"ࠥࡧࡱࡧࡳࡴࡡࡩ࡭ࡽࡺࡵࡳࡧࠥᅋ"):
            self.bstack1l1111ll11_opy_(instance.obj, bstack1ll_opy_ (u"ࠦࡸ࡫ࡴࡶࡲࡢࡧࡱࡧࡳࡴࠤᅌ"))
            self.bstack1l1111ll11_opy_(instance.obj, bstack1ll_opy_ (u"ࠧࡺࡥࡢࡴࡧࡳࡼࡴ࡟ࡤ࡮ࡤࡷࡸࠨᅍ"))
        if bstack1l111l111l_opy_ == bstack1ll_opy_ (u"ࠨ࡭ࡦࡶ࡫ࡳࡩࡥࡦࡪࡺࡷࡹࡷ࡫ࠢᅎ"):
            self.bstack1l1111ll11_opy_(instance.obj, bstack1ll_opy_ (u"ࠢࡴࡧࡷࡹࡵࡥ࡭ࡦࡶ࡫ࡳࡩࠨᅏ"))
            self.bstack1l1111ll11_opy_(instance.obj, bstack1ll_opy_ (u"ࠣࡶࡨࡥࡷࡪ࡯ࡸࡰࡢࡱࡪࡺࡨࡰࡦࠥᅐ"))
    @staticmethod
    def bstack1l1111ll1l_opy_(hook_type, func, args):
        if hook_type in [bstack1ll_opy_ (u"ࠩࡶࡩࡹࡻࡰࡠ࡯ࡨࡸ࡭ࡵࡤࠨᅑ"), bstack1ll_opy_ (u"ࠪࡸࡪࡧࡲࡥࡱࡺࡲࡤࡳࡥࡵࡪࡲࡨࠬᅒ")]:
            _1l1111l1l1_opy_(func, args[0], args[1])
            return
        _call_with_optional_argument(func, args[0])
    def bstack1l1111l11l_opy_(self, hook_type):
        def bstack1l111l11l1_opy_(arg=None):
            self.handler(hook_type, bstack1ll_opy_ (u"ࠫࡧ࡫ࡦࡰࡴࡨࠫᅓ"))
            result = None
            exception = None
            try:
                self.bstack1l1111ll1l_opy_(hook_type, self._1l111l1111_opy_[hook_type], (arg,))
                result = Result(result=bstack1ll_opy_ (u"ࠬࡶࡡࡴࡵࡨࡨࠬᅔ"))
            except Exception as e:
                result = Result(result=bstack1ll_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭ᅕ"), exception=e)
                self.handler(hook_type, bstack1ll_opy_ (u"ࠧࡢࡨࡷࡩࡷ࠭ᅖ"), result)
                raise e.with_traceback(e.__traceback__)
            self.handler(hook_type, bstack1ll_opy_ (u"ࠨࡣࡩࡸࡪࡸࠧᅗ"), result)
        def bstack1l111l1l11_opy_(this, arg=None):
            self.handler(hook_type, bstack1ll_opy_ (u"ࠩࡥࡩ࡫ࡵࡲࡦࠩᅘ"))
            result = None
            exception = None
            try:
                self.bstack1l1111ll1l_opy_(hook_type, self._1l111l1111_opy_[hook_type], (this, arg))
                result = Result(result=bstack1ll_opy_ (u"ࠪࡴࡦࡹࡳࡦࡦࠪᅙ"))
            except Exception as e:
                result = Result(result=bstack1ll_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫᅚ"), exception=e)
                self.handler(hook_type, bstack1ll_opy_ (u"ࠬࡧࡦࡵࡧࡵࠫᅛ"), result)
                raise e.with_traceback(e.__traceback__)
            self.handler(hook_type, bstack1ll_opy_ (u"࠭ࡡࡧࡶࡨࡶࠬᅜ"), result)
        if hook_type in [bstack1ll_opy_ (u"ࠧࡴࡧࡷࡹࡵࡥ࡭ࡦࡶ࡫ࡳࡩ࠭ᅝ"), bstack1ll_opy_ (u"ࠨࡶࡨࡥࡷࡪ࡯ࡸࡰࡢࡱࡪࡺࡨࡰࡦࠪᅞ")]:
            return bstack1l111l1l11_opy_
        return bstack1l111l11l1_opy_
    def bstack1l1111lll1_opy_(self, bstack1l111l111l_opy_):
        def bstack1l1111l111_opy_(this, *args, **kwargs):
            self.bstack1l11111lll_opy_(this, bstack1l111l111l_opy_)
            self._1l111l1l1l_opy_[bstack1l111l111l_opy_](this, *args, **kwargs)
        return bstack1l1111l111_opy_