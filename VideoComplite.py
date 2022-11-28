from VideoCut import *
from config import *
import random
from moviepy.editor import concatenate_videoclips

# функция рандомно выбирающая num_files клипов из папки res\clip и нарезающая клипы длительностью dur и шириной width
def cutClips(num_files, dur=10, width=480):
    list_use = []
    i = 0
    while i < num_files:
        name_clip = random.choice(os.listdir(dir_video))
        if name_clip in used_list:
            continue
        else:
            i += 1
            list_use.append(dir_video + name_clip)
            used_list.append(name_clip)
    
    VideoCut(list_use, dur, width)

def choiceClip(list_file: list):
    while True:
        clip = random.choice(list_file)
        if clip != last_clip:
            last_clip = clip
            break
    file_dict[clip] = file_dict.get(clip, 0) + 1
    if file_dict[clip]==3:
        list_file.remove(clip)
    return clip

def compClips():
    list_file = os.listdir('temp\\')
    out_clip = choiceClip(list_file)
    while True:
        append_clip = choiceClip(list_file)
        recClips(out_clip, append_clip)



if __name__ == '__main__':
    compClips()
    
