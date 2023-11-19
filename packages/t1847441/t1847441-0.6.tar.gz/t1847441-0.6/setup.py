import sys
from setuptools import setup, find_packages

sys.path.append('src')

setup(
    name='t1847441',
    version='0.6',
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    entry_points={
        'console_scripts': [
            't1847441=main:main',
        ],
    },
    include_package_data=True,
    package_data={
        '': ['static/*'],
    },
)

