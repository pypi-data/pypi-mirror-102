# -*- coding: utf-8 -*-
# @Time    : 2021/4/16 19:35
# @Author  : CZY
# @File    : setup.py
# @Software: PyCharm
import setuptools


setuptools.setup(
    name='plot4gmns',
    version='0.0.6',
    author='Zanyang Cui, Junhua Chen',
    author_email='zanyangcui@outlook.com, cjh@bjtu.edu.cn',
    url='https://github.com/PariseC/plot4gmns',
    description='A visualization tool for visualizing and analyzing transportation network and demand files in GMNS format',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    license='GPLv3+',
    packages=['plot4gmns'],
    python_requires=">=3.6.0",
    install_requires=['pandas', 'shapely','numpy','seaborn','matplotlib <=3.3.0','scipy'],
    classifiers=['License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
                 'Programming Language :: Python :: 3']
)
