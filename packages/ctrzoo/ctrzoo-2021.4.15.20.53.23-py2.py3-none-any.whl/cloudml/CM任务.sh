#!/usr/bin/env bash
# @Project      : MICTRZOO
# @Time         : 2021/3/10 8:30 下午
# @Author       : yuanjie
# @Email        : yuanjie@xiaomi.com
# @Software     : PyCharm
# @Description  : https://cloud.d.xiaomi.net/product/docs/cloudml/usage/request_quota_v2#/?_k=ao1jw2
# 定时quota


#cloudml quota_v2 update -p guaranteed \
#-e yuanjie@xiaomi.com \
#-c 32 -M 100 \
#-cs '0 15 * * *' -ce '0 23 * * *' \
#-gt v100-32g -gc 1
##-gt p4-8g -gc 1 -gc 2



cloudml quota_v2 update -p guaranteed \
-e yuanjie@xiaomi.com \
-c 100 -M 128 \
-gt v100-32g -gc 3

#cloudml quota_v2 list


# 作业日志
cloudml jobs_v2 list | grep yuanjie | tail -n 3
cloudml jobs_v2 logs kolibre-jobid306299-yuanjie-13556050
cloudml jobs_v2 desc kolibre-jobid306299-yuanjie-13556050 | grep "Monitoring url"

# 开发环境镜像保存
cloudml dev save_v2 -f me me
cloudml env describe me
