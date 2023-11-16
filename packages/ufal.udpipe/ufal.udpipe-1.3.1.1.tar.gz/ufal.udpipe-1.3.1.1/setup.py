import setuptools
import sys

with open('README') as file:
    readme = file.read()

extra_link_args = []
extra_compile_args = ['-std=c++11', '-w']
if sys.platform == "darwin":
    extra_compile_args += ['-stdlib=libc++']
    extra_link_args += ['-stdlib=libc++']

setuptools.setup(
    name             = 'ufal.udpipe',
    version          = '1.3.1.1',
    description      = 'Bindings to UDPipe library',
    long_description = readme,
    author           = 'Milan Straka',
    author_email     = 'straka@ufal.mff.cuni.cz',
    url              = 'https://ufal.mff.cuni.cz/udpipe',
    license          = 'MPL 2.0',
    packages         = ['ufal', 'ufal.udpipe'],
    ext_modules      = [setuptools.Extension(
        'ufal.udpipe._udpipe',
        ['ufal/udpipe/udpipe.cpp', 'ufal/udpipe/udpipe_python.cpp'],
        language = 'c++',
        extra_compile_args = extra_compile_args,
        extra_link_args = extra_link_args)],
    classifiers      = [
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)',
        'Programming Language :: C++',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries'
    ]
)
