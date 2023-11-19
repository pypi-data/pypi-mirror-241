import setuptools

pkg_vars = dict()
with open("mutty/_version.py") as f:
    exec(f.read(), pkg_vars)

package_version = pkg_vars["__version__"]
minimum_python_version_required = pkg_vars["__version_minimum_python__"]

with open("requirements.txt", "r", encoding="utf8") as reqs:
    required_packages = reqs.read().splitlines()

with open("README.md") as f:
    readme = f.read()

setuptools.setup(
    name="mutty",
    version=package_version,
    author="Joey Greco",
    author_email="joeyagreco@gmail.com",
    description="Python Mutation Testing.",
    long_description_content_type="text/markdown",
    long_description=readme,
    license="MIT",
    url="https://github.com/joeyagreco/mutty",
    packages=setuptools.find_packages(exclude=("test", "doc", "example", "img", ".github")),
    install_requires=required_packages,
    include_package_data=True,
    python_requires=f">={minimum_python_version_required}",
    keywords="mutation mutant test testing",
)
