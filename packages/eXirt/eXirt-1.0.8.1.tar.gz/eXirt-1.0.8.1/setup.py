# read the contents of your README file
from pathlib import Path
from distutils.core import setup

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(name='eXirt',
      description='Explainable Artificial Intelligence tool base in Item Response Theory.',
      author='José de Sousa Ribeiro Filho',
      author_email='jose.sousa.filho@gmail.com',
      version='1.0.8.1',
      packages=['pyexirt'],
      license='CC0 1.0 Universal'
      )

