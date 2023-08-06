#!/usr/bin/env bash
# @Project      : MICTRZOO
# @Time         : 2021/2/8 7:27 下午
# @Author       : yuanjie
# @Email        : yuanjie@xiaomi.com
# @Software     : PyCharm
# @Description  : 字符串http://c.biancheng.net/view/1120.html

# c5__cloudml_cluster

# 变量
project_name="mictrzoo"
secret_name="mictrzoo"
repo="git@git.n.xiaomi.com:yuanjie/MICTRZOO.git"
#s1=${repo##*/}
#secret_name=${s1%.git}

# 创建项目
cloudml project create -n $project_name

# 创建git-secret
cloudml git-secret list
#cloudml git-secret create -n $secret_name -ssh ~/.ssh/id_rsa -kh /tmp/known_hosts # linux
cloudml git-secret create -n $secret_name -ssh ~/.ssh/id_rsa -kh ~/.ssh/known_hosts # mac

# project 关联 git-secret
cloudml project update -cu $repo -ck $secret_name $project_name
