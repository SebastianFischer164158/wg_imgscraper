import os
import re
import requests
from constants import *
from tqdm import tqdm


def imgscraper(thread_id: str) -> int:
    request = requests.get(main_url + thread_id)
    if request.status_code == 200:

        html_response = request.text
        regex_pics = r'<a href="//i\.4cdn\.org/wg/(\d{13}\.[a-zA-Z]*)'
        matches = re.findall(regex_pics, html_response)

        for pic_id in tqdm(matches, ascii=True, desc='Downloaded'):  # pic_id example -> 1606735091906.jpg
            full_pic_url = fr'{https}{base}{pic_id}'
            try:
                pic_req = requests.get(full_pic_url)
                if pic_req.status_code == 200:
                    complete_saving_path = os.path.join(saving_path, pic_id)
                    with open(f"{complete_saving_path}", 'wb') as picfile:
                        picfile.write(pic_req.content)
            except:
                print(f"Could not download {full_pic_url}")
                continue
    else:
        raise Exception(f"200 was not returned -> error {request.status_code}")

    return 0
