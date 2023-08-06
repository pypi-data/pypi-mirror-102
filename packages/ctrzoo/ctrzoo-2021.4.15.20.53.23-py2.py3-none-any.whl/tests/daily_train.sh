#!/usr/bin/env bash
# @Project      : MICTRZOO
# @Time         : 2021/2/19 3:21 下午
# @Author       : yuanjie
# @Email        : yuanjie@xiaomi.com
# @Software     : PyCharmdaily_train_mitv_base_days.sh
# @Description  : ${DESCRIPTION}
# TODO: 用python重写脚本

/home/work/inf/infra-client/bin/hdfs dfs -rm /user/h_data_platform/platform/push/mipush/data/mitvpush/v0_requirements/model/checkpoint_batch/_TRAINING
source scripts/config.sh

eval_day=${1:-$YESTERDAY}

end_day=${2:-$LAST2DAY}

days_num=${3:-21}
config_path="/home/work/yuanjie/zk2file/push_mitv_v0_train.yaml"

train_day="null"

tf_record_trainSample="hdfs://zjyprc-hadoop/user/h_data_platform/platform/push/mipush/data/mitvpush/v0"
cur_path="/user/h_data_platform/platform/push/mipush/data/mitvpush/v0"
for ((i=0; i<$days_num; i+=1))
do
    #echo $i
    cur_day=`date -d"$end_day $i days ago" +"%Y%m%d"`
    filepath=$cur_path"/date="$cur_day
    if $ZJYHDFS_TEST_EXIST "$filepath";
    then
        #continue
        sleep 1s
    else
        continue
    fi
    if [ $train_day == "null" ]; then
        train_day=$cur_day
    else
        train_day=$train_day","$cur_day
    fi
done

echo $eval_day $train_day

waitZjyHdfsReady ${tf_record_trainSample}/date=$eval_day 1 &&
echo 'begin training'
python scripts/daily_train.py --config_path $config_path --train_day $train_day --test_day $eval_day
echo " traning finish"

export_model_base="hdfs://zjyprc-hadoop/user/h_data_platform/platform/push/mipush/data/mitvpush/v0_requirements/export"
export_model_path=$export_model_base/date=${eval_day}
echo " export_model_path: "$export_model_path


online_model="/user/s_feeds/yuanjie/mitv/online_model"
waitZjyHdfsReady ${export_model_path} 1 &&
zjyhdfs -rm ${online_model}/id_map_*
zjyhdfs -rm ${online_model}/layers
zjyhdfs -rm ${online_model}/embedding_group
zjyhdfs -rm ${online_model}/_SUCCESS
zjyhdfs -cp ${export_model_path}/id_map_* ${online_model}
zjyhdfs -cp ${export_model_path}/layers ${online_model}
zjyhdfs -cp ${export_model_path}/embedding_group ${online_model}
zjyhdfs -cp ${export_model_path}/_SUCCESS ${online_model}
# 强制删除TRAINING
#/home/work/inf/infra-client/bin/dfs -rm /user/s_feeds/wangxuntao/online/DNN/mitv/model/base/checkpoint_batch/_TRAINING
echo "final success"
