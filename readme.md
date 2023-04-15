## chatDog  

### 概览

实现了部署在RK3399上，能够实时语音输入输出并带有对应表情的语音小助手

### 技术栈

- ASR:腾讯云实时语音识别
- TTS:腾讯云基础语音转文字
- GPT:GPT3.5模型
- expression:pyqt
- 部署：RK3399ProD

### TODO

1. ~~将ASR模块识别的文件转换为audio文件夹下的answer~~
2. 表情模块
    1. 增加过渡gif
3. ~~TTS模块生成的wav无法被ALSA读出的问题~~
4. 整体代码架构的优化
