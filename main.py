import chat
import word_to_voice
import sys
import os
from ASR.ASR import myAsr
import TTS.tcloud_tts as tts
import display
import json
import time

from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QLabel, QApplication)

class Mythread(QThread):
    def __init__(self):
        super(Mythread,self).__init__()
    def run(self):
        while True:
            time.sleep(1)
            # 初始化GUI

            test = sys.stdin.readline()
            #如果最后为换行符，则去掉
            if(test[-1] == '\n'):
                test = test[:-1]
            if(test == '1'):
                os.system("arecord -DMainMicCapture -r 8000  -f S16_LE -c 2 -d 1000  ./audio/record.wav &")

            if(test == '2'):
                os.system("killall arecord")
                print('stop record success')
                myAsr()
                #读取result.json文件中result.voice_text_str
                with open("result.json", "r",encoding='utf-8') as f:
                    result = f.read()
                    result = json.loads(result)
                    print(result['result']['voice_text_str'])
                word = result['result']['voice_text_str']
                #word=voice_to_word.get_words("./audio/record.wav")
                #word = '今天天气真好'
                print('user: '+word)
                answer=chat.chatGPT("下面的对话中，你要在你的回答的开头用（心情）的方式说明你的回答的感情，比如：（开心）谢谢你的夸奖；（生气）你不应该这样说我。可供选择的词有：开心，难过，生气，害羞，惊讶，疑惑，委屈，无语，平淡\n"+word)
                print('chatdog: ' +answer)

                #提取出answer中的表情
                ansExpression = answer[answer.find('(')+1:answer.find(')')]
                if(ansExpression == ''):
                    ansExpression = answer[answer.find('（')+1:answer.find('）')]

                # 删除answer前的语气词
                answer = answer[answer.find(')')+1:]
                answer = answer[answer.find('）')+1:]

                # 生成表情
                expression.modify(ansExpression)

                tts.task_process(answer)

                os.system("aplay -DSpeakerNormal /home/toybrick/Desktop/project/TTS/test.wav")




app =QApplication(sys.argv)
expression = display.displayer()
myth = Mythread()
myth.start()

sys.exit(app.exec()) 