import os
from ffmpy3 import FFmpeg
from spl import splitAudio
from aip import AipSpeech

# 百度语音转文字
def BAIDU_ASR(wavfile):
    def get_file_content(file):
        with open(file,'rb') as fp:
            return fp.read()
    """ 你的 APPID AK SK """
    APP_ID = '25812903'
    API_KEY = 'yk0kpKntatLKoPAQgcEkClis'
    SECRET_KEY = 'FtVXjLa6M1fpNZlLQIWq6dlwRCCBaDgR'
    client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
    result = client.asr(get_file_content(wavfile),'wav',16000,{
        'dev_pid':1537
    })
    return result['result']

audiFile='fwav-vocals-D minor-141bpm.wav'
filename = 'write_data.txt'
with open(filename,'a') as f: # 如果filename不存在会自动创建， 'w'表示写数据，写之前会清空文件中的原有数据！
    LIS=splitAudio(audiFile)
    for audi in LIS:
        f.write(''.join(BAIDU_ASR(audi)))