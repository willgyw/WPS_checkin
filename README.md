#### wps小程序签到送vip会员
需要用`sid`登录，可以登录[http://zt.wps.cn](http://zt.wps.cn)，查看cookie里的sid获取

邀请用户签到可以额外获得会员，每日最多10个用户，可以申请多个小号，或是用朋友的sid，模拟接受邀请，但需要主账号的invite_userid,可以在网页端发出邀请，然后查看邀请url里的sid，类似`191641526`。

#### 有道云笔记签到
签到领空间，使用cookie里的YNOTE_SESS签到，但过几天就会失效，所以也增加了用户名密码签到，然后更新YNOTE_SESS，密码使用了MD5加密。

