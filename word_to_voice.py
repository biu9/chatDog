# 函数功能: 用gtts库阅读文本,保存为.mp3文件后, 用playsound库阅读出来, 阅读完毕, 函数执行结束
from aip import AipSpeech
APP_ID = '31921804'
API_KEY = 'Z1oeXQ5BtCMNUhXMeQwoNbvr'
SECRET_KEY = 'bGskGIXS8vTwtp6dkiGCWzStc2fzqnWP'
 
client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
# lan="你好，我是百度小助手" 
def gtts_debug(text,mp3_filepath,language):
    from playsound import playsound
    import os
    result = client.synthesis(text, 'zh', 1, { 'vol': 5,'per':4,'spd':5 })
    try:
        result.save(mp3_filepath)
    except:
        os.remove(mp3_filepath)
        print(mp3_filepath,"文件已经存在,但是没有关系!已经删掉了")
        result.save(mp3_filepath)
    print(mp3_filepath,"保存成功")
    playsound(mp3_filepath)
