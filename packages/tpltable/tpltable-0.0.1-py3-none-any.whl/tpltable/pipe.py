import re
import warnings
from typing import Callable, Union

import numpy as np


class _PipeB:
    """
    这是一个处理单个数据ndarray的pipe,目的是挂载多个处理函数,并且可以按照顺序执行
    但是注意,不会改变数据的维度,也不会改变数据的shape
    """

    InK_ATTR = "_tpltable_Pipe_in_keys"
    OutK_ATTR = "_tpltable_Pipe_out_keys"
    RpK_ATTR = "_tpltable_Pipe_replace"
    Rn_ATTR = "_tpltable_Pipe_raw_name"

    def __init__(self, format: list, warn: bool = False):
        """

        :param format: list, 格式为: ["$XXX": str, ...]
        :param warn: bool, 是否开启警告
        """
        self._input_format = format
        self.__funcs = []
        self._build_last_format = format.copy()

        self._warn = warn

    @staticmethod
    def _careful_split(s):
        """
        严格的按照$分割字符串,要求$后必须有字符.
        例如:
            $a$b -> ["$a", "$b"]
            $a$$b -> Raise ValueError
            $a -> ["$a"]
            '' -> []
        :param s:
        :return:
        """
        _ = re.findall(r'\$[^\$]+', s)
        # 检查能否还原
        _s = ''.join(_)
        if _s != s:
            raise ValueError(f"Unexpected string: {s} (Maybe you mean: {_s} ?)")
        # END Check

        return _

    @staticmethod
    def _as_func(func, in_keys: Union[list, tuple, str], out_keys: Union[list, tuple, str], replace: bool):
        if isinstance(in_keys, str):
            in_keys = _PipeB._careful_split(in_keys)
        if isinstance(out_keys, str):
            out_keys = _PipeB._careful_split(out_keys)
        if in_keys is None:
            in_keys = []
        if out_keys is None:
            out_keys = in_keys.copy()

        _raw_func_name = func.__name__

        def wrapped_func(*args, **kwargs):
            return func(*args, **kwargs)

        setattr(wrapped_func, _PipeB.Rn_ATTR, _raw_func_name)
        setattr(wrapped_func, _PipeB.InK_ATTR, in_keys)
        setattr(wrapped_func, _PipeB.OutK_ATTR, out_keys)
        setattr(wrapped_func, _PipeB.RpK_ATTR, replace)
        return wrapped_func

    @staticmethod
    def Func(in_keys: Union[list, tuple, str] = None, out_keys: Union[list, tuple, str] = None, replace=False) -> Callable:
        """
        将目标函数装饰成一个Pipe可以直接使用的函数
        这种处理函数必须返回简单类型或是(list, tuple)[简单类型]
        :param in_keys:
        :param out_keys:
        :param replace: bool, 是否用输出的目标名称替换输入的目标名称
        :return:
        """

        def _inner(func):
            return _PipeB._as_func(func, in_keys, out_keys, replace)

        return _inner

    def _add_into(self, func):
        if not hasattr(func, self.InK_ATTR) or not hasattr(func, self.OutK_ATTR) or not hasattr(func, self.RpK_ATTR):
            raise TypeError("The function must be decorated by Pipe.Func or use Pipe.add to add it")

        in_keys = getattr(func, self.InK_ATTR)
        out_keys = getattr(func, self.OutK_ATTR)
        for k in in_keys:
            if not k.startswith("$"):
                raise ValueError(f"the {getattr(func, _PipeB.Rn_ATTR, func.__name__)}.in_keys: '{k}' must be startswith '$'")
            if k not in self._build_last_format:
                raise ValueError(
                    f"the {getattr(func, _PipeB.Rn_ATTR, func.__name__)} need a key {k}, but not in last layer output format: {self._build_last_format}")

        for k in out_keys:
            if not k.startswith("$"):
                raise ValueError(f"the {getattr(func, _PipeB.Rn_ATTR, func.__name__)}.out_keys: '{k}' must be startswith '$'")

        self._build_last_format = self._induce_format(self._build_last_format, [func], self._warn)
        self.__funcs.append(func)

    def add(self, func, in_keys: Union[list, tuple, str] = None, out_keys: Union[list, tuple, str] = None, replace=False):
        """
        添加一个处理函数, 这种处理函数必须返回简单类型或是(list, tuple)[简单类型]
        :param func: 用于处理数据的函数, 要求函数的形参数量与in_keys的长度一致, 返回值的数量与out_keys的长度一致
        :param in_keys: 函数关注的目标名称, like: $XXX, ...
        :param out_keys: 函数输出的目标名称, like: $XXX, ...
            out_keys=None, 表示输出的目标名称和输入的目标名称一致
        :param replace: bool, 是否用输出的目标名称替换输入的目标名称
        :return:
        """

        func = self._as_func(func, in_keys, out_keys, replace)
        self._add_into(func)

    def __iadd__(self, other):
        """
        重载 += 操作符, 用于添加一个处理函数
        :param other:
        :return:
        """
        self._add_into(other)
        return self

    def __call__(self, data: np.ndarray) -> np.array:
        """
        执行pipe
        根据pipe中添加的函数, 依次执行. 根据目标函数的InK_ATTR, 从data中取出数据; 根据目标函数的OutK_ATTR和返回值, 将数据写入data
        :param data: ndarray of dict {"$XXX": str}
        :return: new data
        """
        if not isinstance(data, np.ndarray):
            raise TypeError("The data must be a ndarray of dict {'$XXX': str}")
        if data.ndim != 2:
            raise ValueError("The ndarr must be a 2d array")
        yCnt, xCnt = data.shape

        # ----------------------- unpack ndarr ----------------------- #
        for ix in range(yCnt):
            for iy in range(xCnt):
                fdata = data[ix, iy]
                if not isinstance(fdata, dict):
                    raise TypeError("The data must be a ndarray of dict {'$XXX': str}")
                if not fdata:  # ignore empty dict
                    continue

                for func in self.__funcs:
                    in_keys = getattr(func, self.InK_ATTR)
                    out_keys = getattr(func, self.OutK_ATTR)
                    replace = getattr(func, self.RpK_ATTR)
                    fname = getattr(func, self.Rn_ATTR, func.__name__)
                    # ----------------------- check > ----------------------- #
                    assert in_keys is not None and isinstance(in_keys,
                                                              (list,
                                                               tuple)), f"the {getattr(func, _PipeB.Rn_ATTR, func.__name__)} must have a {self.InK_ATTR} attribute"

                    if not in_keys:
                        continue
                    if out_keys is None:
                        out_keys = [_ for _ in in_keys]
                    # ----------------------- End check ----------------------- #

                    # in_data = [(fdata.pop(k) if replace else fdata[k]) for k in in_keys]
                    in_data = []
                    for k in in_keys:
                        if k not in fdata:
                            raise ValueError(f"the {getattr(func, _PipeB.Rn_ATTR, func.__name__)} need a key {k}, but not in data: {fdata}")
                        if replace:
                            in_data.append(fdata.pop(k))
                        else:
                            in_data.append(fdata[k])
                    # 检查None, 替换为''
                    for i, v in enumerate(in_data):
                        if v is None:
                            in_data[i] = ''

                    # 执行函数
                    out_data = func(*in_data)
                    if len(out_keys) == 1:
                        out_data = [out_data]
                    if not isinstance(out_data, (list, tuple)):
                        raise ValueError(f"the {getattr(func, _PipeB.Rn_ATTR, func.__name__)} must return a list or tuple. But got {out_data}")
                    if len(list(out_data)) != len(out_keys):
                        raise ValueError(
                            f"the {getattr(func, _PipeB.Rn_ATTR, func.__name__)} must return {len(out_keys)} values. But got {out_data}")

                    for out_k, v in zip(out_keys, out_data):
                        if out_k in fdata and self._warn:
                            # warn
                            warnings.warn(f"the {getattr(func, _PipeB.Rn_ATTR, func.__name__)} will overwrite the {out_k} in data")
                        fdata[out_k] = v

                data[ix, iy] = fdata

        # ----------------------- final adjustment ndarr ----------------------- #
        new_data = data
        for func in self.__funcs:
            in_keys = getattr(func, self.InK_ATTR)
            if in_keys:
                continue  # Only func without in_keys can adjust the total data
            out_keys = getattr(func, self.OutK_ATTR)
            if out_keys and self._warn:
                warnings.warn(f"the {getattr(func, _PipeB.Rn_ATTR, func.__name__)} will change the hole data but has out_keys. Will Ignore")

            # 执行函数
            out_data = func(np.array(new_data))
            if not isinstance(out_data, np.ndarray):
                raise ValueError(f"the {getattr(func, _PipeB.Rn_ATTR, func.__name__)} must return a ndarray. But got {out_data}")
            if out_data.ndim != 2 and self._warn:
                warnings.warn(f"the {getattr(func, _PipeB.Rn_ATTR, func.__name__)} need return a 2d ndarray. But got {out_data.ndim}d ndarray")
            new_data = out_data

        if new_data.ndim != 2:
            raise ValueError(
                "The pipe-out ndarr must be a 2d array. If only got this msg, please turn on the warn by use warn=True to see where is wrong")

        return new_data

    @staticmethod
    def _induce_format(input_format: list, funcs, warn):
        """
        根据funcs中的函数, 推断出输出的格式
        :param input_format: ["$XXX", ...]
        :param funcs:
        :param warn: bool, 是否开启警告
        :return:
        """
        input_format = input_format.copy()
        for func in funcs:
            in_keys = getattr(func, _PipeB.InK_ATTR)
            out_keys = getattr(func, _PipeB.OutK_ATTR)
            replace = getattr(func, _PipeB.RpK_ATTR)
            assert in_keys is not None and isinstance(in_keys,
                                                      (list,
                                                       tuple)), f"the {getattr(func, _PipeB.Rn_ATTR, func.__name__)} must have a {_PipeB.InK_ATTR} attribute"
            if out_keys is None:
                out_keys = [_ for _ in in_keys]

            if replace:
                for k in in_keys:
                    if k not in input_format:
                        raise ValueError(
                            f"the {getattr(func, _PipeB.Rn_ATTR, func.__name__)} need a key {k}, but not in last layer output format: {input_format}")
                    else:
                        input_format.remove(k)
            if in_keys:
                for k in out_keys:
                    if k in input_format and warn:
                        # warn
                        warnings.warn(f"the {getattr(func, _PipeB.Rn_ATTR, func.__name__)} will overwrite the {k} in data")
                    input_format.append(k)
            elif out_keys and warn:
                warnings.warn(f"the {getattr(func, _PipeB.Rn_ATTR, func.__name__)} will change the hole data but has out_keys. Will Ignore")

        return input_format

    @property
    def input_format(self):
        """
        获取pipe的输入的格式
        :return:
        """
        return self._input_format

    @property
    def format(self):
        """
        获取pipe的输出的格式
        自动根据__funcs中的函数, 推断出输出的格式
        :return:
        """
        return self._induce_format(self._input_format, self.__funcs, self._warn)


class Pipe(_PipeB):
    ...


pFunc = Pipe.Func  # 装饰器: 将目标函数装饰成一个Pipe可以直接使用的函数

if __name__ == '__main__':
    fmt = ['$a', '$b']
    pipe = Pipe(fmt)
    pipe.add(lambda a, b: (b, a + b), ['$a', '$b'], ['$a', '$add'])
    pipe.add(lambda a, b: a - b, ['$a', '$b'], ['$sub'])
    pipe.add(lambda a, b: a * b, ['$a', '$b'], ['$mul'])
    pipe.add(lambda a, b: a / b, ['$a', '$b'], ['$div'])
    print(pipe.format)
    # -------------------------------->
    # data:
    data = np.array([
        [{'$a': 1, '$b': 2}, {'$a': 3, '$b': 4}],
        [{'$a': 5, '$b': 6}, {'$a': 7, '$b': 8}]
    ])
    print(data, '\n----------------------------------------------------')
    odata = pipe(data)
    print(odata)
