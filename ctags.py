#!/usr/bin/env python
# coding: utf-8

import os
import sys


ctags = r'E:\Soft\ctags\bin\ctags.exe'
ignore = "__attribute_malloc__,__THROW,__THROWNL,__nonnull+,__wur,__attribute_pure__"
option = "--sort=yes --c-kinds=+pxlt --fields=+S -f.tags --extra=+fq -R "


def run(dirs):
    cmd = '{ctags} -I{ignore} {option}'.format(ctags=ctags, ignore=ignore, option=option)
    print(cmd)
    os.system(cmd)


def main():
    if (len(sys.argv) == 1):
        dirs = ['.']
    else:
        # 统一使用‘/’路径分隔符
        dirs = [os.path.abspath(e).replace('\\', '/') for e in sys.argv[1:]]
        dirs = ' '.join(dirs)

    run(dirs)

if __name__ == "__main__":
    main()
