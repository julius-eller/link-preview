import requests
from bs4 import BeautifulSoup
from fallback import get_title, get_description, get_image, get_site_name


def get_meta(links, headers):
    """Generate preview obj per link."""
    previews = []
    exception_domains = ['Youtube', 'Medium' 'Github']
    for link in links:
        url = link.get('href')
        r = requests.get(url, headers=headers)
        embedded_link = BeautifulSoup(r.content, 'html.parser')
        domain = get_site_name(embedded_link, url)
        if domain in exception_domains:
            print('WARNING:', domain)
        preview_dict = {
            'title': get_title(embedded_link),
            'description': get_description(embedded_link),
            'image': get_image(embedded_link),
            'sitename': get_site_name(embedded_link, url),
            'url': url
            }
        previews.append(preview_dict)
    return previews