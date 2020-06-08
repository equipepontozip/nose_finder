print('Loading Libraries')
import time 
import utilities.tools as utils
from utilities.nose_recognition import NoseFinder
import os

print('Starting Nose Finder')

starting_time = time.clock()
directory = './bread_pictures/'
counter = 0

for filename in os.listdir(directory):
    if filename.endswith(".jpg"): 
        print('processing nariguin')
        name = 'nariguin_%s.png'%(counter)
        try:
            NoseFinder( os.path.join(directory, filename) )._saveCroppedImage( name )
            print('nariguin ',name,' processed')
            counter += 1
        except:
            print('nariguin not found')

utils.final_message()
final_time = time.clock() - starting_time
print("Time elapsed: ", final_time) # CPU seconds elapsed (floating point)
