if (__debug__):
    try:
        from .scraper import Scrape
        from .handlers import RequestHandler, UserHandler
        from .exceptions import UserHasNoLocationException, NonePublicArchiveRepositoryException, NoneFilledPropertyException
    
    except ModuleNotFoundError.__doc__ as mnfe:
        raise mnfe