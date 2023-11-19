import setuptools

setuptools.setup(
    name="mhacks1",
    version="1.3",
    author="aarham",
    author_email="aarham.wasit@gmail.com",
    description="mhacks devtools",
    url="https://pypi.org/project/mhacks1",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'openai',
    ],
    entry_points={
        'console_scripts': [
            'mhacks=mhacks1.testing1:main',
        ],
    },
)
