# ---encoding:utf-8---
# @Time    : 2023/7/8 01:35
# @Author  : caishengxiang
# @Email   : 383301857@qq.com
# @File    : pssh_tool.py
# @Project : caishengxiang
"""

pip install parallel-ssh
"""
import logging

try:
    from pssh.clients import ParallelSSHClient
except Exception as e:
    print('you need pip install parallel-ssh, {}'.format(e))


def run_command(hosts, user, password, cmd, timeout=0, if_raise=False):
    client = ParallelSSHClient(hosts, user=user, password=password, timeout=timeout)
    output = client.run_command(cmd)
    client.pool.join()  # 等执行完
    for host_output in output:
        print("========== results of cmd:【{}】 in host:【{}】 =============".format(cmd, host_output.host))
        for line in host_output.stdout:
            print(line)

        exit_code = host_output.exit_code

        if exit_code != 0:
            errs = ""
            for err in host_output.stderr:
                errs += err
            print("\033[0;31;40m", '【{}】| {}'.format(host_output.host, errs), "\033[0m")
            # logging.error('【{}】| {}'.format(host_output.host, errs))
            if if_raise:
                raise Exception('【{}】| {}'.format(host_output.host, errs))


    del client


def run_commands(hosts, user, password, cmds, timeout=0, if_raise=False):
    for cmd in cmds:
        run_command(hosts=hosts, user=user, password=password, cmd=cmd, timeout=timeout, if_raise=if_raise)


if __name__ == '__main__':
    # run_command(hosts=["175.178.172.183"], user='ubuntu', password='xxxx', cmd='ls -a')
    # run_command(hosts=["175.178.172.183"], user='ubuntu', password='xxxx', cmd='rm ./xxxx')
    # run_command(hosts=["175.178.172.183"], user='ubuntu', password='xxxx', cmd='rm ./xxxx', if_raise=True)

    run_commands(hosts=["192.168.0.111"], user='csx', password='Orange_123',
                 cmds=['ls', 'ls'])
