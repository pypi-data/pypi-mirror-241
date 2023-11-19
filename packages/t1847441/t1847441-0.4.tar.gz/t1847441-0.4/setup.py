from setuptools import setup, find_packages

setup(
    name='t1847441',
    version='0.4',
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    entry_points={
        'console_scripts': [
            't1847441=t1847441:main',
        ],
    },
    include_package_data=True,
    package_data={
        'ваш_пакет': ['static/*'],
    },
)

