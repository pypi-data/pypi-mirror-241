
from setuptools import setup,find_packages
setup(
    name='calculatrice',
    packages=find_packages(),
    install_requires=[],
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Exzard Jean Abellard et Payen Sterlin Myfedjy ',
    description='calculatrice',
    url='https://github.com/fedjyst/calculatrice.git',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ]
    )
#     from Package.calculatrice import Calculator
# from  Package.calculatricesci import Calculator1
# # Demonstration
# print(Calculator.addition(1, 2,)) 

# print(Calculator.soustraction(3,4)) 

# print(Calculator.multiplication(2, 4, 5)) 

# print(Calculator.division(100, 2, 5))

# print(Calculator1.exponentielle(2, 3)) 

# print(Calculator1.factorielle(6)) 

# print(Calculator1.square(9, 1, 25))
