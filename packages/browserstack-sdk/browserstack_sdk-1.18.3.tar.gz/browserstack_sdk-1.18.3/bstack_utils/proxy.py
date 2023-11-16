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
from urllib.parse import urlparse
from bstack_utils.messages import bstack1l111ll1l1_opy_
def bstack11lll1111l_opy_(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except:
        return False
def bstack11lll11l1l_opy_(bstack11lll11l11_opy_, bstack11lll111l1_opy_):
    from pypac import get_pac
    from pypac import PACSession
    from pypac.parser import PACFile
    import socket
    if os.path.isfile(bstack11lll11l11_opy_):
        with open(bstack11lll11l11_opy_) as f:
            pac = PACFile(f.read())
    elif bstack11lll1111l_opy_(bstack11lll11l11_opy_):
        pac = get_pac(url=bstack11lll11l11_opy_)
    else:
        raise Exception(bstack111ll1l_opy_ (u"࠭ࡐࡢࡥࠣࡪ࡮ࡲࡥࠡࡦࡲࡩࡸࠦ࡮ࡰࡶࠣࡩࡽ࡯ࡳࡵ࠼ࠣࡿࢂ࠭ᇓ").format(bstack11lll11l11_opy_))
    session = PACSession(pac)
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect((bstack111ll1l_opy_ (u"ࠢ࠹࠰࠻࠲࠽࠴࠸ࠣᇔ"), 80))
        bstack11lll11111_opy_ = s.getsockname()[0]
        s.close()
    except:
        bstack11lll11111_opy_ = bstack111ll1l_opy_ (u"ࠨ࠲࠱࠴࠳࠶࠮࠱ࠩᇕ")
    proxy_url = session.get_pac().find_proxy_for_url(bstack11lll111l1_opy_, bstack11lll11111_opy_)
    return proxy_url
def bstack1l1l1ll11_opy_(config):
    return bstack111ll1l_opy_ (u"ࠩ࡫ࡸࡹࡶࡐࡳࡱࡻࡽࠬᇖ") in config or bstack111ll1l_opy_ (u"ࠪ࡬ࡹࡺࡰࡴࡒࡵࡳࡽࡿࠧᇗ") in config
def bstack1l1ll11ll_opy_(config):
    if not bstack1l1l1ll11_opy_(config):
        return
    if config.get(bstack111ll1l_opy_ (u"ࠫ࡭ࡺࡴࡱࡒࡵࡳࡽࡿࠧᇘ")):
        return config.get(bstack111ll1l_opy_ (u"ࠬ࡮ࡴࡵࡲࡓࡶࡴࡾࡹࠨᇙ"))
    if config.get(bstack111ll1l_opy_ (u"࠭ࡨࡵࡶࡳࡷࡕࡸ࡯ࡹࡻࠪᇚ")):
        return config.get(bstack111ll1l_opy_ (u"ࠧࡩࡶࡷࡴࡸࡖࡲࡰࡺࡼࠫᇛ"))
def bstack11ll1l1ll_opy_(config, bstack11lll111l1_opy_):
    proxy = bstack1l1ll11ll_opy_(config)
    proxies = {}
    if config.get(bstack111ll1l_opy_ (u"ࠨࡪࡷࡸࡵࡖࡲࡰࡺࡼࠫᇜ")) or config.get(bstack111ll1l_opy_ (u"ࠩ࡫ࡸࡹࡶࡳࡑࡴࡲࡼࡾ࠭ᇝ")):
        if proxy.endswith(bstack111ll1l_opy_ (u"ࠪ࠲ࡵࡧࡣࠨᇞ")):
            proxies = bstack1l1l1l111_opy_(proxy, bstack11lll111l1_opy_)
        else:
            proxies = {
                bstack111ll1l_opy_ (u"ࠫ࡭ࡺࡴࡱࡵࠪᇟ"): proxy
            }
    return proxies
def bstack1l1l1l111_opy_(bstack11lll11l11_opy_, bstack11lll111l1_opy_):
    proxies = {}
    global bstack11lll111ll_opy_
    if bstack111ll1l_opy_ (u"ࠬࡖࡁࡄࡡࡓࡖࡔ࡞࡙ࠨᇠ") in globals():
        return bstack11lll111ll_opy_
    try:
        proxy = bstack11lll11l1l_opy_(bstack11lll11l11_opy_, bstack11lll111l1_opy_)
        if bstack111ll1l_opy_ (u"ࠨࡄࡊࡔࡈࡇ࡙ࠨᇡ") in proxy:
            proxies = {}
        elif bstack111ll1l_opy_ (u"ࠢࡉࡖࡗࡔࠧᇢ") in proxy or bstack111ll1l_opy_ (u"ࠣࡊࡗࡘࡕ࡙ࠢᇣ") in proxy or bstack111ll1l_opy_ (u"ࠤࡖࡓࡈࡑࡓࠣᇤ") in proxy:
            bstack11ll1lllll_opy_ = proxy.split(bstack111ll1l_opy_ (u"ࠥࠤࠧᇥ"))
            if bstack111ll1l_opy_ (u"ࠦ࠿࠵࠯ࠣᇦ") in bstack111ll1l_opy_ (u"ࠧࠨᇧ").join(bstack11ll1lllll_opy_[1:]):
                proxies = {
                    bstack111ll1l_opy_ (u"࠭ࡨࡵࡶࡳࡷࠬᇨ"): bstack111ll1l_opy_ (u"ࠢࠣᇩ").join(bstack11ll1lllll_opy_[1:])
                }
            else:
                proxies = {
                    bstack111ll1l_opy_ (u"ࠨࡪࡷࡸࡵࡹࠧᇪ"): str(bstack11ll1lllll_opy_[0]).lower() + bstack111ll1l_opy_ (u"ࠤ࠽࠳࠴ࠨᇫ") + bstack111ll1l_opy_ (u"ࠥࠦᇬ").join(bstack11ll1lllll_opy_[1:])
                }
        elif bstack111ll1l_opy_ (u"ࠦࡕࡘࡏ࡙࡛ࠥᇭ") in proxy:
            bstack11ll1lllll_opy_ = proxy.split(bstack111ll1l_opy_ (u"ࠧࠦࠢᇮ"))
            if bstack111ll1l_opy_ (u"ࠨ࠺࠰࠱ࠥᇯ") in bstack111ll1l_opy_ (u"ࠢࠣᇰ").join(bstack11ll1lllll_opy_[1:]):
                proxies = {
                    bstack111ll1l_opy_ (u"ࠨࡪࡷࡸࡵࡹࠧᇱ"): bstack111ll1l_opy_ (u"ࠤࠥᇲ").join(bstack11ll1lllll_opy_[1:])
                }
            else:
                proxies = {
                    bstack111ll1l_opy_ (u"ࠪ࡬ࡹࡺࡰࡴࠩᇳ"): bstack111ll1l_opy_ (u"ࠦ࡭ࡺࡴࡱ࠼࠲࠳ࠧᇴ") + bstack111ll1l_opy_ (u"ࠧࠨᇵ").join(bstack11ll1lllll_opy_[1:])
                }
        else:
            proxies = {
                bstack111ll1l_opy_ (u"࠭ࡨࡵࡶࡳࡷࠬᇶ"): proxy
            }
    except Exception as e:
        print(bstack111ll1l_opy_ (u"ࠢࡴࡱࡰࡩࠥ࡫ࡲࡳࡱࡵࠦᇷ"), bstack1l111ll1l1_opy_.format(bstack11lll11l11_opy_, str(e)))
    bstack11lll111ll_opy_ = proxies
    return proxies