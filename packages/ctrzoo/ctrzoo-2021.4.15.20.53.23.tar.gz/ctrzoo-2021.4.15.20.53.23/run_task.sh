#!/usr/bin/env bash
# @Project      : MICTRZOO
# @Time         : 2021/2/8 8:40 下午
# @Author       : yuanjie
# @Email        : yuanjie@xiaomi.com
# @Software     : PyCharm
# @Description  : ${DESCRIPTION}

if [ -n "$1" ]
then TASK=$1
else TASK=./ctrzoo/test.py
fi;
echo "#### RUNNING TASK: ${TASK}"

# common
# pwd: /ml-engine/code/MICTRZOO.git
CLASSPATH=$(${HADOOP_HDFS_HOME}/bin/hadoop classpath --glob)
export PYTHONPATH=$PYTHONPATH:/ml-engine/code/MICTRZOO.git

# HDFS: https://kdc.d.xiaomi.net/
# kinit -k -t ./data/s_feeds.keytab s_feeds@XIAOMI.HADOOP && klist # 默认权限
kinit -k -t ./data/h_browser.keytab h_browser@XIAOMI.HADOOP && klist
# hdfs="/hadoop/zjyprc-hadoop-hadoop-pack-3.1.0-mdh3.1.0.0-SNAPSHOT-20200610/bin/hdfs"
# $hdfs dfs -ls

# PIP
pip install -U -r requirements.txt
pip install -U -i https://pypi.python.org/pypi -r requirements.txt

# RUN
python $TASK

# cloudml jobs_v2 logs kolibre-jobid298626-yuanjie-12477830
