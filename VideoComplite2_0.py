from config import *
from random import choice
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

def cutClips(all_time, width=480, dur=10):
    all_time=((all_time*60)/add_n_clip)*1000
    used_list = [] # список для хранения имен исползованных видеофайлов
    list_use = []
    time_clips = 0

    while time_clips < all_time:
        name_clip = choice(listdir(dir_video))
        if name_clip in used_list:
            continue
        else:
            time_clips += get_track_len(dir_video+name_clip)
            list_use.append(dir_video + name_clip)
            used_list.append(name_clip)
    
    VideoCut(list_use, width, dur)
    
class VideoFile:
    def __init__(self, vf: VideoFileClip) -> None:
        self.videofile = vf
        self.next_videofile = None
    

class ListVideoFiles:
    def __init__(self) -> None:
        self.start_file: VideoFile = None
        self.focus_file: VideoFile = None
    
    def add(self, file: VideoFileClip): # загрузка файла в список
        if self.focus_file:
            self.focus_file.next_videofile = VideoFile(file)
            self.focus_file = self.focus_file.next_videofile
        else:
            self.start_file = file
            self.focus_file = file
    
    def get_file(self): # получение файла из списка
        return_file = self.focus_file.videofile
        if self.focus_file.next_videofile:
            self.focus_file = self.focus_file.next_videofile
        else:
            self.focus_file = self.start_file
        return return_file
                
    def close_files(self): # закрытие всех файлов
        self.focus_file = self.start_file



def choiceClip(list_file: list, last_clip): # случайна выборка из списка имен файлов
                                            # с счётчиком многоразовой выборки add_n_clip    
    while True:
        clip = choice(list_file)
        if clip != last_clip:
            break
    file_dict[clip] = file_dict.get(clip, 0) + 1
    if file_dict[clip]==add_n_clip:
        list_file.remove(clip)
    return clip

def choice_file(la): # случайная выборка из списка
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
          
def create_lib_video(): # создание списка ресурсных видео
    list_file = listdir(dir_temp)
    open_files = ListVideoFiles()
    for _ in range(len(list_file)):
        file_path = dir_temp + choice_file(list_file)
        open_files.add(VideoFileClip(file_path))
    return open_files

def main():
    list_open_files = create_lib_video()
    

       
if __name__ == '__main__':
    main()
    