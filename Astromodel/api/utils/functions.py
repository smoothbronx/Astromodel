from django.core.files.base import ContentFile
from api.models import Query
from json import dumps


createQuery = lambda protocol, request, response: Query(protocol=protocol, debug=request.get("debug", False), **transformData(request=request, response=response)).save()

transformData = lambda **kwargs: dict(map(lambda items: (items[0], generateFile(items[0], items[1], ".json")), kwargs.items()))

generateFile = lambda filename, content, extension: ContentFile(name=filename+extension, content=dumps(content, indent=4))
