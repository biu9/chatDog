# # 函数功能: 用gtts库阅读文本,保存为.mp3文件后, 用playsound库阅读出来, 阅读完毕, 函数执行结束
# def gtts_debug(text,mp3_filepath,language):#参数说明:参数1是朗读的文字,参数2是保存路径,参数3是数字{0英文,1中文,2日语}
#     #大成功,已经实现了定制化文字转语音,但是播放的playsound需要改进(playsound库本身可能会出现bug...)
#     from gtts import gTTS
#     from playsound import playsound
#     import os
#     if int(language) ==0 :
#         s = gTTS(text=text, lang='en', tld='com')
#         # s = gTTS(text=text, lang='en', tld='co.uk')#我比较喜欢美音,但是如果你喜欢英国口音可以尝试这个
#     elif int(language) ==1 :
#         s = gTTS(text=text, lang='zh-CN')
#     elif int(language) ==2 :
#         s = gTTS(text=text, lang='ja')
#     try:
#         s.save(mp3_filepath)
#     except:
#         os.remove(mp3_filepath)
#         print(mp3_filepath,"文件已经存在,但是没有关系!已经删掉了")
#         s.save(mp3_filepath)
#     print(mp3_filepath,"保存成功")
#     playsound(mp3_filepath)
# 函数功能: 用gtts库阅读文本,保存为.mp3文件后, 用playsound库阅读出来, 阅读完毕, 函数执行结束
from  playsound import playsound
from aip import AipSpeech
import wave
APP_ID = '32273566'
API_KEY = 'zTziPhVzlBFpWycLGOif7d29'
SECRET_KEY = 'Akhh6bb9Gw0jk5kX21fibODSGvlGEku6'
 
client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
# lan="你好，我是百度小助手" 
def gtts_debug(text,mp3_filepath,language):
    import os
    # text="你很厉害"
    result = client.synthesis(text, 'zh', 1, { 'vol': 5,'per':4,'spd':5 })
    if not isinstance(result, dict): 
        with open(mp3_filepath, 'wb') as f: 
            f.write(result)
        # os.system('ffmpeg -i '+mp3_filepath+' -vn -ac 2 -ar 44100 -acodec pcm_S16LE -y '+mp3_filepath)
        
        os.system('ffmpeg -i {} -vn -ac 2 -ar 8000 -acodec pcm_s16le -y {}'.format(mp3_filepath,'./audio/1.wav'))

        # f = wave.open(mp3_filepath, "wb")  
        # # 配置声道数、量化位数和取样频率
        # f.setnchannels(1)
        # f.setsampwidth(2)
        # f.setframerate(16000)
        # # 将wav_data转换为二进制数据写入文件
        # f.writeframes(result)
        # f.close()
    else:
        os.remove(mp3_filepath)
        print(mp3_filepath,"文件已经存在,但是没有关系!已经删掉了")
        # result.save(mp3_filepath)
        with open(mp3_filepath, 'wb') as f: 
            f.write(result)
        print("11111")
        # f = wave.open(mp3_filepath, "wb")  
        # # 配置声道数、量化位数和取样频率
        # f.setnchannels(1)
        # f.setsampwidth(2)
        # f.setframerate(16000)
        # # 将wav_data转换为二进制数据写入文件
        # f.writeframes(result)
        # f.close()
        os.system('ffmpeg -i {} -vn -ac 2 -ar 8000 -acodec pcm_s16le -y {}'.format(mp3_filepath,'./audio/1.wav'))

    print(mp3_filepath,"保存成功")
    playsound(mp3_filepath)
