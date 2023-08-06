#! usr/bin/env python
# _*_ coding:utf-8 _*_


from setuptools import setup,find_packages

VERSION = '0.1'

setup(name = 'swagdog',
      version=VERSION,
      description='swagdog cli tools',
      long_description='swagdog cli tools',
      classifiers=[],
      kerwords='swagdog',
      author='guofangmin',
      author_email='1217435382@qq.com',
      url='https://github.com/huahuabiji/ApiTesting.git',
      license='fangmin0325',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=True,
      install_requires=['PyYAML'],
      entry_potions={
          'console_scripts':['swagdog=swagdogsrc.swagdog:entry']
      }




)


