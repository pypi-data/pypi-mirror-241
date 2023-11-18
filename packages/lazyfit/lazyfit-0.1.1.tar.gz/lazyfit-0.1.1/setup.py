from setuptools import setup

######################################################################################################
################ You May Remove All the Comments Once You Finish Modifying the Script ################
######################################################################################################

setup(
    
    name = 'lazyfit', 
    
    version = '0.1.1',
    
    description = 'A python package that helps with the construction and optimization of RBF interpolants.',
    
    package_dir = {'':'src'},
    
    packages = ['lazyfit'],
    
    author = 'Alex Shaffer',
    author_email = 'alex.shaffer144@gmail.com',
    
    
    long_description = open('README.md').read() + '\n\n' + open('CHANGELOG.md').read(),
    long_description_content_type = "text/markdown",
    
    url='https://github.com/redhorn144/lazyfit.git',
    
    
    include_package_data=True,
    
    classifiers  = [
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        "License :: OSI Approved :: BSD License",
        'Intended Audience :: Developers',
        'Intended Audience :: Other Audience',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Education',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: OS Independent',
    ],
    
    install_requires = [

        'numpy ~= 1.23.5',
        'scipy ~= 1.10.1'

    ],
    
    keywords = ['Interpolation', 'Data Science'],
    
    )
