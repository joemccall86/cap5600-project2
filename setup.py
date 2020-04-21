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
