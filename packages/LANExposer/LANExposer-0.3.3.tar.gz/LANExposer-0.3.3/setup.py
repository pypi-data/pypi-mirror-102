from setuptools import setup


setup(
    name='LANExposer',
    version='0.3.3',
    description='Make LAN requests remotely.',
    long_description=open('README.md', 'r').read(),
    long_description_content_type='text/markdown',
    packages=['lanexpose'],
    install_requires=['requests', 'click', 'flask', 'pyngrok'],
    entry_points = {
        'console_scripts': [
            'lanexpose=lanexpose.cli:cli',
        ],
    }
)