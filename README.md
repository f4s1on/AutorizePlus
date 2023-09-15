# AutorizePlus
使用该插件时，推荐本地jdk环境使用Openjdk，否则在使用pkcs7的填充方式时会产生错误

原项目：https://github.com/Quitten/Autorize

原插件Autorize的功能已经比较完善，可以满足明文场景下的越权测试需求，但是针对加密场景下每个用户加密密钥不同的情况并不使用，所以在原插件基础上进行了扩展

使用方法：

勾选Auto Decrypt、填入低权限用户会话、过滤器添加 Scope items only (Scope items限制的是仅查看指定域名的流量，在proxy中配置)

![image](https://github.com/f4s1on/AutorizePlus/assets/57355558/4e756feb-ed6e-44ac-a953-35e1df7f83b2)


选择好网站的加密方法，这里以3des/cbc/pkcs7为例，分别填入高低权限的key和iv(Secret1和iv1是高权限用户的key和iv，Secret2和iv2是低权限用户的key和iv)

设置好请求包和响应包密文的匹配正则，点击Add filter，

然后点击 Autorize is off开启插件

![image](https://github.com/f4s1on/AutorizePlus/assets/57355558/f1c37935-ac63-4958-89bc-623bf26eb4bd)


先看看原始的请求和响应包

![image](https://github.com/f4s1on/AutorizePlus/assets/57355558/cf7b0395-6206-4c6c-847f-dbff7b9fb38f)

在越权插件中看到的请求和响应都是明文，而且对越权的判断正常

![image](https://github.com/f4s1on/AutorizePlus/assets/57355558/f2b79e93-c1b3-4b41-8d0f-d47e6c5e9cdb)
![image](https://github.com/f4s1on/AutorizePlus/assets/57355558/87e44481-2ce4-4b9f-86f3-207bf340ecd5)

