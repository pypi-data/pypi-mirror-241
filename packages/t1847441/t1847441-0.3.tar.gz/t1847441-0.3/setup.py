from setuptools import setup, find_packages

setup(
    name='t1847441',
    version='0.3',
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    entry_points={
        'console_scripts': [
            't1847441=t1847441:main',
        ],
    },
)

