from setuptools import setup, find_packages

setup(
    name='get_patch_tuesday',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        # Add your project's dependencies here
    ],
    entry_points={
        'console_scripts': [
            # Add command line scripts here
            'get-patch-tuesday=get_patch_tuesday.patch_tuesday:main',

        ],
    },
    author='Luke Rawlins',
    author_email='hey@lukerawlins.com',
    description='Finds Patch Tuesday for a given year',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/lt-rawlins/get_patch_tuesday',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)