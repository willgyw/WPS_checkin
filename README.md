#### 我的wps会员 小程序签到

![68747470733a2f2f692e6c6f6c692e6e65742f323031392f30392f32332f4c657875343776556b794b484667452e706e67.png](https://i.loli.net/2020/05/28/LUhpf2FuoEByw59.png)

【我的wps会员】小程序自动签到，除了签到还可以邀请和接受邀请。每天最少可以获得11天会员。

需要用`sid`登录，可以登录[http://zt.wps.cn](http://zt.wps.cn/)，查看cookie里的sid获取

将sid填入`data.json`中的`wps_checkin[sid]`字段。

邀请用户签到可以额外获得会员，每日可邀请最多10个用户，main.py已预置了13个小号用于接受邀请，但需要主账号的invite_userid,invite_userid的获取可以在网页端发出邀请，然后查看邀请url里的sid，类似`191641526`。
将invite_userid填入`data.json`中的`wps_invite[invite_userid]`字段。



#### 如何使用
> 本项目使用python3实现

1. 安装依赖
```
pip install requests 
```
2. 填写`data.json`，json里是登录所需要的一些账号信息。
3. 执行`python main.py`

#### 自动签到
Linux 自动签到参考[crontab](http://www.runoob.com/w3cnote/linux-crontab-tasks.html)

Windows 自动签到可以使用任务计划程序。



