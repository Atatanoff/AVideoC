#CVideo 1.01 - прога для создания 3х часового видео из 10секундных кусочков соедененых рандомно с наложением аудиофайла

from moviepy.editor import VideoFileClip, concatenate_videoclips

# ВНИМАНИЕ!!! завтра оформить эти две функции в класс для нарезки кусочков, объекты класса получают аргументы такие как длина кусочков, список файлов
# ширина файла, фпс

# функция нарезки 10сек кусочков и остатков из видеозаготовок

class VideoCut:
    def __init__(self, clips, width_c=480, length_c=10, fps=24):
        self.list_clips = clips
        self.width_clip = width_c
        self.length_clip = length_c
        self.fps =       
        self.cc = 0
        self.t_start = 0
        self.t_end = 10
        for el in clips:
            with VideoFileClip(el) as clip:
                cc = self.edition_clip(clip, self.t_start, self.t_end, cc)
    def edition_clip(self, cl: VideoFileClip, t_s, t_e, count_clip):
        if cl.duration > t_e:
            cl.subclip(t_s, t_e).write_videofile(f'newclip{count_clip}.mp4')
            return edition_clip(cl, t_e, t_e+10, count_clip+1)
        else:
            cl.subclip(t_s).write_videofile(f'newclip{count_clip}.mp4')
            return count_clip+1
    

            

if __name__ == '__main__':
    clips = ('v1.mp4', 'v2.mp4')
    main(clips)    
