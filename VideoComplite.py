from VideoCut import *
from config import *
from random import choice
from moviepy.editor import concatenate_videoclips



# функция рандомно выбирающая num_files клипов из папки res\clip и нарезающая клипы длительностью dur и шириной width
def cutClips(num_files, width=480, dur=10):
    list_use = []
    i = 0

    while i < num_files:
        name_clip = choice(listdir(dir_video))
        if name_clip in used_list:
            continue
        else:
            i += 1
            list_use.append(dir_video + name_clip)
            used_list.append(name_clip)
    
    VideoCut(list_use, width, dur)
    used_list = []

def choiceClip(list_file: list, last_clip):
    while True:
        clip = choice(list_file)
        if clip != last_clip:
            break
    file_dict[clip] = file_dict.get(clip, 0) + 1
    if file_dict[clip]==3:
        list_file.remove(clip)
    return clip

def compClips(lf, lc, lVFC):
    if lf:    
        file = choiceClip(lf, lc)
        lc = file
        with VideoFileClip(dir_temp+file) as clip:
            lVFC.append(clip)
            compClips(lf, lc, lVFC)
    else:
        concatenate_videoclips(lVFC).write_videofile(dir_out+out_clip)
    
    
def main():
    last_clip = ''
    list_file = listdir(dir_temp)
    list_VFC = []
    compClips(list_file, last_clip, list_VFC)
        

       
if __name__ == '__main__':
    main()
    