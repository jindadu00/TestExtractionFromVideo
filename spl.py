from pydub import AudioSegment
from pydub.utils import make_chunks

def splitAudio(filename,size=40000):
    audio = AudioSegment.from_file(filename, "wav")
    chunks = make_chunks(audio, size)
    audioList=list()
    for i, chunk in enumerate(chunks):
        chunk_name = filename[:-4]+"-{0}.wav".format(i)
        print(chunk_name)
        audioList.append(chunk_name)
        chunk.export(chunk_name, format="wav")
    return audioList

# splitAudio('fwav.wav',size=29000)