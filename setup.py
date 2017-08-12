from setuptools import setup


setup(
    name='kerblog',
    version='0.1',
    license='MIT',
    author='Sean Gilleran',
    author_email='sgilleran@gmail.com',
    url='https://github.com/seangilleran/kerblog',
    download_url='https://github.com/seangilleran/kerblog/tarball/0.3',
    packages=['kerblog'],
    install_requires=[
        'Flask>=0.11',
        'Markdown>=2.6',
        'bleach>=1.4'],
    include_package_data=True,
    zip_safe=False
)

