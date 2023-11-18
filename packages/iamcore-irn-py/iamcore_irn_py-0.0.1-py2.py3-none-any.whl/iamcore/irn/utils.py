from .const import *
from .exceptions import IRNException


def is_invalid_token(token: str) -> bool:
    if not token:
        return True
    return len(IRN_TOKEN_RE.findall(token)) == 0


def validate_empty_tokens(application: str = None, tenant_id: str = None, pool: str = None, resource_type: str = None,
                          resource_path: str = None, resource_id: str = None) -> None:
    if application:
        raise IRNException("Application name is not empty")
    if tenant_id:
        raise IRNException("Tenant ID is not empty")
    if pool:
        raise IRNException("Pool is not empty")
    if resource_type:
        raise IRNException("Resource type is not empty")
    if resource_path:
        raise IRNException("Resource path is not empty")
    if resource_id:
        raise IRNException("Resource ID is not empty")


def validate_irn_tokens(account_id: str = "", application: str = "", tenant_id: str = "", pool: str = "",
                        resource_type: str = "", resource_path: str = "", resource_id: str = ""):
    concatenated_tokens = "".join((
        nvl(account_id),
        nvl(application),
        nvl(tenant_id),
        nvl(pool),
        nvl(resource_type),
        nvl(resource_path),
        nvl(resource_id)
    ))

    if WILDCARD in concatenated_tokens:
        if concatenated_tokens.count(WILDCARD) > 1:
            raise IRNException("Only one asterisk allowed")
        if resource_path is not None and WILDCARD in resource_path:
            raise IRNException("Wildcards not permitted in the resource path")
        if pool and WILDCARD in pool and not pool.endswith(WILDCARD):
            raise IRNException("Misplaced asterisk in pool: can be only last sub-token")
        if not concatenated_tokens.endswith(WILDCARD):
            raise IRNException("Misplaced asterisk: can be only last token")
    # Account token validation
    if WILDCARD == account_id:
        return validate_empty_tokens(application, tenant_id, pool, resource_type, resource_path, resource_id)
    elif is_invalid_token(account_id):
        raise IRNException("Invalid account ID token")

    # Application token validation
    if WILDCARD == application:
        return validate_empty_tokens(tenant_id=tenant_id, pool=pool, resource_type=resource_type,
                                     resource_path=resource_path, resource_id=resource_id)
    elif is_invalid_token(application):
        raise IRNException("Invalid application token")

    # Tenant Id token validation
    if tenant_id is not None and len(tenant_id) > 0:
        if WILDCARD == tenant_id:
            return validate_empty_tokens(pool=pool, resource_type=resource_type, resource_path=resource_path,
                                         resource_id=resource_id)
        elif is_invalid_token(tenant_id):
            raise IRNException("Invalid tenantID token")
    # Pool token validation
    if pool is not None and len(pool) > 0:
        if WILDCARD in pool:
            return validate_empty_tokens(resource_type=resource_type, resource_path=resource_path,
                                         resource_id=resource_id)
        elif not pool.startswith(SUB_TOKEN_SEPARATOR):
            raise IRNException("Pool does not start with '/'")
        elif is_invalid_token(pool.replace(SUB_TOKEN_SEPARATOR, "")):
            raise IRNException("Invalid pool token")

    # Resource type token validation
    if WILDCARD == resource_type:
        return validate_empty_tokens(resource_path=resource_path, resource_id=resource_id)
    elif is_invalid_token(resource_type):
        raise IRNException("Invalid resource type token")
    # Resource path token validation
    if resource_path is not None and len(resource_path) > 0:
        if is_invalid_token(resource_path.replace(SUB_TOKEN_SEPARATOR, "")):
            raise IRNException("Invalid resource path token")
    # Resource Id token validation
    if WILDCARD != resource_id and is_invalid_token(resource_id):
        raise IRNException("Invalid resource ID token")


def nvl(value, default=""):
    if value is None:
        return default
    return value
