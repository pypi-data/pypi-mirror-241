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
import datetime
import json
import os
import platform
import re
import subprocess
import traceback
import tempfile
import multiprocessing
import threading
from urllib.parse import urlparse
import git
import requests
from packaging import version
from bstack_utils.config import Config
from bstack_utils.constants import bstack1l1l11l1ll_opy_, bstack111l1l11l_opy_, bstack1ll1l11l11_opy_, bstack1llllll1ll_opy_
from bstack_utils.messages import bstack1l1l1l11_opy_, bstack111l1llll_opy_
from bstack_utils.proxy import bstack1llll1111_opy_, bstack1l111ll11_opy_
bstack1lll1l1lll_opy_ = Config.get_instance()
def bstack1l1ll11ll1_opy_(config):
    return config[bstack1ll_opy_ (u"ࠪࡹࡸ࡫ࡲࡏࡣࡰࡩࠬྦྷ")]
def bstack1l1l1llll1_opy_(config):
    return config[bstack1ll_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶࡏࡪࡿࠧྨ")]
def bstack1lll11ll1l_opy_():
    try:
        import playwright
        return True
    except ImportError:
        return False
def bstack1l1l111l1l_opy_(obj):
    values = []
    bstack1l11llll11_opy_ = re.compile(bstack1ll_opy_ (u"ࡷࠨ࡞ࡄࡗࡖࡘࡔࡓ࡟ࡕࡃࡊࡣࡡࡪࠫࠥࠤྩ"), re.I)
    for key in obj.keys():
        if bstack1l11llll11_opy_.match(key):
            values.append(obj[key])
    return values
def bstack1l11ll11l1_opy_(config):
    tags = []
    tags.extend(bstack1l1l111l1l_opy_(os.environ))
    tags.extend(bstack1l1l111l1l_opy_(config))
    return tags
def bstack1l111ll111_opy_(markers):
    tags = []
    for marker in markers:
        tags.append(marker.name)
    return tags
def bstack1l111lll1l_opy_(bstack1l11ll1ll1_opy_):
    if not bstack1l11ll1ll1_opy_:
        return bstack1ll_opy_ (u"࠭ࠧྪ")
    return bstack1ll_opy_ (u"ࠢࡼࡿࠣࠬࢀࢃࠩࠣྫ").format(bstack1l11ll1ll1_opy_.name, bstack1l11ll1ll1_opy_.email)
def bstack1l1ll111ll_opy_():
    try:
        repo = git.Repo(search_parent_directories=True)
        bstack1l11l1l11l_opy_ = repo.common_dir
        info = {
            bstack1ll_opy_ (u"ࠣࡵ࡫ࡥࠧྫྷ"): repo.head.commit.hexsha,
            bstack1ll_opy_ (u"ࠤࡶ࡬ࡴࡸࡴࡠࡵ࡫ࡥࠧྭ"): repo.git.rev_parse(repo.head.commit, short=True),
            bstack1ll_opy_ (u"ࠥࡦࡷࡧ࡮ࡤࡪࠥྮ"): repo.active_branch.name,
            bstack1ll_opy_ (u"ࠦࡹࡧࡧࠣྯ"): repo.git.describe(all=True, tags=True, exact_match=True),
            bstack1ll_opy_ (u"ࠧࡩ࡯࡮࡯࡬ࡸࡹ࡫ࡲࠣྰ"): bstack1l111lll1l_opy_(repo.head.commit.committer),
            bstack1ll_opy_ (u"ࠨࡣࡰ࡯ࡰ࡭ࡹࡺࡥࡳࡡࡧࡥࡹ࡫ࠢྱ"): repo.head.commit.committed_datetime.isoformat(),
            bstack1ll_opy_ (u"ࠢࡢࡷࡷ࡬ࡴࡸࠢྲ"): bstack1l111lll1l_opy_(repo.head.commit.author),
            bstack1ll_opy_ (u"ࠣࡣࡸࡸ࡭ࡵࡲࡠࡦࡤࡸࡪࠨླ"): repo.head.commit.authored_datetime.isoformat(),
            bstack1ll_opy_ (u"ࠤࡦࡳࡲࡳࡩࡵࡡࡰࡩࡸࡹࡡࡨࡧࠥྴ"): repo.head.commit.message,
            bstack1ll_opy_ (u"ࠥࡶࡴࡵࡴࠣྵ"): repo.git.rev_parse(bstack1ll_opy_ (u"ࠦ࠲࠳ࡳࡩࡱࡺ࠱ࡹࡵࡰ࡭ࡧࡹࡩࡱࠨྶ")),
            bstack1ll_opy_ (u"ࠧࡩ࡯࡮࡯ࡲࡲࡤ࡭ࡩࡵࡡࡧ࡭ࡷࠨྷ"): bstack1l11l1l11l_opy_,
            bstack1ll_opy_ (u"ࠨࡷࡰࡴ࡮ࡸࡷ࡫ࡥࡠࡩ࡬ࡸࡤࡪࡩࡳࠤྸ"): subprocess.check_output([bstack1ll_opy_ (u"ࠢࡨ࡫ࡷࠦྐྵ"), bstack1ll_opy_ (u"ࠣࡴࡨࡺ࠲ࡶࡡࡳࡵࡨࠦྺ"), bstack1ll_opy_ (u"ࠤ࠰࠱࡬࡯ࡴ࠮ࡥࡲࡱࡲࡵ࡮࠮ࡦ࡬ࡶࠧྻ")]).strip().decode(
                bstack1ll_opy_ (u"ࠪࡹࡹ࡬࠭࠹ࠩྼ")),
            bstack1ll_opy_ (u"ࠦࡱࡧࡳࡵࡡࡷࡥ࡬ࠨ྽"): repo.git.describe(tags=True, abbrev=0, always=True),
            bstack1ll_opy_ (u"ࠧࡩ࡯࡮࡯࡬ࡸࡸࡥࡳࡪࡰࡦࡩࡤࡲࡡࡴࡶࡢࡸࡦ࡭ࠢ྾"): repo.git.rev_list(
                bstack1ll_opy_ (u"ࠨࡻࡾ࠰࠱ࡿࢂࠨ྿").format(repo.head.commit, repo.git.describe(tags=True, abbrev=0, always=True)), count=True)
        }
        remotes = repo.remotes
        bstack1l11ll11ll_opy_ = []
        for remote in remotes:
            bstack1l111lllll_opy_ = {
                bstack1ll_opy_ (u"ࠢ࡯ࡣࡰࡩࠧ࿀"): remote.name,
                bstack1ll_opy_ (u"ࠣࡷࡵࡰࠧ࿁"): remote.url,
            }
            bstack1l11ll11ll_opy_.append(bstack1l111lllll_opy_)
        return {
            bstack1ll_opy_ (u"ࠤࡱࡥࡲ࡫ࠢ࿂"): bstack1ll_opy_ (u"ࠥ࡫࡮ࡺࠢ࿃"),
            **info,
            bstack1ll_opy_ (u"ࠦࡷ࡫࡭ࡰࡶࡨࡷࠧ࿄"): bstack1l11ll11ll_opy_
        }
    except Exception as err:
        print(bstack1ll_opy_ (u"ࠧࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤࡵࡵࡰࡶ࡮ࡤࡸ࡮ࡴࡧࠡࡉ࡬ࡸࠥࡳࡥࡵࡣࡧࡥࡹࡧࠠࡸ࡫ࡷ࡬ࠥ࡫ࡲࡳࡱࡵ࠾ࠥࢁࡽࠣ࿅").format(err))
        return {}
def bstack11l111ll_opy_():
    env = os.environ
    if (bstack1ll_opy_ (u"ࠨࡊࡆࡐࡎࡍࡓ࡙࡟ࡖࡔࡏ࿆ࠦ") in env and len(env[bstack1ll_opy_ (u"ࠢࡋࡇࡑࡏࡎࡔࡓࡠࡗࡕࡐࠧ࿇")]) > 0) or (
            bstack1ll_opy_ (u"ࠣࡌࡈࡒࡐࡏࡎࡔࡡࡋࡓࡒࡋࠢ࿈") in env and len(env[bstack1ll_opy_ (u"ࠤࡍࡉࡓࡑࡉࡏࡕࡢࡌࡔࡓࡅࠣ࿉")]) > 0):
        return {
            bstack1ll_opy_ (u"ࠥࡲࡦࡳࡥࠣ࿊"): bstack1ll_opy_ (u"ࠦࡏ࡫࡮࡬࡫ࡱࡷࠧ࿋"),
            bstack1ll_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡺࡸ࡬ࠣ࿌"): env.get(bstack1ll_opy_ (u"ࠨࡂࡖࡋࡏࡈࡤ࡛ࡒࡍࠤ࿍")),
            bstack1ll_opy_ (u"ࠢ࡫ࡱࡥࡣࡳࡧ࡭ࡦࠤ࿎"): env.get(bstack1ll_opy_ (u"ࠣࡌࡒࡆࡤࡔࡁࡎࡇࠥ࿏")),
            bstack1ll_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣ࿐"): env.get(bstack1ll_opy_ (u"ࠥࡆ࡚ࡏࡌࡅࡡࡑ࡙ࡒࡈࡅࡓࠤ࿑"))
        }
    if env.get(bstack1ll_opy_ (u"ࠦࡈࡏࠢ࿒")) == bstack1ll_opy_ (u"ࠧࡺࡲࡶࡧࠥ࿓") and bstack1l11ll1111_opy_(env.get(bstack1ll_opy_ (u"ࠨࡃࡊࡔࡆࡐࡊࡉࡉࠣ࿔"))):
        return {
            bstack1ll_opy_ (u"ࠢ࡯ࡣࡰࡩࠧ࿕"): bstack1ll_opy_ (u"ࠣࡅ࡬ࡶࡨࡲࡥࡄࡋࠥ࿖"),
            bstack1ll_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧ࿗"): env.get(bstack1ll_opy_ (u"ࠥࡇࡎࡘࡃࡍࡇࡢࡆ࡚ࡏࡌࡅࡡࡘࡖࡑࠨ࿘")),
            bstack1ll_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨ࿙"): env.get(bstack1ll_opy_ (u"ࠧࡉࡉࡓࡅࡏࡉࡤࡐࡏࡃࠤ࿚")),
            bstack1ll_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶࠧ࿛"): env.get(bstack1ll_opy_ (u"ࠢࡄࡋࡕࡇࡑࡋ࡟ࡃࡗࡌࡐࡉࡥࡎࡖࡏࠥ࿜"))
        }
    if env.get(bstack1ll_opy_ (u"ࠣࡅࡌࠦ࿝")) == bstack1ll_opy_ (u"ࠤࡷࡶࡺ࡫ࠢ࿞") and bstack1l11ll1111_opy_(env.get(bstack1ll_opy_ (u"ࠥࡘࡗࡇࡖࡊࡕࠥ࿟"))):
        return {
            bstack1ll_opy_ (u"ࠦࡳࡧ࡭ࡦࠤ࿠"): bstack1ll_opy_ (u"࡚ࠧࡲࡢࡸ࡬ࡷࠥࡉࡉࠣ࿡"),
            bstack1ll_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤ࿢"): env.get(bstack1ll_opy_ (u"ࠢࡕࡔࡄ࡚ࡎ࡙࡟ࡃࡗࡌࡐࡉࡥࡗࡆࡄࡢ࡙ࡗࡒࠢ࿣")),
            bstack1ll_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧࠥ࿤"): env.get(bstack1ll_opy_ (u"ࠤࡗࡖࡆ࡜ࡉࡔࡡࡍࡓࡇࡥࡎࡂࡏࡈࠦ࿥")),
            bstack1ll_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠤ࿦"): env.get(bstack1ll_opy_ (u"࡙ࠦࡘࡁࡗࡋࡖࡣࡇ࡛ࡉࡍࡆࡢࡒ࡚ࡓࡂࡆࡔࠥ࿧"))
        }
    if env.get(bstack1ll_opy_ (u"ࠧࡉࡉࠣ࿨")) == bstack1ll_opy_ (u"ࠨࡴࡳࡷࡨࠦ࿩") and env.get(bstack1ll_opy_ (u"ࠢࡄࡋࡢࡒࡆࡓࡅࠣ࿪")) == bstack1ll_opy_ (u"ࠣࡥࡲࡨࡪࡹࡨࡪࡲࠥ࿫"):
        return {
            bstack1ll_opy_ (u"ࠤࡱࡥࡲ࡫ࠢ࿬"): bstack1ll_opy_ (u"ࠥࡇࡴࡪࡥࡴࡪ࡬ࡴࠧ࿭"),
            bstack1ll_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲࠢ࿮"): None,
            bstack1ll_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢ࿯"): None,
            bstack1ll_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶࠧ࿰"): None
        }
    if env.get(bstack1ll_opy_ (u"ࠢࡃࡋࡗࡆ࡚ࡉࡋࡆࡖࡢࡆࡗࡇࡎࡄࡊࠥ࿱")) and env.get(bstack1ll_opy_ (u"ࠣࡄࡌࡘࡇ࡛ࡃࡌࡇࡗࡣࡈࡕࡍࡎࡋࡗࠦ࿲")):
        return {
            bstack1ll_opy_ (u"ࠤࡱࡥࡲ࡫ࠢ࿳"): bstack1ll_opy_ (u"ࠥࡆ࡮ࡺࡢࡶࡥ࡮ࡩࡹࠨ࿴"),
            bstack1ll_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲࠢ࿵"): env.get(bstack1ll_opy_ (u"ࠧࡈࡉࡕࡄࡘࡇࡐࡋࡔࡠࡉࡌࡘࡤࡎࡔࡕࡒࡢࡓࡗࡏࡇࡊࡐࠥ࿶")),
            bstack1ll_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥࠣ࿷"): None,
            bstack1ll_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨ࿸"): env.get(bstack1ll_opy_ (u"ࠣࡄࡌࡘࡇ࡛ࡃࡌࡇࡗࡣࡇ࡛ࡉࡍࡆࡢࡒ࡚ࡓࡂࡆࡔࠥ࿹"))
        }
    if env.get(bstack1ll_opy_ (u"ࠤࡆࡍࠧ࿺")) == bstack1ll_opy_ (u"ࠥࡸࡷࡻࡥࠣ࿻") and bstack1l11ll1111_opy_(env.get(bstack1ll_opy_ (u"ࠦࡉࡘࡏࡏࡇࠥ࿼"))):
        return {
            bstack1ll_opy_ (u"ࠧࡴࡡ࡮ࡧࠥ࿽"): bstack1ll_opy_ (u"ࠨࡄࡳࡱࡱࡩࠧ࿾"),
            bstack1ll_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥ࿿"): env.get(bstack1ll_opy_ (u"ࠣࡆࡕࡓࡓࡋ࡟ࡃࡗࡌࡐࡉࡥࡌࡊࡐࡎࠦက")),
            bstack1ll_opy_ (u"ࠤ࡭ࡳࡧࡥ࡮ࡢ࡯ࡨࠦခ"): None,
            bstack1ll_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠤဂ"): env.get(bstack1ll_opy_ (u"ࠦࡉࡘࡏࡏࡇࡢࡆ࡚ࡏࡌࡅࡡࡑ࡙ࡒࡈࡅࡓࠤဃ"))
        }
    if env.get(bstack1ll_opy_ (u"ࠧࡉࡉࠣင")) == bstack1ll_opy_ (u"ࠨࡴࡳࡷࡨࠦစ") and bstack1l11ll1111_opy_(env.get(bstack1ll_opy_ (u"ࠢࡔࡇࡐࡅࡕࡎࡏࡓࡇࠥဆ"))):
        return {
            bstack1ll_opy_ (u"ࠣࡰࡤࡱࡪࠨဇ"): bstack1ll_opy_ (u"ࠤࡖࡩࡲࡧࡰࡩࡱࡵࡩࠧဈ"),
            bstack1ll_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡸࡶࡱࠨဉ"): env.get(bstack1ll_opy_ (u"ࠦࡘࡋࡍࡂࡒࡋࡓࡗࡋ࡟ࡐࡔࡊࡅࡓࡏ࡚ࡂࡖࡌࡓࡓࡥࡕࡓࡎࠥည")),
            bstack1ll_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢဋ"): env.get(bstack1ll_opy_ (u"ࠨࡓࡆࡏࡄࡔࡍࡕࡒࡆࡡࡍࡓࡇࡥࡎࡂࡏࡈࠦဌ")),
            bstack1ll_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨဍ"): env.get(bstack1ll_opy_ (u"ࠣࡕࡈࡑࡆࡖࡈࡐࡔࡈࡣࡏࡕࡂࡠࡋࡇࠦဎ"))
        }
    if env.get(bstack1ll_opy_ (u"ࠤࡆࡍࠧဏ")) == bstack1ll_opy_ (u"ࠥࡸࡷࡻࡥࠣတ") and bstack1l11ll1111_opy_(env.get(bstack1ll_opy_ (u"ࠦࡌࡏࡔࡍࡃࡅࡣࡈࡏࠢထ"))):
        return {
            bstack1ll_opy_ (u"ࠧࡴࡡ࡮ࡧࠥဒ"): bstack1ll_opy_ (u"ࠨࡇࡪࡶࡏࡥࡧࠨဓ"),
            bstack1ll_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥန"): env.get(bstack1ll_opy_ (u"ࠣࡅࡌࡣࡏࡕࡂࡠࡗࡕࡐࠧပ")),
            bstack1ll_opy_ (u"ࠤ࡭ࡳࡧࡥ࡮ࡢ࡯ࡨࠦဖ"): env.get(bstack1ll_opy_ (u"ࠥࡇࡎࡥࡊࡐࡄࡢࡒࡆࡓࡅࠣဗ")),
            bstack1ll_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴࠥဘ"): env.get(bstack1ll_opy_ (u"ࠧࡉࡉࡠࡌࡒࡆࡤࡏࡄࠣမ"))
        }
    if env.get(bstack1ll_opy_ (u"ࠨࡃࡊࠤယ")) == bstack1ll_opy_ (u"ࠢࡵࡴࡸࡩࠧရ") and bstack1l11ll1111_opy_(env.get(bstack1ll_opy_ (u"ࠣࡄࡘࡍࡑࡊࡋࡊࡖࡈࠦလ"))):
        return {
            bstack1ll_opy_ (u"ࠤࡱࡥࡲ࡫ࠢဝ"): bstack1ll_opy_ (u"ࠥࡆࡺ࡯࡬ࡥ࡭࡬ࡸࡪࠨသ"),
            bstack1ll_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲࠢဟ"): env.get(bstack1ll_opy_ (u"ࠧࡈࡕࡊࡎࡇࡏࡎ࡚ࡅࡠࡄࡘࡍࡑࡊ࡟ࡖࡔࡏࠦဠ")),
            bstack1ll_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥࠣအ"): env.get(bstack1ll_opy_ (u"ࠢࡃࡗࡌࡐࡉࡑࡉࡕࡇࡢࡐࡆࡈࡅࡍࠤဢ")) or env.get(bstack1ll_opy_ (u"ࠣࡄࡘࡍࡑࡊࡋࡊࡖࡈࡣࡕࡏࡐࡆࡎࡌࡒࡊࡥࡎࡂࡏࡈࠦဣ")),
            bstack1ll_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣဤ"): env.get(bstack1ll_opy_ (u"ࠥࡆ࡚ࡏࡌࡅࡍࡌࡘࡊࡥࡂࡖࡋࡏࡈࡤࡔࡕࡎࡄࡈࡖࠧဥ"))
        }
    if bstack1l11ll1111_opy_(env.get(bstack1ll_opy_ (u"࡙ࠦࡌ࡟ࡃࡗࡌࡐࡉࠨဦ"))):
        return {
            bstack1ll_opy_ (u"ࠧࡴࡡ࡮ࡧࠥဧ"): bstack1ll_opy_ (u"ࠨࡖࡪࡵࡸࡥࡱࠦࡓࡵࡷࡧ࡭ࡴࠦࡔࡦࡣࡰࠤࡘ࡫ࡲࡷ࡫ࡦࡩࡸࠨဨ"),
            bstack1ll_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥဩ"): bstack1ll_opy_ (u"ࠣࡽࢀࡿࢂࠨဪ").format(env.get(bstack1ll_opy_ (u"ࠩࡖ࡝ࡘ࡚ࡅࡎࡡࡗࡉࡆࡓࡆࡐࡗࡑࡈࡆ࡚ࡉࡐࡐࡖࡉࡗ࡜ࡅࡓࡗࡕࡍࠬါ")), env.get(bstack1ll_opy_ (u"ࠪࡗ࡞࡙ࡔࡆࡏࡢࡘࡊࡇࡍࡑࡔࡒࡎࡊࡉࡔࡊࡆࠪာ"))),
            bstack1ll_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨိ"): env.get(bstack1ll_opy_ (u"࡙࡙ࠧࡔࡖࡈࡑࡤࡊࡅࡇࡋࡑࡍ࡙ࡏࡏࡏࡋࡇࠦီ")),
            bstack1ll_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶࠧု"): env.get(bstack1ll_opy_ (u"ࠢࡃࡗࡌࡐࡉࡥࡂࡖࡋࡏࡈࡎࡊࠢူ"))
        }
    if bstack1l11ll1111_opy_(env.get(bstack1ll_opy_ (u"ࠣࡃࡓࡔ࡛ࡋ࡙ࡐࡔࠥေ"))):
        return {
            bstack1ll_opy_ (u"ࠤࡱࡥࡲ࡫ࠢဲ"): bstack1ll_opy_ (u"ࠥࡅࡵࡶࡶࡦࡻࡲࡶࠧဳ"),
            bstack1ll_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲࠢဴ"): bstack1ll_opy_ (u"ࠧࢁࡽ࠰ࡲࡵࡳ࡯࡫ࡣࡵ࠱ࡾࢁ࠴ࢁࡽ࠰ࡤࡸ࡭ࡱࡪࡳ࠰ࡽࢀࠦဵ").format(env.get(bstack1ll_opy_ (u"࠭ࡁࡑࡒ࡙ࡉ࡞ࡕࡒࡠࡗࡕࡐࠬံ")), env.get(bstack1ll_opy_ (u"ࠧࡂࡒࡓ࡚ࡊ࡟ࡏࡓࡡࡄࡇࡈࡕࡕࡏࡖࡢࡒࡆࡓࡅࠨ့")), env.get(bstack1ll_opy_ (u"ࠨࡃࡓࡔ࡛ࡋ࡙ࡐࡔࡢࡔࡗࡕࡊࡆࡅࡗࡣࡘࡒࡕࡈࠩး")), env.get(bstack1ll_opy_ (u"ࠩࡄࡔࡕ࡜ࡅ࡚ࡑࡕࡣࡇ࡛ࡉࡍࡆࡢࡍࡉ္࠭"))),
            bstack1ll_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩ်ࠧ"): env.get(bstack1ll_opy_ (u"ࠦࡆࡖࡐࡗࡇ࡜ࡓࡗࡥࡊࡐࡄࡢࡒࡆࡓࡅࠣျ")),
            bstack1ll_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦြ"): env.get(bstack1ll_opy_ (u"ࠨࡁࡑࡒ࡙ࡉ࡞ࡕࡒࡠࡄࡘࡍࡑࡊ࡟ࡏࡗࡐࡆࡊࡘࠢွ"))
        }
    if env.get(bstack1ll_opy_ (u"ࠢࡂ࡜ࡘࡖࡊࡥࡈࡕࡖࡓࡣ࡚࡙ࡅࡓࡡࡄࡋࡊࡔࡔࠣှ")) and env.get(bstack1ll_opy_ (u"ࠣࡖࡉࡣࡇ࡛ࡉࡍࡆࠥဿ")):
        return {
            bstack1ll_opy_ (u"ࠤࡱࡥࡲ࡫ࠢ၀"): bstack1ll_opy_ (u"ࠥࡅࡿࡻࡲࡦࠢࡆࡍࠧ၁"),
            bstack1ll_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲࠢ၂"): bstack1ll_opy_ (u"ࠧࢁࡽࡼࡿ࠲ࡣࡧࡻࡩ࡭ࡦ࠲ࡶࡪࡹࡵ࡭ࡶࡶࡃࡧࡻࡩ࡭ࡦࡌࡨࡂࢁࡽࠣ၃").format(env.get(bstack1ll_opy_ (u"࠭ࡓ࡚ࡕࡗࡉࡒࡥࡔࡆࡃࡐࡊࡔ࡛ࡎࡅࡃࡗࡍࡔࡔࡓࡆࡔ࡙ࡉࡗ࡛ࡒࡊࠩ၄")), env.get(bstack1ll_opy_ (u"ࠧࡔ࡛ࡖࡘࡊࡓ࡟ࡕࡇࡄࡑࡕࡘࡏࡋࡇࡆࡘࠬ၅")), env.get(bstack1ll_opy_ (u"ࠨࡄࡘࡍࡑࡊ࡟ࡃࡗࡌࡐࡉࡏࡄࠨ၆"))),
            bstack1ll_opy_ (u"ࠤ࡭ࡳࡧࡥ࡮ࡢ࡯ࡨࠦ၇"): env.get(bstack1ll_opy_ (u"ࠥࡆ࡚ࡏࡌࡅࡡࡅ࡙ࡎࡒࡄࡊࡆࠥ၈")),
            bstack1ll_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴࠥ၉"): env.get(bstack1ll_opy_ (u"ࠧࡈࡕࡊࡎࡇࡣࡇ࡛ࡉࡍࡆࡌࡈࠧ၊"))
        }
    if any([env.get(bstack1ll_opy_ (u"ࠨࡃࡐࡆࡈࡆ࡚ࡏࡌࡅࡡࡅ࡙ࡎࡒࡄࡠࡋࡇࠦ။")), env.get(bstack1ll_opy_ (u"ࠢࡄࡑࡇࡉࡇ࡛ࡉࡍࡆࡢࡖࡊ࡙ࡏࡍࡘࡈࡈࡤ࡙ࡏࡖࡔࡆࡉࡤ࡜ࡅࡓࡕࡌࡓࡓࠨ၌")), env.get(bstack1ll_opy_ (u"ࠣࡅࡒࡈࡊࡈࡕࡊࡎࡇࡣࡘࡕࡕࡓࡅࡈࡣ࡛ࡋࡒࡔࡋࡒࡒࠧ၍"))]):
        return {
            bstack1ll_opy_ (u"ࠤࡱࡥࡲ࡫ࠢ၎"): bstack1ll_opy_ (u"ࠥࡅ࡜࡙ࠠࡄࡱࡧࡩࡇࡻࡩ࡭ࡦࠥ၏"),
            bstack1ll_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲࠢၐ"): env.get(bstack1ll_opy_ (u"ࠧࡉࡏࡅࡇࡅ࡙ࡎࡒࡄࡠࡒࡘࡆࡑࡏࡃࡠࡄࡘࡍࡑࡊ࡟ࡖࡔࡏࠦၑ")),
            bstack1ll_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥࠣၒ"): env.get(bstack1ll_opy_ (u"ࠢࡄࡑࡇࡉࡇ࡛ࡉࡍࡆࡢࡆ࡚ࡏࡌࡅࡡࡌࡈࠧၓ")),
            bstack1ll_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠢၔ"): env.get(bstack1ll_opy_ (u"ࠤࡆࡓࡉࡋࡂࡖࡋࡏࡈࡤࡈࡕࡊࡎࡇࡣࡎࡊࠢၕ"))
        }
    if env.get(bstack1ll_opy_ (u"ࠥࡦࡦࡳࡢࡰࡱࡢࡦࡺ࡯࡬ࡥࡐࡸࡱࡧ࡫ࡲࠣၖ")):
        return {
            bstack1ll_opy_ (u"ࠦࡳࡧ࡭ࡦࠤၗ"): bstack1ll_opy_ (u"ࠧࡈࡡ࡮ࡤࡲࡳࠧၘ"),
            bstack1ll_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤၙ"): env.get(bstack1ll_opy_ (u"ࠢࡣࡣࡰࡦࡴࡵ࡟ࡣࡷ࡬ࡰࡩࡘࡥࡴࡷ࡯ࡸࡸ࡛ࡲ࡭ࠤၚ")),
            bstack1ll_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧࠥၛ"): env.get(bstack1ll_opy_ (u"ࠤࡥࡥࡲࡨ࡯ࡰࡡࡶ࡬ࡴࡸࡴࡋࡱࡥࡒࡦࡳࡥࠣၜ")),
            bstack1ll_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠤၝ"): env.get(bstack1ll_opy_ (u"ࠦࡧࡧ࡭ࡣࡱࡲࡣࡧࡻࡩ࡭ࡦࡑࡹࡲࡨࡥࡳࠤၞ"))
        }
    if env.get(bstack1ll_opy_ (u"ࠧ࡝ࡅࡓࡅࡎࡉࡗࠨၟ")) or env.get(bstack1ll_opy_ (u"ࠨࡗࡆࡔࡆࡏࡊࡘ࡟ࡎࡃࡌࡒࡤࡖࡉࡑࡇࡏࡍࡓࡋ࡟ࡔࡖࡄࡖ࡙ࡋࡄࠣၠ")):
        return {
            bstack1ll_opy_ (u"ࠢ࡯ࡣࡰࡩࠧၡ"): bstack1ll_opy_ (u"࡙ࠣࡨࡶࡨࡱࡥࡳࠤၢ"),
            bstack1ll_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧၣ"): env.get(bstack1ll_opy_ (u"࡛ࠥࡊࡘࡃࡌࡇࡕࡣࡇ࡛ࡉࡍࡆࡢ࡙ࡗࡒࠢၤ")),
            bstack1ll_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨၥ"): bstack1ll_opy_ (u"ࠧࡓࡡࡪࡰࠣࡔ࡮ࡶࡥ࡭࡫ࡱࡩࠧၦ") if env.get(bstack1ll_opy_ (u"ࠨࡗࡆࡔࡆࡏࡊࡘ࡟ࡎࡃࡌࡒࡤࡖࡉࡑࡇࡏࡍࡓࡋ࡟ࡔࡖࡄࡖ࡙ࡋࡄࠣၧ")) else None,
            bstack1ll_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨၨ"): env.get(bstack1ll_opy_ (u"࡙ࠣࡈࡖࡈࡑࡅࡓࡡࡊࡍ࡙ࡥࡃࡐࡏࡐࡍ࡙ࠨၩ"))
        }
    if any([env.get(bstack1ll_opy_ (u"ࠤࡊࡇࡕࡥࡐࡓࡑࡍࡉࡈ࡚ࠢၪ")), env.get(bstack1ll_opy_ (u"ࠥࡋࡈࡒࡏࡖࡆࡢࡔࡗࡕࡊࡆࡅࡗࠦၫ")), env.get(bstack1ll_opy_ (u"ࠦࡌࡕࡏࡈࡎࡈࡣࡈࡒࡏࡖࡆࡢࡔࡗࡕࡊࡆࡅࡗࠦၬ"))]):
        return {
            bstack1ll_opy_ (u"ࠧࡴࡡ࡮ࡧࠥၭ"): bstack1ll_opy_ (u"ࠨࡇࡰࡱࡪࡰࡪࠦࡃ࡭ࡱࡸࡨࠧၮ"),
            bstack1ll_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥၯ"): None,
            bstack1ll_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧࠥၰ"): env.get(bstack1ll_opy_ (u"ࠤࡓࡖࡔࡐࡅࡄࡖࡢࡍࡉࠨၱ")),
            bstack1ll_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠤၲ"): env.get(bstack1ll_opy_ (u"ࠦࡇ࡛ࡉࡍࡆࡢࡍࡉࠨၳ"))
        }
    if env.get(bstack1ll_opy_ (u"࡙ࠧࡈࡊࡒࡓࡅࡇࡒࡅࠣၴ")):
        return {
            bstack1ll_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦၵ"): bstack1ll_opy_ (u"ࠢࡔࡪ࡬ࡴࡵࡧࡢ࡭ࡧࠥၶ"),
            bstack1ll_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟ࡶࡴ࡯ࠦၷ"): env.get(bstack1ll_opy_ (u"ࠤࡖࡌࡎࡖࡐࡂࡄࡏࡉࡤࡈࡕࡊࡎࡇࡣ࡚ࡘࡌࠣၸ")),
            bstack1ll_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧၹ"): bstack1ll_opy_ (u"ࠦࡏࡵࡢࠡࠥࡾࢁࠧၺ").format(env.get(bstack1ll_opy_ (u"࡙ࠬࡈࡊࡒࡓࡅࡇࡒࡅࡠࡌࡒࡆࡤࡏࡄࠨၻ"))) if env.get(bstack1ll_opy_ (u"ࠨࡓࡉࡋࡓࡔࡆࡈࡌࡆࡡࡍࡓࡇࡥࡉࡅࠤၼ")) else None,
            bstack1ll_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨၽ"): env.get(bstack1ll_opy_ (u"ࠣࡕࡋࡍࡕࡖࡁࡃࡎࡈࡣࡇ࡛ࡉࡍࡆࡢࡒ࡚ࡓࡂࡆࡔࠥၾ"))
        }
    if bstack1l11ll1111_opy_(env.get(bstack1ll_opy_ (u"ࠤࡑࡉ࡙ࡒࡉࡇ࡛ࠥၿ"))):
        return {
            bstack1ll_opy_ (u"ࠥࡲࡦࡳࡥࠣႀ"): bstack1ll_opy_ (u"ࠦࡓ࡫ࡴ࡭࡫ࡩࡽࠧႁ"),
            bstack1ll_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡺࡸ࡬ࠣႂ"): env.get(bstack1ll_opy_ (u"ࠨࡄࡆࡒࡏࡓ࡞ࡥࡕࡓࡎࠥႃ")),
            bstack1ll_opy_ (u"ࠢ࡫ࡱࡥࡣࡳࡧ࡭ࡦࠤႄ"): env.get(bstack1ll_opy_ (u"ࠣࡕࡌࡘࡊࡥࡎࡂࡏࡈࠦႅ")),
            bstack1ll_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣႆ"): env.get(bstack1ll_opy_ (u"ࠥࡆ࡚ࡏࡌࡅࡡࡌࡈࠧႇ"))
        }
    if bstack1l11ll1111_opy_(env.get(bstack1ll_opy_ (u"ࠦࡌࡏࡔࡉࡗࡅࡣࡆࡉࡔࡊࡑࡑࡗࠧႈ"))):
        return {
            bstack1ll_opy_ (u"ࠧࡴࡡ࡮ࡧࠥႉ"): bstack1ll_opy_ (u"ࠨࡇࡪࡶࡋࡹࡧࠦࡁࡤࡶ࡬ࡳࡳࡹࠢႊ"),
            bstack1ll_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥႋ"): bstack1ll_opy_ (u"ࠣࡽࢀ࠳ࢀࢃ࠯ࡢࡥࡷ࡭ࡴࡴࡳ࠰ࡴࡸࡲࡸ࠵ࡻࡾࠤႌ").format(env.get(bstack1ll_opy_ (u"ࠩࡊࡍ࡙ࡎࡕࡃࡡࡖࡉࡗ࡜ࡅࡓࡡࡘࡖࡑႍ࠭")), env.get(bstack1ll_opy_ (u"ࠪࡋࡎ࡚ࡈࡖࡄࡢࡖࡊࡖࡏࡔࡋࡗࡓࡗ࡟ࠧႎ")), env.get(bstack1ll_opy_ (u"ࠫࡌࡏࡔࡉࡗࡅࡣࡗ࡛ࡎࡠࡋࡇࠫႏ"))),
            bstack1ll_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢ႐"): env.get(bstack1ll_opy_ (u"ࠨࡇࡊࡖࡋ࡙ࡇࡥࡗࡐࡔࡎࡊࡑࡕࡗࠣ႑")),
            bstack1ll_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨ႒"): env.get(bstack1ll_opy_ (u"ࠣࡉࡌࡘࡍ࡛ࡂࡠࡔࡘࡒࡤࡏࡄࠣ႓"))
        }
    if env.get(bstack1ll_opy_ (u"ࠤࡆࡍࠧ႔")) == bstack1ll_opy_ (u"ࠥࡸࡷࡻࡥࠣ႕") and env.get(bstack1ll_opy_ (u"࡛ࠦࡋࡒࡄࡇࡏࠦ႖")) == bstack1ll_opy_ (u"ࠧ࠷ࠢ႗"):
        return {
            bstack1ll_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦ႘"): bstack1ll_opy_ (u"ࠢࡗࡧࡵࡧࡪࡲࠢ႙"),
            bstack1ll_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟ࡶࡴ࡯ࠦႚ"): bstack1ll_opy_ (u"ࠤ࡫ࡸࡹࡶ࠺࠰࠱ࡾࢁࠧႛ").format(env.get(bstack1ll_opy_ (u"࡚ࠪࡊࡘࡃࡆࡎࡢ࡙ࡗࡒࠧႜ"))),
            bstack1ll_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨႝ"): None,
            bstack1ll_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦ႞"): None,
        }
    if env.get(bstack1ll_opy_ (u"ࠨࡔࡆࡃࡐࡇࡎ࡚࡙ࡠࡘࡈࡖࡘࡏࡏࡏࠤ႟")):
        return {
            bstack1ll_opy_ (u"ࠢ࡯ࡣࡰࡩࠧႠ"): bstack1ll_opy_ (u"ࠣࡖࡨࡥࡲࡩࡩࡵࡻࠥႡ"),
            bstack1ll_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧႢ"): None,
            bstack1ll_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧႣ"): env.get(bstack1ll_opy_ (u"࡙ࠦࡋࡁࡎࡅࡌࡘ࡞ࡥࡐࡓࡑࡍࡉࡈ࡚࡟ࡏࡃࡐࡉࠧႤ")),
            bstack1ll_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦႥ"): env.get(bstack1ll_opy_ (u"ࠨࡂࡖࡋࡏࡈࡤࡔࡕࡎࡄࡈࡖࠧႦ"))
        }
    if any([env.get(bstack1ll_opy_ (u"ࠢࡄࡑࡑࡇࡔ࡛ࡒࡔࡇࠥႧ")), env.get(bstack1ll_opy_ (u"ࠣࡅࡒࡒࡈࡕࡕࡓࡕࡈࡣ࡚ࡘࡌࠣႨ")), env.get(bstack1ll_opy_ (u"ࠤࡆࡓࡓࡉࡏࡖࡔࡖࡉࡤ࡛ࡓࡆࡔࡑࡅࡒࡋࠢႩ")), env.get(bstack1ll_opy_ (u"ࠥࡇࡔࡔࡃࡐࡗࡕࡗࡊࡥࡔࡆࡃࡐࠦႪ"))]):
        return {
            bstack1ll_opy_ (u"ࠦࡳࡧ࡭ࡦࠤႫ"): bstack1ll_opy_ (u"ࠧࡉ࡯࡯ࡥࡲࡹࡷࡹࡥࠣႬ"),
            bstack1ll_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤႭ"): None,
            bstack1ll_opy_ (u"ࠢ࡫ࡱࡥࡣࡳࡧ࡭ࡦࠤႮ"): env.get(bstack1ll_opy_ (u"ࠣࡄࡘࡍࡑࡊ࡟ࡋࡑࡅࡣࡓࡇࡍࡆࠤႯ")) or None,
            bstack1ll_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣႰ"): env.get(bstack1ll_opy_ (u"ࠥࡆ࡚ࡏࡌࡅࡡࡌࡈࠧႱ"), 0)
        }
    if env.get(bstack1ll_opy_ (u"ࠦࡌࡕ࡟ࡋࡑࡅࡣࡓࡇࡍࡆࠤႲ")):
        return {
            bstack1ll_opy_ (u"ࠧࡴࡡ࡮ࡧࠥႳ"): bstack1ll_opy_ (u"ࠨࡇࡰࡅࡇࠦႴ"),
            bstack1ll_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥႵ"): None,
            bstack1ll_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧࠥႶ"): env.get(bstack1ll_opy_ (u"ࠤࡊࡓࡤࡐࡏࡃࡡࡑࡅࡒࡋࠢႷ")),
            bstack1ll_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠤႸ"): env.get(bstack1ll_opy_ (u"ࠦࡌࡕ࡟ࡑࡋࡓࡉࡑࡏࡎࡆࡡࡆࡓ࡚ࡔࡔࡆࡔࠥႹ"))
        }
    if env.get(bstack1ll_opy_ (u"ࠧࡉࡆࡠࡄࡘࡍࡑࡊ࡟ࡊࡆࠥႺ")):
        return {
            bstack1ll_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦႻ"): bstack1ll_opy_ (u"ࠢࡄࡱࡧࡩࡋࡸࡥࡴࡪࠥႼ"),
            bstack1ll_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟ࡶࡴ࡯ࠦႽ"): env.get(bstack1ll_opy_ (u"ࠤࡆࡊࡤࡈࡕࡊࡎࡇࡣ࡚ࡘࡌࠣႾ")),
            bstack1ll_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧႿ"): env.get(bstack1ll_opy_ (u"ࠦࡈࡌ࡟ࡑࡋࡓࡉࡑࡏࡎࡆࡡࡑࡅࡒࡋࠢჀ")),
            bstack1ll_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦჁ"): env.get(bstack1ll_opy_ (u"ࠨࡃࡇࡡࡅ࡙ࡎࡒࡄࡠࡋࡇࠦჂ"))
        }
    return {bstack1ll_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨჃ"): None}
def get_host_info():
    return {
        bstack1ll_opy_ (u"ࠣࡪࡲࡷࡹࡴࡡ࡮ࡧࠥჄ"): platform.node(),
        bstack1ll_opy_ (u"ࠤࡳࡰࡦࡺࡦࡰࡴࡰࠦჅ"): platform.system(),
        bstack1ll_opy_ (u"ࠥࡸࡾࡶࡥࠣ჆"): platform.machine(),
        bstack1ll_opy_ (u"ࠦࡻ࡫ࡲࡴ࡫ࡲࡲࠧჇ"): platform.version(),
        bstack1ll_opy_ (u"ࠧࡧࡲࡤࡪࠥ჈"): platform.architecture()[0]
    }
def bstack111ll111l_opy_():
    try:
        import selenium
        return True
    except ImportError:
        return False
def bstack1l11l1l111_opy_():
    if bstack1lll1l1lll_opy_.get_property(bstack1ll_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡥࡳࡦࡵࡶ࡭ࡴࡴࠧ჉")):
        return bstack1ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠭჊")
    return bstack1ll_opy_ (u"ࠨࡷࡱ࡯ࡳࡵࡷ࡯ࡡࡪࡶ࡮ࡪࠧ჋")
def bstack1l11l11l1l_opy_(driver):
    info = {
        bstack1ll_opy_ (u"ࠩࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠨ჌"): driver.capabilities,
        bstack1ll_opy_ (u"ࠪࡷࡪࡹࡳࡪࡱࡱࡣ࡮ࡪࠧჍ"): driver.session_id,
        bstack1ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࠬ჎"): driver.capabilities.get(bstack1ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠪ჏"), None),
        bstack1ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠨა"): driver.capabilities.get(bstack1ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠨბ"), None),
        bstack1ll_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪგ"): driver.capabilities.get(bstack1ll_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡒࡦࡳࡥࠨდ"), None),
    }
    if bstack1l11l1l111_opy_() == bstack1ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠩე"):
        info[bstack1ll_opy_ (u"ࠫࡵࡸ࡯ࡥࡷࡦࡸࠬვ")] = bstack1ll_opy_ (u"ࠬࡧࡰࡱ࠯ࡤࡹࡹࡵ࡭ࡢࡶࡨࠫზ") if bstack11l1l1ll_opy_() else bstack1ll_opy_ (u"࠭ࡡࡶࡶࡲࡱࡦࡺࡥࠨთ")
    return info
def bstack11l1l1ll_opy_():
    if bstack1lll1l1lll_opy_.get_property(bstack1ll_opy_ (u"ࠧࡢࡲࡳࡣࡦࡻࡴࡰ࡯ࡤࡸࡪ࠭ი")):
        return True
    if bstack1l11ll1111_opy_(os.environ.get(bstack1ll_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡊࡕࡢࡅࡕࡖ࡟ࡂࡗࡗࡓࡒࡇࡔࡆࠩკ"), None)):
        return True
    return False
def bstack1llll1l11l_opy_(bstack1l11l11ll1_opy_, url, data, config):
    headers = config.get(bstack1ll_opy_ (u"ࠩ࡫ࡩࡦࡪࡥࡳࡵࠪლ"), None)
    proxies = bstack1llll1111_opy_(config, url)
    auth = config.get(bstack1ll_opy_ (u"ࠪࡥࡺࡺࡨࠨმ"), None)
    response = requests.request(
            bstack1l11l11ll1_opy_,
            url=url,
            headers=headers,
            auth=auth,
            json=data,
            proxies=proxies
        )
    return response
def bstack11ll111ll_opy_(bstack1ll1l1l111_opy_, size):
    bstack1ll1ll1l_opy_ = []
    while len(bstack1ll1l1l111_opy_) > size:
        bstack11111l11_opy_ = bstack1ll1l1l111_opy_[:size]
        bstack1ll1ll1l_opy_.append(bstack11111l11_opy_)
        bstack1ll1l1l111_opy_ = bstack1ll1l1l111_opy_[size:]
    bstack1ll1ll1l_opy_.append(bstack1ll1l1l111_opy_)
    return bstack1ll1ll1l_opy_
def bstack1l111ll11l_opy_(message, bstack1l11l1l1l1_opy_=False):
    os.write(1, bytes(message, bstack1ll_opy_ (u"ࠫࡺࡺࡦ࠮࠺ࠪნ")))
    os.write(1, bytes(bstack1ll_opy_ (u"ࠬࡢ࡮ࠨო"), bstack1ll_opy_ (u"࠭ࡵࡵࡨ࠰࠼ࠬპ")))
    if bstack1l11l1l1l1_opy_:
        with open(bstack1ll_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࠭ࡰ࠳࠴ࡽ࠲࠭ჟ") + os.environ[bstack1ll_opy_ (u"ࠨࡄࡖࡣ࡙ࡋࡓࡕࡑࡓࡗࡤࡈࡕࡊࡎࡇࡣࡍࡇࡓࡉࡇࡇࡣࡎࡊࠧრ")] + bstack1ll_opy_ (u"ࠩ࠱ࡰࡴ࡭ࠧს"), bstack1ll_opy_ (u"ࠪࡥࠬტ")) as f:
            f.write(message + bstack1ll_opy_ (u"ࠫࡡࡴࠧუ"))
def bstack1l11l1ll11_opy_():
    return os.environ[bstack1ll_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡆ࡛ࡔࡐࡏࡄࡘࡎࡕࡎࠨფ")].lower() == bstack1ll_opy_ (u"࠭ࡴࡳࡷࡨࠫქ")
def bstack1lll1ll1l1_opy_(bstack1l11llllll_opy_):
    return bstack1ll_opy_ (u"ࠧࡼࡿ࠲ࡿࢂ࠭ღ").format(bstack1l1l11l1ll_opy_, bstack1l11llllll_opy_)
def bstack1lllll1ll1_opy_():
    return datetime.datetime.utcnow().isoformat() + bstack1ll_opy_ (u"ࠨ࡜ࠪყ")
def bstack1l11l1l1ll_opy_(start, finish):
    return (datetime.datetime.fromisoformat(finish.rstrip(bstack1ll_opy_ (u"ࠩ࡝ࠫშ"))) - datetime.datetime.fromisoformat(start.rstrip(bstack1ll_opy_ (u"ࠪ࡞ࠬჩ")))).total_seconds() * 1000
def bstack1l11lll1l1_opy_(timestamp):
    return datetime.datetime.utcfromtimestamp(timestamp).isoformat() + bstack1ll_opy_ (u"ࠫ࡟࠭ც")
def bstack1l11lllll1_opy_(outcome):
    _, exception, _ = outcome.excinfo or (None, None, None)
    if exception:
        return bstack1ll_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬძ")
    else:
        return bstack1ll_opy_ (u"࠭ࡰࡢࡵࡶࡩࡩ࠭წ")
def bstack1l11ll1111_opy_(val):
    if val is None:
        return False
    return val.__str__().lower() == bstack1ll_opy_ (u"ࠧࡵࡴࡸࡩࠬჭ")
def bstack1l11l11l11_opy_(val):
    return val.__str__().lower() == bstack1ll_opy_ (u"ࠨࡨࡤࡰࡸ࡫ࠧხ")
def bstack1l1lll1111_opy_(bstack1l1l1111l1_opy_=Exception, class_method=False, default_value=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except bstack1l1l1111l1_opy_ as e:
                print(bstack1ll_opy_ (u"ࠤࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡨࡸࡲࡨࡺࡩࡰࡰࠣࡿࢂࠦ࠭࠿ࠢࡾࢁ࠿ࠦࡻࡾࠤჯ").format(func.__name__, bstack1l1l1111l1_opy_.__name__, str(e)))
                return default_value
        return wrapper
    def bstack1l111l1ll1_opy_(bstack1l11l111ll_opy_):
        def wrapped(cls, *args, **kwargs):
            try:
                return bstack1l11l111ll_opy_(cls, *args, **kwargs)
            except bstack1l1l1111l1_opy_ as e:
                print(bstack1ll_opy_ (u"ࠥࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡩࡹࡳࡩࡴࡪࡱࡱࠤࢀࢃࠠ࠮ࡀࠣࡿࢂࡀࠠࡼࡿࠥჰ").format(bstack1l11l111ll_opy_.__name__, bstack1l1l1111l1_opy_.__name__, str(e)))
                return default_value
        return wrapped
    if class_method:
        return bstack1l111l1ll1_opy_
    else:
        return decorator
def bstack1l111lll1_opy_(bstack1l1lll1lll_opy_):
    if bstack1ll_opy_ (u"ࠫࡦࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠨჱ") in bstack1l1lll1lll_opy_ and bstack1l11l11l11_opy_(bstack1l1lll1lll_opy_[bstack1ll_opy_ (u"ࠬࡧࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠩჲ")]):
        return False
    if bstack1ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠨჳ") in bstack1l1lll1lll_opy_ and bstack1l11l11l11_opy_(bstack1l1lll1lll_opy_[bstack1ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠩჴ")]):
        return False
    return True
def bstack1ll1ll11l1_opy_():
    try:
        from pytest_bdd import reporting
        return True
    except Exception as e:
        return False
def bstack1l1l1ll11_opy_(hub_url):
    if bstack1l1lllllll_opy_() <= version.parse(bstack1ll_opy_ (u"ࠨ࠵࠱࠵࠸࠴࠰ࠨჵ")):
        if hub_url != bstack1ll_opy_ (u"ࠩࠪჶ"):
            return bstack1ll_opy_ (u"ࠥ࡬ࡹࡺࡰ࠻࠱࠲ࠦჷ") + hub_url + bstack1ll_opy_ (u"ࠦ࠿࠾࠰࠰ࡹࡧ࠳࡭ࡻࡢࠣჸ")
        return bstack1ll1l11l11_opy_
    if hub_url != bstack1ll_opy_ (u"ࠬ࠭ჹ"):
        return bstack1ll_opy_ (u"ࠨࡨࡵࡶࡳࡷ࠿࠵࠯ࠣჺ") + hub_url + bstack1ll_opy_ (u"ࠢ࠰ࡹࡧ࠳࡭ࡻࡢࠣ჻")
    return bstack1llllll1ll_opy_
def bstack1l11llll1l_opy_():
    return isinstance(os.getenv(bstack1ll_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡑ࡛ࡗࡉࡘ࡚࡟ࡑࡎࡘࡋࡎࡔࠧჼ")), str)
def bstack1ll111ll_opy_(url):
    return urlparse(url).hostname
def bstack1l11l11l1_opy_(hostname):
    for bstack1lll1111l1_opy_ in bstack111l1l11l_opy_:
        regex = re.compile(bstack1lll1111l1_opy_)
        if regex.match(hostname):
            return True
    return False
def bstack1l11lll1ll_opy_(bstack1l11ll1l11_opy_, file_name, logger):
    bstack1l11ll1ll_opy_ = os.path.join(os.path.expanduser(bstack1ll_opy_ (u"ࠩࢁࠫჽ")), bstack1l11ll1l11_opy_)
    try:
        if not os.path.exists(bstack1l11ll1ll_opy_):
            os.makedirs(bstack1l11ll1ll_opy_)
        file_path = os.path.join(os.path.expanduser(bstack1ll_opy_ (u"ࠪࢂࠬჾ")), bstack1l11ll1l11_opy_, file_name)
        if not os.path.isfile(file_path):
            with open(file_path, bstack1ll_opy_ (u"ࠫࡼ࠭ჿ")):
                pass
            with open(file_path, bstack1ll_opy_ (u"ࠧࡽࠫࠣᄀ")) as outfile:
                json.dump({}, outfile)
        return file_path
    except Exception as e:
        logger.debug(bstack1l1l1l11_opy_.format(str(e)))
def bstack1l1l111ll1_opy_(file_name, key, value, logger):
    file_path = bstack1l11lll1ll_opy_(bstack1ll_opy_ (u"࠭࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠭ᄁ"), file_name, logger)
    if file_path != None:
        if os.path.exists(file_path):
            bstack11lllll1_opy_ = json.load(open(file_path, bstack1ll_opy_ (u"ࠧࡳࡤࠪᄂ")))
        else:
            bstack11lllll1_opy_ = {}
        bstack11lllll1_opy_[key] = value
        with open(file_path, bstack1ll_opy_ (u"ࠣࡹ࠮ࠦᄃ")) as outfile:
            json.dump(bstack11lllll1_opy_, outfile)
def bstack1l1ll1ll1_opy_(file_name, logger):
    file_path = bstack1l11lll1ll_opy_(bstack1ll_opy_ (u"ࠩ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠩᄄ"), file_name, logger)
    bstack11lllll1_opy_ = {}
    if file_path != None and os.path.exists(file_path):
        with open(file_path, bstack1ll_opy_ (u"ࠪࡶࠬᄅ")) as bstack1llllllll_opy_:
            bstack11lllll1_opy_ = json.load(bstack1llllllll_opy_)
    return bstack11lllll1_opy_
def bstack11111l11l_opy_(file_path, logger):
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
    except Exception as e:
        logger.debug(bstack1ll_opy_ (u"ࠫࡊࡸࡲࡰࡴࠣ࡭ࡳࠦࡤࡦ࡮ࡨࡸ࡮ࡴࡧࠡࡨ࡬ࡰࡪࡀࠠࠨᄆ") + file_path + bstack1ll_opy_ (u"ࠬࠦࠧᄇ") + str(e))
def bstack1l1lllllll_opy_():
    from selenium import webdriver
    return version.parse(webdriver.__version__)
class Notset:
    def __repr__(self):
        return bstack1ll_opy_ (u"ࠨ࠼ࡏࡑࡗࡗࡊ࡚࠾ࠣᄈ")
def bstack111lll111_opy_(config):
    if bstack1ll_opy_ (u"ࠧࡪࡵࡓࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹ࠭ᄉ") in config:
        del (config[bstack1ll_opy_ (u"ࠨ࡫ࡶࡔࡱࡧࡹࡸࡴ࡬࡫࡭ࡺࠧᄊ")])
        return False
    if bstack1l1lllllll_opy_() < version.parse(bstack1ll_opy_ (u"ࠩ࠶࠲࠹࠴࠰ࠨᄋ")):
        return False
    if bstack1l1lllllll_opy_() >= version.parse(bstack1ll_opy_ (u"ࠪ࠸࠳࠷࠮࠶ࠩᄌ")):
        return True
    if bstack1ll_opy_ (u"ࠫࡺࡹࡥࡘ࠵ࡆࠫᄍ") in config and config[bstack1ll_opy_ (u"ࠬࡻࡳࡦ࡙࠶ࡇࠬᄎ")] is False:
        return False
    else:
        return True
def bstack1ll11ll111_opy_(args_list, bstack1l111l1lll_opy_):
    index = -1
    for value in bstack1l111l1lll_opy_:
        try:
            index = args_list.index(value)
            return index
        except Exception as e:
            return index
    return index
class Result:
    def __init__(self, result=None, duration=None, exception=None, bstack1l1l111lll_opy_=None):
        self.result = result
        self.duration = duration
        self.exception = exception
        self.exception_type = type(self.exception).__name__ if exception else None
        self.bstack1l1l111lll_opy_ = bstack1l1l111lll_opy_
    @classmethod
    def passed(cls):
        return Result(result=bstack1ll_opy_ (u"࠭ࡰࡢࡵࡶࡩࡩ࠭ᄏ"))
    @classmethod
    def failed(cls, exception=None):
        return Result(result=bstack1ll_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧᄐ"), exception=exception)
    def bstack1l11l111l1_opy_(self):
        if self.result != bstack1ll_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨᄑ"):
            return None
        if bstack1ll_opy_ (u"ࠤࡄࡷࡸ࡫ࡲࡵ࡫ࡲࡲࠧᄒ") in self.exception_type:
            return bstack1ll_opy_ (u"ࠥࡅࡸࡹࡥࡳࡶ࡬ࡳࡳࡋࡲࡳࡱࡵࠦᄓ")
        return bstack1ll_opy_ (u"࡚ࠦࡴࡨࡢࡰࡧࡰࡪࡪࡅࡳࡴࡲࡶࠧᄔ")
    def bstack1l1l111l11_opy_(self):
        if self.result != bstack1ll_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬᄕ"):
            return None
        if self.bstack1l1l111lll_opy_:
            return self.bstack1l1l111lll_opy_
        return bstack1l1l111111_opy_(self.exception)
def bstack1l1l111111_opy_(exc):
    return traceback.format_exception(exc)
def bstack1l11ll111l_opy_(message):
    if isinstance(message, str):
        return not bool(message and message.strip())
    return True
def bstack1llll11l_opy_(object, key, default_value):
    if key in object.__dict__.keys():
        return object.__dict__.get(key)
    return default_value
def bstack1ll11l1lll_opy_(config, logger):
    try:
        import playwright
        bstack1l11lll11l_opy_ = playwright.__file__
        bstack1l1l1111ll_opy_ = os.path.split(bstack1l11lll11l_opy_)
        bstack1l11l1llll_opy_ = bstack1l1l1111ll_opy_[0] + bstack1ll_opy_ (u"࠭࠯ࡥࡴ࡬ࡺࡪࡸ࠯ࡱࡣࡦ࡯ࡦ࡭ࡥ࠰࡮࡬ࡦ࠴ࡩ࡬ࡪ࠱ࡦࡰ࡮࠴ࡪࡴࠩᄖ")
        os.environ[bstack1ll_opy_ (u"ࠧࡈࡎࡒࡆࡆࡒ࡟ࡂࡉࡈࡒ࡙ࡥࡈࡕࡖࡓࡣࡕࡘࡏ࡙࡛ࠪᄗ")] = bstack1l111ll11_opy_(config)
        with open(bstack1l11l1llll_opy_, bstack1ll_opy_ (u"ࠨࡴࠪᄘ")) as f:
            bstack1l11ll11_opy_ = f.read()
            bstack1l1l11111l_opy_ = bstack1ll_opy_ (u"ࠩࡪࡰࡴࡨࡡ࡭࠯ࡤ࡫ࡪࡴࡴࠨᄙ")
            bstack1l11l11lll_opy_ = bstack1l11ll11_opy_.find(bstack1l1l11111l_opy_)
            if bstack1l11l11lll_opy_ is -1:
              process = subprocess.Popen(bstack1ll_opy_ (u"ࠥࡲࡵࡳࠠࡪࡰࡶࡸࡦࡲ࡬ࠡࡩ࡯ࡳࡧࡧ࡬࠮ࡣࡪࡩࡳࡺࠢᄚ"), shell=True, cwd=bstack1l1l1111ll_opy_[0])
              process.wait()
              bstack1l11ll1lll_opy_ = bstack1ll_opy_ (u"ࠫࠧࡻࡳࡦࠢࡶࡸࡷ࡯ࡣࡵࠤ࠾ࠫᄛ")
              bstack1l11lll111_opy_ = bstack1ll_opy_ (u"ࠧࠨࠢࠡ࡞ࠥࡹࡸ࡫ࠠࡴࡶࡵ࡭ࡨࡺ࡜ࠣ࠽ࠣࡧࡴࡴࡳࡵࠢࡾࠤࡧࡵ࡯ࡵࡵࡷࡶࡦࡶࠠࡾࠢࡀࠤࡷ࡫ࡱࡶ࡫ࡵࡩ࠭࠭ࡧ࡭ࡱࡥࡥࡱ࠳ࡡࡨࡧࡱࡸࠬ࠯࠻ࠡ࡫ࡩࠤ࠭ࡶࡲࡰࡥࡨࡷࡸ࠴ࡥ࡯ࡸ࠱ࡋࡑࡕࡂࡂࡎࡢࡅࡌࡋࡎࡕࡡࡋࡘ࡙ࡖ࡟ࡑࡔࡒ࡜࡞࠯ࠠࡣࡱࡲࡸࡸࡺࡲࡢࡲࠫ࠭ࡀࠦࠢࠣࠤᄜ")
              bstack1l11ll1l1l_opy_ = bstack1l11ll11_opy_.replace(bstack1l11ll1lll_opy_, bstack1l11lll111_opy_)
              with open(bstack1l11l1llll_opy_, bstack1ll_opy_ (u"࠭ࡷࠨᄝ")) as f:
                f.write(bstack1l11ll1l1l_opy_)
    except Exception as e:
        logger.error(bstack111l1llll_opy_.format(str(e)))
def bstack11llll11l_opy_():
  try:
    bstack1l111ll1l1_opy_ = os.path.join(tempfile.gettempdir(), bstack1ll_opy_ (u"ࠧࡰࡲࡷ࡭ࡲࡧ࡬ࡠࡪࡸࡦࡤࡻࡲ࡭࠰࡭ࡷࡴࡴࠧᄞ"))
    bstack1l111llll1_opy_ = []
    if os.path.exists(bstack1l111ll1l1_opy_):
      with open(bstack1l111ll1l1_opy_) as f:
        bstack1l111llll1_opy_ = json.load(f)
      os.remove(bstack1l111ll1l1_opy_)
    return bstack1l111llll1_opy_
  except:
    pass
  return []
def bstack1lll11l1_opy_(bstack111l111l1_opy_):
  try:
    bstack1l111llll1_opy_ = []
    bstack1l111ll1l1_opy_ = os.path.join(tempfile.gettempdir(), bstack1ll_opy_ (u"ࠨࡱࡳࡸ࡮ࡳࡡ࡭ࡡ࡫ࡹࡧࡥࡵࡳ࡮࠱࡮ࡸࡵ࡮ࠨᄟ"))
    if os.path.exists(bstack1l111ll1l1_opy_):
      with open(bstack1l111ll1l1_opy_) as f:
        bstack1l111llll1_opy_ = json.load(f)
    bstack1l111llll1_opy_.append(bstack111l111l1_opy_)
    with open(bstack1l111ll1l1_opy_, bstack1ll_opy_ (u"ࠩࡺࠫᄠ")) as f:
        json.dump(bstack1l111llll1_opy_, f)
  except:
    pass
def bstack1ll11ll11_opy_(logger, bstack1l11l11111_opy_ = False):
  try:
    test_name = os.environ.get(bstack1ll_opy_ (u"ࠪࡔ࡞࡚ࡅࡔࡖࡢࡘࡊ࡙ࡔࡠࡐࡄࡑࡊ࠭ᄡ"), bstack1ll_opy_ (u"ࠫࠬᄢ"))
    if test_name == bstack1ll_opy_ (u"ࠬ࠭ᄣ"):
        test_name = threading.current_thread().__dict__.get(bstack1ll_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹࡈࡤࡥࡡࡷࡩࡸࡺ࡟࡯ࡣࡰࡩࠬᄤ"), bstack1ll_opy_ (u"ࠧࠨᄥ"))
    bstack1l11l1lll1_opy_ = bstack1ll_opy_ (u"ࠨ࠮ࠣࠫᄦ").join(threading.current_thread().bstackTestErrorMessages)
    if bstack1l11l11111_opy_:
        bstack1l1l1l1l_opy_ = os.environ.get(bstack1ll_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡒࡏࡅ࡙ࡌࡏࡓࡏࡢࡍࡓࡊࡅ࡙ࠩᄧ"), bstack1ll_opy_ (u"ࠪ࠴ࠬᄨ"))
        bstack1ll1l1l1ll_opy_ = {bstack1ll_opy_ (u"ࠫࡳࡧ࡭ࡦࠩᄩ"): test_name, bstack1ll_opy_ (u"ࠬ࡫ࡲࡳࡱࡵࠫᄪ"): bstack1l11l1lll1_opy_, bstack1ll_opy_ (u"࠭ࡩ࡯ࡦࡨࡼࠬᄫ"): bstack1l1l1l1l_opy_}
        bstack1l111ll1ll_opy_ = []
        bstack1l11l1ll1l_opy_ = os.path.join(tempfile.gettempdir(), bstack1ll_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺ࡟ࡱࡲࡳࡣࡪࡸࡲࡰࡴࡢࡰ࡮ࡹࡴ࠯࡬ࡶࡳࡳ࠭ᄬ"))
        if os.path.exists(bstack1l11l1ll1l_opy_):
            with open(bstack1l11l1ll1l_opy_) as f:
                bstack1l111ll1ll_opy_ = json.load(f)
        bstack1l111ll1ll_opy_.append(bstack1ll1l1l1ll_opy_)
        with open(bstack1l11l1ll1l_opy_, bstack1ll_opy_ (u"ࠨࡹࠪᄭ")) as f:
            json.dump(bstack1l111ll1ll_opy_, f)
    else:
        bstack1ll1l1l1ll_opy_ = {bstack1ll_opy_ (u"ࠩࡱࡥࡲ࡫ࠧᄮ"): test_name, bstack1ll_opy_ (u"ࠪࡩࡷࡸ࡯ࡳࠩᄯ"): bstack1l11l1lll1_opy_, bstack1ll_opy_ (u"ࠫ࡮ࡴࡤࡦࡺࠪᄰ"): str(multiprocessing.current_process().name)}
        if bstack1ll_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯ࡤ࡫ࡲࡳࡱࡵࡣࡱ࡯ࡳࡵࠩᄱ") not in multiprocessing.current_process().__dict__.keys():
            multiprocessing.current_process().bstack1ll1ll111_opy_ = []
        multiprocessing.current_process().bstack1ll1ll111_opy_.append(bstack1ll1l1l1ll_opy_)
  except Exception as e:
      logger.warn(bstack1ll_opy_ (u"ࠨࡕ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡶࡸࡴࡸࡥࠡࡲࡼࡸࡪࡹࡴࠡࡨࡸࡲࡳ࡫࡬ࠡࡦࡤࡸࡦࡀࠠࡼࡿࠥᄲ").format(e))
def bstack1ll111ll1_opy_(error_message, test_name, index, logger):
  try:
    bstack1l11l1111l_opy_ = []
    bstack1ll1l1l1ll_opy_ = {bstack1ll_opy_ (u"ࠧ࡯ࡣࡰࡩࠬᄳ"): test_name, bstack1ll_opy_ (u"ࠨࡧࡵࡶࡴࡸࠧᄴ"): error_message, bstack1ll_opy_ (u"ࠩ࡬ࡲࡩ࡫ࡸࠨᄵ"): index}
    bstack1l111lll11_opy_ = os.path.join(tempfile.gettempdir(), bstack1ll_opy_ (u"ࠪࡶࡴࡨ࡯ࡵࡡࡨࡶࡷࡵࡲࡠ࡮࡬ࡷࡹ࠴ࡪࡴࡱࡱࠫᄶ"))
    if os.path.exists(bstack1l111lll11_opy_):
        with open(bstack1l111lll11_opy_) as f:
            bstack1l11l1111l_opy_ = json.load(f)
    bstack1l11l1111l_opy_.append(bstack1ll1l1l1ll_opy_)
    with open(bstack1l111lll11_opy_, bstack1ll_opy_ (u"ࠫࡼ࠭ᄷ")) as f:
        json.dump(bstack1l11l1111l_opy_, f)
  except Exception as e:
    logger.warn(bstack1ll_opy_ (u"࡛ࠧ࡮ࡢࡤ࡯ࡩࠥࡺ࡯ࠡࡵࡷࡳࡷ࡫ࠠࡳࡱࡥࡳࡹࠦࡦࡶࡰࡱࡩࡱࠦࡤࡢࡶࡤ࠾ࠥࢁࡽࠣᄸ").format(e))
def bstack1l11l1ll1_opy_(bstack1ll1lll1ll_opy_, name, logger):
  try:
    bstack1ll1l1l1ll_opy_ = {bstack1ll_opy_ (u"࠭࡮ࡢ࡯ࡨࠫᄹ"): name, bstack1ll_opy_ (u"ࠧࡦࡴࡵࡳࡷ࠭ᄺ"): bstack1ll1lll1ll_opy_, bstack1ll_opy_ (u"ࠨ࡫ࡱࡨࡪࡾࠧᄻ"): str(threading.current_thread()._name)}
    return bstack1ll1l1l1ll_opy_
  except Exception as e:
    logger.warn(bstack1ll_opy_ (u"ࠤࡘࡲࡦࡨ࡬ࡦࠢࡷࡳࠥࡹࡴࡰࡴࡨࠤࡧ࡫ࡨࡢࡸࡨࠤ࡫ࡻ࡮࡯ࡧ࡯ࠤࡩࡧࡴࡢ࠼ࠣࡿࢂࠨᄼ").format(e))
  return