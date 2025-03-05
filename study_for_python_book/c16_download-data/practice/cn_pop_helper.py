import os
from populations import Populations


# change work dir
os.chdir("practice")

pops = Populations('cn_pop_last74_format.csv')   
pops.draw_figure()          