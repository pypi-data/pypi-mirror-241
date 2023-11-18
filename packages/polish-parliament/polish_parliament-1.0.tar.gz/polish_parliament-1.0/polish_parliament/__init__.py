""" A client library for accessing API for Polish parliament (Sejm) """
from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
