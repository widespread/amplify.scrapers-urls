from .helper import *
from utils.helpers.index import request_with_retry, get_proxies, download_gz_file, error_slack_message
from services.slack.slack_message import send_slack_message


COMPETITOR = 'alliedelec'
URL = 'https://us.rs-online.com/sitemap.xml'


def get_and_store_alliedelec_urls():
    try:
        proxies, headers = get_proxies()
        page = request_with_retry(
            "get", URL, COMPETITOR, proxies=proxies, headers=headers)
        if page.status_code != 200:
            message = f"Error: {COMPETITOR}{page.text}"
            send_slack_message(message)
        sitemap_index = BeautifulSoup(page.content, 'html.parser')
        sitemap_url = [
            element.text for element in sitemap_index.findAll('loc')]
        for count, data in enumerate(sitemap_url, start=1):
            path = download_gz_file(COMPETITOR, data, count)
            store_data(path)
    except Exception as e:
        error_slack_message(e)

