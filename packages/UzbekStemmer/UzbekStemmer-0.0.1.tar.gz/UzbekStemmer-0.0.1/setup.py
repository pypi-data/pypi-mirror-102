from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setup(
    name='UzbekStemmer',
    version='0.0.1',
    author='Ulugbek Salaev',
    author_email='ulugbek0302@gmail.com',
    classifiers=classifiers,
    description='Uzbek Stemmer',
    long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
    url='',
    license='MIT',
    keywords='uzbek stemmer',
    packages=find_packages(),
    install_requires=['']
)
