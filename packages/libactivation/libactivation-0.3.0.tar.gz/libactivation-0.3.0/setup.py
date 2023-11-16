from setuptools import setup, find_packages

setup(
        name="libactivation", 
        version="0.3.0",
        author="Bastiaan Quast",
        author_email="<bquast@gmail.com>",
        packages=find_packages(),
        install_requires=['numpy',],
        keywords=['sigmoid', 'ReLU'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)
