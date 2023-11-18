import sys


from .sc import SCError
from .Style import STYLE


def get_midse(_string, start_string, end_string):
    """
    返回 所有在start_string和end_string之间的字符串组成的list

    :param _string: 字符串

    :param start_string: 起始字符串

    :param end_string: 结束字符串

    :returns: list
    """

    if _string == "":
        raise SCError("字符串为空...", "请填充字符串")
    if start_string == '' or end_string == '':
        raise SCError("分隔符为空...", "请填充分隔符")

    start_index = 0
    result = []
    while True:
        start_index = _string.find(start_string, start_index)
        if start_index == -1:
            break
        start_index += len(start_string)
        end_index = _string.find(end_string, start_index)
        if end_index == -1:
            break
        substring = _string[start_index:end_index]
        result.append(substring)
        start_index = end_index + len(end_string)
    return result


def perr(Err: Exception, ExtraMsg: str= '',Bool_Proceed: bool|int=True):
    """
    简化报错, 默认 继续执行

    :param Bool_Proceed: 是否继续执行  [1继续执行 0退出程序]
    """

    except_type, except_value, except_traceback = sys.exc_info()
    except_file = except_traceback.tb_frame.f_code.co_filename
    except_line = except_traceback.tb_lineno

    errdict = {"报错-文件行数": f"{except_file}:{except_line}",
               "报错-类型信息": repr(except_type.__name__) + '  '+ repr(except_value)}
    if ExtraMsg:
        errdict["额外-信息提示"] = ExtraMsg
    for k, v in errdict.items():
        print(restrop(k, f=5), restrop(v))
    if not Bool_Proceed:
        exit()


def pic(Variable_name):
    """
    输出 变量名 | 变量类型 | 值

    :param name:str "变量名"
    """
    def RetrieveName(var): # 获取变量名称
        import inspect
        stacks = inspect.stack()
        try:
            callFunc = stacks[1].function
            code = stacks[2].code_context[0]
            startIndex = code.index(callFunc)
            startIndex = code.index("(", startIndex + len(callFunc)) + 1
            endIndex = code.index(")", startIndex)
            return code[startIndex:endIndex].strip()
        except:
            return ""

    try:
        str_vn = RetrieveName(Variable_name)
        print(restrop(str_vn), '|',
              restrop(type(Variable_name).__name__, f=5), '|',
              restrop(Variable_name, f=3))
    except Exception as err:
        raise SCError("变量未定义")


def restrop(text, m='', f=1, b=''):
    """
    mode       模式简记
    ------------------------------
    0默认-1高亮-4下滑-5闪烁-7泛白-8隐藏

    fore back  颜色简记
    ------------------------------
    0黑-1红-2绿-3黄-4蓝-5紫-6青-7灰

    :param text: str
    :param m: mode 模式
    :param f: fore 字体颜色
    :param b: back 背景颜色
    :return: str
    """
    try:
        str_mode = '%s' % STYLE['mode'][m] if STYLE['mode'][m] else ''
        str_fore = '%s' % STYLE['fore'][f] if STYLE['fore'][f] else ''
        str_back = '%s' % STYLE['back'][b] if STYLE['back'][b] else ''
    except Exception as err:
        raise SCError(err, "请检查参数输入")

    style = ';'.join([s for s in [str_mode, str_fore, str_back] if s])
    style = '\033[%sm' % style if style else ''
    end = '\033[%sm' % STYLE['default']['end'] if style else ''

    return '%s%s%s' % (style, text, end)
