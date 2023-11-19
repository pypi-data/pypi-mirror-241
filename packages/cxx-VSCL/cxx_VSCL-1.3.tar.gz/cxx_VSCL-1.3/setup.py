from setuptools import setup

setup(
    name='cxx_VSCL',
    version='1.3',
    authors='陈向学',
    description='深职院虚仿',
    packages=["cxx_VSCL"],
    include_package_data=True,
    install_requires=[
        'websocket-client==1.5.2'
    ]
)