import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.md')) as f:
    README = f.read()

with open(os.path.join(here, 'pip-freeze.txt')) as f:
    all_requires = [line.strip() for line in filter(None, f.readlines())]

dependency_links = [requirement for requirement in all_requires
                    if requirement.startswith('https://')]

install_requires = [(requirement.partition('#egg=')[-1]
                     if requirement in dependency_links
                     else requirement) for requirement in all_requires]

from pprint import pprint
pprint(dependency_links)
pprint(install_requires)

with open(os.path.join(here, 'VERSION')) as f:
    version = f.read().strip()

setup(name='rapidpro',
      version=version,
      description=(
          "RapidPro allows organizations to visually build scalable "
          "interactive messaging applications."),
      long_description=README,
      classifiers=[
      "Programming Language :: Python",
      ],
      author='Nyaruka, UNICEF',
      author_email='rapidpro@googlegroups.com',
      url='http://github.com/rapidpro/rapidpro',
      license='GNU Affero General Public License',
      keywords='rapidpro',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=install_requires,
      dependency_links=dependency_links)
