from setuptools import setup, find_packages

setup(
    name="drawscape-factorio",
    version="0.12",
    description="Drawscape Factorio",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    entry_points={
        'console_scripts': [
            'drawscape-factorio=drawscape_factorio.main:main',
        ],
    },
)