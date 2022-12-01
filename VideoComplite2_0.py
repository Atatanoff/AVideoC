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
    file_mp3 = dir_audio + choice_file(list_mp3)
    play = AudioSegment.from_mp3(file_mp3).fade_in(3000)
    len_play = len(play)
    while len_play < len_clip:
        file_mp3 = dir_audio + choice_file(list_mp3)
        play = play.append(AudioSegment.from_mp3(file_mp3), crossfade=crossfade)
        len_play = len(play)
    play = play[:len_clip-1000]
    play = play.fade_out(3000)
    play.export(dir_out+out_audio, format=format_audio)
          
def create_lib_video(): # создание связанного списка из рессурсных видео
    list_file = listdir(dir_temp)
    open_files = []
    for _ in range(len(list_file)):
        file_path = dir_temp + choice_file(list_file)
        open_files.append(VideoFileClip(file_path))
    return open_files

def main():
    list_open_files = create_lib_video()
    lict_comp_files = []
    len_out_clip = 0
    i = 0
    start = 0
    try:
        while len_out_clip < duraion_out_clip:
            video = list_open_files[i]
            video_dur = int(video.duration)
            if video_dur <=10:
                pass
            s = randint(0, video_dur-10)
            clip = video.subclip(s, s+10).resize(width_out_clip)
            if randint(0, 1):
                clip = clip.fx(vfx.mirror_x)
            dur = clip.duration

            lict_comp_files.append(clip.set_start(start).crossfadein(crossfadein))
            start = start + dur - crossfadein
            i+=1
            if i==len(list_open_files):
                i = 0
            len_out_clip = dur-crossfadein
        final_clip = CompositeVideoClip(lict_comp_files)
        len_clip = final_clip.duration*1000
        make_wav(len_clip)
        final_audio = AudioFileClip(dir_out+out_audio)
        final_clip.set_audio(final_audio).write_videofile(dir_out+out_clip)

    finally:
        for el in list_open_files:
            el.close()
        print('все файлы закрыты')
           
if __name__ == '__main__':
    main()
    