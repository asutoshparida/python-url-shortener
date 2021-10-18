URL_SHORTEN_BASE_ROUTE = "url"


def register_routes(api, app, root="v1"):
    '''
    register each different API entity(base route) with namespace
    '''
    from .url_shortener_controller import url_shortener_api
    api.add_namespace(url_shortener_api, path=f"/{URL_SHORTEN_BASE_ROUTE}")
