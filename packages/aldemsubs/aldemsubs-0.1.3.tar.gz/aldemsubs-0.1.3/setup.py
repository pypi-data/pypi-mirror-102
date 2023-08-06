import setuptools

with open('README.md', 'r') as f:
    long_description = f.read()

setuptools.setup(
    name="aldemsubs",
    version="0.1.3",
    author="Paul Hillmann - 80KiloMett",
    author_email="80kilomett@posteo.de",
    description="Subscribe to Youtube channels via RSS",
    url="https://gitlab.com/80KiloMett/aldemsubs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license_files=['LICENSE'],
    packages=setuptools.find_packages(exclude=('tests')),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
    ],
    install_requires=[
        "feedparser",
        "youtube-dl",
    ],
    extras_require={
        'dev': [
            'pytest',
        ]
    },
    scripts=['bin/aldemsubs'],
    python_requires='>=3.7',
)
