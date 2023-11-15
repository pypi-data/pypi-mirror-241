from setuptools import setup, find_packages

setup(
    name="pklue",
    version="0.1.1",
    description="Korean Datasets for Instruction Tuning",
    packages=["pklue"],
    author="Jeongwook Kim",
    author_email="k0s1k0s1k0@korea.ac.kr",
    install_requires=[
        'datasets',
    ],
)