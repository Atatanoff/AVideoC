from VideoCut import *
from config import *
from random import choice
from moviepy.editor import concatenate_videoclips
from shutil import copyfile


# функция рандомно выбирающая num_files клипов из папки res\clip и нарезающая клипы длительностью dur и шириной width
def cutClips(num_files, dur=10, width=480):
    list_use = []
    i = 0
    while i < num_files:
        name_clip = choice(os.listdir(dir_video))
        if name_clip in used_list:
            continue
        else:
            i += 1
            list_use.append(dir_video + name_clip)
            used_list.append(name_clip)
    
    VideoCut(list_use, dur, width)

def choiceClip(list_file: list, last_clip):
    while True:
        clip = choice(list_file)
        if clip != last_clip:
            break
    file_dict[clip] = file_dict.get(clip, 0) + 1
    if file_dict[clip]==3:
        list_file.remove(clip)
    return clip

def recClips(cl1, cl2):
    with VideoFileClip(cl1) as cl1, VideoFileClip(cl2) as cl2:
        concatenate_videoclips([cl1, cl2]).write_videofile('out\\outclip.mp4')


def compClips():
    last_clip = ''
    list_file = listdir(dir_temp)
    copy_file = choiceClip(list_file, last_clip)
    copyfile(f'{dir_temp+copy_file}', f'{dir_out+out_clip}')
    while list_file:
        append_clip = choiceClip(list_file, last_clip)
        last_clip = append_clip
        recClips(dir_out+out_clip, dir_temp+append_clip)
        
      
if __name__ == '__main__':
    compClips()
    
