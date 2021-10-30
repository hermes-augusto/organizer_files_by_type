from utils import get_all_info_file, cp_file_to_new


def main():
    #Set vars with dir to organize
    old_dir = 'D:/Hermes-Augusto/Documents/test'
    new_dir = 'D:/Hermes-Augusto/Documents/organized'
    type_files , dates_files, fail_filee, dir_origs = get_all_info_file(old_dir)
    cp_file_to_new(dates_files,type_files,dir_origs,new_dir)


if __name__ == '__main__':
    main()
