# CM作业

2021-02-08T12:18:10.421171061Z INFO:root:Try to run fdsfuse command: fdsfuse browser-algo-nanjing /fds -o use_cache=/fdscache
2021-02-08T12:18:11.959872154Z fuse: failed to exec fusermount: No such file or directory
2021-02-08T12:18:11.962419335Z INFO:root:Try to run keytab init command: echo XAQAkfddMQENb3r|kinit s_feeds@XIAOMI.HADOOP
2021-02-08T12:18:11.971625200Z Password for s_feeds@XIAOMI.HADOOP:
2021-02-08T12:18:12.211847901Z rev-8e425f3d5832b20fa785f5c5765a9d149eca6257



从yaml读取配置 cloudml jobs submit -f FILENAME


# 保存dev镜像
```
cloudml dev list
cloudml dev save_v2 -f me me
cloudml env describe me # cr.d.xiaomi.net/cloud-ml/devsave:33103-me
```

# 监控任务
Monitoring url:  http://falcon.srv/#/dashboard/charts?id=91802062&graph_type=h&cf=AVERAGE&start=1614329430&end=1614333030
Billing url:     https://grafana-c5-cloudml-xiaomi.dun.mi.com/d/mvuNcKcMz/cloudml_billing?orgId=1&var-namespace=ns-33103&var-task_type=TrainJob&var-job_name=kolibre-jobid298626-yuanjie-12578619
```
kolibre-jobid{作业id}-yuanjie*

cloudml jobs_v2 describe kolibre-jobid298626-yuanjie-12581646


```

蜂鸟迁移
https://xiaomi.f.mioffice.cn/docs/dock4KX4Rlr4baZLxnqYhyMhPxc
