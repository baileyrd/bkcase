# -*- coding:cp936 -*-
'''
�ҵ�ԭʼĿ¼���ظ���

�����ļ�����ȷ����
�ϲ��ļ��У� xxx_20
��ǰ�ļ���, 146_xxx��146ת16���ƣ�Ϊ92��
���ַ������ӣ�
2092������Ϊ�ļ�����
'''
import os
import sys
from maplet_tools import get_sig_arr

inws = r'd:\maplet_dvk\MapPicDir'

all_arr = get_sig_arr(inws)


def finddupl(lst):
    """�ҳ� lst �����ظ�����
        (���ظ������޹أ������ظ�λ���޹�)
    """
    exists, dupl = set(), set()
    for item in lst:
        if item in exists:
            dupl.add(item)
        else:
            exists.add(item)
    return dupl


print('Result ----')
print(finddupl(all_arr))
