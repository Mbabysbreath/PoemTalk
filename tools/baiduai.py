from aip import AipSpeech
from pydub import AudioSegment
from pygame import mixer
import os
from playsound import playsound
#语音合成-文件转语音
def so_syn(txtname):
    """ 你的 APPID AK SK """
    APP_ID = '23849535'
    API_KEY = 'ko3ZcdGIDhkrU2wlmk6ANTQR'
    SECRET_KEY = 'DrGDDQRY7pevdmNunHhKQTdjk4HiyLSe'

    client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
    with open(txtname,'r',encoding='utf-8') as sub:
        num=0
        while True:
            text=sub.read(1023)
            if text:
                num+=1
                print(num)
                result=client.synthesis(text,'zh',1,{'spd':4,'vol':5,'per':0})
                print(result)
                if not isinstance(result,dict):
                    with open('audio/郡斋雨中与诸文士燕集.mp3', 'wb')as f:
                        print('----1')
                        f.write(result)

                print("正在合成"+str(num)+'段文本')
            else:
                break
#语音文件拼接
from pydub import AudioSegment
# def mp3_to_wav(mp3_path, wav_path):
#     song = AudioSegment.from_mp3(mp3_path)
#     song.export(wav_path, format="wav")
#
# if __name__ == '__main__':
#     mp3_to_wav('audio.mp3',"audio.wav")

def joinvoice():
    finally_sound=AudioSegment.empty()
    # for i in os.listdir(savefile):
    sound=AudioSegment.from_mp3('audio/郡斋雨中与诸文士燕集.mp3')
    finally_sound+=sound
    finally_sound.export('audio/1.wav',format="wav")
#语音文件播放
def play(filename):
    mixer.init(frequency=16000)
    mixer.music.load(filename)
    mixer.music.play()
    userin=input('输入p停止播放')
    if userin=='p':
        mixer.music.pause()
    mixer.music.stop()
if __name__=='__main__':

    txtname='audio/data.txt'
    savefile='audio'
    result_name='resultsound.wav'
    so_syn(txtname)
    joinvoice()
    play('audio/1.wav')
    # playsound('2.mp3')

