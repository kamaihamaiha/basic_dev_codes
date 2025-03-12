import os
from populations import Populations
from populations_with_age import PopulationsWithAge


# change work dir
# os.chdir("practice")

# pops = Populations('cn_pop_last74_format.csv')   
# pops.draw_figure()        
# 

pops = PopulationsWithAge('docs/pop_with_ages-since-1990_format.csv')  
pops.draw_figure()