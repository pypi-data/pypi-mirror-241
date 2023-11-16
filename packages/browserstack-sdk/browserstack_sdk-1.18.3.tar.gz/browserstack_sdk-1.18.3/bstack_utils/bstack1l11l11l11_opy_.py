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
from _pytest import fixtures
from _pytest.python import _call_with_optional_argument
from pytest import Module, Class
from bstack_utils.helper import Result
def _1l11l11lll_opy_(method, this, arg):
    arg_count = method.__code__.co_argcount
    if arg_count > 1:
        method(this, arg)
    else:
        method(this)
class bstack1l11l1ll1l_opy_:
    def __init__(self, handler):
        self._1l11l1l1l1_opy_ = {}
        self._1l11l11l1l_opy_ = {}
        self.handler = handler
        self.patch()
        pass
    def patch(self):
        self._1l11l1l1l1_opy_[bstack111ll1l_opy_ (u"ࠫ࡫ࡻ࡮ࡤࡶ࡬ࡳࡳࡥࡦࡪࡺࡷࡹࡷ࡫ࠧᄍ")] = Module._inject_setup_function_fixture
        self._1l11l1l1l1_opy_[bstack111ll1l_opy_ (u"ࠬࡳ࡯ࡥࡷ࡯ࡩࡤ࡬ࡩࡹࡶࡸࡶࡪ࠭ᄎ")] = Module._inject_setup_module_fixture
        self._1l11l1l1l1_opy_[bstack111ll1l_opy_ (u"࠭ࡣ࡭ࡣࡶࡷࡤ࡬ࡩࡹࡶࡸࡶࡪ࠭ᄏ")] = Class._inject_setup_class_fixture
        self._1l11l1l1l1_opy_[bstack111ll1l_opy_ (u"ࠧ࡮ࡧࡷ࡬ࡴࡪ࡟ࡧ࡫ࡻࡸࡺࡸࡥࠨᄐ")] = Class._inject_setup_method_fixture
        Module._inject_setup_function_fixture = self.bstack1l11l1111l_opy_(bstack111ll1l_opy_ (u"ࠨࡨࡸࡲࡨࡺࡩࡰࡰࡢࡪ࡮ࡾࡴࡶࡴࡨࠫᄑ"))
        Module._inject_setup_module_fixture = self.bstack1l11l1111l_opy_(bstack111ll1l_opy_ (u"ࠩࡰࡳࡩࡻ࡬ࡦࡡࡩ࡭ࡽࡺࡵࡳࡧࠪᄒ"))
        Class._inject_setup_class_fixture = self.bstack1l11l1111l_opy_(bstack111ll1l_opy_ (u"ࠪࡧࡱࡧࡳࡴࡡࡩ࡭ࡽࡺࡵࡳࡧࠪᄓ"))
        Class._inject_setup_method_fixture = self.bstack1l11l1111l_opy_(bstack111ll1l_opy_ (u"ࠫࡲ࡫ࡴࡩࡱࡧࡣ࡫࡯ࡸࡵࡷࡵࡩࠬᄔ"))
    def bstack1l11l11ll1_opy_(self, bstack1l11l1l1ll_opy_, hook_type):
        meth = getattr(bstack1l11l1l1ll_opy_, hook_type, None)
        if meth is not None and fixtures.getfixturemarker(meth) is None:
            self._1l11l11l1l_opy_[hook_type] = meth
            setattr(bstack1l11l1l1ll_opy_, hook_type, self.bstack1l11l1lll1_opy_(hook_type))
    def bstack1l11l1l11l_opy_(self, instance, bstack1l11l1ll11_opy_):
        if bstack1l11l1ll11_opy_ == bstack111ll1l_opy_ (u"ࠧ࡬ࡵ࡯ࡥࡷ࡭ࡴࡴ࡟ࡧ࡫ࡻࡸࡺࡸࡥࠣᄕ"):
            self.bstack1l11l11ll1_opy_(instance.obj, bstack111ll1l_opy_ (u"ࠨࡳࡦࡶࡸࡴࡤ࡬ࡵ࡯ࡥࡷ࡭ࡴࡴࠢᄖ"))
            self.bstack1l11l11ll1_opy_(instance.obj, bstack111ll1l_opy_ (u"ࠢࡵࡧࡤࡶࡩࡵࡷ࡯ࡡࡩࡹࡳࡩࡴࡪࡱࡱࠦᄗ"))
        if bstack1l11l1ll11_opy_ == bstack111ll1l_opy_ (u"ࠣ࡯ࡲࡨࡺࡲࡥࡠࡨ࡬ࡼࡹࡻࡲࡦࠤᄘ"):
            self.bstack1l11l11ll1_opy_(instance.obj, bstack111ll1l_opy_ (u"ࠤࡶࡩࡹࡻࡰࡠ࡯ࡲࡨࡺࡲࡥࠣᄙ"))
            self.bstack1l11l11ll1_opy_(instance.obj, bstack111ll1l_opy_ (u"ࠥࡸࡪࡧࡲࡥࡱࡺࡲࡤࡳ࡯ࡥࡷ࡯ࡩࠧᄚ"))
        if bstack1l11l1ll11_opy_ == bstack111ll1l_opy_ (u"ࠦࡨࡲࡡࡴࡵࡢࡪ࡮ࡾࡴࡶࡴࡨࠦᄛ"):
            self.bstack1l11l11ll1_opy_(instance.obj, bstack111ll1l_opy_ (u"ࠧࡹࡥࡵࡷࡳࡣࡨࡲࡡࡴࡵࠥᄜ"))
            self.bstack1l11l11ll1_opy_(instance.obj, bstack111ll1l_opy_ (u"ࠨࡴࡦࡣࡵࡨࡴࡽ࡮ࡠࡥ࡯ࡥࡸࡹࠢᄝ"))
        if bstack1l11l1ll11_opy_ == bstack111ll1l_opy_ (u"ࠢ࡮ࡧࡷ࡬ࡴࡪ࡟ࡧ࡫ࡻࡸࡺࡸࡥࠣᄞ"):
            self.bstack1l11l11ll1_opy_(instance.obj, bstack111ll1l_opy_ (u"ࠣࡵࡨࡸࡺࡶ࡟࡮ࡧࡷ࡬ࡴࡪࠢᄟ"))
            self.bstack1l11l11ll1_opy_(instance.obj, bstack111ll1l_opy_ (u"ࠤࡷࡩࡦࡸࡤࡰࡹࡱࡣࡲ࡫ࡴࡩࡱࡧࠦᄠ"))
    @staticmethod
    def bstack1l11l111l1_opy_(hook_type, func, args):
        if hook_type in [bstack111ll1l_opy_ (u"ࠪࡷࡪࡺࡵࡱࡡࡰࡩࡹ࡮࡯ࡥࠩᄡ"), bstack111ll1l_opy_ (u"ࠫࡹ࡫ࡡࡳࡦࡲࡻࡳࡥ࡭ࡦࡶ࡫ࡳࡩ࠭ᄢ")]:
            _1l11l11lll_opy_(func, args[0], args[1])
            return
        _call_with_optional_argument(func, args[0])
    def bstack1l11l1lll1_opy_(self, hook_type):
        def bstack1l11l111ll_opy_(arg=None):
            self.handler(hook_type, bstack111ll1l_opy_ (u"ࠬࡨࡥࡧࡱࡵࡩࠬᄣ"))
            result = None
            exception = None
            try:
                self.bstack1l11l111l1_opy_(hook_type, self._1l11l11l1l_opy_[hook_type], (arg,))
                result = Result(result=bstack111ll1l_opy_ (u"࠭ࡰࡢࡵࡶࡩࡩ࠭ᄤ"))
            except Exception as e:
                result = Result(result=bstack111ll1l_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧᄥ"), exception=e)
                self.handler(hook_type, bstack111ll1l_opy_ (u"ࠨࡣࡩࡸࡪࡸࠧᄦ"), result)
                raise e.with_traceback(e.__traceback__)
            self.handler(hook_type, bstack111ll1l_opy_ (u"ࠩࡤࡪࡹ࡫ࡲࠨᄧ"), result)
        def bstack1l11l1l111_opy_(this, arg=None):
            self.handler(hook_type, bstack111ll1l_opy_ (u"ࠪࡦࡪ࡬࡯ࡳࡧࠪᄨ"))
            result = None
            exception = None
            try:
                self.bstack1l11l111l1_opy_(hook_type, self._1l11l11l1l_opy_[hook_type], (this, arg))
                result = Result(result=bstack111ll1l_opy_ (u"ࠫࡵࡧࡳࡴࡧࡧࠫᄩ"))
            except Exception as e:
                result = Result(result=bstack111ll1l_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬᄪ"), exception=e)
                self.handler(hook_type, bstack111ll1l_opy_ (u"࠭ࡡࡧࡶࡨࡶࠬᄫ"), result)
                raise e.with_traceback(e.__traceback__)
            self.handler(hook_type, bstack111ll1l_opy_ (u"ࠧࡢࡨࡷࡩࡷ࠭ᄬ"), result)
        if hook_type in [bstack111ll1l_opy_ (u"ࠨࡵࡨࡸࡺࡶ࡟࡮ࡧࡷ࡬ࡴࡪࠧᄭ"), bstack111ll1l_opy_ (u"ࠩࡷࡩࡦࡸࡤࡰࡹࡱࡣࡲ࡫ࡴࡩࡱࡧࠫᄮ")]:
            return bstack1l11l1l111_opy_
        return bstack1l11l111ll_opy_
    def bstack1l11l1111l_opy_(self, bstack1l11l1ll11_opy_):
        def bstack1l11l11111_opy_(this, *args, **kwargs):
            self.bstack1l11l1l11l_opy_(this, bstack1l11l1ll11_opy_)
            self._1l11l1l1l1_opy_[bstack1l11l1ll11_opy_](this, *args, **kwargs)
        return bstack1l11l11111_opy_