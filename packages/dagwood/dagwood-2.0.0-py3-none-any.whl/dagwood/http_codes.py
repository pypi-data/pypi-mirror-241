class HttpResponse:
    """
    Class for storing HTTP response information.
    """

    def __init__(self, code, message, explanation, response_type):
        self.code = code
        self.message = message
        self.explanation = explanation
        self.type = response_type


class ResponseTypes:
    """
    Enum for the different types of HTTP responses.
    """

    INFO = "Informational"
    SUCCESS = "Success"
    REDIRECT = "Redirection"
    CLIENT_ERROR = "Client Error"
    SERVER_ERROR = "Server Error"


def interpret(code: int) -> HttpResponse:
    """
    Find the HTTP response information for the given code.

    Parameters
    ----------
    code : int
        The HTTP response code.

    Returns
    -------
    HttpResponse
        The HttpResponse object with the given code.
    """
    responses = get_codes()
    message, explanation, response_type = responses.get(
        code, ("Unknown", "No description available.", "Unknown")
    )
    return HttpResponse(code, message, explanation, response_type)


def get_enums():
    return [
        ResponseTypes.INFO,
        ResponseTypes.SUCCESS,
        ResponseTypes.REDIRECT,
        ResponseTypes.CLIENT_ERROR,
        ResponseTypes.SERVER_ERROR,
    ]


def get_codes() -> dict:
    """
    Get a dictionary of HTTP response codes and their information.

    Returns
    -------
    dict
        A dictionary of HTTP response codes and their information.
    """
    return {
        # Informational Responses
        100: (
            "Continue",
            "The server has received the request headers, and the client should proceed to send the request body.",
            ResponseTypes.INFO,
        ),
        101: (
            "Switching Protocols",
            "The requester has asked the server to switch protocols.",
            ResponseTypes.INFO,
        ),
        102: (
            "Processing",
            "The server has received and is processing the request, but no response is available yet.",
            ResponseTypes.INFO,
        ),
        103: (
            "Early Hints",
            "Used to return some response headers before final HTTP message.",
            ResponseTypes.INFO,
        ),
        # Success Responses
        200: ("OK", "The request has succeeded.", ResponseTypes.SUCCESS),
        201: (
            "Created",
            "The request has been fulfilled and has resulted in one or more new resources being created.",
            ResponseTypes.SUCCESS,
        ),
        202: (
            "Accepted",
            "The request has been accepted for processing, but the processing has not been completed.",
            ResponseTypes.SUCCESS,
        ),
        203: (
            "Non-Authoritative Information",
            "The server is a transforming proxy that received a 200 OK from its origin, but is returning a modified version of the origin's response.",
            ResponseTypes.SUCCESS,
        ),
        204: (
            "No Content",
            "The server successfully processed the request and is not returning any content.",
            ResponseTypes.SUCCESS,
        ),
        205: (
            "Reset Content",
            "The server successfully processed the request, but is not returning any content. Unlike a 204 response, this response requires that the requester reset the document view.",
            ResponseTypes.SUCCESS,
        ),
        206: (
            "Partial Content",
            "The server is delivering only part of the resource due to a range header sent by the client.",
            ResponseTypes.SUCCESS,
        ),
        207: (
            "Multi-Status",
            "The message body that follows is by default an XML message and can contain a number of separate response codes, depending on how many sub-requests were made.",
            ResponseTypes.SUCCESS,
        ),
        208: (
            "Already Reported",
            "The members of a DAV binding have already been enumerated in a preceding part of the (multistatus) response, and are not being included again.",
            ResponseTypes.SUCCESS,
        ),
        226: (
            "IM Used",
            "The server has fulfilled a request for the resource, and the response is a representation of the result of one or more instance-manipulations applied to the current instance.",
            ResponseTypes.SUCCESS,
        ),
        # Redirection Messages
        300: (
            "Multiple Choices",
            "A link list. The user can select a link and go to that location. Maximum five addresses.",
            ResponseTypes.REDIRECT,
        ),
        301: (
            "Moved Permanently",
            "The URL of the requested resource has been changed permanently. The new URL is given in the response.",
            ResponseTypes.REDIRECT,
        ),
        302: (
            "Found",
            "The server sent this response to direct the client to get the requested resource at another URI with a GET request.",
            ResponseTypes.REDIRECT,
        ),
        303: (
            "See Other",
            "The server sent this response to direct the client to get the requested resource at another URI with a GET request.",
            ResponseTypes.REDIRECT,
        ),
        304: (
            "Not Modified",
            "Indicates that the resource has not been modified since the version specified by the request headers If-Modified-Since or If-None-Match.",
            ResponseTypes.REDIRECT,
        ),
        305: (
            "Use Proxy",
            "Depreciated. The requested resource is available only through a proxy, the address for which is provided in the response.",
            ResponseTypes.REDIRECT,
        ),
        306: (
            "Switch Proxy",
            'No longer used. Originally meant "Subsequent requests should use the specified proxy."',
            ResponseTypes.REDIRECT,
        ),
        307: (
            "Temporary Redirect",
            "The server sends this response to direct the client to get the requested resource at another URI with same method that was used in the prior request.",
            ResponseTypes.REDIRECT,
        ),
        308: (
            "Permanent Redirect",
            "This means that the resource is now permanently located at another URI, specified by the Location: HTTP Response header.",
            ResponseTypes.REDIRECT,
        ),
        # Client Error Responses
        400: (
            "Bad Request",
            "The server cannot or will not process the request due to something that is perceived to be a client error.",
            ResponseTypes.CLIENT_ERROR,
        ),
        401: (
            "Unauthorized",
            "Similar to 403 Forbidden, but specifically for use when authentication is required and has failed or has not yet been provided.",
            ResponseTypes.CLIENT_ERROR,
        ),
        402: (
            "Payment Required",
            "Reserved for future use.",
            ResponseTypes.CLIENT_ERROR,
        ),
        403: (
            "Forbidden",
            "The request contained valid data and was understood by the server, but the server is refusing action.",
            ResponseTypes.CLIENT_ERROR,
        ),
        404: (
            "Not Found",
            "The server can not find the requested resource.",
            ResponseTypes.CLIENT_ERROR,
        ),
        405: (
            "Method Not Allowed",
            "The request method is known by the server but has been disabled and cannot be used.",
            ResponseTypes.CLIENT_ERROR,
        ),
        406: (
            "Not Acceptable",
            "The requested resource is only capable of generating content not acceptable according to the Accept headers sent in the request.",
            ResponseTypes.CLIENT_ERROR,
        ),
        407: (
            "Proxy Authentication Required",
            "The client must first authenticate itself with the proxy.",
            ResponseTypes.CLIENT_ERROR,
        ),
        408: (
            "Request Timeout",
            "The server timed out waiting for the request.",
            ResponseTypes.CLIENT_ERROR,
        ),
        409: (
            "Conflict",
            "The request could not be completed because of a conflict in the request.",
            ResponseTypes.CLIENT_ERROR,
        ),
        410: (
            "Gone",
            "The requested page is no longer available.",
            ResponseTypes.CLIENT_ERROR,
        ),
        411: (
            "Length Required",
            'The "Content-Length" is not defined. The server will not accept the request without it.',
            ResponseTypes.CLIENT_ERROR,
        ),
        412: (
            "Precondition Failed",
            "The precondition given in the request evaluated to false by the server.",
            ResponseTypes.CLIENT_ERROR,
        ),
        413: (
            "Payload Too Large",
            "The server will not accept the request, because the request payload is too large.",
            ResponseTypes.CLIENT_ERROR,
        ),
        414: (
            "URI Too Long",
            "The server will not accept the request, because the URL is too long.",
            ResponseTypes.CLIENT_ERROR,
        ),
        415: (
            "Unsupported Media Type",
            "The server will not accept the request, because the media type is not supported.",
            ResponseTypes.CLIENT_ERROR,
        ),
        416: (
            "Range Not Satisfiable",
            "The client has asked for a portion of the file, but the server cannot supply that portion.",
            ResponseTypes.CLIENT_ERROR,
        ),
        417: (
            "Expectation Failed",
            "The server cannot meet the requirements of the Expect request-header field.",
            ResponseTypes.CLIENT_ERROR,
        ),
        418: (
            "I'm a teapot",
            "The server refuses the attempt to brew coffee with a teapot.",
            ResponseTypes.CLIENT_ERROR,
        ),
        421: (
            "Misdirected Request",
            "The request was directed at a server that is not able to produce a response.",
            ResponseTypes.CLIENT_ERROR,
        ),
        422: (
            "Unprocessable Entity",
            "The request was well-formed but was unable to be followed due to semantic errors.",
            ResponseTypes.CLIENT_ERROR,
        ),
        423: (
            "Locked",
            "The resource that is being accessed is locked.",
            ResponseTypes.CLIENT_ERROR,
        ),
        424: (
            "Failed Dependency",
            "The request failed due to failure of a previous request.",
            ResponseTypes.CLIENT_ERROR,
        ),
        425: (
            "Too Early",
            "Indicates that the server is unwilling to risk processing a request that might be replayed.",
            ResponseTypes.CLIENT_ERROR,
        ),
        426: (
            "Upgrade Required",
            "The client should switch to a different protocol such as TLS/1.0.",
            ResponseTypes.CLIENT_ERROR,
        ),
        428: (
            "Precondition Required",
            "The origin server requires the request to be conditional.",
            ResponseTypes.CLIENT_ERROR,
        ),
        429: (
            "Too Many Requests",
            "The user has sent too many requests in a given amount of time.",
            ResponseTypes.CLIENT_ERROR,
        ),
        431: (
            "Request Header Fields Too Large",
            "The server is unwilling to process the request because its header fields are too large.",
            ResponseTypes.CLIENT_ERROR,
        ),
        451: (
            "Unavailable For Legal Reasons",
            "The user requests an illegal resource, such as a web page censored by a government.",
            ResponseTypes.CLIENT_ERROR,
        ),
        # Server Error Responses
        500: (
            "Internal Server Error",
            "The server has encountered a situation it does not know how to handle.",
            ResponseTypes.SERVER_ERROR,
        ),
        501: (
            "Not Implemented",
            "The request method is not supported by the server and cannot be handled.",
            ResponseTypes.SERVER_ERROR,
        ),
        502: (
            "Bad Gateway",
            "The server, while acting as a gateway or proxy, received an invalid response from an inbound server it accessed while attempting to fulfill the request.",
            ResponseTypes.SERVER_ERROR,
        ),
        503: (
            "Service Unavailable",
            "The server is not ready to handle the request.",
            ResponseTypes.SERVER_ERROR,
        ),
        504: (
            "Gateway Timeout",
            "The server, while acting as a gateway or proxy, did not receive a timely response from an upstream server it needed to access in order to complete the request.",
            ResponseTypes.SERVER_ERROR,
        ),
        505: (
            "HTTP Version Not Supported",
            "The server does not support the HTTP protocol version used in the request.",
            ResponseTypes.SERVER_ERROR,
        ),
        506: (
            "Variant Also Negotiates",
            "Transparent content negotiation for the request results in a circular reference.",
            ResponseTypes.SERVER_ERROR,
        ),
        507: (
            "Insufficient Storage",
            "The server is unable to store the representation needed to complete the request.",
            ResponseTypes.SERVER_ERROR,
        ),
        508: (
            "Loop Detected",
            "The server detected an infinite loop while processing the request.",
            ResponseTypes.SERVER_ERROR,
        ),
        510: (
            "Not Extended",
            "Further extensions to the request are required for the server to fulfill it.",
            ResponseTypes.SERVER_ERROR,
        ),
        511: (
            "Network Authentication Required",
            "The client needs to authenticate to gain network access.",
            ResponseTypes.SERVER_ERROR,
        ),
    }
