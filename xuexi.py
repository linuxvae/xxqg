# coding=utf-8

import uiautomator2 as ut2
import time

#阅读文章
def read_articles(d):
	d(className="android.widget.LinearLayout", instance=18).swipe("left", steps=20)
	print("read_articles\n")
	for i in range(6):
		try:
			if d(className="android.widget.LinearLayout", instance=18).count == 0:
				print(u"android.widget.LinearLayout instance=18 == 0 \n")
				d(scrollable=True).scroll(steps=100)
				continue
			d(className="android.widget.LinearLayout", instance=18).click()

			if d(text=u"好观点将会被优先展示").count == 0 and d(text=u"欢迎发表你的观点").count == 0:
				print(u"好观点将会被优先展示 == 0\n")
				time.sleep(1)
				d.press("back")
				time.sleep(1)
				d(scrollable=True).scroll(steps=100)
				continue
		
			#d.implicitly_wait(10.0)
			print("cliek 18 \n")
			for i in range(5):
				time.sleep(5)
				if d(scrollable=True).scroll(steps=100) ==False:
					break
			for i in range(5):
				time.sleep(5)
				if d(scrollable=True).scroll.backward(steps=100) ==False:
					break
			#输入内容
			print(u"发表观点 \n")
			d(resourceId="cn.xuexi.android:id/home_bottom_tab_icon_group", className="android.widget.FrameLayout", instance=2).click()
			d(className="android.widget.EditText").send_keys(u"民族的伟大复兴，实现两个一百年")
			d(text=u"发布").click()
			time.sleep(1)
			d.press("back")
			time.sleep(1)
			d(scrollable=True).scroll(steps=100)#阅读文章
		except Exception as e:
			print(e)
def play_video(d):
	print("play_video\n")
	d(resourceId="cn.xuexi.android:id/home_bottom_tab_icon", className="android.widget.ImageView")[2].click()
	for i in range(12):
		d(className="android.widget.LinearLayout", instance=18).click()
		time.sleep(20)
		d.press("back")
		time.sleep(1)
		d(scrollable=True).scroll(steps=100)
		print("play_video once\n")		

def main():
	d = ut2.connect('http://192.168.1.104:7912')
	print(d.info)
	d.app_start('cn.xuexi.android')
	time.sleep(10)
	read_articles(d)
	play_video(d)
	
if __name__ == '__main__':
    main()