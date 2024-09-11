from setuptools import setup, find_packages

setup(
    name="drawscape-factorio",
    version="0.15.19",
    description="Drawscape Factorio",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(where="src"),
    url="https://github.com/drawscape-labs/drawscape-factorio",
    package_dir={"": "src"},
    entry_points={
        'console_scripts': [
            'drawscape-factorio=drawscape_factorio.main:main',
        ],
    },
    install_requires=[
        'svgwrite',
        'argparse'
    ],
)