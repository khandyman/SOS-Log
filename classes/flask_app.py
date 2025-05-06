
class FlaskApp(object):
    def __init__(self, app, **configs):
        self._app = app
        self.configs(**configs)

    def configs(self, **configs):
        for config, value in configs:
            self._app.config[config.upper()] = value

    def add_endpoint(
            self,
            endpoint=None,
            endpoint_name=None,
            handler=None,
            methods=None
    ):
        if methods is None:
            methods = ['GET', 'POST']

        self._app.add_url_rule(endpoint, endpoint_name, handler, methods=methods)

    def run(self, **kwargs):
        self._app.run(**kwargs)
