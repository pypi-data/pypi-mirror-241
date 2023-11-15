import json

from convergence.helpers.controller_helpers import convert_object_to_dict
from convergence.internal.observability.request_log import RequestLog
from convergence.internal.observability.serializer_config import ILogSerializer


class JsonLogSerializer(ILogSerializer):
    def __init__(self, path, production):
        self.path = path
        self.production = production

    def save(self, request_log: RequestLog):
        # kwargs = {}
        #
        # if not self.production:
        #     kwargs['indent'] = '  '
        #
        # with open(self.path + '/' + request_log.request_identifier + '.txt', 'w') as file:
        #     json_str = jsonpickle.encode(request_log, **kwargs)
        #     file.write(json_str)
        kwargs = {}

        if not self.production:
            kwargs['indent'] = '  '

        with open(self.path + '/' + request_log.request_identifier + '.txt', 'w') as file:
            json.dump(convert_object_to_dict(request_log), file, **kwargs)
