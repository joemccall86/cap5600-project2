"""
/**
 * Setup class used by setup-tools in Python
 *
 * @author Joe McCall; Chris Zahuranec
 * @date 4/24/2020
 * @info Course CAP5600
 */
"""
from setuptools import setup, find_packages

setup(
    name="Project2",
    version="0.1",
    packages=find_packages(),

    # Project uses PANDAS. As of this writing 1.0.3 is required
    install_requires=[
        'pandas>=1.0.3',
        'requests>=2.23.0'
    ]
)
