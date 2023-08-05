#!/usr/bin/env bash
# @Project      : AppZoo
# @Time         : 2021/2/23 8:31 下午
# @Author       : yuanjie
# @Email        : yuanjie@xiaomi.com
# @Software     : PyCharm
# @Description  : ${DESCRIPTION}


docker commit  -a 'yuanjie' -m 'ann' {ContainerID} cr.d.xiaomi.net/yuanjie/{ImageName}
docker push cr.d.xiaomi.net/yuanjie/{ImageName}