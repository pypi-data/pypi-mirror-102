#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Time    : 2021/4/20 8:34
@Software: PyCharm
"""

import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="accio_api",  # 包的名字
    version="0.0.2",  # 版本号
    author="accio",  # 作者
    author_email="xx@example.com",
    description="accio",  # 描述
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://pypi.org/project/accio-api/",  # 可以写github上的地址，或者其他地址

    # 依赖包
    install_requires=[
        'pytest',
        'requests',
    ],
    # project_urls={
    #     "Bug Tracker": "https://github.com/pypa/sampleproject/issues",
    # },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages = setuptools.find_packages('src'),
    package_dir={"": "src"},
    package_data = {
            # 任何包中含有.txt文件，都包含它
            '': ['*.txt'],
            # 包含demo包data文件夹中的 *.dat文件
            # 'demo': ['data/*.dat'],
        },


# include_package_data = True,
    # packages=setuptools.find_packages(exclude=['test', 'examples', 'script', 'tutorials']),  # 包内不需要引用的文件夹
    # packages=setuptools.find_packages(exclude=["Assert.py"]),
    # packages=setuptools.find_packages(where="yttttttttttttttttttttttttttttt"),
    python_requires=">=3.6",
)