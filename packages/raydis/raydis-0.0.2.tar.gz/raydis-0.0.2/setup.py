from setuptools import setup, find_packages

long_desc = open('README.txt').read()

setup(
  name='raydis',
  version='0.0.2',
  py_modules=['raydis'],
  url='https://github.com/mdfarhaan/raydis',
  author='Mohammed Farhaan',
  author_email='farhaanm110@gmail.com',
  description='Python module to send Discord Message using Discord Webhooks',
  long_description=long_desc,  
  packages=find_packages(),
  license='MIT',
  install_requires=[
    'requests==2.21.0',
    'Discord-Webhooks==1.0.4'
  ],
  classifiers=[
    'Development Status :: 5 - Production/Stable',
    'Environment :: Other Environment',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.6',
  ],
)

