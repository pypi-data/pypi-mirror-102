#!/usr/bin/env bash
# @Project      : MICTRZOO
# @Time         : 2021/2/4 6:37 下午
# @Author       : yuanjie
# @Email        : yuanjie@xiaomi.com
# @Software     : PyCharm
# @Description  : ${DESCRIPTION}

# 分布式：https://cloud.d.xiaomi.net/product/docs/cloudml/trainjob/0512_trainjob_v2
cloudml -k owner jobs_v2 submit -n test -m trainer.task -u fds://wukong/test.tar.gz -p test \
-F tensorflow \
--cluster_spec='{"ps":{"count": 1, "memeory_limit": "1G"}, "worker": {"count": 1, "memory_limit": "1G"}}'

