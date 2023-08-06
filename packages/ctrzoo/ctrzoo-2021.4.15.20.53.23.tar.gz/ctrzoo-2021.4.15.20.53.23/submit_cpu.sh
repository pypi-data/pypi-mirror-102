#!/usr/bin/env bash
DATA=`date +'%Y%m%d-%H-%M-%S'`

if [ -n "$2" ]
then taget_name=$2
else taget_name="tql$DATA"
fi;


project_name=$1 # 主程序命名项目名
#if cloudml jobs delete $project_name | grep "Successfully";
#then echo "删除 ..." && sleep 18s;
#fi;
#   --priority_class {guaranteed,preferred,best-effort}
cloudml jobs submit \
-n $taget_name \
-m $project_name \
-u ./ \
-c 7 -M 22G \
-d cr.d.xiaomi.net/cloud-ml/devsave:33103-me \
-hka h_browser@XIAOMI.HADOOP -hkt tql -he hdfs://zjyprc-hadoop \
--priority_class guaranteed \
-cst '0 15 * * *' -ce '0 23 * * *' \
-g 1 # -gt v100 -gm 32g

#-pc "pip install -U --no-cache-dir -i https://pypi.python.org/pypi meutils bertzoo"


rm -rf ./build/ ./*.egg-info/ ./dist/ *checkpoints*;
mv ./*.yaml ./checkpoints
# cloudml jobs list
