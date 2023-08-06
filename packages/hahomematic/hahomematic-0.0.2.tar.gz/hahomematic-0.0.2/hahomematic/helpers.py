# pylint: disable=line-too-long
"""
Helper functions used within hahomematic
"""

import logging
import json
import ssl
import urllib
import urllib.request

from hahomematic.const import (
    ATTR_NAME,
    ATTR_TYPE,
    ATTR_VALUE,
    ATTR_HM_LIST,
    ATTR_HM_LOGIC,
    ATTR_HM_NUMBER,
    DEFAULT_TLS,
    DEFAULT_VERIFY_TLS,
    PATH_JSON_RPC,
)
from hahomematic import config

LOG = logging.getLogger(__name__)

VERIFIED_CTX = ssl.create_default_context()
UNVERIFIED_CTX = ssl.create_default_context()
UNVERIFIED_CTX.check_hostname = False
UNVERIFIED_CTX.verify_mode = ssl.CERT_NONE

def generate_unique_id(address, parameter=None):
    """
    Build unique id from address and parameter.
    """
    if parameter is None:
        return f"{address.replace(':', '_').replace('-', '_')}".lower()
    return f"{address.replace(':', '_').replace('-', '_')}_{parameter}".lower()

def make_http_credentials(username=None, password=None):
    """Build auth part for api_url."""
    credentials = ''
    if username is None:
        return credentials
    if username is not None:
        if ':' in username:
            return credentials
        credentials += username
    if credentials and password is not None:
        credentials += ":%s" % password
    return "%s@" % credentials

# pylint: disable=too-many-arguments
def build_api_url(host, port, path, username=None, password=None, tls=False):
    """Build XML-RPC API URL from components."""
    credentials = make_http_credentials(username, password)
    scheme = 'http'
    if not path:
        path = ''
    if path and not path.startswith('/'):
        path = "/{}".format(path)
    if tls:
        scheme += 's'
    return "{}://{}{}:{}{}".format(scheme, credentials, host, port, path)

# pylint: disable=dangerous-default-value
def json_rpc_post(host, jsonport, method, params={}, tls=DEFAULT_TLS, verify_tls=DEFAULT_VERIFY_TLS):
    """Reusable JSON-RPC POST function."""
    LOG.debug("helpers.json_rpc_post: Method: %s", method)
    try:
        payload = json.dumps(
            {"method": method, "params": params, "jsonrpc": "1.1", "id": 0}).encode('utf-8')

        headers = {"Content-Type": 'application/json',
                   "Content-Length": len(payload)}
        if tls:
            apiendpoint = "https://%s:%s%s" % (host, jsonport, PATH_JSON_RPC)
        else:
            apiendpoint = "http://%s:%s%s" % (host, jsonport, PATH_JSON_RPC)
        LOG.debug("helpers.json_rpc_post: API-Endpoint: %s", apiendpoint)
        req = urllib.request.Request(apiendpoint, payload, headers)
        if tls:
            if verify_tls:
                resp = urllib.request.urlopen(req, timeout=config.TIMEOUT, context=VERIFIED_CTX)
            else:
                resp = urllib.request.urlopen(req, timeout=config.TIMEOUT, context=UNVERIFIED_CTX)
        else:
            resp = urllib.request.urlopen(req, timeout=config.TIMEOUT)
        if resp.status == 200:
            try:
                return json.loads(resp.read().decode('utf-8'))
            except ValueError:
                LOG.exception("helpers.json_rpc_post: Failed to parse JSON. Trying workaround.")
                # Workaround for bug in CCU
                return json.loads(resp.read().decode('utf-8').replace("\\", ""))
        else:
            LOG.error("helpers.json_rpc_post: Status: %i", resp.status)
            return {'error': resp.status, 'result': {}}
    # pylint: disable=broad-except
    except Exception as err:
        LOG.exception("helpers.json_rpc_post: Exception")
        return {'error': str(err), 'result': {}}

def parse_ccu_sys_var(data):
    """Helper to parse type of system variables of CCU."""
    # pylint: disable=no-else-return
    if data[ATTR_TYPE] == ATTR_HM_LOGIC:
        return data[ATTR_NAME], data[ATTR_VALUE] == 'true'
    elif data[ATTR_TYPE] == ATTR_HM_NUMBER:
        return data[ATTR_NAME], float(data[ATTR_VALUE])
    elif data[ATTR_TYPE] == ATTR_HM_LIST:
        return data[ATTR_NAME], int(data[ATTR_VALUE])
    return data[ATTR_NAME], data[ATTR_VALUE]
