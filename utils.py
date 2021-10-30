import os, shutil, re, mimetypes, time, datetime, logging


#Make logging info
def log():
    filename="log/log_organized_file_"+datetime.datetime.now().strftime("%H:%M")+".log"
    logging.basicConfig(filename=filename,
                        format='%(asctime)s %(message)s',
                        filemode='w')
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    return logger


def get_all_info_file(old_dir):
    type_files = []
    dates_files = []
    fail_filee = []
    dir_origs = []
    logger  = log()
    print("Start: "+datetime.datetime.now().strftime("%H:%M:%S"))
    for root, dirs, files in os.walk(old_dir):
        try:
            for i in files:
                type_files.append(re.match("(.*?)/",mimetypes.guess_type(i)[0]).group(1))
                x = os.path.join(str(root),str(i))
                dir_origs.append(x)
                dates_files.append(time.strftime("%Y-%m",time.strptime(time.ctime(os.path.getctime(x)))))
        except:
            fail_filee.append(x)
            pass
    type_files = [i.replace('application','others') for i in type_files]
    print("End: "+datetime.datetime.now().strftime("%H:%M:%S"))
    return type_files ,    dates_files,    fail_filee ,    dir_origs


#Make dirs for date and type
#Make sure the is were dir have created to put your files is up(var new_dir)
def mk_dir_new(dates_files,type_files, new_dir):
    logger  = log()
    for i in zip(dates_files,type_files):
        x = os.path.join(new_dir,i[1],i[0])
        if not os.path.exists(x):
            os.makedirs(x)
            print("Directory " , x ,  " Created ")
        else:
            print("Directory " , x ,  " already exists")


#Copy file to dirs
def cp_file_to_new(dates_files,type_files,dir_origs,new_dir):
    logger  = log()
    print("Start: "+datetime.datetime.now().strftime("%H:%M:%S"))
    mk_dir_new(dates_files,type_files, new_dir)
    for i in zip(dates_files,type_files,dir_origs):
        dir_dest = os.path.join(new_dir,i[1],i[0])
        file_orig = i[2]
        shutil.copy2(file_orig,dir_dest)
    print(datetime.datetime.now().strftime("%H:%M:%S"))
    print("End...")
    input("Press Enter....")


