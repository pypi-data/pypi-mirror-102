from distutils.core import setup
from setuptools import find_packages

with open("README.md", "r", encoding='UTF-8') as f:
  long_description = f.read()

setup(name='SignatureSuper-Resolution',  # 包名
      version='1.0.0',  # 版本号
      description='Sinature Super-Resolution',
      long_description=long_description,
      author='zhou peng cheng',
      author_email='707480880@qq.com',
      url='http://192.168.3.42:3000/zhoupengcheng/ssr',
      install_requires=[],
      license='MIT License',
      packages=find_packages(),
      platforms=["all"],
      classifiers=[
          'Intended Audience :: Developers',
          'Operating System :: OS Independent',
          'Natural Language :: Chinese (Simplified)',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
          'Topic :: Software Development :: Libraries'
      ],
      )