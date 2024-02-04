from setuptools import setup, find_packages

setup(
    name='JP_Consumer-Theory',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'sympy',          # Dependency for symbolic mathematics
        'numpy',          # Dependency for numerical computations
        'scipy',          # Dependency for optimization (fsolve)
        'matplotlib',     # Dependency for plotting
    ],
    author='Jorge Andres Pulgarin Barbosa',
    author_email='japulgarin@uninorte.edu.co',
    description='A Python package for consumer theory optimization and plotting',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Japulgarin/JP_Consumer-Theory',
    license='MIT',
)
