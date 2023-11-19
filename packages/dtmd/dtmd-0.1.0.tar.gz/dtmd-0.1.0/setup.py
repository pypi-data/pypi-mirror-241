from setuptools import setup, find_packages

setup(
    name='dtmd',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    description='A tool to convert directory contents to Markdown.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/adriangalilea/dtm',
    author='Adrian Galilea Delgado',
    author_email='adriangalilea@gmail.com',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    install_requires=[
        'rich',
        'pyperclip',
        'fnmatch'
    ],
    entry_points={
        'console_scripts': [
            'dtj=dtj.main:main',
        ],
    },
)
