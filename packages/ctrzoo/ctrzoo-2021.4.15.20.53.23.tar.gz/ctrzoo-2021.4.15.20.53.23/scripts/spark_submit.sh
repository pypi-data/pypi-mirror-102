#!/usr/bin/env bash
# @Project      : MICTRZOO
# @Time         : 2021/3/22 6:03 下午
# @Author       : yuanjie
# @Email        : yuanjie@xiaomi.com
# @Software     : PyCharm
# @Description  : ${DESCRIPTION}
class=com.xiaomi.data.recommender.dnnctr.DnnTFRecordSamplesPushMitv
jar=hdfs://zjyprc-hadoop/user/s_feeds/yuanjie/deep-learning-pipeline-0.1-SNAPSHOT.jar
#start_day="2017-11-15"
start_day=`date -d '-1 day' +%Y-%m-%d`
if [[ $# -gt 0 ]]; then
    start_day=$1; shift
fi
echo "开始日期：$start_day"
INFRA_CLIENT_HOME=/home/work/tools/infra-client
$INFRA_CLIENT_HOME/bin/spark-submit \
    --cluster zjyprc-hadoop \
    --class "$class" \
    --master "yarn-cluster" \
    --queue "root.production.cloud_group.feeds.pipeline" \
    --conf spark.yarn.job.owners=yuanjie \
    --conf spark.yarn.executor.memoryOverhead=4096 \
    --conf spark.speculation=true \
    --num-executors 800 \
    --driver-memory 8g \
    $jar \
    -startDay=$start_day \
    -days=1 \
    -input=/user/s_feeds/dev/user_growth/push/dnn/mitv/impression \
    -output=/user/h_data_platform/platform/push/mipush/data/mitvpush/v0 \
    -dir=hdfs://zjyprc-hadoop/user/h_data_platform/platform/push/mipush/data/mitvpush/v0_requirements \
    -featureGroupSize=37 \
    -sampleRatio=1
