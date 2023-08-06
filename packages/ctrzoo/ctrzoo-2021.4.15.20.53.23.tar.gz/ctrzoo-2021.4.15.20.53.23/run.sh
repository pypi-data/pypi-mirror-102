#!/usr/bin/env bash
# @Project      : MICTRZOO
# @Time         : 2021/2/8 8:40 下午
# @Author       : yuanjie
# @Email        : yuanjie@xiaomi.com
# @Software     : PyCharm
# @Description  : ${DESCRIPTION}


# 需放到命令行里
CLASSPATH=$(${HADOOP_HDFS_HOME}/bin/hadoop classpath --glob)
export PYTHONPATH=$PYTHONPATH:/ml-engine/code/MICTRZOO.git

# HDFS: https://kdc.d.xiaomi.net/
kinit -k -t ./data/s_feeds.keytab s_feeds@XIAOMI.HADOOP && klist # 默认权限
kinit -k -t ./data/h_browser.keytab h_browser@XIAOMI.HADOOP && klist


# PIP
pip install -U -r requirements.txt
pip install -U -i https://pypi.python.org/pypi -r requirements.txt
