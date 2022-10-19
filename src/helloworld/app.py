"""
My first application
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
from urllib.request import urlopen ,Request
import re
import urllib
import time
#app主题
class HelloWorld(toga.App):

    def startup(self):
        """
        Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        #主框架
        main_box = toga.Box(style=Pack(direction=COLUMN))

        #嵌套框架---1
        name_label=toga.Label('计算器:',style=Pack(padding=(0,5)))
        self.name_input=toga.TextInput(style=Pack(flex=1))
        name_box=toga.Box(style=Pack(direction=ROW,padding=5))
        name_box.add(name_label)
        name_box.add(self.name_input)
        name_button=toga.Button('计算结果',on_press=self.calculate,style=Pack(padding=5))
        #嵌套框架---2
        douyin_label=toga.Label('抖音链接',style=Pack(padding=(0,5)))
        self.douyin_input=toga.TextInput(style=Pack(flex=1))
        douyin_box=toga.Box(style=Pack(direction=ROW,padding=5))
        douyin_box.add(douyin_label)
        douyin_box.add(self.douyin_input)
        douyin_button=toga.Button('解析链接',on_press=self.get_html,style=Pack(padding=5))
        #添加到主框架内
        main_box.add(name_box)
        main_box.add(name_button)
        main_box.add(douyin_box)
        main_box.add(douyin_button)
        
        #主窗口
        self.main_window = toga.MainWindow(title='love you')
        self.main_window.content = main_box
        self.main_window.show()
    def get_html(self,widget):
        head={}
        head['Cookie']='douyin.com; ttwid=1%7CXpx1mOrkAnKoJtL89a4Q5HE70ftHQIZb0Ygn909hMR0%7C1653977203%7C9b99e4a81f7b4691f8d8b12c20df8d892feab100e5492a37f80ecaa62199eff5; odin_tt=8b8288e76bafd2a0b3f8250ba31b769ede9464284bddfc66cdc253fbd75396402ae421afee28a51fc0115fce094567a41c5d8aec94f6c40537fa4e7ea1ced773; n_mh=HYw7AtmJi-q28N9008QLFgMnF7UFQb-iX2ufVfcgCFY; sid_guard=614800c4e84e2ac806c899a6805e038c%7C1653976970%7C5184000%7CSat%2C+30-Jul-2022+06%3A02%3A50+GMT; msToken=jEiFZJOQqpzArdzJukLVrXTTmSRS-cj2APCVpqpEAYzB3_R376Yv0R0uNlkoHcWI_7xfHZ9FycJOZf1c-CIwJTS5rh6W4hXcsFH0ZaT139ljwMV6KL5G7ZVt_OXQnF50TQ==; home_can_add_dy_2_desktop=%220%22; strategyABtestKey=1663062638.46; s_v_web_id=verify_l7uld0ll_Mw2HsiVE_cvwD_4SeZ_B3k3_tSup4cBkFPJV; passport_csrf_token=d67a369d2f0aac92088f1325554a2e91; passport_csrf_token_default=d67a369d2f0aac92088f1325554a2e91; SEARCH_RESULT_LIST_TYPE=%22single%22; douyin.com; __ac_nonce=063205f86000386dbbfbc; __ac_signature=_02B4Z6wo00f01a2bcUQAAIDAWBNVUkgblzmtunXAAAhHtrAsQqt.igadqoO.aIuui5ce.26pdmkKlsxS1ePHCCAqg6Ebd3nYAdpJmWCHDwLuVVk1ajFnSBfI-.feqWWjtGro.Uwtqk4x9Cd715; tt_scid=S9Vpq9-G-D728NMiJFwB-TQvPtxWSl6-J4GwfU26EBjvuEUaBXumr-TEOF4v3S0G6912; msToken=6Qxv-6Ntpr8LFC5Pb2CiA1QWLyqnffg7ki7uvqHqlrduZXBgszWrZiakcddpTN3XNhrTeMfbK1awODkZp0gTpsshtjckL-BUCi5ph3PQgMx10yBXSjvClJbPC2CG5WpQjQ=='
        head['User-Agent']='Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0'
        url=re.findall('https://v.douyin.com/.*?/',self.douyin_input.value)[0]
        self.main_window.info_dialog(
            'URL',url
        )
        resp=Request(url,headers=head)
        try:
            res=urlopen(resp)
            self.main_window.info_dialog(
                'Successfully','正在解析'+url
                )
        except:
            self.main_window.info_dialog(
                'error',f'{url} 网址解析错误'
                )
            #解码网页源码
            html=urllib.parse.unquote(str(res.read(),'utf-8'))
        try:
            hrefs=re.findall('src":"(.*?)&ch=26',html)
            #找到标题和链接
            title=f'VID_{time.strftime("%Y%m%d")}'+re.findall('<span class="Nu66P_ba"><span><span><span><span>(.*?)</span></span>',html)[0]+'.mp4'
            url='https:'+hrefs[0]
            bitfile=urlopen(url).read()
            
            path=f'C:User\Administrator\Desktop\{title}'
        except:
            self.main_window.info_dialog('title','message')
        #写入文件
        with open(path,'wb') as file:
            file.write(bitfile)
        self.main_window.info_dialog(
            title,f'{path}保存成功'
            )

    #计算函数
    def calculate(self,widget):
        try:
            self.main_window.info_dialog(
                '计算结果:','{}={}'.format(self.name_input.value, eval(self.name_input.value))
                )
        except:
            self.main_window.info_dialog(
                '错误','输入的式子不可计算'
                )
    
    


def main():
    return HelloWorld()
