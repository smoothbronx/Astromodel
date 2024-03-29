access_denied = {
    "wsgi": {
        "code": 403,
        "error": "Access denied.",
        "addition": "Your token is out of date or invalid."
                    " If you need a token, then inform the administration of the resource.",
        "contact": "xenofium.manager@gmail.com"
    },
    "asgi": {
        "event": "server.access_denied",
        "message": "Your token is out of date or invalid. If you need a token, then inform the administration of the resource."
    }
}
