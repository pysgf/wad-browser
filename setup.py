from distutils.core import setup

setup(
    name='wad-browser',
    version='0.0.1',
    packages=['wadbrowser'],
    scripts=[
        'scripts/wad-browser'
    ]
    license='LICENSE.txt',
    description='A wad browser for the doomworld archive.'
)
