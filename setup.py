from setuptools import setup, find_packages

setup(
    name="gps_lib",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        'pyserial',
    ],
    author="Nathan Adkins",
    author_email="npa00003@mix.wvu.edu",
    description="Interfacing with the NEO-6M-0-001 Blox GPS Module",
    license="MIT",
    keywords="gps robotics",
)