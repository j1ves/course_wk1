#!/usr/bin/env python

from ciscoconfparse import CiscoConfParse

cisco_cfg = CiscoConfParse("cisco_config_file.txt")

crypto_maps = cisco_cfg.find_objects(r"^crypto map")
tranform_set = cisco_cfg.find_objects(r"^crypto ipsec transform-set")

def find_pfs_2(crypto_maps):
    for cm in crypto_maps:
        for i in cm.children:
            if "set pfs group2" in i.text:
                print cm.text + "is using pfs G2"

def find_non_aes_crypto(tranform_set,crypto_maps):
    non_aes_list = []
    for ts in tranform_set:
        if "-aes" not in ts.text:
            non_aes_list.append(ts.text.split()[3])
    for cm in crypto_maps:
        for i in cm.children:
            if "set transform-set" in i.text:
                print i.text.split()[2]
                if i.text.split()[2] in non_aes_list:
                    print cm.text + "is using TS " + i.text.split()[2] + " which isn't using AES"

find_pfs_2(crypto_maps)
find_non_aes_crypto(tranform_set,crypto_maps)


