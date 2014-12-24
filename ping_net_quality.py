#! /usr/bin/env python
# -*- coding: UTF-8 -*-
# File: testping_net_quality.py
# Date: 2008-09-24
# Author: Michael Field
# Version: 0.1 Beta

import sys
import os
import getopt
import commands
import re
import time

CNC={
     '219.158.28.121': '中国网通骨干网',
	  '202.108.100.166': '中国网通北京网通',
	  '218.69.33.1': '天津网通',
	  '220.248.112.1': '上海网通',
	  '221.192.1.1': '河北石家庄网通',
	  '218.26.176.1': '山西太原网通',
	  '60.31.195.1': '内蒙古呼和浩特网通',
	  '218.25.255.1': '辽宁大连网通',
	  '221.8.96.1': '吉林长春网通',
	  '218.7.249.154': '黑龙江哈尔滨网通',
	  '218.59.169.109': '山东威海网通',
	  '202.111.148.1': '河南淮阳网通',
	  '58.240.48.43': '江苏南京网通',
	  '60.12.193.1': '浙江湖州网通',
	  '221.3.131.1': '云南昆明网通',
	  '221.10.239.1': '四川成都网通',
	  '221.11.1.1': '陕西西安网通',
	  '221.7.129.163': '广西南宁网通',
	  '58.22.97.1': '福建福州网通',
	  '221.5.196.1': '重庆网通',
	  '221.8.18.8': '长春网通',
	  '202.97.224.68': '黑龙江网通',
	  '202.99.160.1': '河北网通1',
	  '202.96.69.38': '大连网通',
	  '221.10.216.98': '四川网通',
	  '60.210.17.1': '淄博网通',
     '60.209.5.254': '青岛网通',
     '60.12.166.1': '金华网通',
     '58.19.183.1': '襄樊网通',
     '221.208.172.1': '哈尔滨网通',
     '60.31.255.115': '内蒙古网通',
     '202.99.192.68': '山西网通',
     '202.99.160.68': '河北网通2',
     '218.104.32.106': '江苏网通',
     '222.138.109.1': '开封网通',
     '218.107.56.1': '广东网通',
     '210.52.149.2': '湖北网通',
     '60.18.94.1': '辽宁网通',
     }

CTC={
     '61.152.188.1': '上海电信1',
     '61.129.51.254': '上海电信2',
     '218.1.64.33': '上海热线',
     '61.145.125.229': '广东互联星空_广州电信',
     '61.140.60.90': '广东电信',
     '218.18.104.1': '深圳电信 ',
     '218.16.239.129': '汕头电信',
     '218.75.107.60': '浙江互联星空_杭州电信',
     '61.186.95.92': '湖南互联星空_长沙电信',
     '221.236.17.1': '四川互联星空_成都电信',
     '61.139.33.1': '绵阳电信 ',
     '222.176.2.214': '重庆电信',
     '220.179.251.234': '安徽电信',
     '202.102.192.80': '安徽合肥电信',
     '219.148.197.6': '辽宁沈阳电信',
     '219.146.11.20': '山东互联星空_济南电信',
     '58.56.19.129': '山东电信',
     '222.173.123.1': '青岛电信 ',
     '219.148.62.194': '河北石家庄电信',
     '58.53.192.150': '湖北互联星空_湖北电信',
     '218.77.178.229': '海南互联星空_海口电信',
     '219.141.62.111': '贵州互联星空_贵阳电信',
     '61.166.150.110': '云南互联星空_曲靖电信',
     '218.30.85.83': '陕西互联星空_西安电信',
     '218.30.64.121': '北京互联星空_西安电信',
     '61.134.40.138': '陕西渭南 ',
     '60.164.225.1': '甘肃互联星空_甘肃电信',
     '219.159.67.2': '广西互联星空_南宁电信',
     '202.100.128.201': '青海互联星空_西宁电信',
     '202.100.109.157': '宁夏互联星空_石嘴山电信',
     '219.150.150.1': '河南互联星空_郑州电信',
     '221.238.193.1': '天津互联星空_天津电信',
     '202.109.204.150': '福建福州电信',
     '61.131.11.1': '福建泉州 ',
     '220.175.8.1': '江西电信',
     '218.65.103.201': '江西南昌电信',
     '61.186.95.92': '湖南电信',
     '60.190.223.1': '绍兴电信 ',
     '219.150.150.150': '河南电信 ',
     '219.150.32.184': '天津电信  ',
     '61.139.37.1': '南充电信',
     '219.149.194.31': '吉林互联星空_长春电信',
     '219.148.162.4': '内蒙古互联星空_呼和浩特电信',
     '219.147.130.76': '黑龙江互联星空_哈尔滨电信',
     '220.182.54.199': '西藏互联星空_拉萨电信',
     '61.128.101.1': '新疆互联星空_阿克苏电信',
    }

EDU={
     '202.112.128.1': '北京航空航天大学',
     '166.111.8.28': '北京清华大学',
     '202.114.0.242': '湖北武汉华中科技大学',
     '202.117.0.20': '陕西西安交通大学',
     '202.112.26.34': '上海交通大学',
     '202.203.128.33': '云南昆明教育网',
     '202.115.64.33': '四川成都西南交通大学',
     '202.201.48.2': '甘肃兰州西北师范大学',
     '202.116.160.33': '广州华南农业大学',
     }


def usage():
    print "USEAGE:"
    print "\t%s -n CNC|CTC|EDU [-t MINs] [-f file]" %sys.argv[0]
    print "\tCNC 网通线路; CTC 电信线路; EDU 教育网;"
    print "\t-t MINs 测试的时间;默认为10分钟;"
    print "\t-f file 输出结果到文件;默认为当前目录文本文件ping.result"
    print "\t-h|-?, 帮助信息"
    print "for example:"
    print "\t./testping_net_quality.py -n CTC -t 60"
    print "\t在测试网络所在主机上执行以上指令表示测试网络为电信，测试时间1小时;"

def pin(IP):
    xpin=commands.getoutput("ping -c1 %s" %IP)
    ms='time=\d+.\d+'
    mstime=re.search(ms,xpin)
    if not mstime:
        MS='timeout'
        return MS
    else:
        MS=mstime.group().split('=')[1]
        return MS
        
def count(min,ips=None):
    if not ips:
        print "Nothing to pass"
    if ips == 'EDU':
        ips = EDU
    if ips == 'CTC':
        ips = CTC
    if ips == 'CNC':
        ips = CNC    
    nowsecond = int(time.time())
    second = min * 60
    endtime = nowsecond + second
    nums = 0
    timeout = 0
    total_ms = 0
    result={}
    while nowsecond <= endtime:
        for I in ips:
            nums += 1
            MS = pin(I)
            if MS == 'timeout':
                timeout += 1
            else:
                total_ms += float(MS)
            lostpacket = timeout*1.0 / nums
            avgms = total_ms / nums
            result[I]=(ips[I],avgms,lostpacket)
        nowsecond = int(time.time())
    return result
 
if __name__ == '__main__':
    file = 'ping.result'
    mins = 10
    network = ''
    args = sys.argv[1:]
    try:
        (opts, getopts) = getopt.getopt(args, 'n:f:t:h?')
    except:
        print "\nInvalid command line option detected."
        usage()
        sys.exit(1)

    for opt, arg in opts:
        if opt in ('-n'):
            network = arg
        if opt in ('-h', '-?'):
            usage()
            sys.exit(0)
        if opt in ('-f'):
            file = arg
        if opt in ('-t'):
            mins = int(arg)

    if os.path.dirname(file):
        if os.path.exists(os.path.dirname(file)):
            f = open(file, 'w')
        else:
            print "File's path is wrong. please check it."
            usage()
            sys.exit(0)
    else:
        f = open(file, 'w')

    if network not in ['CTC','CNC','EDU'] or not isinstance(mins,int):
        usage()
        sys.exit(0)
    else:
        result = count(mins,network)
        for line in result:
            value = result[line]
            f.write(line + '\t'+ value[0] + '\t'+ str('%.2f'%value[1]) + '\t'+ str('%.2f'%value[2]) + '\n')
        f.close
