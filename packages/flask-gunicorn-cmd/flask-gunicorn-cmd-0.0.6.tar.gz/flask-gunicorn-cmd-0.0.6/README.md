# flask-gunicorn-cmd

Command line wrapper to run a named Flask script inside a Gunicorn server.

This project is used in [ContainDS Dashboards](https://github.com/ideonate/cdsdashboards), which is a user-friendly 
way to launch Jupyter notebooks as shareable dashboards inside JupyterHub. Also works with Streamlit and other 
visualization frameworks.

## Install and Run

Install using pip.

```
pip install flask-gunicorn-cmd
```

The file to start is specified on the command line, for example:

```
flask-gunicorn-cmd ~/Dev/myflaskscript.py
```

By default the server will listen on port 8888, importing the Flask app named 'app', or locating the first app.Flask 
object that it can find otherwise.

To specify a different port, use the --port flag.

To explicitly specify the name of your Flask app, use the --server-name flag.

```
flask-gunicorn-cmd --server-name=app --port=8888 --workers=4 ~/Dev/myflaskscript.py
```

To run directly in python: `python -m flask_gunicorn_cmd.main <rest of command line>`

## Changelog

- v0.0.6 Change CWD to script's folder, and also add that folder to the Python search path.
