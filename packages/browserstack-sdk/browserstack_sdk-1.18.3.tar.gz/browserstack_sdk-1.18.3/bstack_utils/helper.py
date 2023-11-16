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
import datetime
import json
import os
import platform
import re
import subprocess
import traceback
from urllib.parse import urlparse
import git
import requests
from packaging import version
from bstack_utils.config import Config
from bstack_utils.constants import bstack1l1l1llll1_opy_, bstack1ll1l1l1l_opy_, bstack11ll11l1l_opy_, bstack1ll11l1ll_opy_
from bstack_utils.messages import bstack1ll11ll1l1_opy_, bstack1ll1l1ll1_opy_
from bstack_utils.proxy import bstack11ll1l1ll_opy_, bstack1l1ll11ll_opy_
bstack1ll1l1llll_opy_ = Config.get_instance()
def bstack1l1lllll1l_opy_(config):
    return config[bstack111ll1l_opy_ (u"ࠧࡶࡵࡨࡶࡓࡧ࡭ࡦࠩྖ")]
def bstack1l1llll1ll_opy_(config):
    return config[bstack111ll1l_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡌࡧࡼࠫྗ")]
def bstack111l11ll_opy_():
    try:
        import playwright
        return True
    except ImportError:
        return False
def bstack1l1l1111l1_opy_(obj):
    values = []
    bstack1l1l1l1lll_opy_ = re.compile(bstack111ll1l_opy_ (u"ࡴࠥࡢࡈ࡛ࡓࡕࡑࡐࡣ࡙ࡇࡇࡠ࡞ࡧ࠯ࠩࠨ྘"), re.I)
    for key in obj.keys():
        if bstack1l1l1l1lll_opy_.match(key):
            values.append(obj[key])
    return values
def bstack1l1l11llll_opy_(config):
    tags = []
    tags.extend(bstack1l1l1111l1_opy_(os.environ))
    tags.extend(bstack1l1l1111l1_opy_(config))
    return tags
def bstack1l1l11lll1_opy_(markers):
    tags = []
    for marker in markers:
        tags.append(marker.name)
    return tags
def bstack1l1l11l1ll_opy_(bstack1l11lll111_opy_):
    if not bstack1l11lll111_opy_:
        return bstack111ll1l_opy_ (u"ࠪࠫྙ")
    return bstack111ll1l_opy_ (u"ࠦࢀࢃࠠࠩࡽࢀ࠭ࠧྚ").format(bstack1l11lll111_opy_.name, bstack1l11lll111_opy_.email)
def bstack1l1ll1ll11_opy_():
    try:
        repo = git.Repo(search_parent_directories=True)
        bstack1l1l111ll1_opy_ = repo.common_dir
        info = {
            bstack111ll1l_opy_ (u"ࠧࡹࡨࡢࠤྛ"): repo.head.commit.hexsha,
            bstack111ll1l_opy_ (u"ࠨࡳࡩࡱࡵࡸࡤࡹࡨࡢࠤྜ"): repo.git.rev_parse(repo.head.commit, short=True),
            bstack111ll1l_opy_ (u"ࠢࡣࡴࡤࡲࡨ࡮ࠢྜྷ"): repo.active_branch.name,
            bstack111ll1l_opy_ (u"ࠣࡶࡤ࡫ࠧྞ"): repo.git.describe(all=True, tags=True, exact_match=True),
            bstack111ll1l_opy_ (u"ࠤࡦࡳࡲࡳࡩࡵࡶࡨࡶࠧྟ"): bstack1l1l11l1ll_opy_(repo.head.commit.committer),
            bstack111ll1l_opy_ (u"ࠥࡧࡴࡳ࡭ࡪࡶࡷࡩࡷࡥࡤࡢࡶࡨࠦྠ"): repo.head.commit.committed_datetime.isoformat(),
            bstack111ll1l_opy_ (u"ࠦࡦࡻࡴࡩࡱࡵࠦྡ"): bstack1l1l11l1ll_opy_(repo.head.commit.author),
            bstack111ll1l_opy_ (u"ࠧࡧࡵࡵࡪࡲࡶࡤࡪࡡࡵࡧࠥྡྷ"): repo.head.commit.authored_datetime.isoformat(),
            bstack111ll1l_opy_ (u"ࠨࡣࡰ࡯ࡰ࡭ࡹࡥ࡭ࡦࡵࡶࡥ࡬࡫ࠢྣ"): repo.head.commit.message,
            bstack111ll1l_opy_ (u"ࠢࡳࡱࡲࡸࠧྤ"): repo.git.rev_parse(bstack111ll1l_opy_ (u"ࠣ࠯࠰ࡷ࡭ࡵࡷ࠮ࡶࡲࡴࡱ࡫ࡶࡦ࡮ࠥྥ")),
            bstack111ll1l_opy_ (u"ࠤࡦࡳࡲࡳ࡯࡯ࡡࡪ࡭ࡹࡥࡤࡪࡴࠥྦ"): bstack1l1l111ll1_opy_,
            bstack111ll1l_opy_ (u"ࠥࡻࡴࡸ࡫ࡵࡴࡨࡩࡤ࡭ࡩࡵࡡࡧ࡭ࡷࠨྦྷ"): subprocess.check_output([bstack111ll1l_opy_ (u"ࠦ࡬࡯ࡴࠣྨ"), bstack111ll1l_opy_ (u"ࠧࡸࡥࡷ࠯ࡳࡥࡷࡹࡥࠣྩ"), bstack111ll1l_opy_ (u"ࠨ࠭࠮ࡩ࡬ࡸ࠲ࡩ࡯࡮࡯ࡲࡲ࠲ࡪࡩࡳࠤྪ")]).strip().decode(
                bstack111ll1l_opy_ (u"ࠧࡶࡶࡩ࠱࠽࠭ྫ")),
            bstack111ll1l_opy_ (u"ࠣ࡮ࡤࡷࡹࡥࡴࡢࡩࠥྫྷ"): repo.git.describe(tags=True, abbrev=0, always=True),
            bstack111ll1l_opy_ (u"ࠤࡦࡳࡲࡳࡩࡵࡵࡢࡷ࡮ࡴࡣࡦࡡ࡯ࡥࡸࡺ࡟ࡵࡣࡪࠦྭ"): repo.git.rev_list(
                bstack111ll1l_opy_ (u"ࠥࡿࢂ࠴࠮ࡼࡿࠥྮ").format(repo.head.commit, repo.git.describe(tags=True, abbrev=0, always=True)), count=True)
        }
        remotes = repo.remotes
        bstack1l11lll1ll_opy_ = []
        for remote in remotes:
            bstack1l1l11111l_opy_ = {
                bstack111ll1l_opy_ (u"ࠦࡳࡧ࡭ࡦࠤྯ"): remote.name,
                bstack111ll1l_opy_ (u"ࠧࡻࡲ࡭ࠤྰ"): remote.url,
            }
            bstack1l11lll1ll_opy_.append(bstack1l1l11111l_opy_)
        return {
            bstack111ll1l_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦྱ"): bstack111ll1l_opy_ (u"ࠢࡨ࡫ࡷࠦྲ"),
            **info,
            bstack111ll1l_opy_ (u"ࠣࡴࡨࡱࡴࡺࡥࡴࠤླ"): bstack1l11lll1ll_opy_
        }
    except Exception as err:
        print(bstack111ll1l_opy_ (u"ࠤࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡲࡲࡴࡺࡲࡡࡵ࡫ࡱ࡫ࠥࡍࡩࡵࠢࡰࡩࡹࡧࡤࡢࡶࡤࠤࡼ࡯ࡴࡩࠢࡨࡶࡷࡵࡲ࠻ࠢࡾࢁࠧྴ").format(err))
        return {}
def bstack1ll111111_opy_():
    env = os.environ
    if (bstack111ll1l_opy_ (u"ࠥࡎࡊࡔࡋࡊࡐࡖࡣ࡚ࡘࡌࠣྵ") in env and len(env[bstack111ll1l_opy_ (u"ࠦࡏࡋࡎࡌࡋࡑࡗࡤ࡛ࡒࡍࠤྶ")]) > 0) or (
            bstack111ll1l_opy_ (u"ࠧࡐࡅࡏࡍࡌࡒࡘࡥࡈࡐࡏࡈࠦྷ") in env and len(env[bstack111ll1l_opy_ (u"ࠨࡊࡆࡐࡎࡍࡓ࡙࡟ࡉࡑࡐࡉࠧྸ")]) > 0):
        return {
            bstack111ll1l_opy_ (u"ࠢ࡯ࡣࡰࡩࠧྐྵ"): bstack111ll1l_opy_ (u"ࠣࡌࡨࡲࡰ࡯࡮ࡴࠤྺ"),
            bstack111ll1l_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧྻ"): env.get(bstack111ll1l_opy_ (u"ࠥࡆ࡚ࡏࡌࡅࡡࡘࡖࡑࠨྼ")),
            bstack111ll1l_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨ྽"): env.get(bstack111ll1l_opy_ (u"ࠧࡐࡏࡃࡡࡑࡅࡒࡋࠢ྾")),
            bstack111ll1l_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶࠧ྿"): env.get(bstack111ll1l_opy_ (u"ࠢࡃࡗࡌࡐࡉࡥࡎࡖࡏࡅࡉࡗࠨ࿀"))
        }
    if env.get(bstack111ll1l_opy_ (u"ࠣࡅࡌࠦ࿁")) == bstack111ll1l_opy_ (u"ࠤࡷࡶࡺ࡫ࠢ࿂") and bstack1l1l11ll11_opy_(env.get(bstack111ll1l_opy_ (u"ࠥࡇࡎࡘࡃࡍࡇࡆࡍࠧ࿃"))):
        return {
            bstack111ll1l_opy_ (u"ࠦࡳࡧ࡭ࡦࠤ࿄"): bstack111ll1l_opy_ (u"ࠧࡉࡩࡳࡥ࡯ࡩࡈࡏࠢ࿅"),
            bstack111ll1l_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤ࿆"): env.get(bstack111ll1l_opy_ (u"ࠢࡄࡋࡕࡇࡑࡋ࡟ࡃࡗࡌࡐࡉࡥࡕࡓࡎࠥ࿇")),
            bstack111ll1l_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧࠥ࿈"): env.get(bstack111ll1l_opy_ (u"ࠤࡆࡍࡗࡉࡌࡆࡡࡍࡓࡇࠨ࿉")),
            bstack111ll1l_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠤ࿊"): env.get(bstack111ll1l_opy_ (u"ࠦࡈࡏࡒࡄࡎࡈࡣࡇ࡛ࡉࡍࡆࡢࡒ࡚ࡓࠢ࿋"))
        }
    if env.get(bstack111ll1l_opy_ (u"ࠧࡉࡉࠣ࿌")) == bstack111ll1l_opy_ (u"ࠨࡴࡳࡷࡨࠦ࿍") and bstack1l1l11ll11_opy_(env.get(bstack111ll1l_opy_ (u"ࠢࡕࡔࡄ࡚ࡎ࡙ࠢ࿎"))):
        return {
            bstack111ll1l_opy_ (u"ࠣࡰࡤࡱࡪࠨ࿏"): bstack111ll1l_opy_ (u"ࠤࡗࡶࡦࡼࡩࡴࠢࡆࡍࠧ࿐"),
            bstack111ll1l_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡸࡶࡱࠨ࿑"): env.get(bstack111ll1l_opy_ (u"࡙ࠦࡘࡁࡗࡋࡖࡣࡇ࡛ࡉࡍࡆࡢ࡛ࡊࡈ࡟ࡖࡔࡏࠦ࿒")),
            bstack111ll1l_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢ࿓"): env.get(bstack111ll1l_opy_ (u"ࠨࡔࡓࡃ࡙ࡍࡘࡥࡊࡐࡄࡢࡒࡆࡓࡅࠣ࿔")),
            bstack111ll1l_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨ࿕"): env.get(bstack111ll1l_opy_ (u"ࠣࡖࡕࡅ࡛ࡏࡓࡠࡄࡘࡍࡑࡊ࡟ࡏࡗࡐࡆࡊࡘࠢ࿖"))
        }
    if env.get(bstack111ll1l_opy_ (u"ࠤࡆࡍࠧ࿗")) == bstack111ll1l_opy_ (u"ࠥࡸࡷࡻࡥࠣ࿘") and env.get(bstack111ll1l_opy_ (u"ࠦࡈࡏ࡟ࡏࡃࡐࡉࠧ࿙")) == bstack111ll1l_opy_ (u"ࠧࡩ࡯ࡥࡧࡶ࡬࡮ࡶࠢ࿚"):
        return {
            bstack111ll1l_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦ࿛"): bstack111ll1l_opy_ (u"ࠢࡄࡱࡧࡩࡸ࡮ࡩࡱࠤ࿜"),
            bstack111ll1l_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟ࡶࡴ࡯ࠦ࿝"): None,
            bstack111ll1l_opy_ (u"ࠤ࡭ࡳࡧࡥ࡮ࡢ࡯ࡨࠦ࿞"): None,
            bstack111ll1l_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠤ࿟"): None
        }
    if env.get(bstack111ll1l_opy_ (u"ࠦࡇࡏࡔࡃࡗࡆࡏࡊ࡚࡟ࡃࡔࡄࡒࡈࡎࠢ࿠")) and env.get(bstack111ll1l_opy_ (u"ࠧࡈࡉࡕࡄࡘࡇࡐࡋࡔࡠࡅࡒࡑࡒࡏࡔࠣ࿡")):
        return {
            bstack111ll1l_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦ࿢"): bstack111ll1l_opy_ (u"ࠢࡃ࡫ࡷࡦࡺࡩ࡫ࡦࡶࠥ࿣"),
            bstack111ll1l_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟ࡶࡴ࡯ࠦ࿤"): env.get(bstack111ll1l_opy_ (u"ࠤࡅࡍ࡙ࡈࡕࡄࡍࡈࡘࡤࡍࡉࡕࡡࡋࡘ࡙ࡖ࡟ࡐࡔࡌࡋࡎࡔࠢ࿥")),
            bstack111ll1l_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧ࿦"): None,
            bstack111ll1l_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴࠥ࿧"): env.get(bstack111ll1l_opy_ (u"ࠧࡈࡉࡕࡄࡘࡇࡐࡋࡔࡠࡄࡘࡍࡑࡊ࡟ࡏࡗࡐࡆࡊࡘࠢ࿨"))
        }
    if env.get(bstack111ll1l_opy_ (u"ࠨࡃࡊࠤ࿩")) == bstack111ll1l_opy_ (u"ࠢࡵࡴࡸࡩࠧ࿪") and bstack1l1l11ll11_opy_(env.get(bstack111ll1l_opy_ (u"ࠣࡆࡕࡓࡓࡋࠢ࿫"))):
        return {
            bstack111ll1l_opy_ (u"ࠤࡱࡥࡲ࡫ࠢ࿬"): bstack111ll1l_opy_ (u"ࠥࡈࡷࡵ࡮ࡦࠤ࿭"),
            bstack111ll1l_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲࠢ࿮"): env.get(bstack111ll1l_opy_ (u"ࠧࡊࡒࡐࡐࡈࡣࡇ࡛ࡉࡍࡆࡢࡐࡎࡔࡋࠣ࿯")),
            bstack111ll1l_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥࠣ࿰"): None,
            bstack111ll1l_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨ࿱"): env.get(bstack111ll1l_opy_ (u"ࠣࡆࡕࡓࡓࡋ࡟ࡃࡗࡌࡐࡉࡥࡎࡖࡏࡅࡉࡗࠨ࿲"))
        }
    if env.get(bstack111ll1l_opy_ (u"ࠤࡆࡍࠧ࿳")) == bstack111ll1l_opy_ (u"ࠥࡸࡷࡻࡥࠣ࿴") and bstack1l1l11ll11_opy_(env.get(bstack111ll1l_opy_ (u"ࠦࡘࡋࡍࡂࡒࡋࡓࡗࡋࠢ࿵"))):
        return {
            bstack111ll1l_opy_ (u"ࠧࡴࡡ࡮ࡧࠥ࿶"): bstack111ll1l_opy_ (u"ࠨࡓࡦ࡯ࡤࡴ࡭ࡵࡲࡦࠤ࿷"),
            bstack111ll1l_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥ࿸"): env.get(bstack111ll1l_opy_ (u"ࠣࡕࡈࡑࡆࡖࡈࡐࡔࡈࡣࡔࡘࡇࡂࡐࡌ࡞ࡆ࡚ࡉࡐࡐࡢ࡙ࡗࡒࠢ࿹")),
            bstack111ll1l_opy_ (u"ࠤ࡭ࡳࡧࡥ࡮ࡢ࡯ࡨࠦ࿺"): env.get(bstack111ll1l_opy_ (u"ࠥࡗࡊࡓࡁࡑࡊࡒࡖࡊࡥࡊࡐࡄࡢࡒࡆࡓࡅࠣ࿻")),
            bstack111ll1l_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴࠥ࿼"): env.get(bstack111ll1l_opy_ (u"࡙ࠧࡅࡎࡃࡓࡌࡔࡘࡅࡠࡌࡒࡆࡤࡏࡄࠣ࿽"))
        }
    if env.get(bstack111ll1l_opy_ (u"ࠨࡃࡊࠤ࿾")) == bstack111ll1l_opy_ (u"ࠢࡵࡴࡸࡩࠧ࿿") and bstack1l1l11ll11_opy_(env.get(bstack111ll1l_opy_ (u"ࠣࡉࡌࡘࡑࡇࡂࡠࡅࡌࠦက"))):
        return {
            bstack111ll1l_opy_ (u"ࠤࡱࡥࡲ࡫ࠢခ"): bstack111ll1l_opy_ (u"ࠥࡋ࡮ࡺࡌࡢࡤࠥဂ"),
            bstack111ll1l_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲࠢဃ"): env.get(bstack111ll1l_opy_ (u"ࠧࡉࡉࡠࡌࡒࡆࡤ࡛ࡒࡍࠤင")),
            bstack111ll1l_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥࠣစ"): env.get(bstack111ll1l_opy_ (u"ࠢࡄࡋࡢࡎࡔࡈ࡟ࡏࡃࡐࡉࠧဆ")),
            bstack111ll1l_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠢဇ"): env.get(bstack111ll1l_opy_ (u"ࠤࡆࡍࡤࡐࡏࡃࡡࡌࡈࠧဈ"))
        }
    if env.get(bstack111ll1l_opy_ (u"ࠥࡇࡎࠨဉ")) == bstack111ll1l_opy_ (u"ࠦࡹࡸࡵࡦࠤည") and bstack1l1l11ll11_opy_(env.get(bstack111ll1l_opy_ (u"ࠧࡈࡕࡊࡎࡇࡏࡎ࡚ࡅࠣဋ"))):
        return {
            bstack111ll1l_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦဌ"): bstack111ll1l_opy_ (u"ࠢࡃࡷ࡬ࡰࡩࡱࡩࡵࡧࠥဍ"),
            bstack111ll1l_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟ࡶࡴ࡯ࠦဎ"): env.get(bstack111ll1l_opy_ (u"ࠤࡅ࡙ࡎࡒࡄࡌࡋࡗࡉࡤࡈࡕࡊࡎࡇࡣ࡚ࡘࡌࠣဏ")),
            bstack111ll1l_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧတ"): env.get(bstack111ll1l_opy_ (u"ࠦࡇ࡛ࡉࡍࡆࡎࡍ࡙ࡋ࡟ࡍࡃࡅࡉࡑࠨထ")) or env.get(bstack111ll1l_opy_ (u"ࠧࡈࡕࡊࡎࡇࡏࡎ࡚ࡅࡠࡒࡌࡔࡊࡒࡉࡏࡇࡢࡒࡆࡓࡅࠣဒ")),
            bstack111ll1l_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶࠧဓ"): env.get(bstack111ll1l_opy_ (u"ࠢࡃࡗࡌࡐࡉࡑࡉࡕࡇࡢࡆ࡚ࡏࡌࡅࡡࡑ࡙ࡒࡈࡅࡓࠤန"))
        }
    if bstack1l1l11ll11_opy_(env.get(bstack111ll1l_opy_ (u"ࠣࡖࡉࡣࡇ࡛ࡉࡍࡆࠥပ"))):
        return {
            bstack111ll1l_opy_ (u"ࠤࡱࡥࡲ࡫ࠢဖ"): bstack111ll1l_opy_ (u"࡚ࠥ࡮ࡹࡵࡢ࡮ࠣࡗࡹࡻࡤࡪࡱࠣࡘࡪࡧ࡭ࠡࡕࡨࡶࡻ࡯ࡣࡦࡵࠥဗ"),
            bstack111ll1l_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲࠢဘ"): bstack111ll1l_opy_ (u"ࠧࢁࡽࡼࡿࠥမ").format(env.get(bstack111ll1l_opy_ (u"࠭ࡓ࡚ࡕࡗࡉࡒࡥࡔࡆࡃࡐࡊࡔ࡛ࡎࡅࡃࡗࡍࡔࡔࡓࡆࡔ࡙ࡉࡗ࡛ࡒࡊࠩယ")), env.get(bstack111ll1l_opy_ (u"ࠧࡔ࡛ࡖࡘࡊࡓ࡟ࡕࡇࡄࡑࡕࡘࡏࡋࡇࡆࡘࡎࡊࠧရ"))),
            bstack111ll1l_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧࠥလ"): env.get(bstack111ll1l_opy_ (u"ࠤࡖ࡝ࡘ࡚ࡅࡎࡡࡇࡉࡋࡏࡎࡊࡖࡌࡓࡓࡏࡄࠣဝ")),
            bstack111ll1l_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠤသ"): env.get(bstack111ll1l_opy_ (u"ࠦࡇ࡛ࡉࡍࡆࡢࡆ࡚ࡏࡌࡅࡋࡇࠦဟ"))
        }
    if bstack1l1l11ll11_opy_(env.get(bstack111ll1l_opy_ (u"ࠧࡇࡐࡑࡘࡈ࡝ࡔࡘࠢဠ"))):
        return {
            bstack111ll1l_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦအ"): bstack111ll1l_opy_ (u"ࠢࡂࡲࡳࡺࡪࡿ࡯ࡳࠤဢ"),
            bstack111ll1l_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟ࡶࡴ࡯ࠦဣ"): bstack111ll1l_opy_ (u"ࠤࡾࢁ࠴ࡶࡲࡰ࡬ࡨࡧࡹ࠵ࡻࡾ࠱ࡾࢁ࠴ࡨࡵࡪ࡮ࡧࡷ࠴ࢁࡽࠣဤ").format(env.get(bstack111ll1l_opy_ (u"ࠪࡅࡕࡖࡖࡆ࡛ࡒࡖࡤ࡛ࡒࡍࠩဥ")), env.get(bstack111ll1l_opy_ (u"ࠫࡆࡖࡐࡗࡇ࡜ࡓࡗࡥࡁࡄࡅࡒ࡙ࡓ࡚࡟ࡏࡃࡐࡉࠬဦ")), env.get(bstack111ll1l_opy_ (u"ࠬࡇࡐࡑࡘࡈ࡝ࡔࡘ࡟ࡑࡔࡒࡎࡊࡉࡔࡠࡕࡏ࡙ࡌ࠭ဧ")), env.get(bstack111ll1l_opy_ (u"࠭ࡁࡑࡒ࡙ࡉ࡞ࡕࡒࡠࡄࡘࡍࡑࡊ࡟ࡊࡆࠪဨ"))),
            bstack111ll1l_opy_ (u"ࠢ࡫ࡱࡥࡣࡳࡧ࡭ࡦࠤဩ"): env.get(bstack111ll1l_opy_ (u"ࠣࡃࡓࡔ࡛ࡋ࡙ࡐࡔࡢࡎࡔࡈ࡟ࡏࡃࡐࡉࠧဪ")),
            bstack111ll1l_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣါ"): env.get(bstack111ll1l_opy_ (u"ࠥࡅࡕࡖࡖࡆ࡛ࡒࡖࡤࡈࡕࡊࡎࡇࡣࡓ࡛ࡍࡃࡇࡕࠦာ"))
        }
    if env.get(bstack111ll1l_opy_ (u"ࠦࡆࡠࡕࡓࡇࡢࡌ࡙࡚ࡐࡠࡗࡖࡉࡗࡥࡁࡈࡇࡑࡘࠧိ")) and env.get(bstack111ll1l_opy_ (u"࡚ࠧࡆࡠࡄࡘࡍࡑࡊࠢီ")):
        return {
            bstack111ll1l_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦု"): bstack111ll1l_opy_ (u"ࠢࡂࡼࡸࡶࡪࠦࡃࡊࠤူ"),
            bstack111ll1l_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟ࡶࡴ࡯ࠦေ"): bstack111ll1l_opy_ (u"ࠤࡾࢁࢀࢃ࠯ࡠࡤࡸ࡭ࡱࡪ࠯ࡳࡧࡶࡹࡱࡺࡳࡀࡤࡸ࡭ࡱࡪࡉࡥ࠿ࡾࢁࠧဲ").format(env.get(bstack111ll1l_opy_ (u"ࠪࡗ࡞࡙ࡔࡆࡏࡢࡘࡊࡇࡍࡇࡑࡘࡒࡉࡇࡔࡊࡑࡑࡗࡊࡘࡖࡆࡔࡘࡖࡎ࠭ဳ")), env.get(bstack111ll1l_opy_ (u"ࠫࡘ࡟ࡓࡕࡇࡐࡣ࡙ࡋࡁࡎࡒࡕࡓࡏࡋࡃࡕࠩဴ")), env.get(bstack111ll1l_opy_ (u"ࠬࡈࡕࡊࡎࡇࡣࡇ࡛ࡉࡍࡆࡌࡈࠬဵ"))),
            bstack111ll1l_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥࠣံ"): env.get(bstack111ll1l_opy_ (u"ࠢࡃࡗࡌࡐࡉࡥࡂࡖࡋࡏࡈࡎࡊ့ࠢ")),
            bstack111ll1l_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠢး"): env.get(bstack111ll1l_opy_ (u"ࠤࡅ࡙ࡎࡒࡄࡠࡄࡘࡍࡑࡊࡉࡅࠤ္"))
        }
    if any([env.get(bstack111ll1l_opy_ (u"ࠥࡇࡔࡊࡅࡃࡗࡌࡐࡉࡥࡂࡖࡋࡏࡈࡤࡏࡄ်ࠣ")), env.get(bstack111ll1l_opy_ (u"ࠦࡈࡕࡄࡆࡄࡘࡍࡑࡊ࡟ࡓࡇࡖࡓࡑ࡜ࡅࡅࡡࡖࡓ࡚ࡘࡃࡆࡡ࡙ࡉࡗ࡙ࡉࡐࡐࠥျ")), env.get(bstack111ll1l_opy_ (u"ࠧࡉࡏࡅࡇࡅ࡙ࡎࡒࡄࡠࡕࡒ࡙ࡗࡉࡅࡠࡘࡈࡖࡘࡏࡏࡏࠤြ"))]):
        return {
            bstack111ll1l_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦွ"): bstack111ll1l_opy_ (u"ࠢࡂ࡙ࡖࠤࡈࡵࡤࡦࡄࡸ࡭ࡱࡪࠢှ"),
            bstack111ll1l_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟ࡶࡴ࡯ࠦဿ"): env.get(bstack111ll1l_opy_ (u"ࠤࡆࡓࡉࡋࡂࡖࡋࡏࡈࡤࡖࡕࡃࡎࡌࡇࡤࡈࡕࡊࡎࡇࡣ࡚ࡘࡌࠣ၀")),
            bstack111ll1l_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧ၁"): env.get(bstack111ll1l_opy_ (u"ࠦࡈࡕࡄࡆࡄࡘࡍࡑࡊ࡟ࡃࡗࡌࡐࡉࡥࡉࡅࠤ၂")),
            bstack111ll1l_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦ၃"): env.get(bstack111ll1l_opy_ (u"ࠨࡃࡐࡆࡈࡆ࡚ࡏࡌࡅࡡࡅ࡙ࡎࡒࡄࡠࡋࡇࠦ၄"))
        }
    if env.get(bstack111ll1l_opy_ (u"ࠢࡣࡣࡰࡦࡴࡵ࡟ࡣࡷ࡬ࡰࡩࡔࡵ࡮ࡤࡨࡶࠧ၅")):
        return {
            bstack111ll1l_opy_ (u"ࠣࡰࡤࡱࡪࠨ၆"): bstack111ll1l_opy_ (u"ࠤࡅࡥࡲࡨ࡯ࡰࠤ၇"),
            bstack111ll1l_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡸࡶࡱࠨ၈"): env.get(bstack111ll1l_opy_ (u"ࠦࡧࡧ࡭ࡣࡱࡲࡣࡧࡻࡩ࡭ࡦࡕࡩࡸࡻ࡬ࡵࡵࡘࡶࡱࠨ၉")),
            bstack111ll1l_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢ၊"): env.get(bstack111ll1l_opy_ (u"ࠨࡢࡢ࡯ࡥࡳࡴࡥࡳࡩࡱࡵࡸࡏࡵࡢࡏࡣࡰࡩࠧ။")),
            bstack111ll1l_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨ၌"): env.get(bstack111ll1l_opy_ (u"ࠣࡤࡤࡱࡧࡵ࡯ࡠࡤࡸ࡭ࡱࡪࡎࡶ࡯ࡥࡩࡷࠨ၍"))
        }
    if env.get(bstack111ll1l_opy_ (u"ࠤ࡚ࡉࡗࡉࡋࡆࡔࠥ၎")) or env.get(bstack111ll1l_opy_ (u"࡛ࠥࡊࡘࡃࡌࡇࡕࡣࡒࡇࡉࡏࡡࡓࡍࡕࡋࡌࡊࡐࡈࡣࡘ࡚ࡁࡓࡖࡈࡈࠧ၏")):
        return {
            bstack111ll1l_opy_ (u"ࠦࡳࡧ࡭ࡦࠤၐ"): bstack111ll1l_opy_ (u"ࠧ࡝ࡥࡳࡥ࡮ࡩࡷࠨၑ"),
            bstack111ll1l_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤၒ"): env.get(bstack111ll1l_opy_ (u"ࠢࡘࡇࡕࡇࡐࡋࡒࡠࡄࡘࡍࡑࡊ࡟ࡖࡔࡏࠦၓ")),
            bstack111ll1l_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧࠥၔ"): bstack111ll1l_opy_ (u"ࠤࡐࡥ࡮ࡴࠠࡑ࡫ࡳࡩࡱ࡯࡮ࡦࠤၕ") if env.get(bstack111ll1l_opy_ (u"࡛ࠥࡊࡘࡃࡌࡇࡕࡣࡒࡇࡉࡏࡡࡓࡍࡕࡋࡌࡊࡐࡈࡣࡘ࡚ࡁࡓࡖࡈࡈࠧၖ")) else None,
            bstack111ll1l_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴࠥၗ"): env.get(bstack111ll1l_opy_ (u"ࠧ࡝ࡅࡓࡅࡎࡉࡗࡥࡇࡊࡖࡢࡇࡔࡓࡍࡊࡖࠥၘ"))
        }
    if any([env.get(bstack111ll1l_opy_ (u"ࠨࡇࡄࡒࡢࡔࡗࡕࡊࡆࡅࡗࠦၙ")), env.get(bstack111ll1l_opy_ (u"ࠢࡈࡅࡏࡓ࡚ࡊ࡟ࡑࡔࡒࡎࡊࡉࡔࠣၚ")), env.get(bstack111ll1l_opy_ (u"ࠣࡉࡒࡓࡌࡒࡅࡠࡅࡏࡓ࡚ࡊ࡟ࡑࡔࡒࡎࡊࡉࡔࠣၛ"))]):
        return {
            bstack111ll1l_opy_ (u"ࠤࡱࡥࡲ࡫ࠢၜ"): bstack111ll1l_opy_ (u"ࠥࡋࡴࡵࡧ࡭ࡧࠣࡇࡱࡵࡵࡥࠤၝ"),
            bstack111ll1l_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲࠢၞ"): None,
            bstack111ll1l_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢၟ"): env.get(bstack111ll1l_opy_ (u"ࠨࡐࡓࡑࡍࡉࡈ࡚࡟ࡊࡆࠥၠ")),
            bstack111ll1l_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨၡ"): env.get(bstack111ll1l_opy_ (u"ࠣࡄࡘࡍࡑࡊ࡟ࡊࡆࠥၢ"))
        }
    if env.get(bstack111ll1l_opy_ (u"ࠤࡖࡌࡎࡖࡐࡂࡄࡏࡉࠧၣ")):
        return {
            bstack111ll1l_opy_ (u"ࠥࡲࡦࡳࡥࠣၤ"): bstack111ll1l_opy_ (u"ࠦࡘ࡮ࡩࡱࡲࡤࡦࡱ࡫ࠢၥ"),
            bstack111ll1l_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡺࡸ࡬ࠣၦ"): env.get(bstack111ll1l_opy_ (u"ࠨࡓࡉࡋࡓࡔࡆࡈࡌࡆࡡࡅ࡙ࡎࡒࡄࡠࡗࡕࡐࠧၧ")),
            bstack111ll1l_opy_ (u"ࠢ࡫ࡱࡥࡣࡳࡧ࡭ࡦࠤၨ"): bstack111ll1l_opy_ (u"ࠣࡌࡲࡦࠥࠩࡻࡾࠤၩ").format(env.get(bstack111ll1l_opy_ (u"ࠩࡖࡌࡎࡖࡐࡂࡄࡏࡉࡤࡐࡏࡃࡡࡌࡈࠬၪ"))) if env.get(bstack111ll1l_opy_ (u"ࠥࡗࡍࡏࡐࡑࡃࡅࡐࡊࡥࡊࡐࡄࡢࡍࡉࠨၫ")) else None,
            bstack111ll1l_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴࠥၬ"): env.get(bstack111ll1l_opy_ (u"࡙ࠧࡈࡊࡒࡓࡅࡇࡒࡅࡠࡄࡘࡍࡑࡊ࡟ࡏࡗࡐࡆࡊࡘࠢၭ"))
        }
    if bstack1l1l11ll11_opy_(env.get(bstack111ll1l_opy_ (u"ࠨࡎࡆࡖࡏࡍࡋ࡟ࠢၮ"))):
        return {
            bstack111ll1l_opy_ (u"ࠢ࡯ࡣࡰࡩࠧၯ"): bstack111ll1l_opy_ (u"ࠣࡐࡨࡸࡱ࡯ࡦࡺࠤၰ"),
            bstack111ll1l_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧၱ"): env.get(bstack111ll1l_opy_ (u"ࠥࡈࡊࡖࡌࡐ࡛ࡢ࡙ࡗࡒࠢၲ")),
            bstack111ll1l_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨၳ"): env.get(bstack111ll1l_opy_ (u"࡙ࠧࡉࡕࡇࡢࡒࡆࡓࡅࠣၴ")),
            bstack111ll1l_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶࠧၵ"): env.get(bstack111ll1l_opy_ (u"ࠢࡃࡗࡌࡐࡉࡥࡉࡅࠤၶ"))
        }
    if bstack1l1l11ll11_opy_(env.get(bstack111ll1l_opy_ (u"ࠣࡉࡌࡘࡍ࡛ࡂࡠࡃࡆࡘࡎࡕࡎࡔࠤၷ"))):
        return {
            bstack111ll1l_opy_ (u"ࠤࡱࡥࡲ࡫ࠢၸ"): bstack111ll1l_opy_ (u"ࠥࡋ࡮ࡺࡈࡶࡤࠣࡅࡨࡺࡩࡰࡰࡶࠦၹ"),
            bstack111ll1l_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲࠢၺ"): bstack111ll1l_opy_ (u"ࠧࢁࡽ࠰ࡽࢀ࠳ࡦࡩࡴࡪࡱࡱࡷ࠴ࡸࡵ࡯ࡵ࠲ࡿࢂࠨၻ").format(env.get(bstack111ll1l_opy_ (u"࠭ࡇࡊࡖࡋ࡙ࡇࡥࡓࡆࡔ࡙ࡉࡗࡥࡕࡓࡎࠪၼ")), env.get(bstack111ll1l_opy_ (u"ࠧࡈࡋࡗࡌ࡚ࡈ࡟ࡓࡇࡓࡓࡘࡏࡔࡐࡔ࡜ࠫၽ")), env.get(bstack111ll1l_opy_ (u"ࠨࡉࡌࡘࡍ࡛ࡂࡠࡔࡘࡒࡤࡏࡄࠨၾ"))),
            bstack111ll1l_opy_ (u"ࠤ࡭ࡳࡧࡥ࡮ࡢ࡯ࡨࠦၿ"): env.get(bstack111ll1l_opy_ (u"ࠥࡋࡎ࡚ࡈࡖࡄࡢ࡛ࡔࡘࡋࡇࡎࡒ࡛ࠧႀ")),
            bstack111ll1l_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴࠥႁ"): env.get(bstack111ll1l_opy_ (u"ࠧࡍࡉࡕࡊࡘࡆࡤࡘࡕࡏࡡࡌࡈࠧႂ"))
        }
    if env.get(bstack111ll1l_opy_ (u"ࠨࡃࡊࠤႃ")) == bstack111ll1l_opy_ (u"ࠢࡵࡴࡸࡩࠧႄ") and env.get(bstack111ll1l_opy_ (u"ࠣࡘࡈࡖࡈࡋࡌࠣႅ")) == bstack111ll1l_opy_ (u"ࠤ࠴ࠦႆ"):
        return {
            bstack111ll1l_opy_ (u"ࠥࡲࡦࡳࡥࠣႇ"): bstack111ll1l_opy_ (u"࡛ࠦ࡫ࡲࡤࡧ࡯ࠦႈ"),
            bstack111ll1l_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡺࡸ࡬ࠣႉ"): bstack111ll1l_opy_ (u"ࠨࡨࡵࡶࡳ࠾࠴࠵ࡻࡾࠤႊ").format(env.get(bstack111ll1l_opy_ (u"ࠧࡗࡇࡕࡇࡊࡒ࡟ࡖࡔࡏࠫႋ"))),
            bstack111ll1l_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧࠥႌ"): None,
            bstack111ll1l_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲႍࠣ"): None,
        }
    if env.get(bstack111ll1l_opy_ (u"ࠥࡘࡊࡇࡍࡄࡋࡗ࡝ࡤ࡜ࡅࡓࡕࡌࡓࡓࠨႎ")):
        return {
            bstack111ll1l_opy_ (u"ࠦࡳࡧ࡭ࡦࠤႏ"): bstack111ll1l_opy_ (u"࡚ࠧࡥࡢ࡯ࡦ࡭ࡹࡿࠢ႐"),
            bstack111ll1l_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤ႑"): None,
            bstack111ll1l_opy_ (u"ࠢ࡫ࡱࡥࡣࡳࡧ࡭ࡦࠤ႒"): env.get(bstack111ll1l_opy_ (u"ࠣࡖࡈࡅࡒࡉࡉࡕ࡛ࡢࡔࡗࡕࡊࡆࡅࡗࡣࡓࡇࡍࡆࠤ႓")),
            bstack111ll1l_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣ႔"): env.get(bstack111ll1l_opy_ (u"ࠥࡆ࡚ࡏࡌࡅࡡࡑ࡙ࡒࡈࡅࡓࠤ႕"))
        }
    if any([env.get(bstack111ll1l_opy_ (u"ࠦࡈࡕࡎࡄࡑࡘࡖࡘࡋࠢ႖")), env.get(bstack111ll1l_opy_ (u"ࠧࡉࡏࡏࡅࡒ࡙ࡗ࡙ࡅࡠࡗࡕࡐࠧ႗")), env.get(bstack111ll1l_opy_ (u"ࠨࡃࡐࡐࡆࡓ࡚ࡘࡓࡆࡡࡘࡗࡊࡘࡎࡂࡏࡈࠦ႘")), env.get(bstack111ll1l_opy_ (u"ࠢࡄࡑࡑࡇࡔ࡛ࡒࡔࡇࡢࡘࡊࡇࡍࠣ႙"))]):
        return {
            bstack111ll1l_opy_ (u"ࠣࡰࡤࡱࡪࠨႚ"): bstack111ll1l_opy_ (u"ࠤࡆࡳࡳࡩ࡯ࡶࡴࡶࡩࠧႛ"),
            bstack111ll1l_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡸࡶࡱࠨႜ"): None,
            bstack111ll1l_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨႝ"): env.get(bstack111ll1l_opy_ (u"ࠧࡈࡕࡊࡎࡇࡣࡏࡕࡂࡠࡐࡄࡑࡊࠨ႞")) or None,
            bstack111ll1l_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶࠧ႟"): env.get(bstack111ll1l_opy_ (u"ࠢࡃࡗࡌࡐࡉࡥࡉࡅࠤႠ"), 0)
        }
    if env.get(bstack111ll1l_opy_ (u"ࠣࡉࡒࡣࡏࡕࡂࡠࡐࡄࡑࡊࠨႡ")):
        return {
            bstack111ll1l_opy_ (u"ࠤࡱࡥࡲ࡫ࠢႢ"): bstack111ll1l_opy_ (u"ࠥࡋࡴࡉࡄࠣႣ"),
            bstack111ll1l_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲࠢႤ"): None,
            bstack111ll1l_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢႥ"): env.get(bstack111ll1l_opy_ (u"ࠨࡇࡐࡡࡍࡓࡇࡥࡎࡂࡏࡈࠦႦ")),
            bstack111ll1l_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨႧ"): env.get(bstack111ll1l_opy_ (u"ࠣࡉࡒࡣࡕࡏࡐࡆࡎࡌࡒࡊࡥࡃࡐࡗࡑࡘࡊࡘࠢႨ"))
        }
    if env.get(bstack111ll1l_opy_ (u"ࠤࡆࡊࡤࡈࡕࡊࡎࡇࡣࡎࡊࠢႩ")):
        return {
            bstack111ll1l_opy_ (u"ࠥࡲࡦࡳࡥࠣႪ"): bstack111ll1l_opy_ (u"ࠦࡈࡵࡤࡦࡈࡵࡩࡸ࡮ࠢႫ"),
            bstack111ll1l_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡺࡸ࡬ࠣႬ"): env.get(bstack111ll1l_opy_ (u"ࠨࡃࡇࡡࡅ࡙ࡎࡒࡄࡠࡗࡕࡐࠧႭ")),
            bstack111ll1l_opy_ (u"ࠢ࡫ࡱࡥࡣࡳࡧ࡭ࡦࠤႮ"): env.get(bstack111ll1l_opy_ (u"ࠣࡅࡉࡣࡕࡏࡐࡆࡎࡌࡒࡊࡥࡎࡂࡏࡈࠦႯ")),
            bstack111ll1l_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣႰ"): env.get(bstack111ll1l_opy_ (u"ࠥࡇࡋࡥࡂࡖࡋࡏࡈࡤࡏࡄࠣႱ"))
        }
    return {bstack111ll1l_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴࠥႲ"): None}
def get_host_info():
    return {
        bstack111ll1l_opy_ (u"ࠧ࡮࡯ࡴࡶࡱࡥࡲ࡫ࠢႳ"): platform.node(),
        bstack111ll1l_opy_ (u"ࠨࡰ࡭ࡣࡷࡪࡴࡸ࡭ࠣႴ"): platform.system(),
        bstack111ll1l_opy_ (u"ࠢࡵࡻࡳࡩࠧႵ"): platform.machine(),
        bstack111ll1l_opy_ (u"ࠣࡸࡨࡶࡸ࡯࡯࡯ࠤႶ"): platform.version(),
        bstack111ll1l_opy_ (u"ࠤࡤࡶࡨ࡮ࠢႷ"): platform.architecture()[0]
    }
def bstack1ll11l11l_opy_():
    try:
        import selenium
        return True
    except ImportError:
        return False
def bstack1l1l11l1l1_opy_():
    if bstack1ll1l1llll_opy_.get_property(bstack111ll1l_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡢࡷࡪࡹࡳࡪࡱࡱࠫႸ")):
        return bstack111ll1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠪႹ")
    return bstack111ll1l_opy_ (u"ࠬࡻ࡮࡬ࡰࡲࡻࡳࡥࡧࡳ࡫ࡧࠫႺ")
def bstack1l1l1l111l_opy_(driver):
    info = {
        bstack111ll1l_opy_ (u"࠭ࡣࡢࡲࡤࡦ࡮ࡲࡩࡵ࡫ࡨࡷࠬႻ"): driver.capabilities,
        bstack111ll1l_opy_ (u"ࠧࡴࡧࡶࡷ࡮ࡵ࡮ࡠ࡫ࡧࠫႼ"): driver.session_id,
        bstack111ll1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࠩႽ"): driver.capabilities.get(bstack111ll1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡑࡥࡲ࡫ࠧႾ"), None),
        bstack111ll1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬႿ"): driver.capabilities.get(bstack111ll1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠬჀ"), None),
        bstack111ll1l_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࠧჁ"): driver.capabilities.get(bstack111ll1l_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡏࡣࡰࡩࠬჂ"), None),
    }
    if bstack1l1l11l1l1_opy_() == bstack111ll1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠭Ⴣ"):
        info[bstack111ll1l_opy_ (u"ࠨࡲࡵࡳࡩࡻࡣࡵࠩჄ")] = bstack111ll1l_opy_ (u"ࠩࡤࡴࡵ࠳ࡡࡶࡶࡲࡱࡦࡺࡥࠨჅ") if bstack11l1ll111_opy_() else bstack111ll1l_opy_ (u"ࠪࡥࡺࡺ࡯࡮ࡣࡷࡩࠬ჆")
    return info
def bstack11l1ll111_opy_():
    if bstack1ll1l1llll_opy_.get_property(bstack111ll1l_opy_ (u"ࠫࡦࡶࡰࡠࡣࡸࡸࡴࡳࡡࡵࡧࠪჇ")):
        return True
    if bstack1l1l11ll11_opy_(os.environ.get(bstack111ll1l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡎ࡙࡟ࡂࡒࡓࡣࡆ࡛ࡔࡐࡏࡄࡘࡊ࠭჈"), None)):
        return True
    return False
def bstack11111l11l_opy_(bstack1l11ll11l1_opy_, url, data, config):
    headers = config.get(bstack111ll1l_opy_ (u"࠭ࡨࡦࡣࡧࡩࡷࡹࠧ჉"), None)
    proxies = bstack11ll1l1ll_opy_(config, url)
    auth = config.get(bstack111ll1l_opy_ (u"ࠧࡢࡷࡷ࡬ࠬ჊"), None)
    response = requests.request(
            bstack1l11ll11l1_opy_,
            url=url,
            headers=headers,
            auth=auth,
            json=data,
            proxies=proxies
        )
    return response
def bstack1llllll111_opy_(bstack1ll1l111l_opy_, size):
    bstack1ll1lll1ll_opy_ = []
    while len(bstack1ll1l111l_opy_) > size:
        bstack11lllll1_opy_ = bstack1ll1l111l_opy_[:size]
        bstack1ll1lll1ll_opy_.append(bstack11lllll1_opy_)
        bstack1ll1l111l_opy_ = bstack1ll1l111l_opy_[size:]
    bstack1ll1lll1ll_opy_.append(bstack1ll1l111l_opy_)
    return bstack1ll1lll1ll_opy_
def bstack1l1l111l1l_opy_(message, bstack1l1l1l1l1l_opy_=False):
    os.write(1, bytes(message, bstack111ll1l_opy_ (u"ࠨࡷࡷࡪ࠲࠾ࠧ჋")))
    os.write(1, bytes(bstack111ll1l_opy_ (u"ࠩ࡟ࡲࠬ჌"), bstack111ll1l_opy_ (u"ࠪࡹࡹ࡬࠭࠹ࠩჍ")))
    if bstack1l1l1l1l1l_opy_:
        with open(bstack111ll1l_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮࠱ࡴ࠷࠱ࡺ࠯ࠪ჎") + os.environ[bstack111ll1l_opy_ (u"ࠬࡈࡓࡠࡖࡈࡗ࡙ࡕࡐࡔࡡࡅ࡙ࡎࡒࡄࡠࡊࡄࡗࡍࡋࡄࡠࡋࡇࠫ჏")] + bstack111ll1l_opy_ (u"࠭࠮࡭ࡱࡪࠫა"), bstack111ll1l_opy_ (u"ࠧࡢࠩბ")) as f:
            f.write(message + bstack111ll1l_opy_ (u"ࠨ࡞ࡱࠫგ"))
def bstack1l1l1l11ll_opy_():
    return os.environ[bstack111ll1l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡃࡘࡘࡔࡓࡁࡕࡋࡒࡒࠬდ")].lower() == bstack111ll1l_opy_ (u"ࠪࡸࡷࡻࡥࠨე")
def bstack11llllll1_opy_(bstack1l11lllll1_opy_):
    return bstack111ll1l_opy_ (u"ࠫࢀࢃ࠯ࡼࡿࠪვ").format(bstack1l1l1llll1_opy_, bstack1l11lllll1_opy_)
def bstack1111ll111_opy_():
    return datetime.datetime.utcnow().isoformat() + bstack111ll1l_opy_ (u"ࠬࡠࠧზ")
def bstack1l11lll1l1_opy_(start, finish):
    return (datetime.datetime.fromisoformat(finish.rstrip(bstack111ll1l_opy_ (u"࡚࠭ࠨთ"))) - datetime.datetime.fromisoformat(start.rstrip(bstack111ll1l_opy_ (u"࡛ࠧࠩი")))).total_seconds() * 1000
def bstack1l11ll1lll_opy_(timestamp):
    return datetime.datetime.utcfromtimestamp(timestamp).isoformat() + bstack111ll1l_opy_ (u"ࠨ࡜ࠪკ")
def bstack1l1l111111_opy_(outcome):
    _, exception, _ = outcome.excinfo or (None, None, None)
    if exception:
        return bstack111ll1l_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩლ")
    else:
        return bstack111ll1l_opy_ (u"ࠪࡴࡦࡹࡳࡦࡦࠪმ")
def bstack1l1l11ll11_opy_(val):
    if val is None:
        return False
    return val.__str__().lower() == bstack111ll1l_opy_ (u"ࠫࡹࡸࡵࡦࠩნ")
def bstack1l11ll1111_opy_(val):
    return val.__str__().lower() == bstack111ll1l_opy_ (u"ࠬ࡬ࡡ࡭ࡵࡨࠫო")
def bstack1l1lll11l1_opy_(bstack1l1l11l111_opy_=Exception, class_method=False, default_value=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except bstack1l1l11l111_opy_ as e:
                print(bstack111ll1l_opy_ (u"ࠨࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥ࡬ࡵ࡯ࡥࡷ࡭ࡴࡴࠠࡼࡿࠣ࠱ࡃࠦࡻࡾ࠼ࠣࡿࢂࠨპ").format(func.__name__, bstack1l1l11l111_opy_.__name__, str(e)))
                return default_value
        return wrapper
    def bstack1l11llll1l_opy_(bstack1l1l111lll_opy_):
        def wrapped(cls, *args, **kwargs):
            try:
                return bstack1l1l111lll_opy_(cls, *args, **kwargs)
            except bstack1l1l11l111_opy_ as e:
                print(bstack111ll1l_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡦࡶࡰࡦࡸ࡮ࡵ࡮ࠡࡽࢀࠤ࠲ࡄࠠࡼࡿ࠽ࠤࢀࢃࠢჟ").format(bstack1l1l111lll_opy_.__name__, bstack1l1l11l111_opy_.__name__, str(e)))
                return default_value
        return wrapped
    if class_method:
        return bstack1l11llll1l_opy_
    else:
        return decorator
def bstack1ll1111ll_opy_(bstack1ll111l111_opy_):
    if bstack111ll1l_opy_ (u"ࠨࡣࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠬრ") in bstack1ll111l111_opy_ and bstack1l11ll1111_opy_(bstack1ll111l111_opy_[bstack111ll1l_opy_ (u"ࠩࡤࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳ࠭ს")]):
        return False
    if bstack111ll1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠬტ") in bstack1ll111l111_opy_ and bstack1l11ll1111_opy_(bstack1ll111l111_opy_[bstack111ll1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳ࠭უ")]):
        return False
    return True
def bstack1lllllllll_opy_():
    try:
        from pytest_bdd import reporting
        return True
    except Exception as e:
        return False
def bstack111111111_opy_(hub_url):
    if bstack1lllll1l1l_opy_() <= version.parse(bstack111ll1l_opy_ (u"ࠬ࠹࠮࠲࠵࠱࠴ࠬფ")):
        if hub_url != bstack111ll1l_opy_ (u"࠭ࠧქ"):
            return bstack111ll1l_opy_ (u"ࠢࡩࡶࡷࡴ࠿࠵࠯ࠣღ") + hub_url + bstack111ll1l_opy_ (u"ࠣ࠼࠻࠴࠴ࡽࡤ࠰ࡪࡸࡦࠧყ")
        return bstack11ll11l1l_opy_
    if hub_url != bstack111ll1l_opy_ (u"ࠩࠪშ"):
        return bstack111ll1l_opy_ (u"ࠥ࡬ࡹࡺࡰࡴ࠼࠲࠳ࠧჩ") + hub_url + bstack111ll1l_opy_ (u"ࠦ࠴ࡽࡤ࠰ࡪࡸࡦࠧც")
    return bstack1ll11l1ll_opy_
def bstack1l1l11ll1l_opy_():
    return isinstance(os.getenv(bstack111ll1l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡕ࡟ࡔࡆࡕࡗࡣࡕࡒࡕࡈࡋࡑࠫძ")), str)
def bstack11l1llll1_opy_(url):
    return urlparse(url).hostname
def bstack11l111lll_opy_(hostname):
    for bstack1111l1l11_opy_ in bstack1ll1l1l1l_opy_:
        regex = re.compile(bstack1111l1l11_opy_)
        if regex.match(hostname):
            return True
    return False
def bstack1l11l1llll_opy_(bstack1l1l1l1111_opy_, file_name, logger):
    bstack11111111_opy_ = os.path.join(os.path.expanduser(bstack111ll1l_opy_ (u"࠭ࡾࠨწ")), bstack1l1l1l1111_opy_)
    try:
        if not os.path.exists(bstack11111111_opy_):
            os.makedirs(bstack11111111_opy_)
        file_path = os.path.join(os.path.expanduser(bstack111ll1l_opy_ (u"ࠧࡿࠩჭ")), bstack1l1l1l1111_opy_, file_name)
        if not os.path.isfile(file_path):
            with open(file_path, bstack111ll1l_opy_ (u"ࠨࡹࠪხ")):
                pass
            with open(file_path, bstack111ll1l_opy_ (u"ࠤࡺ࠯ࠧჯ")) as outfile:
                json.dump({}, outfile)
        return file_path
    except Exception as e:
        logger.debug(bstack1ll11ll1l1_opy_.format(str(e)))
def bstack1l11lll11l_opy_(file_name, key, value, logger):
    file_path = bstack1l11l1llll_opy_(bstack111ll1l_opy_ (u"ࠪ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠪჰ"), file_name, logger)
    if file_path != None:
        if os.path.exists(file_path):
            bstack111l111l1_opy_ = json.load(open(file_path, bstack111ll1l_opy_ (u"ࠫࡷࡨࠧჱ")))
        else:
            bstack111l111l1_opy_ = {}
        bstack111l111l1_opy_[key] = value
        with open(file_path, bstack111ll1l_opy_ (u"ࠧࡽࠫࠣჲ")) as outfile:
            json.dump(bstack111l111l1_opy_, outfile)
def bstack1lll11l11_opy_(file_name, logger):
    file_path = bstack1l11l1llll_opy_(bstack111ll1l_opy_ (u"࠭࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠭ჳ"), file_name, logger)
    bstack111l111l1_opy_ = {}
    if file_path != None and os.path.exists(file_path):
        with open(file_path, bstack111ll1l_opy_ (u"ࠧࡳࠩჴ")) as bstack1l11lllll_opy_:
            bstack111l111l1_opy_ = json.load(bstack1l11lllll_opy_)
    return bstack111l111l1_opy_
def bstack1lllll11l_opy_(file_path, logger):
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
    except Exception as e:
        logger.debug(bstack111ll1l_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡪࡰࠣࡨࡪࡲࡥࡵ࡫ࡱ࡫ࠥ࡬ࡩ࡭ࡧ࠽ࠤࠬჵ") + file_path + bstack111ll1l_opy_ (u"ࠩࠣࠫჶ") + str(e))
def bstack1lllll1l1l_opy_():
    from selenium import webdriver
    return version.parse(webdriver.__version__)
class Notset:
    def __repr__(self):
        return bstack111ll1l_opy_ (u"ࠥࡀࡓࡕࡔࡔࡇࡗࡂࠧჷ")
def bstack1111lll1_opy_(config):
    if bstack111ll1l_opy_ (u"ࠫ࡮ࡹࡐ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࠪჸ") in config:
        del (config[bstack111ll1l_opy_ (u"ࠬ࡯ࡳࡑ࡮ࡤࡽࡼࡸࡩࡨࡪࡷࠫჹ")])
        return False
    if bstack1lllll1l1l_opy_() < version.parse(bstack111ll1l_opy_ (u"࠭࠳࠯࠶࠱࠴ࠬჺ")):
        return False
    if bstack1lllll1l1l_opy_() >= version.parse(bstack111ll1l_opy_ (u"ࠧ࠵࠰࠴࠲࠺࠭჻")):
        return True
    if bstack111ll1l_opy_ (u"ࠨࡷࡶࡩ࡜࠹ࡃࠨჼ") in config and config[bstack111ll1l_opy_ (u"ࠩࡸࡷࡪ࡝࠳ࡄࠩჽ")] is False:
        return False
    else:
        return True
def bstack11l111l1l_opy_(args_list, bstack1l11ll11ll_opy_):
    index = -1
    for value in bstack1l11ll11ll_opy_:
        try:
            index = args_list.index(value)
            return index
        except Exception as e:
            return index
    return index
class Result:
    def __init__(self, result=None, duration=None, exception=None, bstack1l1l111l11_opy_=None):
        self.result = result
        self.duration = duration
        self.exception = exception
        self.exception_type = type(self.exception).__name__ if exception else None
        self.bstack1l1l111l11_opy_ = bstack1l1l111l11_opy_
    @classmethod
    def passed(cls):
        return Result(result=bstack111ll1l_opy_ (u"ࠪࡴࡦࡹࡳࡦࡦࠪჾ"))
    @classmethod
    def failed(cls, exception=None):
        return Result(result=bstack111ll1l_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫჿ"), exception=exception)
    def bstack1l11ll1l1l_opy_(self):
        if self.result != bstack111ll1l_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬᄀ"):
            return None
        if bstack111ll1l_opy_ (u"ࠨࡁࡴࡵࡨࡶࡹ࡯࡯࡯ࠤᄁ") in self.exception_type:
            return bstack111ll1l_opy_ (u"ࠢࡂࡵࡶࡩࡷࡺࡩࡰࡰࡈࡶࡷࡵࡲࠣᄂ")
        return bstack111ll1l_opy_ (u"ࠣࡗࡱ࡬ࡦࡴࡤ࡭ࡧࡧࡉࡷࡸ࡯ࡳࠤᄃ")
    def bstack1l11ll111l_opy_(self):
        if self.result != bstack111ll1l_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩᄄ"):
            return None
        if self.bstack1l1l111l11_opy_:
            return self.bstack1l1l111l11_opy_
        return bstack1l11ll1l11_opy_(self.exception)
def bstack1l11ll1l11_opy_(exc):
    return traceback.format_exception(exc)
def bstack1l1l1l11l1_opy_(message):
    if isinstance(message, str):
        return not bool(message and message.strip())
    return True
def bstack11l11l11_opy_(object, key, default_value):
    if key in object.__dict__.keys():
        return object.__dict__.get(key)
    return default_value
def bstack1l111lll1_opy_(config, logger):
    try:
        import playwright
        bstack1l11ll1ll1_opy_ = playwright.__file__
        bstack1l1l1ll111_opy_ = os.path.split(bstack1l11ll1ll1_opy_)
        bstack1l11llll11_opy_ = bstack1l1l1ll111_opy_[0] + bstack111ll1l_opy_ (u"ࠪ࠳ࡩࡸࡩࡷࡧࡵ࠳ࡵࡧࡣ࡬ࡣࡪࡩ࠴ࡲࡩࡣ࠱ࡦࡰ࡮࠵ࡣ࡭࡫࠱࡮ࡸ࠭ᄅ")
        os.environ[bstack111ll1l_opy_ (u"ࠫࡌࡒࡏࡃࡃࡏࡣࡆࡍࡅࡏࡖࡢࡌ࡙࡚ࡐࡠࡒࡕࡓ࡝࡟ࠧᄆ")] = bstack1l1ll11ll_opy_(config)
        with open(bstack1l11llll11_opy_, bstack111ll1l_opy_ (u"ࠬࡸࠧᄇ")) as f:
            bstack11llll1l_opy_ = f.read()
            bstack1l1l11l11l_opy_ = bstack111ll1l_opy_ (u"࠭ࡧ࡭ࡱࡥࡥࡱ࠳ࡡࡨࡧࡱࡸࠬᄈ")
            bstack1l11llllll_opy_ = bstack11llll1l_opy_.find(bstack1l1l11l11l_opy_)
            if bstack1l11llllll_opy_ is -1:
              process = subprocess.Popen(bstack111ll1l_opy_ (u"ࠢ࡯ࡲࡰࠤ࡮ࡴࡳࡵࡣ࡯ࡰࠥ࡭࡬ࡰࡤࡤࡰ࠲ࡧࡧࡦࡰࡷࠦᄉ"), shell=True, cwd=bstack1l1l1ll111_opy_[0])
              process.wait()
              bstack1l1l1l1ll1_opy_ = bstack111ll1l_opy_ (u"ࠨࠤࡸࡷࡪࠦࡳࡵࡴ࡬ࡧࡹࠨ࠻ࠨᄊ")
              bstack1l1l1l1l11_opy_ = bstack111ll1l_opy_ (u"ࠤࠥࠦࠥࡢࠢࡶࡵࡨࠤࡸࡺࡲࡪࡥࡷࡠࠧࡁࠠࡤࡱࡱࡷࡹࠦࡻࠡࡤࡲࡳࡹࡹࡴࡳࡣࡳࠤࢂࠦ࠽ࠡࡴࡨࡵࡺ࡯ࡲࡦࠪࠪ࡫ࡱࡵࡢࡢ࡮࠰ࡥ࡬࡫࡮ࡵࠩࠬ࠿ࠥ࡯ࡦࠡࠪࡳࡶࡴࡩࡥࡴࡵ࠱ࡩࡳࡼ࠮ࡈࡎࡒࡆࡆࡒ࡟ࡂࡉࡈࡒ࡙ࡥࡈࡕࡖࡓࡣࡕࡘࡏ࡙࡛ࠬࠤࡧࡵ࡯ࡵࡵࡷࡶࡦࡶࠨࠪ࠽ࠣࠦࠧࠨᄋ")
              bstack1l1l1111ll_opy_ = bstack11llll1l_opy_.replace(bstack1l1l1l1ll1_opy_, bstack1l1l1l1l11_opy_)
              with open(bstack1l11llll11_opy_, bstack111ll1l_opy_ (u"ࠪࡻࠬᄌ")) as f:
                f.write(bstack1l1l1111ll_opy_)
    except Exception as e:
        logger.error(bstack1ll1l1ll1_opy_.format(str(e)))