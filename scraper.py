import re
import requests
from constants import *
from tqdm import tqdm


def imgscraper(thread_id: str) -> str:
    request = requests.get(main_url+thread_id)
    if request.status_code == 200:
        html_response = request.text
        regex_pics = r'<a href="//i\.4cdn\.org/wg/(\d{13}\.[a-zA-Z]*)'
        matches = re.findall(regex_pics, html_response)
        # print(matches)
        for pic_id in matches:
            full_pic_url = fr'{https}{base}{pic_id}'
            # print(full_pic_url)
            pic_req = requests.get(full_pic_url)

            # test case right now, only downloads the first image
            # remove the break and correct new image name for every time
            # just use the pic id tbh.

            if pic_req.status_code == 200:
                with open("testpic.jpg",'wb') as picfile:
                    picfile.write(pic_req.content)
            break
    else:
        raise Exception(f"200 was not returned -> error {request.status_code}")

# <a\s+(?:[^>]*?\s+)?href=(["'])(.*?)\1

# this one works:
# <a href="\/\/i\.4cdn\.org\/wg\/\d{13}\.[a-zA-Z]*