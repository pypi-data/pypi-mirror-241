import pickle,os


def save(fn,obj):
    with open(fn,'wb+') as f:
        pickle.dump(obj,f)


def load(fn):
    with open(fn,'rb') as f:
        return pickle.load(f)


def make_bin_number(*args):
    bin_string = ''
    for arg in args:
        if arg:
            bin_string += '1'
        else:
            bin_string += '0'
    return int(bin_string,2)


def repair_safe_file(fn,weak = True):
    fn_tmp = fn + '.tmp'
    fn_bak = fn + '.bak'
    fn_exist = os.path.exists(fn)
    fn_tmp_exist = os.path.exists(fn_tmp)
    fn_bak_exist = os.path.exists(fn_bak)
    solution_num = make_bin_number(fn_exist, fn_tmp_exist, fn_bak_exist)
    if weak:
        if solution_num == 7:
            os.remove(fn)
            os.remove(fn_tmp)
            os.remove(fn_bak)
        elif solution_num == 0 or solution_num == 4:
            pass
        elif solution_num == 1:
            os.remove(fn_bak)
        elif solution_num == 2:
            os.remove(fn_tmp)
        elif solution_num == 3:
            # 4. Rename x.y.tmp to x.y
            os.rename(fn_tmp, fn)
            # 5. Delete x.y.bak
            os.remove(fn_bak)
        elif solution_num == 5:
            os.remove(fn_bak)
        elif solution_num == 6:
            os.remove(fn_tmp)
    else:
        if solution_num != 4 or solution_num != 0 :
            if fn_exist:
                os.remove(fn)
            if fn_tmp_exist:
                os.remove(fn_tmp)
            if fn_bak_exist:
                os.remove(fn_bak)
    return solution_num


def safe_save(fn,obj):
    fn_tmp = fn + '.tmp'
    fn_bak = fn + '.bak'
    fn_exist = os.path.exists(fn)
    #fn_tmp_exist = os.path.exists(fn_tmp)
    #fn_bak_exist = os.path.exists(fn_bak)
    #solution_num = make_bin_number(fn_exist, fn_tmp_exist, fn_bak_exist)

    if fn_exist:
        # 1. 原始文件x.y
        pass
        # 2. 新文件写入x.y.tmp
        save(fn_tmp,obj)
        # 3. Rename x.y to x.y.bak
        os.rename(fn,fn_bak)
        # 4. Rename x.y.tmp to x.y
        os.rename(fn_tmp,fn)
        # 5. Delete x.y.bak
        os.remove(fn_bak)
        return True
    else:
        # 1. 写入x.y.tmp
        save(fn_tmp,obj)
        # 2. 改名 x.y
        os.rename(fn_tmp,fn)
        return True


def safe_load(fn):
    fn_tmp = fn+'.tmp'
    fn_bak = fn+'.bak'
    fn_exist = os.path.exists(fn)
    fn_tmp_exist = os.path.exists(fn_tmp)
    fn_bak_exist = os.path.exists(fn_bak)
    solution_num = make_bin_number(fn_exist,fn_tmp_exist,fn_bak_exist)
    if solution_num == 7 or solution_num == 1:
        print('Error: 不符合安全存储协议')
        return None
    if solution_num == 0:
        print('Error: 未找到文件或不符合安全存储协议')
        return None
    if solution_num == 2:
        os.remove(fn_tmp)
        print('Error: 不能安全读取，文件可能未写完')
        return None
    if solution_num == 3:
        # 4. Rename x.y.tmp to x.y
        os.rename(fn_tmp,fn)
        # 5. Delete x.y.bak
        os.remove(fn_bak)
        return load(fn)
    if solution_num == 4:
        return load(fn)
    if solution_num == 5:
        # 5. Delete x.y.bak
        os.remove(fn_bak)
        return load(fn)
    if solution_num == 6:
        os.remove(fn_tmp)
        return load(fn)


