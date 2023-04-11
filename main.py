import voice_to_word
import chat
import word_to_voice
import sys
import os
from ASR.ASR import myAsr
import json

while True:
    test = sys.stdin.readline()
    #如果最后为换行符，则去掉
    if(test[-1] == '\n'):
        test = test[:-1]
    if(test == 'start record'):
        os.system("arecord -DMainMicCapture -r 44100  -f S16_LE -c 2 -d 1000  ./audio/record.wav &")

    if(test == 'stop record'):
        os.system("killall arecord")
        print('stop record success')
        myAsr()
        #读取result.json文件中result.voice_text_str
        with open("result.json", "r",encoding='utf-8') as f:
            result = f.read()
            result = json.loads(result)
            print(result['result']['voice_text_str'])
        #word = result['result']['voice_text_str']
        #word=voice_to_word.get_words("./audio/record.wav")
        word = '今天天气真好'
        print('user: '+word)
        answer=chat.chatGPT("下面的对话中，你要在你的回答的开头用（心情）的方式说明你的回答的感情，比如：（开心）谢谢你的夸奖；（生气）你不应该这样说我。可供选择的词有：开心，难过，生气，害羞，惊讶，疑惑，委屈，无语，平淡\n"+word)
        print('chatdog: ' +answer)

        word_to_voice.gtts_debug(answer,"./audio/answer.wav",1)

        os.system("aplay -DHeadphoneNormal ./audio/answer.wav")