from setuptools import setup, find_packages

VERSION = '0.0.3' 
DESCRIPTION = 'A simple logger module'
LONG_DESCRIPTION = 'A simple logger module that prints the data with tags like [INFO], [ERROR], [WARNING]'

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="BetterPrintLogger", 
        version=VERSION,
        author="Dhanush Gowdhaman",
        author_email="dhanush.gowdhaman@gmail.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        
        keywords=['python', 'first package', 'print'],
        classifiers= [
            "Development Status :: 1 - Planning",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)