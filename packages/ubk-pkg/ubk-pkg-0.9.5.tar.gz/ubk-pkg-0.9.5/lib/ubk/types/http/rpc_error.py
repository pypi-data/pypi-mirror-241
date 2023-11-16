"""
jsonrpc error response
"""
from typing import Union
from pydantic import BaseModel


class ErrorMessage(BaseModel):
    """
    the error messages
    """
    uz: str = None
    ru: str = None
    en: str = None


class Error(BaseModel):
    """
    the error base response.
    """
    code: int = None
    message: Union[str, ErrorMessage] = None


class Host(BaseModel):
    """
    the host.
    """
    host: str
    timestamp: str


class JsonRPCError(BaseModel):
    """
    the json rpc error response.
    """
    jsonrpc: str = None
    id: str = None
    status: bool = None
    origin: str = None
    host: Host = None
    error: Error = None
