import pathlib
from setuptools import setup, find_packages

setup(
    name='tkrdisc',
    license='MIT',
    version='0.2.5',
    author='tlkr.',
    author_email='toolkitr.email@gmail.com',
    description='Custom Discord API Wrapper',
    long_description=pathlib.Path('README.md').read_text(),
    long_description_content_type='text/markdown',
    url='https://github.com/toolkitr/tkrdisc',
    entry_points={"console_scripts": ["tkrdisc=tkrdisc.cli:main"]},
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
        'Typing :: Typed',
    ],
    keywords='tkrdiscord, discordtool, tkrdisc',
    python_requires='>=3.10.0,<3.12',
    install_requires=[
      "aiohttp>=3.7.4",
      "asyncio>=3.4.3",
      "async-timeout>=3.0.1",
      "requests>=2.26.0",
      "datetime>=4.3.1",
    ],
    project_urls={
        'Bug Reports': 'https://github.com/toolkitr/tkrdisc/issues',
        'Source': 'https://github.com/toolkitr/tkrdisc',
    },
)