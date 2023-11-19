import setuptools

setuptools.setup(
    name="mhacks1",
    version="1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A small example package",
    url="http://example.com/my_package",
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
            'mhacks1-run=mhacks1.handler:main',
        ],
    },
)
