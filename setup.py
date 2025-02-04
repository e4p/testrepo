from setuptools import setup

setup(
    name='evanptestmodule',
    version='0.3',
    description='test module',
    author='Evan Parker',
    author_email='',
    py_modules=['evanptestmodule'],
    license='Apache 2.0',
    test_suite='nose.collector',
    tests_require=['nose'],
    use_2to3=False,
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Other Audience',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Other/Nonlisted Topic',
    ]
)
