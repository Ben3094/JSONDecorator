from json import JSONDecoder, JSONEncoder, dumps

class JSONDecorator(object):
    TO_EXPORT = dict()

    def __init__(self, *args, encoder=JSONEncoder, decoder=JSONDecoder):
        className = args[0].__qualname__.split('.')[0]
        if not args[0] in JSONDecorator.TO_EXPORT:
            JSONDecorator.TO_EXPORT[className] = list()
        
        JSONDecorator.TO_EXPORT[className].append((args[0].__name__, encoder, decoder))

    def __call__(self, func):
        def wrapped(*args, **kwargs):
            return func(*args, **kwargs)

class JSONDecoratedFieldsClassEncoder(JSONEncoder):
    def default(self, o):
        result = dict()
        for attrName in JSONDecorator.TO_EXPORT[o.__class__.__name__]:
            result |= dumps(getattr(o, attrName))
        return result