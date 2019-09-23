# !/usr/bin/env python
# coding=utf-8
import requests
import time
import json
import sys
from note163 import *
from wps import *

# 解决https访问警告
# from requests.packages.urllib3.exceptions import InsecureRequestWarning,InsecurePlatformWarning
# requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
# requests.packages.urllib3.disable_warnings(InsecurePlatformWarning)


if __name__ == '__main__':
    now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))

    print("--------------------------"+now+"----------------------------")
    # print("\n            ===模拟wps小程序签到===")

    f = open(sys.path[0]+'/data.json', 'r', encoding="utf8")
    data = json.load(f)
    f.close()

    sid = data['wps_checkin']

    for item in sid:
        print("\n    为{}签到---↓".format(item['name']))
        wps_clockin(item['sid'])

    # sys.exit()
    wps_inv = data['wps_invite']
    # 这13个账号被邀请
    invite_sid = [
                "V02StVuaNcoKrZ3BuvJQ1FcFS_xnG2k00af250d4002664c02f",
                "V02SWIvKWYijG6Rggo4m0xvDKj1m7ew00a8e26d3002508b828",
                "V02Sr3nJ9IicoHWfeyQLiXgvrRpje6E00a240b890023270f97",
                "V02SBsNOf4sJZNFo4jOHdgHg7-2Tn1s00a338776000b669579",
                "V02ScVbtm2pQD49ArcgGLv360iqQFLs014c8062e000b6c37b6",
                "V02S2oI49T-Jp0_zJKZ5U38dIUSIl8Q00aa679530026780e96",
                "V02ShotJqqiWyubCX0VWTlcbgcHqtSQ00a45564e002678124c",
                "V02SFiqdXRGnH5oAV2FmDDulZyGDL3M00a61660c0026781be1",
                "V02S7tldy5ltYcikCzJ8PJQDSy_ElEs00a327c3c0026782526",
                "V02SPoOluAnWda0dTBYTXpdetS97tyI00a16135e002684bb5c",
                "V02Sb8gxW2inr6IDYrdHK_ywJnayd6s00ab7472b0026849b17",
                "V02SwV15KQ_8n6brU98_2kLnnFUDUOw00adf3fda0026934a7f",
                "V02SC1mOHS0RiUBxeoA8NTliH2h2NGc00a803c35002693584d"
            ]
    print("\n\n            ===wps邀请=== ")
    for item in wps_inv:
        print("    为{}邀请---↓".format(item['name']))
        wps_invite(invite_sid, item['invite_userid'])

    print("\n\n          ===有道云笔记签到===")
    note = data['noteyoudao']
    for index,item in enumerate(note):
        YNOTE_SESS = noteyoudao(item['YNOTE_SESS'], item['user'], item['passwd'])
        if YNOTE_SESS is not None:
            # cookie失效，更新
            data['noteyoudao'][index]['YNOTE_SESS'] = YNOTE_SESS
            f = open(sys.path[0]+'/data.json', 'w', encoding="utf8",)
            json.dump(data, f, ensure_ascii=False)

            

    # noteyoudao()
