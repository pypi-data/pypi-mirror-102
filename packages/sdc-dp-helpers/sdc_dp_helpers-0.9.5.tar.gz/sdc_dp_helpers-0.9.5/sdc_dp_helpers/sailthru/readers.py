"""
    CUSTOM READERS CLASSES
        - Class which manages reader tasks like auth, requests, pagination
"""
import os

import yaml
from sailthru import SailthruClient

from sdc_dp_helpers.api_utilities.retry_managers import request_handler
from sdc_dp_helpers.sailthru.config_magagers import ConfigManager, get_queries
from sdc_dp_helpers.api_utilities.date_managers import date_handler


class CustomSailThruReader:
    """
        Custom SailThru Reader
    """

    def __init__(self, api_key_path):
        self.api_key_path = api_key_path
        self.sailthru_client = SailthruClient(
            api_key=self.get_api_key()[0],
            secret=self.get_api_key()[1]
        )

    def get_api_key(self) -> list:
        """
            Gathers key and value pairs of key and their secret.
        """
        with open(self.api_key_path, 'r') as file:
            data = yaml.safe_load(file)
            return [data.get('api_key'), data.get('api_secret')]

    def get_all_templates(self, filter_by='name') -> list:
        """
            Templates are dynamic for the SailThru stats endpoint.
            Therefore we can gather all templates for each api request and return
            a list of relevant information for the reader.
            :filter_by: str. The key value that we can return, such as name or id.
            :return: list. A list of relevant template values.
        """
        response = self.sailthru_client.get_templates()
        data = response.get_body()
        print(f'Template Response:{data}')

        items = []
        for item in data['templates']:
            items.append(item.get(filter_by, None))

        return items

    @request_handler(
        wait=int(os.environ.get('REQUEST_WAIT_TIME', 0)),
        backoff_factor=float(os.environ.get('REQUEST_BACKOFF_FACTOR', 0.01)),
        backoff_method=os.environ.get('REQUEST_BACKOFF_METHOD', 0.01)
    )
    def get_all_stats(self, configs):
        """
        Stats returned are based on the cred provided &
        Additional parameters are dependent on the stat value:
            - list - information about your subscriber counts on
              all lists or a particular list
            - blast - information about a particular campaign
            - send - information about a particular triggered message

        :configs: str. Path to the list of configs to iterate over.
        :returns: dict. Response of the particular query.
        """

        query_config = get_queries(configs)
        print('Query config:{}'.format(query_config))

        data_set = []
        for query in query_config:
            # handle date ranges

            query['start_date'] = date_handler(query['start_date'])
            query['end_date'] = date_handler(query['end_date'])
            print(f'Query: {query}')

            # send queries require templates, here we use dynamic templates
            api_get = ConfigManager(sailthru_client=self.sailthru_client, query=query)

            if query.get('stat') == 'send':
                templates = self.get_all_templates()

                for template in templates:
                    query.update({'template': template})
                    data = api_get.get_stat_api()

                    if data is not None:
                        data_set.append(data)

            else:
                data = api_get.get_stat_api()
                if data is not None:
                    data_set.append(data)

        return data_set
