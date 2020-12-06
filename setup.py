from setuptools import setup, find_packages


setup(
    name='adventofcode',
    version='0.2020.6',
    project_urls={
        'Source': 'https://github.com/codertee/adventofcode',
    },
    description='adventofcode.com solutions',
    author='codertee',
    maintainer='codertee',
    license='BSD',
    packages=find_packages(),
    zip_safe=False,
    entry_points={
        'console_scripts': ['adventofcode = adventofcode.cmdline:execute']
    },
    python_requires='>=3.7'
)