from setuptools import setup, find_packages

VERSION = "0.1"
DESCRIPTION = "Test module to see if i can get things set up in anaconda"
LONG_DESCRIPTION = "Test module to see if i can get things set up in anaconda"

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="example_package_mhawks", 
        version=VERSION,
        author="Michael Hawks",
        author_email="<youremail@email.com>",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        
        keywords=['python', 'first package'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 3",
            "Operating System :: OS Independent"
        ]
)