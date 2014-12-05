import logging

from ckan_api_client.high_level import CkanHighlevelClient
from jobcontrol.globals import current_app


def download_and_print_ckan_datasets(ckan_url):
    """
    Download and print datasets from ckan
    """

    client = CkanHighlevelClient(ckan_url)

    logger = logging.getLogger('ckan_crawl_demo')
    logger.info('Starting function')

    total = len(client.list_datasets())
    current_app.report_progress(None, 0, total)

    for cnt, dataset in enumerate(client.iter_datasets()):
        logger.debug(repr(dataset))
        current_app.report_progress(None, cnt + 1, total)

    return total
