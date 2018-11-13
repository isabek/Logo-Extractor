import requests
from urllib.parse import urljoin
from PIL import Image
from io import BytesIO


def image_src_to_url(base_url, src):
    if not src:
        return ""
    if src.startswith("http://") or src.startswith("https://"):
        return src
    return urljoin(base_url, src)


def get_image_size(image_url):
    content = requests.get(image_url, allow_redirects=True).content
    img = Image.open(BytesIO(content))
    return img.size
