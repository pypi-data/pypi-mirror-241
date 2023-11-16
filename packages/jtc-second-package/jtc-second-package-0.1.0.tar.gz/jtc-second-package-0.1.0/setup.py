from setuptools import setup, find_packages

setup(
    name='jtc-second-package',
    version='0.1.0',
    author='jmccay2',
    author_email='j.mccay164@hotmail.com',
    description='Second package of JTC.',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)