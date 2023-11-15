import pkg_resources

from pathlib import Path


mapping = {}

web_func = {}

service_resolvers = {}


class Resolver:
    def __init__(self, host, mock):
        self.mock = mock
        self.host = host
        for entry_point in pkg_resources.iter_entry_points('swodl_service_resolvers'):
            service_resolvers[entry_point.name] = entry_point.load()
            try:
                from swodl_interpreter.inbuild_functions import functions

                functions.update(
                    service_resolvers[entry_point.name]().get_functions())
            except:
                pass

    def _get_resolver(self):
        filtered = [v for k, v in service_resolvers.items() if k != 'mock']
        if self.mock and Path(self.mock).exists():
            r = service_resolvers.get('mock', None)
            r.resolver = filtered[0]() if filtered else None
            r.config['mock'] = self.mock
            return r
        elif filtered:
            return filtered[0]
        return None

    def get(self, path, name):
        service, interface = path.split('/')
        if name in mapping:
            name = mapping[name]

        def web(*args, **kwargs):
            resolver = self._get_resolver()
            if resolver == None:
                return None
            resolver.host = self.host
            try:
                s = resolver().get_service(service, interface)
            except Exception as e:
                raise ResolveException(
                    f'Failed to find {service}/{interface} service in {self.host}. {e}'
                )
            try:
                method = s.get_method(name)
            except Exception as e:
                raise ResolveException(
                    f'Failed to get {name} from {service}/{interface}. {e}'
                )
            return method(*args, **kwargs)

        web_func[name] = web
        return web_func[name]

    def get_config(self, profileName, keys, default=''):
        return self._get_resolver()().get_config(profileName, keys, default)

    def get_wf(self, name):
        return self._get_resolver()().get_wf(name)

    def get_services(self):
        resolver = self._get_resolver()
        if resolver:
            return resolver().get_services()


class ResolveException(Exception):
    pass
