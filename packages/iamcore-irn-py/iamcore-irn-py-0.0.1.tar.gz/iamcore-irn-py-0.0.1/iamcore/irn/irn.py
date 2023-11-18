from base64 import b64encode, b64decode
from typing import List

from .const import (
    WILDCARD, PREFIX_TOKEN, TOKEN_SEPARATOR,
    SUB_TOKEN_SEPARATOR,
    IRN_TOKEN_INDEX_PREFIX,
    IRN_TOKEN_INDEX_ACCOUNT_ID,
    IRN_TOKEN_INDEX_APPLICATION,
    IRN_TOKEN_INDEX_TENANT_ID,
    IRN_TOKEN_INDEX_POOL,
    IRN_TOKEN_INDEX_RESOURCE,
    IRN_TOKEN_INDEX_RESOURCE_TYPE,
    IRN_TOKEN_INDEX_RESOURCE_PATH,
    IRN_TOKEN_INDEX_RESOURCE_ID
)
from .exceptions import IRNException
from .utils import nvl, validate_irn_tokens


class IRN(object):
    """
    IRN is the Iamcore Resource Name: a regular or a wildcard one.

    <p>The standard string IRN representation is:
    irn:<account ID>:<application>:[<tenant ID>]:[<pool>]:<resource type>[/<resource path>]/<resource ID>

    <p>IRN (sub-)tokens consist of latin letters (`a-zA-Z`), digits (`0-9`), dashes (`-`),
    underscores (`_`), at signs (`@`), and dots (`.`).

    <p>Semicolon (`:`) and slash (`/`) are reserved separators for IRN tokens and sub-tokens, respectively.

    <p>Asterisk (`*`) is reserved for IRN wildcards. There might only be one trailing asterisk in an IRN.
    """

    __account_id: str
    __application: str
    __tenant_id: str
    __pool: List[str]
    __resource_type: str
    __resource_path: List[str]
    __resource_id: str

    @property
    def account_id(self):
        return nvl(self.__account_id)

    @property
    def application(self):
        return nvl(self.__application)

    @property
    def tenant_id(self) -> str:
        return nvl(self.__tenant_id)

    @property
    def pool(self) -> str:
        if self.__pool:
            return SUB_TOKEN_SEPARATOR.join(self.__pool)
        return ""

    @property
    def resource_type(self) -> str:
        return nvl(self.__resource_type)

    @property
    def resource_path(self) -> str:
        if self.__resource_path:
            return SUB_TOKEN_SEPARATOR.join(self.__resource_path)
        return ""

    @property
    def resource_id(self) -> str:
        return nvl(self.__resource_id)

    def __irn(self) -> str:
        if WILDCARD == self.account_id:
            return WILDCARD

        application = self.application
        irn = TOKEN_SEPARATOR.join((
            PREFIX_TOKEN, self.account_id, application
        ))
        if WILDCARD == application:
            return irn

        irn += TOKEN_SEPARATOR
        tenant_id = self.tenant_id
        if tenant_id:
            irn += tenant_id
            if WILDCARD == tenant_id:
                return irn

        pool = self.pool
        irn += TOKEN_SEPARATOR + pool
        if WILDCARD in pool:
            return irn

        resource_type = self.resource_type
        irn += TOKEN_SEPARATOR + resource_type
        if WILDCARD == resource_type:
            return irn

        resource_path = self.resource_path
        if resource_path:
            irn += SUB_TOKEN_SEPARATOR + self.resource_path
        irn += SUB_TOKEN_SEPARATOR + self.resource_id
        return irn

    def __repr__(self):
        return self.__irn()

    def __str__(self):
        return self.__irn()

    def to_base64(self) -> str:
        return b64encode(self.__irn().encode()).decode()

    def __init__(self, account_id: str = None, application: str = None, tenant_id: str = None, pool: str = None,
                 resource_type: str = None, resource_path: str = None, resource_id: str = None):
        if pool and len(pool) > 0:
            self.__pool = pool.split(SUB_TOKEN_SEPARATOR)
        else:
            self.__pool = []
        if resource_path:
            self.__resource_path = [
                subToken
                for subToken in resource_path.split(SUB_TOKEN_SEPARATOR)
                if subToken
            ]
        else:
            self.__resource_path = []
        self.__account_id = account_id
        self.__application = application
        self.__tenant_id = tenant_id
        self.__resource_type = resource_type
        self.__resource_id = resource_id

    @classmethod
    def create(cls, account_id: str = "", application: str = "", tenant_id: str = "", pool: str = "",
               resource_type: str = "", resource_path: str = "", resource_id: str = ""):
        validate_irn_tokens(account_id, application, tenant_id, pool, resource_type, resource_path, resource_id)
        return cls(account_id, application, tenant_id, pool, resource_type, resource_path, resource_id)

    @classmethod
    def of(cls, value: object):
        if isinstance(value, IRN):
            return value
        if isinstance(value, str):
            if value.startswith(PREFIX_TOKEN + TOKEN_SEPARATOR) or value == WILDCARD:
                return cls.from_irn_str(value)
            else:
                return cls.from_base64(value)
        raise IRNException("Unexpected irn type")

    @classmethod
    def from_base64(cls, b64: str):
        irn = b64decode(b64.encode()).decode()
        return cls.from_irn_str(irn)

    @classmethod
    def from_irn_str(cls, irn: str):
        if WILDCARD == irn:
            # Special case for blanket wildcard IRNs ("*"), no extra parsing and validation required
            return IRN(account_id=irn)

        input_tokens = irn.split(TOKEN_SEPARATOR)

        if PREFIX_TOKEN != input_tokens[IRN_TOKEN_INDEX_PREFIX]:
            raise IRNException("Unexpected prefix token")

        if not input_tokens[-1]:
            raise IRNException("Last token is empty")

        irn_tokens = [
            input_tokens[i] if len(input_tokens) > i else None
            for i in range(8)
        ]
        if irn_tokens[IRN_TOKEN_INDEX_RESOURCE]:
            resource_sub_tokens = irn_tokens[IRN_TOKEN_INDEX_RESOURCE].split(SUB_TOKEN_SEPARATOR)
            irn_tokens[IRN_TOKEN_INDEX_RESOURCE_PATH] = SUB_TOKEN_SEPARATOR.join(resource_sub_tokens[1:-1])
            if len(resource_sub_tokens) >= 1:
                irn_tokens[IRN_TOKEN_INDEX_RESOURCE_TYPE] = resource_sub_tokens[0]
            if len(resource_sub_tokens) >= 2:
                irn_tokens[IRN_TOKEN_INDEX_RESOURCE_ID] = resource_sub_tokens[-1]

        return IRN.create(
            irn_tokens[IRN_TOKEN_INDEX_ACCOUNT_ID],
            irn_tokens[IRN_TOKEN_INDEX_APPLICATION],
            irn_tokens[IRN_TOKEN_INDEX_TENANT_ID],
            irn_tokens[IRN_TOKEN_INDEX_POOL],
            irn_tokens[IRN_TOKEN_INDEX_RESOURCE_TYPE],
            irn_tokens[IRN_TOKEN_INDEX_RESOURCE_PATH],
            irn_tokens[IRN_TOKEN_INDEX_RESOURCE_ID]
        )
