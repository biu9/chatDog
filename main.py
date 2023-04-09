import voice_to_word
import chat
import word_to_voice
import sys
import os

while True:
    test = sys.stdin.readline()
    #如果最后为换行符，则去掉
    if(test[-1] == '\n'):
        test = test[:-1]
    if(test == 'start record'):
        os.system("arecord -DMainMicCapture -r 44100  -f S16_LE -c 2 -d 1000  ./audio/record.wav &")

    if(test == 'stop record'):
        os.system("killall arecord")
        print('11111')
        word=voice_to_word.get_words("./audio/record.wav")
        print('user: '+word)
        answer=chat.chatGPT("下面的对话中，你要在你的回答的开头用（心情）的方式说明你的回答的感情，比如：（开心）谢谢你的夸奖；（生气）你不应该这样说我。可供选择的词有：开心，难过，生气，害羞，惊讶，疑惑，委屈，无语，平淡\n"+word)
        print('chatdog: ' +answer)

        word_to_voice.gtts_debug(answer,"./audio/answer.wav",1)

        os.system("aplay -DHeadphoneNormal ./audio/answer.wav")