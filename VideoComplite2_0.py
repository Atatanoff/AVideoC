from config import *
from random import choice, randint
from moviepy.editor import CompositeVideoClip, vfx, AudioFileClip, VideoFileClip
from pydub import AudioSegment
from pymediainfo import MediaInfo
from os import listdir


#предусмотреть увелечение рекурсии в compClips
# функция рандомно выбирающая num_files клипов из папки res\clip и нарезающая клипы длительностью dur и шириной width

def get_track_len(file_path): #функция возвращающая длину видефайла в милисекундах
    media_info = MediaInfo.parse(file_path)
    for track in media_info.tracks:
        if track.track_type == "Video":
            return int(track.duration)
    return 0
                 
def choice_file(la): # случайная выборка из передаваемого списка
    file_name = choice(la)
    la.remove(file_name)
    return file_name

def make_wav(len_clip): # монтаж аудиодорожки для выходного файла 
    list_mp3 = listdir(dir_audio)
    play = AudioSegment.from_mp3(choice_wav(list_mp3)).fade_in(3000)
    len_play = len(play)
    while len_play < len_clip:
        play = play.append(AudioSegment.from_mp3(choice_wav(list_mp3)), crossfade=crossfade)
        len_play = len(play)
    play = play[:len_clip-1000]
    play = play.fade_out(3000)
    play.export(dir_out+out_audio, format=format_audio)
          
def create_lib_video(): # создание связанного списка из рессурсных видео
    list_file = listdir(dir_temp)
    open_files = ListVideoFiles()
    for _ in range(len(list_file)):
        file_path = dir_temp + choice_file(list_file)
        open_files.add(Temp(file_path))
    return open_files

def rand_sub(vf: VideoFileClip):
    pass


def main():
    list_open_files = create_lib_video()
    try:
        file = list_open_files.get_file()
        t_start = randint(0, int(file.duration)-10)
        clip = CompositeVideoClip()
            
    except Exception as e:
        
        print(e,' произошла ошибка начальнике')
        raise e
    finally:
        list_open_files.close_files()
           
if __name__ == '__main__':
    main()
    