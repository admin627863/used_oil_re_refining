from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in used_oil_re_refining/__init__.py
from used_oil_re_refining import __version__ as version

setup(
	name="used_oil_re_refining",
	version=version,
	description="Used Oil Re-refining ",
	author="alantechnologies",
	author_email="jayakumar@alantechnologies.net",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
