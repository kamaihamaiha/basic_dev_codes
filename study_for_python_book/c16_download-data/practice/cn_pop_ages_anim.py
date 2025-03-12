import matplotlib.pyplot as plt
import matplotlib.animation as animation
import os
import time
from populations_with_age import PopulationsWithAge
from moviepy import VideoFileClip, AudioFileClip, concatenate_videoclips, CompositeVideoClip

# change work dir
os.chdir("practice")
pops = PopulationsWithAge('docs/pop_with_ages-since-1990_format.csv')



# 示例数据
years = pops.years
population = pops.totals

fig, ax = plt.subplots(figsize=(10, 6))
year_display_start = years[0]
year_display_end = years[-1] + 2 # 8 is added to make the plot look better
ax.set_xlim(year_display_start, year_display_end) 
ax.set_ylim(0, max(population) + 30000) # 10000 is added to make the plot look better
ax.set_xlabel('Year')
ax.set_ylabel('Population (Ten Thousands)')
ax.set_title('China Population of different age groups Over the Last 34 Years')
plt.xticks(range(year_display_start, year_display_end, 5)) # 4年一个刻度


line_total, = ax.plot([], [], lw=2, label='total', color='gray')
line_young, = ax.plot([], [], lw=2, label='young', color='green')
line_middle, = ax.plot([], [], lw=2, label='middle', color='blue')
line_older, = ax.plot([], [], lw=2, label='older', color='black')
annotation_year = ax.text(0.4, 0.95, '', transform=ax.transAxes, fontsize=12, color='red')
annotation_young = ax.text(0.4, 0.9, '', transform=ax.transAxes, fontsize=12, color='green')
annotation_middle = ax.text(0.4, 0.85, '', transform=ax.transAxes, fontsize=12, color='blue')
annotation_older = ax.text(0.4, 0.8, '', transform=ax.transAxes, fontsize=8, color='black')
annotation_total= ax.text(0.4, 0.75, '', transform=ax.transAxes, fontsize=8, color='gray')

def init():
    line_total.set_data([], [])
    line_young.set_data([], [])
    line_middle.set_data([], [])
    line_older.set_data([], [])
    annotation_year.set_text('')
    annotation_young.set_text('')
    annotation_middle.set_text('')
    annotation_older.set_text('')
    annotation_total.set_text('')
    return line_total, line_young, line_middle, line_older, annotation_year, annotation_young, annotation_middle, annotation_older, annotation_total

def animate(i):
    end = i+1
    x = years[:end]
    y_total = population[:end]
    y_young= pops.youngs[:end]
    y_middle= pops.middles[:end]
    y_older= pops.olders[:end]
    line_total.set_data(x, y_total)
    line_young.set_data(x, y_young)
    line_older.set_data(x, y_older)
    line_middle.set_data(x, y_middle)
    annotation_year.set_text(f'Year: {years[i]}')
    annotation_young.set_text(f'0-14 years: {pops.youngs[i]}')
    annotation_middle.set_text(f'15-64 years: {pops.middles[i]}')
    annotation_older.set_text(f'65+ years: {pops.olders[i]}')
    annotation_total.set_text(f'total: {population[i]}')

    
    return line_total, line_young, line_middle, line_older, annotation_year, annotation_young, annotation_middle, annotation_older, annotation_total


anim = animation.FuncAnimation(fig, animate, frames=len(years), init_func=init, blit=True, interval=200)

def make_video():
    # save original video
    video_file = 'cn_pop_anim.mp4'
    anim.save(video_file, writer='ffmpeg')
    
    video = VideoFileClip(video_file)
    return video


def add_bgm(video):
    video_file = 'cn_pop_anim_with_bgm.mp4'
    audio = AudioFileClip('sunrise_aigei_com.mp3').subclipped(0, video.duration)    
    video = video.with_audio(audio)
    video.write_videofile(video_file, codec='libx264')

video = make_video()
# time.sleep(2)
add_bgm(video)

plt.show()