from setuptools import setup
from io import open


def read(filename):
	with open(filename, encoding='utf-8') as file:
		return file.read()


setup(
	name='npdchecker',
	version='0.0.1a1',
	url='https://gitlab.com/whiteapfel/NPDChecker',
	license='Mozilla Public License 2.0',
	author='WhiteApfel',
	install_requires=['httpx'],
	author_email='white@pfel.ru',
	description='Tool for checking the status of the NPD-payer in Russia',
	long_description=read('README.md'),
	long_description_content_type="text/markdown",
	keywords='НПД проверка ФНС статус NPD check FNS status'
)
