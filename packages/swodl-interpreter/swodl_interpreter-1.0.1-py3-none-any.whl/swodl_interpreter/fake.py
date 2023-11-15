class WebFake:
    def get_service(self, service, interface):
        return WebFake()

    def get_method(self, name):
        def web(*args, **kwargs):
            if name == 'ERROR':
                raise Exception(name)
            return f'{name}'.join(args)

        return web

    config = {'Test': {'Test': 'Test'}}

    def get_config(self, profileName, keys, default=''):
        if profileName in self.config:
            profile = self.config[profileName]
            for key in keys.split('/'):
                if key in profile:
                    profile = profile[key]
                else:
                    return default
            return profile
        else:
            return default

    def get_wf(self, name):
        if name == 'fake':
            return 'var fake = 123;'
        else:
            raise Exception('FAKE')

    def get_functions(self):
        return {'ololo': lambda a: 'olo' * a}
