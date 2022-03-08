#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import socket
import os

from ..util_core.v2ray import restart, V2ray
from ..util_core.writer import GroupWriter
from ..util_core.group import Mtproto, SS
from ..util_core.selector import GroupSelector
from ..util_core.utils import get_ip, gen_cert, readchar, is_ipv4, is_email

class TLSModifier:
    def __init__(self, group_tag, group_index, domain='', alpn=None, xtls=False):
        self.domain = domain
        self.alpn = alpn
        self.xtls = xtls
        self.writer = GroupWriter(group_tag, group_index)
    
    @restart(True)
        sudo lsof -t -i tcp:80 -s tcp:listen | sudo xargs kill
cd /root/
wget https://raw.githubusercontent.com/acmesh-official/acme.sh/master/acme.sh
bash acme.sh --install
rm acme.sh
cd .acme.sh
bash acme.sh --register-account -m djarumpentol01@gmail.com
bash acme.sh --issue --standalone -d $domain --force
bash acme.sh --installcert -d $domain --fullchainpath /etc/xray/xray.crt --keypath /etc/xray/xray.key
