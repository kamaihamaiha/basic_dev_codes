import matplotlib.pyplot as plt
import matplotlib.animation as animation
import os
from populations import Populations

# change work dir
os.chdir("practice")
pops = Populations('cn_pop_last74_format.csv')



# 示例数据
years = pops.years
population = pops.totals

fig, ax = plt.subplots()
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
    annotation.set_text(f'Year: {years[i]}\nPopulation: {population[i]}\n Excludes HK, Macau, Taiwan\nSource: National Bureau of Statistics of China')

    
    return line, annotation

ani = animation.FuncAnimation(fig, animate, frames=len(years), init_func=init, blit=True, interval=100)

plt.show()