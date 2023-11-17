from setuptools import setup, find_packages

setup(
    name='emmonite',
    version='0.1.3',
    packages=find_packages(),
    description='Conjunto de librerias',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Javier Bahamondes',
    author_email='jbahamondes@enorchile.cl',
    url='https://github.com/javierbahamondes/emmonite.git',
    install_requires=[
        # No es necesari instalar ningun paquete adicional ya que los utilizados son de python
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Communications :: Email',
    ],
)

