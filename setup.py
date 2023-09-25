from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in erp_champions_pos/__init__.py
from erp_champions_pos import __version__ as version

setup(
	name="erp_champions_pos",
	version=version,
	description="ERP Champions POS Awesome Changes",
	author="Simon Wanyama",
	author_email="wanyamasp@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
