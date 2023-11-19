import re

import numpy as np

from tpltable.tablef import BookTableF
from tpltable.pipe import Pipe, pFunc
from tpltable.filefinder import tHWEXCEL_find

# Format In ----------------------------------
summery, _ = tHWEXCEL_find('')
fpaths = summery.tolist(summery.FPATH)
btf = BookTableF('a.xlsx')
print(btf.format)

all_data = []
for fpath in fpaths:
    all_data.append(btf.readf(fpath, simplify=False))

print(*all_data, sep='\n')
# exit(0)

# Pipe ----------------------------------
@pFunc('$fTIME')
def get_time(rname) -> str:
    _ = re.split(r'[：:]', rname)
    assert len(_) >= 1, f'can not split {rname}'
    return _[-1]

@pFunc('$fAUTHOR')
def get_name(rname) -> str:
    _ = re.split(r'[：:]', rname)
    assert len(_) >= 1, f'can not split {rname}'
    return _[-1]


@pFunc('$HW_NAME', '$HW_NAME$LINE_NAME')
def get_line_name(rname) -> (str, str):
    rname = re.sub(r'\s', '', rname)
    _ = re.findall(r'10[kK][vV]\w+线[\w#]+环网柜', rname)
    if not _:
        return rname, None
    _ = _[0]
    _ = _[4:-3]
    index = _.find('线')
    if index == -1:
        return rname, None
    return _[index + 1:], _[:index + 1]


def newline(rname) -> str:
    """
    为过长的目标自动换行
    :param rname:
    :return:
    """
    # 假定长度超过7的为过长,需要每7个字符换行
    if len(rname) < 7:
        return rname
    _ = []
    for i in range(0, len(rname), 7):
        _.append(rname[i:i + 7])
    return '\n'.join(_)


@pFunc()
def reshape(data: np.ndarray) -> np.ndarray:
    """
    对数据进行reshape,并清除空数据
    :param data: ndarray of dict
    :return:
    """
    data = data.reshape(-1)
    # 去除空{}数据
    data = data[data != {}]
    return data.reshape((-1, 1))


pipe = Pipe(btf.format)
pipe += get_name
pipe += get_time
pipe += get_line_name
pipe.add(newline, '$HW_DTU_ftNAME')
pipe.add(newline, '$HW_PROTECT_ftNAME')
pipe.add(newline, '$HW_ftNAME')
pipe += reshape
print(pipe.format)

new_data = None
for _dDict in all_data:
    for _data in _dDict.values():
        _ = pipe(_data)
        if new_data is None:
            new_data = _
        else:
            new_data = np.vstack((new_data, _))
if new_data is None:
    print('no any data found')
    exit(0)

# Format Out ----------------------------------
o_btf = BookTableF('c.xlsx')
o_btf.writef(new_data).save('d.xlsx')
