# xxqg
工具：uiautomator2 、qpython、atx-agent


# 使用方法
*   使用电脑进行安装atx-agent\uiautomator2软件 <tr>
1.  电脑安装uiautomator2 <tr>
<pre><code>
    pip install --pre uiautomator2
    pip install pillow
</code></pre>
2.  设备安装atx-agent
首先Android设备连接到PC，并能够adb devices发现该设备，执行命令
  <pre><code>
   python -m uiautomator2 init  
  </code></pre>
最后提示success，代表atx-agent初始化成功。
 此时你可以下载xuexi.py,在本地目录进行python xuexi.py 运行脚本（内部的IP地址换成自己手机的IP地址或者查看https://github.com/openatx/uiautomator2#connect-to-a-device 进行USB方式的连接）
  
**********************************************************************
  <p>以上方法适用于USB连接情况下运行脚本，可不可以不适用USB连接，直接在手机上运行脚本呢？</p>
  <p>使用Qpython</p>  
  
*  安卓手机 IOS应该也可以
1.  手机应用中下载Qpython  或者qpython3L
2.  qpython中点击pip console 选择进行pip install 安装 huamanize、progress、requests、retry 四个库（如果是qpython3 就是pip3 install ）
4.  python -m uiautomator2 init  这步会把atx-agent启动并保持后台运行
3.  adb push xuexi.py /storage/emulated/0/qpython/script3/   把脚本push到设备中的qpython目录去
4.  qpython 中打开脚本，点击运行，既可刷起来

