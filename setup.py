"""
pip install -e src/
python3 src/test.py
"""
from setuptools import setup, Extension, find_packages

setup(
    license_files           =   ['LICENSE'],
    python_requires         =   ">3.11",       # only applies to sdist
    name                    =   "bcops",
    version                 =   "0.0.15",
    description             =   "BCOPS tools",
    package_dir             =   {"bcops": "src/bcops"},
    package_data            =   {'bcops': ['data/*']},
    include_package_data    =   True,
    scripts                 =   [
                                    'src/bcops/bcops_bmpf_afunav',
                                    'src/bcops/bcops_bmpf_downlink_idleframes',
                                    'src/bcops/bcops_bmpf_bct_pass',
                                    'src/bcops/bcops_bmpf_ocm_segment',
                                    'src/bcops/bcops_bmpf_kml_arrange',
                                    'src/bcops/bcops_product_compact_creation_date',
                                    'src/bcops/bcops_maap_query_datatake',
                                    'src/bcops/bcops_maap_query_product'
                                 ],
    install_requires        =   ['pytest', 'loguru', 'lxml', 'click', 'pystac_client', 'pytz'],
    extras_require          =   {},
)

print("Completed execution of python setup pyeocfi:")
print("\U0001F606")