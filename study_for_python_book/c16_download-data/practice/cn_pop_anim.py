import matplotlib.pyplot as plt
import matplotlib.animation as animation
import os
import time
from populations import Populations
from moviepy import VideoFileClip, AudioFileClip, concatenate_videoclips, CompositeVideoClip

# change work dir
os.chdir("practice")
pops = Populations('cn_pop_last74_format.csv')



# 示例数据
years = pops.years
population = pops.totals

fig, ax = plt.subplots(figsize=(10, 6))
year_display_start = years[0]
year_display_end = years[-1] + 6 # 8 is added to make the plot look better
ax.set_xlim(year_display_start, year_display_end) 
ax.set_ylim(0, max(population) + 30000) # 10000 is added to make the plot look better
ax.set_xlabel('Year')
ax.set_ylabel('Population (Ten Thousands)')
ax.set_title('China Population Over the Last 74 Years')
plt.xticks(range(year_display_start, year_display_end, 5)) # 5年一个刻度


line_total, = ax.plot([], [], lw=2, label='total')
line_urben, = ax.plot([], [], lw=2, label='citizen')
line_rural, = ax.plot([], [], lw=2, label='country')
annotation = ax.text(0.2, 0.9, '', transform=ax.transAxes, fontsize=12, color='blue')
annotation_urben = ax.text(0.2, 0.85, '', transform=ax.transAxes, fontsize=12, color='orange')
annotation_rural= ax.text(0.2, 0.8, '', transform=ax.transAxes, fontsize=12, color='green')
annotation_other= ax.text(0.2, 0.72, '', transform=ax.transAxes, fontsize=8, color='gray')

def init():
    line_total.set_data([], [])
    line_urben.set_data([], [])
    line_rural.set_data([], [])
    annotation.set_text('')
    annotation_urben.set_text('')
    annotation_rural.set_text('')
    annotation_other.set_text('')
    return line_total, line_urben, line_rural, annotation

def animate(i):
    end = i+1
    x = years[:end]
    y_total = population[:end]
    y_urben= pops.citizens[:end]
    y_rural= pops.countries[:end]
    line_total.set_data(x, y_total)
    line_urben.set_data(x, y_urben)
    line_rural.set_data(x, y_rural)
    annotation.set_text(f'Year: {years[i]}\nPopulation: {population[i]}')
    annotation_urben.set_text(f'urben population: {pops.citizens[i]}, {pops.citizens[i] * 100 / population[i]:.1f}%')
    annotation_rural.set_text(f'rural population: {pops.countries[i]}')
    annotation_other.set_text(f'Excludes HK, Macau, Taiwan\nSource: National Bureau of Statistics of China')

    
    return line_total, line_urben, line_rural, annotation, annotation_urben, annotation_rural, annotation_other


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
time.sleep(2)
add_bgm(video)

plt.show()