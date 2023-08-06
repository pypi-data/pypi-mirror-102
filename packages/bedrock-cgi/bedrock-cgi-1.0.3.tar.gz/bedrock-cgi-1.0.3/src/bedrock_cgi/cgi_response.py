import sys
from .constant import MIME_TYPE_JSON, CHARSET, CHARSET_UTF8

# cgi response headers
HEADER_STATUS = "STATUS"
HEADER_CONTENT_TYPE = "CONTENT-TYPE"

# cgi response header values
STATUS_OK = "200 OK"
STATUS_BAD_REQUEST = "400 Bad Request"
STATUS_INTERNAL_SERVER_ERROR = "500 Internal Server Error"
STATUS_UNSUPPORTED_REQUEST_METHOD = "501 Unsupported Request"

def __writeEncoded (string, encoding):
    sys.stdout.buffer.write (string.encode (encoding))

def respond (headerStatus, response, encoding = CHARSET_UTF8):
    # print the headers...
    __writeEncoded ("{}: {}\n".format (HEADER_STATUS, headerStatus), encoding)
    __writeEncoded ("{}: {}; {}={}\n".format (HEADER_CONTENT_TYPE, MIME_TYPE_JSON, CHARSET, CHARSET_UTF8), encoding)
    __writeEncoded ("X-Content-Type-Options: nosniff\n", encoding)
    __writeEncoded ("Access-Control-Allow-Origin: *\n", encoding)
    __writeEncoded ("Access-Control-Allow-Headers: *\n", encoding)
    __writeEncoded ("Access-Control-Allow-Methods: POST,OPTIONS\n", encoding)
    __writeEncoded ("\n", encoding)

    # print the response, note that it is already encoded, so from here needs to be treated as raw bytes
    __writeEncoded(response, encoding)

    # NOTE, no further responses should be issued after this
