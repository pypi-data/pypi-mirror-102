from setuptools import setup

setup(
    name='mpd_what',
    version='1.0.1',
    author='github.com/charmparticle',
    packages=['mpd_what'],
    scripts=['bin/mpd_what'],
    url='https://github.com/charmparticle/mpd_what',
    license='GPL3',
    description='A python album art and music info getter',
    long_description=open('README.md').read(),
    install_requires=[
        "python-mpd2",
        "pyyaml",
        "requests",
        "latest-user-agents",
        "python-magic",
        "pylast",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)

