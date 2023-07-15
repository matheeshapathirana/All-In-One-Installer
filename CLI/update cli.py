import os
import os
import random
import shutil
import git
from datetime import datetime
from datetime import date

########################################################################################################################
import random
rand_number = random.randint(1, 99999)
########################################################################################################################
now = datetime.now()
current_time = now.strftime("%H_%M_%S")
time_now = (current_time)
today = date.today()

main_path = 'D:/OneDrive - adithya/Programming/Python/All-In-One-Installer/Bin'
is_main_path = os.path.isdir(main_path)
if is_main_path == True:
    second_path= 'D:/OneDrive - adithya/Programming/Python/All-In-One-Installer/Bin/Version'
    is_main
        f = open(f'D:/OneDrive - adithya/Programming/Python/All-In-One-Installer/Bin/Version/version.txt', 'w+')
        f.write('100')

else:
    os.mkdir('D:/OneDrive - adithya/Programming/Python/All-In-One-Installer/Bin')
    os.mkdir(f'D:/OneDrive - adithya/Programming/Python/All-In-One-Installer/Bin/Version')
    f = open(f'DD:/OneDrive - adithya/Programming/Python/All-In-One-Installer/Bin/Version/version.txt', 'w+')
    f.write('100')
