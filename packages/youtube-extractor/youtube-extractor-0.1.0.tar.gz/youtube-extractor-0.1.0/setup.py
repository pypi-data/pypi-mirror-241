from setuptools import setup, find_packages

setup(
    name='youtube-extractor',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        # Add any dependencies your package needs
        'requests',
    ],
    entry_points={
        'console_scripts': [
            # If your package provides any command-line scripts
        ],
    },
    author='super nived',
    author_email='nivedchandran7@gmail.com',
    description='A package for extracting YouTube video IDs from URLs',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/super-nived/youtube-extractor',
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
