import matplotlib.pyplot as plt
import matplotlib.animation as animation
import os
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


line, = ax.plot([], [], lw=2)
annotation = ax.text(0.3, 0.8, '', transform=ax.transAxes, fontsize=12, color='red')

def init():
    line.set_data([], [])
    annotation.set_text('')
    return line, annotation

def animate(i):
    x = years[:i+1]
    y = population[:i+1]
    line.set_data(x, y)
    annotation.set_text(f'Year: {years[i]}\nPopulation: {population[i]}\nExcludes HK, Macau, Taiwan\nSource: National Bureau of Statistics of China')

    
    return line, annotation


ani = animation.FuncAnimation(fig, animate, frames=len(years), init_func=init, blit=True, interval=200)
plt.show()

# # save the animation
# ani.save('cn_pop_anim.mp4', writer='ffmpeg')

# video = VideoFileClip("cn_pop_anim.mp4")
# # 获取最后一帧
# last_frame = video.to_ImageClip(video.duration - 0.01)

# # 创建停留的静态帧
# pause_duration = 2  # 停留时间（秒）
# pause_clip = last_frame.with_duration(pause_duration)

# # 合并视频和静态帧
# final_clip = concatenate_videoclips([video, pause_clip])
# # final_clip = CompositeVideoClip([video, pause_clip.set_start(video.duration)])


# # 保存最终视频
# final_clip.write_videofile("animation_with_pause.mp4", codec='libx264')

# # 合并视频和音频
# video = VideoFileClip("animation_with_pause.mp4")
# audio = AudioFileClip("sunrise_aigei_com.mp3")

# # 确保音频长度与视频一致
# audio = audio.subclipped(0, video.duration)

# # 将音频与视频合并
# video = video.with_audio(audio)

# # 保存合并后的视频
# video.write_videofile("animation_with_music.mp4", codec='libx264')

# plt.show()