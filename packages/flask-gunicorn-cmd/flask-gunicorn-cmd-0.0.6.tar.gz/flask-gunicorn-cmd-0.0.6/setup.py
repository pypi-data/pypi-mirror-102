import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()

# read requirements.txt
with open('requirements.txt', 'r') as f:
    content = f.read()
li_req = content.split('\n')
install_requires = [e.strip() for e in li_req if len(e)]

setuptools.setup(
    name="flask-gunicorn-cmd",
    version="0.0.6",
    author="Dan Lester",
    author_email="dan@ideonate.com",
    description="Command line wrapper to run a named Flask script inside a Gunicorn server",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ideonate/flask-gunicorn-cmd",
    packages=setuptools.find_packages(),
    install_requires=install_requires,
    include_package_data=True,
    zip_safe=False,
    entry_points={"console_scripts": ["flask-gunicorn-cmd = flask_gunicorn_cmd.main:run"]},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)


