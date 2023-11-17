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
import atexit
import datetime
import inspect
import logging
import os
import sys
import threading
from uuid import uuid4
import tempfile
import pytest
from packaging import version
from browserstack_sdk.__init__ import (bstack111l11lll_opy_, bstack1lll11lll1_opy_, update, bstack1111l1l11_opy_,
                                       bstack111ll111_opy_, bstack11111llll_opy_, bstack1lll1l11l1_opy_, bstack1ll11lll11_opy_,
                                       bstack11ll11111_opy_, bstack11l111l11_opy_, bstack11111l1l_opy_, bstack11ll1ll1l_opy_,
                                       bstack1ll11111l_opy_, getAccessibilityResults, getAccessibilityResultsSummary)
from browserstack_sdk._version import __version__
from bstack_utils.capture import bstack1l1l1l11ll_opy_
from bstack_utils.constants import bstack1l1llll1_opy_, bstack11l1ll1ll_opy_, bstack11l1111l_opy_, bstack1111ll1ll_opy_, \
    bstack111ll11l_opy_
from bstack_utils.helper import bstack1llll11l_opy_, bstack111ll111l_opy_, bstack1l11l1ll11_opy_, bstack1lllll1ll1_opy_, bstack1l11lllll1_opy_, \
    bstack1l111ll111_opy_, bstack1l1lllllll_opy_, bstack1l1l1ll11_opy_, bstack1l11llll1l_opy_, bstack1ll1ll11l1_opy_, Notset, \
    bstack111lll111_opy_, bstack1l11l1l1ll_opy_, bstack1l1l111111_opy_, Result, bstack1l11lll1l1_opy_, bstack1l11ll111l_opy_, bstack1l1lll1111_opy_, bstack1lll11l1_opy_, bstack1ll11ll11_opy_
from bstack_utils.bstack1l1111llll_opy_ import bstack1l111l11ll_opy_
from bstack_utils.messages import bstack1111ll111_opy_, bstack1l11l111l_opy_, bstack1lll1l1l_opy_, bstack1ll1l111_opy_, bstack1ll1lll1_opy_, \
    bstack111l1llll_opy_, bstack11ll1111l_opy_, bstack11ll1l11_opy_, bstack11ll1l1l1_opy_, bstack1llll11ll1_opy_, \
    bstack1l1l1ll1l_opy_, bstack1ll1111lll_opy_
from bstack_utils.proxy import bstack1l111ll11_opy_, bstack11llllll_opy_
from bstack_utils.bstack1lll1l11_opy_ import bstack11ll111l1l_opy_, bstack11ll111l11_opy_, bstack11l1lll1ll_opy_, bstack11ll11111l_opy_, \
    bstack11ll1111l1_opy_, bstack11ll111111_opy_, bstack11l1lllll1_opy_, bstack1ll11l11_opy_, bstack11l1llll1l_opy_
from bstack_utils.bstack11l1l11l1l_opy_ import bstack11l1l1l1l1_opy_
from bstack_utils.bstack11l1ll1lll_opy_ import bstack11ll1111_opy_, bstack1llllll1l1_opy_, bstack1ll1llll11_opy_
from bstack_utils.bstack11l11ll1l1_opy_ import bstack11l11ll111_opy_
from bstack_utils.bstack1ll11l1l11_opy_ import bstack11l1l1l1_opy_
import bstack_utils.bstack1l1l1l1l1_opy_ as bstack1lll1ll1_opy_
bstack11ll11ll1_opy_ = None
bstack111ll1ll_opy_ = None
bstack1lll1l1ll1_opy_ = None
bstack1lll111l1_opy_ = None
bstack11lll11ll_opy_ = None
bstack1ll111l11l_opy_ = None
bstack1ll1111l1_opy_ = None
bstack1l1l11ll1_opy_ = None
bstack1l1111lll_opy_ = None
bstack1ll11ll1ll_opy_ = None
bstack1llllll111_opy_ = None
bstack11l111lll_opy_ = None
bstack11111111l_opy_ = None
bstack1lll11l11l_opy_ = bstack1ll_opy_ (u"ࠪࠫᎂ")
CONFIG = {}
bstack1l11l11ll_opy_ = False
bstack1l111l111_opy_ = bstack1ll_opy_ (u"ࠫࠬᎃ")
bstack1l1111ll_opy_ = bstack1ll_opy_ (u"ࠬ࠭ᎄ")
bstack111111ll_opy_ = False
bstack11l1l1l1l_opy_ = []
bstack1l1l11l11_opy_ = bstack11l1ll1ll_opy_
bstack111ll111l1_opy_ = bstack1ll_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭ᎅ")
bstack111l1lllll_opy_ = False
logger = logging.getLogger(__name__)
logging.basicConfig(level=bstack1l1l11l11_opy_,
                    format=bstack1ll_opy_ (u"ࠧ࡝ࡰࠨࠬࡦࡹࡣࡵ࡫ࡰࡩ࠮ࡹࠠ࡜ࠧࠫࡲࡦࡳࡥࠪࡵࡠ࡟ࠪ࠮࡬ࡦࡸࡨࡰࡳࡧ࡭ࡦࠫࡶࡡࠥ࠳ࠠࠦࠪࡰࡩࡸࡹࡡࡨࡧࠬࡷࠬᎆ"),
                    datefmt=bstack1ll_opy_ (u"ࠨࠧࡋ࠾ࠪࡓ࠺ࠦࡕࠪᎇ"),
                    stream=sys.stdout)
store = {
    bstack1ll_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢ࡬ࡴࡵ࡫ࡠࡷࡸ࡭ࡩ࠭ᎈ"): []
}
def bstack1llll11l11_opy_():
    global CONFIG
    global bstack1l1l11l11_opy_
    if bstack1ll_opy_ (u"ࠪࡰࡴ࡭ࡌࡦࡸࡨࡰࠬᎉ") in CONFIG:
        bstack1l1l11l11_opy_ = bstack1l1llll1_opy_[CONFIG[bstack1ll_opy_ (u"ࠫࡱࡵࡧࡍࡧࡹࡩࡱ࠭ᎊ")]]
        logging.getLogger().setLevel(bstack1l1l11l11_opy_)
try:
    from playwright.sync_api import (
        BrowserContext,
        Page
    )
except:
    pass
import json
_111l111l11_opy_ = {}
current_test_uuid = None
def bstack1ll1l11ll1_opy_(page, bstack1llll1lll_opy_):
    try:
        page.evaluate(bstack1ll_opy_ (u"ࠧࡥࠠ࠾ࡀࠣࡿࢂࠨᎋ"),
                      bstack1ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࠥࡥࡨࡺࡩࡰࡰࠥ࠾ࠥࠨࡳࡦࡶࡖࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠢ࠭ࠢࠥࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸࠨ࠺ࠡࡽࠥࡲࡦࡳࡥࠣ࠼ࠪᎌ") + json.dumps(
                          bstack1llll1lll_opy_) + bstack1ll_opy_ (u"ࠢࡾࡿࠥᎍ"))
    except Exception as e:
        print(bstack1ll_opy_ (u"ࠣࡧࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡱ࡮ࡤࡽࡼࡸࡩࡨࡪࡷࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠥࡴࡡ࡮ࡧࠣࡿࢂࠨᎎ"), e)
def bstack1lll11l111_opy_(page, message, level):
    try:
        page.evaluate(bstack1ll_opy_ (u"ࠤࡢࠤࡂࡄࠠࡼࡿࠥᎏ"), bstack1ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁࠢࡢࡥࡷ࡭ࡴࡴࠢ࠻ࠢࠥࡥࡳࡴ࡯ࡵࡣࡷࡩࠧ࠲ࠠࠣࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠦ࠿ࠦࡻࠣࡦࡤࡸࡦࠨ࠺ࠨ᎐") + json.dumps(
            message) + bstack1ll_opy_ (u"ࠫ࠱ࠨ࡬ࡦࡸࡨࡰࠧࡀࠧ᎑") + json.dumps(level) + bstack1ll_opy_ (u"ࠬࢃࡽࠨ᎒"))
    except Exception as e:
        print(bstack1ll_opy_ (u"ࠨࡥࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠢࡤࡲࡳࡵࡴࡢࡶ࡬ࡳࡳࠦࡻࡾࠤ᎓"), e)
def bstack11lll111_opy_(page, status, message=bstack1ll_opy_ (u"ࠢࠣ᎔")):
    try:
        if (status == bstack1ll_opy_ (u"ࠣࡨࡤ࡭ࡱ࡫ࡤࠣ᎕")):
            page.evaluate(bstack1ll_opy_ (u"ࠤࡢࠤࡂࡄࠠࡼࡿࠥ᎖"),
                          bstack1ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁࠢࡢࡥࡷ࡭ࡴࡴࠢ࠻ࠢࠥࡷࡪࡺࡓࡦࡵࡶ࡭ࡴࡴࡓࡵࡣࡷࡹࡸࠨࠬࠡࠤࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠧࡀࠠࡼࠤࡵࡩࡦࡹ࡯࡯ࠤ࠽ࠫ᎗") + json.dumps(
                              bstack1ll_opy_ (u"ࠦࡘࡩࡥ࡯ࡣࡵ࡭ࡴࠦࡦࡢ࡫࡯ࡩࡩࠦࡷࡪࡶ࡫࠾ࠥࠨ᎘") + str(message)) + bstack1ll_opy_ (u"ࠬ࠲ࠢࡴࡶࡤࡸࡺࡹࠢ࠻ࠩ᎙") + json.dumps(status) + bstack1ll_opy_ (u"ࠨࡽࡾࠤ᎚"))
        else:
            page.evaluate(bstack1ll_opy_ (u"ࠢࡠࠢࡀࡂࠥࢁࡽࠣ᎛"),
                          bstack1ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࡿࠧࡧࡣࡵ࡫ࡲࡲࠧࡀࠠࠣࡵࡨࡸࡘ࡫ࡳࡴ࡫ࡲࡲࡘࡺࡡࡵࡷࡶࠦ࠱ࠦࠢࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠥ࠾ࠥࢁࠢࡴࡶࡤࡸࡺࡹࠢ࠻ࠩ᎜") + json.dumps(
                              status) + bstack1ll_opy_ (u"ࠤࢀࢁࠧ᎝"))
    except Exception as e:
        print(bstack1ll_opy_ (u"ࠥࡩࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹࠦࡳࡦࡶࠣࡷࡪࡹࡳࡪࡱࡱࠤࡸࡺࡡࡵࡷࡶࠤࢀࢃࠢ᎞"), e)
def pytest_configure(config):
    config.args = bstack11l1l1l1_opy_.bstack111lll1l11_opy_(config.args)
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    bstack111l1l11l1_opy_ = item.config.getoption(bstack1ll_opy_ (u"ࠫࡸࡱࡩࡱࡕࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪ࠭᎟"))
    plugins = item.config.getoption(bstack1ll_opy_ (u"ࠧࡶ࡬ࡶࡩ࡬ࡲࡸࠨᎠ"))
    report = outcome.get_result()
    bstack111l1111l1_opy_(item, call, report)
    if bstack1ll_opy_ (u"ࠨࡰࡺࡶࡨࡷࡹࡥࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡵࡲࡵࡨ࡫ࡱࠦᎡ") not in plugins or bstack1ll1ll11l1_opy_():
        return
    summary = []
    driver = getattr(item, bstack1ll_opy_ (u"ࠢࡠࡦࡵ࡭ࡻ࡫ࡲࠣᎢ"), None)
    page = getattr(item, bstack1ll_opy_ (u"ࠣࡡࡳࡥ࡬࡫ࠢᎣ"), None)
    try:
        if (driver == None):
            driver = threading.current_thread().bstackSessionDriver
    except:
        pass
    item._driver = driver
    if (driver is not None):
        bstack111ll11lll_opy_(item, report, summary, bstack111l1l11l1_opy_)
    if (page is not None):
        bstack111l1l1l11_opy_(item, report, summary, bstack111l1l11l1_opy_)
def bstack111ll11lll_opy_(item, report, summary, bstack111l1l11l1_opy_):
    if report.when in [bstack1ll_opy_ (u"ࠤࡶࡩࡹࡻࡰࠣᎤ"), bstack1ll_opy_ (u"ࠥࡸࡪࡧࡲࡥࡱࡺࡲࠧᎥ")]:
        return
    if not bstack1l11l1ll11_opy_():
        return
    try:
        if (str(bstack111l1l11l1_opy_).lower() != bstack1ll_opy_ (u"ࠫࡹࡸࡵࡦࠩᎦ")):
            item._driver.execute_script(
                bstack1ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࡼࠤࡤࡧࡹ࡯࡯࡯ࠤ࠽ࠤࠧࡹࡥࡵࡕࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪࠨࠬࠡࠤࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠧࡀࠠࡼࠤࡱࡥࡲ࡫ࠢ࠻ࠢࠪᎧ") + json.dumps(
                    report.nodeid) + bstack1ll_opy_ (u"࠭ࡽࡾࠩᎨ"))
        os.environ[bstack1ll_opy_ (u"ࠧࡑ࡛ࡗࡉࡘ࡚࡟ࡕࡇࡖࡘࡤࡔࡁࡎࡇࠪᎩ")] = report.nodeid
    except Exception as e:
        summary.append(
            bstack1ll_opy_ (u"࡙ࠣࡄࡖࡓࡏࡎࡈ࠼ࠣࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦ࡭ࡢࡴ࡮ࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠥࡴࡡ࡮ࡧ࠽ࠤࢀ࠶ࡽࠣᎪ").format(e)
        )
    passed = report.passed or report.skipped or (report.failed and hasattr(report, bstack1ll_opy_ (u"ࠤࡺࡥࡸࡾࡦࡢ࡫࡯ࠦᎫ")))
    bstack1lll111ll_opy_ = bstack1ll_opy_ (u"ࠥࠦᎬ")
    bstack11l1llll1l_opy_(report)
    if not passed:
        try:
            bstack1lll111ll_opy_ = report.longrepr.reprcrash
        except Exception as e:
            summary.append(
                bstack1ll_opy_ (u"ࠦ࡜ࡇࡒࡏࡋࡑࡋ࠿ࠦࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡧࡩࡹ࡫ࡲ࡮࡫ࡱࡩࠥ࡬ࡡࡪ࡮ࡸࡶࡪࠦࡲࡦࡣࡶࡳࡳࡀࠠࡼ࠲ࢀࠦᎭ").format(e)
            )
        try:
            if (threading.current_thread().bstackTestErrorMessages == None):
                threading.current_thread().bstackTestErrorMessages = []
        except Exception as e:
            threading.current_thread().bstackTestErrorMessages = []
        threading.current_thread().bstackTestErrorMessages.append(str(bstack1lll111ll_opy_))
    if not report.skipped:
        passed = report.passed or (report.failed and hasattr(report, bstack1ll_opy_ (u"ࠧࡽࡡࡴࡺࡩࡥ࡮ࡲࠢᎮ")))
        bstack1lll111ll_opy_ = bstack1ll_opy_ (u"ࠨࠢᎯ")
        if not passed:
            try:
                bstack1lll111ll_opy_ = report.longrepr.reprcrash
            except Exception as e:
                summary.append(
                    bstack1ll_opy_ (u"ࠢࡘࡃࡕࡒࡎࡔࡇ࠻ࠢࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡪࡥࡵࡧࡵࡱ࡮ࡴࡥࠡࡨࡤ࡭ࡱࡻࡲࡦࠢࡵࡩࡦࡹ࡯࡯࠼ࠣࡿ࠵ࢃࠢᎰ").format(e)
                )
            try:
                if (threading.current_thread().bstackTestErrorMessages == None):
                    threading.current_thread().bstackTestErrorMessages = []
            except Exception as e:
                threading.current_thread().bstackTestErrorMessages = []
            threading.current_thread().bstackTestErrorMessages.append(str(bstack1lll111ll_opy_))
        try:
            if passed:
                item._driver.execute_script(
                    bstack1ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࡿࡡࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠢࡢࡥࡷ࡭ࡴࡴࠢ࠻ࠢࠥࡥࡳࡴ࡯ࡵࡣࡷࡩࠧ࠲ࠠ࡝ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠥࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸࠨ࠺ࠡࡽ࡟ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠤ࡯ࡩࡻ࡫࡬ࠣ࠼ࠣࠦ࡮ࡴࡦࡰࠤ࠯ࠤࡡࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠦࡩࡧࡴࡢࠤ࠽ࠤࠬᎱ")
                    + json.dumps(bstack1ll_opy_ (u"ࠤࡳࡥࡸࡹࡥࡥࠣࠥᎲ"))
                    + bstack1ll_opy_ (u"ࠥࡠࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࢃ࡜ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࢂࠨᎳ")
                )
            else:
                item._driver.execute_script(
                    bstack1ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻ࡝ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠥࡥࡨࡺࡩࡰࡰࠥ࠾ࠥࠨࡡ࡯ࡰࡲࡸࡦࡺࡥࠣ࠮ࠣࡠࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠨࡡࡳࡩࡸࡱࡪࡴࡴࡴࠤ࠽ࠤࢀࡢࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠧࡲࡥࡷࡧ࡯ࠦ࠿ࠦࠢࡦࡴࡵࡳࡷࠨࠬࠡ࡞ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠣࡦࡤࡸࡦࠨ࠺ࠡࠩᎴ")
                    + json.dumps(str(bstack1lll111ll_opy_))
                    + bstack1ll_opy_ (u"ࠧࡢࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡾ࡞ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡽࠣᎵ")
                )
        except Exception as e:
            summary.append(bstack1ll_opy_ (u"ࠨࡗࡂࡔࡑࡍࡓࡍ࠺ࠡࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡦࡴ࡮ࡰࡶࡤࡸࡪࡀࠠࡼ࠲ࢀࠦᎶ").format(e))
def bstack111ll11111_opy_(test_name, error_message):
    try:
        bstack111l11111l_opy_ = []
        bstack1l1l1l1l_opy_ = os.environ.get(bstack1ll_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡐࡍࡃࡗࡊࡔࡘࡍࡠࡋࡑࡈࡊ࡞ࠧᎷ"), bstack1ll_opy_ (u"ࠨ࠲ࠪᎸ"))
        bstack1ll1l1l1ll_opy_ = {bstack1ll_opy_ (u"ࠩࡱࡥࡲ࡫ࠧᎹ"): test_name, bstack1ll_opy_ (u"ࠪࡩࡷࡸ࡯ࡳࠩᎺ"): error_message, bstack1ll_opy_ (u"ࠫ࡮ࡴࡤࡦࡺࠪᎻ"): bstack1l1l1l1l_opy_}
        bstack111l1lll11_opy_ = os.path.join(tempfile.gettempdir(), bstack1ll_opy_ (u"ࠬࡶࡷࡠࡲࡼࡸࡪࡹࡴࡠࡧࡵࡶࡴࡸ࡟࡭࡫ࡶࡸ࠳ࡰࡳࡰࡰࠪᎼ"))
        if os.path.exists(bstack111l1lll11_opy_):
            with open(bstack111l1lll11_opy_) as f:
                bstack111l11111l_opy_ = json.load(f)
        bstack111l11111l_opy_.append(bstack1ll1l1l1ll_opy_)
        with open(bstack111l1lll11_opy_, bstack1ll_opy_ (u"࠭ࡷࠨᎽ")) as f:
            json.dump(bstack111l11111l_opy_, f)
    except Exception as e:
        logger.debug(bstack1ll_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡳࡩࡷࡹࡩࡴࡶ࡬ࡲ࡬ࠦࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࠣࡴࡾࡺࡥࡴࡶࠣࡩࡷࡸ࡯ࡳࡵ࠽ࠤࠬᎾ") + str(e))
def bstack111l1l1l11_opy_(item, report, summary, bstack111l1l11l1_opy_):
    if report.when in [bstack1ll_opy_ (u"ࠣࡵࡨࡸࡺࡶࠢᎿ"), bstack1ll_opy_ (u"ࠤࡷࡩࡦࡸࡤࡰࡹࡱࠦᏀ")]:
        return
    if (str(bstack111l1l11l1_opy_).lower() != bstack1ll_opy_ (u"ࠪࡸࡷࡻࡥࠨᏁ")):
        bstack1ll1l11ll1_opy_(item._page, report.nodeid)
    passed = report.passed or report.skipped or (report.failed and hasattr(report, bstack1ll_opy_ (u"ࠦࡼࡧࡳࡹࡨࡤ࡭ࡱࠨᏂ")))
    bstack1lll111ll_opy_ = bstack1ll_opy_ (u"ࠧࠨᏃ")
    bstack11l1llll1l_opy_(report)
    if not report.skipped:
        if not passed:
            try:
                bstack1lll111ll_opy_ = report.longrepr.reprcrash
            except Exception as e:
                summary.append(
                    bstack1ll_opy_ (u"ࠨࡗࡂࡔࡑࡍࡓࡍ࠺ࠡࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡩ࡫ࡴࡦࡴࡰ࡭ࡳ࡫ࠠࡧࡣ࡬ࡰࡺࡸࡥࠡࡴࡨࡥࡸࡵ࡮࠻ࠢࡾ࠴ࢂࠨᏄ").format(e)
                )
        try:
            if passed:
                bstack11lll111_opy_(item._page, bstack1ll_opy_ (u"ࠢࡱࡣࡶࡷࡪࡪࠢᏅ"))
            else:
                error_message = bstack1ll_opy_ (u"ࠨࠩᏆ")
                if bstack1lll111ll_opy_:
                    bstack1lll11l111_opy_(item._page, str(bstack1lll111ll_opy_), bstack1ll_opy_ (u"ࠤࡨࡶࡷࡵࡲࠣᏇ"))
                    bstack11lll111_opy_(item._page, bstack1ll_opy_ (u"ࠥࡪࡦ࡯࡬ࡦࡦࠥᏈ"), str(bstack1lll111ll_opy_))
                    error_message = str(bstack1lll111ll_opy_)
                else:
                    bstack11lll111_opy_(item._page, bstack1ll_opy_ (u"ࠦ࡫ࡧࡩ࡭ࡧࡧࠦᏉ"))
                bstack111ll11111_opy_(report.nodeid, error_message)
        except Exception as e:
            summary.append(bstack1ll_opy_ (u"ࠧ࡝ࡁࡓࡐࡌࡒࡌࡀࠠࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡹࡵࡪࡡࡵࡧࠣࡷࡪࡹࡳࡪࡱࡱࠤࡸࡺࡡࡵࡷࡶ࠾ࠥࢁ࠰ࡾࠤᏊ").format(e))
try:
    from typing import Generator
    import pytest_playwright.pytest_playwright as p
    @pytest.fixture
    def page(context: BrowserContext, request: pytest.FixtureRequest) -> Generator[Page, None, None]:
        page = context.new_page()
        request.node._page = page
        yield page
except:
    pass
def pytest_addoption(parser):
    parser.addoption(bstack1ll_opy_ (u"ࠨ࠭࠮ࡵ࡮࡭ࡵ࡙ࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠥᏋ"), default=bstack1ll_opy_ (u"ࠢࡇࡣ࡯ࡷࡪࠨᏌ"), help=bstack1ll_opy_ (u"ࠣࡃࡸࡸࡴࡳࡡࡵ࡫ࡦࠤࡸ࡫ࡴࠡࡵࡨࡷࡸ࡯࡯࡯ࠢࡱࡥࡲ࡫ࠢᏍ"))
    try:
        import pytest_selenium.pytest_selenium
    except:
        parser.addoption(bstack1ll_opy_ (u"ࠤ࠰࠱ࡩࡸࡩࡷࡧࡵࠦᏎ"), action=bstack1ll_opy_ (u"ࠥࡷࡹࡵࡲࡦࠤᏏ"), default=bstack1ll_opy_ (u"ࠦࡨ࡮ࡲࡰ࡯ࡨࠦᏐ"),
                         help=bstack1ll_opy_ (u"ࠧࡊࡲࡪࡸࡨࡶࠥࡺ࡯ࠡࡴࡸࡲࠥࡺࡥࡴࡶࡶࠦᏑ"))
def bstack111l11llll_opy_(log):
    if not (log[bstack1ll_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧᏒ")] and log[bstack1ll_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨᏓ")].strip()):
        return
    active = bstack111ll1111l_opy_()
    log = {
        bstack1ll_opy_ (u"ࠨ࡮ࡨࡺࡪࡲࠧᏔ"): log[bstack1ll_opy_ (u"ࠩ࡯ࡩࡻ࡫࡬ࠨᏕ")],
        bstack1ll_opy_ (u"ࠪࡸ࡮ࡳࡥࡴࡶࡤࡱࡵ࠭Ꮦ"): datetime.datetime.utcnow().isoformat() + bstack1ll_opy_ (u"ࠫ࡟࠭Ꮧ"),
        bstack1ll_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ࠭Ꮨ"): log[bstack1ll_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧᏙ")],
    }
    if active:
        if active[bstack1ll_opy_ (u"ࠧࡵࡻࡳࡩࠬᏚ")] == bstack1ll_opy_ (u"ࠨࡪࡲࡳࡰ࠭Ꮫ"):
            log[bstack1ll_opy_ (u"ࠩ࡫ࡳࡴࡱ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩᏜ")] = active[bstack1ll_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪᏝ")]
        elif active[bstack1ll_opy_ (u"ࠫࡹࡿࡰࡦࠩᏞ")] == bstack1ll_opy_ (u"ࠬࡺࡥࡴࡶࠪᏟ"):
            log[bstack1ll_opy_ (u"࠭ࡴࡦࡵࡷࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭Ꮰ")] = active[bstack1ll_opy_ (u"ࠧࡵࡧࡶࡸࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧᏡ")]
    bstack11l1l1l1_opy_.bstack11l1111l1l_opy_([log])
def bstack111ll1111l_opy_():
    if len(store[bstack1ll_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡ࡫ࡳࡴࡱ࡟ࡶࡷ࡬ࡨࠬᏢ")]) > 0 and store[bstack1ll_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢ࡬ࡴࡵ࡫ࡠࡷࡸ࡭ࡩ࠭Ꮳ")][-1]:
        return {
            bstack1ll_opy_ (u"ࠪࡸࡾࡶࡥࠨᏤ"): bstack1ll_opy_ (u"ࠫ࡭ࡵ࡯࡬ࠩᏥ"),
            bstack1ll_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠬᏦ"): store[bstack1ll_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡩࡱࡲ࡯ࡤࡻࡵࡪࡦࠪᏧ")][-1]
        }
    if store.get(bstack1ll_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡶࡨࡷࡹࡥࡵࡶ࡫ࡧࠫᏨ"), None):
        return {
            bstack1ll_opy_ (u"ࠨࡶࡼࡴࡪ࠭Ꮹ"): bstack1ll_opy_ (u"ࠩࡷࡩࡸࡺࠧᏪ"),
            bstack1ll_opy_ (u"ࠪࡸࡪࡹࡴࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪᏫ"): store[bstack1ll_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤࡺࡥࡴࡶࡢࡹࡺ࡯ࡤࠨᏬ")]
        }
    return None
bstack111l1ll111_opy_ = bstack1l1l1l11ll_opy_(bstack111l11llll_opy_)
def pytest_runtest_call(item):
    try:
        global CONFIG
        global bstack111l1lllll_opy_
        if bstack111l1lllll_opy_:
            driver = getattr(item, bstack1ll_opy_ (u"ࠬࡥࡤࡳ࡫ࡹࡩࡷ࠭Ꮽ"), None)
            bstack111l11l11l_opy_ = bstack1lll1ll1_opy_.bstack1l1lll111l_opy_(CONFIG, bstack1l111ll111_opy_(item.own_markers))
            item._a11y_started = bstack1lll1ll1_opy_.bstack1l1ll11l11_opy_(driver, bstack111l11l11l_opy_)
        if not bstack11l1l1l1_opy_.on() or bstack111ll111l1_opy_ != bstack1ll_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭Ꮾ"):
            return
        global current_test_uuid, bstack111l1ll111_opy_
        bstack111l1ll111_opy_.start()
        bstack111ll11l11_opy_ = {
            bstack1ll_opy_ (u"ࠧࡶࡷ࡬ࡨࠬᏯ"): uuid4().__str__(),
            bstack1ll_opy_ (u"ࠨࡵࡷࡥࡷࡺࡥࡥࡡࡤࡸࠬᏰ"): datetime.datetime.utcnow().isoformat() + bstack1ll_opy_ (u"ࠩ࡝ࠫᏱ")
        }
        current_test_uuid = bstack111ll11l11_opy_[bstack1ll_opy_ (u"ࠪࡹࡺ࡯ࡤࠨᏲ")]
        store[bstack1ll_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤࡺࡥࡴࡶࡢࡹࡺ࡯ࡤࠨᏳ")] = bstack111ll11l11_opy_[bstack1ll_opy_ (u"ࠬࡻࡵࡪࡦࠪᏴ")]
        threading.current_thread().current_test_uuid = current_test_uuid
        _111l111l11_opy_[item.nodeid] = {**_111l111l11_opy_[item.nodeid], **bstack111ll11l11_opy_}
        bstack111ll11l1l_opy_(item, _111l111l11_opy_[item.nodeid], bstack1ll_opy_ (u"࠭ࡔࡦࡵࡷࡖࡺࡴࡓࡵࡣࡵࡸࡪࡪࠧᏵ"))
    except Exception as err:
        print(bstack1ll_opy_ (u"ࠧࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡰࡺࡶࡨࡷࡹࡥࡲࡶࡰࡷࡩࡸࡺ࡟ࡤࡣ࡯ࡰ࠿ࠦࡻࡾࠩ᏶"), str(err))
def pytest_runtest_setup(item):
    if bstack1l11llll1l_opy_():
        atexit.register(bstack1ll1l1ll1l_opy_)
        try:
            item.config.hook.pytest_selenium_runtest_makereport = bstack11ll111l1l_opy_
        except Exception as err:
            threading.current_thread().testStatus = bstack1ll_opy_ (u"ࠨࡲࡤࡷࡸ࡫ࡤࠨ᏷")
    try:
        if not bstack11l1l1l1_opy_.on():
            return
        bstack111l1ll111_opy_.start()
        uuid = uuid4().__str__()
        bstack111ll11l11_opy_ = {
            bstack1ll_opy_ (u"ࠩࡸࡹ࡮ࡪࠧᏸ"): uuid,
            bstack1ll_opy_ (u"ࠪࡷࡹࡧࡲࡵࡧࡧࡣࡦࡺࠧᏹ"): datetime.datetime.utcnow().isoformat() + bstack1ll_opy_ (u"ࠫ࡟࠭ᏺ"),
            bstack1ll_opy_ (u"ࠬࡺࡹࡱࡧࠪᏻ"): bstack1ll_opy_ (u"࠭ࡨࡰࡱ࡮ࠫᏼ"),
            bstack1ll_opy_ (u"ࠧࡩࡱࡲ࡯ࡤࡺࡹࡱࡧࠪᏽ"): bstack1ll_opy_ (u"ࠨࡄࡈࡊࡔࡘࡅࡠࡇࡄࡇࡍ࠭᏾"),
            bstack1ll_opy_ (u"ࠩ࡫ࡳࡴࡱ࡟࡯ࡣࡰࡩࠬ᏿"): bstack1ll_opy_ (u"ࠪࡷࡪࡺࡵࡱࠩ᐀")
        }
        threading.current_thread().bstack111l1l11ll_opy_ = uuid
        store[bstack1ll_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤࡺࡥࡴࡶࡢ࡭ࡹ࡫࡭ࠨᐁ")] = item
        store[bstack1ll_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡨࡰࡱ࡮ࡣࡺࡻࡩࡥࠩᐂ")] = [uuid]
        if not _111l111l11_opy_.get(item.nodeid, None):
            _111l111l11_opy_[item.nodeid] = {bstack1ll_opy_ (u"࠭ࡨࡰࡱ࡮ࡷࠬᐃ"): [], bstack1ll_opy_ (u"ࠧࡧ࡫ࡻࡸࡺࡸࡥࡴࠩᐄ"): []}
        _111l111l11_opy_[item.nodeid][bstack1ll_opy_ (u"ࠨࡪࡲࡳࡰࡹࠧᐅ")].append(bstack111ll11l11_opy_[bstack1ll_opy_ (u"ࠩࡸࡹ࡮ࡪࠧᐆ")])
        _111l111l11_opy_[item.nodeid + bstack1ll_opy_ (u"ࠪ࠱ࡸ࡫ࡴࡶࡲࠪᐇ")] = bstack111ll11l11_opy_
        bstack111l1ll11l_opy_(item, bstack111ll11l11_opy_, bstack1ll_opy_ (u"ࠫࡍࡵ࡯࡬ࡔࡸࡲࡘࡺࡡࡳࡶࡨࡨࠬᐈ"))
    except Exception as err:
        print(bstack1ll_opy_ (u"ࠬࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤࡵࡿࡴࡦࡵࡷࡣࡷࡻ࡮ࡵࡧࡶࡸࡤࡹࡥࡵࡷࡳ࠾ࠥࢁࡽࠨᐉ"), str(err))
def pytest_runtest_teardown(item):
    try:
        if getattr(item, bstack1ll_opy_ (u"࠭࡟ࡢ࠳࠴ࡽࡤࡹࡴࡢࡴࡷࡩࡩ࠭ᐊ"), False):
            logger.info(bstack1ll_opy_ (u"ࠢࡂࡷࡷࡳࡲࡧࡴࡦࠢࡷࡩࡸࡺࠠࡤࡣࡶࡩࠥ࡫ࡸࡦࡥࡸࡸ࡮ࡵ࡮ࠡࡪࡤࡷࠥ࡫࡮ࡥࡧࡧ࠲ࠥࡖࡲࡰࡥࡨࡷࡸ࡯࡮ࡨࠢࡩࡳࡷࠦࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡴࡦࡵࡷ࡭ࡳ࡭ࠠࡪࡵࠣࡹࡳࡪࡥࡳࡹࡤࡽ࠳ࠦࠢᐋ"))
            driver = getattr(item, bstack1ll_opy_ (u"ࠨࡡࡧࡶ࡮ࡼࡥࡳࠩᐌ"), None)
            bstack1lll1ll1_opy_.bstack1l1ll1l1ll_opy_(driver, item)
        if not bstack11l1l1l1_opy_.on():
            return
        bstack111ll11l11_opy_ = {
            bstack1ll_opy_ (u"ࠩࡸࡹ࡮ࡪࠧᐍ"): uuid4().__str__(),
            bstack1ll_opy_ (u"ࠪࡷࡹࡧࡲࡵࡧࡧࡣࡦࡺࠧᐎ"): datetime.datetime.utcnow().isoformat() + bstack1ll_opy_ (u"ࠫ࡟࠭ᐏ"),
            bstack1ll_opy_ (u"ࠬࡺࡹࡱࡧࠪᐐ"): bstack1ll_opy_ (u"࠭ࡨࡰࡱ࡮ࠫᐑ"),
            bstack1ll_opy_ (u"ࠧࡩࡱࡲ࡯ࡤࡺࡹࡱࡧࠪᐒ"): bstack1ll_opy_ (u"ࠨࡃࡉࡘࡊࡘ࡟ࡆࡃࡆࡌࠬᐓ"),
            bstack1ll_opy_ (u"ࠩ࡫ࡳࡴࡱ࡟࡯ࡣࡰࡩࠬᐔ"): bstack1ll_opy_ (u"ࠪࡸࡪࡧࡲࡥࡱࡺࡲࠬᐕ")
        }
        _111l111l11_opy_[item.nodeid + bstack1ll_opy_ (u"ࠫ࠲ࡺࡥࡢࡴࡧࡳࡼࡴࠧᐖ")] = bstack111ll11l11_opy_
        bstack111l1ll11l_opy_(item, bstack111ll11l11_opy_, bstack1ll_opy_ (u"ࠬࡎ࡯ࡰ࡭ࡕࡹࡳ࡙ࡴࡢࡴࡷࡩࡩ࠭ᐗ"))
    except Exception as err:
        print(bstack1ll_opy_ (u"࠭ࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡶࡹࡵࡧࡶࡸࡤࡸࡵ࡯ࡶࡨࡷࡹࡥࡴࡦࡣࡵࡨࡴࡽ࡮࠻ࠢࡾࢁࠬᐘ"), str(err))
@pytest.hookimpl(hookwrapper=True)
def pytest_fixture_setup(fixturedef, request):
    if not bstack11l1l1l1_opy_.on():
        yield
        return
    start_time = datetime.datetime.now()
    if bstack11ll11111l_opy_(fixturedef.argname):
        store[bstack1ll_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠ࡯ࡲࡨࡺࡲࡥࡠ࡫ࡷࡩࡲ࠭ᐙ")] = request.node
    elif bstack11ll1111l1_opy_(fixturedef.argname):
        store[bstack1ll_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡࡦࡰࡦࡹࡳࡠ࡫ࡷࡩࡲ࠭ᐚ")] = request.node
    outcome = yield
    try:
        fixture = {
            bstack1ll_opy_ (u"ࠩࡱࡥࡲ࡫ࠧᐛ"): fixturedef.argname,
            bstack1ll_opy_ (u"ࠪࡶࡪࡹࡵ࡭ࡶࠪᐜ"): bstack1l11lllll1_opy_(outcome),
            bstack1ll_opy_ (u"ࠫࡩࡻࡲࡢࡶ࡬ࡳࡳ࠭ᐝ"): (datetime.datetime.now() - start_time).total_seconds() * 1000
        }
        bstack111ll1l11l_opy_ = store[bstack1ll_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡴࡦࡵࡷࡣ࡮ࡺࡥ࡮ࠩᐞ")]
        if not _111l111l11_opy_.get(bstack111ll1l11l_opy_.nodeid, None):
            _111l111l11_opy_[bstack111ll1l11l_opy_.nodeid] = {bstack1ll_opy_ (u"࠭ࡦࡪࡺࡷࡹࡷ࡫ࡳࠨᐟ"): []}
        _111l111l11_opy_[bstack111ll1l11l_opy_.nodeid][bstack1ll_opy_ (u"ࠧࡧ࡫ࡻࡸࡺࡸࡥࡴࠩᐠ")].append(fixture)
    except Exception as err:
        logger.debug(bstack1ll_opy_ (u"ࠨࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡱࡻࡷࡩࡸࡺ࡟ࡧ࡫ࡻࡸࡺࡸࡥࡠࡵࡨࡸࡺࡶ࠺ࠡࡽࢀࠫᐡ"), str(err))
if bstack1ll1ll11l1_opy_() and bstack11l1l1l1_opy_.on():
    def pytest_bdd_before_step(request, step):
        try:
            _111l111l11_opy_[request.node.nodeid][bstack1ll_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡥࡣࡷࡥࠬᐢ")].bstack11l11l1l1l_opy_(id(step))
        except Exception as err:
            print(bstack1ll_opy_ (u"ࠪࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡳࡽࡹ࡫ࡳࡵࡡࡥࡨࡩࡥࡢࡦࡨࡲࡶࡪࡥࡳࡵࡧࡳ࠾ࠥࢁࡽࠨᐣ"), str(err))
    def pytest_bdd_step_error(request, step, exception):
        try:
            _111l111l11_opy_[request.node.nodeid][bstack1ll_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡧࡥࡹࡧࠧᐤ")].bstack11l11l111l_opy_(id(step), Result.failed(exception=exception))
        except Exception as err:
            print(bstack1ll_opy_ (u"ࠬࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤࡵࡿࡴࡦࡵࡷࡣࡧࡪࡤࡠࡵࡷࡩࡵࡥࡥࡳࡴࡲࡶ࠿ࠦࡻࡾࠩᐥ"), str(err))
    def pytest_bdd_after_step(request, step):
        try:
            bstack11l11ll1l1_opy_: bstack11l11ll111_opy_ = _111l111l11_opy_[request.node.nodeid][bstack1ll_opy_ (u"࠭ࡴࡦࡵࡷࡣࡩࡧࡴࡢࠩᐦ")]
            bstack11l11ll1l1_opy_.bstack11l11l111l_opy_(id(step), Result.passed())
        except Exception as err:
            print(bstack1ll_opy_ (u"ࠧࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡰࡺࡶࡨࡷࡹࡥࡢࡥࡦࡢࡷࡹ࡫ࡰࡠࡧࡵࡶࡴࡸ࠺ࠡࡽࢀࠫᐧ"), str(err))
    def pytest_bdd_before_scenario(request, feature, scenario):
        global bstack111ll111l1_opy_
        try:
            if not bstack11l1l1l1_opy_.on() or bstack111ll111l1_opy_ != bstack1ll_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴ࠮ࡤࡧࡨࠬᐨ"):
                return
            global bstack111l1ll111_opy_
            bstack111l1ll111_opy_.start()
            if not _111l111l11_opy_.get(request.node.nodeid, None):
                _111l111l11_opy_[request.node.nodeid] = {}
            bstack11l11ll1l1_opy_ = bstack11l11ll111_opy_.bstack11l111ll11_opy_(
                scenario, feature, request.node,
                name=bstack11ll111111_opy_(request.node, scenario),
                bstack11l111llll_opy_=bstack1lllll1ll1_opy_(),
                file_path=feature.filename,
                scope=[feature.name],
                framework=bstack1ll_opy_ (u"ࠩࡓࡽࡹ࡫ࡳࡵ࠯ࡦࡹࡨࡻ࡭ࡣࡧࡵࠫᐩ"),
                tags=bstack11l1lllll1_opy_(feature, scenario)
            )
            _111l111l11_opy_[request.node.nodeid][bstack1ll_opy_ (u"ࠪࡸࡪࡹࡴࡠࡦࡤࡸࡦ࠭ᐪ")] = bstack11l11ll1l1_opy_
            bstack111l1111ll_opy_(bstack11l11ll1l1_opy_.uuid)
            bstack11l1l1l1_opy_.bstack111lll111l_opy_(bstack1ll_opy_ (u"࡙ࠫ࡫ࡳࡵࡔࡸࡲࡘࡺࡡࡳࡶࡨࡨࠬᐫ"), bstack11l11ll1l1_opy_)
        except Exception as err:
            print(bstack1ll_opy_ (u"ࠬࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤࡵࡿࡴࡦࡵࡷࡣࡧࡪࡤࡠࡤࡨࡪࡴࡸࡥࡠࡵࡦࡩࡳࡧࡲࡪࡱ࠽ࠤࢀࢃࠧᐬ"), str(err))
def bstack111l1ll1ll_opy_(bstack111l11l1ll_opy_):
    if bstack111l11l1ll_opy_ in store[bstack1ll_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡩࡱࡲ࡯ࡤࡻࡵࡪࡦࠪᐭ")]:
        store[bstack1ll_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡪࡲࡳࡰࡥࡵࡶ࡫ࡧࠫᐮ")].remove(bstack111l11l1ll_opy_)
def bstack111l1111ll_opy_(bstack111l11lll1_opy_):
    store[bstack1ll_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡࡷࡩࡸࡺ࡟ࡶࡷ࡬ࡨࠬᐯ")] = bstack111l11lll1_opy_
    threading.current_thread().current_test_uuid = bstack111l11lll1_opy_
@bstack11l1l1l1_opy_.bstack11l1111111_opy_
def bstack111l1111l1_opy_(item, call, report):
    global bstack111ll111l1_opy_
    try:
        if report.when == bstack1ll_opy_ (u"ࠩࡦࡥࡱࡲࠧᐰ"):
            bstack111l1ll111_opy_.reset()
        if report.when == bstack1ll_opy_ (u"ࠪࡧࡦࡲ࡬ࠨᐱ"):
            if bstack111ll111l1_opy_ == bstack1ll_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࠫᐲ"):
                _111l111l11_opy_[item.nodeid][bstack1ll_opy_ (u"ࠬ࡬ࡩ࡯࡫ࡶ࡬ࡪࡪ࡟ࡢࡶࠪᐳ")] = bstack1l11lll1l1_opy_(report.stop)
                bstack111ll11l1l_opy_(item, _111l111l11_opy_[item.nodeid], bstack1ll_opy_ (u"࠭ࡔࡦࡵࡷࡖࡺࡴࡆࡪࡰ࡬ࡷ࡭࡫ࡤࠨᐴ"), report, call)
                store[bstack1ll_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡶࡨࡷࡹࡥࡵࡶ࡫ࡧࠫᐵ")] = None
            elif bstack111ll111l1_opy_ == bstack1ll_opy_ (u"ࠣࡲࡼࡸࡪࡹࡴ࠮ࡤࡧࡨࠧᐶ"):
                bstack11l11ll1l1_opy_ = _111l111l11_opy_[item.nodeid][bstack1ll_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡥࡣࡷࡥࠬᐷ")]
                bstack11l11ll1l1_opy_.set(hooks=_111l111l11_opy_[item.nodeid].get(bstack1ll_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡴࠩᐸ"), []))
                exception, bstack1l1l111lll_opy_ = None, None
                if call.excinfo:
                    exception = call.excinfo.value
                    bstack1l1l111lll_opy_ = [call.excinfo.exconly(), report.longreprtext]
                bstack11l11ll1l1_opy_.stop(time=bstack1l11lll1l1_opy_(report.stop), result=Result(result=report.outcome, exception=exception, bstack1l1l111lll_opy_=bstack1l1l111lll_opy_))
                bstack11l1l1l1_opy_.bstack111lll111l_opy_(bstack1ll_opy_ (u"࡙ࠫ࡫ࡳࡵࡔࡸࡲࡋ࡯࡮ࡪࡵ࡫ࡩࡩ࠭ᐹ"), _111l111l11_opy_[item.nodeid][bstack1ll_opy_ (u"ࠬࡺࡥࡴࡶࡢࡨࡦࡺࡡࠨᐺ")])
        elif report.when in [bstack1ll_opy_ (u"࠭ࡳࡦࡶࡸࡴࠬᐻ"), bstack1ll_opy_ (u"ࠧࡵࡧࡤࡶࡩࡵࡷ࡯ࠩᐼ")]:
            bstack111l1lll1l_opy_ = item.nodeid + bstack1ll_opy_ (u"ࠨ࠯ࠪᐽ") + report.when
            if report.skipped:
                hook_type = bstack1ll_opy_ (u"ࠩࡅࡉࡋࡕࡒࡆࡡࡈࡅࡈࡎࠧᐾ") if report.when == bstack1ll_opy_ (u"ࠪࡷࡪࡺࡵࡱࠩᐿ") else bstack1ll_opy_ (u"ࠫࡆࡌࡔࡆࡔࡢࡉࡆࡉࡈࠨᑀ")
                _111l111l11_opy_[bstack111l1lll1l_opy_] = {
                    bstack1ll_opy_ (u"ࠬࡻࡵࡪࡦࠪᑁ"): uuid4().__str__(),
                    bstack1ll_opy_ (u"࠭ࡳࡵࡣࡵࡸࡪࡪ࡟ࡢࡶࠪᑂ"): datetime.datetime.utcfromtimestamp(report.start).isoformat() + bstack1ll_opy_ (u"࡛ࠧࠩᑃ"),
                    bstack1ll_opy_ (u"ࠨࡪࡲࡳࡰࡥࡴࡺࡲࡨࠫᑄ"): hook_type
                }
            _111l111l11_opy_[bstack111l1lll1l_opy_][bstack1ll_opy_ (u"ࠩࡩ࡭ࡳ࡯ࡳࡩࡧࡧࡣࡦࡺࠧᑅ")] = datetime.datetime.utcfromtimestamp(report.stop).isoformat() + bstack1ll_opy_ (u"ࠪ࡞ࠬᑆ")
            bstack111l1ll1ll_opy_(_111l111l11_opy_[bstack111l1lll1l_opy_][bstack1ll_opy_ (u"ࠫࡺࡻࡩࡥࠩᑇ")])
            bstack111l1ll11l_opy_(item, _111l111l11_opy_[bstack111l1lll1l_opy_], bstack1ll_opy_ (u"ࠬࡎ࡯ࡰ࡭ࡕࡹࡳࡌࡩ࡯࡫ࡶ࡬ࡪࡪࠧᑈ"), report, call)
            if report.when == bstack1ll_opy_ (u"࠭ࡳࡦࡶࡸࡴࠬᑉ"):
                if report.outcome == bstack1ll_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧᑊ"):
                    bstack111ll11l11_opy_ = {
                        bstack1ll_opy_ (u"ࠨࡷࡸ࡭ࡩ࠭ᑋ"): uuid4().__str__(),
                        bstack1ll_opy_ (u"ࠩࡶࡸࡦࡸࡴࡦࡦࡢࡥࡹ࠭ᑌ"): bstack1lllll1ll1_opy_(),
                        bstack1ll_opy_ (u"ࠪࡪ࡮ࡴࡩࡴࡪࡨࡨࡤࡧࡴࠨᑍ"): bstack1lllll1ll1_opy_()
                    }
                    _111l111l11_opy_[item.nodeid] = {**_111l111l11_opy_[item.nodeid], **bstack111ll11l11_opy_}
                    bstack111ll11l1l_opy_(item, _111l111l11_opy_[item.nodeid], bstack1ll_opy_ (u"࡙ࠫ࡫ࡳࡵࡔࡸࡲࡘࡺࡡࡳࡶࡨࡨࠬᑎ"))
                    bstack111ll11l1l_opy_(item, _111l111l11_opy_[item.nodeid], bstack1ll_opy_ (u"࡚ࠬࡥࡴࡶࡕࡹࡳࡌࡩ࡯࡫ࡶ࡬ࡪࡪࠧᑏ"), report, call)
    except Exception as err:
        print(bstack1ll_opy_ (u"࠭ࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥ࡮ࡡ࡯ࡦ࡯ࡩࡤࡵ࠱࠲ࡻࡢࡸࡪࡹࡴࡠࡧࡹࡩࡳࡺ࠺ࠡࡽࢀࠫᑐ"), str(err))
def bstack111l11l111_opy_(test, bstack111ll11l11_opy_, result=None, call=None, bstack1l1l11ll_opy_=None, outcome=None):
    file_path = os.path.relpath(test.fspath.strpath, start=os.getcwd())
    bstack11l11ll1l1_opy_ = {
        bstack1ll_opy_ (u"ࠧࡶࡷ࡬ࡨࠬᑑ"): bstack111ll11l11_opy_[bstack1ll_opy_ (u"ࠨࡷࡸ࡭ࡩ࠭ᑒ")],
        bstack1ll_opy_ (u"ࠩࡷࡽࡵ࡫ࠧᑓ"): bstack1ll_opy_ (u"ࠪࡸࡪࡹࡴࠨᑔ"),
        bstack1ll_opy_ (u"ࠫࡳࡧ࡭ࡦࠩᑕ"): test.name,
        bstack1ll_opy_ (u"ࠬࡨ࡯ࡥࡻࠪᑖ"): {
            bstack1ll_opy_ (u"࠭࡬ࡢࡰࡪࠫᑗ"): bstack1ll_opy_ (u"ࠧࡱࡻࡷ࡬ࡴࡴࠧᑘ"),
            bstack1ll_opy_ (u"ࠨࡥࡲࡨࡪ࠭ᑙ"): inspect.getsource(test.obj)
        },
        bstack1ll_opy_ (u"ࠩ࡬ࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭ᑚ"): test.name,
        bstack1ll_opy_ (u"ࠪࡷࡨࡵࡰࡦࠩᑛ"): test.name,
        bstack1ll_opy_ (u"ࠫࡸࡩ࡯ࡱࡧࡶࠫᑜ"): bstack11l1l1l1_opy_.bstack111lllll1l_opy_(test),
        bstack1ll_opy_ (u"ࠬ࡬ࡩ࡭ࡧࡢࡲࡦࡳࡥࠨᑝ"): file_path,
        bstack1ll_opy_ (u"࠭࡬ࡰࡥࡤࡸ࡮ࡵ࡮ࠨᑞ"): file_path,
        bstack1ll_opy_ (u"ࠧࡳࡧࡶࡹࡱࡺࠧᑟ"): bstack1ll_opy_ (u"ࠨࡲࡨࡲࡩ࡯࡮ࡨࠩᑠ"),
        bstack1ll_opy_ (u"ࠩࡹࡧࡤ࡬ࡩ࡭ࡧࡳࡥࡹ࡮ࠧᑡ"): file_path,
        bstack1ll_opy_ (u"ࠪࡷࡹࡧࡲࡵࡧࡧࡣࡦࡺࠧᑢ"): bstack111ll11l11_opy_[bstack1ll_opy_ (u"ࠫࡸࡺࡡࡳࡶࡨࡨࡤࡧࡴࠨᑣ")],
        bstack1ll_opy_ (u"ࠬ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࠨᑤ"): bstack1ll_opy_ (u"࠭ࡐࡺࡶࡨࡷࡹ࠭ᑥ"),
        bstack1ll_opy_ (u"ࠧࡤࡷࡶࡸࡴࡳࡒࡦࡴࡸࡲࡕࡧࡲࡢ࡯ࠪᑦ"): {
            bstack1ll_opy_ (u"ࠨࡴࡨࡶࡺࡴ࡟࡯ࡣࡰࡩࠬᑧ"): test.nodeid
        },
        bstack1ll_opy_ (u"ࠩࡷࡥ࡬ࡹࠧᑨ"): bstack1l111ll111_opy_(test.own_markers)
    }
    if bstack1l1l11ll_opy_ in [bstack1ll_opy_ (u"ࠪࡘࡪࡹࡴࡓࡷࡱࡗࡰ࡯ࡰࡱࡧࡧࠫᑩ"), bstack1ll_opy_ (u"࡙ࠫ࡫ࡳࡵࡔࡸࡲࡋ࡯࡮ࡪࡵ࡫ࡩࡩ࠭ᑪ")]:
        bstack11l11ll1l1_opy_[bstack1ll_opy_ (u"ࠬࡳࡥࡵࡣࠪᑫ")] = {
            bstack1ll_opy_ (u"࠭ࡦࡪࡺࡷࡹࡷ࡫ࡳࠨᑬ"): bstack111ll11l11_opy_.get(bstack1ll_opy_ (u"ࠧࡧ࡫ࡻࡸࡺࡸࡥࡴࠩᑭ"), [])
        }
    if bstack1l1l11ll_opy_ == bstack1ll_opy_ (u"ࠨࡖࡨࡷࡹࡘࡵ࡯ࡕ࡮࡭ࡵࡶࡥࡥࠩᑮ"):
        bstack11l11ll1l1_opy_[bstack1ll_opy_ (u"ࠩࡵࡩࡸࡻ࡬ࡵࠩᑯ")] = bstack1ll_opy_ (u"ࠪࡷࡰ࡯ࡰࡱࡧࡧࠫᑰ")
        bstack11l11ll1l1_opy_[bstack1ll_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡵࠪᑱ")] = bstack111ll11l11_opy_[bstack1ll_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡶࠫᑲ")]
        bstack11l11ll1l1_opy_[bstack1ll_opy_ (u"࠭ࡦࡪࡰ࡬ࡷ࡭࡫ࡤࡠࡣࡷࠫᑳ")] = bstack111ll11l11_opy_[bstack1ll_opy_ (u"ࠧࡧ࡫ࡱ࡭ࡸ࡮ࡥࡥࡡࡤࡸࠬᑴ")]
    if result:
        bstack11l11ll1l1_opy_[bstack1ll_opy_ (u"ࠨࡴࡨࡷࡺࡲࡴࠨᑵ")] = result.outcome
        bstack11l11ll1l1_opy_[bstack1ll_opy_ (u"ࠩࡧࡹࡷࡧࡴࡪࡱࡱࡣ࡮ࡴ࡟࡮ࡵࠪᑶ")] = result.duration * 1000
        bstack11l11ll1l1_opy_[bstack1ll_opy_ (u"ࠪࡪ࡮ࡴࡩࡴࡪࡨࡨࡤࡧࡴࠨᑷ")] = bstack111ll11l11_opy_[bstack1ll_opy_ (u"ࠫ࡫࡯࡮ࡪࡵ࡫ࡩࡩࡥࡡࡵࠩᑸ")]
        if result.failed:
            bstack11l11ll1l1_opy_[bstack1ll_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡸࡶࡪࡥࡴࡺࡲࡨࠫᑹ")] = bstack11l1l1l1_opy_.bstack1l11l111l1_opy_(call.excinfo.typename)
            bstack11l11ll1l1_opy_[bstack1ll_opy_ (u"࠭ࡦࡢ࡫࡯ࡹࡷ࡫ࠧᑺ")] = bstack11l1l1l1_opy_.bstack111ll1llll_opy_(call.excinfo, result)
        bstack11l11ll1l1_opy_[bstack1ll_opy_ (u"ࠧࡩࡱࡲ࡯ࡸ࠭ᑻ")] = bstack111ll11l11_opy_[bstack1ll_opy_ (u"ࠨࡪࡲࡳࡰࡹࠧᑼ")]
    if outcome:
        bstack11l11ll1l1_opy_[bstack1ll_opy_ (u"ࠩࡵࡩࡸࡻ࡬ࡵࠩᑽ")] = bstack1l11lllll1_opy_(outcome)
        bstack11l11ll1l1_opy_[bstack1ll_opy_ (u"ࠪࡨࡺࡸࡡࡵ࡫ࡲࡲࡤ࡯࡮ࡠ࡯ࡶࠫᑾ")] = 0
        bstack11l11ll1l1_opy_[bstack1ll_opy_ (u"ࠫ࡫࡯࡮ࡪࡵ࡫ࡩࡩࡥࡡࡵࠩᑿ")] = bstack111ll11l11_opy_[bstack1ll_opy_ (u"ࠬ࡬ࡩ࡯࡫ࡶ࡬ࡪࡪ࡟ࡢࡶࠪᒀ")]
        if bstack11l11ll1l1_opy_[bstack1ll_opy_ (u"࠭ࡲࡦࡵࡸࡰࡹ࠭ᒁ")] == bstack1ll_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧᒂ"):
            bstack11l11ll1l1_opy_[bstack1ll_opy_ (u"ࠨࡨࡤ࡭ࡱࡻࡲࡦࡡࡷࡽࡵ࡫ࠧᒃ")] = bstack1ll_opy_ (u"ࠩࡘࡲ࡭ࡧ࡮ࡥ࡮ࡨࡨࡊࡸࡲࡰࡴࠪᒄ")  # bstack111l11l1l1_opy_
            bstack11l11ll1l1_opy_[bstack1ll_opy_ (u"ࠪࡪࡦ࡯࡬ࡶࡴࡨࠫᒅ")] = [{bstack1ll_opy_ (u"ࠫࡧࡧࡣ࡬ࡶࡵࡥࡨ࡫ࠧᒆ"): [bstack1ll_opy_ (u"ࠬࡹ࡯࡮ࡧࠣࡩࡷࡸ࡯ࡳࠩᒇ")]}]
        bstack11l11ll1l1_opy_[bstack1ll_opy_ (u"࠭ࡨࡰࡱ࡮ࡷࠬᒈ")] = bstack111ll11l11_opy_[bstack1ll_opy_ (u"ࠧࡩࡱࡲ࡯ࡸ࠭ᒉ")]
    return bstack11l11ll1l1_opy_
def bstack111l1l111l_opy_(test, bstack111l1l1l1l_opy_, bstack1l1l11ll_opy_, result, call, outcome, bstack111l111lll_opy_):
    file_path = os.path.relpath(test.fspath.strpath, start=os.getcwd())
    hook_type = bstack111l1l1l1l_opy_[bstack1ll_opy_ (u"ࠨࡪࡲࡳࡰࡥࡴࡺࡲࡨࠫᒊ")]
    hook_name = bstack111l1l1l1l_opy_[bstack1ll_opy_ (u"ࠩ࡫ࡳࡴࡱ࡟࡯ࡣࡰࡩࠬᒋ")]
    hook_data = {
        bstack1ll_opy_ (u"ࠪࡹࡺ࡯ࡤࠨᒌ"): bstack111l1l1l1l_opy_[bstack1ll_opy_ (u"ࠫࡺࡻࡩࡥࠩᒍ")],
        bstack1ll_opy_ (u"ࠬࡺࡹࡱࡧࠪᒎ"): bstack1ll_opy_ (u"࠭ࡨࡰࡱ࡮ࠫᒏ"),
        bstack1ll_opy_ (u"ࠧ࡯ࡣࡰࡩࠬᒐ"): bstack1ll_opy_ (u"ࠨࡽࢀࠫᒑ").format(bstack11ll111l11_opy_(hook_name)),
        bstack1ll_opy_ (u"ࠩࡥࡳࡩࡿࠧᒒ"): {
            bstack1ll_opy_ (u"ࠪࡰࡦࡴࡧࠨᒓ"): bstack1ll_opy_ (u"ࠫࡵࡿࡴࡩࡱࡱࠫᒔ"),
            bstack1ll_opy_ (u"ࠬࡩ࡯ࡥࡧࠪᒕ"): None
        },
        bstack1ll_opy_ (u"࠭ࡳࡤࡱࡳࡩࠬᒖ"): test.name,
        bstack1ll_opy_ (u"ࠧࡴࡥࡲࡴࡪࡹࠧᒗ"): bstack11l1l1l1_opy_.bstack111lllll1l_opy_(test, hook_name),
        bstack1ll_opy_ (u"ࠨࡨ࡬ࡰࡪࡥ࡮ࡢ࡯ࡨࠫᒘ"): file_path,
        bstack1ll_opy_ (u"ࠩ࡯ࡳࡨࡧࡴࡪࡱࡱࠫᒙ"): file_path,
        bstack1ll_opy_ (u"ࠪࡶࡪࡹࡵ࡭ࡶࠪᒚ"): bstack1ll_opy_ (u"ࠫࡵ࡫࡮ࡥ࡫ࡱ࡫ࠬᒛ"),
        bstack1ll_opy_ (u"ࠬࡼࡣࡠࡨ࡬ࡰࡪࡶࡡࡵࡪࠪᒜ"): file_path,
        bstack1ll_opy_ (u"࠭ࡳࡵࡣࡵࡸࡪࡪ࡟ࡢࡶࠪᒝ"): bstack111l1l1l1l_opy_[bstack1ll_opy_ (u"ࠧࡴࡶࡤࡶࡹ࡫ࡤࡠࡣࡷࠫᒞ")],
        bstack1ll_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࠫᒟ"): bstack1ll_opy_ (u"ࠩࡓࡽࡹ࡫ࡳࡵ࠯ࡦࡹࡨࡻ࡭ࡣࡧࡵࠫᒠ") if bstack111ll111l1_opy_ == bstack1ll_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶ࠰ࡦࡩࡪࠧᒡ") else bstack1ll_opy_ (u"ࠫࡕࡿࡴࡦࡵࡷࠫᒢ"),
        bstack1ll_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡢࡸࡾࡶࡥࠨᒣ"): hook_type
    }
    bstack111l1llll1_opy_ = bstack111l1l1ll1_opy_(_111l111l11_opy_.get(test.nodeid, None))
    if bstack111l1llll1_opy_:
        hook_data[bstack1ll_opy_ (u"࠭ࡴࡦࡵࡷࡣࡷࡻ࡮ࡠ࡫ࡧࠫᒤ")] = bstack111l1llll1_opy_
    if result:
        hook_data[bstack1ll_opy_ (u"ࠧࡳࡧࡶࡹࡱࡺࠧᒥ")] = result.outcome
        hook_data[bstack1ll_opy_ (u"ࠨࡦࡸࡶࡦࡺࡩࡰࡰࡢ࡭ࡳࡥ࡭ࡴࠩᒦ")] = result.duration * 1000
        hook_data[bstack1ll_opy_ (u"ࠩࡩ࡭ࡳ࡯ࡳࡩࡧࡧࡣࡦࡺࠧᒧ")] = bstack111l1l1l1l_opy_[bstack1ll_opy_ (u"ࠪࡪ࡮ࡴࡩࡴࡪࡨࡨࡤࡧࡴࠨᒨ")]
        if result.failed:
            hook_data[bstack1ll_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡷࡵࡩࡤࡺࡹࡱࡧࠪᒩ")] = bstack11l1l1l1_opy_.bstack1l11l111l1_opy_(call.excinfo.typename)
            hook_data[bstack1ll_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡸࡶࡪ࠭ᒪ")] = bstack11l1l1l1_opy_.bstack111ll1llll_opy_(call.excinfo, result)
    if outcome:
        hook_data[bstack1ll_opy_ (u"࠭ࡲࡦࡵࡸࡰࡹ࠭ᒫ")] = bstack1l11lllll1_opy_(outcome)
        hook_data[bstack1ll_opy_ (u"ࠧࡥࡷࡵࡥࡹ࡯࡯࡯ࡡ࡬ࡲࡤࡳࡳࠨᒬ")] = 100
        hook_data[bstack1ll_opy_ (u"ࠨࡨ࡬ࡲ࡮ࡹࡨࡦࡦࡢࡥࡹ࠭ᒭ")] = bstack111l1l1l1l_opy_[bstack1ll_opy_ (u"ࠩࡩ࡭ࡳ࡯ࡳࡩࡧࡧࡣࡦࡺࠧᒮ")]
        if hook_data[bstack1ll_opy_ (u"ࠪࡶࡪࡹࡵ࡭ࡶࠪᒯ")] == bstack1ll_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫᒰ"):
            hook_data[bstack1ll_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡸࡶࡪࡥࡴࡺࡲࡨࠫᒱ")] = bstack1ll_opy_ (u"࠭ࡕ࡯ࡪࡤࡲࡩࡲࡥࡥࡇࡵࡶࡴࡸࠧᒲ")  # bstack111l11l1l1_opy_
            hook_data[bstack1ll_opy_ (u"ࠧࡧࡣ࡬ࡰࡺࡸࡥࠨᒳ")] = [{bstack1ll_opy_ (u"ࠨࡤࡤࡧࡰࡺࡲࡢࡥࡨࠫᒴ"): [bstack1ll_opy_ (u"ࠩࡶࡳࡲ࡫ࠠࡦࡴࡵࡳࡷ࠭ᒵ")]}]
    if bstack111l111lll_opy_:
        hook_data[bstack1ll_opy_ (u"ࠪࡶࡪࡹࡵ࡭ࡶࠪᒶ")] = bstack111l111lll_opy_.result
        hook_data[bstack1ll_opy_ (u"ࠫࡩࡻࡲࡢࡶ࡬ࡳࡳࡥࡩ࡯ࡡࡰࡷࠬᒷ")] = bstack1l11l1l1ll_opy_(bstack111l1l1l1l_opy_[bstack1ll_opy_ (u"ࠬࡹࡴࡢࡴࡷࡩࡩࡥࡡࡵࠩᒸ")], bstack111l1l1l1l_opy_[bstack1ll_opy_ (u"࠭ࡦࡪࡰ࡬ࡷ࡭࡫ࡤࡠࡣࡷࠫᒹ")])
        hook_data[bstack1ll_opy_ (u"ࠧࡧ࡫ࡱ࡭ࡸ࡮ࡥࡥࡡࡤࡸࠬᒺ")] = bstack111l1l1l1l_opy_[bstack1ll_opy_ (u"ࠨࡨ࡬ࡲ࡮ࡹࡨࡦࡦࡢࡥࡹ࠭ᒻ")]
        if hook_data[bstack1ll_opy_ (u"ࠩࡵࡩࡸࡻ࡬ࡵࠩᒼ")] == bstack1ll_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪᒽ"):
            hook_data[bstack1ll_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡷࡵࡩࡤࡺࡹࡱࡧࠪᒾ")] = bstack11l1l1l1_opy_.bstack1l11l111l1_opy_(bstack111l111lll_opy_.exception_type)
            hook_data[bstack1ll_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡸࡶࡪ࠭ᒿ")] = [{bstack1ll_opy_ (u"࠭ࡢࡢࡥ࡮ࡸࡷࡧࡣࡦࠩᓀ"): bstack1l1l111111_opy_(bstack111l111lll_opy_.exception)}]
    return hook_data
def bstack111ll11l1l_opy_(test, bstack111ll11l11_opy_, bstack1l1l11ll_opy_, result=None, call=None, outcome=None):
    bstack11l11ll1l1_opy_ = bstack111l11l111_opy_(test, bstack111ll11l11_opy_, result, call, bstack1l1l11ll_opy_, outcome)
    driver = getattr(test, bstack1ll_opy_ (u"ࠧࡠࡦࡵ࡭ࡻ࡫ࡲࠨᓁ"), None)
    if bstack1l1l11ll_opy_ == bstack1ll_opy_ (u"ࠨࡖࡨࡷࡹࡘࡵ࡯ࡕࡷࡥࡷࡺࡥࡥࠩᓂ") and driver:
        bstack11l11ll1l1_opy_[bstack1ll_opy_ (u"ࠩ࡬ࡲࡹ࡫ࡧࡳࡣࡷ࡭ࡴࡴࡳࠨᓃ")] = bstack11l1l1l1_opy_.bstack111llllll1_opy_(driver)
    if bstack1l1l11ll_opy_ == bstack1ll_opy_ (u"ࠪࡘࡪࡹࡴࡓࡷࡱࡗࡰ࡯ࡰࡱࡧࡧࠫᓄ"):
        bstack1l1l11ll_opy_ = bstack1ll_opy_ (u"࡙ࠫ࡫ࡳࡵࡔࡸࡲࡋ࡯࡮ࡪࡵ࡫ࡩࡩ࠭ᓅ")
    bstack111llll11l_opy_ = {
        bstack1ll_opy_ (u"ࠬ࡫ࡶࡦࡰࡷࡣࡹࡿࡰࡦࠩᓆ"): bstack1l1l11ll_opy_,
        bstack1ll_opy_ (u"࠭ࡴࡦࡵࡷࡣࡷࡻ࡮ࠨᓇ"): bstack11l11ll1l1_opy_
    }
    bstack11l1l1l1_opy_.bstack111ll1l1ll_opy_(bstack111llll11l_opy_)
def bstack111l1ll11l_opy_(test, bstack111ll11l11_opy_, bstack1l1l11ll_opy_, result=None, call=None, outcome=None, bstack111l111lll_opy_=None):
    hook_data = bstack111l1l111l_opy_(test, bstack111ll11l11_opy_, bstack1l1l11ll_opy_, result, call, outcome, bstack111l111lll_opy_)
    bstack111llll11l_opy_ = {
        bstack1ll_opy_ (u"ࠧࡦࡸࡨࡲࡹࡥࡴࡺࡲࡨࠫᓈ"): bstack1l1l11ll_opy_,
        bstack1ll_opy_ (u"ࠨࡪࡲࡳࡰࡥࡲࡶࡰࠪᓉ"): hook_data
    }
    bstack11l1l1l1_opy_.bstack111ll1l1ll_opy_(bstack111llll11l_opy_)
def bstack111l1l1ll1_opy_(bstack111ll11l11_opy_):
    if not bstack111ll11l11_opy_:
        return None
    if bstack111ll11l11_opy_.get(bstack1ll_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡥࡣࡷࡥࠬᓊ"), None):
        return getattr(bstack111ll11l11_opy_[bstack1ll_opy_ (u"ࠪࡸࡪࡹࡴࡠࡦࡤࡸࡦ࠭ᓋ")], bstack1ll_opy_ (u"ࠫࡺࡻࡩࡥࠩᓌ"), None)
    return bstack111ll11l11_opy_.get(bstack1ll_opy_ (u"ࠬࡻࡵࡪࡦࠪᓍ"), None)
@pytest.fixture(autouse=True)
def second_fixture(caplog, request):
    yield
    try:
        if not bstack11l1l1l1_opy_.on():
            return
        places = [bstack1ll_opy_ (u"࠭ࡳࡦࡶࡸࡴࠬᓎ"), bstack1ll_opy_ (u"ࠧࡤࡣ࡯ࡰࠬᓏ"), bstack1ll_opy_ (u"ࠨࡶࡨࡥࡷࡪ࡯ࡸࡰࠪᓐ")]
        bstack111lllll11_opy_ = []
        for bstack111l1ll1l1_opy_ in places:
            records = caplog.get_records(bstack111l1ll1l1_opy_)
            bstack111l111l1l_opy_ = bstack1ll_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩᓑ") if bstack111l1ll1l1_opy_ == bstack1ll_opy_ (u"ࠪࡧࡦࡲ࡬ࠨᓒ") else bstack1ll_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫᓓ")
            bstack111ll111ll_opy_ = request.node.nodeid + (bstack1ll_opy_ (u"ࠬ࠭ᓔ") if bstack111l1ll1l1_opy_ == bstack1ll_opy_ (u"࠭ࡣࡢ࡮࡯ࠫᓕ") else bstack1ll_opy_ (u"ࠧ࠮ࠩᓖ") + bstack111l1ll1l1_opy_)
            bstack111l11lll1_opy_ = bstack111l1l1ll1_opy_(_111l111l11_opy_.get(bstack111ll111ll_opy_, None))
            if not bstack111l11lll1_opy_:
                continue
            for record in records:
                if bstack1l11ll111l_opy_(record.message):
                    continue
                bstack111lllll11_opy_.append({
                    bstack1ll_opy_ (u"ࠨࡶ࡬ࡱࡪࡹࡴࡢ࡯ࡳࠫᓗ"): datetime.datetime.utcfromtimestamp(record.created).isoformat() + bstack1ll_opy_ (u"ࠩ࡝ࠫᓘ"),
                    bstack1ll_opy_ (u"ࠪࡰࡪࡼࡥ࡭ࠩᓙ"): record.levelname,
                    bstack1ll_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬᓚ"): record.message,
                    bstack111l111l1l_opy_: bstack111l11lll1_opy_
                })
        if len(bstack111lllll11_opy_) > 0:
            bstack11l1l1l1_opy_.bstack11l1111l1l_opy_(bstack111lllll11_opy_)
    except Exception as err:
        print(bstack1ll_opy_ (u"ࠬࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤࡸ࡫ࡣࡰࡰࡧࡣ࡫࡯ࡸࡵࡷࡵࡩ࠿ࠦࡻࡾࠩᓛ"), str(err))
def bstack111l1l1lll_opy_(driver_command, response):
    if driver_command == bstack1ll_opy_ (u"࠭ࡳࡤࡴࡨࡩࡳࡹࡨࡰࡶࠪᓜ"):
        bstack11l1l1l1_opy_.bstack11l11111ll_opy_({
            bstack1ll_opy_ (u"ࠧࡪ࡯ࡤ࡫ࡪ࠭ᓝ"): response[bstack1ll_opy_ (u"ࠨࡸࡤࡰࡺ࡫ࠧᓞ")],
            bstack1ll_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩᓟ"): store[bstack1ll_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣࡹ࡫ࡳࡵࡡࡸࡹ࡮ࡪࠧᓠ")]
        })
def bstack1ll1l1ll1l_opy_():
    global bstack11l1l1l1l_opy_
    bstack11l1l1l1_opy_.bstack11l1111l11_opy_()
    for driver in bstack11l1l1l1l_opy_:
        try:
            driver.quit()
        except Exception as e:
            pass
def bstack11111ll1_opy_(self, *args, **kwargs):
    bstack1lll1111ll_opy_ = bstack11ll11ll1_opy_(self, *args, **kwargs)
    bstack11l1l1l1_opy_.bstack1l11ll111_opy_(self)
    return bstack1lll1111ll_opy_
def bstack1ll111ll11_opy_(framework_name):
    global bstack1lll11l11l_opy_
    global bstack11lll1lll_opy_
    bstack1lll11l11l_opy_ = framework_name
    logger.info(bstack1ll1111lll_opy_.format(bstack1lll11l11l_opy_.split(bstack1ll_opy_ (u"ࠫ࠲࠭ᓡ"))[0]))
    try:
        from selenium import webdriver
        from selenium.webdriver.common.service import Service
        from selenium.webdriver.remote.webdriver import WebDriver
        if bstack1l11l1ll11_opy_():
            Service.start = bstack1lll1l11l1_opy_
            Service.stop = bstack1ll11lll11_opy_
            webdriver.Remote.__init__ = bstack1lllll11l_opy_
            webdriver.Remote.get = bstack111l1ll11_opy_
            if not isinstance(os.getenv(bstack1ll_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡕ࡟ࡔࡆࡕࡗࡣࡕࡇࡒࡂࡎࡏࡉࡑ࠭ᓢ")), str):
                return
            WebDriver.close = bstack11ll11111_opy_
            WebDriver.quit = bstack1lll1lll1_opy_
            WebDriver.getAccessibilityResults = getAccessibilityResults
            WebDriver.getAccessibilityResultsSummary = getAccessibilityResultsSummary
        if not bstack1l11l1ll11_opy_() and bstack11l1l1l1_opy_.on():
            webdriver.Remote.__init__ = bstack11111ll1_opy_
        bstack11lll1lll_opy_ = True
    except Exception as e:
        pass
    bstack1lllll111l_opy_()
    if os.environ.get(bstack1ll_opy_ (u"࠭ࡓࡆࡎࡈࡒࡎ࡛ࡍࡠࡑࡕࡣࡕࡒࡁ࡚࡙ࡕࡍࡌࡎࡔࡠࡋࡑࡗ࡙ࡇࡌࡍࡇࡇࠫᓣ")):
        bstack11lll1lll_opy_ = eval(os.environ.get(bstack1ll_opy_ (u"ࠧࡔࡇࡏࡉࡓࡏࡕࡎࡡࡒࡖࡤࡖࡌࡂ࡛࡚ࡖࡎࡍࡈࡕࡡࡌࡒࡘ࡚ࡁࡍࡎࡈࡈࠬᓤ")))
    if not bstack11lll1lll_opy_:
        bstack11111l1l_opy_(bstack1ll_opy_ (u"ࠣࡒࡤࡧࡰࡧࡧࡦࡵࠣࡲࡴࡺࠠࡪࡰࡶࡸࡦࡲ࡬ࡦࡦࠥᓥ"), bstack1l1l1ll1l_opy_)
    if bstack111l1l1l1_opy_():
        try:
            from selenium.webdriver.remote.remote_connection import RemoteConnection
            RemoteConnection._get_proxy_url = bstack1l1lll11_opy_
        except Exception as e:
            logger.error(bstack111l1llll_opy_.format(str(e)))
    if bstack1ll_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࠩᓦ") in str(framework_name).lower():
        if not bstack1l11l1ll11_opy_():
            return
        try:
            from pytest_selenium import pytest_selenium
            from _pytest.config import Config
            pytest_selenium.pytest_report_header = bstack111ll111_opy_
            from pytest_selenium.drivers import browserstack
            browserstack.pytest_selenium_runtest_makereport = bstack11111llll_opy_
            Config.getoption = bstack1ll11l111_opy_
        except Exception as e:
            pass
        try:
            from pytest_bdd import reporting
            reporting.runtest_makereport = bstack1l11111l_opy_
        except Exception as e:
            pass
def bstack1lll1lll1_opy_(self):
    global bstack1lll11l11l_opy_
    global bstack1ll11l1ll_opy_
    global bstack111ll1ll_opy_
    try:
        if bstack1ll_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࠪᓧ") in bstack1lll11l11l_opy_ and self.session_id != None and bstack1llll11l_opy_(threading.current_thread(), bstack1ll_opy_ (u"ࠫࡹ࡫ࡳࡵࡕࡷࡥࡹࡻࡳࠨᓨ"), bstack1ll_opy_ (u"ࠬ࠭ᓩ")) != bstack1ll_opy_ (u"࠭ࡳ࡬࡫ࡳࡴࡪࡪࠧᓪ"):
            bstack1ll1l1lll_opy_ = bstack1ll_opy_ (u"ࠧࡱࡣࡶࡷࡪࡪࠧᓫ") if len(threading.current_thread().bstackTestErrorMessages) == 0 else bstack1ll_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨᓬ")
            bstack11ll11l1l_opy_ = bstack11ll1111_opy_(bstack1ll_opy_ (u"ࠩࡶࡩࡹ࡙ࡥࡴࡵ࡬ࡳࡳ࡙ࡴࡢࡶࡸࡷࠬᓭ"), bstack1ll_opy_ (u"ࠪࠫᓮ"), bstack1ll1l1lll_opy_, bstack1ll_opy_ (u"ࠫ࠱ࠦࠧᓯ").join(
                threading.current_thread().bstackTestErrorMessages), bstack1ll_opy_ (u"ࠬ࠭ᓰ"), bstack1ll_opy_ (u"࠭ࠧᓱ"))
            bstack1ll11ll11_opy_(logger, True)
            if self != None:
                self.execute_script(bstack11ll11l1l_opy_)
    except Exception as e:
        logger.debug(bstack1ll_opy_ (u"ࠢࡆࡴࡵࡳࡷࠦࡷࡩ࡫࡯ࡩࠥࡳࡡࡳ࡭࡬ࡲ࡬ࠦࡳࡵࡣࡷࡹࡸࡀࠠࠣᓲ") + str(e))
    bstack111ll1ll_opy_(self)
    self.session_id = None
def bstack1lllll11l_opy_(self, command_executor,
             desired_capabilities=None, browser_profile=None, proxy=None,
             keep_alive=True, file_detector=None, options=None):
    global CONFIG
    global bstack1ll11l1ll_opy_
    global bstack1lll1l111l_opy_
    global bstack111111ll_opy_
    global bstack1lll11l11l_opy_
    global bstack11ll11ll1_opy_
    global bstack11l1l1l1l_opy_
    global bstack1l111l111_opy_
    global bstack1l1111ll_opy_
    global bstack111l1lllll_opy_
    CONFIG[bstack1ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡓࡅࡍࠪᓳ")] = str(bstack1lll11l11l_opy_) + str(__version__)
    command_executor = bstack1l1l1ll11_opy_(bstack1l111l111_opy_)
    logger.debug(bstack1ll1l111_opy_.format(command_executor))
    proxy = bstack1ll11111l_opy_(CONFIG, proxy)
    bstack1l1l1l1l_opy_ = 0
    try:
        if bstack111111ll_opy_ is True:
            bstack1l1l1l1l_opy_ = int(os.environ.get(bstack1ll_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡒࡏࡅ࡙ࡌࡏࡓࡏࡢࡍࡓࡊࡅ࡙ࠩᓴ")))
    except:
        bstack1l1l1l1l_opy_ = 0
    bstack1l1l1111_opy_ = bstack111l11lll_opy_(CONFIG, bstack1l1l1l1l_opy_)
    logger.debug(bstack11ll1l11_opy_.format(str(bstack1l1l1111_opy_)))
    if bstack1ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࠧᓵ") in CONFIG and CONFIG[bstack1ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࠨᓶ")]:
        bstack1ll1llll11_opy_(bstack1l1l1111_opy_, bstack1l1111ll_opy_)
    if desired_capabilities:
        bstack11l1l1ll1_opy_ = bstack1lll11lll1_opy_(desired_capabilities)
        bstack11l1l1ll1_opy_[bstack1ll_opy_ (u"ࠬࡻࡳࡦ࡙࠶ࡇࠬᓷ")] = bstack111lll111_opy_(CONFIG)
        bstack1111111ll_opy_ = bstack111l11lll_opy_(bstack11l1l1ll1_opy_)
        if bstack1111111ll_opy_:
            bstack1l1l1111_opy_ = update(bstack1111111ll_opy_, bstack1l1l1111_opy_)
        desired_capabilities = None
    if options:
        bstack11l111l11_opy_(options, bstack1l1l1111_opy_)
    if not options:
        options = bstack1111l1l11_opy_(bstack1l1l1111_opy_)
    if bstack1lll1ll1_opy_.bstack11l11lll1_opy_(CONFIG, bstack1l1l1l1l_opy_) and bstack1lll1ll1_opy_.bstack111l11l11_opy_(bstack1l1l1111_opy_, options):
        bstack111l1lllll_opy_ = True
        bstack1lll1ll1_opy_.set_capabilities(bstack1l1l1111_opy_, CONFIG)
    if proxy and bstack1l1lllllll_opy_() >= version.parse(bstack1ll_opy_ (u"࠭࠴࠯࠳࠳࠲࠵࠭ᓸ")):
        options.proxy(proxy)
    if options and bstack1l1lllllll_opy_() >= version.parse(bstack1ll_opy_ (u"ࠧ࠴࠰࠻࠲࠵࠭ᓹ")):
        desired_capabilities = None
    if (
            not options and not desired_capabilities
    ) or (
            bstack1l1lllllll_opy_() < version.parse(bstack1ll_opy_ (u"ࠨ࠵࠱࠼࠳࠶ࠧᓺ")) and not desired_capabilities
    ):
        desired_capabilities = {}
        desired_capabilities.update(bstack1l1l1111_opy_)
    logger.info(bstack1lll1l1l_opy_)
    if bstack1l1lllllll_opy_() >= version.parse(bstack1ll_opy_ (u"ࠩ࠷࠲࠶࠶࠮࠱ࠩᓻ")):
        bstack11ll11ll1_opy_(self, command_executor=command_executor,
                  options=options, keep_alive=keep_alive, file_detector=file_detector)
    elif bstack1l1lllllll_opy_() >= version.parse(bstack1ll_opy_ (u"ࠪ࠷࠳࠾࠮࠱ࠩᓼ")):
        bstack11ll11ll1_opy_(self, command_executor=command_executor,
                  desired_capabilities=desired_capabilities, options=options,
                  browser_profile=browser_profile, proxy=proxy,
                  keep_alive=keep_alive, file_detector=file_detector)
    elif bstack1l1lllllll_opy_() >= version.parse(bstack1ll_opy_ (u"ࠫ࠷࠴࠵࠴࠰࠳ࠫᓽ")):
        bstack11ll11ll1_opy_(self, command_executor=command_executor,
                  desired_capabilities=desired_capabilities,
                  browser_profile=browser_profile, proxy=proxy,
                  keep_alive=keep_alive, file_detector=file_detector)
    else:
        bstack11ll11ll1_opy_(self, command_executor=command_executor,
                  desired_capabilities=desired_capabilities,
                  browser_profile=browser_profile, proxy=proxy,
                  keep_alive=keep_alive)
    try:
        bstack111l111l1_opy_ = bstack1ll_opy_ (u"ࠬ࠭ᓾ")
        if bstack1l1lllllll_opy_() >= version.parse(bstack1ll_opy_ (u"࠭࠴࠯࠲࠱࠴ࡧ࠷ࠧᓿ")):
            bstack111l111l1_opy_ = self.caps.get(bstack1ll_opy_ (u"ࠢࡰࡲࡷ࡭ࡲࡧ࡬ࡉࡷࡥ࡙ࡷࡲࠢᔀ"))
        else:
            bstack111l111l1_opy_ = self.capabilities.get(bstack1ll_opy_ (u"ࠣࡱࡳࡸ࡮ࡳࡡ࡭ࡊࡸࡦ࡚ࡸ࡬ࠣᔁ"))
        if bstack111l111l1_opy_:
            bstack1lll11l1_opy_(bstack111l111l1_opy_)
            if bstack1l1lllllll_opy_() <= version.parse(bstack1ll_opy_ (u"ࠩ࠶࠲࠶࠹࠮࠱ࠩᔂ")):
                self.command_executor._url = bstack1ll_opy_ (u"ࠥ࡬ࡹࡺࡰ࠻࠱࠲ࠦᔃ") + bstack1l111l111_opy_ + bstack1ll_opy_ (u"ࠦ࠿࠾࠰࠰ࡹࡧ࠳࡭ࡻࡢࠣᔄ")
            else:
                self.command_executor._url = bstack1ll_opy_ (u"ࠧ࡮ࡴࡵࡲࡶ࠾࠴࠵ࠢᔅ") + bstack111l111l1_opy_ + bstack1ll_opy_ (u"ࠨ࠯ࡸࡦ࠲࡬ࡺࡨࠢᔆ")
            logger.debug(bstack1l11l111l_opy_.format(bstack111l111l1_opy_))
        else:
            logger.debug(bstack1111ll111_opy_.format(bstack1ll_opy_ (u"ࠢࡐࡲࡷ࡭ࡲࡧ࡬ࠡࡊࡸࡦࠥࡴ࡯ࡵࠢࡩࡳࡺࡴࡤࠣᔇ")))
    except Exception as e:
        logger.debug(bstack1111ll111_opy_.format(e))
    bstack1ll11l1ll_opy_ = self.session_id
    if bstack1ll_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࠨᔈ") in bstack1lll11l11l_opy_:
        threading.current_thread().bstack111ll11l1_opy_ = self.session_id
        threading.current_thread().bstackSessionDriver = self
        threading.current_thread().bstackTestErrorMessages = []
        bstack11l1l1l1_opy_.bstack1l11ll111_opy_(self)
    bstack11l1l1l1l_opy_.append(self)
    if bstack1ll_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬᔉ") in CONFIG and bstack1ll_opy_ (u"ࠪࡷࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠨᔊ") in CONFIG[bstack1ll_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧᔋ")][bstack1l1l1l1l_opy_]:
        bstack1lll1l111l_opy_ = CONFIG[bstack1ll_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨᔌ")][bstack1l1l1l1l_opy_][bstack1ll_opy_ (u"࠭ࡳࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠫᔍ")]
    logger.debug(bstack1llll11ll1_opy_.format(bstack1ll11l1ll_opy_))
def bstack111l1ll11_opy_(self, url):
    global bstack1l1111lll_opy_
    global CONFIG
    try:
        bstack1llllll1l1_opy_(url, CONFIG, logger)
    except Exception as err:
        logger.debug(bstack11ll1l1l1_opy_.format(str(err)))
    try:
        bstack1l1111lll_opy_(self, url)
    except Exception as e:
        try:
            bstack11111lll_opy_ = str(e)
            if any(err_msg in bstack11111lll_opy_ for err_msg in bstack1111ll1ll_opy_):
                bstack1llllll1l1_opy_(url, CONFIG, logger, True)
        except Exception as err:
            logger.debug(bstack11ll1l1l1_opy_.format(str(err)))
        raise e
def bstack1ll11llll1_opy_(item, when):
    global bstack11l111lll_opy_
    try:
        bstack11l111lll_opy_(item, when)
    except Exception as e:
        pass
def bstack1l11111l_opy_(item, call, rep):
    global bstack11111111l_opy_
    global bstack11l1l1l1l_opy_
    name = bstack1ll_opy_ (u"ࠧࠨᔎ")
    try:
        if rep.when == bstack1ll_opy_ (u"ࠨࡥࡤࡰࡱ࠭ᔏ"):
            bstack1ll11l1ll_opy_ = threading.current_thread().bstack111ll11l1_opy_
            bstack111l1l11l1_opy_ = item.config.getoption(bstack1ll_opy_ (u"ࠩࡶ࡯࡮ࡶࡓࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠫᔐ"))
            try:
                if (str(bstack111l1l11l1_opy_).lower() != bstack1ll_opy_ (u"ࠪࡸࡷࡻࡥࠨᔑ")):
                    name = str(rep.nodeid)
                    bstack11ll11l1l_opy_ = bstack11ll1111_opy_(bstack1ll_opy_ (u"ࠫࡸ࡫ࡴࡔࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠬᔒ"), name, bstack1ll_opy_ (u"ࠬ࠭ᔓ"), bstack1ll_opy_ (u"࠭ࠧᔔ"), bstack1ll_opy_ (u"ࠧࠨᔕ"), bstack1ll_opy_ (u"ࠨࠩᔖ"))
                    os.environ[bstack1ll_opy_ (u"ࠩࡓ࡝࡙ࡋࡓࡕࡡࡗࡉࡘ࡚࡟ࡏࡃࡐࡉࠬᔗ")] = name
                    for driver in bstack11l1l1l1l_opy_:
                        if bstack1ll11l1ll_opy_ == driver.session_id:
                            driver.execute_script(bstack11ll11l1l_opy_)
            except Exception as e:
                logger.debug(bstack1ll_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥࡹࡥࡵࡶ࡬ࡲ࡬ࠦࡳࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠤ࡫ࡵࡲࠡࡲࡼࡸࡪࡹࡴ࠮ࡤࡧࡨࠥࡹࡥࡴࡵ࡬ࡳࡳࡀࠠࡼࡿࠪᔘ").format(str(e)))
            try:
                bstack1ll11l11_opy_(rep.outcome.lower())
                if rep.outcome.lower() != bstack1ll_opy_ (u"ࠫࡸࡱࡩࡱࡲࡨࡨࠬᔙ"):
                    status = bstack1ll_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬᔚ") if rep.outcome.lower() == bstack1ll_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭ᔛ") else bstack1ll_opy_ (u"ࠧࡱࡣࡶࡷࡪࡪࠧᔜ")
                    reason = bstack1ll_opy_ (u"ࠨࠩᔝ")
                    if status == bstack1ll_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩᔞ"):
                        reason = rep.longrepr.reprcrash.message
                        if (not threading.current_thread().bstackTestErrorMessages):
                            threading.current_thread().bstackTestErrorMessages = []
                        threading.current_thread().bstackTestErrorMessages.append(reason)
                    level = bstack1ll_opy_ (u"ࠪ࡭ࡳ࡬࡯ࠨᔟ") if status == bstack1ll_opy_ (u"ࠫࡵࡧࡳࡴࡧࡧࠫᔠ") else bstack1ll_opy_ (u"ࠬ࡫ࡲࡳࡱࡵࠫᔡ")
                    data = name + bstack1ll_opy_ (u"࠭ࠠࡱࡣࡶࡷࡪࡪࠡࠨᔢ") if status == bstack1ll_opy_ (u"ࠧࡱࡣࡶࡷࡪࡪࠧᔣ") else name + bstack1ll_opy_ (u"ࠨࠢࡩࡥ࡮ࡲࡥࡥࠣࠣࠫᔤ") + reason
                    bstack1l11l1lll_opy_ = bstack11ll1111_opy_(bstack1ll_opy_ (u"ࠩࡤࡲࡳࡵࡴࡢࡶࡨࠫᔥ"), bstack1ll_opy_ (u"ࠪࠫᔦ"), bstack1ll_opy_ (u"ࠫࠬᔧ"), bstack1ll_opy_ (u"ࠬ࠭ᔨ"), level, data)
                    for driver in bstack11l1l1l1l_opy_:
                        if bstack1ll11l1ll_opy_ == driver.session_id:
                            driver.execute_script(bstack1l11l1lll_opy_)
            except Exception as e:
                logger.debug(bstack1ll_opy_ (u"࠭ࡅࡳࡴࡲࡶࠥ࡯࡮ࠡࡵࡨࡸࡹ࡯࡮ࡨࠢࡶࡩࡸࡹࡩࡰࡰࠣࡧࡴࡴࡴࡦࡺࡷࠤ࡫ࡵࡲࠡࡲࡼࡸࡪࡹࡴ࠮ࡤࡧࡨࠥࡹࡥࡴࡵ࡬ࡳࡳࡀࠠࡼࡿࠪᔩ").format(str(e)))
    except Exception as e:
        logger.debug(bstack1ll_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡪࡩࡹࡺࡩ࡯ࡩࠣࡷࡹࡧࡴࡦࠢ࡬ࡲࠥࡶࡹࡵࡧࡶࡸ࠲ࡨࡤࡥࠢࡷࡩࡸࡺࠠࡴࡶࡤࡸࡺࡹ࠺ࠡࡽࢀࠫᔪ").format(str(e)))
    bstack11111111l_opy_(item, call, rep)
notset = Notset()
def bstack1ll11l111_opy_(self, name: str, default=notset, skip: bool = False):
    global bstack1llllll111_opy_
    if str(name).lower() == bstack1ll_opy_ (u"ࠨࡦࡵ࡭ࡻ࡫ࡲࠨᔫ"):
        return bstack1ll_opy_ (u"ࠤࡅࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࠣᔬ")
    else:
        return bstack1llllll111_opy_(self, name, default, skip)
def bstack1l1lll11_opy_(self):
    global CONFIG
    global bstack1ll1111l1_opy_
    try:
        proxy = bstack1l111ll11_opy_(CONFIG)
        if proxy:
            if proxy.endswith(bstack1ll_opy_ (u"ࠪ࠲ࡵࡧࡣࠨᔭ")):
                proxies = bstack11llllll_opy_(proxy, bstack1l1l1ll11_opy_())
                if len(proxies) > 0:
                    protocol, bstack1l1llll11_opy_ = proxies.popitem()
                    if bstack1ll_opy_ (u"ࠦ࠿࠵࠯ࠣᔮ") in bstack1l1llll11_opy_:
                        return bstack1l1llll11_opy_
                    else:
                        return bstack1ll_opy_ (u"ࠧ࡮ࡴࡵࡲ࠽࠳࠴ࠨᔯ") + bstack1l1llll11_opy_
            else:
                return proxy
    except Exception as e:
        logger.error(bstack1ll_opy_ (u"ࠨࡅࡳࡴࡲࡶࠥ࡯࡮ࠡࡵࡨࡸࡹ࡯࡮ࡨࠢࡳࡶࡴࡾࡹࠡࡷࡵࡰࠥࡀࠠࡼࡿࠥᔰ").format(str(e)))
    return bstack1ll1111l1_opy_(self)
def bstack111l1l1l1_opy_():
    return (bstack1ll_opy_ (u"ࠧࡩࡶࡷࡴࡕࡸ࡯ࡹࡻࠪᔱ") in CONFIG or bstack1ll_opy_ (u"ࠨࡪࡷࡸࡵࡹࡐࡳࡱࡻࡽࠬᔲ") in CONFIG) and bstack111ll111l_opy_() and bstack1l1lllllll_opy_() >= version.parse(
        bstack11l1111l_opy_)
def bstack1l11llll_opy_(self,
               executablePath=None,
               channel=None,
               args=None,
               ignoreDefaultArgs=None,
               handleSIGINT=None,
               handleSIGTERM=None,
               handleSIGHUP=None,
               timeout=None,
               env=None,
               headless=None,
               devtools=None,
               proxy=None,
               downloadsPath=None,
               slowMo=None,
               tracesDir=None,
               chromiumSandbox=None,
               firefoxUserPrefs=None
               ):
    global CONFIG
    global bstack1lll1l111l_opy_
    global bstack111111ll_opy_
    global bstack1lll11l11l_opy_
    CONFIG[bstack1ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡔࡆࡎࠫᔳ")] = str(bstack1lll11l11l_opy_) + str(__version__)
    bstack1l1l1l1l_opy_ = 0
    try:
        if bstack111111ll_opy_ is True:
            bstack1l1l1l1l_opy_ = int(os.environ.get(bstack1ll_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡓࡐࡆ࡚ࡆࡐࡔࡐࡣࡎࡔࡄࡆ࡚ࠪᔴ")))
    except:
        bstack1l1l1l1l_opy_ = 0
    CONFIG[bstack1ll_opy_ (u"ࠦ࡮ࡹࡐ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࠥᔵ")] = True
    bstack1l1l1111_opy_ = bstack111l11lll_opy_(CONFIG, bstack1l1l1l1l_opy_)
    logger.debug(bstack11ll1l11_opy_.format(str(bstack1l1l1111_opy_)))
    if CONFIG.get(bstack1ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࠩᔶ")):
        bstack1ll1llll11_opy_(bstack1l1l1111_opy_, bstack1l1111ll_opy_)
    if bstack1ll_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩᔷ") in CONFIG and bstack1ll_opy_ (u"ࠧࡴࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠬᔸ") in CONFIG[bstack1ll_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫᔹ")][bstack1l1l1l1l_opy_]:
        bstack1lll1l111l_opy_ = CONFIG[bstack1ll_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬᔺ")][bstack1l1l1l1l_opy_][bstack1ll_opy_ (u"ࠪࡷࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠨᔻ")]
    import urllib
    import json
    bstack1ll11ll1_opy_ = bstack1ll_opy_ (u"ࠫࡼࡹࡳ࠻࠱࠲ࡧࡩࡶ࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡣࡰ࡯࠲ࡴࡱࡧࡹࡸࡴ࡬࡫࡭ࡺ࠿ࡤࡣࡳࡷࡂ࠭ᔼ") + urllib.parse.quote(json.dumps(bstack1l1l1111_opy_))
    browser = self.connect(bstack1ll11ll1_opy_)
    return browser
def bstack1lllll111l_opy_():
    global bstack11lll1lll_opy_
    try:
        from playwright._impl._browser_type import BrowserType
        BrowserType.launch = bstack1l11llll_opy_
        bstack11lll1lll_opy_ = True
    except Exception as e:
        pass
def bstack111ll11ll1_opy_():
    global CONFIG
    global bstack1l11l11ll_opy_
    global bstack1l111l111_opy_
    global bstack1l1111ll_opy_
    global bstack111111ll_opy_
    CONFIG = json.loads(os.environ.get(bstack1ll_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡈࡕࡎࡇࡋࡊࠫᔽ")))
    bstack1l11l11ll_opy_ = eval(os.environ.get(bstack1ll_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡏࡓࡠࡃࡓࡔࡤࡇࡕࡕࡑࡐࡅ࡙ࡋࠧᔾ")))
    bstack1l111l111_opy_ = os.environ.get(bstack1ll_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡈࡖࡄࡢ࡙ࡗࡒࠧᔿ"))
    bstack11ll1ll1l_opy_(CONFIG, bstack1l11l11ll_opy_)
    bstack1llll11l11_opy_()
    global bstack11ll11ll1_opy_
    global bstack111ll1ll_opy_
    global bstack1lll1l1ll1_opy_
    global bstack1lll111l1_opy_
    global bstack11lll11ll_opy_
    global bstack1ll111l11l_opy_
    global bstack1l1l11ll1_opy_
    global bstack1l1111lll_opy_
    global bstack1ll1111l1_opy_
    global bstack1llllll111_opy_
    global bstack11l111lll_opy_
    global bstack11111111l_opy_
    try:
        from selenium import webdriver
        from selenium.webdriver.remote.webdriver import WebDriver
        bstack11ll11ll1_opy_ = webdriver.Remote.__init__
        bstack111ll1ll_opy_ = WebDriver.quit
        bstack1l1l11ll1_opy_ = WebDriver.close
        bstack1l1111lll_opy_ = WebDriver.get
    except Exception as e:
        pass
    if (bstack1ll_opy_ (u"ࠨࡪࡷࡸࡵࡖࡲࡰࡺࡼࠫᕀ") in CONFIG or bstack1ll_opy_ (u"ࠩ࡫ࡸࡹࡶࡳࡑࡴࡲࡼࡾ࠭ᕁ") in CONFIG) and bstack111ll111l_opy_():
        if bstack1l1lllllll_opy_() < version.parse(bstack11l1111l_opy_):
            logger.error(bstack11ll1111l_opy_.format(bstack1l1lllllll_opy_()))
        else:
            try:
                from selenium.webdriver.remote.remote_connection import RemoteConnection
                bstack1ll1111l1_opy_ = RemoteConnection._get_proxy_url
            except Exception as e:
                logger.error(bstack111l1llll_opy_.format(str(e)))
    try:
        from _pytest.config import Config
        bstack1llllll111_opy_ = Config.getoption
        from _pytest import runner
        bstack11l111lll_opy_ = runner._update_current_test_var
    except Exception as e:
        logger.warn(e, bstack1ll1lll1_opy_)
    try:
        from pytest_bdd import reporting
        bstack11111111l_opy_ = reporting.runtest_makereport
    except Exception as e:
        logger.debug(bstack1ll_opy_ (u"ࠪࡔࡱ࡫ࡡࡴࡧࠣ࡭ࡳࡹࡴࡢ࡮࡯ࠤࡵࡿࡴࡦࡵࡷ࠱ࡧࡪࡤࠡࡶࡲࠤࡷࡻ࡮ࠡࡲࡼࡸࡪࡹࡴ࠮ࡤࡧࡨࠥࡺࡥࡴࡶࡶࠫᕂ"))
    bstack1l1111ll_opy_ = CONFIG.get(bstack1ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨᕃ"), {}).get(bstack1ll_opy_ (u"ࠬࡲ࡯ࡤࡣ࡯ࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧᕄ"))
    bstack111111ll_opy_ = True
    bstack1ll111ll11_opy_(bstack111ll11l_opy_)
if (bstack1l11llll1l_opy_()):
    bstack111ll11ll1_opy_()
@bstack1l1lll1111_opy_(class_method=False)
def bstack111l11ll11_opy_(hook_name, event, bstack111ll1l111_opy_=None):
    if hook_name not in [bstack1ll_opy_ (u"࠭ࡳࡦࡶࡸࡴࡤ࡬ࡵ࡯ࡥࡷ࡭ࡴࡴࠧᕅ"), bstack1ll_opy_ (u"ࠧࡵࡧࡤࡶࡩࡵࡷ࡯ࡡࡩࡹࡳࡩࡴࡪࡱࡱࠫᕆ"), bstack1ll_opy_ (u"ࠨࡵࡨࡸࡺࡶ࡟࡮ࡱࡧࡹࡱ࡫ࠧᕇ"), bstack1ll_opy_ (u"ࠩࡷࡩࡦࡸࡤࡰࡹࡱࡣࡲࡵࡤࡶ࡮ࡨࠫᕈ"), bstack1ll_opy_ (u"ࠪࡷࡪࡺࡵࡱࡡࡦࡰࡦࡹࡳࠨᕉ"), bstack1ll_opy_ (u"ࠫࡹ࡫ࡡࡳࡦࡲࡻࡳࡥࡣ࡭ࡣࡶࡷࠬᕊ"), bstack1ll_opy_ (u"ࠬࡹࡥࡵࡷࡳࡣࡲ࡫ࡴࡩࡱࡧࠫᕋ"), bstack1ll_opy_ (u"࠭ࡴࡦࡣࡵࡨࡴࡽ࡮ࡠ࡯ࡨࡸ࡭ࡵࡤࠨᕌ")]:
        return
    node = store[bstack1ll_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡶࡨࡷࡹࡥࡩࡵࡧࡰࠫᕍ")]
    if hook_name in [bstack1ll_opy_ (u"ࠨࡵࡨࡸࡺࡶ࡟࡮ࡱࡧࡹࡱ࡫ࠧᕎ"), bstack1ll_opy_ (u"ࠩࡷࡩࡦࡸࡤࡰࡹࡱࡣࡲࡵࡤࡶ࡮ࡨࠫᕏ")]:
        node = store[bstack1ll_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣࡲࡵࡤࡶ࡮ࡨࡣ࡮ࡺࡥ࡮ࠩᕐ")]
    elif hook_name in [bstack1ll_opy_ (u"ࠫࡸ࡫ࡴࡶࡲࡢࡧࡱࡧࡳࡴࠩᕑ"), bstack1ll_opy_ (u"ࠬࡺࡥࡢࡴࡧࡳࡼࡴ࡟ࡤ࡮ࡤࡷࡸ࠭ᕒ")]:
        node = store[bstack1ll_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡤ࡮ࡤࡷࡸࡥࡩࡵࡧࡰࠫᕓ")]
    if event == bstack1ll_opy_ (u"ࠧࡣࡧࡩࡳࡷ࡫ࠧᕔ"):
        hook_type = bstack11l1lll1ll_opy_(hook_name)
        uuid = uuid4().__str__()
        bstack111l1l1l1l_opy_ = {
            bstack1ll_opy_ (u"ࠨࡷࡸ࡭ࡩ࠭ᕕ"): uuid,
            bstack1ll_opy_ (u"ࠩࡶࡸࡦࡸࡴࡦࡦࡢࡥࡹ࠭ᕖ"): bstack1lllll1ll1_opy_(),
            bstack1ll_opy_ (u"ࠪࡸࡾࡶࡥࠨᕗ"): bstack1ll_opy_ (u"ࠫ࡭ࡵ࡯࡬ࠩᕘ"),
            bstack1ll_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡢࡸࡾࡶࡥࠨᕙ"): hook_type,
            bstack1ll_opy_ (u"࠭ࡨࡰࡱ࡮ࡣࡳࡧ࡭ࡦࠩᕚ"): hook_name
        }
        store[bstack1ll_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡪࡲࡳࡰࡥࡵࡶ࡫ࡧࠫᕛ")].append(uuid)
        bstack111l1l1111_opy_ = node.nodeid
        if hook_type == bstack1ll_opy_ (u"ࠨࡄࡈࡊࡔࡘࡅࡠࡇࡄࡇࡍ࠭ᕜ"):
            if not _111l111l11_opy_.get(bstack111l1l1111_opy_, None):
                _111l111l11_opy_[bstack111l1l1111_opy_] = {bstack1ll_opy_ (u"ࠩ࡫ࡳࡴࡱࡳࠨᕝ"): []}
            _111l111l11_opy_[bstack111l1l1111_opy_][bstack1ll_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡴࠩᕞ")].append(bstack111l1l1l1l_opy_[bstack1ll_opy_ (u"ࠫࡺࡻࡩࡥࠩᕟ")])
        _111l111l11_opy_[bstack111l1l1111_opy_ + bstack1ll_opy_ (u"ࠬ࠳ࠧᕠ") + hook_name] = bstack111l1l1l1l_opy_
        bstack111l1ll11l_opy_(node, bstack111l1l1l1l_opy_, bstack1ll_opy_ (u"࠭ࡈࡰࡱ࡮ࡖࡺࡴࡓࡵࡣࡵࡸࡪࡪࠧᕡ"))
    elif event == bstack1ll_opy_ (u"ࠧࡢࡨࡷࡩࡷ࠭ᕢ"):
        bstack111l1lll1l_opy_ = node.nodeid + bstack1ll_opy_ (u"ࠨ࠯ࠪᕣ") + hook_name
        _111l111l11_opy_[bstack111l1lll1l_opy_][bstack1ll_opy_ (u"ࠩࡩ࡭ࡳ࡯ࡳࡩࡧࡧࡣࡦࡺࠧᕤ")] = bstack1lllll1ll1_opy_()
        bstack111l1ll1ll_opy_(_111l111l11_opy_[bstack111l1lll1l_opy_][bstack1ll_opy_ (u"ࠪࡹࡺ࡯ࡤࠨᕥ")])
        bstack111l1ll11l_opy_(node, _111l111l11_opy_[bstack111l1lll1l_opy_], bstack1ll_opy_ (u"ࠫࡍࡵ࡯࡬ࡔࡸࡲࡋ࡯࡮ࡪࡵ࡫ࡩࡩ࠭ᕦ"), bstack111l111lll_opy_=bstack111ll1l111_opy_)
def bstack111l11ll1l_opy_():
    global bstack111ll111l1_opy_
    if bstack1ll1ll11l1_opy_():
        bstack111ll111l1_opy_ = bstack1ll_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸ࠲ࡨࡤࡥࠩᕧ")
    else:
        bstack111ll111l1_opy_ = bstack1ll_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭ᕨ")
@bstack11l1l1l1_opy_.bstack11l1111111_opy_
def bstack111l111ll1_opy_():
    bstack111l11ll1l_opy_()
    if bstack111ll111l_opy_():
        bstack11l1l1l1l1_opy_(bstack111l1l1lll_opy_)
    bstack1l1111llll_opy_ = bstack1l111l11ll_opy_(bstack111l11ll11_opy_)
bstack111l111ll1_opy_()