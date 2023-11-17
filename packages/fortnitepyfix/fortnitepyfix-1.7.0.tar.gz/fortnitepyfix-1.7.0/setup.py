import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


extras_require = {
    'docs': [
        'sphinxcontrib_trio==1.1.2',
        'furo==2021.4.11b34',
        'Jinja2<3.1',
    ]
}


try:
    with open('requirements.txt') as f:
        requirements = f.read().splitlines()
except FileNotFoundError:
    pass

setuptools.setup(
    name="fortnitepyfix",
    version="1.7.0",
    author="klld",
    description="fortnitepyfix",
    long_description=long_description,
    license='MIT',
    long_description_content_type="text/markdown",
    url="https://github.com/Terbau/fortnitepy",

    project_urls={
        "Documentation": "https://fortnitepy.readthedocs.io/en/latest/",
        "Issue tracker": "https://github.com/Terbau/fortnitepy/issues",
    },
    extras_require=extras_require,
    packages=['fortnitepyfix', 'fortnitepyfix.ext.commands'],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ],
    install_requires=[
        'sphinxcontrib_trio==1.1.2',
        'furo==2021.4.11b34',
        'Jinja2<3.1',
        'aiohttp>=3.3',
        'aioxmpp>=0.10.4',
        'pytz',
        'aioconsole'
      ],
)