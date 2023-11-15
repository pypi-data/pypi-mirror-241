from setuptools import setup, find_packages

VERSION = '0.0.2'
DESCRIPTION = 'package using setup.py'
LONG_DESCRIPTION = 'First project using setup.py'
requirements = []
extra_requirements = {"dev": ["pytest"]}

# Setting up
setup(
    # the name must match the folder name 'verysimplemodule'
    name="setuppy_mahfooz",
    version=VERSION,
    author="Mahfooz Alam",
    author_email="mahfooz.iiitian@gmail.com",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages("src"),
    package_dir={"": "src"},
    install_requires=requirements,
    extras_require=extra_requirements,
    keywords=['python', 'setup.py', "package"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)