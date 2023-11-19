from setuptools import setup, find_packages

setup(
    name='sandi_connect',
    version='0.1.1',
    author='Luis Gonzalez',
    author_email='luis.gonzalez.pi@usach.cl',
    description='Librería para conectar a un broker MQTT utilizando WebSockets',
    long_description='Aquí puedes proporcionar una descripción más detallada de tu librería y su funcionalidad.',
    url='https://github.com/C-SESLAB/sandi_connect',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    keywords='mqtt websocket library UDP PMU',
    install_requires=[
        'paho-mqtt',
        'crcmod',
        'python-dotenv'
    ],
)
