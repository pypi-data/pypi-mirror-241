from setuptools import setup, find_packages

setup(
    name='t1847441',
    version='0.9',
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    entry_points={
        'console_scripts': [
            't1847441=t1847441.entry:entry_point',
        ],
    },
    include_package_data=True,
    package_data={
        '': ['static/*'],
    },
)

