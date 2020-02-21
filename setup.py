import io
import re
from setuptools import setup, find_packages

# Read in requirements.txt
with open("requirements.txt", "r") as f_requirements:
    requirements = f_requirements.readlines()
requirements = [r.strip() for r in requirements]

with io.open("src/host_setup/__init__.py", "rt", encoding="utf8") as f:
    version = re.search(r"__version__ = \"(.*?)\"", f.read()).group(1)
    print(version)

setup(
    name="host_setup",
    version=version,
    author="Jacques Perrault",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=requirements,
    zip_safe=False,
)
