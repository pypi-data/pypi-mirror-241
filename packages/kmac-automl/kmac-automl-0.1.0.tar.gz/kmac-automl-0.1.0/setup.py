from setuptools import setup, find_packages


setup(
    name='kmac-automl',
    version='0.1.0',
    packages=find_packages(where='src'),
    install_requires=['pycaret[full]'],
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    author='KMAC-DX',
    author_email='yyam1020@kmac.co.kr',
    description='KMAC AutoML Solution',
    license='KMAC',
    # keywords='AutoML machine-learning',
    package_dir={"": "src"},
    url='https://github.com/yyam1020-kmac/automl'
)

