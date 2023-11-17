from setuptools import setup, find_packages

setup(
    name='aziraclient',
    version='0.1.3',
    author='Emmanuel Akanji',
    author_email='omoebun52@gmail.com',
    description='A library built for azira application to make it easier for users to subscribe to crypto tokens and continuously receive data in near real-time',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/manny-uncharted/aziraclient',  # Replace with your own GitHub URL
    packages=find_packages(),
    install_requires=[
        "amqp==5.2.0",
        "annotated-types==0.6.0",
        "anyio==3.7.1",
        "async-timeout==4.0.3",
        "fastapi==0.104.1",
        "fastapi-socketio==0.0.10",
        "httpcore==1.0.1",
        "httpx==0.25.1",
        "idna==3.4",
        "iniconfig==2.0.0",
        "iso8601==2.1.0",
        "jwt==1.3.1",
        "kombu==5.3.3",
        "Mako==1.3.0",
        "pytest==7.4.3",
        "python-engineio==4.8.0",
        "python-socketio==5.10.0",
        "requests==2.31.0",
        "websockets==12.0",
        "zmq==0.0.0",

    ],
    classifiers=[
        # Classifiers help users find your project
        # Full list: https://pypi.org/classifiers/
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
