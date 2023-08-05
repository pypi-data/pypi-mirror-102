# -*- coding: utf-8 -*-

"""
    signing

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

from signing.api_helper import APIHelper


class Configuration(object):

    """A class used for configuring the SDK by a user.

    This class need not be instantiated and all properties and methods
    are accessible without instance creation.

    """

    # Set the array parameter serialization method
    # (allowed: indexed, unindexed, plain, csv, tsv, psv)
    array_serialization = "indexed"

    # An enum for SDK environments
    class Environment(object):
        PRODUCTION = 0

    # An enum for API servers
    class Server(object):
        SERVER_1 = 0

    # The environment in which the SDK is running
    environment = Environment.PRODUCTION


    # All the environments the SDK can run in
    environments = {
        Environment.PRODUCTION: {
            Server.SERVER_1: 'http://127.0.0.1:8000',
        },
    }

    @classmethod
    def get_base_uri(cls, server=Server.SERVER_1):
        """Generates the appropriate base URI for the environment and the server.

        Args:
            server (Configuration.Server): The server enum for which the base URI is required.

        Returns:
            String: The base URI.

        """
        return cls.environments[cls.environment][server]
