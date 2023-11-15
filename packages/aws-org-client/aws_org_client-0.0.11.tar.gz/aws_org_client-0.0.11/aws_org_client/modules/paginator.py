import boto3
import inspect
from aws_org_client.modules.logger import Logger


logger = Logger(__name__)


class Paginator:
    def __init__(self, client):
        """Initialise client for identity store.

        Args:
            identity_store_id (string): The globally unique identifier for the identity store.
        """
        logger.info("Init paginator...")
        self.client = client

    def paginate(self, **kwargs):
        """
        Generic paginator function.

        Args:
            kwargs:
        """
        paginator_name = inspect.stack()[1][3]
        if "PaginatorName" in kwargs:
            paginator_name = kwargs["PaginatorName"]

        result_key = kwargs["ResultKey"]
        operation_parameters = kwargs["OperationalParameters"]

        paginator = self.client.get_paginator(paginator_name)

        page_iterator = paginator.paginate(**operation_parameters)

        elements = [element for page in page_iterator for element in page[result_key]]

        return elements
