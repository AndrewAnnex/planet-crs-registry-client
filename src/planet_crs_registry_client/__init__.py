"""A client library for accessing planet_crs_registry"""

__version__ = '0.1.0'

__all__ = (
    "AuthenticatedClient",
    "Client",
)

from .client import AuthenticatedClient, Client
