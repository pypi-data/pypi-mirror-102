import sys
from .constant import MIME_TYPE_JSON, CHARSET, CHARSET_UTF8, HEADER_STATUS, HEADER_CONTENT_TYPE, REQUEST_METHOD_POST, REQUEST_METHOD_OPTIONS

def respond (headerStatus, response, encoding = CHARSET_UTF8):
    def __writeEncoded (string = ""):
        sys.stdout.buffer.write ("{}\n".format (string).encode (encoding))

        # print the headers...
    __writeEncoded ("{}: {}".format (HEADER_STATUS, headerStatus))
    __writeEncoded ("{}: {}; {}={}".format (HEADER_CONTENT_TYPE, MIME_TYPE_JSON, CHARSET, CHARSET_UTF8))
    __writeEncoded ("X-Content-Type-Options: nosniff")
    __writeEncoded ("Access-Control-Allow-Origin: *")
    __writeEncoded ("Access-Control-Allow-Headers: *")
    __writeEncoded ("Access-Control-Allow-Methods: {},{}".format (REQUEST_METHOD_POST, REQUEST_METHOD_OPTIONS))
    __writeEncoded ()

    # print the response, note that it is already encoded, so from here needs to be treated as raw bytes
    __writeEncoded(response)

    # NOTE, no further responses should be issued after this
