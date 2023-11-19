from setuptools import setup, find_packages

setup(
    name='t1847441',
    version='0.7',
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    entry_points={
        'console_scripts': [
            't1847441=__main__:main',
        ],
    },
    include_package_data=True,
    package_data={
        '': ['static/*'],
    },
)

