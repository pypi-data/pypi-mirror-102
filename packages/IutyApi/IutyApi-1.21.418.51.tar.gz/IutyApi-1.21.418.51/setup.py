from setuptools import setup

version = '1.21.0418.0051'

entry_points={
        'console_scripts': [
            'ipb = IutyApi.server.webserver:main'
        ]
    }

setup(
    name="IutyApi",
    version= version,
    #version = ver,
    packages=[
        "IutyApi.stock",
        "IutyApi.task",
        "IutyApi.usr",
        "IutyApi.dev",
        "IutyApi.file",
        
        "IutyApi.server",
        
        ]
)