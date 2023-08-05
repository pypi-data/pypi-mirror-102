# -*- coding: utf-8 -*-

"""
    signing

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

from signing.api_helper import APIHelper
from signing.configuration import Configuration
from signing.controllers.base_controller import BaseController

class MiscController(BaseController):

    """A Controller to access Endpoints in the signing API."""


    def sign(self,
                x_api_key,
                x_api_client,
                content_type,
                body):
        """Does a POST request to /sign.

        TODO: type endpoint description here.

        Args:
            x_api_key (string): TODO: type description here. Example: 
            x_api_client (string): TODO: type description here. Example: 
            content_type (string): TODO: type description here. Example: 
            body (object): TODO: type description here. Example: 

        Returns:
            void: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/sign'
        _query_builder = Configuration.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'X-API-Key': x_api_key,
            'X-API-Client': x_api_client,
            'Content-Type': content_type
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
        _context = self.execute_request(_request)
        self.validate_response(_context)
