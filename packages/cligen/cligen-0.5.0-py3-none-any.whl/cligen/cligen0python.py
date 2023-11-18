
from __future__ import annotations


import sys
import pprint
import datetime
import shutil
from dataclasses import dataclass, field, MISSING
import inspect
from typing import Optional
from itertools import chain
from textwrap import dedent

import ruamel.yaml

from cligen.cligen import CliGenBase, VERSION, PKG_DATA, quoted
from . import __version__

_pregen = """\
# coding: utf-8
# flake8: noqa
# cligen: {version}, dd: {today}, args: {args}

from __future__ import annotations

{imports}
from typing import Optional, List, ClassVar, Any, Union, Callable
from dataclasses import dataclass, MISSING, field, fields, asdict, InitVar\
{verimp}

@dataclass
class HelpState:
    max_help_position: int = 30
    indent_level: int = 0
    spaces_per_indent: int = 2
    stack: list[int, str] = field(default_factory=list)
    out: Any = sys.stdout
    columns: int = shutil.get_terminal_size().columns

    def write(self, parser, s=None, indent=None):
        if indent is None:
            indent = self.indent_level * self.spaces_per_indent
        if indent:  
            self.out.write(' ' * indent)
        if s is None:
            assert len(self.stack) > 0, 'stack empty while trying to write'
            s = self.stack.pop()
        self.out.write(s)
        self.out.flush()

    def write_nl(self, parser, s=None, indent=None):
        self.write(parser=parser, s=s, indent=indent)
        self.out.write('\\n')

    def expand(self, parser):
        self.stack[-1] = self.stack[-1].format(pd=parser)

    def write_options(self, parser):
        assert len(self.stack) > 1, 'should have at least two strings on stack'
        while len(self.stack) > 1:
            s0 = self.stack.pop(0)
            s1 = self.stack.pop(0)
            if len(s1) == 0:
                self.write_nl(parser, s0)
                continue
            indent_cols = self.indent_level * self.spaces_per_indent
            s1 = s1.format(pd=parser)
            lines = []
            for paragraph in s1.splitlines():
                lines.extend(textwrap.wrap(paragraph, width=self.columns-(self.max_help_position+2)))
            if len(s0) + indent_cols + 2 >= self.max_help_position:
                 self.write_nl(parser, s0)
                 self.write_nl(parser, lines[0], indent=self.max_help_position)
            else:
                self.write_nl(parser, f'{{s0:<{{self.max_help_position-indent_cols}}s}}{{lines[0]}}')
            for line in lines[1:]:
                self.write_nl(parser, line, indent=self.max_help_position)

    def indent(self, parser):
        self.indent_level += 1

    def dedent(self, parser):
        self.indent_level -= 1
        assert self.indent_level >= 0, 'negative indent'

    # def set_max_help_position(self):
    #     assert len(self.stack) > 0, 'stack empty while trying to write'
    #     assert isinstance(self.stack[-1], int)
    #     self.max_help_position = self.stack.pop()

    def push(self, n):
        self.stack.append(n)


@dataclass
class BaseParser:
    _option_argument: InitVar[Optional[Any]] = None
    _prog_name: ClassVar[Optional[str]] = None
    _help_global: ClassVar[list[Union[Callable[[Any], None], str]]] = [{help_states}
    ]
    # help_data: list[int] = field(default_factory=list)

    # def add_str(self, s):
    #     self._help_global.append(s)
    #     return len(self._help_global) - 1

    def help(self, args, arg_idx):
        help_state = HelpState()
        for x in self.help_nrs:
            nxt = BaseParser._help_global[x]
            if isinstance(nxt , str):
                help_state.push(nxt)
            else:
                assert isinstance(nxt, Callable)
                nxt(help_state, self)
        sys.exit(0)

    def parse(self, args: List[str], arg_idx: List[int], data: Optional[dict]=None) -> BaseParser:
        raise NotImplementedError
        return self

    def long_token(self, token: str, args: list[str], arg_idx: list[int]) -> (str, Union[None, str]):
        token = token[2:]
        if '=' in token:
            token, self._option_argument = token.split('=', 1)
        elif arg_idx[0] < len(args):
            self._option_argument = args[arg_idx[0]]
        else:
            self._option_argument = None
        return token

    def optarg(self, x, args: List[str], arg_idx : List[int]) -> None:
        if self._option_argument is not None:
            arg_idx[0] += 1
            return self._option_argument
        print(f"missing argument for option {{'--' if len(x) > 1 else '-'}}{{x}}")
        sys.exit(1)

    def short_arg(self, args: List[str], arg_idx : List[int]) -> None:
        char_idx = arg_idx[1]
        if (char_idx + 1) == len(args[arg_idx[0]-1]):
            # it is the last character, so take next argument
            try:
                return self.next_arg(args, arg_idx)
            except IndexError:
                self._option_argument = None
                self.optarg(args[arg_idx[0]-2][arg_idx[1]])
        return args[arg_idx[0]-1][char_idx+1:]

    def next_arg(self, args: List[str], arg_idx : List[int], optarg: Optional[str] = None) -> None:
        if optarg is not None:
            return optarg
        cur_idx = arg_idx[0]
        arg_idx[0] += 1
        return args[cur_idx]

    def sub(self, p):
        for x, val in asdict(p).items():
            setattr(self, x, val)
        return self

    def error(self, args: List[str], arg_idx : List[int]) -> None:
        print('problem parsing', args[arg_idx[0]-1])
        raise ValueError

    def check(self):
        pass

    def check_narg(self, name, val, range):
        length = 0 if val is None else len(val)
        low = range[0]
        high = range[1] if range[1] >= low else sys.maxsize
        if range[1] >= low:
            if low <= length <= high:
                return
            print(f'number of arguments for {{name!r}} not in range ({{low}} <= {{length}} <= {{high}})')
            sys.exit(1)
        else:
            if length < low:
                print(f'number of arguments ({{length}}) for {{name!r}} should be at least {{low}})')
                sys.exit(1)

    @property
    def prog(self):
        return BaseParser._prog_name if BaseParser._prog_name is not None else os.path.basename(sys.argv[0])
"""

_list_versions = """\
def list_versions(pkg_name: str, version: typing.Union[str, None], pkgs: typing.Sequence[str]) -> int:
    version_data = [
        ('Python', '{v.major}.{v.minor}.{v.micro}'.format(v=sys.version_info)),
        (pkg_name, __version__ if version is None else version),
    ]
    for pkg in pkgs:
        try:
            version_data.append(
                (pkg,  getattr(importlib.import_module(pkg), '__version__', '--'))
            )
        except ModuleNotFoundError:
            version_data.append((pkg, 'NA'))
        except KeyError:
            pass
    longest = max([len(x[0]) for x in version_data]) + 1
    for pkg, ver in version_data:
        print('{:{}s} {}'.format(pkg + ':', longest, ver))
    return 0

"""

_postgen = """\

if __name__ == '__main__':
    sys.exit(main())
"""

@dataclass
class PData:
    path: list[str]
    parent: Optional[PData] = None
    subparsers: list[PData] = field(default_factory=list)
    options: list[Option] = field(default_factory=list)
    arguments: list[Option] = field(default_factory=list)
    default_subparser: Optional[PData] = None
    description: Optional[str] = None
    help: Optional[str] = None
    epilog: Optional[str] = None

    def add_optarg(self, optargs):
        for oa in optargs:
            if oa.is_arg:
                self.arguments.append(oa)
            else:
                self.options.append(oa)

    @property
    def name(self):
        if self.path:
            return self.path[-1]
        return ''

    @property
    def class_name(self):
        return ''.join([sp.capitalize() for sp in self.path] + ['CmdParser'])

    def gen_parser_names_recursive(self, data=[]):
        data.append(self.class_name)
        for sp in self.subparsers:
            sp.gen_parser_names_recursive(data)
        return data

    def all_options(self, local_first=False):
        if local_first:
            for opt in self.options:
                yield opt
        if self.parent:
            for opt in self.parent.all_options(local_first=local_first):
                if opt.is_global:
                    yield opt
        if not local_first:
            for opt in self.options:
                yield opt


@dataclass
class Option:
    long_opts: list[str] = field(default_factory=list)
    short_opts: list[str] = field(default_factory=list)
    help: Optional[str] = None
    typ: str = 'str'
    action: Optional[str] = None
    target: Optional[str] = None
    default: Any = None
    nargs: Optional[tuple[int, int]] = None
    const: Optional[Any] = None
    is_arg: bool = False
    is_global: bool = True

WRITE = 0
WRITE_LN = 1
WRITE_OPTIONS = 2
EXPAND = 3
INDENT = 4
DEDENT = 5

class CliGen0Python(CliGenBase):
    def __init__(
        self,
        data,
        verimp_file=None,
        extend_main=None,
        pkg_data=None,
        debug=False,  # if True insert debug = print
        comment=False,
        loader=None,
    ):
        super().__init__(
            data,
            verimp_file=verimp_file,
            extend_main=extend_main,
            pkg_data=pkg_data,
            debug=debug,
            comment=comment,
            loader=loader,
        )
        self._prl = None
        self._actions = self.load_actions(dir='action_p', comment=comment)
        self._actions_used = set()
        self._configs = self.load_configs(dir='config_p', comment=comment)
        self._configs_used = []
        self._imports = set(['', 'sys', 'os', 'shutil', 'textwrap', 'importlib'])
        self._pdata = None
        self._help_states: list[str] = [
            'HelpState.write',
            'HelpState.write_nl',
            'HelpState.write_options',
            'HelpState.expand',
            'HelpState.indent',
            'HelpState.dedent',
        ]

    def uncomment(self, s):
        """
        remove lines that are commented out, unless the start with ## then remove one
        of the hashes and insert the comment in the output
        do not strip the lines
        """
        if self._comment:
            return s
        lines = []
        for line in s.splitlines(True):
            if not (lls := line.lstrip()).startswith('#'):
                lines.append(line)
                continue
            if len(lls) > 1 and lls[1] == '#':
                lines.append(line.replace('##', '#', 1))
        return ''.join(lines)

    def add_help_state(self, s):
        try:
            idx = self._help_states.index(s)
        except ValueError:
            idx = len(self._help_states)
            # print('adding state', idx, repr(s))
            self._help_states.append(s)
        return idx

    def gen_parser(self, data=None, fp=sys.stdout, base_indent=4):
        def gen_parsed_data(data, path, parent=None):
            # could attach data to pd as well if needed
            pd = PData(path, parent=parent)
            kws, optargs, sub_parsers = self.get_kw(data, pdata=pd)
            for attr in ['help', 'description', 'epilog']:
                if attr in kws:
                    setattr(pd, attr, kws[attr])
            pd.add_optarg(optargs)
            for subparser in sub_parsers:
                sp_name, subparser_data = list(subparser.items())[0]
                # multiple sub commands cannot mutate path itself with append
                npath = path.copy()
                npath.append(sp_name)
                res = gen_parsed_data(subparser_data, path=npath, parent=pd)
                pd.subparsers.append(res)
            return pd

        if data is None:
            data = self._data
        path = []
        # so pre_gen and post_gen can get at it
        self._pdata = gen_parsed_data(data, path)
        # print(f'{self._pdata=}')
        # pprint.pprint(self._pdata, width=shutil.get_terminal_size()[0])
        self.gen_one_parser(self._pdata, fp=fp, base_indent=base_indent)

    def generate_help(self, pd, fp=sys.stdout, base_indent=4):
        # generate help by inserting (new) strings and concatenating indices
        bi = ' ' * base_indent
        usage = 'usage: {pd.prog}'
        if pd.parent:
            usage += ' ' + pd.name
        usage += ' [-h]'
        for oa in pd.all_options(local_first=True):
            if oa.typ == 'str':
                target = ' ' + oa.target.upper()
            else:
                target = ''
            if oa.long_opts:
                usage += f' [--{oa.long_opts[0]}{target}]'
            else:
                usage += f' [-{oa.short_opts[0]}{target}]'
        if pd.parent is None:
            usage += ' [--version]'
        help_nrs = [self.add_help_state(usage), EXPAND, WRITE_LN]
        if pd.subparsers:
            args = '{' + ','.join([sp.name for sp in pd.subparsers]) + '} ...'
            help_nrs.extend([
                INDENT, INDENT, INDENT, INDENT, INDENT,
                self.add_help_state(args), WRITE_LN,
                DEDENT, DEDENT, DEDENT, DEDENT, DEDENT,
            ])
        help_nrs.extend([self.add_help_state(''), WRITE_LN])
        if pd.description is not None:
            help_nrs.extend([self.add_help_state(pd.description), WRITE_LN])
            help_nrs.extend([self.add_help_state(''), WRITE_LN])
        if pd.subparsers:
            help_nrs.extend([self.add_help_state('sub-comamnds:'), WRITE_LN])
            help_nrs.append(INDENT)
            for sp in pd.subparsers:
                h = '' if sp.help is None else sp.help
                help_nrs.extend([self.add_help_state(sp.name), self.add_help_state(h)])
            help_nrs.append(WRITE_OPTIONS)
            help_nrs.append(DEDENT)
            help_nrs.extend([self.add_help_state(''), WRITE_LN])

        first_time = True
        help_nrs.extend([self.add_help_state('positional arguments:'), WRITE_LN])
        help_nrs.append(INDENT)
        for arg in pd.arguments:
            if first_time:
                first_time = False
            h = '' if arg.help is None else arg.help
            if self._add_defaults is not None and arg.typ not in ['bool']:
                # don't specify a type even if we know ao.typ
                h += self._add_defaults % (dict(default=f'{{pd.{arg.target}!r}}'))
            help_nrs.extend([self.add_help_state(arg.long_opts[0]), self.add_help_state(h)])
        if not first_time:
            help_nrs.append(WRITE_OPTIONS)
            help_nrs.append(DEDENT)
            help_nrs.extend([self.add_help_state(''), WRITE_LN])


        help_nrs.append(INDENT)
        help_nrs.extend([
            self.add_help_state('-h, --help'),
            self.add_help_state('show this help message and exit'),
        ])
        for oa in pd.all_options(local_first=True):
            if oa.typ == 'str':
                target = ' ' + oa.target.upper()
            else:
                target = ''
            ops = []
            for lo in oa.long_opts:
                ops.append(f'--{lo}{target}')
            for so in oa.short_opts:
                ops.append(f'-{so}{target}')
            if ops:
                h = '' if oa.help is None else oa.help
                if self._add_defaults is not None and oa.typ not in ['bool']:
                    # don't specify a type even if we know ao.typ
                    h += self._add_defaults % (dict(default=f'{{pd.{oa.target}!r}}'))
                help_nrs.extend([self.add_help_state(', '.join(ops)), self.add_help_state(h)])

        if pd.parent is None:
            help_nrs.extend([
                self.add_help_state('--version'),
                self.add_help_state('show program\'s version number and exit'),
            ])
        help_nrs.append(WRITE_OPTIONS)
        help_nrs.append(DEDENT)

        print(f'{bi}help_nrs: ClassVar(list[int]) = {help_nrs}', file=fp)

    def gen_one_parser(self, parsed_data, fp=sys.stdout, base_indent=4):
        bi = ' ' * base_indent
        pd = parsed_data
        if self._prl is None:
            self._prl = ' | '.join(pd.gen_parser_names_recursive())

        print(f'\n\n@dataclass', file=fp)
        pcn = pd.parent.class_name if pd.parent is not None else 'BaseParser'
        print(f'class {pd.class_name}({pcn}):', file=fp)
        if pd.path:
            print(f"{bi}_name: ClassVar[str] = '{'.'.join(pd.path)}'", file=fp)

        # generate attribute info
        for oa in chain(pd.options, pd.arguments):
            # don't generate attributes for parent class, they will be copied by sub()
            typ = oa.typ
            if oa.nargs is not None:
                default = 'field(default_factory=list)'
            elif oa.default is None and typ == 'int':
                default = 0
            elif oa.default is None and typ in self._actions:
                default = self._actions[typ]['params'].get('default')
                typ = self._actions[typ]['params'].get('type', typ)
            else:
                if oa.typ == 'str':
                    default = repr(oa.default)
                else:
                    default = oa.default
            if oa.nargs is not None:
                typ = f'list[{typ}]'
            elif default is None:
                typ = f'Optional[{typ}]'
            print(f'{bi}{oa.target}: {typ} = {default}', file=fp)

        self.generate_help(pd, fp=fp, base_indent=4)

        default_sub_parser = None
        # for subparser in self.sub_parsers:
        #     print(f'{subparser=}')

        print(f'\n{bi}def parse(self, args: list[str], arg_idx : list[int], config: Optional[Any]=None) -> {self._prl}:', file=fp)
        print(f'{bi*2}if config is not None:', file=fp)
        print(f'{bi*3}config.update_parser(self, {pd.name!r})', file=fp)
        print(f'{bi}{bi}token = args[arg_idx[0]]', file=fp)
        print(f'{bi}{bi}arg_idx[0] += 1', file=fp)
        print(f"{bi}{bi}if token[:2] == '--':", file=fp)
        print(f'{bi}{bi}    token = self.long_token(token, args, arg_idx)', file=fp)
        print(f"{bi}{bi}    if token == 'help':", file=fp)
        print(f'{bi}{bi}        self.help(args, arg_idx)', file=fp)
        for oa in pd.all_options():
            self.gen_option_code(oa, False, bi*3, bi, fp)
        print(f'{bi}{bi}    else:', file=fp)
        # ToDo instantiate CmdParser with argument and index to continue with
        # until then you need to roll back what you work on
        if pd.default_subparser is not None:
            print(f'{bi}{bi}        arg_idx[0] -= 1', file=fp)  # need to roll back what you work on
            print(f'{bi}{bi}        return {pd.default_subparser.class_name}().sub(self)', file=fp)
        else:
            print(f'{bi}{bi}        self.error(args, arg_idx)', file=fp)
        print(f"{bi}{bi}elif token[:1] == '-':", file=fp)
        print(f'{bi}{bi}    arg_idx[1] = 0', file=fp)
        print(f'{bi}{bi}    cur_idx = arg_idx[0]', file=fp)
        # -1 in next line for the dash
        print(f'{bi}{bi}    while cur_idx == arg_idx[0] and (len(token) - 1) > arg_idx[1]:', file=fp)
        print(f'{bi}{bi}        arg_idx[1] += 1', file=fp)
        print(f'{bi}{bi}        arg_char = arg_idx[1]', file=fp)
        print(f"{bi}{bi}        if token[arg_char] == 'h':", file=fp)
        print(f'{bi}{bi}            self.help(args, arg_idx)', file=fp)
        for oa in pd.all_options():
            self.gen_option_code(oa, True, bi*4, bi, fp)
        print(f'{bi}{bi}        else:', file=fp)
        # ToDo instantiate CmdParser with argument and index to continue with
        # until then you need to roll back what you work on
        if pd.default_subparser is not None:
            print(f'{bi}{bi}            assert arg_char == 1', file=fp)
            print(f'{bi}{bi}            arg_idx[0] -= 1', file=fp)  # need to roll back what you work on
            print(f'{bi}{bi}            return {pd.default_subparser.class_name}().sub(self)', file=fp)
        else:
            print(f"{bi}{bi}            print(f'{{token=}} {{arg_char=}}')", file=fp)
            print(f'{bi}{bi}            self.error(args, arg_idx)', file=fp)
        for sp in pd.subparsers:
            print(f"{bi}{bi}elif token == '{sp.name}':", file=fp)
            print(f'{bi*3}return {sp.class_name}().sub(self)', file=fp)
        no_args = True
        for oa in pd.arguments:
            if self.gen_argument_code(oa, oa.long_opts, bi*2, bi, fp):
                no_args = False
        if no_args:
            print(f'{bi}{bi}else:', file=fp)
            if pd.default_subparser is not None:
                print(f'{bi*3}arg_idx[0] -= 1', file=fp)  # need to roll back what you work on
                print(f'{bi*3}return {pd.default_subparser.class_name}().sub(self)', file=fp)
            else:
                print(f'{bi}{bi}    self.error(args, arg_idx)', file=fp)
        print(f'{bi}{bi}return self\n', file=fp)

        self.gen_check(pd, bi=bi, fp=fp)

        # print(f'{bi}parsers = []', file=fp)
        # if self._configs_used:
        #     config_name = self._configs[self._configs_used[-1]]['name']
        #     print(
        #         f'{bi}config = {config_name}(path={quoted(self._config_file)})', file=fp,
        #     )
        #     # testing
        #     # print(f'{bi}print(config.data)', file=fp)
        #     # print(f'{bi}print("testing", config.get("global", "keep", pd=3))', file=fp)
        #     # print(f'{bi}print("testing", config.get("global", "bla", pd=4))', file=fp)
        # if name is None:
        #     if self.smart_formatter:
        #         if kw:
        #             kw += ', '
        #         kw += 'formatter_class=SmartFormatter'
        #     # this is the ArgumentParser as defined in _pregen
        #     print(f'{bi}parsers.append(ArgumentParser({kw}))', file=fp)
        # for oa in optargs:
        #     oas = self.optarg_str(*oa)
        #     print(f'{bi}parsers[-1].add_argument({oas})', file=fp)
        # # print(f"{bi}parsers[-1].add_argument('--version', action='version', version=__version__)", file=fp)
        # if VERSION in self._import_line:
        #     print(
        #         f"{bi}parsers[-1].add_argument('--version', action='store_true', help='show program\\'s version number and exit')",
        #         file=fp,
        #     )
        # if self.sub_parsers:
        #     print(f'{bi}subp = parsers[-1].add_subparsers()', file=fp)
             
        for subparser in pd.subparsers:
            self.gen_one_parser(subparser, fp=fp, base_indent=base_indent)

            # sp_name, subparser_data = list(subparser.items())[0]
            # npath = path.copy()  # multiple sub commands cannot mutate path itself with append
            # npath.append(sp_name)
            # self.gen_one_parser(subparser_data, npath, fp=fp, base_indent=base_indent)
#            if self.smart_formatter:
#                if kw:
#                    kw += ', '
#                kw += 'formatter_class=SmartFormatter'
#            kwcomma = ', ' if kw else ''
#            print(f"{bi}px = subp.add_parser('{sp_name}'{kwcomma}{kw})", file=fp)
#            # the following line might not be needed for alternate defaults setting using config.get()
#            # that line adds the name of the subparser to the subparser
#            sp_name_clean = self.clean_name(sp_name)
#            print(f"{bi}px.set_defaults(subparser_func='{sp_name_clean}')", file=fp)
#            print(f'{bi}parsers.append(px)', file=fp)
#            # print('optargs 1', optargs)
#            for oa in optargs + self._global_options:
#                oas = self.optarg_str(*oa, subparser=sp_name)
#                print(f'{bi}parsers[-1].add_argument({oas})', file=fp)
#        if self.sub_parsers:
#            print(f'{bi}parsers.pop()', file=fp)
#            
#        if name is None:
#            if self._default_subparser:
#                sp = self._default_subparser
#                spn = repr([list(k.keys())[0] for k in self.sub_parsers])
#                fp.write(default_sub_parser_resolution.format(bi=bi, sp=sp, sp_names=spn))
#                
#            if self._help_all:
#                fp.write(help_all_text.format(bi=bi))
#            # print(f'{bi}print(\'cmdarg:\', cmdarg)', file=fp)
#            print(f'{bi}args = parsers[0].parse_args(args=cmdarg[1:])', file=fp)
#            if self.debug:
#                print(f"{bi}debug('args 1:', args)", file=fp)
#            # global options processing
#            if self._global_default_options:
#                print(f'{bi}for gl in {self._global_default_options}:', file=fp)
#                print(f"{bi}{bi}glv = getattr(args, '_gl_' + gl, None)", file=fp)
#                if self.sub_parsers:
#                    print(
#                        f'{bi}{bi}if isinstance(getattr(args, gl, None), (DefaultVal, type(None))) and glv is not None:',
#                        file=fp,
#                    )
#                    print(f'{bi}{bi}{bi}setattr(args, gl, glv)', file=fp)
#                else:
#                    print(f'{bi}{bi}setattr(args, gl, glv)', file=fp)
#                print(f"{bi}{bi}delattr(args, '_gl_' + gl)", file=fp)
#                print(f'{bi}{bi}if isinstance(getattr(args, gl, None), DefaultVal):', file=fp)
#                print(f'{bi}{bi}{bi}setattr(args, gl, getattr(args, gl).val)', file=fp)
#            if self.debug:
#                print(f"{bi}debug('args 2:', args)", file=fp)
#            if False and self._required_options:
#                print(f'{bi}req_options_found = True', file=fp)
#                qo = ', '.join([f"'{o}'" for o in self._required_options])
#                print(f'{bi}for attr in [{qo}]:', file=fp)
#                print(f'{bi}{bi}if getattr(args, attr, None) is None:', file=fp)
#                print(f"{bi}{bi}{bi}attr = ('--' if len(attr) > 1 else '-') + attr", file=fp)
#                print(f"{bi}{bi}{bi}print('missing required option', attr)", file=fp)
#                print(f'{bi}{bi}{bi}req_options_found = False', file=fp)
#                print(f'{bi}{bi}if not req_options_found:', file=fp)
#                print(f'{bi}{bi}{bi}sys.exit(1)', file=fp)
#                # self._required_options:
#                # if not hassatr
        if len(pd.path) == 0:
            self.gen_main(return_type=self._prl, default=pd.default_subparser, fp=fp, base_indent=base_indent)

    def gen_check(self, pd, bi, fp=sys.stdout):
        first = True
        for oa in chain(pd.options, pd.arguments):
            if oa.nargs is None:
                continue
            if first:
                first = False
                print(f'{bi}def check(self):', file=fp)
                print(f'{bi*2}super().check()', file=fp)
            print(f"{bi*2}self.check_narg('{oa.target}', self.{oa.target}, {oa.nargs})", file=fp)

    def gen_option_code(self, oa, short, bi, ei, fp):
        # bi base indent depending on context
        # ei extra indent relative to that (normally 4 spaces)
        if oa.is_arg:
            return
        if short:
            opts = oa.short_opts
            ind = '[arg_char]'
        else:
            opts = oa.long_opts
            ind = ''
        # check if this matches the option
        if len(opts) == 1:
            print(f"{bi}elif token{ind} == '{opts[0]}':", file=fp)
        elif len(opts) > 1:
            print(f"{bi}elif token{ind} in {opts}:", file=fp)
        else:
            return
            # print("no long or short option to match?", oa)
            # sys.exit(1)
        if oa.typ == 'int' and oa.action == 'count':
            val = oa.const if oa.const is not None else 1
            print(f"{bi}{ei}self.{oa.target} += {val}", file=fp)
        elif oa.typ == 'bool':
            print(f"{bi}{ei}self.{oa.target} = True", file=fp)
        elif oa.typ == 'str':
            if short:
                 print(f"{bi}{ei}self.{oa.target} = self.short_arg(args, arg_idx)", file=fp)
            else:
                 print(f"{bi}{ei}self.{oa.target} = self.optarg(token{ind}, args, arg_idx)", file=fp)
        elif oa.typ in ['int', 'float']:
            if short:
                 print(f"{bi}{ei}self.{oa.target} = {oa.typ}(self.short_arg(args, arg_idx))", file=fp)
            else:
                 print(f"{bi}{ei}self.{oa.target} = {oa.typ}(self.optarg(token{ind}, args, arg_idx))", file=fp)
        elif oa.typ in self._actions:
            v = self._actions[oa.typ]
            if short:
                 print(f"{bi}{ei}self.{oa.target} = gen_{oa.typ}(self.short_arg(args, arg_idx))", file=fp)
            else:
                 print(f"{bi}{ei}self.{oa.target} = gen_{oa.typ}(self.optarg(token{ind}, args, arg_idx))", file=fp)
            self._actions_used.add(oa.typ)
            self._imports.update(v['imports'])
        else:
            print('actions', list(self._actions.keys()))
            print('don\'t know how to generate code for option', oa)
            sys.exit(1)

    def gen_argument_code(self, oa, opts, bi, ei, fp):
        if not oa.is_arg:
            return False
        # bi base indent depending on context
        # ei extra indent (normally 4 spaces)
        assert len(opts) == 1
        if oa.typ != 'str':
            print(f'{oa.typ=}')
            return
            assert oa.typ == 'str'
        print(f'{bi}else:', file=fp)
        print(f'{bi}{ei}self.{oa.target}.append(token)', file=fp)
        return True

    def gen_pre(self, fp=sys.stdout, base_indent=4):
        # include everything before the actual parsing code
        # write the header
        bi = ' ' * base_indent
        help_states = ''
        for hs in self._help_states:
            quote = ''
            if not hs.startswith('HelpState.'):
                hs = repr(hs)

            help_states += f'\n        {quote}{hs}{quote},'
        fp.write(
            self.uncomment(_pregen).format(
                version=__version__,
                today=datetime.date.today(),
                imports='\nimport '.join(sorted(self._imports)),
                verimp=self._import_line,
                max_help_position=self._max_help_position,
                args=' '.join(sys.argv[1:]),  # invocation arguments
                help_states=help_states,
            )
        )
        # from !Module argument
        if self._import_from_module:
            mn = self._import_from_module
            funs = ', '.join([k.name for k in self._pdata.subparsers])
            print(f'from {mn} import {funs}', file=fp)
        if self._debug:
            fp.write('debug = print\n\n')
        # # needed for defaults of global options
        # if self._global_default_options:
        #     # DefaultVal might not be there, if it is it can be tested with isinstance(X, str)i
        #     # e.g. in DateAction, to do conversion
        #     fp.write(
        #         dedent(
        #             """
        #         class DefaultVal(str):
        #             def __init__(self, val: typing.Any):
        #                 self.val = val

        #             def __str__(self) -> str:
        #                 return str(self.val)

        #     """
        #         )
        #     )
        for c in self._configs_used:
            fp.write('\n\n')
            fp.write(self._configs[c]['body'])
        for a in sorted(self._actions_used):
            # assume no newlines before and after each class definition in action/*.py
            fp.write('\n')
            fp.write(self._actions[a]['body'])
            fp.write('\n')

    def gen_main(self, return_type, default=None, fp=sys.stdout, base_indent=4):
        # generate main entry
        bi = ' ' * base_indent
        if self._configs_used:
            config_name = self._configs[self._configs_used[-1]]['name']
        else:
            config_name = 'Any'

        print(f'\ndef parse(\n{bi}cmdarg: typing.List[str],\n{bi}config: Optional[{config_name}] = None,\n) -> {return_type}:', file=fp)

        if VERSION in self._import_line:
            print(f"{bi}if '--version' in cmdarg:", file=fp)
            if self._pkg_data:
                # if ver is static generated during cligen, you would need to regenerate even
                # if a version is updated without commandline change
                # here we staticly generate a list of packages, but dynamically get the version
                ver = None
                pkgs = []
                fpn = self._pkg_data['full_package_name']
                if isinstance(self._pkg_data.get('install_requires', []), list):
                    to_inst = self._pkg_data.get('install_requires', [])
                elif self._pkg_data.get('install_requires') is not None:
                    to_inst = self._pkg_data['install_requires'].get('any', [])
                else:
                    to_inst = []
                for pkg in to_inst:
                    for x in '=!<>~':
                        pkg = pkg.split(x, 1)[0]
                    if pkg in ['ruamel.std.argparse', 'ruamel.appconfig']:
                        print(
                            f'found required package "{pkg}" which is not needed with cligen'
                        )
                    pkgs.append(pkg)
                print(
                    f"{bi}{bi}if '-v' in cmdarg or '--verbose' in cmdarg:", file=fp
                )
                print(
                    f"{bi}{bi}{bi}return list_versions(pkg_name='{fpn}', version={ver}, pkgs={pkgs})",
                    file=fp,
                )
            elif False and PKG_DATA in self._import_line:
                print(
                    f"{bi}{bi}if '-v' in cmdarg or '--verbose' in cmdarg:", file=fp
                )
                print(
                    f"{bi}{bi}{bi}return list_versions(pkg_name='{fpn}', version={ver}, pkgs={pkgs})",
                    file=fp,
                )
            print(f'{bi}{bi}print(__version__)', file=fp)
            print(f'{bi}{bi}return 0', file=fp)
                
        print(f'{bi}arg_idx = [0, 0]', file=fp)
        print(f'{bi}result = CmdParser()', file=fp)
        default_data = ''
        if self._configs_used is not None:
            default_data = ', config'
        if default is not None:
            # otherwise parse will not be called
            print(f'{bi}if len(cmdarg) == 0:', file=fp)
            print(f'{bi*2}cmdarg.append({default.name!r})', file=fp)
        print(f'{bi}while arg_idx[0] < len(cmdarg):', file=fp)
        print(f'{bi*2}result = result.parse(cmdarg, arg_idx{default_data})', file=fp)
        # print(f"{bi}f_or attr in ['_option_argument']:", file=fp)
        # print(f'{bi*2}try:', file=fp)
        # print(f'{bi*3}delattr(result, attr)', file=fp)
        # print(f'{bi*3}print("result:", result)', file=fp)
        # print(f'{bi*2}except AttributeError:', file=fp)
        # print(f'{bi*3}raise', file=fp)
        print(f'{bi}result.check()', file=fp)
        print(f'{bi}return result', file=fp)

        # if self._shorthands:
        #     raise NotImplementedError
        #     print(
        #         f'{bi}sh_subp = {self._shorthands}.get(cmdarg[0].rsplit(os.sep, 1)[-1])',
        #         file=fp,
        #     )
        #     print(f'{bi}if sh_subp is not None:', file=fp)
        #     print(f'{bi}{bi}cmdarg.insert(1, sh_subp)', file=fp)
        print(f'\n\ndef main(cmdarg: typing.Optional[typing.List[str]]=None) -> int:', file=fp)
        print(f'{bi}cmdarg = sys.argv[1:] if cmdarg is None else cmdarg', file=fp)
        if self._loader._args.timeit:
            self._imports.add('time')
            print(f'{bi}start = time.time()', file=fp)
        if self._configs_used:
            print(
                f'{bi}config = {config_name}(path={quoted(self._config_file)})', file=fp,
            )
            print(f'{bi}args = parse(cmdarg, config)', file=fp)
        else:
            print(f'{bi}args = parse(cmdarg)', file=fp)
        print(f'{bi}if isinstance(args, int):', file=fp)
        print(f'{bi*2}return args', file=fp)
        if self._debug:
            print(f"{bi}print(f'{{args=}}')", file=fp)
        if self._configs_used:
            cfg_parm = ', config=config'  # so that the main code has access to the config file
        else:
            cfg_parm = ''
        if self._import_from_module is not None:
            ifm = self._import_from_module
            print(f"{bi}funcname = getattr(args, '_name', None)", file=fp)
            print(f'{bi}if funcname is None:', file=fp)
            print(f"{bi*2}args.help()", file=fp)
            if self._loader._args.timeit:
                print(f"{bi}print(f'cligen time: {{time.time()-start:.4f}}s')", file=fp)
            if ifm:
                print(
                    f'{bi}fun = getattr(importlib.import_module("{ifm}"), funcname)',
                    file=fp,
                )
                print(f'{bi}ret_val = fun(args)', file=fp)  # add config?
            else:  # inserted in __main__ itself
                print(f'{bi}ret_val = globals()[funcname](args)', file=fp)  # add config?
            print(f'{bi}if ret_val is None:', file=fp)
            print(f'{bi}{bi}return 0', file=fp)
            print(f'{bi}if isinstance(ret_val, int):', file=fp)
            print(f'{bi}{bi}return ret_val', file=fp)
            print(f'{bi}return -1', file=fp)
            print('\n', file=fp)
        elif self._instantiate is not None:
            try:
                m, c = self._instantiate.rsplit('.', 1)
                print(
                    f"""{bi}cls = getattr(importlib.import_module('{m}'), '{c}')""",
                    file=fp,
                )
                print(f'{bi}obj = cls(args{cfg_parm})', file=fp)
            except ValueError:
                c = self._instantiate
                print(f'{bi}obj = {c}(args{cfg_parm})', file=fp)
            print(f"{bi}funcname = getattr(args, '_name', None)", file=fp)
            # print(f'{bi}if funcname == \'version\' and not hasattr(obj, \'version\'):', file=fp)
            # print(f'{bi}{bi}return list_versions()', file=fp)
            print(f'{bi}if funcname is None:', file=fp)
            if self.sub_parsers:
                print(f"{bi*2}parsers[0].parse_args(['--help'])", file=fp)
            else:
                # if no subparsers you need to have a run method, or do everything from init() and exit()
                print(f"{bi*2}funcname = 'run'", file=fp)
            # print(f'{bi}fun = getattr(obj, args.subparser_func)', file=fp)
            print(
                f"{bi}fun = getattr(obj, funcname + '_subcommand', None)  # type: ignore",
                file=fp,
            )
            print(f'{bi}if fun is None:', file=fp)
            # print(f"{bi*2}print('no _subcommand')", file=fp)
            print(f'{bi*2}fun = getattr(obj, funcname)  # type: ignore', file=fp)
            # print(f'{bi}else:', file=fp)
            # print(f"{bi*2}print('found _subcommand')", file=fp)
            if self._loader._args.timeit:
                print(f"{bi}print(f'cligen time: {{time.time()-start:.4f}}s')", file=fp)
            print(f'{bi}ret_val = fun()', file=fp)
            print(f'{bi}if ret_val is None:', file=fp)
            print(f'{bi}{bi}return 0', file=fp)
            print(f'{bi}if isinstance(ret_val, int):', file=fp)
            print(f'{bi}{bi}return ret_val', file=fp)
            print(f'{bi}return -1', file=fp)
            print('\n', file=fp)
        elif self._no_sub_parser is not None:
            try:
                m, c = self._no_sub_parser.rsplit('.', 1)
                print(
                    f"""{bi}entry = getattr(importlib.import_module('{m}'), '{c}')""",
                    file=fp,
                )
                print(f'{bi}res = entry(args{cfg_parm})', file=fp)
            except ValueError:
                c = self._no_sub_parser
                print(f'{bi}res = {c}(args{cfg_parm})', file=fp)
            print('>>>>>>>>> resolve exit value, if not int assuming .retval attribute')
            print(
                f"{bi}return res if isinstance(res, int) else getattr(res, 'retval', 0)",
                file=fp,
            )
            print('\n', file=fp)
        else:
            print('need to have either !Module, !Instance, or !Main in cli YAML')
            sys.exit(1)


    def gen_post(self, fp=sys.stdout):
        if self.extend_main:
            fp.write(self.extend_main)
        if self._pkg_data:
            fp.write(self.uncomment(_list_versions))
        elif False and PKG_DATA in self._import_line:  # this happens in _test/data
            # need to parse the _package_data there
            fp.write(_list_versions)
        fp.write(_postgen)

    def get_kw(self, data, pdata: PData = None):
        # get all the keywords
        # path is a list of nested subcommands, if there is one level it will have length 1
        top_level = pdata.parent is None

        res = {}
        optarg = []
        subparsers = []
        todo = []
        sp_name = pdata.name # path[0] if len(path) > 0 else ''
        for elem in data:
            # print('get_kw: elem', elem, elem.tag.value)
            tag = elem.tag.value
            if tag is None:
                assert isinstance(elem, dict)
                if isinstance(elem, dict) and isinstance(list(elem.values())[0], list):
                    subparsers.append(elem)
                    continue  # skip subparsers
                res.update(elem)  # key-value pair
                continue
            if not top_level and tag == '!DefaultSubparser':
                parent = pdata.parent
                assert parent is not None
                if pdata.parent.default_subparser not in [None, pdata]:
                    print(
                        f'cannot have !DefaultSubparser for both "{pdata.parent.default_subparser.name}" and "{pdata.name}"'
                    )
                    sys.exit(1)
                parent.default_subparser = pdata
                continue
            if not top_level and tag == '!Alias':
                res.setdefault('aliases', []).extend(
                    elem if isinstance(elem, list) else [elem.value]
                )
                continue
            if not top_level and tag == '!Shorthand':
                v = elem.value
                if elem.value in self._shorthands:
                    print(
                        f'shorthand {v!r}, for subparser {sp_name!r} reused for {self._shorthands[v]!r}'
                    )
                    sys.exit(1)
                self._shorthands[v] = sp_name
                continue
            if top_level and tag == 'Width':
                self._max_help_position = int(elem.value)
                continue
            if top_level and tag == '!Module':
                todo.append(tag)
                self._import_from_module = elem.value
                continue
            if top_level and tag == '!Instance':
                todo.append(tag)
                self._instantiate = elem.value
                continue
            if top_level and tag == '!Main':
                todo.append(tag)
                self._no_sub_parser = elem.value
                continue
            if top_level and tag == '!AddDefaults':
                self._add_defaults = elem.value
                continue
            # if top_level and tag == '!HelpAll':
            #    self._help_all = True
            #    continue
            if top_level and tag == '!Config':
                # determine config file type and path, don't expand paths at cligen run time!
                if isinstance(elem, list):
                    v = elem[0]
                    self._config_file = Path(elem[1])
                else:
                    if elem.value[0] in '~/':
                        # assume a full path with extension determining config typ
                        self._config_file = Path(elem.value)
                        v = self._config_file.suffix.lstrip('.')
                    elif '/' in elem.value:
                        # assume a partial path with extension determining config typ
                        self._config_file = elem.value
                        v = Path(self._config_file).suffix.lstrip('.')
                    else:
                        v = elem.value
                        if self._pkg_data:
                            self._config_file = self._pkg_data.get(
                                'config_subdir', self._pkg_data['full_package_name']
                            )
                        elif PKG_DATA in self._import_line:
                            self._config_file = "_package_data['full_package_name']"
                if v not in self._configs and v.lower() in self._configs:
                    v = elem.value = v.lower()
                if v not in self._configs:
                    print('unknown config format', v)
                    sys.exit(1)
                if '_base' not in self._configs_used:
                    if self._configs['_base']['name'] in self._configs[v]['body']:
                        self._configs_used.insert(0, '_base')
                        self._imports.update(self._configs['_base']['imports'])
                self._configs_used.append(v)
                self._imports.update(self._configs[v]['imports'])
                continue
            if tag in self._all_option_tags:
                optarg.append(oa := self.gen_opt(tag, elem))
                if tag in self._pre_subparser_option_tags:
                    oa.is_global = False
                continue
            if tag in self._arg_tags:
                optarg.append(self.gen_opt(tag, elem, argument=True))
                continue
            key = self._tag_map[tag[1:]]
            try:
                res[key] = elem.value
            except AttributeError as e:
                # you can tag an anchored scalar, but if you do "!Help &name text1 text2"
                # you get the same result as "&name !Help text1 text2"
                # so you cannot do "!Prolog *name", but in cligen you can do "!Prolog [*name]"
                try:
                    res[key] = elem[0].value
                except Exception:
                    raise e
        # return ', '.join(['{k}={v!r}'.format(k=k, v=v) for k,v in res.items()]), optarg
        if sp_name:
            # print('get_kw', sp_name, res, optarg, subparsers)
            if 'description' in res and 'help' not in res:
                # if no help, take the first line of the description
                res['help'] = res['description'.split('\n')[0]]
        if len(todo) > 1:
            print('you can have only one of\n-', '\n- '.join(todo))
            sys.exit(1)
        # if self._add_defaults is not None:
        #     # print(f'{self._add_defaults}')
        #     for oa in optarg:
        #         print('  ', oa)
        #         continue
        #         if not isinstance(oa[1], dict):
        #             continue
        #         oa = oa[1]
        #         act = oa.get('action')
        #         if act in _standard_actions:
        #             if not _standard_actions[act]['defaults']:
        #                 continue
        #         elif act:
        #             if act in ['CountAction']:  # ToDo load from file into self._actions
        #                 continue
        #         if 'help' in oa:
        #             oa['help'] += self._add_defaults

        for oa in optarg:
            if oa.target is None:
                if oa.long_opts:
                    oa.target = self.targetify(oa.long_opts[0])
                else:
                    oa.target = self.targetify(oa.short_opts[0])

        if self._debug:
            print('optarg', pdata.path)
            for oa in optarg:
                print('  ', oa)
        # print('subparsers')
        # for sp in subparsers:
        #     print(sp)
        kws = res
        # kws = self.kws(res)  # generate kws for argparse
        return kws, optarg, subparsers

    def gen_opt(self, orgtag, data, argument=False):
        # print('gen_opt: elem', orgtag, data, argument)
        # long_opts = []
        # short_opts = []
        # kw = dict(long_opts=long_opts, short_opts=short_opts)
        kw = Option()
        long_opts = kw.long_opts
        short_opts = kw.short_opts
        attribute = None
        for elem in data:
            tag = None
            try:
                tag = elem.tag.value
            except AttributeError:
                # this is an untagged value
                if isinstance(elem, str):
                    if '=' in elem:
                        print(f'\n>>>>> there is an equal sign in {elem},', end='')
                        alt = elem.replace('=', ': ')
                        print(f' are you sure this should not be: {alt} ?\n')
                    if attribute is None:
                        attribute = elem
                    if argument or len(elem) != 1:
                        long_opts.append(elem)
                    else:
                        short_opts.append(elem)
                    continue
            if tag is None:
                if isinstance(elem, dict):
                    assert len(elem) == 1
                    key, value = list(elem.items())[0]
                    if 'required' in elem and elem['required']:
                        print('cannot use "required: True", use tag option with !ReqOption')
                        sys.exit(1)
                    if key in ['type', 'default']:
                        print(f'upgrade key {key} to a tag')
                    if key == 'type':
                        kw.typ = value
                    elif key == 'nargs':
                        self.set_nargs(kw, value)
                    else:
                        assert hasattr(kw, key), f'untagged {key!r} not in {kw}'
                        setattr(kw, key, value)
            else:
                if tag in ['!Default', '!Def']:
                    if isinstance(elem, list):
                        kw.default = list(elem)
                    else:
                        kw.default = elem.value
                    continue
                if tag == '!Type':
                    kw.typ = elem.value
                    continue
                if tag == '!Dest':
                    kw.target = elem.value
                    continue
                if tag == '!Action':
                    # ToDo: warning to upgrade to !Type
                    if elem.value == 'store_true':
                        if kw.typ in [None, 'str']:
                            kw.typ = 'bool'
                        continue
                    elif elem.value == 'date':
                        if kw.typ in [None, 'str']:
                            kw.typ = 'date'
                        continue
                    elif elem.value == 'count':
                        kw.typ = 'int'
                    else:
                        print('unknown action:', elem.value)
                        sys.exit(1)
                    # for k1, v1 in self._actions.items():
                    #     if elem.value == k1:
                    #         print(f'change "!Action {tag}" to "!Action {v1["stem"]}')
                    #         sys.exit(1)
                    #     if elem.value == v1['stem']:
                    #         elem.value = k1
                    #         break
                    # else:
                    #     if elem.value not in _standard_actions:
                    #         print('unknown action:', elem.value)
                try:
                    key = self._tag_map[tag[1:]]
                except Exception as e:
                    if tag and tag[-1] == ':':
                        print('are you sure you want a colon at the end of the tag?')
                    print('exception', e)
                    print(self._tag_map)
                    sys.exit(-1)
                if key == 'help':
                    if self._add_defaults is None:
                        if elem.value.startswith('D|'):
                            self.smart_formatter = True
                        elif elem.value.startswith('R|'):
                            self.smart_formatter = True
                        elif elem.value.startswith('*|'):
                            self.smart_formatter = True
                if key in ['nargs']:
                    self.set_nargs(kw, elem)
                    continue
                    # try:
                    #     elem.value = int(elem.value)
                    # except ValueError:
                    #     pass
                if key == 'type':
                    # ToDo: warning to upgrade to !Type
                    raise NotImplementedError
                    kw.typ = elem.value
                else:
                    assert hasattr(kw, key)
                    setattr(kw, key, elem.value)
        # only add global options when not processing subparsers
        if self.sub_parsers is None and orgtag not in self._pre_subparser_option_tags:
            self._global_options.append(kw)
            # if orgtag.startswith('!Req'):
            #     print('cannot have global !ReqOption, replicate for each subparser')
            #     sys.exit(1)
        else:
            if orgtag.startswith('!Req'):
                kw['required'] = True
        if argument:
            assert len(short_opts) == 0
            assert len(long_opts) == 1
            kw.is_arg = True
        return kw

    def set_nargs(self, kw, elem):
        if isinstance(elem, list):
            assert len(elem) == 2
            assert isinstance(elem[0], int)
            assert isinstance(elem[1], int)
            setattr(kw, key, (elem[0], elem[1]))
            return
        if hasattr(elem, 'value'):
            elem = elem.value
        if isinstance(elem, tuple):
            # happens when processing data twice
            assert len(elem) == 2
            assert isinstance(elem[0], int)
            assert isinstance(elem[1], int)
        elif elem == '*':
            elem = [0, -1]
        elif elem == '+':
            elem = [1, -1]
        elif elem == '?':
            elem = [0, 1]
        else:
            try:
                v = int(elem)
                if v == 0:
                    return
                elem = (v, v)
            except TypeError:
                print(f'{elem=}')
                raise
        setattr(kw, 'nargs', elem)

    def targetify(self, s):
        # an option can e.g. contain a days, which is not a valid attribute name
        for x in '-':
            s = s.replace(x, '_')
        return s


some_old_stuff = '''
from __future__ import annotations
# type Union vs | 
 
"""
parsing routines for commandline

actions:
   - set to value (optional type)
   - append to list
   - splitappend
   - count (up, down)
   - set true
   - set false
   - check single store
   - date

https://github.com/huggingface/transformers/blob/c5d7754b1140aaad95ad36c5d9ddfda5abda19f6/src/transformers/hf_argparser.py#L109
looks good, but has all kinds of interpreting going on based on the field, IMO that
should be all in the generated code -> simpler data structure and more boilerplate like code

There is no such thing as an optional subcommand. Either a command has subcommand or it has not.
Therefore a command could search for its subcommands, and if not found, create a default command.
"""

   
'''
