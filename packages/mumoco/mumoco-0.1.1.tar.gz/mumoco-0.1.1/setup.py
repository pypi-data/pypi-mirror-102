from setuptools import setup

setup(
    name='mumoco',
    version='0.1.1',
    packages=['src', 'src.conanbuilder'],
    url='https://github.com/disroop/mumoco',
    license='LICENSE.txt',
    author='michel',
    author_email='michel.meyer@disroop.ch',
    description='This is tool helps to work with multiple conan modules simultaneously.',
    install_requires=[
          'conan',
      ],
    entry_points={
    'console_scripts': [
        'mumoco = src.mumoco:main']
    },
)
