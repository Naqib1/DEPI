def File_Read(fname):
    with open(fname) as f:
        content_list=f.readline()
        print(content_list)


