import setuptools

with open("README.md", "r") as file_obj:
    long_description = file_obj.read()

def get_requirements(f):
    requires = []
    with open(f) as file_obj:
        for req in file_obj:
            req = req.strip()
            if len(req) > 1 and "# " not in req:
                requires.append(req)
    return requires

packages = setuptools.find_packages()

setuptools.setup(
    name="nubium-utils",
    version="0.24.0",
    author="Edward Brennan",
    author_email="ebrennan@redhat.com",
    description="Some Kafka utility functions and patterns for the nubium project",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.corp.redhat.com/mkt-ops-de/nubium-utils.git",
    packages=packages,
    install_requires=get_requirements('requirements.txt'),
    tests_require=get_requirements('requirements-faust.txt'),
    extras_require={"dev": get_requirements('requirements-dev.txt'), "faust": get_requirements('requirements-faust.txt')},
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
