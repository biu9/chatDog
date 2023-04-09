# 函数功能: 用gtts库阅读文本,保存为.mp3文件后, 用playsound库阅读出来, 阅读完毕, 函数执行结束
def gtts_debug(text,mp3_filepath,language):#参数说明:参数1是朗读的文字,参数2是保存路径,参数3是数字{0英文,1中文,2日语}
    #大成功,已经实现了定制化文字转语音,但是播放的playsound需要改进(playsound库本身可能会出现bug...)
    from gtts import gTTS
    from playsound import playsound
    import os
    if int(language) ==0 :
        s = gTTS(text=text, lang='en', tld='com')
        # s = gTTS(text=text, lang='en', tld='co.uk')#我比较喜欢美音,但是如果你喜欢英国口音可以尝试这个
    elif int(language) ==1 :
        s = gTTS(text=text, lang='zh-CN')
    elif int(language) ==2 :
        s = gTTS(text=text, lang='ja')
    try:
        s.save(mp3_filepath)
    except:
        os.remove(mp3_filepath)
        print(mp3_filepath,"文件已经存在,但是没有关系!已经删掉了")
        s.save(mp3_filepath)
    print(mp3_filepath,"保存成功")
    playsound(mp3_filepath)
