import easygui as g
import sys
import Core as c

def urlBox():
    url = g.enterbox(msg="请输入歌曲所在网页",title="请输入：",default='示例：https://music.163.com/#/song?id=1293886117')
    try:
        _id = int(url.split('id=')[1])
    except:
        g.msgbox('网易云音乐网址格式错误。')
        sys.exit(0)
    downloadBox(_id)

def findBox():
    name = g.enterbox(msg="请输入关键字，以空格分隔",title="请输入关键字：",default='年少有为 李荣浩')
    song_list = c.get_id_by_name(name)
    if song_list==None:
        g.msgbox("找不到该歌曲有关信息。")
        sys.exit(0)
    name_list = [i[0]+'  '+i[1] for i in song_list]
    reply_index = name_list.index(g.choicebox('请选择要下载的内容',choices=name_list))
    downloadBox(song_list[reply_index][2]) 

def downloadBox(_id):
    try:
        url,name = c.get_music_url_by_id(_id)
        if url == None:
            g.msgbox("ID:{}没有对应歌曲。".format(_id),title='警告')
            sys.exit(0)
        address = g.filesavebox(msg="请选择要保存的位置",default=name)
        c.download(url,path=address)
    except ConnectionError as e:
        g.msgbox("网络错误。",title='警告')
        sys.exit(0)
    except Exception as e:
        g.msgbox("未知错误。",title='警告')
        sys.exit(0)

    g.msgbox(name+"下载成功",title='恭喜',ok_button='退出')
    

def HelloBox():
    if g.ccbox(msg='欢迎使用王某开发的网易云音乐下载器，本产品只用于编程交流，请支持正版。技术交流QQ：1439347960',title='欢迎',choices=('继续','退出')) :
        if g.ccbox(msg='请选择使用哪种方式搜索你想要的歌曲。',title='请选择找歌方式',choices=('基于网址','搜索')):
            urlBox()
        else:
            findBox()
    else:
        sys.exit(0)

if __name__ == '__main__':
    HelloBox()