import os
import logging
import importlib.util
import sys

import gunicorn.app.base
import click

class FlaskException(Exception):
    pass

class StandaloneApplication(gunicorn.app.base.BaseApplication):

    def __init__(self, app, options=None):
        self.options = options or {}
        self.application = app
        super().__init__()

    def load_config(self):
        config = {key: value for key, value in self.options.items()
                  if key in self.cfg.settings and value is not None}
        for key, value in config.items():
            self.cfg.set(key.lower(), value)

    def load(self):
        return self.application

def make_app(command, server_name=None, debug=False):

    # Command can be absolute, or could be relative to cwd
    app_py_path = os.path.join(os.getcwd(), command)

    print("Fetching Flask script {}".format(app_py_path))

    dirname = os.path.dirname(app_py_path)

    basename = os.path.basename(app_py_path)

    (scriptname, _) = os.path.splitext(basename)

    if os.path.isdir(dirname):
        print("CWD to {}".format(dirname))
        os.chdir(dirname)

        # Add script's folder to Python search path too
        sys.path.append(dirname)

    print("Importing user Flask app")

    spec = importlib.util.spec_from_file_location(scriptname, app_py_path)
    userscript = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(userscript)

    app = None

    if server_name is not None:
        # We have been given an explicit server name (e.g. 'app')
        app = getattr(userscript, server_name, None)

    else:
        # Look for 'app' first, but if it's not right just search for the first Flask object
        
        app = getattr(userscript, 'app', None)

        flaskclassstr = ".app.Flask'>"

        if app is None or not flaskclassstr in str(type(app)):
            from inspect import getmembers
            membs = getmembers(userscript, lambda x: flaskclassstr in str(type(x)))
            if len(membs) > 0:
                app = membs[0][1]

    if app is None:
        raise FlaskException('Cannot find a Flask app inside your script file. There needs to be a flask.app.Flask object. Looking for an object based on server_name {}.'.format(server_name))

    return app


@click.command()
@click.option('--port', default=8888, type=click.INT, help='port for the proxy server to listen on')
@click.option('--ip', default=None, help='Address to listen on')
@click.option('--server-name', default=None, type=click.STRING, 
                help='Name of the flask app inside your script (default None means search for a suitable Flask var)')
@click.option('--workers', default=2, type=click.INT, help='Number of workers')
@click.option('--debug/--no-debug', default=False, help='To display debug level logs')
@click.argument('command', nargs=1, required=True)
def run(port, ip, server_name, workers, debug, command):

    if debug:
        print('Setting debug')

    app = make_app(command, server_name, debug)

    if ip is None:
        ip ='0.0.0.0'

    options = {
        'bind': '%s:%s' % (ip, str(port)),
        'workers': workers,
    }
    StandaloneApplication(app, options).run()

if __name__ == '__main__':

    try:

        run()

    except SystemExit as se:
        print('Caught SystemExit {}'.format(se))
