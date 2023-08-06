#!/usr/bin/env bash

train_day='20210313'
eval_day='20210314'
config_path="/home/work/yuanjie/zk2file/push_mitv_v0_train.yaml"
zjyhdfs="/home/work/inf/infra-client/bin/hdfs dfs"
$zjyhdfs -rm /user/h_data_platform/platform/push/mipush/data/mitvpush/v0_requirements/model/checkpoint_batch/_TRAINING


# train
echo 'begin training'
python scripts/daily_train.py --config_path $config_path --train_day $train_day --test_day $eval_day
echo " traning finish"

# export
export_model_base="hdfs://zjyprc-hadoop/user/h_data_platform/platform/push/mipush/data/mitvpush/v0_requirements/export"
export_model_path=$export_model_base/date=${eval_day}
echo " export_model_path: "$export_model_path

# replace
online_model="/user/s_feeds/yuanjie/mitv/online_model"
#waitZjyHdfsReady ${export_model_path} 1 &&
$zjyhdfs -rm ${online_model}/id_map_*
$zjyhdfs -rm ${online_model}/layers
$zjyhdfs -rm ${online_model}/embedding_group
$zjyhdfs -rm ${online_model}/_SUCCESS
$zjyhdfs -cp ${export_model_path}/id_map_* ${online_model}
$zjyhdfs -cp ${export_model_path}/layers ${online_model}
$zjyhdfs -cp ${export_model_path}/embedding_group ${online_model}
$zjyhdfs -cp ${export_model_path}/_SUCCESS ${online_model}
echo "final success"
