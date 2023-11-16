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
import atexit
import datetime
import inspect
import logging
import os
import sys
import threading
from uuid import uuid4
import pytest
from packaging import version
from browserstack_sdk.__init__ import (bstack1lllllll1l_opy_, bstack1ll1l1111l_opy_, update, bstack1ll11111l_opy_,
                                       bstack1111lllll_opy_, bstack111l11lll_opy_, bstack11l1l11l1_opy_, bstack11l111ll_opy_,
                                       bstack11l1l1ll_opy_, bstack1lll1111_opy_, bstack1l1lll111_opy_, bstack1llll1l11l_opy_,
                                       bstack111l1lll_opy_, getAccessibilityResults, getAccessibilityResultsSummary)
from browserstack_sdk._version import __version__
from bstack_utils.capture import bstack1l1ll11l1l_opy_
from bstack_utils.constants import bstack1lll1ll1_opy_, bstack1llll11111_opy_, bstack1llll11l1l_opy_, bstack1lll1llll1_opy_, \
    bstack11llllll_opy_
from bstack_utils.helper import bstack11l11l11_opy_, bstack1ll11l11l_opy_, bstack1l1l1l11ll_opy_, bstack1111ll111_opy_, bstack1l1l111111_opy_, \
    bstack1l1l11lll1_opy_, bstack1lllll1l1l_opy_, bstack111111111_opy_, bstack1l1l11ll1l_opy_, bstack1lllllllll_opy_, Notset, \
    bstack1111lll1_opy_, bstack1l11lll1l1_opy_, bstack1l11ll1l11_opy_, Result, bstack1l11ll1lll_opy_, bstack1l1l1l11l1_opy_, bstack1l1lll11l1_opy_
from bstack_utils.bstack1l11l11l11_opy_ import bstack1l11l1ll1l_opy_
from bstack_utils.messages import bstack1ll1l11l1_opy_, bstack111l11ll1_opy_, bstack1lll1l1l1_opy_, bstack11ll1l11_opy_, bstack11l11l1ll_opy_, \
    bstack1ll1l1ll1_opy_, bstack1ll1lll1l1_opy_, bstack1ll1ll1l1_opy_, bstack111llll1_opy_, bstack11lll11l_opy_, \
    bstack11111llll_opy_, bstack1l111ll1l_opy_
from bstack_utils.proxy import bstack1l1ll11ll_opy_, bstack1l1l1l111_opy_
from bstack_utils.bstack1ll1l11l11_opy_ import bstack11ll1ll1ll_opy_, bstack11ll1llll1_opy_, bstack11ll1l1111_opy_, bstack11ll1l1l11_opy_, \
    bstack11ll1ll111_opy_, bstack11ll1l1ll1_opy_, bstack11ll1lll1l_opy_, bstack1lll111ll1_opy_, bstack11ll1l11ll_opy_
from bstack_utils.bstack11ll11111l_opy_ import bstack11ll1111l1_opy_
from bstack_utils.bstack11ll1l11l1_opy_ import bstack1l1ll1111_opy_, bstack1ll1l1l111_opy_, bstack11l11111l_opy_
from bstack_utils.bstack11l1l11l11_opy_ import bstack11l1l1l111_opy_
from bstack_utils.bstack1l1111l11_opy_ import bstack1l11lll1l_opy_
import bstack_utils.bstack11ll1111_opy_ as bstack111l1l11l_opy_
bstack11lll1l11_opy_ = None
bstack1ll1l111ll_opy_ = None
bstack1ll1l11111_opy_ = None
bstack1l1l111ll_opy_ = None
bstack11lll1l1l_opy_ = None
bstack11l1llll_opy_ = None
bstack1111l1111_opy_ = None
bstack1llllll1l1_opy_ = None
bstack1ll11l1l1_opy_ = None
bstack11l1111ll_opy_ = None
bstack1l1l11ll1_opy_ = None
bstack1l1l1ll1_opy_ = None
bstack1ll1ll1lll_opy_ = None
bstack111111lll_opy_ = bstack111ll1l_opy_ (u"ࠫࠬፒ")
CONFIG = {}
bstack111l1l1ll_opy_ = False
bstack1ll11111_opy_ = bstack111ll1l_opy_ (u"ࠬ࠭ፓ")
bstack11l11llll_opy_ = bstack111ll1l_opy_ (u"࠭ࠧፔ")
bstack1l11ll1l_opy_ = False
bstack1lll1l11l1_opy_ = []
bstack11l1ll1ll_opy_ = bstack1llll11111_opy_
bstack111ll111ll_opy_ = bstack111ll1l_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺࠧፕ")
bstack111ll1lll1_opy_ = False
logger = logging.getLogger(__name__)
logging.basicConfig(level=bstack11l1ll1ll_opy_,
                    format=bstack111ll1l_opy_ (u"ࠨ࡞ࡱࠩ࠭ࡧࡳࡤࡶ࡬ࡱࡪ࠯ࡳࠡ࡝ࠨࠬࡳࡧ࡭ࡦࠫࡶࡡࡠࠫࠨ࡭ࡧࡹࡩࡱࡴࡡ࡮ࡧࠬࡷࡢࠦ࠭ࠡࠧࠫࡱࡪࡹࡳࡢࡩࡨ࠭ࡸ࠭ፖ"),
                    datefmt=bstack111ll1l_opy_ (u"ࠩࠨࡌ࠿ࠫࡍ࠻ࠧࡖࠫፗ"),
                    stream=sys.stdout)
store = {
    bstack111ll1l_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣ࡭ࡵ࡯࡬ࡡࡸࡹ࡮ࡪࠧፘ"): []
}
def bstack1l1l11l1l_opy_():
    global CONFIG
    global bstack11l1ll1ll_opy_
    if bstack111ll1l_opy_ (u"ࠫࡱࡵࡧࡍࡧࡹࡩࡱ࠭ፙ") in CONFIG:
        bstack11l1ll1ll_opy_ = bstack1lll1ll1_opy_[CONFIG[bstack111ll1l_opy_ (u"ࠬࡲ࡯ࡨࡎࡨࡺࡪࡲࠧፚ")]]
        logging.getLogger().setLevel(bstack11l1ll1ll_opy_)
try:
    from playwright.sync_api import (
        BrowserContext,
        Page
    )
except:
    pass
import json
_111llllll1_opy_ = {}
current_test_uuid = None
def bstack1l1ll11l1_opy_(page, bstack1llll1l1ll_opy_):
    try:
        page.evaluate(bstack111ll1l_opy_ (u"ࠨ࡟ࠡ࠿ࡁࠤࢀࢃࠢ፛"),
                      bstack111ll1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࡾࠦࡦࡩࡴࡪࡱࡱࠦ࠿ࠦࠢࡴࡧࡷࡗࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠣ࠮ࠣࠦࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠢ࠻ࠢࡾࠦࡳࡧ࡭ࡦࠤ࠽ࠫ፜") + json.dumps(
                          bstack1llll1l1ll_opy_) + bstack111ll1l_opy_ (u"ࠣࡿࢀࠦ፝"))
    except Exception as e:
        print(bstack111ll1l_opy_ (u"ࠤࡨࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࠥࡹࡥࡴࡵ࡬ࡳࡳࠦ࡮ࡢ࡯ࡨࠤࢀࢃࠢ፞"), e)
def bstack1l11ll1ll_opy_(page, message, level):
    try:
        page.evaluate(bstack111ll1l_opy_ (u"ࠥࡣࠥࡃ࠾ࠡࡽࢀࠦ፟"), bstack111ll1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻࠣࡣࡦࡸ࡮ࡵ࡮ࠣ࠼ࠣࠦࡦࡴ࡮ࡰࡶࡤࡸࡪࠨࠬࠡࠤࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠧࡀࠠࡼࠤࡧࡥࡹࡧࠢ࠻ࠩ፠") + json.dumps(
            message) + bstack111ll1l_opy_ (u"ࠬ࠲ࠢ࡭ࡧࡹࡩࡱࠨ࠺ࠨ፡") + json.dumps(level) + bstack111ll1l_opy_ (u"࠭ࡽࡾࠩ።"))
    except Exception as e:
        print(bstack111ll1l_opy_ (u"ࠢࡦࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࠣࡥࡳࡴ࡯ࡵࡣࡷ࡭ࡴࡴࠠࡼࡿࠥ፣"), e)
def bstack1l1lll1l_opy_(page, status, message=bstack111ll1l_opy_ (u"ࠣࠤ፤")):
    try:
        if (status == bstack111ll1l_opy_ (u"ࠤࡩࡥ࡮ࡲࡥࡥࠤ፥")):
            page.evaluate(bstack111ll1l_opy_ (u"ࠥࡣࠥࡃ࠾ࠡࡽࢀࠦ፦"),
                          bstack111ll1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻࠣࡣࡦࡸ࡮ࡵ࡮ࠣ࠼ࠣࠦࡸ࡫ࡴࡔࡧࡶࡷ࡮ࡵ࡮ࡔࡶࡤࡸࡺࡹࠢ࠭ࠢࠥࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸࠨ࠺ࠡࡽࠥࡶࡪࡧࡳࡰࡰࠥ࠾ࠬ፧") + json.dumps(
                              bstack111ll1l_opy_ (u"࡙ࠧࡣࡦࡰࡤࡶ࡮ࡵࠠࡧࡣ࡬ࡰࡪࡪࠠࡸ࡫ࡷ࡬࠿ࠦࠢ፨") + str(message)) + bstack111ll1l_opy_ (u"࠭ࠬࠣࡵࡷࡥࡹࡻࡳࠣ࠼ࠪ፩") + json.dumps(status) + bstack111ll1l_opy_ (u"ࠢࡾࡿࠥ፪"))
        else:
            page.evaluate(bstack111ll1l_opy_ (u"ࠣࡡࠣࡁࡃࠦࡻࡾࠤ፫"),
                          bstack111ll1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࠨࡡࡤࡶ࡬ࡳࡳࠨ࠺ࠡࠤࡶࡩࡹ࡙ࡥࡴࡵ࡬ࡳࡳ࡙ࡴࡢࡶࡸࡷࠧ࠲ࠠࠣࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠦ࠿ࠦࡻࠣࡵࡷࡥࡹࡻࡳࠣ࠼ࠪ፬") + json.dumps(
                              status) + bstack111ll1l_opy_ (u"ࠥࢁࢂࠨ፭"))
    except Exception as e:
        print(bstack111ll1l_opy_ (u"ࠦࡪࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡴࡱࡧࡹࡸࡴ࡬࡫࡭ࡺࠠࡴࡧࡷࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠥࡹࡴࡢࡶࡸࡷࠥࢁࡽࠣ፮"), e)
def pytest_configure(config):
    config.args = bstack1l11lll1l_opy_.bstack11l111ll11_opy_(config.args)
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    bstack111ll11l11_opy_ = item.config.getoption(bstack111ll1l_opy_ (u"ࠬࡹ࡫ࡪࡲࡖࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠧ፯"))
    plugins = item.config.getoption(bstack111ll1l_opy_ (u"ࠨࡰ࡭ࡷࡪ࡭ࡳࡹࠢ፰"))
    report = outcome.get_result()
    bstack111lll111l_opy_(item, call, report)
    if bstack111ll1l_opy_ (u"ࠢࡱࡻࡷࡩࡸࡺ࡟ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡶ࡬ࡶࡩ࡬ࡲࠧ፱") not in plugins or bstack1lllllllll_opy_():
        return
    summary = []
    driver = getattr(item, bstack111ll1l_opy_ (u"ࠣࡡࡧࡶ࡮ࡼࡥࡳࠤ፲"), None)
    page = getattr(item, bstack111ll1l_opy_ (u"ࠤࡢࡴࡦ࡭ࡥࠣ፳"), None)
    try:
        if (driver == None):
            driver = threading.current_thread().bstackSessionDriver
    except:
        pass
    item._driver = driver
    if (driver is not None):
        bstack111l1lll1l_opy_(item, report, summary, bstack111ll11l11_opy_)
    if (page is not None):
        bstack111lll1lll_opy_(item, report, summary, bstack111ll11l11_opy_)
def bstack111l1lll1l_opy_(item, report, summary, bstack111ll11l11_opy_):
    if report.when in [bstack111ll1l_opy_ (u"ࠥࡷࡪࡺࡵࡱࠤ፴"), bstack111ll1l_opy_ (u"ࠦࡹ࡫ࡡࡳࡦࡲࡻࡳࠨ፵")]:
        return
    if not bstack1l1l1l11ll_opy_():
        return
    try:
        if (str(bstack111ll11l11_opy_).lower() != bstack111ll1l_opy_ (u"ࠬࡺࡲࡶࡧࠪ፶")):
            item._driver.execute_script(
                bstack111ll1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࠥࡥࡨࡺࡩࡰࡰࠥ࠾ࠥࠨࡳࡦࡶࡖࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠢ࠭ࠢࠥࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸࠨ࠺ࠡࡽࠥࡲࡦࡳࡥࠣ࠼ࠣࠫ፷") + json.dumps(
                    report.nodeid) + bstack111ll1l_opy_ (u"ࠧࡾࡿࠪ፸"))
    except Exception as e:
        summary.append(
            bstack111ll1l_opy_ (u"࡙ࠣࡄࡖࡓࡏࡎࡈ࠼ࠣࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦ࡭ࡢࡴ࡮ࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠥࡴࡡ࡮ࡧ࠽ࠤࢀ࠶ࡽࠣ፹").format(e)
        )
    passed = report.passed or report.skipped or (report.failed and hasattr(report, bstack111ll1l_opy_ (u"ࠤࡺࡥࡸࡾࡦࡢ࡫࡯ࠦ፺")))
    bstack1l111l1ll_opy_ = bstack111ll1l_opy_ (u"ࠥࠦ፻")
    bstack11ll1l11ll_opy_(report)
    if not passed:
        try:
            bstack1l111l1ll_opy_ = report.longrepr.reprcrash
        except Exception as e:
            summary.append(
                bstack111ll1l_opy_ (u"ࠦ࡜ࡇࡒࡏࡋࡑࡋ࠿ࠦࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡧࡩࡹ࡫ࡲ࡮࡫ࡱࡩࠥ࡬ࡡࡪ࡮ࡸࡶࡪࠦࡲࡦࡣࡶࡳࡳࡀࠠࡼ࠲ࢀࠦ፼").format(e)
            )
        try:
            if (threading.current_thread().bstackTestErrorMessages == None):
                threading.current_thread().bstackTestErrorMessages = []
        except Exception as e:
            threading.current_thread().bstackTestErrorMessages = []
        threading.current_thread().bstackTestErrorMessages.append(str(bstack1l111l1ll_opy_))
    if not report.skipped:
        passed = report.passed or (report.failed and hasattr(report, bstack111ll1l_opy_ (u"ࠧࡽࡡࡴࡺࡩࡥ࡮ࡲࠢ፽")))
        bstack1l111l1ll_opy_ = bstack111ll1l_opy_ (u"ࠨࠢ፾")
        if not passed:
            try:
                bstack1l111l1ll_opy_ = report.longrepr.reprcrash
            except Exception as e:
                summary.append(
                    bstack111ll1l_opy_ (u"ࠢࡘࡃࡕࡒࡎࡔࡇ࠻ࠢࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡪࡥࡵࡧࡵࡱ࡮ࡴࡥࠡࡨࡤ࡭ࡱࡻࡲࡦࠢࡵࡩࡦࡹ࡯࡯࠼ࠣࡿ࠵ࢃࠢ፿").format(e)
                )
            try:
                if (threading.current_thread().bstackTestErrorMessages == None):
                    threading.current_thread().bstackTestErrorMessages = []
            except Exception as e:
                threading.current_thread().bstackTestErrorMessages = []
            threading.current_thread().bstackTestErrorMessages.append(str(bstack1l111l1ll_opy_))
        try:
            if passed:
                item._driver.execute_script(
                    bstack111ll1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࡿࡡࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠢࡢࡥࡷ࡭ࡴࡴࠢ࠻ࠢࠥࡥࡳࡴ࡯ࡵࡣࡷࡩࠧ࠲ࠠ࡝ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠥࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸࠨ࠺ࠡࡽ࡟ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠤ࡯ࡩࡻ࡫࡬ࠣ࠼ࠣࠦ࡮ࡴࡦࡰࠤ࠯ࠤࡡࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠦࡩࡧࡴࡢࠤ࠽ࠤࠬᎀ")
                    + json.dumps(bstack111ll1l_opy_ (u"ࠤࡳࡥࡸࡹࡥࡥࠣࠥᎁ"))
                    + bstack111ll1l_opy_ (u"ࠥࡠࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࢃ࡜ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࢂࠨᎂ")
                )
            else:
                item._driver.execute_script(
                    bstack111ll1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻ࡝ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠥࡥࡨࡺࡩࡰࡰࠥ࠾ࠥࠨࡡ࡯ࡰࡲࡸࡦࡺࡥࠣ࠮ࠣࡠࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠨࡡࡳࡩࡸࡱࡪࡴࡴࡴࠤ࠽ࠤࢀࡢࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠧࡲࡥࡷࡧ࡯ࠦ࠿ࠦࠢࡦࡴࡵࡳࡷࠨࠬࠡ࡞ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠣࡦࡤࡸࡦࠨ࠺ࠡࠩᎃ")
                    + json.dumps(str(bstack1l111l1ll_opy_))
                    + bstack111ll1l_opy_ (u"ࠧࡢࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡾ࡞ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡽࠣᎄ")
                )
        except Exception as e:
            summary.append(bstack111ll1l_opy_ (u"ࠨࡗࡂࡔࡑࡍࡓࡍ࠺ࠡࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡦࡴ࡮ࡰࡶࡤࡸࡪࡀࠠࡼ࠲ࢀࠦᎅ").format(e))
def bstack111lll1lll_opy_(item, report, summary, bstack111ll11l11_opy_):
    if report.when in [bstack111ll1l_opy_ (u"ࠢࡴࡧࡷࡹࡵࠨᎆ"), bstack111ll1l_opy_ (u"ࠣࡶࡨࡥࡷࡪ࡯ࡸࡰࠥᎇ")]:
        return
    if (str(bstack111ll11l11_opy_).lower() != bstack111ll1l_opy_ (u"ࠩࡷࡶࡺ࡫ࠧᎈ")):
        bstack1l1ll11l1_opy_(item._page, report.nodeid)
    passed = report.passed or report.skipped or (report.failed and hasattr(report, bstack111ll1l_opy_ (u"ࠥࡻࡦࡹࡸࡧࡣ࡬ࡰࠧᎉ")))
    bstack1l111l1ll_opy_ = bstack111ll1l_opy_ (u"ࠦࠧᎊ")
    bstack11ll1l11ll_opy_(report)
    if not report.skipped:
        if not passed:
            try:
                bstack1l111l1ll_opy_ = report.longrepr.reprcrash
            except Exception as e:
                summary.append(
                    bstack111ll1l_opy_ (u"ࠧ࡝ࡁࡓࡐࡌࡒࡌࡀࠠࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡨࡪࡺࡥࡳ࡯࡬ࡲࡪࠦࡦࡢ࡫࡯ࡹࡷ࡫ࠠࡳࡧࡤࡷࡴࡴ࠺ࠡࡽ࠳ࢁࠧᎋ").format(e)
                )
        try:
            if passed:
                bstack1l1lll1l_opy_(item._page, bstack111ll1l_opy_ (u"ࠨࡰࡢࡵࡶࡩࡩࠨᎌ"))
            else:
                if bstack1l111l1ll_opy_:
                    bstack1l11ll1ll_opy_(item._page, str(bstack1l111l1ll_opy_), bstack111ll1l_opy_ (u"ࠢࡦࡴࡵࡳࡷࠨᎍ"))
                    bstack1l1lll1l_opy_(item._page, bstack111ll1l_opy_ (u"ࠣࡨࡤ࡭ࡱ࡫ࡤࠣᎎ"), str(bstack1l111l1ll_opy_))
                else:
                    bstack1l1lll1l_opy_(item._page, bstack111ll1l_opy_ (u"ࠤࡩࡥ࡮ࡲࡥࡥࠤᎏ"))
        except Exception as e:
            summary.append(bstack111ll1l_opy_ (u"࡛ࠥࡆࡘࡎࡊࡐࡊ࠾ࠥࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡷࡳࡨࡦࡺࡥࠡࡵࡨࡷࡸ࡯࡯࡯ࠢࡶࡸࡦࡺࡵࡴ࠼ࠣࡿ࠵ࢃࠢ᎐").format(e))
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
    parser.addoption(bstack111ll1l_opy_ (u"ࠦ࠲࠳ࡳ࡬࡫ࡳࡗࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠣ᎑"), default=bstack111ll1l_opy_ (u"ࠧࡌࡡ࡭ࡵࡨࠦ᎒"), help=bstack111ll1l_opy_ (u"ࠨࡁࡶࡶࡲࡱࡦࡺࡩࡤࠢࡶࡩࡹࠦࡳࡦࡵࡶ࡭ࡴࡴࠠ࡯ࡣࡰࡩࠧ᎓"))
    try:
        import pytest_selenium.pytest_selenium
    except:
        parser.addoption(bstack111ll1l_opy_ (u"ࠢ࠮࠯ࡧࡶ࡮ࡼࡥࡳࠤ᎔"), action=bstack111ll1l_opy_ (u"ࠣࡵࡷࡳࡷ࡫ࠢ᎕"), default=bstack111ll1l_opy_ (u"ࠤࡦ࡬ࡷࡵ࡭ࡦࠤ᎖"),
                         help=bstack111ll1l_opy_ (u"ࠥࡈࡷ࡯ࡶࡦࡴࠣࡸࡴࠦࡲࡶࡰࠣࡸࡪࡹࡴࡴࠤ᎗"))
def bstack111llll111_opy_(log):
    if not (log[bstack111ll1l_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬ᎘")] and log[bstack111ll1l_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ࠭᎙")].strip()):
        return
    active = bstack111lll1l1l_opy_()
    log = {
        bstack111ll1l_opy_ (u"࠭࡬ࡦࡸࡨࡰࠬ᎚"): log[bstack111ll1l_opy_ (u"ࠧ࡭ࡧࡹࡩࡱ࠭᎛")],
        bstack111ll1l_opy_ (u"ࠨࡶ࡬ࡱࡪࡹࡴࡢ࡯ࡳࠫ᎜"): datetime.datetime.utcnow().isoformat() + bstack111ll1l_opy_ (u"ࠩ࡝ࠫ᎝"),
        bstack111ll1l_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫ᎞"): log[bstack111ll1l_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬ᎟")],
    }
    if active:
        if active[bstack111ll1l_opy_ (u"ࠬࡺࡹࡱࡧࠪᎠ")] == bstack111ll1l_opy_ (u"࠭ࡨࡰࡱ࡮ࠫᎡ"):
            log[bstack111ll1l_opy_ (u"ࠧࡩࡱࡲ࡯ࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧᎢ")] = active[bstack111ll1l_opy_ (u"ࠨࡪࡲࡳࡰࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨᎣ")]
        elif active[bstack111ll1l_opy_ (u"ࠩࡷࡽࡵ࡫ࠧᎤ")] == bstack111ll1l_opy_ (u"ࠪࡸࡪࡹࡴࠨᎥ"):
            log[bstack111ll1l_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫᎦ")] = active[bstack111ll1l_opy_ (u"ࠬࡺࡥࡴࡶࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠬᎧ")]
    bstack1l11lll1l_opy_.bstack11l111l1ll_opy_([log])
def bstack111lll1l1l_opy_():
    if len(store[bstack111ll1l_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡩࡱࡲ࡯ࡤࡻࡵࡪࡦࠪᎨ")]) > 0 and store[bstack111ll1l_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡪࡲࡳࡰࡥࡵࡶ࡫ࡧࠫᎩ")][-1]:
        return {
            bstack111ll1l_opy_ (u"ࠨࡶࡼࡴࡪ࠭Ꭺ"): bstack111ll1l_opy_ (u"ࠩ࡫ࡳࡴࡱࠧᎫ"),
            bstack111ll1l_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪᎬ"): store[bstack111ll1l_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤ࡮࡯ࡰ࡭ࡢࡹࡺ࡯ࡤࠨᎭ")][-1]
        }
    if store.get(bstack111ll1l_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡴࡦࡵࡷࡣࡺࡻࡩࡥࠩᎮ"), None):
        return {
            bstack111ll1l_opy_ (u"࠭ࡴࡺࡲࡨࠫᎯ"): bstack111ll1l_opy_ (u"ࠧࡵࡧࡶࡸࠬᎰ"),
            bstack111ll1l_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨᎱ"): store[bstack111ll1l_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢࡸࡪࡹࡴࡠࡷࡸ࡭ࡩ࠭Ꮂ")]
        }
    return None
bstack111ll1l111_opy_ = bstack1l1ll11l1l_opy_(bstack111llll111_opy_)
def pytest_runtest_call(item):
    try:
        global CONFIG
        global bstack111ll1lll1_opy_
        if bstack111ll1lll1_opy_:
            driver = getattr(item, bstack111ll1l_opy_ (u"ࠪࡣࡩࡸࡩࡷࡧࡵࠫᎳ"), None)
            bstack111ll1ll1l_opy_ = bstack111l1l11l_opy_.bstack1l1lll1ll1_opy_(CONFIG, bstack1l1l11lll1_opy_(item.own_markers))
            item._a11y_started = bstack111l1l11l_opy_.bstack1l1lll11ll_opy_(driver, bstack111ll1ll1l_opy_)
        if not bstack1l11lll1l_opy_.on() or bstack111ll111ll_opy_ != bstack111ll1l_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࠫᎴ"):
            return
        global current_test_uuid, bstack111ll1l111_opy_
        bstack111ll1l111_opy_.start()
        bstack111ll11l1l_opy_ = {
            bstack111ll1l_opy_ (u"ࠬࡻࡵࡪࡦࠪᎵ"): uuid4().__str__(),
            bstack111ll1l_opy_ (u"࠭ࡳࡵࡣࡵࡸࡪࡪ࡟ࡢࡶࠪᎶ"): datetime.datetime.utcnow().isoformat() + bstack111ll1l_opy_ (u"࡛ࠧࠩᎷ")
        }
        current_test_uuid = bstack111ll11l1l_opy_[bstack111ll1l_opy_ (u"ࠨࡷࡸ࡭ࡩ࠭Ꮈ")]
        store[bstack111ll1l_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢࡸࡪࡹࡴࡠࡷࡸ࡭ࡩ࠭Ꮉ")] = bstack111ll11l1l_opy_[bstack111ll1l_opy_ (u"ࠪࡹࡺ࡯ࡤࠨᎺ")]
        threading.current_thread().current_test_uuid = current_test_uuid
        _111llllll1_opy_[item.nodeid] = {**_111llllll1_opy_[item.nodeid], **bstack111ll11l1l_opy_}
        bstack111ll1l1ll_opy_(item, _111llllll1_opy_[item.nodeid], bstack111ll1l_opy_ (u"࡙ࠫ࡫ࡳࡵࡔࡸࡲࡘࡺࡡࡳࡶࡨࡨࠬᎻ"))
    except Exception as err:
        print(bstack111ll1l_opy_ (u"ࠬࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤࡵࡿࡴࡦࡵࡷࡣࡷࡻ࡮ࡵࡧࡶࡸࡤࡩࡡ࡭࡮࠽ࠤࢀࢃࠧᎼ"), str(err))
def pytest_runtest_setup(item):
    if bstack1l1l11ll1l_opy_():
        atexit.register(bstack11l11lll1_opy_)
        try:
            item.config.hook.pytest_selenium_runtest_makereport = bstack11ll1ll1ll_opy_
        except Exception as err:
            threading.current_thread().testStatus = bstack111ll1l_opy_ (u"࠭ࡰࡢࡵࡶࡩࡩ࠭Ꮍ")
    try:
        if not bstack1l11lll1l_opy_.on():
            return
        bstack111ll1l111_opy_.start()
        uuid = uuid4().__str__()
        bstack111ll11l1l_opy_ = {
            bstack111ll1l_opy_ (u"ࠧࡶࡷ࡬ࡨࠬᎾ"): uuid,
            bstack111ll1l_opy_ (u"ࠨࡵࡷࡥࡷࡺࡥࡥࡡࡤࡸࠬᎿ"): datetime.datetime.utcnow().isoformat() + bstack111ll1l_opy_ (u"ࠩ࡝ࠫᏀ"),
            bstack111ll1l_opy_ (u"ࠪࡸࡾࡶࡥࠨᏁ"): bstack111ll1l_opy_ (u"ࠫ࡭ࡵ࡯࡬ࠩᏂ"),
            bstack111ll1l_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡢࡸࡾࡶࡥࠨᏃ"): bstack111ll1l_opy_ (u"࠭ࡂࡆࡈࡒࡖࡊࡥࡅࡂࡅࡋࠫᏄ"),
            bstack111ll1l_opy_ (u"ࠧࡩࡱࡲ࡯ࡤࡴࡡ࡮ࡧࠪᏅ"): bstack111ll1l_opy_ (u"ࠨࡵࡨࡸࡺࡶࠧᏆ")
        }
        threading.current_thread().bstack111ll1l11l_opy_ = uuid
        store[bstack111ll1l_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢࡸࡪࡹࡴࡠ࡫ࡷࡩࡲ࠭Ꮗ")] = item
        store[bstack111ll1l_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣ࡭ࡵ࡯࡬ࡡࡸࡹ࡮ࡪࠧᏈ")] = [uuid]
        if not _111llllll1_opy_.get(item.nodeid, None):
            _111llllll1_opy_[item.nodeid] = {bstack111ll1l_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡵࠪᏉ"): [], bstack111ll1l_opy_ (u"ࠬ࡬ࡩࡹࡶࡸࡶࡪࡹࠧᏊ"): []}
        _111llllll1_opy_[item.nodeid][bstack111ll1l_opy_ (u"࠭ࡨࡰࡱ࡮ࡷࠬᏋ")].append(bstack111ll11l1l_opy_[bstack111ll1l_opy_ (u"ࠧࡶࡷ࡬ࡨࠬᏌ")])
        _111llllll1_opy_[item.nodeid + bstack111ll1l_opy_ (u"ࠨ࠯ࡶࡩࡹࡻࡰࠨᏍ")] = bstack111ll11l1l_opy_
        bstack111ll11111_opy_(item, bstack111ll11l1l_opy_, bstack111ll1l_opy_ (u"ࠩࡋࡳࡴࡱࡒࡶࡰࡖࡸࡦࡸࡴࡦࡦࠪᏎ"))
    except Exception as err:
        print(bstack111ll1l_opy_ (u"ࠪࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡳࡽࡹ࡫ࡳࡵࡡࡵࡹࡳࡺࡥࡴࡶࡢࡷࡪࡺࡵࡱ࠼ࠣࡿࢂ࠭Ꮟ"), str(err))
def pytest_runtest_teardown(item):
    try:
        if getattr(item, bstack111ll1l_opy_ (u"ࠫࡤࡧ࠱࠲ࡻࡢࡷࡹࡧࡲࡵࡧࡧࠫᏐ"), False):
            logger.info(bstack111ll1l_opy_ (u"ࠧࡇࡵࡵࡱࡰࡥࡹ࡫ࠠࡵࡧࡶࡸࠥࡩࡡࡴࡧࠣࡩࡽ࡫ࡣࡶࡶ࡬ࡳࡳࠦࡨࡢࡵࠣࡩࡳࡪࡥࡥ࠰ࠣࡔࡷࡵࡣࡦࡵࡶ࡭ࡳ࡭ࠠࡧࡱࡵࠤࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡹ࡫ࡳࡵ࡫ࡱ࡫ࠥ࡯ࡳࠡࡷࡱࡨࡪࡸࡷࡢࡻ࠱ࠤࠧᏑ"))
            driver = getattr(item, bstack111ll1l_opy_ (u"࠭࡟ࡥࡴ࡬ࡺࡪࡸࠧᏒ"), None)
            bstack111l1l11l_opy_.bstack1l1llll11l_opy_(driver, item)
        if not bstack1l11lll1l_opy_.on():
            return
        bstack111ll11l1l_opy_ = {
            bstack111ll1l_opy_ (u"ࠧࡶࡷ࡬ࡨࠬᏓ"): uuid4().__str__(),
            bstack111ll1l_opy_ (u"ࠨࡵࡷࡥࡷࡺࡥࡥࡡࡤࡸࠬᏔ"): datetime.datetime.utcnow().isoformat() + bstack111ll1l_opy_ (u"ࠩ࡝ࠫᏕ"),
            bstack111ll1l_opy_ (u"ࠪࡸࡾࡶࡥࠨᏖ"): bstack111ll1l_opy_ (u"ࠫ࡭ࡵ࡯࡬ࠩᏗ"),
            bstack111ll1l_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡢࡸࡾࡶࡥࠨᏘ"): bstack111ll1l_opy_ (u"࠭ࡁࡇࡖࡈࡖࡤࡋࡁࡄࡊࠪᏙ"),
            bstack111ll1l_opy_ (u"ࠧࡩࡱࡲ࡯ࡤࡴࡡ࡮ࡧࠪᏚ"): bstack111ll1l_opy_ (u"ࠨࡶࡨࡥࡷࡪ࡯ࡸࡰࠪᏛ")
        }
        _111llllll1_opy_[item.nodeid + bstack111ll1l_opy_ (u"ࠩ࠰ࡸࡪࡧࡲࡥࡱࡺࡲࠬᏜ")] = bstack111ll11l1l_opy_
        bstack111ll11111_opy_(item, bstack111ll11l1l_opy_, bstack111ll1l_opy_ (u"ࠪࡌࡴࡵ࡫ࡓࡷࡱࡗࡹࡧࡲࡵࡧࡧࠫᏝ"))
    except Exception as err:
        print(bstack111ll1l_opy_ (u"ࠫࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡴࡾࡺࡥࡴࡶࡢࡶࡺࡴࡴࡦࡵࡷࡣࡹ࡫ࡡࡳࡦࡲࡻࡳࡀࠠࡼࡿࠪᏞ"), str(err))
@pytest.hookimpl(hookwrapper=True)
def pytest_fixture_setup(fixturedef, request):
    if not bstack1l11lll1l_opy_.on():
        yield
        return
    start_time = datetime.datetime.now()
    if bstack11ll1l1l11_opy_(fixturedef.argname):
        store[bstack111ll1l_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥ࡭ࡰࡦࡸࡰࡪࡥࡩࡵࡧࡰࠫᏟ")] = request.node
    elif bstack11ll1ll111_opy_(fixturedef.argname):
        store[bstack111ll1l_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡤ࡮ࡤࡷࡸࡥࡩࡵࡧࡰࠫᏠ")] = request.node
    outcome = yield
    try:
        fixture = {
            bstack111ll1l_opy_ (u"ࠧ࡯ࡣࡰࡩࠬᏡ"): fixturedef.argname,
            bstack111ll1l_opy_ (u"ࠨࡴࡨࡷࡺࡲࡴࠨᏢ"): bstack1l1l111111_opy_(outcome),
            bstack111ll1l_opy_ (u"ࠩࡧࡹࡷࡧࡴࡪࡱࡱࠫᏣ"): (datetime.datetime.now() - start_time).total_seconds() * 1000
        }
        bstack111lll11l1_opy_ = store[bstack111ll1l_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣࡹ࡫ࡳࡵࡡ࡬ࡸࡪࡳࠧᏤ")]
        if not _111llllll1_opy_.get(bstack111lll11l1_opy_.nodeid, None):
            _111llllll1_opy_[bstack111lll11l1_opy_.nodeid] = {bstack111ll1l_opy_ (u"ࠫ࡫࡯ࡸࡵࡷࡵࡩࡸ࠭Ꮵ"): []}
        _111llllll1_opy_[bstack111lll11l1_opy_.nodeid][bstack111ll1l_opy_ (u"ࠬ࡬ࡩࡹࡶࡸࡶࡪࡹࠧᏦ")].append(fixture)
    except Exception as err:
        logger.debug(bstack111ll1l_opy_ (u"࠭ࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡶࡹࡵࡧࡶࡸࡤ࡬ࡩࡹࡶࡸࡶࡪࡥࡳࡦࡶࡸࡴ࠿ࠦࡻࡾࠩᏧ"), str(err))
if bstack1lllllllll_opy_() and bstack1l11lll1l_opy_.on():
    def pytest_bdd_before_step(request, step):
        try:
            _111llllll1_opy_[request.node.nodeid][bstack111ll1l_opy_ (u"ࠧࡵࡧࡶࡸࡤࡪࡡࡵࡣࠪᏨ")].bstack11l1ll11l1_opy_(id(step))
        except Exception as err:
            print(bstack111ll1l_opy_ (u"ࠨࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡱࡻࡷࡩࡸࡺ࡟ࡣࡦࡧࡣࡧ࡫ࡦࡰࡴࡨࡣࡸࡺࡥࡱ࠼ࠣࡿࢂ࠭Ꮹ"), str(err))
    def pytest_bdd_step_error(request, step, exception):
        try:
            _111llllll1_opy_[request.node.nodeid][bstack111ll1l_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡥࡣࡷࡥࠬᏪ")].bstack11l1l111l1_opy_(id(step), Result.failed(exception=exception))
        except Exception as err:
            print(bstack111ll1l_opy_ (u"ࠪࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡳࡽࡹ࡫ࡳࡵࡡࡥࡨࡩࡥࡳࡵࡧࡳࡣࡪࡸࡲࡰࡴ࠽ࠤࢀࢃࠧᏫ"), str(err))
    def pytest_bdd_after_step(request, step):
        try:
            bstack11l1l11l11_opy_: bstack11l1l1l111_opy_ = _111llllll1_opy_[request.node.nodeid][bstack111ll1l_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡧࡥࡹࡧࠧᏬ")]
            bstack11l1l11l11_opy_.bstack11l1l111l1_opy_(id(step), Result.passed())
        except Exception as err:
            print(bstack111ll1l_opy_ (u"ࠬࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤࡵࡿࡴࡦࡵࡷࡣࡧࡪࡤࡠࡵࡷࡩࡵࡥࡥࡳࡴࡲࡶ࠿ࠦࡻࡾࠩᏭ"), str(err))
    def pytest_bdd_before_scenario(request, feature, scenario):
        global bstack111ll111ll_opy_
        try:
            if not bstack1l11lll1l_opy_.on() or bstack111ll111ll_opy_ != bstack111ll1l_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠳ࡢࡥࡦࠪᏮ"):
                return
            global bstack111ll1l111_opy_
            bstack111ll1l111_opy_.start()
            if not _111llllll1_opy_.get(request.node.nodeid, None):
                _111llllll1_opy_[request.node.nodeid] = {}
            bstack11l1l11l11_opy_ = bstack11l1l1l111_opy_.bstack11l1l1l11l_opy_(
                scenario, feature, request.node,
                name=bstack11ll1l1ll1_opy_(request.node, scenario),
                bstack11l1l11lll_opy_=bstack1111ll111_opy_(),
                file_path=feature.filename,
                scope=[feature.name],
                framework=bstack111ll1l_opy_ (u"ࠧࡑࡻࡷࡩࡸࡺ࠭ࡤࡷࡦࡹࡲࡨࡥࡳࠩᏯ"),
                tags=bstack11ll1lll1l_opy_(feature, scenario)
            )
            _111llllll1_opy_[request.node.nodeid][bstack111ll1l_opy_ (u"ࠨࡶࡨࡷࡹࡥࡤࡢࡶࡤࠫᏰ")] = bstack11l1l11l11_opy_
            bstack111lll1l11_opy_(bstack11l1l11l11_opy_.uuid)
            bstack1l11lll1l_opy_.bstack11l11lll1l_opy_(bstack111ll1l_opy_ (u"ࠩࡗࡩࡸࡺࡒࡶࡰࡖࡸࡦࡸࡴࡦࡦࠪᏱ"), bstack11l1l11l11_opy_)
        except Exception as err:
            print(bstack111ll1l_opy_ (u"ࠪࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡳࡽࡹ࡫ࡳࡵࡡࡥࡨࡩࡥࡢࡦࡨࡲࡶࡪࡥࡳࡤࡧࡱࡥࡷ࡯࡯࠻ࠢࡾࢁࠬᏲ"), str(err))
def bstack11l111111l_opy_(bstack111lll1ll1_opy_):
    if bstack111lll1ll1_opy_ in store[bstack111ll1l_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤ࡮࡯ࡰ࡭ࡢࡹࡺ࡯ࡤࠨᏳ")]:
        store[bstack111ll1l_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡨࡰࡱ࡮ࡣࡺࡻࡩࡥࠩᏴ")].remove(bstack111lll1ll1_opy_)
def bstack111lll1l11_opy_(bstack111ll1111l_opy_):
    store[bstack111ll1l_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡵࡧࡶࡸࡤࡻࡵࡪࡦࠪᏵ")] = bstack111ll1111l_opy_
    threading.current_thread().current_test_uuid = bstack111ll1111l_opy_
@bstack1l11lll1l_opy_.bstack11l11l1ll1_opy_
def bstack111lll111l_opy_(item, call, report):
    global bstack111ll111ll_opy_
    try:
        if report.when == bstack111ll1l_opy_ (u"ࠧࡤࡣ࡯ࡰࠬ᏶"):
            bstack111ll1l111_opy_.reset()
        if report.when == bstack111ll1l_opy_ (u"ࠨࡥࡤࡰࡱ࠭᏷"):
            if bstack111ll111ll_opy_ == bstack111ll1l_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࠩᏸ"):
                _111llllll1_opy_[item.nodeid][bstack111ll1l_opy_ (u"ࠪࡪ࡮ࡴࡩࡴࡪࡨࡨࡤࡧࡴࠨᏹ")] = bstack1l11ll1lll_opy_(report.stop)
                bstack111ll1l1ll_opy_(item, _111llllll1_opy_[item.nodeid], bstack111ll1l_opy_ (u"࡙ࠫ࡫ࡳࡵࡔࡸࡲࡋ࡯࡮ࡪࡵ࡫ࡩࡩ࠭ᏺ"), report, call)
                store[bstack111ll1l_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡴࡦࡵࡷࡣࡺࡻࡩࡥࠩᏻ")] = None
            elif bstack111ll111ll_opy_ == bstack111ll1l_opy_ (u"ࠨࡰࡺࡶࡨࡷࡹ࠳ࡢࡥࡦࠥᏼ"):
                bstack11l1l11l11_opy_ = _111llllll1_opy_[item.nodeid][bstack111ll1l_opy_ (u"ࠧࡵࡧࡶࡸࡤࡪࡡࡵࡣࠪᏽ")]
                bstack11l1l11l11_opy_.set(hooks=_111llllll1_opy_[item.nodeid].get(bstack111ll1l_opy_ (u"ࠨࡪࡲࡳࡰࡹࠧ᏾"), []))
                exception, bstack1l1l111l11_opy_ = None, None
                if call.excinfo:
                    exception = call.excinfo.value
                    bstack1l1l111l11_opy_ = [call.excinfo.exconly(), report.longreprtext]
                bstack11l1l11l11_opy_.stop(time=bstack1l11ll1lll_opy_(report.stop), result=Result(result=report.outcome, exception=exception, bstack1l1l111l11_opy_=bstack1l1l111l11_opy_))
                bstack1l11lll1l_opy_.bstack11l11lll1l_opy_(bstack111ll1l_opy_ (u"ࠩࡗࡩࡸࡺࡒࡶࡰࡉ࡭ࡳ࡯ࡳࡩࡧࡧࠫ᏿"), _111llllll1_opy_[item.nodeid][bstack111ll1l_opy_ (u"ࠪࡸࡪࡹࡴࡠࡦࡤࡸࡦ࠭᐀")])
        elif report.when in [bstack111ll1l_opy_ (u"ࠫࡸ࡫ࡴࡶࡲࠪᐁ"), bstack111ll1l_opy_ (u"ࠬࡺࡥࡢࡴࡧࡳࡼࡴࠧᐂ")]:
            bstack111ll1l1l1_opy_ = item.nodeid + bstack111ll1l_opy_ (u"࠭࠭ࠨᐃ") + report.when
            if report.skipped:
                hook_type = bstack111ll1l_opy_ (u"ࠧࡃࡇࡉࡓࡗࡋ࡟ࡆࡃࡆࡌࠬᐄ") if report.when == bstack111ll1l_opy_ (u"ࠨࡵࡨࡸࡺࡶࠧᐅ") else bstack111ll1l_opy_ (u"ࠩࡄࡊ࡙ࡋࡒࡠࡇࡄࡇࡍ࠭ᐆ")
                _111llllll1_opy_[bstack111ll1l1l1_opy_] = {
                    bstack111ll1l_opy_ (u"ࠪࡹࡺ࡯ࡤࠨᐇ"): uuid4().__str__(),
                    bstack111ll1l_opy_ (u"ࠫࡸࡺࡡࡳࡶࡨࡨࡤࡧࡴࠨᐈ"): datetime.datetime.utcfromtimestamp(report.start).isoformat() + bstack111ll1l_opy_ (u"ࠬࡠࠧᐉ"),
                    bstack111ll1l_opy_ (u"࠭ࡨࡰࡱ࡮ࡣࡹࡿࡰࡦࠩᐊ"): hook_type
                }
            _111llllll1_opy_[bstack111ll1l1l1_opy_][bstack111ll1l_opy_ (u"ࠧࡧ࡫ࡱ࡭ࡸ࡮ࡥࡥࡡࡤࡸࠬᐋ")] = datetime.datetime.utcfromtimestamp(report.stop).isoformat() + bstack111ll1l_opy_ (u"ࠨ࡜ࠪᐌ")
            bstack11l111111l_opy_(_111llllll1_opy_[bstack111ll1l1l1_opy_][bstack111ll1l_opy_ (u"ࠩࡸࡹ࡮ࡪࠧᐍ")])
            bstack111ll11111_opy_(item, _111llllll1_opy_[bstack111ll1l1l1_opy_], bstack111ll1l_opy_ (u"ࠪࡌࡴࡵ࡫ࡓࡷࡱࡊ࡮ࡴࡩࡴࡪࡨࡨࠬᐎ"), report, call)
            if report.when == bstack111ll1l_opy_ (u"ࠫࡸ࡫ࡴࡶࡲࠪᐏ"):
                if report.outcome == bstack111ll1l_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬᐐ"):
                    bstack111ll11l1l_opy_ = {
                        bstack111ll1l_opy_ (u"࠭ࡵࡶ࡫ࡧࠫᐑ"): uuid4().__str__(),
                        bstack111ll1l_opy_ (u"ࠧࡴࡶࡤࡶࡹ࡫ࡤࡠࡣࡷࠫᐒ"): bstack1111ll111_opy_(),
                        bstack111ll1l_opy_ (u"ࠨࡨ࡬ࡲ࡮ࡹࡨࡦࡦࡢࡥࡹ࠭ᐓ"): bstack1111ll111_opy_()
                    }
                    _111llllll1_opy_[item.nodeid] = {**_111llllll1_opy_[item.nodeid], **bstack111ll11l1l_opy_}
                    bstack111ll1l1ll_opy_(item, _111llllll1_opy_[item.nodeid], bstack111ll1l_opy_ (u"ࠩࡗࡩࡸࡺࡒࡶࡰࡖࡸࡦࡸࡴࡦࡦࠪᐔ"))
                    bstack111ll1l1ll_opy_(item, _111llllll1_opy_[item.nodeid], bstack111ll1l_opy_ (u"ࠪࡘࡪࡹࡴࡓࡷࡱࡊ࡮ࡴࡩࡴࡪࡨࡨࠬᐕ"), report, call)
    except Exception as err:
        print(bstack111ll1l_opy_ (u"ࠫࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣ࡬ࡦࡴࡤ࡭ࡧࡢࡳ࠶࠷ࡹࡠࡶࡨࡷࡹࡥࡥࡷࡧࡱࡸ࠿ࠦࡻࡾࠩᐖ"), str(err))
def bstack11l1111111_opy_(test, bstack111ll11l1l_opy_, result=None, call=None, bstack111l11l1_opy_=None, outcome=None):
    file_path = os.path.relpath(test.fspath.strpath, start=os.getcwd())
    bstack11l1l11l11_opy_ = {
        bstack111ll1l_opy_ (u"ࠬࡻࡵࡪࡦࠪᐗ"): bstack111ll11l1l_opy_[bstack111ll1l_opy_ (u"࠭ࡵࡶ࡫ࡧࠫᐘ")],
        bstack111ll1l_opy_ (u"ࠧࡵࡻࡳࡩࠬᐙ"): bstack111ll1l_opy_ (u"ࠨࡶࡨࡷࡹ࠭ᐚ"),
        bstack111ll1l_opy_ (u"ࠩࡱࡥࡲ࡫ࠧᐛ"): test.name,
        bstack111ll1l_opy_ (u"ࠪࡦࡴࡪࡹࠨᐜ"): {
            bstack111ll1l_opy_ (u"ࠫࡱࡧ࡮ࡨࠩᐝ"): bstack111ll1l_opy_ (u"ࠬࡶࡹࡵࡪࡲࡲࠬᐞ"),
            bstack111ll1l_opy_ (u"࠭ࡣࡰࡦࡨࠫᐟ"): inspect.getsource(test.obj)
        },
        bstack111ll1l_opy_ (u"ࠧࡪࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫᐠ"): test.name,
        bstack111ll1l_opy_ (u"ࠨࡵࡦࡳࡵ࡫ࠧᐡ"): test.name,
        bstack111ll1l_opy_ (u"ࠩࡶࡧࡴࡶࡥࡴࠩᐢ"): bstack1l11lll1l_opy_.bstack11l11111ll_opy_(test),
        bstack111ll1l_opy_ (u"ࠪࡪ࡮ࡲࡥࡠࡰࡤࡱࡪ࠭ᐣ"): file_path,
        bstack111ll1l_opy_ (u"ࠫࡱࡵࡣࡢࡶ࡬ࡳࡳ࠭ᐤ"): file_path,
        bstack111ll1l_opy_ (u"ࠬࡸࡥࡴࡷ࡯ࡸࠬᐥ"): bstack111ll1l_opy_ (u"࠭ࡰࡦࡰࡧ࡭ࡳ࡭ࠧᐦ"),
        bstack111ll1l_opy_ (u"ࠧࡷࡥࡢࡪ࡮ࡲࡥࡱࡣࡷ࡬ࠬᐧ"): file_path,
        bstack111ll1l_opy_ (u"ࠨࡵࡷࡥࡷࡺࡥࡥࡡࡤࡸࠬᐨ"): bstack111ll11l1l_opy_[bstack111ll1l_opy_ (u"ࠩࡶࡸࡦࡸࡴࡦࡦࡢࡥࡹ࠭ᐩ")],
        bstack111ll1l_opy_ (u"ࠪࡪࡷࡧ࡭ࡦࡹࡲࡶࡰ࠭ᐪ"): bstack111ll1l_opy_ (u"ࠫࡕࡿࡴࡦࡵࡷࠫᐫ"),
        bstack111ll1l_opy_ (u"ࠬࡩࡵࡴࡶࡲࡱࡗ࡫ࡲࡶࡰࡓࡥࡷࡧ࡭ࠨᐬ"): {
            bstack111ll1l_opy_ (u"࠭ࡲࡦࡴࡸࡲࡤࡴࡡ࡮ࡧࠪᐭ"): test.nodeid
        },
        bstack111ll1l_opy_ (u"ࠧࡵࡣࡪࡷࠬᐮ"): bstack1l1l11lll1_opy_(test.own_markers)
    }
    if bstack111l11l1_opy_ in [bstack111ll1l_opy_ (u"ࠨࡖࡨࡷࡹࡘࡵ࡯ࡕ࡮࡭ࡵࡶࡥࡥࠩᐯ"), bstack111ll1l_opy_ (u"ࠩࡗࡩࡸࡺࡒࡶࡰࡉ࡭ࡳ࡯ࡳࡩࡧࡧࠫᐰ")]:
        bstack11l1l11l11_opy_[bstack111ll1l_opy_ (u"ࠪࡱࡪࡺࡡࠨᐱ")] = {
            bstack111ll1l_opy_ (u"ࠫ࡫࡯ࡸࡵࡷࡵࡩࡸ࠭ᐲ"): bstack111ll11l1l_opy_.get(bstack111ll1l_opy_ (u"ࠬ࡬ࡩࡹࡶࡸࡶࡪࡹࠧᐳ"), [])
        }
    if bstack111l11l1_opy_ == bstack111ll1l_opy_ (u"࠭ࡔࡦࡵࡷࡖࡺࡴࡓ࡬࡫ࡳࡴࡪࡪࠧᐴ"):
        bstack11l1l11l11_opy_[bstack111ll1l_opy_ (u"ࠧࡳࡧࡶࡹࡱࡺࠧᐵ")] = bstack111ll1l_opy_ (u"ࠨࡵ࡮࡭ࡵࡶࡥࡥࠩᐶ")
        bstack11l1l11l11_opy_[bstack111ll1l_opy_ (u"ࠩ࡫ࡳࡴࡱࡳࠨᐷ")] = bstack111ll11l1l_opy_[bstack111ll1l_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡴࠩᐸ")]
        bstack11l1l11l11_opy_[bstack111ll1l_opy_ (u"ࠫ࡫࡯࡮ࡪࡵ࡫ࡩࡩࡥࡡࡵࠩᐹ")] = bstack111ll11l1l_opy_[bstack111ll1l_opy_ (u"ࠬ࡬ࡩ࡯࡫ࡶ࡬ࡪࡪ࡟ࡢࡶࠪᐺ")]
    if result:
        bstack11l1l11l11_opy_[bstack111ll1l_opy_ (u"࠭ࡲࡦࡵࡸࡰࡹ࠭ᐻ")] = result.outcome
        bstack11l1l11l11_opy_[bstack111ll1l_opy_ (u"ࠧࡥࡷࡵࡥࡹ࡯࡯࡯ࡡ࡬ࡲࡤࡳࡳࠨᐼ")] = result.duration * 1000
        bstack11l1l11l11_opy_[bstack111ll1l_opy_ (u"ࠨࡨ࡬ࡲ࡮ࡹࡨࡦࡦࡢࡥࡹ࠭ᐽ")] = bstack111ll11l1l_opy_[bstack111ll1l_opy_ (u"ࠩࡩ࡭ࡳ࡯ࡳࡩࡧࡧࡣࡦࡺࠧᐾ")]
        if result.failed:
            bstack11l1l11l11_opy_[bstack111ll1l_opy_ (u"ࠪࡪࡦ࡯࡬ࡶࡴࡨࡣࡹࡿࡰࡦࠩᐿ")] = bstack1l11lll1l_opy_.bstack1l11ll1l1l_opy_(call.excinfo.typename)
            bstack11l1l11l11_opy_[bstack111ll1l_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡷࡵࡩࠬᑀ")] = bstack1l11lll1l_opy_.bstack11l111l1l1_opy_(call.excinfo, result)
        bstack11l1l11l11_opy_[bstack111ll1l_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡶࠫᑁ")] = bstack111ll11l1l_opy_[bstack111ll1l_opy_ (u"࠭ࡨࡰࡱ࡮ࡷࠬᑂ")]
    if outcome:
        bstack11l1l11l11_opy_[bstack111ll1l_opy_ (u"ࠧࡳࡧࡶࡹࡱࡺࠧᑃ")] = bstack1l1l111111_opy_(outcome)
        bstack11l1l11l11_opy_[bstack111ll1l_opy_ (u"ࠨࡦࡸࡶࡦࡺࡩࡰࡰࡢ࡭ࡳࡥ࡭ࡴࠩᑄ")] = 0
        bstack11l1l11l11_opy_[bstack111ll1l_opy_ (u"ࠩࡩ࡭ࡳ࡯ࡳࡩࡧࡧࡣࡦࡺࠧᑅ")] = bstack111ll11l1l_opy_[bstack111ll1l_opy_ (u"ࠪࡪ࡮ࡴࡩࡴࡪࡨࡨࡤࡧࡴࠨᑆ")]
        if bstack11l1l11l11_opy_[bstack111ll1l_opy_ (u"ࠫࡷ࡫ࡳࡶ࡮ࡷࠫᑇ")] == bstack111ll1l_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬᑈ"):
            bstack11l1l11l11_opy_[bstack111ll1l_opy_ (u"࠭ࡦࡢ࡫࡯ࡹࡷ࡫࡟ࡵࡻࡳࡩࠬᑉ")] = bstack111ll1l_opy_ (u"ࠧࡖࡰ࡫ࡥࡳࡪ࡬ࡦࡦࡈࡶࡷࡵࡲࠨᑊ")  # bstack11l11111l1_opy_
            bstack11l1l11l11_opy_[bstack111ll1l_opy_ (u"ࠨࡨࡤ࡭ࡱࡻࡲࡦࠩᑋ")] = [{bstack111ll1l_opy_ (u"ࠩࡥࡥࡨࡱࡴࡳࡣࡦࡩࠬᑌ"): [bstack111ll1l_opy_ (u"ࠪࡷࡴࡳࡥࠡࡧࡵࡶࡴࡸࠧᑍ")]}]
        bstack11l1l11l11_opy_[bstack111ll1l_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡵࠪᑎ")] = bstack111ll11l1l_opy_[bstack111ll1l_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡶࠫᑏ")]
    return bstack11l1l11l11_opy_
def bstack111ll11lll_opy_(test, bstack111l1lllll_opy_, bstack111l11l1_opy_, result, call, outcome, bstack111ll111l1_opy_):
    file_path = os.path.relpath(test.fspath.strpath, start=os.getcwd())
    hook_type = bstack111l1lllll_opy_[bstack111ll1l_opy_ (u"࠭ࡨࡰࡱ࡮ࡣࡹࡿࡰࡦࠩᑐ")]
    hook_name = bstack111l1lllll_opy_[bstack111ll1l_opy_ (u"ࠧࡩࡱࡲ࡯ࡤࡴࡡ࡮ࡧࠪᑑ")]
    hook_data = {
        bstack111ll1l_opy_ (u"ࠨࡷࡸ࡭ࡩ࠭ᑒ"): bstack111l1lllll_opy_[bstack111ll1l_opy_ (u"ࠩࡸࡹ࡮ࡪࠧᑓ")],
        bstack111ll1l_opy_ (u"ࠪࡸࡾࡶࡥࠨᑔ"): bstack111ll1l_opy_ (u"ࠫ࡭ࡵ࡯࡬ࠩᑕ"),
        bstack111ll1l_opy_ (u"ࠬࡴࡡ࡮ࡧࠪᑖ"): bstack111ll1l_opy_ (u"࠭ࡻࡾࠩᑗ").format(bstack11ll1llll1_opy_(hook_name)),
        bstack111ll1l_opy_ (u"ࠧࡣࡱࡧࡽࠬᑘ"): {
            bstack111ll1l_opy_ (u"ࠨ࡮ࡤࡲ࡬࠭ᑙ"): bstack111ll1l_opy_ (u"ࠩࡳࡽࡹ࡮࡯࡯ࠩᑚ"),
            bstack111ll1l_opy_ (u"ࠪࡧࡴࡪࡥࠨᑛ"): None
        },
        bstack111ll1l_opy_ (u"ࠫࡸࡩ࡯ࡱࡧࠪᑜ"): test.name,
        bstack111ll1l_opy_ (u"ࠬࡹࡣࡰࡲࡨࡷࠬᑝ"): bstack1l11lll1l_opy_.bstack11l11111ll_opy_(test, hook_name),
        bstack111ll1l_opy_ (u"࠭ࡦࡪ࡮ࡨࡣࡳࡧ࡭ࡦࠩᑞ"): file_path,
        bstack111ll1l_opy_ (u"ࠧ࡭ࡱࡦࡥࡹ࡯࡯࡯ࠩᑟ"): file_path,
        bstack111ll1l_opy_ (u"ࠨࡴࡨࡷࡺࡲࡴࠨᑠ"): bstack111ll1l_opy_ (u"ࠩࡳࡩࡳࡪࡩ࡯ࡩࠪᑡ"),
        bstack111ll1l_opy_ (u"ࠪࡺࡨࡥࡦࡪ࡮ࡨࡴࡦࡺࡨࠨᑢ"): file_path,
        bstack111ll1l_opy_ (u"ࠫࡸࡺࡡࡳࡶࡨࡨࡤࡧࡴࠨᑣ"): bstack111l1lllll_opy_[bstack111ll1l_opy_ (u"ࠬࡹࡴࡢࡴࡷࡩࡩࡥࡡࡵࠩᑤ")],
        bstack111ll1l_opy_ (u"࠭ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࠩᑥ"): bstack111ll1l_opy_ (u"ࠧࡑࡻࡷࡩࡸࡺ࠭ࡤࡷࡦࡹࡲࡨࡥࡳࠩᑦ") if bstack111ll111ll_opy_ == bstack111ll1l_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴ࠮ࡤࡧࡨࠬᑧ") else bstack111ll1l_opy_ (u"ࠩࡓࡽࡹ࡫ࡳࡵࠩᑨ"),
        bstack111ll1l_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡠࡶࡼࡴࡪ࠭ᑩ"): hook_type
    }
    bstack111lll11ll_opy_ = bstack111l1llll1_opy_(_111llllll1_opy_.get(test.nodeid, None))
    if bstack111lll11ll_opy_:
        hook_data[bstack111ll1l_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳࡥࡩࡥࠩᑪ")] = bstack111lll11ll_opy_
    if result:
        hook_data[bstack111ll1l_opy_ (u"ࠬࡸࡥࡴࡷ࡯ࡸࠬᑫ")] = result.outcome
        hook_data[bstack111ll1l_opy_ (u"࠭ࡤࡶࡴࡤࡸ࡮ࡵ࡮ࡠ࡫ࡱࡣࡲࡹࠧᑬ")] = result.duration * 1000
        hook_data[bstack111ll1l_opy_ (u"ࠧࡧ࡫ࡱ࡭ࡸ࡮ࡥࡥࡡࡤࡸࠬᑭ")] = bstack111l1lllll_opy_[bstack111ll1l_opy_ (u"ࠨࡨ࡬ࡲ࡮ࡹࡨࡦࡦࡢࡥࡹ࠭ᑮ")]
        if result.failed:
            hook_data[bstack111ll1l_opy_ (u"ࠩࡩࡥ࡮ࡲࡵࡳࡧࡢࡸࡾࡶࡥࠨᑯ")] = bstack1l11lll1l_opy_.bstack1l11ll1l1l_opy_(call.excinfo.typename)
            hook_data[bstack111ll1l_opy_ (u"ࠪࡪࡦ࡯࡬ࡶࡴࡨࠫᑰ")] = bstack1l11lll1l_opy_.bstack11l111l1l1_opy_(call.excinfo, result)
    if outcome:
        hook_data[bstack111ll1l_opy_ (u"ࠫࡷ࡫ࡳࡶ࡮ࡷࠫᑱ")] = bstack1l1l111111_opy_(outcome)
        hook_data[bstack111ll1l_opy_ (u"ࠬࡪࡵࡳࡣࡷ࡭ࡴࡴ࡟ࡪࡰࡢࡱࡸ࠭ᑲ")] = 100
        hook_data[bstack111ll1l_opy_ (u"࠭ࡦࡪࡰ࡬ࡷ࡭࡫ࡤࡠࡣࡷࠫᑳ")] = bstack111l1lllll_opy_[bstack111ll1l_opy_ (u"ࠧࡧ࡫ࡱ࡭ࡸ࡮ࡥࡥࡡࡤࡸࠬᑴ")]
        if hook_data[bstack111ll1l_opy_ (u"ࠨࡴࡨࡷࡺࡲࡴࠨᑵ")] == bstack111ll1l_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩᑶ"):
            hook_data[bstack111ll1l_opy_ (u"ࠪࡪࡦ࡯࡬ࡶࡴࡨࡣࡹࡿࡰࡦࠩᑷ")] = bstack111ll1l_opy_ (u"࡚ࠫࡴࡨࡢࡰࡧࡰࡪࡪࡅࡳࡴࡲࡶࠬᑸ")  # bstack11l11111l1_opy_
            hook_data[bstack111ll1l_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡸࡶࡪ࠭ᑹ")] = [{bstack111ll1l_opy_ (u"࠭ࡢࡢࡥ࡮ࡸࡷࡧࡣࡦࠩᑺ"): [bstack111ll1l_opy_ (u"ࠧࡴࡱࡰࡩࠥ࡫ࡲࡳࡱࡵࠫᑻ")]}]
    if bstack111ll111l1_opy_:
        hook_data[bstack111ll1l_opy_ (u"ࠨࡴࡨࡷࡺࡲࡴࠨᑼ")] = bstack111ll111l1_opy_.result
        hook_data[bstack111ll1l_opy_ (u"ࠩࡧࡹࡷࡧࡴࡪࡱࡱࡣ࡮ࡴ࡟࡮ࡵࠪᑽ")] = bstack1l11lll1l1_opy_(bstack111l1lllll_opy_[bstack111ll1l_opy_ (u"ࠪࡷࡹࡧࡲࡵࡧࡧࡣࡦࡺࠧᑾ")], bstack111l1lllll_opy_[bstack111ll1l_opy_ (u"ࠫ࡫࡯࡮ࡪࡵ࡫ࡩࡩࡥࡡࡵࠩᑿ")])
        hook_data[bstack111ll1l_opy_ (u"ࠬ࡬ࡩ࡯࡫ࡶ࡬ࡪࡪ࡟ࡢࡶࠪᒀ")] = bstack111l1lllll_opy_[bstack111ll1l_opy_ (u"࠭ࡦࡪࡰ࡬ࡷ࡭࡫ࡤࡠࡣࡷࠫᒁ")]
        if hook_data[bstack111ll1l_opy_ (u"ࠧࡳࡧࡶࡹࡱࡺࠧᒂ")] == bstack111ll1l_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨᒃ"):
            hook_data[bstack111ll1l_opy_ (u"ࠩࡩࡥ࡮ࡲࡵࡳࡧࡢࡸࡾࡶࡥࠨᒄ")] = bstack1l11lll1l_opy_.bstack1l11ll1l1l_opy_(bstack111ll111l1_opy_.exception_type)
            hook_data[bstack111ll1l_opy_ (u"ࠪࡪࡦ࡯࡬ࡶࡴࡨࠫᒅ")] = [{bstack111ll1l_opy_ (u"ࠫࡧࡧࡣ࡬ࡶࡵࡥࡨ࡫ࠧᒆ"): bstack1l11ll1l11_opy_(bstack111ll111l1_opy_.exception)}]
    return hook_data
def bstack111ll1l1ll_opy_(test, bstack111ll11l1l_opy_, bstack111l11l1_opy_, result=None, call=None, outcome=None):
    bstack11l1l11l11_opy_ = bstack11l1111111_opy_(test, bstack111ll11l1l_opy_, result, call, bstack111l11l1_opy_, outcome)
    driver = getattr(test, bstack111ll1l_opy_ (u"ࠬࡥࡤࡳ࡫ࡹࡩࡷ࠭ᒇ"), None)
    if bstack111l11l1_opy_ == bstack111ll1l_opy_ (u"࠭ࡔࡦࡵࡷࡖࡺࡴࡓࡵࡣࡵࡸࡪࡪࠧᒈ") and driver:
        bstack11l1l11l11_opy_[bstack111ll1l_opy_ (u"ࠧࡪࡰࡷࡩ࡬ࡸࡡࡵ࡫ࡲࡲࡸ࠭ᒉ")] = bstack1l11lll1l_opy_.bstack11l1111lll_opy_(driver)
    if bstack111l11l1_opy_ == bstack111ll1l_opy_ (u"ࠨࡖࡨࡷࡹࡘࡵ࡯ࡕ࡮࡭ࡵࡶࡥࡥࠩᒊ"):
        bstack111l11l1_opy_ = bstack111ll1l_opy_ (u"ࠩࡗࡩࡸࡺࡒࡶࡰࡉ࡭ࡳ࡯ࡳࡩࡧࡧࠫᒋ")
    bstack11l11lllll_opy_ = {
        bstack111ll1l_opy_ (u"ࠪࡩࡻ࡫࡮ࡵࡡࡷࡽࡵ࡫ࠧᒌ"): bstack111l11l1_opy_,
        bstack111ll1l_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳ࠭ᒍ"): bstack11l1l11l11_opy_
    }
    bstack1l11lll1l_opy_.bstack11l11lll11_opy_(bstack11l11lllll_opy_)
def bstack111ll11111_opy_(test, bstack111ll11l1l_opy_, bstack111l11l1_opy_, result=None, call=None, outcome=None, bstack111ll111l1_opy_=None):
    hook_data = bstack111ll11lll_opy_(test, bstack111ll11l1l_opy_, bstack111l11l1_opy_, result, call, outcome, bstack111ll111l1_opy_)
    bstack11l11lllll_opy_ = {
        bstack111ll1l_opy_ (u"ࠬ࡫ࡶࡦࡰࡷࡣࡹࡿࡰࡦࠩᒎ"): bstack111l11l1_opy_,
        bstack111ll1l_opy_ (u"࠭ࡨࡰࡱ࡮ࡣࡷࡻ࡮ࠨᒏ"): hook_data
    }
    bstack1l11lll1l_opy_.bstack11l11lll11_opy_(bstack11l11lllll_opy_)
def bstack111l1llll1_opy_(bstack111ll11l1l_opy_):
    if not bstack111ll11l1l_opy_:
        return None
    if bstack111ll11l1l_opy_.get(bstack111ll1l_opy_ (u"ࠧࡵࡧࡶࡸࡤࡪࡡࡵࡣࠪᒐ"), None):
        return getattr(bstack111ll11l1l_opy_[bstack111ll1l_opy_ (u"ࠨࡶࡨࡷࡹࡥࡤࡢࡶࡤࠫᒑ")], bstack111ll1l_opy_ (u"ࠩࡸࡹ࡮ࡪࠧᒒ"), None)
    return bstack111ll11l1l_opy_.get(bstack111ll1l_opy_ (u"ࠪࡹࡺ࡯ࡤࠨᒓ"), None)
@pytest.fixture(autouse=True)
def second_fixture(caplog, request):
    yield
    try:
        if not bstack1l11lll1l_opy_.on():
            return
        places = [bstack111ll1l_opy_ (u"ࠫࡸ࡫ࡴࡶࡲࠪᒔ"), bstack111ll1l_opy_ (u"ࠬࡩࡡ࡭࡮ࠪᒕ"), bstack111ll1l_opy_ (u"࠭ࡴࡦࡣࡵࡨࡴࡽ࡮ࠨᒖ")]
        bstack11l11llll1_opy_ = []
        for bstack111ll1llll_opy_ in places:
            records = caplog.get_records(bstack111ll1llll_opy_)
            bstack111lllll11_opy_ = bstack111ll1l_opy_ (u"ࠧࡵࡧࡶࡸࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧᒗ") if bstack111ll1llll_opy_ == bstack111ll1l_opy_ (u"ࠨࡥࡤࡰࡱ࠭ᒘ") else bstack111ll1l_opy_ (u"ࠩ࡫ࡳࡴࡱ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩᒙ")
            bstack111lllll1l_opy_ = request.node.nodeid + (bstack111ll1l_opy_ (u"ࠪࠫᒚ") if bstack111ll1llll_opy_ == bstack111ll1l_opy_ (u"ࠫࡨࡧ࡬࡭ࠩᒛ") else bstack111ll1l_opy_ (u"ࠬ࠳ࠧᒜ") + bstack111ll1llll_opy_)
            bstack111ll1111l_opy_ = bstack111l1llll1_opy_(_111llllll1_opy_.get(bstack111lllll1l_opy_, None))
            if not bstack111ll1111l_opy_:
                continue
            for record in records:
                if bstack1l1l1l11l1_opy_(record.message):
                    continue
                bstack11l11llll1_opy_.append({
                    bstack111ll1l_opy_ (u"࠭ࡴࡪ࡯ࡨࡷࡹࡧ࡭ࡱࠩᒝ"): datetime.datetime.utcfromtimestamp(record.created).isoformat() + bstack111ll1l_opy_ (u"࡛ࠧࠩᒞ"),
                    bstack111ll1l_opy_ (u"ࠨ࡮ࡨࡺࡪࡲࠧᒟ"): record.levelname,
                    bstack111ll1l_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪᒠ"): record.message,
                    bstack111lllll11_opy_: bstack111ll1111l_opy_
                })
        if len(bstack11l11llll1_opy_) > 0:
            bstack1l11lll1l_opy_.bstack11l111l1ll_opy_(bstack11l11llll1_opy_)
    except Exception as err:
        print(bstack111ll1l_opy_ (u"ࠪࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡶࡩࡨࡵ࡮ࡥࡡࡩ࡭ࡽࡺࡵࡳࡧ࠽ࠤࢀࢃࠧᒡ"), str(err))
def bstack111lllllll_opy_(driver_command, response):
    if driver_command == bstack111ll1l_opy_ (u"ࠫࡸࡩࡲࡦࡧࡱࡷ࡭ࡵࡴࠨᒢ"):
        bstack1l11lll1l_opy_.bstack11l111l11l_opy_({
            bstack111ll1l_opy_ (u"ࠬ࡯࡭ࡢࡩࡨࠫᒣ"): response[bstack111ll1l_opy_ (u"࠭ࡶࡢ࡮ࡸࡩࠬᒤ")],
            bstack111ll1l_opy_ (u"ࠧࡵࡧࡶࡸࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧᒥ"): store[bstack111ll1l_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡࡷࡩࡸࡺ࡟ࡶࡷ࡬ࡨࠬᒦ")]
        })
def bstack11l11lll1_opy_():
    global bstack1lll1l11l1_opy_
    bstack1l11lll1l_opy_.bstack11l1111l11_opy_()
    for driver in bstack1lll1l11l1_opy_:
        try:
            driver.quit()
        except Exception as e:
            pass
def bstack11ll11l11_opy_(self, *args, **kwargs):
    bstack1111llll_opy_ = bstack11lll1l11_opy_(self, *args, **kwargs)
    bstack1l11lll1l_opy_.bstack1lll1111l_opy_(self)
    return bstack1111llll_opy_
def bstack111ll1ll1_opy_(framework_name):
    global bstack111111lll_opy_
    global bstack1ll1l1ll1l_opy_
    bstack111111lll_opy_ = framework_name
    logger.info(bstack1l111ll1l_opy_.format(bstack111111lll_opy_.split(bstack111ll1l_opy_ (u"ࠩ࠰ࠫᒧ"))[0]))
    try:
        from selenium import webdriver
        from selenium.webdriver.common.service import Service
        from selenium.webdriver.remote.webdriver import WebDriver
        if bstack1l1l1l11ll_opy_():
            Service.start = bstack11l1l11l1_opy_
            Service.stop = bstack11l111ll_opy_
            webdriver.Remote.__init__ = bstack11lll1l1_opy_
            webdriver.Remote.get = bstack11ll1l111_opy_
            if not isinstance(os.getenv(bstack111ll1l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡓ࡝࡙ࡋࡓࡕࡡࡓࡅࡗࡇࡌࡍࡇࡏࠫᒨ")), str):
                return
            WebDriver.close = bstack11l1l1ll_opy_
            WebDriver.quit = bstack11l1l11ll_opy_
            WebDriver.getAccessibilityResults = getAccessibilityResults
            WebDriver.getAccessibilityResultsSummary = getAccessibilityResultsSummary
        if not bstack1l1l1l11ll_opy_() and bstack1l11lll1l_opy_.on():
            webdriver.Remote.__init__ = bstack11ll11l11_opy_
        bstack1ll1l1ll1l_opy_ = True
    except Exception as e:
        pass
    bstack1lll1l111l_opy_()
    if os.environ.get(bstack111ll1l_opy_ (u"ࠫࡘࡋࡌࡆࡐࡌ࡙ࡒࡥࡏࡓࡡࡓࡐࡆ࡟ࡗࡓࡋࡊࡌ࡙ࡥࡉࡏࡕࡗࡅࡑࡒࡅࡅࠩᒩ")):
        bstack1ll1l1ll1l_opy_ = eval(os.environ.get(bstack111ll1l_opy_ (u"࡙ࠬࡅࡍࡇࡑࡍ࡚ࡓ࡟ࡐࡔࡢࡔࡑࡇ࡙ࡘࡔࡌࡋࡍ࡚࡟ࡊࡐࡖࡘࡆࡒࡌࡆࡆࠪᒪ")))
    if not bstack1ll1l1ll1l_opy_:
        bstack1l1lll111_opy_(bstack111ll1l_opy_ (u"ࠨࡐࡢࡥ࡮ࡥ࡬࡫ࡳࠡࡰࡲࡸࠥ࡯࡮ࡴࡶࡤࡰࡱ࡫ࡤࠣᒫ"), bstack11111llll_opy_)
    if bstack1l1l1l1l_opy_():
        try:
            from selenium.webdriver.remote.remote_connection import RemoteConnection
            RemoteConnection._get_proxy_url = bstack1l11l111_opy_
        except Exception as e:
            logger.error(bstack1ll1l1ll1_opy_.format(str(e)))
    if bstack111ll1l_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺࠧᒬ") in str(framework_name).lower():
        if not bstack1l1l1l11ll_opy_():
            return
        try:
            from pytest_selenium import pytest_selenium
            from _pytest.config import Config
            pytest_selenium.pytest_report_header = bstack1111lllll_opy_
            from pytest_selenium.drivers import browserstack
            browserstack.pytest_selenium_runtest_makereport = bstack111l11lll_opy_
            Config.getoption = bstack1l11111l_opy_
        except Exception as e:
            pass
        try:
            from pytest_bdd import reporting
            reporting.runtest_makereport = bstack1l11l1111_opy_
        except Exception as e:
            pass
def bstack11l1l11ll_opy_(self):
    global bstack111111lll_opy_
    global bstack1l1l1l1l1_opy_
    global bstack1ll1l111ll_opy_
    try:
        if bstack111ll1l_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࠨᒭ") in bstack111111lll_opy_ and self.session_id != None and bstack11l11l11_opy_(threading.current_thread(), bstack111ll1l_opy_ (u"ࠩࡷࡩࡸࡺࡓࡵࡣࡷࡹࡸ࠭ᒮ"), bstack111ll1l_opy_ (u"ࠪࠫᒯ")) != bstack111ll1l_opy_ (u"ࠫࡸࡱࡩࡱࡲࡨࡨࠬᒰ"):
            bstack111l11l1l_opy_ = bstack111ll1l_opy_ (u"ࠬࡶࡡࡴࡵࡨࡨࠬᒱ") if len(threading.current_thread().bstackTestErrorMessages) == 0 else bstack111ll1l_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭ᒲ")
            bstack11ll11ll_opy_ = bstack1l1ll1111_opy_(bstack111ll1l_opy_ (u"ࠧࡴࡧࡷࡗࡪࡹࡳࡪࡱࡱࡗࡹࡧࡴࡶࡵࠪᒳ"), bstack111ll1l_opy_ (u"ࠨࠩᒴ"), bstack111l11l1l_opy_, bstack111ll1l_opy_ (u"ࠩ࠯ࠤࠬᒵ").join(
                threading.current_thread().bstackTestErrorMessages), bstack111ll1l_opy_ (u"ࠪࠫᒶ"), bstack111ll1l_opy_ (u"ࠫࠬᒷ"))
            if self != None:
                self.execute_script(bstack11ll11ll_opy_)
    except Exception as e:
        logger.debug(bstack111ll1l_opy_ (u"ࠧࡋࡲࡳࡱࡵࠤࡼ࡮ࡩ࡭ࡧࠣࡱࡦࡸ࡫ࡪࡰࡪࠤࡸࡺࡡࡵࡷࡶ࠾ࠥࠨᒸ") + str(e))
    bstack1ll1l111ll_opy_(self)
    self.session_id = None
def bstack11lll1l1_opy_(self, command_executor,
             desired_capabilities=None, browser_profile=None, proxy=None,
             keep_alive=True, file_detector=None, options=None):
    global CONFIG
    global bstack1l1l1l1l1_opy_
    global bstack1111llll1_opy_
    global bstack1l11ll1l_opy_
    global bstack111111lll_opy_
    global bstack11lll1l11_opy_
    global bstack1lll1l11l1_opy_
    global bstack1ll11111_opy_
    global bstack11l11llll_opy_
    global bstack111ll1lll1_opy_
    CONFIG[bstack111ll1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡘࡊࡋࠨᒹ")] = str(bstack111111lll_opy_) + str(__version__)
    command_executor = bstack111111111_opy_(bstack1ll11111_opy_)
    logger.debug(bstack11ll1l11_opy_.format(command_executor))
    proxy = bstack111l1lll_opy_(CONFIG, proxy)
    bstack1lll1l11l_opy_ = 0
    try:
        if bstack1l11ll1l_opy_ is True:
            bstack1lll1l11l_opy_ = int(os.environ.get(bstack111ll1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡐࡍࡃࡗࡊࡔࡘࡍࡠࡋࡑࡈࡊ࡞ࠧᒺ")))
    except:
        bstack1lll1l11l_opy_ = 0
    bstack1llll1111l_opy_ = bstack1lllllll1l_opy_(CONFIG, bstack1lll1l11l_opy_)
    logger.debug(bstack1ll1ll1l1_opy_.format(str(bstack1llll1111l_opy_)))
    if bstack111ll1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡌࡰࡥࡤࡰࠬᒻ") in CONFIG and CONFIG[bstack111ll1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡍࡱࡦࡥࡱ࠭ᒼ")]:
        bstack11l11111l_opy_(bstack1llll1111l_opy_, bstack11l11llll_opy_)
    if desired_capabilities:
        bstack1lll1lll_opy_ = bstack1ll1l1111l_opy_(desired_capabilities)
        bstack1lll1lll_opy_[bstack111ll1l_opy_ (u"ࠪࡹࡸ࡫ࡗ࠴ࡅࠪᒽ")] = bstack1111lll1_opy_(CONFIG)
        bstack111ll111l_opy_ = bstack1lllllll1l_opy_(bstack1lll1lll_opy_)
        if bstack111ll111l_opy_:
            bstack1llll1111l_opy_ = update(bstack111ll111l_opy_, bstack1llll1111l_opy_)
        desired_capabilities = None
    if options:
        bstack1lll1111_opy_(options, bstack1llll1111l_opy_)
    if not options:
        options = bstack1ll11111l_opy_(bstack1llll1111l_opy_)
    if bstack111l1l11l_opy_.bstack1lll1l11_opy_(CONFIG, bstack1lll1l11l_opy_) and bstack111l1l11l_opy_.bstack1ll1ll1l_opy_(bstack1llll1111l_opy_, options):
        bstack111ll1lll1_opy_ = True
        bstack111l1l11l_opy_.set_capabilities(bstack1llll1111l_opy_, CONFIG)
    if proxy and bstack1lllll1l1l_opy_() >= version.parse(bstack111ll1l_opy_ (u"ࠫ࠹࠴࠱࠱࠰࠳ࠫᒾ")):
        options.proxy(proxy)
    if options and bstack1lllll1l1l_opy_() >= version.parse(bstack111ll1l_opy_ (u"ࠬ࠹࠮࠹࠰࠳ࠫᒿ")):
        desired_capabilities = None
    if (
            not options and not desired_capabilities
    ) or (
            bstack1lllll1l1l_opy_() < version.parse(bstack111ll1l_opy_ (u"࠭࠳࠯࠺࠱࠴ࠬᓀ")) and not desired_capabilities
    ):
        desired_capabilities = {}
        desired_capabilities.update(bstack1llll1111l_opy_)
    logger.info(bstack1lll1l1l1_opy_)
    if bstack1lllll1l1l_opy_() >= version.parse(bstack111ll1l_opy_ (u"ࠧ࠵࠰࠴࠴࠳࠶ࠧᓁ")):
        bstack11lll1l11_opy_(self, command_executor=command_executor,
                  options=options, keep_alive=keep_alive, file_detector=file_detector)
    elif bstack1lllll1l1l_opy_() >= version.parse(bstack111ll1l_opy_ (u"ࠨ࠵࠱࠼࠳࠶ࠧᓂ")):
        bstack11lll1l11_opy_(self, command_executor=command_executor,
                  desired_capabilities=desired_capabilities, options=options,
                  browser_profile=browser_profile, proxy=proxy,
                  keep_alive=keep_alive, file_detector=file_detector)
    elif bstack1lllll1l1l_opy_() >= version.parse(bstack111ll1l_opy_ (u"ࠩ࠵࠲࠺࠹࠮࠱ࠩᓃ")):
        bstack11lll1l11_opy_(self, command_executor=command_executor,
                  desired_capabilities=desired_capabilities,
                  browser_profile=browser_profile, proxy=proxy,
                  keep_alive=keep_alive, file_detector=file_detector)
    else:
        bstack11lll1l11_opy_(self, command_executor=command_executor,
                  desired_capabilities=desired_capabilities,
                  browser_profile=browser_profile, proxy=proxy,
                  keep_alive=keep_alive)
    try:
        bstack11ll1111l_opy_ = bstack111ll1l_opy_ (u"ࠪࠫᓄ")
        if bstack1lllll1l1l_opy_() >= version.parse(bstack111ll1l_opy_ (u"ࠫ࠹࠴࠰࠯࠲ࡥ࠵ࠬᓅ")):
            bstack11ll1111l_opy_ = self.caps.get(bstack111ll1l_opy_ (u"ࠧࡵࡰࡵ࡫ࡰࡥࡱࡎࡵࡣࡗࡵࡰࠧᓆ"))
        else:
            bstack11ll1111l_opy_ = self.capabilities.get(bstack111ll1l_opy_ (u"ࠨ࡯ࡱࡶ࡬ࡱࡦࡲࡈࡶࡤࡘࡶࡱࠨᓇ"))
        if bstack11ll1111l_opy_:
            if bstack1lllll1l1l_opy_() <= version.parse(bstack111ll1l_opy_ (u"ࠧ࠴࠰࠴࠷࠳࠶ࠧᓈ")):
                self.command_executor._url = bstack111ll1l_opy_ (u"ࠣࡪࡷࡸࡵࡀ࠯࠰ࠤᓉ") + bstack1ll11111_opy_ + bstack111ll1l_opy_ (u"ࠤ࠽࠼࠵࠵ࡷࡥ࠱࡫ࡹࡧࠨᓊ")
            else:
                self.command_executor._url = bstack111ll1l_opy_ (u"ࠥ࡬ࡹࡺࡰࡴ࠼࠲࠳ࠧᓋ") + bstack11ll1111l_opy_ + bstack111ll1l_opy_ (u"ࠦ࠴ࡽࡤ࠰ࡪࡸࡦࠧᓌ")
            logger.debug(bstack111l11ll1_opy_.format(bstack11ll1111l_opy_))
        else:
            logger.debug(bstack1ll1l11l1_opy_.format(bstack111ll1l_opy_ (u"ࠧࡕࡰࡵ࡫ࡰࡥࡱࠦࡈࡶࡤࠣࡲࡴࡺࠠࡧࡱࡸࡲࡩࠨᓍ")))
    except Exception as e:
        logger.debug(bstack1ll1l11l1_opy_.format(e))
    bstack1l1l1l1l1_opy_ = self.session_id
    if bstack111ll1l_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭ᓎ") in bstack111111lll_opy_:
        threading.current_thread().bstack111l1111_opy_ = self.session_id
        threading.current_thread().bstackSessionDriver = self
        threading.current_thread().bstackTestErrorMessages = []
        bstack1l11lll1l_opy_.bstack1lll1111l_opy_(self)
    bstack1lll1l11l1_opy_.append(self)
    if bstack111ll1l_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪᓏ") in CONFIG and bstack111ll1l_opy_ (u"ࠨࡵࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪ࠭ᓐ") in CONFIG[bstack111ll1l_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬᓑ")][bstack1lll1l11l_opy_]:
        bstack1111llll1_opy_ = CONFIG[bstack111ll1l_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ᓒ")][bstack1lll1l11l_opy_][bstack111ll1l_opy_ (u"ࠫࡸ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠩᓓ")]
    logger.debug(bstack11lll11l_opy_.format(bstack1l1l1l1l1_opy_))
def bstack11ll1l111_opy_(self, url):
    global bstack1ll11l1l1_opy_
    global CONFIG
    try:
        bstack1ll1l1l111_opy_(url, CONFIG, logger)
    except Exception as err:
        logger.debug(bstack111llll1_opy_.format(str(err)))
    try:
        bstack1ll11l1l1_opy_(self, url)
    except Exception as e:
        try:
            bstack11lll11l1_opy_ = str(e)
            if any(err_msg in bstack11lll11l1_opy_ for err_msg in bstack1lll1llll1_opy_):
                bstack1ll1l1l111_opy_(url, CONFIG, logger, True)
        except Exception as err:
            logger.debug(bstack111llll1_opy_.format(str(err)))
        raise e
def bstack1lll11ll_opy_(item, when):
    global bstack1l1l1ll1_opy_
    try:
        bstack1l1l1ll1_opy_(item, when)
    except Exception as e:
        pass
def bstack1l11l1111_opy_(item, call, rep):
    global bstack1ll1ll1lll_opy_
    global bstack1lll1l11l1_opy_
    name = bstack111ll1l_opy_ (u"ࠬ࠭ᓔ")
    try:
        if rep.when == bstack111ll1l_opy_ (u"࠭ࡣࡢ࡮࡯ࠫᓕ"):
            bstack1l1l1l1l1_opy_ = threading.current_thread().bstack111l1111_opy_
            bstack111ll11l11_opy_ = item.config.getoption(bstack111ll1l_opy_ (u"ࠧࡴ࡭࡬ࡴࡘ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠩᓖ"))
            try:
                if (str(bstack111ll11l11_opy_).lower() != bstack111ll1l_opy_ (u"ࠨࡶࡵࡹࡪ࠭ᓗ")):
                    name = str(rep.nodeid)
                    bstack11ll11ll_opy_ = bstack1l1ll1111_opy_(bstack111ll1l_opy_ (u"ࠩࡶࡩࡹ࡙ࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠪᓘ"), name, bstack111ll1l_opy_ (u"ࠪࠫᓙ"), bstack111ll1l_opy_ (u"ࠫࠬᓚ"), bstack111ll1l_opy_ (u"ࠬ࠭ᓛ"), bstack111ll1l_opy_ (u"࠭ࠧᓜ"))
                    for driver in bstack1lll1l11l1_opy_:
                        if bstack1l1l1l1l1_opy_ == driver.session_id:
                            driver.execute_script(bstack11ll11ll_opy_)
            except Exception as e:
                logger.debug(bstack111ll1l_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡶࡩࡹࡺࡩ࡯ࡩࠣࡷࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠡࡨࡲࡶࠥࡶࡹࡵࡧࡶࡸ࠲ࡨࡤࡥࠢࡶࡩࡸࡹࡩࡰࡰ࠽ࠤࢀࢃࠧᓝ").format(str(e)))
            try:
                bstack1lll111ll1_opy_(rep.outcome.lower())
                if rep.outcome.lower() != bstack111ll1l_opy_ (u"ࠨࡵ࡮࡭ࡵࡶࡥࡥࠩᓞ"):
                    status = bstack111ll1l_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩᓟ") if rep.outcome.lower() == bstack111ll1l_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪᓠ") else bstack111ll1l_opy_ (u"ࠫࡵࡧࡳࡴࡧࡧࠫᓡ")
                    reason = bstack111ll1l_opy_ (u"ࠬ࠭ᓢ")
                    if status == bstack111ll1l_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭ᓣ"):
                        reason = rep.longrepr.reprcrash.message
                        if (not threading.current_thread().bstackTestErrorMessages):
                            threading.current_thread().bstackTestErrorMessages = []
                        threading.current_thread().bstackTestErrorMessages.append(reason)
                    level = bstack111ll1l_opy_ (u"ࠧࡪࡰࡩࡳࠬᓤ") if status == bstack111ll1l_opy_ (u"ࠨࡲࡤࡷࡸ࡫ࡤࠨᓥ") else bstack111ll1l_opy_ (u"ࠩࡨࡶࡷࡵࡲࠨᓦ")
                    data = name + bstack111ll1l_opy_ (u"ࠪࠤࡵࡧࡳࡴࡧࡧࠥࠬᓧ") if status == bstack111ll1l_opy_ (u"ࠫࡵࡧࡳࡴࡧࡧࠫᓨ") else name + bstack111ll1l_opy_ (u"ࠬࠦࡦࡢ࡫࡯ࡩࡩࠧࠠࠨᓩ") + reason
                    bstack1lll11l11l_opy_ = bstack1l1ll1111_opy_(bstack111ll1l_opy_ (u"࠭ࡡ࡯ࡰࡲࡸࡦࡺࡥࠨᓪ"), bstack111ll1l_opy_ (u"ࠧࠨᓫ"), bstack111ll1l_opy_ (u"ࠨࠩᓬ"), bstack111ll1l_opy_ (u"ࠩࠪᓭ"), level, data)
                    for driver in bstack1lll1l11l1_opy_:
                        if bstack1l1l1l1l1_opy_ == driver.session_id:
                            driver.execute_script(bstack1lll11l11l_opy_)
            except Exception as e:
                logger.debug(bstack111ll1l_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥࡹࡥࡵࡶ࡬ࡲ࡬ࠦࡳࡦࡵࡶ࡭ࡴࡴࠠࡤࡱࡱࡸࡪࡾࡴࠡࡨࡲࡶࠥࡶࡹࡵࡧࡶࡸ࠲ࡨࡤࡥࠢࡶࡩࡸࡹࡩࡰࡰ࠽ࠤࢀࢃࠧᓮ").format(str(e)))
    except Exception as e:
        logger.debug(bstack111ll1l_opy_ (u"ࠫࡊࡸࡲࡰࡴࠣ࡭ࡳࠦࡧࡦࡶࡷ࡭ࡳ࡭ࠠࡴࡶࡤࡸࡪࠦࡩ࡯ࠢࡳࡽࡹ࡫ࡳࡵ࠯ࡥࡨࡩࠦࡴࡦࡵࡷࠤࡸࡺࡡࡵࡷࡶ࠾ࠥࢁࡽࠨᓯ").format(str(e)))
    bstack1ll1ll1lll_opy_(item, call, rep)
notset = Notset()
def bstack1l11111l_opy_(self, name: str, default=notset, skip: bool = False):
    global bstack1l1l11ll1_opy_
    if str(name).lower() == bstack111ll1l_opy_ (u"ࠬࡪࡲࡪࡸࡨࡶࠬᓰ"):
        return bstack111ll1l_opy_ (u"ࠨࡂࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࠧᓱ")
    else:
        return bstack1l1l11ll1_opy_(self, name, default, skip)
def bstack1l11l111_opy_(self):
    global CONFIG
    global bstack1111l1111_opy_
    try:
        proxy = bstack1l1ll11ll_opy_(CONFIG)
        if proxy:
            if proxy.endswith(bstack111ll1l_opy_ (u"ࠧ࠯ࡲࡤࡧࠬᓲ")):
                proxies = bstack1l1l1l111_opy_(proxy, bstack111111111_opy_())
                if len(proxies) > 0:
                    protocol, bstack1lllll1111_opy_ = proxies.popitem()
                    if bstack111ll1l_opy_ (u"ࠣ࠼࠲࠳ࠧᓳ") in bstack1lllll1111_opy_:
                        return bstack1lllll1111_opy_
                    else:
                        return bstack111ll1l_opy_ (u"ࠤ࡫ࡸࡹࡶ࠺࠰࠱ࠥᓴ") + bstack1lllll1111_opy_
            else:
                return proxy
    except Exception as e:
        logger.error(bstack111ll1l_opy_ (u"ࠥࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥࡹࡥࡵࡶ࡬ࡲ࡬ࠦࡰࡳࡱࡻࡽࠥࡻࡲ࡭ࠢ࠽ࠤࢀࢃࠢᓵ").format(str(e)))
    return bstack1111l1111_opy_(self)
def bstack1l1l1l1l_opy_():
    return (bstack111ll1l_opy_ (u"ࠫ࡭ࡺࡴࡱࡒࡵࡳࡽࡿࠧᓶ") in CONFIG or bstack111ll1l_opy_ (u"ࠬ࡮ࡴࡵࡲࡶࡔࡷࡵࡸࡺࠩᓷ") in CONFIG) and bstack1ll11l11l_opy_() and bstack1lllll1l1l_opy_() >= version.parse(
        bstack1llll11l1l_opy_)
def bstack11ll11ll1_opy_(self,
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
    global bstack1111llll1_opy_
    global bstack1l11ll1l_opy_
    global bstack111111lll_opy_
    CONFIG[bstack111ll1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡘࡊࡋࠨᓸ")] = str(bstack111111lll_opy_) + str(__version__)
    bstack1lll1l11l_opy_ = 0
    try:
        if bstack1l11ll1l_opy_ is True:
            bstack1lll1l11l_opy_ = int(os.environ.get(bstack111ll1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡐࡍࡃࡗࡊࡔࡘࡍࡠࡋࡑࡈࡊ࡞ࠧᓹ")))
    except:
        bstack1lll1l11l_opy_ = 0
    CONFIG[bstack111ll1l_opy_ (u"ࠣ࡫ࡶࡔࡱࡧࡹࡸࡴ࡬࡫࡭ࡺࠢᓺ")] = True
    bstack1llll1111l_opy_ = bstack1lllllll1l_opy_(CONFIG, bstack1lll1l11l_opy_)
    logger.debug(bstack1ll1ll1l1_opy_.format(str(bstack1llll1111l_opy_)))
    if CONFIG.get(bstack111ll1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡍࡱࡦࡥࡱ࠭ᓻ")):
        bstack11l11111l_opy_(bstack1llll1111l_opy_, bstack11l11llll_opy_)
    if bstack111ll1l_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ᓼ") in CONFIG and bstack111ll1l_opy_ (u"ࠫࡸ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠩᓽ") in CONFIG[bstack111ll1l_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨᓾ")][bstack1lll1l11l_opy_]:
        bstack1111llll1_opy_ = CONFIG[bstack111ll1l_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩᓿ")][bstack1lll1l11l_opy_][bstack111ll1l_opy_ (u"ࠧࡴࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠬᔀ")]
    import urllib
    import json
    bstack1ll1l111l1_opy_ = bstack111ll1l_opy_ (u"ࠨࡹࡶࡷ࠿࠵࠯ࡤࡦࡳ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡧࡴࡳ࠯ࡱ࡮ࡤࡽࡼࡸࡩࡨࡪࡷࡃࡨࡧࡰࡴ࠿ࠪᔁ") + urllib.parse.quote(json.dumps(bstack1llll1111l_opy_))
    browser = self.connect(bstack1ll1l111l1_opy_)
    return browser
def bstack1lll1l111l_opy_():
    global bstack1ll1l1ll1l_opy_
    try:
        from playwright._impl._browser_type import BrowserType
        BrowserType.launch = bstack11ll11ll1_opy_
        bstack1ll1l1ll1l_opy_ = True
    except Exception as e:
        pass
def bstack111llll1l1_opy_():
    global CONFIG
    global bstack111l1l1ll_opy_
    global bstack1ll11111_opy_
    global bstack11l11llll_opy_
    global bstack1l11ll1l_opy_
    CONFIG = json.loads(os.environ.get(bstack111ll1l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡅࡒࡒࡋࡏࡇࠨᔂ")))
    bstack111l1l1ll_opy_ = eval(os.environ.get(bstack111ll1l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡌࡗࡤࡇࡐࡑࡡࡄ࡙࡙ࡕࡍࡂࡖࡈࠫᔃ")))
    bstack1ll11111_opy_ = os.environ.get(bstack111ll1l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡌ࡚ࡈ࡟ࡖࡔࡏࠫᔄ"))
    bstack1llll1l11l_opy_(CONFIG, bstack111l1l1ll_opy_)
    bstack1l1l11l1l_opy_()
    global bstack11lll1l11_opy_
    global bstack1ll1l111ll_opy_
    global bstack1ll1l11111_opy_
    global bstack1l1l111ll_opy_
    global bstack11lll1l1l_opy_
    global bstack11l1llll_opy_
    global bstack1llllll1l1_opy_
    global bstack1ll11l1l1_opy_
    global bstack1111l1111_opy_
    global bstack1l1l11ll1_opy_
    global bstack1l1l1ll1_opy_
    global bstack1ll1ll1lll_opy_
    try:
        from selenium import webdriver
        from selenium.webdriver.remote.webdriver import WebDriver
        bstack11lll1l11_opy_ = webdriver.Remote.__init__
        bstack1ll1l111ll_opy_ = WebDriver.quit
        bstack1llllll1l1_opy_ = WebDriver.close
        bstack1ll11l1l1_opy_ = WebDriver.get
    except Exception as e:
        pass
    if (bstack111ll1l_opy_ (u"ࠬ࡮ࡴࡵࡲࡓࡶࡴࡾࡹࠨᔅ") in CONFIG or bstack111ll1l_opy_ (u"࠭ࡨࡵࡶࡳࡷࡕࡸ࡯ࡹࡻࠪᔆ") in CONFIG) and bstack1ll11l11l_opy_():
        if bstack1lllll1l1l_opy_() < version.parse(bstack1llll11l1l_opy_):
            logger.error(bstack1ll1lll1l1_opy_.format(bstack1lllll1l1l_opy_()))
        else:
            try:
                from selenium.webdriver.remote.remote_connection import RemoteConnection
                bstack1111l1111_opy_ = RemoteConnection._get_proxy_url
            except Exception as e:
                logger.error(bstack1ll1l1ll1_opy_.format(str(e)))
    try:
        from _pytest.config import Config
        bstack1l1l11ll1_opy_ = Config.getoption
        from _pytest import runner
        bstack1l1l1ll1_opy_ = runner._update_current_test_var
    except Exception as e:
        logger.warn(e, bstack11l11l1ll_opy_)
    try:
        from pytest_bdd import reporting
        bstack1ll1ll1lll_opy_ = reporting.runtest_makereport
    except Exception as e:
        logger.debug(bstack111ll1l_opy_ (u"ࠧࡑ࡮ࡨࡥࡸ࡫ࠠࡪࡰࡶࡸࡦࡲ࡬ࠡࡲࡼࡸࡪࡹࡴ࠮ࡤࡧࡨࠥࡺ࡯ࠡࡴࡸࡲࠥࡶࡹࡵࡧࡶࡸ࠲ࡨࡤࡥࠢࡷࡩࡸࡺࡳࠨᔇ"))
    bstack11l11llll_opy_ = CONFIG.get(bstack111ll1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࡌࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬᔈ"), {}).get(bstack111ll1l_opy_ (u"ࠩ࡯ࡳࡨࡧ࡬ࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫᔉ"))
    bstack1l11ll1l_opy_ = True
    bstack111ll1ll1_opy_(bstack11llllll_opy_)
if (bstack1l1l11ll1l_opy_()):
    bstack111llll1l1_opy_()
@bstack1l1lll11l1_opy_(class_method=False)
def bstack111llll1ll_opy_(hook_name, event, bstack111ll11ll1_opy_=None):
    if hook_name not in [bstack111ll1l_opy_ (u"ࠪࡷࡪࡺࡵࡱࡡࡩࡹࡳࡩࡴࡪࡱࡱࠫᔊ"), bstack111ll1l_opy_ (u"ࠫࡹ࡫ࡡࡳࡦࡲࡻࡳࡥࡦࡶࡰࡦࡸ࡮ࡵ࡮ࠨᔋ"), bstack111ll1l_opy_ (u"ࠬࡹࡥࡵࡷࡳࡣࡲࡵࡤࡶ࡮ࡨࠫᔌ"), bstack111ll1l_opy_ (u"࠭ࡴࡦࡣࡵࡨࡴࡽ࡮ࡠ࡯ࡲࡨࡺࡲࡥࠨᔍ"), bstack111ll1l_opy_ (u"ࠧࡴࡧࡷࡹࡵࡥࡣ࡭ࡣࡶࡷࠬᔎ"), bstack111ll1l_opy_ (u"ࠨࡶࡨࡥࡷࡪ࡯ࡸࡰࡢࡧࡱࡧࡳࡴࠩᔏ"), bstack111ll1l_opy_ (u"ࠩࡶࡩࡹࡻࡰࡠ࡯ࡨࡸ࡭ࡵࡤࠨᔐ"), bstack111ll1l_opy_ (u"ࠪࡸࡪࡧࡲࡥࡱࡺࡲࡤࡳࡥࡵࡪࡲࡨࠬᔑ")]:
        return
    node = store[bstack111ll1l_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤࡺࡥࡴࡶࡢ࡭ࡹ࡫࡭ࠨᔒ")]
    if hook_name in [bstack111ll1l_opy_ (u"ࠬࡹࡥࡵࡷࡳࡣࡲࡵࡤࡶ࡮ࡨࠫᔓ"), bstack111ll1l_opy_ (u"࠭ࡴࡦࡣࡵࡨࡴࡽ࡮ࡠ࡯ࡲࡨࡺࡲࡥࠨᔔ")]:
        node = store[bstack111ll1l_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠ࡯ࡲࡨࡺࡲࡥࡠ࡫ࡷࡩࡲ࠭ᔕ")]
    elif hook_name in [bstack111ll1l_opy_ (u"ࠨࡵࡨࡸࡺࡶ࡟ࡤ࡮ࡤࡷࡸ࠭ᔖ"), bstack111ll1l_opy_ (u"ࠩࡷࡩࡦࡸࡤࡰࡹࡱࡣࡨࡲࡡࡴࡵࠪᔗ")]:
        node = store[bstack111ll1l_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣࡨࡲࡡࡴࡵࡢ࡭ࡹ࡫࡭ࠨᔘ")]
    if event == bstack111ll1l_opy_ (u"ࠫࡧ࡫ࡦࡰࡴࡨࠫᔙ"):
        hook_type = bstack11ll1l1111_opy_(hook_name)
        uuid = uuid4().__str__()
        bstack111l1lllll_opy_ = {
            bstack111ll1l_opy_ (u"ࠬࡻࡵࡪࡦࠪᔚ"): uuid,
            bstack111ll1l_opy_ (u"࠭ࡳࡵࡣࡵࡸࡪࡪ࡟ࡢࡶࠪᔛ"): bstack1111ll111_opy_(),
            bstack111ll1l_opy_ (u"ࠧࡵࡻࡳࡩࠬᔜ"): bstack111ll1l_opy_ (u"ࠨࡪࡲࡳࡰ࠭ᔝ"),
            bstack111ll1l_opy_ (u"ࠩ࡫ࡳࡴࡱ࡟ࡵࡻࡳࡩࠬᔞ"): hook_type,
            bstack111ll1l_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡠࡰࡤࡱࡪ࠭ᔟ"): hook_name
        }
        store[bstack111ll1l_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤ࡮࡯ࡰ࡭ࡢࡹࡺ࡯ࡤࠨᔠ")].append(uuid)
        bstack111llll11l_opy_ = node.nodeid
        if hook_type == bstack111ll1l_opy_ (u"ࠬࡈࡅࡇࡑࡕࡉࡤࡋࡁࡄࡊࠪᔡ"):
            if not _111llllll1_opy_.get(bstack111llll11l_opy_, None):
                _111llllll1_opy_[bstack111llll11l_opy_] = {bstack111ll1l_opy_ (u"࠭ࡨࡰࡱ࡮ࡷࠬᔢ"): []}
            _111llllll1_opy_[bstack111llll11l_opy_][bstack111ll1l_opy_ (u"ࠧࡩࡱࡲ࡯ࡸ࠭ᔣ")].append(bstack111l1lllll_opy_[bstack111ll1l_opy_ (u"ࠨࡷࡸ࡭ࡩ࠭ᔤ")])
        _111llllll1_opy_[bstack111llll11l_opy_ + bstack111ll1l_opy_ (u"ࠩ࠰ࠫᔥ") + hook_name] = bstack111l1lllll_opy_
        bstack111ll11111_opy_(node, bstack111l1lllll_opy_, bstack111ll1l_opy_ (u"ࠪࡌࡴࡵ࡫ࡓࡷࡱࡗࡹࡧࡲࡵࡧࡧࠫᔦ"))
    elif event == bstack111ll1l_opy_ (u"ࠫࡦ࡬ࡴࡦࡴࠪᔧ"):
        bstack111ll1l1l1_opy_ = node.nodeid + bstack111ll1l_opy_ (u"ࠬ࠳ࠧᔨ") + hook_name
        _111llllll1_opy_[bstack111ll1l1l1_opy_][bstack111ll1l_opy_ (u"࠭ࡦࡪࡰ࡬ࡷ࡭࡫ࡤࡠࡣࡷࠫᔩ")] = bstack1111ll111_opy_()
        bstack11l111111l_opy_(_111llllll1_opy_[bstack111ll1l1l1_opy_][bstack111ll1l_opy_ (u"ࠧࡶࡷ࡬ࡨࠬᔪ")])
        bstack111ll11111_opy_(node, _111llllll1_opy_[bstack111ll1l1l1_opy_], bstack111ll1l_opy_ (u"ࠨࡊࡲࡳࡰࡘࡵ࡯ࡈ࡬ࡲ࡮ࡹࡨࡦࡦࠪᔫ"), bstack111ll111l1_opy_=bstack111ll11ll1_opy_)
def bstack111ll1ll11_opy_():
    global bstack111ll111ll_opy_
    if bstack1lllllllll_opy_():
        bstack111ll111ll_opy_ = bstack111ll1l_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵ࠯ࡥࡨࡩ࠭ᔬ")
    else:
        bstack111ll111ll_opy_ = bstack111ll1l_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࠪᔭ")
@bstack1l11lll1l_opy_.bstack11l11l1ll1_opy_
def bstack111lll1111_opy_():
    bstack111ll1ll11_opy_()
    if bstack1ll11l11l_opy_():
        bstack11ll1111l1_opy_(bstack111lllllll_opy_)
    bstack1l11l11l11_opy_ = bstack1l11l1ll1l_opy_(bstack111llll1ll_opy_)
bstack111lll1111_opy_()