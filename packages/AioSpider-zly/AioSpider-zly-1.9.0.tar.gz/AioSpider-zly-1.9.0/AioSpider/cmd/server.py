import os
import subprocess
from pathlib import Path

import requests
from tqdm import tqdm

from AioSpider.tools.file_tools import (
    decompress_zip, move, delete_files, rename
)
from AioSpider.tools.program_tools import (
    get_ipv4, start_cmd, close_program_by_port, server_running
)
from AioSpider import settings
from AioSpider.cmd.cmd import AioSpiderCommand, CommandName
from AioSpider.cmd.args import AioSpiderArgs, ArgsP, ArgsH
from AioSpider.cmd.options import AioSpiderOptions


INSTALL_URL = 'http://101.42.138.122:9004/media/resource-master.zip'
RESOURCE_ZIP_PATH = Path(__file__).parent.parent / 'resource.zip'
RESOURCE_PATH = Path(__file__).parent.parent / 'resource'
REDIS_PATH = Path(__file__).parent.parent / 'resource' / 'Redis-x64'


class ServerCommand(AioSpiderCommand):

    def execute(self):

        if self.command_name.name == 'start':
            self.start_server()
        elif self.command_name.name == 'stop':
            self.stop_server()
        else:
            raise Exception(f'command error, AioSpider server 没有该参数，AioSpider {ArgsH()} 查看帮助')

    def start_server(self):
        """
        启动节点服务器   aioSpider server run -h 0.0.0.0 -p 10086
        """

        cwd = Path.cwd()

        port = None
        host = None

        for arg in self.args:
            if isinstance(arg, ArgsH):
                host = arg.name
            if isinstance(arg, ArgsP):
                port = arg.name
                
        if port is None:
            port = settings.ServerConfig.slaver['port']
            
        if host is None:
            host = settings.ServerConfig.slaver['host']

        os.chdir(Path(__file__).parent.parent / 'server')
        pid = start_cmd(f'uvicorn main:app --host {host} --port {port}', close=True)
        os.chdir(cwd)

        print(f'{host}:{port} 启动成功：IPV4: {get_ipv4()}')
        
    def stop_server(self):
        """
        关闭节点服务器   aioSpider server stop -p 10086
        """

        port = None

        for arg in self.args:
            if isinstance(arg, ArgsP):
                port = arg.name

        if port is None:
            port = settings.ServerConfig.slaver['port']

        close_program_by_port(port)
        print(f'{get_ipv4()}服务器关闭成功')

    def add_name(self, name: CommandName):
        self.command_name = name

    def add_args(self, args: AioSpiderArgs):
        self.args.append(args)

    def add_options(self, option: AioSpiderOptions):
        self.options.append(option)
        
        
class RedisCommand(AioSpiderCommand):

    def execute(self):

        if self.command_name.name == 'start':
            self.start_redis()
        elif self.command_name.name == 'stop':
            self.stop_redis()
        else:
            raise Exception(f'command error, AioSpider server 没有该参数，AioSpider {ArgsH()} 查看帮助')

    def start_redis(self):
        """
        启动redis服务器   aioSpider redis run
        """

        redis_path = REDIS_PATH / 'redis-server.exe'
        if not redis_path.exists():
            raise SystemError('找不到 redis 服务器')

        if not server_running(port=6379):
            process = subprocess.Popen(
                redis_path, stdout=subprocess.PIPE, stderr=subprocess.PIPE
            )

        print('redis 服务启动成功：127.0.0.1:6379')
        
    def stop_redis(self):
        """
        关闭redis服务器   aioSpider server stop -p 10086
        """

        port = None

        for arg in self.args:
            if isinstance(arg, ArgsP):
                port = arg.name

        if port is None:
            port = 6379

        close_program_by_port(port)
        print('reids服务器关闭成功')

    def add_name(self, name: CommandName):
        self.command_name = name

    def add_args(self, args: AioSpiderArgs):
        self.args.append(args)

    def add_options(self, option: AioSpiderOptions):
        self.options.append(option)


class InstallCommand(AioSpiderCommand):

    def execute(self):
        self.install()

    def install(self):
        """
        下载浏览器 aioSpider install
        """

        try:
            res = requests.get(INSTALL_URL, stream=True)
        except Exception as e:
            print(f'下载失败，原因：{e}')
            return

        # 获取文件总大小
        total_size = int(res.headers.get('content-length', 0))

        with RESOURCE_ZIP_PATH.open('wb') as f, tqdm(
                desc="下载进度",
                total=total_size,
                unit="B",
                unit_scale=True,
                unit_divisor=1024,
        ) as progress_bar:
            for chunk in res.iter_content(chunk_size=1024 * 4):
                f.write(chunk)
                progress_bar.update(len(chunk))

        decompress_zip(RESOURCE_ZIP_PATH, RESOURCE_PATH)
        move(RESOURCE_PATH / 'resource-master', RESOURCE_PATH.parent)
        delete_files(RESOURCE_PATH)
        rename(RESOURCE_PATH.parent / 'resource-master', RESOURCE_PATH.parent / 'resource')

        print('AioSpider 浏览器适配成功成功')

    def add_name(self, name: CommandName):
        self.command_name = name

    def add_args(self, args: AioSpiderArgs):
        self.args.append(args)

    def add_options(self, option: AioSpiderOptions):
        self.options.append(option)
