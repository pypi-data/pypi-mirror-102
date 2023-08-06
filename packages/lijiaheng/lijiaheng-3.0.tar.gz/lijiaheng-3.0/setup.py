# encoding:utf-8
from setuptools import setup, find_packages

setup(
    name='lijiaheng',
    version='3.0',
    description='测试setuptools的功能',
    author='lijiaheng',
    author_email='417452756@qq.com',
    url='https://www.lijiaheng.cn',
    keywords='lijiaheng',
    packages=find_packages(exclude=[]),
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'lijiaheng=main.lijiaheng:main',
        ],
    },
    scripts=[],
    install_requires=['redis'],
)
