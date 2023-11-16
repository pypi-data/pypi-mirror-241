from setuptools import setup, find_packages

setup(
    name="tree-commands",
    version="1.0.4",
    description="Build click commands using a tree directory structure",
    long_description="Build click commands using a tree directory structure",
    author="Gabriel Delgado",
    author_email="gadc1996@gmail.com",
    url="https://github.com/gadc1996",
    packages=find_packages(),
    install_requires=[
        "click",
        # Agrega otras dependencias si las tienes
    ],
    entry_points={
        "console_scripts": [
            'tree-commands = tree_commands.root:group',
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
