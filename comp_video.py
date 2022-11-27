#CVideo 1.01 - прога для создания 3х часового видео из кусочков соедененых рандомно с наложением аудиофайла

from moviepy.editor import VideoFileClip, concatenate_videoclips

#************************************************************************#
#       VideoCut класс для нарезки кусочков из видеозаготовок            #
#        self.list_clips - список видеозаготовок                         #
#        self.width_clip - ширина клипов                                 #
#        t_end - время конца обрезки видеозаготовки                 #
#        self.fps = fps - частота кадров                                 #
#        self.count_clip   - счетчик клипов                         #
#        t_start - время начала обрезки видеозаготовка          #
#        self.length_clip = длина клипа                                  #
##########################################################################        

class VideoCut:
    def __init__(self, clips, width_c=480, length_c=10, fps=24):
        self.list_clips = clips
        self.width_clip = width_c
        self.length_clip = length_c
        self.fps = fps
        self.count_clip = 0
        
        for el in clips:
            with VideoFileClip(el) as clip:
                self.edition_clip(clip)
        print(f"Всего нарезано клипов: {self.count_clip} штук")
    
    def edition_clip(self, cl: VideoFileClip):
        flag = cl.duration
        t_start = 0
        t_end = self.length_clip 
        while flag > t_end:
            cl.subclip(t_start, t_end).resize(width = self.width_clip).write_videofile(f'newclip{self.count_clip}.mp4', fps=self.fps)
            self.count_clip +=1
            t_start = t_end
            t_end += self.length_clip
            print('\n')
        if flag > 4:
            cl.subclip(t_start).resize(width = self.width_clip).write_videofile(f'newclip{self.count_clip}.mp4', fps=self.fps)
            self.count_clip +=1
            print('\n')
                  

if __name__ == '__main__':
    clips = ('v1.mp4', 'v2.mp4','v3.mp4')
    VideoCut(clips)
