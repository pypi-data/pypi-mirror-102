from setuptools import setup, find_packages


install_requires = [
    'Flask>=1.1.2',
    'Flask-GraphQL>=2.0.1',
    'Flask-Sockets>=0.2.1',
    'graphql-ws>=0.3.1',
    'gevent>=1.5.0',
    'gevent-websocket>=0.10.1',
    'graphene>=2.1.8',
    'Rx>=1.6.1'
]

setup(
    name='rss_to_graphql',
    version='0.0.1',
    author='Kuda Savanhu',
    maintainer='Kuda Savanhu',
    description='A microservice proxy to convert an rss feed to a GraphQL API endpoint',
    long_description=open('README.md').read(),
    long_description_content_type = "text/markdown",
    packages=find_packages(),
    install_requires=install_requires,

    keywords=['python', 'rss to graphql', 'requests', 'rss', 'graphql'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Operating System :: OS Independent',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Topic :: Utilities',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Server',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
