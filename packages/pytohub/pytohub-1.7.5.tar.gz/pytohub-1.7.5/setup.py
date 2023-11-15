from setuptools import setup

f = open("README.md","r").read()

setup(
    name="pytohub",
    version="v1.7.5",
    author="mas6y6",
    long_description=f,
    long_description_content_type='text/markdown',
    description="This is a module that can connect to your lego RI hub or lego SPIKE PRIME hub and can directly upload modules to your hub",
    license="MIT",
    packages=["pytohub"],
    install_requires=["get-key","requests","progressbar2","serial"]
)