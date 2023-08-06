from setuptools import setup

with open('README.md', 'r') as f:
	DESCRIPTION = f.read()

setup(name='amogus',
      version='0.1',
      description='AMOGUS',
      long_description=DESCRIPTION,
      long_description_content_type="text/markdown",
      url='http://github.com/dmitrijkotov634/amogus',
      author='Dmitry Kotov',
      author_email='dmitrijkotov634@gmail.com',
      license='MIT',
      packages=['amogus'])