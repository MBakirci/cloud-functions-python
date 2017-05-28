from setuptools import setup

setup(
    name='pycloudfn',
    version='0.1.106',
    description='GCP Cloud functions in python',
    url='https://github.com/MartinSahlen/cloud-functions-python',
    author='Martin Sahlen',
    author_email='martin8900@gmail.com',
    license='MIT',
    entry_points={
        'console_scripts': ['py-cloud-fn=cloudfn.cli:main'],
    },
    install_requires=[
        'pyinstaller==3.2.1',
        'Jinja2==2.9.6',
        'python-dateutil==2.6.0',
        'werkzeug==0.12',
        'django==1.11.1',
    ],
    include_package_data=True,
    packages=['cloudfn'],
    zip_safe=False
)
