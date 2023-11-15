import re
import json

from runpy import run_path
from pathlib import Path


class MockMethod:
    def __init__(self, results):
        self.results = results

    def __call__(self, *args):
        if not self.results:
            return None
        r = [x['result']
             for x in self.results['cases'] if x['args'] == list(args)]
        if r:
            return r[0]
        else:
            return self.results['default']


class MockService:
    def __init__(self, methods):
        self.methods = methods

    def get_method(self, name):
        m = self.methods.get(name, None)
        if not hasattr(self, 'resolver'):
            return MockMethod(m)
        return self.real.get_method(name)


class Mock:
    config = {}

    def __init__(self):
        if 'mock' in Mock.config:
            if re.search(r'\.py$', str(Mock.config['mock'])):
                mock = run_path(str(Mock.config['mock']))
                self.mock = mock['config']
            else:
                with open(Mock.config['mock'], 'r') as f:
                    self.mock = json.loads(f.read())

    def get_service(self, service, interface):
        s = MockService(self.mock['services'].get(
            service, {}).get(interface, {}))
        if hasattr(self, 'resolver') and self.resolver:
            s.real = self.resolver.get_service(service, interface)
        return s

    def get_services(self):
        def _get_method(s):
            return {'methods': {k: x['cases'][0]['args'] for k, x in s.items()}}

        def _get_interfaces(s):
            return {'interfaces': {k: _get_method(v) for k, v in s.items()}}

        def _get_services(s):
            return {
                k: {'type': 8, 'doc': f'{k} service'} | _get_interfaces(v)
                for k, v in s.items()
            }

        return _get_services(self.mock['services'])

    def get_config(self, profile_name, keys, default=''):
        profile = self.mock['config'].get(profile_name, {})
        for key in keys.split('/'):
            if key in profile:
                profile = profile[key]
            else:
                return default or None
        return profile or None

    def get_wf(self, name):
        with open(Path(Mock.config['wfs']) / name, 'r') as f:
            return f.read()

    def get_functions(self):
        return {'mock': lambda: 'Mock!'}
