""" A client library for accessing Kraken's REST API and Websockets API."""
from .http import HTTPAuthenticatedClient, HTTPClient

__all__ = (
    "HTTPAuthenticatedClient",
    "HTTPClient",
)
