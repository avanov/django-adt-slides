from .types import Language

def includeme(config):
    RULES = {'language': Language}
    config.add_route('articles.regional.index', '/articles/{language}', RULES)
