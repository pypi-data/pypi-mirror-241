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
from urllib.parse import urlparse
from bstack_utils.messages import bstack1l11111l11_opy_
def bstack11ll11l111_opy_(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except:
        return False
def bstack11ll111lll_opy_(bstack11ll11ll11_opy_, bstack11ll11l1l1_opy_):
    from pypac import get_pac
    from pypac import PACSession
    from pypac.parser import PACFile
    import socket
    if os.path.isfile(bstack11ll11ll11_opy_):
        with open(bstack11ll11ll11_opy_) as f:
            pac = PACFile(f.read())
    elif bstack11ll11l111_opy_(bstack11ll11ll11_opy_):
        pac = get_pac(url=bstack11ll11ll11_opy_)
    else:
        raise Exception(bstack1ll_opy_ (u"ࠬࡖࡡࡤࠢࡩ࡭ࡱ࡫ࠠࡥࡱࡨࡷࠥࡴ࡯ࡵࠢࡨࡼ࡮ࡹࡴ࠻ࠢࡾࢁࠬሃ").format(bstack11ll11ll11_opy_))
    session = PACSession(pac)
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect((bstack1ll_opy_ (u"ࠨ࠸࠯࠺࠱࠼࠳࠾ࠢሄ"), 80))
        bstack11ll111ll1_opy_ = s.getsockname()[0]
        s.close()
    except:
        bstack11ll111ll1_opy_ = bstack1ll_opy_ (u"ࠧ࠱࠰࠳࠲࠵࠴࠰ࠨህ")
    proxy_url = session.get_pac().find_proxy_for_url(bstack11ll11l1l1_opy_, bstack11ll111ll1_opy_)
    return proxy_url
def bstack1lll11lll_opy_(config):
    return bstack1ll_opy_ (u"ࠨࡪࡷࡸࡵࡖࡲࡰࡺࡼࠫሆ") in config or bstack1ll_opy_ (u"ࠩ࡫ࡸࡹࡶࡳࡑࡴࡲࡼࡾ࠭ሇ") in config
def bstack1l111ll11_opy_(config):
    if not bstack1lll11lll_opy_(config):
        return
    if config.get(bstack1ll_opy_ (u"ࠪ࡬ࡹࡺࡰࡑࡴࡲࡼࡾ࠭ለ")):
        return config.get(bstack1ll_opy_ (u"ࠫ࡭ࡺࡴࡱࡒࡵࡳࡽࡿࠧሉ"))
    if config.get(bstack1ll_opy_ (u"ࠬ࡮ࡴࡵࡲࡶࡔࡷࡵࡸࡺࠩሊ")):
        return config.get(bstack1ll_opy_ (u"࠭ࡨࡵࡶࡳࡷࡕࡸ࡯ࡹࡻࠪላ"))
def bstack1llll1111_opy_(config, bstack11ll11l1l1_opy_):
    proxy = bstack1l111ll11_opy_(config)
    proxies = {}
    if config.get(bstack1ll_opy_ (u"ࠧࡩࡶࡷࡴࡕࡸ࡯ࡹࡻࠪሌ")) or config.get(bstack1ll_opy_ (u"ࠨࡪࡷࡸࡵࡹࡐࡳࡱࡻࡽࠬል")):
        if proxy.endswith(bstack1ll_opy_ (u"ࠩ࠱ࡴࡦࡩࠧሎ")):
            proxies = bstack11llllll_opy_(proxy, bstack11ll11l1l1_opy_)
        else:
            proxies = {
                bstack1ll_opy_ (u"ࠪ࡬ࡹࡺࡰࡴࠩሏ"): proxy
            }
    return proxies
def bstack11llllll_opy_(bstack11ll11ll11_opy_, bstack11ll11l1l1_opy_):
    proxies = {}
    global bstack11ll11l1ll_opy_
    if bstack1ll_opy_ (u"ࠫࡕࡇࡃࡠࡒࡕࡓ࡝࡟ࠧሐ") in globals():
        return bstack11ll11l1ll_opy_
    try:
        proxy = bstack11ll111lll_opy_(bstack11ll11ll11_opy_, bstack11ll11l1l1_opy_)
        if bstack1ll_opy_ (u"ࠧࡊࡉࡓࡇࡆࡘࠧሑ") in proxy:
            proxies = {}
        elif bstack1ll_opy_ (u"ࠨࡈࡕࡖࡓࠦሒ") in proxy or bstack1ll_opy_ (u"ࠢࡉࡖࡗࡔࡘࠨሓ") in proxy or bstack1ll_opy_ (u"ࠣࡕࡒࡇࡐ࡙ࠢሔ") in proxy:
            bstack11ll11l11l_opy_ = proxy.split(bstack1ll_opy_ (u"ࠤࠣࠦሕ"))
            if bstack1ll_opy_ (u"ࠥ࠾࠴࠵ࠢሖ") in bstack1ll_opy_ (u"ࠦࠧሗ").join(bstack11ll11l11l_opy_[1:]):
                proxies = {
                    bstack1ll_opy_ (u"ࠬ࡮ࡴࡵࡲࡶࠫመ"): bstack1ll_opy_ (u"ࠨࠢሙ").join(bstack11ll11l11l_opy_[1:])
                }
            else:
                proxies = {
                    bstack1ll_opy_ (u"ࠧࡩࡶࡷࡴࡸ࠭ሚ"): str(bstack11ll11l11l_opy_[0]).lower() + bstack1ll_opy_ (u"ࠣ࠼࠲࠳ࠧማ") + bstack1ll_opy_ (u"ࠤࠥሜ").join(bstack11ll11l11l_opy_[1:])
                }
        elif bstack1ll_opy_ (u"ࠥࡔࡗࡕࡘ࡚ࠤም") in proxy:
            bstack11ll11l11l_opy_ = proxy.split(bstack1ll_opy_ (u"ࠦࠥࠨሞ"))
            if bstack1ll_opy_ (u"ࠧࡀ࠯࠰ࠤሟ") in bstack1ll_opy_ (u"ࠨࠢሠ").join(bstack11ll11l11l_opy_[1:]):
                proxies = {
                    bstack1ll_opy_ (u"ࠧࡩࡶࡷࡴࡸ࠭ሡ"): bstack1ll_opy_ (u"ࠣࠤሢ").join(bstack11ll11l11l_opy_[1:])
                }
            else:
                proxies = {
                    bstack1ll_opy_ (u"ࠩ࡫ࡸࡹࡶࡳࠨሣ"): bstack1ll_opy_ (u"ࠥ࡬ࡹࡺࡰ࠻࠱࠲ࠦሤ") + bstack1ll_opy_ (u"ࠦࠧሥ").join(bstack11ll11l11l_opy_[1:])
                }
        else:
            proxies = {
                bstack1ll_opy_ (u"ࠬ࡮ࡴࡵࡲࡶࠫሦ"): proxy
            }
    except Exception as e:
        print(bstack1ll_opy_ (u"ࠨࡳࡰ࡯ࡨࠤࡪࡸࡲࡰࡴࠥሧ"), bstack1l11111l11_opy_.format(bstack11ll11ll11_opy_, str(e)))
    bstack11ll11l1ll_opy_ = proxies
    return proxies