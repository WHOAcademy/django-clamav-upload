from setuptools import find_packages, setup

setup(
    name='django-clamav-upload',
    version='0.1.3',
    packages=find_packages(exclude=['tests', 'tests.*']),
    url='https://github.com/musashiXXX/django-clamav-upload',
    download_url='https://github.com/musashiXXX/django-clamav-upload/tarball/0.1.2',
    license='LICENSE.txt',
    author='Charles Hamilton',
    author_email='musashi@nefaria.com',
    description='A simple upload handler for django that scans inbound streams for malicious content',
    long_description='README.md',
    python_requires='>=3.8',
    install_requires=[
        'Django>=4.2,<6.0',
        'pyClamd==0.3.17',
        'python-magic>=0.4.18',
    ],
    classifiers=[
        'Framework :: Django',
        'Framework :: Django :: 4.2',
        'Framework :: Django :: 5.0',
        'Framework :: Django :: 5.1',
        'Framework :: Django :: 5.2',
        'Programming Language :: Python :: 3',
    ],
    keywords='clamav django upload'
)
