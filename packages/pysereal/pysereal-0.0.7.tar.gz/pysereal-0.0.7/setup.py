from setuptools import setup, find_packages

VERSION = "0.0.7"
DESCRIPTION = "Serial"

# Setting up
setup(
    name="pysereal",
    version=VERSION,
    author="Rye",
    author_email="rye@rye.com",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=[
        ""
        "discord==2.2.3",
        "InquirerPy==0.3.4",
        "Pillow==9.5.0",
        "psutil==5.9.5",
        "pycryptodome==3.17",
        "pyobf2==1.2.0",
        "pywin32==306",
        "Requests==2.31.0",
        "WMI==1.5.1",
        "urllib3==2.0.2",
        "attrs==23.1.0",
    ],
    keywords=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows",
    ],
)
