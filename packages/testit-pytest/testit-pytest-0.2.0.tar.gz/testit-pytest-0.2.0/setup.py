from setuptools import setup

setup(
    name='testit-pytest',
    version='0.2.0',
    description='Pytest plugin for TestIT',
    url='https://pypi.org/project/testit-pytest/',
    author='Pavel Butuzov',
    author_email='pavel.butuzov@testit.software',
    license='proprietary',
    py_modules=['testit', 'testit_pytest'],
    packages=['testit_pytest'],
    package_dir={'testit_pytest': 'src'},
    install_requires=['pytest', 'requests'],
    entry_points={'pytest11': ['testit_pytest = testit_pytest.plugin']}
)
