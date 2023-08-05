# -*- coding:utf-8 -*-
#
# Copyright (C) 2019-2020 Alibaba Group Holding Limited


import os
import sys
import pickle

from .tools import *
from .log import logger
from .yoc import YoC
from .builder import *

import warnings
warnings.filterwarnings("ignore", category=SyntaxWarning)

try:
    try:
        import SCons.Script as SCons
    except:
        import scons
        for path in scons.__path__:
            sys.path.append(path)
            import SCons.Script as SCons
except:
    scons_path = []
    for path in sys.path:
        if os.path.isdir(os.path.join(path, "scons")):
            scons_path.append(os.path.join(path, "scons"))
    if scons_path:
        sys.path += scons_path
        import SCons.Script as SCons


SCons.AddOption('--verbose', dest='verbose', default=True,
                action='store_false',
                help='verbose command line output')


SCons.AddOption('--board', dest='board', default=None,
                action='store', nargs=1, type='string',
                help='board component name')

class Make(object):
    def __init__(self, elf=None, objcopy=None, objdump=None):
        try:
            with open('.sconsign.dblite', "rb") as f:
                pickle.load(f)
        except ValueError:
            os.remove('.sconsign.dblite')
        except:
            pass

        board_name = SCons.GetOption('board')
        print_depends = False
        if not SCons.GetOption('verbose'):
            print_depends = True
        self.yoc = YoC()
        solution = self.yoc.getSolution(board_name, print_depends=print_depends)
        if solution:
            self.build_env = Builder(solution)
            self.build_env.env.AppendUnique(
                ELF_FILE=elf, OBJCOPY_FILE=objcopy, OBJDUMP_FILE=objdump)
            # self.build_env.env.AppendUnique(BOARD_NAME=board, CHIP_NAME=chip)
        else:
            self.build_env = None

    def library_yaml(self):
        package_file = self.build_env.env.GetBuildPath('package.yaml')
        conf = yaml_load(package_file)
        if conf and 'name' in conf:
            component = self.yoc.components.get(conf['name'])
            self.build_env.build_component(component)
            component.export()

    def build_component(self, component):
        new_file = False
        file_name = os.path.join(component.path, 'SConscript')
        if not os.path.exists(file_name):
            file_name = genSConcript(component.path)
            new_file = True
        if os.path.isfile(file_name):
            SCons.SConscript(file_name, exports={"env": self.build_env.env.Clone(
            )}, variant_dir='out/' + component.name, duplicate=0)
            if new_file:
                os.remove(file_name)

    def build_components(self, components=None):
        if self.build_env.env['PLATFORM'] == 'win32':
            self.build_env.env['SPAWN'] = win_longcmd_spawn
            put_string("install win_longcmd_spawn patch in windows.")
        if components != None:
            for c in components:
                component = self.yoc.components.get(c)
                if component:
                    self.build_component(component)
        else:
            for component in self.build_env.solution.components:
                self.build_component(component)

    def build_image(self, elf=None, objcopy=None, objdump=None, product=None):
        if self.build_env.env['PLATFORM'] == 'win32':
            self.build_env.env['SPAWN'] = win_longcmd_spawn
            put_string("install win_longcmd_spawn patch in windows.")
        self.build_env.build_image(elf, objcopy, objdump, product)

def win_longcmd_spawn(sh, escape, cmd, args, spawnenv):
    import win32file
    import win32event
    import win32process
    import win32security
    from SCons.Platform.win32 import spawn

    if cmd.startswith('arm-') or cmd.startswith('csky-') or cmd.startswith('riscv-'):
        #put_string("use win_longcmd_spawn patch for %s in windows." % cmd)
        newargs = ' '.join(args[1:])
        for p in spawnenv["PATH"].split(";"):
            exe_file = os.path.join(p, "%s.exe" % cmd)
            if os.path.isfile(exe_file):
                cmd = exe_file
                break
        cmdline = cmd + " " + newargs
        handle = win32process.CreateProcess(None, cmdline, None, None, 1, 0, spawnenv, None, win32process.STARTUPINFO())
        win32event.WaitForSingleObject(handle[0], win32event.INFINITE)
        exit_code = win32process.GetExitCodeProcess(handle[0])
        win32file.CloseHandle(handle[0])
        win32file.CloseHandle(handle[1])
    else:
        exit_code = spawn(sh, escape, cmd, args, spawnenv)
    return exit_code
