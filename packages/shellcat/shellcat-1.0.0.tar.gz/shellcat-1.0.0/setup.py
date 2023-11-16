from setuptools import setup, find_packages

setup(
    name='shellcat',
    version='1.0.0',
    packages=find_packages(),
    description='ShellCat is a python tool for generating reverse shell payloads',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='serioton',
    author_email='ahmedaminederbali5@gmail.com',
    url='https://github.com/seriotonctf/shellcat',
    install_requires=[
        'requests',
        'pyperclip',
        'urllib3',
        # etc.
    ],
    entry_points={
        'console_scripts': [
            'shellcat.py = shellcat.main_module:main_function',
        ],
    },
    classifiers=[
        # Trove classifiers
        # Full list at https://pypi.org/classifiers/
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
