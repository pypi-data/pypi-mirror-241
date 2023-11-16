import os
import sys
from pathlib import Path

from pip._internal import main
from setuptools import setup, find_packages


if sys.version_info < (3, 8, 0):
    raise SystemExit("Sorry! AioSpider requires python 3.8.0 or later.")

if sys.version_info > (3, 11, 0):
    raise SystemExit("Sorry! AioSpider requires python 3.11.0 early.")

version = (Path(__file__).parent / 'AioSpider/__version__').read_text()

requires = [
    i for i in (Path(__file__).parent / 'requirements.txt').read_text().split('\n') if i
]

if sys.version_info < (3, 9, 0):
    requires.append('numpy==1.24.4')
    requires.append('pandas==2.0.3')
else:
    requires.append('pandas==2.1.2')

if sys.platform == 'win32':
    requires.append('pycryptodome')
else:
    requires.append('pycrypto')

packages = find_packages()


def get_readme_md():
    with open('README.md', encoding='utf-8') as f:
        return f.read()


setup(
    name='AioSpider-zly',       # 包名
    version=version,            # 版本号
    description='高并发异步爬虫框架',
    long_description=get_readme_md(),
    long_description_content_type="text/markdown",
    author='zly717216',
    author_email='zly717216@qq.com',
    url='https://github.com/zly717216/AioSpider',
    maintainer='zly',
    license="MIT",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords=[
        "异步网页抓取", "网络爬虫", "异步爬虫", "Python 异步抓取", "数据提取", "网络数据挖掘", "异步爬虫框架",
        "网络爬取工具", "数据采集", "数据挖掘工具"
    ],
    packages=packages,
    install_requires=requires,
    entry_points={
        'console_scripts': [
            'aioSpider = AioSpider.aioSpider:main'
        ]
    },
    zip_safe=False,
    include_package_data=True,
    python_requires='>=3.7',
)

# python setup.py clean --all
# python setup.py sdist
# python setup.py install
# python setup.py bdist_wheel
# twine upload dist/AioSpider-1.9.0.tar.gz
