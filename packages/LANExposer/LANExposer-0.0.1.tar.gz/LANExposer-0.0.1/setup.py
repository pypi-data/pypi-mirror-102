from setuptools import setup


setup(
    name='LANExposer',
    version='0.0.1',
    description='Make LAN requests remotely.',
    long_description=open('README.md', 'r').read(),
    long_description_content_type='text/markdown',
    entry_points = {
        'console_scripts': [
            'lanexpose=lanexpose.cli:cli',
        ],
    }
)