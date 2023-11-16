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

require = '''
aiocsv==1.2.4
aiofiles==23.2.1
aiohttp==3.8.6
aiomysql==0.2.0
aioredis==2.0.1
aiosqlite==0.19.0
motor==3.3.1
beautifulsoup4==4.12.2
bitarray==2.8.2
chardet==3.0.4
cchardet==2.1.7
ddddocr==1.4.8
loguru==0.7.2
lxml==4.9.3
pydash==7.0.6
opencv-python==4.8.1.78
pillow==9.5.0
openpyxl==3.1.2
pycryptodome==3.19.0
PyExecJS==1.5.1
pymongo==4.5.0
pymysql==1.1.0
redis==5.0.1
requests==2.31.0
rsa==4.9
selenium==4.14.0
playwright==1.39.0
tabula-py==2.8.2
tqdm==4.66.1
w3lib==2.1.2
dataframe_image==0.2.2
'''

requires = [
    i for i in require.split('\n') if i
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
