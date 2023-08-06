#!/usr/bin/env bash
# @Project      : sparse-zoo
# @Time         : 2021/3/29 5:00 下午
# @Author       : yuanjie
# @Email        : yuanjie@xiaomi.com
# @Software     : PyCharm
# @Description  :
# git pull origin yuanjie
# sh conf/mivideo_push/train.sh

train_day="20210327"

eval_day='20210328'

#cd ~/yuanjie/sparse-zoo
config_path="conf/mivideo_push/dnn_v1.yml"

# 强行删除training flag
#/home/work/inf/infra-client/bin/hdfs dfs -rm /user/h_data_platform/platform/push/mipush/data/mitvpush/v1_requirements/model/checkpoint_batch/_TRAIN*

# train
echo 'begin training'
python scripts/daily_train.py --config_path $config_path --train_day $train_day --test_day $eval_day
echo " traning finish"

# export
#export_model_base="hdfs://zjyprc-hadoop/user/h_data_platform/platform/push/mipush/data/mitvpush/v0_requirements/export"
#export_model_path=$export_model_base/date=${eval_day}
#echo " export_model_path: "$export_model_path

# replace
#online_model="/user/s_feeds/yuanjie/mitv/v0_online_model"
#waitZjyHdfsReady ${export_model_path} 1 &&
#zjyhdfs -rm ${online_model}/id_map_*
#zjyhdfs -rm ${online_model}/layers
#zjyhdfs -rm ${online_model}/embedding_group
#zjyhdfs -rm ${online_model}/_SUCCESS
#zjyhdfs -cp ${export_model_path}/id_map_* ${online_model}
#zjyhdfs -cp ${export_model_path}/layers ${online_model}
#zjyhdfs -cp ${export_model_path}/embedding_group ${online_model}
#zjyhdfs -cp ${export_model_path}/_SUCCESS ${online_model}
#echo "final success"