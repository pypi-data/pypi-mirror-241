# -*-coding:utf-8-*-
"""
pip install paramiko
pip install pyecharts

如需监控网络 服务器：
sudo yum install epel-release
sudo yum install nload
"""
import time
import logging
import os
import datetime
import re
import pathlib
from concurrent.futures import ThreadPoolExecutor

try:
    import paramiko
except:
    raise Exception('you need: pip install paramiko')

from caishengxiang.utils.draw_tools.echarts_draw import Draw
from pyecharts.charts import Page


def exec_ssh_command(hostname, username, password, cmd='top -bn 1'):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=hostname, username=username, password=password)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    output = stdout.read()
    content = output.decode()
    ssh.close()
    return content


class Monitor:
    def __init__(self, hostname, username, password, save_dir="./monitors"):
        self.hostname = hostname
        self.username = username
        self.password = password
        self.save_dir = os.path.abspath(save_dir)
        pathlib.Path(self.save_dir).mkdir(parents=True, exist_ok=True)
        self.monitor_map = dict()
        self.page = Page()
        self.thread_pool = ThreadPoolExecutor(max_workers=10)

    def _exec_ssh_command(self, command: str = 'top -bn 1'):
        return exec_ssh_command(self.hostname, self.username, self.password, command)

    def default_time_handle(self):
        return str(datetime.datetime.now())

    def default_content_handle(self, content: str):
        content = content.strip()
        return float(content)

    def add_monitor(self, command, content_handle=None, time_handle=None, y_name='使用率%',
                    x_name='时间', title='cpu监控'):
        if self.monitor_map.get(title):
            raise Exception('已经存在同名监控:{}'.format(title))
        self.monitor_map[title] = {
            'command': command,
            'content_handle': content_handle if content_handle else self.default_content_handle,
            'time_handle': time_handle if time_handle else self.default_time_handle,
            'draw': Draw(y_name=y_name, x_name=x_name,
                         title='{hostname}:{title}'.format(hostname=self.hostname, title=title),
                         save_path=os.path.join(self.save_dir,
                                                '{hostname}_{title}.html'.format(hostname=self.hostname, title=title)))
        }

    def _look(self, command, draw, content_handle, time_handle):
        try:
            content = self._exec_ssh_command(command)
            y_data = content_handle(content)
            x_data = time_handle()
            draw.add_data(x_data=x_data, y_data=y_data)
            draw.save()
        except Exception as e:
            logging.error('command:{} error:{}'.format(command, e))

    def looks(self):
        for title, monitor_dict in self.monitor_map.items():
            command = monitor_dict['command']
            content_handle = monitor_dict['content_handle']
            time_handle = monitor_dict['time_handle']
            draw = monitor_dict['draw']
            self.thread_pool.submit(self._look, command, draw, content_handle, time_handle)

    def end(self):
        for title, monitor_dict in self.monitor_map.items():
            draw = monitor_dict['draw']
            self.page.add(draw.draw())
        self.page.render(os.path.join(self.save_dir, '{}_总监控.html'.format(self.hostname)))

    def start_server(self, host='0.0.0.0', port=8888):
        """启动监控web服务"""
        pass

if __name__ == '__main__':
    def top_cpu_usage(content):
        """
        return 使用率(%)
        """
        lines = content.split('\n')
        cpu_line = [x for x in lines if 'Cpu(s)' in x][0]
        cpu_strs = cpu_line.split(':')[1].split(',')
        cpu_id_str = cpu_strs[3].strip()
        cpu_id = float(cpu_id_str.split()[0])
        usage = 100 - cpu_id
        return round(usage, 2)


    def top_memory_usage(content):
        """
        return 字节
        """
        lines = content.split('\n')
        mem_line = [x for x in lines if x.startswith('KiB Mem')][0]
        mem_infos = mem_line.split(',')
        used = [x for x in mem_infos if 'used' in x][0]
        used = used.split()[0]
        # return int(used) # 字节
        return round(used / 1024, 2)  # MiB
        # return round(used / (1024 * 1024), 2) # GiB


    # from pyecharts.globals import CurrentConfig, OnlineHostType
    #
    # dir_path = os.path.dirname(__file__)
    # assets_path = os.path.join(dir_path, 'assets')
    # CurrentConfig.ONLINE_HOST = assets_path + '/'

    monitor1 = Monitor(hostname='192.168.0.111', username='csx', password='Orange_123', save_dir="D:\\tmp\\monitor")
    monitor1.add_monitor(command="free -m | sed -n '2p'|awk '{print $3/$2*100}'", y_name='内存使用率%', title='内存监控')
    monitor1.add_monitor(command="top -bn 1", content_handle=top_cpu_usage, y_name='cpu使用率%', title='cpu监控')

    monitor2 = Monitor(hostname='192.168.0.112', username='csx', password='Orange_123', save_dir="D:\\tmp\\monitor")
    monitor2.add_monitor(command="free -m | sed -n '2p'|awk '{print $3/$2*100}'", y_name='内存使用率%', title='内存监控')
    monitor2.add_monitor(command="top -bn 1", content_handle=top_cpu_usage, y_name='cpu使用率%', title='cpu监控')

    monitor3 = Monitor(hostname='192.168.0.108', username='csx', password='Orange_123', save_dir="D:\\tmp\\monitor")
    monitor3.add_monitor(command="free -m | sed -n '2p'|awk '{print $3/$2*100}'", y_name='内存使用率%', title='内存监控')
    monitor3.add_monitor(command="top -bn 1", content_handle=top_cpu_usage, y_name='cpu使用率%', title='cpu监控')

    look_time = 100  # 秒
    for i in range(look_time):
        monitor1.looks()
        monitor2.looks()
        monitor3.looks()
        time.sleep(0.1)
    monitor1.end()
    monitor2.end()
    monitor3.end()
