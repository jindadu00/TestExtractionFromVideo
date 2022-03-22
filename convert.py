from ffmpy3 import FFmpeg
# 视频转wav音频
def vedio_to_wav(file):
    inputfile = file
    file_type = file.split('.')[-1]
    outputfile = inputfile.replace(file_type, 'wav')
    ff = FFmpeg(
                inputs={file: None},
                outputs={outputfile: '-vn -ar 44100 -ac 2 -ab 192 -f wav'}
                )
    print(ff.cmd)
    ff.run()
    return outputfile

vedio_to_wav('fflv.flv')