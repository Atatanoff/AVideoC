from VideoCut import *
from config import *
from random import choice
from moviepy.editor import CompositeVideoClip, vfx, AudioFileClip
from pydub import AudioSegment
from pymediainfo import MediaInfo


#предусмотреть увелечение рекурсии в compClips
# функция рандомно выбирающая num_files клипов из папки res\clip и нарезающая клипы длительностью dur и шириной width

def get_track_len(file_path):
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
    

def choiceClip(list_file: list, last_clip):
    while True:
        clip = choice(list_file)
        if clip != last_clip:
            break
    file_dict[clip] = file_dict.get(clip, 0) + 1
    if file_dict[clip]==add_n_clip:
        list_file.remove(clip)
    return clip

def choice_wav(la):
    play_name = choice(la)
    la.remove(play_name)
    return dir_audio+play_name

def make_wav(len_clip):
    list_mp3 = listdir(dir_audio)
    play = AudioSegment.from_mp3(choice_wav(list_mp3)).fade_in(3000)
    len_play = len(play)
    while len_play < len_clip:
        play = play.append(AudioSegment.from_mp3(choice_wav(list_mp3)), crossfade=2000)
        len_play = len(play)
    play = play[:len_clip-1000]
    play = play.fade_out(3000)
    play.export(dir_out+out_audio, format='mp3')
          
def compClips(lf, lc, lVFC,start=0):
    if lf:    
        file = choiceClip(lf, lc)
        lc = file
        mirror = 1 if file_dict.get(file,0) == 2 else 0 
        with VideoFileClip(dir_temp+file) as clip:
            if mirror:
                clip = clip.fx(vfx.mirror_x)
            lVFC.append(clip.set_start(start).crossfadein(1))
            compClips(lf, lc, lVFC,start+clip.duration-1)
    else:
        final_clip = CompositeVideoClip(lVFC)
        len_clip = final_clip.duration*1000
        make_wav(len_clip)
        final_audio = AudioFileClip(dir_out+out_audio)
        final_clip.set_audio(final_audio).write_videofile(dir_out+out_clip)

def main():
    cutClips(20, 1920)
    last_clip = ''
    list_file = listdir(dir_temp)
    list_VFC = []
    compClips(list_file, last_clip, list_VFC)
    

       
if __name__ == '__main__':
    main()
    