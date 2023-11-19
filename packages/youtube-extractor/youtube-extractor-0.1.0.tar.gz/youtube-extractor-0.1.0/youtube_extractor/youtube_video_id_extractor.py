
import re

def extract_video_id_from_url(url):
    regex_full_url = r'[?&]v=([^&#]*)'
    regex_short_url = r'youtu.be/([^/?&]*)'
    regex_shorts_url = r'shorts/([a-zA-Z0-9_-]+)\?'

    match_full_url = re.search(regex_full_url, url)
    match_short_url = re.search(regex_short_url, url)
    match_shorts_url = re.search(regex_shorts_url, url)

    if match_full_url and match_full_url.group(1):
        return match_full_url.group(1)
    elif match_short_url and match_short_url.group(1):
        return match_short_url.group(1)
    elif match_shorts_url and match_shorts_url.group(1):
        return match_shorts_url.group(1)

    return None
