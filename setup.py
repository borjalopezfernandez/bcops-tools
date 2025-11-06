"""
pip install -e src/
python3 src/test.py
"""
from setuptools import setup, Extension, find_packages

setup(
    license_files           =   ['LICENSE'],
    python_requires         =   ">3.11",       # only applies to sdist
    name                    =   "bcops",
    version                 =   "0.0.2",
    description             =   "BCOPS tools",
    package_dir             =   {"": "src"},
    scripts                 =   ['src/bcops_maap_query_datatake'],
    install_requires        =   ['pytest', 'loguru', 'click', 'pystac_client'],
    extras_require          =   {},
)

print("Completed execution of python setup pyeocfi:")
print("\U0001F606")
