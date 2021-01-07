import os
import re
import requests
from constants import *
from tqdm import tqdm


# TODO: fix regex to include umlaut matches; currently unable to find e.g. é û
# https://regex101.com/r/Rnfqr7/1
# https://regex101.com/r/Rnfqr7/2
#  also optimize regex so that it operates as a singular one

def imgscraper(thread_id: str, dir_to_store: str) -> int:
    request = requests.get(main_url + thread_id)
    if request.status_code == 200:

        html_response = request.text
        # regex_pics = r'<a href="//i\.4cdn\.org/wg/(\d{13}\.[a-zA-Z]*)'
        # href="\/\/is2\.4chan\.org\/wg\/(\d{13}\.[a-zA-Z]*)
        # do not break regexes as they will fail if indented/newlined/etc.
        regex_pics_4chan = r'href="\/\/i\.4cdn\.org\/wg\/(\d{13}\.[a-zA-Z]*)'
        regex_pics_is24chan = r'href="\/\/is2\.4chan\.org\/wg\/(\d{13}\.[a-zA-Z]*)'
        matches1 = re.findall(regex_pics_4chan, html_response)
        matches2 = re.findall(regex_pics_is24chan, html_response)
        matches = matches1 + matches2

        for pic_id in tqdm(matches, ascii=True, desc='Downloaded'):
            # pic_id example -> 1606735091906.jpg
            full_pic_url = fr'{https}{base}{pic_id}'
            try:
                pic_req = requests.get(full_pic_url)

                if pic_req.status_code == 200:
                    complete_saving_path = os.path.join(dir_to_store, pic_id)
                    with open(f"{complete_saving_path}", 'wb') as picfile:
                        picfile.write(pic_req.content)
                else:
                    print("IA M HERE")
            except:
                print(f"Could not download {full_pic_url}")
                continue
    else:
        raise Exception(f"200 was not returned -> error {request.status_code}")

    return 0

#
# if __name__ == '__main__':
#     imgscraper("7704276", 'D:\\Downloads\\WallPapers4chanwg')
