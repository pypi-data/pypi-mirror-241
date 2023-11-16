# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src\\plugins'}

packages = \
['hikari_bot_official', 'hikari_bot_official.game']

package_data = \
{'': ['*']}

install_requires = \
['Jinja2>=3.0.0,<4.0.0',
 'beautifulsoup4>=4.11.1,<5.0.0',
 'hikari-core>=1.0.0,<2.0.0',
 'httpx[http2]>=0.24.0',
 'nonebot-adapter-qq>=1.1.0,<2.0.0',
 'nonebot-plugin-apscheduler>=0.2.0,<0.3.0',
 'nonebot2[fastapi,httpx,websockets]>=2.1.0,<3.0.0',
 'orjson>=3.8.11,<4.0.0',
 'oss2>=2.18.3,<3.0.0']

setup_kwargs = {
    'name': 'hikari-bot-official',
    'version': '0.1.6',
    'description': 'Nonebot2 HikariBot For QQ-Official,支持战舰世界水表查询',
    'long_description': '<!-- markdownlint-disable MD033 MD041 -->\n<p align="center">\n  <a href="https://github.com/benx1n/HikariBot"><img src="https://s2.loli.net/2022/05/28/SFsER8m6TL7jwJ2.png" alt="Hikari " style="width:200px; height:200px" ></a>\n</p>\n\n<div align="center">\n\n# Hikari\n\n<!-- prettier-ignore-start -->\n<!-- markdownlint-disable-next-line MD036 -->\n战舰世界水表BOT\n<!-- prettier-ignore-end -->\n\n<p align="center">\n  <a href="https://pypi.python.org/pypi/hikari-bot">\n    <img src="https://img.shields.io/pypi/v/hikari-bot" alt="pypi">\n  </a>\n  <img src="https://img.shields.io/badge/python-3.8.0+-blue" alt="python">\n  <a href="http://hits.dwyl.com/benx1n/HikariBot">\n    <img src="https://hits.dwyl.com/benx1n/HikariBot.svg?style=flat-square" alt="hits">\n  </a>\n  <a href="https://github.com/benx1n/HikariBot/stargazers"><img src="https://img.shields.io/github/stars/benx1n/HikariBot" alt="GitHub stars"style="max-width: 100%;">\n  </a>\n  <br/>\n  <a href="https://jq.qq.com/?_wv=1027&k=S2WcTKi5">\n    <img src="https://img.shields.io/badge/QQ%E7%BE%A4-967546463-orange?style=flat-square" alt="QQ Chat Group">\n  </a>\n  <a href="https://qun.qq.com/qqweb/qunpro/share?_wv=3&_wwv=128&appChannel=share&inviteCode=1W4NX2S&from=181074&biz=ka#/pc">\n    <img src="https://img.shields.io/badge/QQ%E9%A2%91%E9%81%93-yuyuko助手-5492ff?style=flat-square" alt="QQ Channel">\n  </a>\n\n# 💘您不打算给可爱的Hikari点个Star吗QAQ\n</p>\n</div>\n\n## 简介\n\n战舰世界水表BOT，基于Nonebot2，适配QQ官方机器人\n水表人，出击！wws me recent！！！  \n\n\n## 特色\n\n- [x] 账号总体、单船、近期战绩\n- [x] 全指令支持参数乱序\n- [x] 快速切换绑定账号\n- [x] 实时推送对局信息\n- [x] 支持@快速查询\n- [x] 全异步，高并发下性能更优\n- [x] 适配官方BOT\n\n  <details>\n  <summary>点我查看功能列表</summary>\n\n  - 绑定账号：wws bind/set/绑定 [服务器+游戏昵称]：\n  - 查询账号绑定列表：wws [查询/查]绑定/绑定列表 [me/@群友]：\n  - 切换删除绑定账号：wws [切换/删除]绑定 [序号]\n  - 查询账号总体战绩：wws [(服务器+游戏昵称)/@群友/me]\n  - 查询账号历史记录：wws [(服务器+游戏昵称)/@群友/me] record\n  - 查询账号近期战绩：wws [(服务器+游戏昵称)/@群友/me] recent [日期]\n  - 查询单船总体战绩：wws [(服务器+游戏昵称)/@群友/me] ship [船名]\n  - 查询单船近期战绩：wws [(服务器+游戏昵称)/@群友/me] ship [船名] recent [日期]\n  - 查询服务器排行榜：wws [服务器+战舰名] rank/ship.rank\n  - 查询军团详细信息：wws [(服务器+军团名)/@群友/me] clan\n  - 查询军团历史记录：wws [(服务器+军团名)/@群友/me] clan record\n  - 查询舰船中英文名：wws [搜/查船名] [国家][等级][类型]\n  - 添加游戏战绩监控: wws [添加监控] [服务器] [游戏昵称] [备注名]\n  - 查询游戏战绩监控: wws [查询监控]\n  - 删除游戏战绩监控: wws [删除监控] [监控序号]\n  - 重置全部战绩监控: wws [重置监控](该指令仅限superuser使用)\n  - 检查版本更新：wws 检查更新\n  - 更新：wws 更新Hikari\n  - 查看帮助：wws help\n  - 噗噗：一言\n\n  </details>\n## 在Windows系统上快速部署\n\n  `windows安装python版本请勿大于3.11,建议版本3.10`\n\n1. 下载Hikari的最新Release并解压到合适文件夹\n2. 复制一份`.env.prod-example`文件，并将其重命名为`.env.prod`,打开并按其中注释编辑\n    >只显示了.env，没有后面的后缀？请百度`windows如何显示文件后缀名`\n    ```\n    API_TOKEN = xxxxxxxx #无需引号，TOKEN即回复您的邮件所带的一串由[数字+冒号+英文/数字]组成的字符串\n    SUPERUSERS=["QQ号"]\n    ```\n   - 最后TOKEN应该长这样 `API_TOKEN = 123764323:ba1f2511fc30423bdbb183fe33`\n\n3. 双击`启动.bat`\n\n\n## 更新\n实验性更新指令：`wws 更新Hikari`\n请确保在能登录上服务器的情况下使用\n以下是旧更新方法\n1. 按不同版本\n   - Windows一键包：下载最新一键包，复制旧版本中`accounts`文件夹和`env.prod`文件替换至新版文件夹中即可\n   - 完整版：以管理员身份运行`更新.bat`或执行`./manage.sh update`\n      >等效于在cmd中执行如下代码\n      ```\n      pip install --upgrade hikari-bot\n      git pull\n      ```\n   - 插件版：在cmd中执行如下代码\n      ```\n      pip install --upgrade hikari-bot\n      ```\n2. **对比`.env.prod-example`中新增的配置项，并同步至你本地的`env.prod`**\n    - install结束后会打印当前版本\n    - 您也可以通过`pip show hikari-bot`查看当前Hikari版本\n    - 如果没有更新到最新版请等待一会儿，镜像站一般每五分钟同步\n    - 从0.3.2.2版本开始，您没有填写的配置将按.env文件中的默认配置执行，具体逻辑为\n      - 私聊、频道默认禁用\n      - 群聊默认开启，默认屏蔽官方交流群\n\n\n\n## 可能会遇到的问题\n\n### 出现ZoneInfoNotFoundError报错\n>\n>您可以在[这里](https://github.com/nonebot/nonebot2/issues/78)找到相关解决办法\n>\n### Recent和绑定提示\'鉴权失败\'\n1. 检查Token是否配置正确，token格式为`XXXXX:XXXXXX`\n2. 如果配置正确可能是Token失效了，请重新申请\n\n\n\n### Ubuntu系统下部署字体不正常(针对一些云服务器的Ubuntu镜像，不保证成功，只是提供一个解决方案)\n  1. 执行以下命令，完善字体库并将中文设置成默认语言（部分Ubuntu可能不需要该步骤，可直接从第二步开始）\n  ```\n  sudo apt install fonts-noto  \n  sudo locale-gen zh_CN zh_CN.UTF-8  \n  sudo update-locale LC_ALL=zh_CN.UTF-8 LANG=zh_CN.UTF-8  \n  sudo fc-cache -fv\n  ```\n  \n  2. 在你的Windows电脑上打开`C:\\Windows\\fonts`文件夹，找到里面的微软雅黑字体，将其复制出来，放在任意目录，应该会得到`msyh.ttc`，`mshybd.ttc`，`msyhl.ttc`三个文件。（不会有人还用Win7吧？）\n\n  3. 进入到`/usr/share/fonts`文件夹下，创建一个文件夹命名为`msyh`，然后进入其中\n  ```\n  cd /usr/share/fonts \n  sudo mkdir msyh \n  cd msyh\n  ```\n  \n  4. 将三个字体文件上传到`msyh`文件夹中(过程中遇到的问题请自行解决)\n\n  5. 执行以下命令（此时你应该是在`msyh`文件夹下），加载字体\n  ```\n  sudo mkfontscale \n  sudo mkfontdir \n  sudo fc-cache -fv\n  ```\n  \n  6. （可选，若不正常可尝试）重启Hikari。\n\n\n## 贡献代码\n\n请向dev分支提交PR\n\n## 鸣谢\n\n感谢以下开发者及项目做出的贡献与支持\n\n<a href="https://github.com//benx1n/HikariBot/graphs/contributors">\n  <img src="https://contrib.rocks/image?repo=benx1n/HikariBot" />\n</a>\n\n[Nonebot2](https://github.com/nonebot/nonebot2)  \n[go-cqhttp](https://github.com/Mrs4s/go-cqhttp)  \n[战舰世界API平台](https://wows.shinoaki.com/)  \n\n## 开源相关\nMIT\n修改、分发代码时请保留原作者相关信息\n\n## 赞助\n<p align="left">\n  <a href="https://afdian.net/a/JustOneSummer?tab=home"><img src="https://hikari-resource.oss-cn-shanghai.aliyuncs.com/%E7%88%B1%E5%8F%91%E7%94%B5.png" alt="afdian" ></a>\n</p>\n',
    'author': 'benx1n',
    'author_email': 'shirakamikanade@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/benx1n/HikariBot-Official',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8.0,<4.0.0',
}


setup(**setup_kwargs)
