# coding: utf-8
# flake8: noqa
# cligen: 0.5.0, dd: 2023-11-16, args: 

from __future__ import annotations


import importlib
import os
import pathlib
import ruamel.yaml
import sys
import typing
from typing import Optional, List, ClassVar, Any, Union, Callable
from dataclasses import dataclass, MISSING, field, fields, asdict, InitVar

from . import __version__


@dataclass
class HelpState:
    max_help_position: int = 30
    indent_level: int = 0
    spaces_per_indent: int = 2
    stack: list[int, str] = field(default_factory=list)
    out: Any = sys.stdout

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
        self.out.write('\n')

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
            else:
                s1 = s1.format(pd=parser)
                s1 = s1.replace('\n', '\n' + ' ' * self.max_help_position)
            if len(s0) + (self.indent_level * self.spaces_per_indent) >= self.max_help_position:
                self.write_nl(parser, s0)
                self.write_nl(parser, s1, indent=self.max_help_position)
            else:
                self.write_nl(parser, f'{s0:<{self.max_help_position-(self.indent_level*self.spaces_per_indent)}s}{s1}')

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
    _help_global: ClassVar[list[Union[Callable[[Any], None], str]]] = [
        HelpState.write,
        HelpState.write_nl,
        HelpState.write_options,
        HelpState.expand,
        HelpState.indent,
        HelpState.dedent,
        'usage: {pd.prog} [-h] [--verbose] [--comment] [--debug] [--timeit] [--version]',
        '{gen,replace,update,convert,comment,snippet} ...',
        '',
        'sub-comamnds:',
        'gen',
        'generate __main__.py',
        'replace',
        'replace a string in the _cligen_data/cli.yaml',
        'update',
        'common updates to _cligen_data/cli.yaml\n- remove explicit default adding on !Help if !AddDefaults is set',
        'convert',
        'analyse argument file that uses ruamel.std.argparse and generate cligen data\n- commands currently cannot have a different name (using set first @subparser argument)',
        'comment',
        'show cligen_data comments (from cligen.__init__.py)',
        'snippet',
        'work on snippets (site-packages/cligen/_snippet, ~/.config/cligen/snippet), by default insert\nbased on matching arguments',
        'positional arguments:',
        '-h, --help',
        'show this help message and exit',
        '--verbose, -v',
        'increase verbosity level (default: {pd.verbose!r})',
        '--comment',
        "don't strip comments from included code (config)",
        '--debug',
        'insert debug statements in generated code',
        '--timeit',
        "insert code to time from startup to calling method/function'",
        '--version',
        "show program's version number and exit",
        'usage: {pd.prog} gen [-h] [--type TYPE] [--output OUTPUT] [--meld] [--verbose] [--comment] [--debug] [--timeit]',
        '--type TYPE',
        'select python/argparse (default: {pd.type!r})',
        '--output OUTPUT',
        'output to file (default: {pd.output!r})',
        '--meld',
        'present output as diff for inspection',
        'usage: {pd.prog} replace [-h] [--from FRM] [--to TO] [--backup] [--verbose] [--comment] [--debug] [--timeit]',
        'path',
        'path pattern to scan for replacement',
        '--from FRM',
        'original string to match (default: {pd.frm!r})',
        '--to TO',
        'replacement string (default: {pd.to!r})',
        '--backup',
        'make a timestamped backup of the file (.YYYYMMDD-HHMMSS)',
        'usage: {pd.prog} update [-h] [--test] [--verbose] [--comment] [--debug] [--timeit]',
        '--test',
        "don't save",
        'usage: {pd.prog} convert [-h] [--append] [--verbose] [--comment] [--debug] [--timeit]',
        '--append',
        'append _cligen_data to __init__.py',
        'usage: {pd.prog} comment [-h] [--update UPDATE] [--verbose] [--comment] [--debug] [--timeit]',
        '--update UPDATE',
        'update cligen_data comments in __init__.py (argument can be directory or file) (default: {pd.update!r})',
        'usage: {pd.prog} snippet [-h] [--list] [--log LOG] [--verbose] [--comment] [--debug] [--timeit]',
        'arg',
        '--list',
        'list available snippets for current environment',
        '--log LOG',
        'file to log output to (default: {pd.log!r})',
    ]
    # help_data: list[int] = field(default_factory=list)

    def add_str(self, s):
        self._help_global.append(s)
        return len(self._help_global) - 1

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

    def parse(self, args: List[str], arg_idx: List[int]) -> BaseParser:
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
        print(f"missing argument for option {'--' if len(x) > 1 else '-'}{x}")
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
            print(f'number of arguments for {name!r} not in range ({low} <= {length} <= {high})')
            sys.exit(1)
        else:
            if length < low:
                print(f'number of arguments ({length}) for {name!r} should be at least {low})')
                sys.exit(1)

    @property
    def prog(self):
        return BaseParser._prog_name if BaseParser._prog_name is not None else os.path.basename(sys.argv[0])


class ConfigBase:
    suffix = ""

    def __init__(self, path: typing.Optional[typing.Union[pathlib.Path, str]]=None):
        self._data = None
        tmp_path = self.get_config_parm()
        if tmp_path:
            self._path = tmp_path
        elif isinstance(path, pathlib.Path):
            self._path = path
        elif path is not None:
            if path[0] in '~/':
                self._path = pathlib.Path(path).expanduser()
            elif '/' in path:  # assume '!Config config_dir/config_name'
                self._path = self.config_dir / path
            else:
                self._path = self.config_dir / path / (path.rsplit('.')[-1] + self.suffix)
        else:
            raise NotImplementedError

    @property
    def data(self) -> typing.Any:
        if self._data is None:
            self._data = self.load()  # NOQA
        return self._data

    def get(self, *args: typing.Any, pd: typing.Optional[typing.Any]=None) -> typing.Any:
        data = self.data
        try:
            for arg in args:
                if arg in data:
                    data = data[arg]
                else:
                    break
            else:
                return data
        except Exception as e:
            print(f'exception getting "{arg}" from "{args}" ({self.data})') 
            return {}
        if args[0] != 'global':
            return self.get(*(['global'] + list(args[1:])), pd=pd)
        return pd

    def get_config_parm(self) -> typing.Union[pathlib.Path, None]:
        for idx, arg in enumerate(sys.argv[1:]):
            if arg.startswith('--config'):
                if len(arg) > 8 and arg[8] == '=':
                    return pathlib.Path(arg[9:])
                else:
                    try:
                        return pathlib.Path(sys.argv[idx + 2])
                    except IndexError:
                        print('--config needs an argument')
                        sys.exit(1)
        return None

    @property
    def config_dir(self) -> pathlib.Path:
        attr = '_' + sys._getframe().f_code.co_name
        if not hasattr(self, attr):
            if sys.platform.startswith('win32'):
                d = os.environ['APPDATA']
            else:
                d = os.environ.get(
                    'XDG_CONFIG_HOME', os.path.join(os.environ['HOME'], '.config')
                )
            pd = pathlib.Path(d)
            setattr(self, attr, pd)
            return pd
        return getattr(self, attr)  # type: ignore

    def load(self) -> typing.Any:
        raise NotImplementedError


class ConfigYAML(ConfigBase):
    suffix = '.yaml'

    def load(self) -> typing.Any:
        yaml = ruamel.yaml.YAML(typ='safe')
        try:
            data = yaml.load(self._path)
        except (FileNotFoundError, TypeError, KeyError):
            return {}
        return data

    def __repr__(self) -> str:
        return f'ConfigYAML(path="{self._path}")'


@dataclass
class CmdParser(BaseParser):
    verbose: int = 0
    comment: Optional[bool] = None
    debug: Optional[bool] = None
    timeit: Optional[bool] = None
    help_nrs: ClassVar(list[int]) = [6, 3, 1, 4, 4, 4, 4, 4, 7, 1, 5, 5, 5, 5, 5, 8, 1, 9, 1, 4, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 2, 5, 8, 1, 22, 1, 4, 4, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 2, 5]

    def parse(self, args: List[str], arg_idx : List[int]) -> CmdParser | GenCmdParser | ReplaceCmdParser | UpdateCmdParser | ConvertCmdParser | CommentCmdParser | SnippetCmdParser:
        token = args[arg_idx[0]]
        arg_idx[0] += 1
        if token[:2] == '--':
            token = self.long_token(token, args, arg_idx)
            if token == 'help':
                self.help(args, arg_idx)
            elif token == 'verbose':
                self.verbose += 1
            elif token == 'comment':
                self.comment = True
            elif token == 'debug':
                self.debug = True
            elif token == 'timeit':
                self.timeit = True
            else:
                arg_idx[0] -= 1
                return GenCmdParser().sub(self)
        elif token[:1] == '-':
            arg_idx[1] = 0
            cur_idx = arg_idx[0]
            while cur_idx == arg_idx[0] and (len(token) - 1) > arg_idx[1]:
                arg_idx[1] += 1
                arg_char = arg_idx[1]
                if token[arg_char] == 'h':
                    self.help(args, arg_idx)
                elif token[arg_char] == 'v':
                    self.verbose += 1
                else:
                    assert arg_char == 1
                    arg_idx[0] -= 1
                    return GenCmdParser().sub(self)
        elif token == 'gen':
            return GenCmdParser().sub(self)
        elif token == 'replace':
            return ReplaceCmdParser().sub(self)
        elif token == 'update':
            return UpdateCmdParser().sub(self)
        elif token == 'convert':
            return ConvertCmdParser().sub(self)
        elif token == 'comment':
            return CommentCmdParser().sub(self)
        elif token == 'snippet':
            return SnippetCmdParser().sub(self)
        else:
            arg_idx[0] -= 1
            return GenCmdParser().sub(self)
        return self


@dataclass
class GenCmdParser(CmdParser):
    _name: ClassVar[str] = 'gen'
    type: str = 'python'
    output: str = '__main__.py'
    meld: Optional[bool] = None
    help_nrs: ClassVar(list[int]) = [35, 3, 1, 8, 1, 11, 1, 8, 1, 22, 1, 4, 4, 23, 24, 36, 37, 38, 39, 40, 41, 25, 26, 27, 28, 29, 30, 31, 32, 2, 5]

    def parse(self, args: List[str], arg_idx : List[int]) -> CmdParser | GenCmdParser | ReplaceCmdParser | UpdateCmdParser | ConvertCmdParser | CommentCmdParser | SnippetCmdParser:
        token = args[arg_idx[0]]
        arg_idx[0] += 1
        if token[:2] == '--':
            token = self.long_token(token, args, arg_idx)
            if token == 'help':
                self.help(args, arg_idx)
            elif token == 'verbose':
                self.verbose += 1
            elif token == 'comment':
                self.comment = True
            elif token == 'debug':
                self.debug = True
            elif token == 'timeit':
                self.timeit = True
            elif token == 'type':
                self.type = self.optarg(token, args, arg_idx)
            elif token == 'output':
                self.output = self.optarg(token, args, arg_idx)
            elif token == 'meld':
                self.meld = True
            else:
                self.error(args, arg_idx)
        elif token[:1] == '-':
            arg_idx[1] = 0
            cur_idx = arg_idx[0]
            while cur_idx == arg_idx[0] and (len(token) - 1) > arg_idx[1]:
                arg_idx[1] += 1
                arg_char = arg_idx[1]
                if token[arg_char] == 'h':
                    self.help(args, arg_idx)
                elif token[arg_char] == 'v':
                    self.verbose += 1
                else:
                    print(f'{token=} {arg_char=}')
                    self.error(args, arg_idx)
        else:
            self.error(args, arg_idx)
        return self


@dataclass
class ReplaceCmdParser(CmdParser):
    _name: ClassVar[str] = 'replace'
    frm: str = None
    to: str = None
    backup: Optional[bool] = None
    path: list[str] = field(default_factory=list)
    help_nrs: ClassVar(list[int]) = [42, 3, 1, 8, 1, 13, 1, 8, 1, 22, 1, 4, 43, 44, 2, 5, 8, 1, 4, 23, 24, 45, 46, 47, 48, 49, 50, 25, 26, 27, 28, 29, 30, 31, 32, 2, 5]

    def parse(self, args: List[str], arg_idx : List[int]) -> CmdParser | GenCmdParser | ReplaceCmdParser | UpdateCmdParser | ConvertCmdParser | CommentCmdParser | SnippetCmdParser:
        token = args[arg_idx[0]]
        arg_idx[0] += 1
        if token[:2] == '--':
            token = self.long_token(token, args, arg_idx)
            if token == 'help':
                self.help(args, arg_idx)
            elif token == 'verbose':
                self.verbose += 1
            elif token == 'comment':
                self.comment = True
            elif token == 'debug':
                self.debug = True
            elif token == 'timeit':
                self.timeit = True
            elif token == 'from':
                self.frm = self.optarg(token, args, arg_idx)
            elif token == 'to':
                self.to = self.optarg(token, args, arg_idx)
            elif token == 'backup':
                self.backup = True
            else:
                self.error(args, arg_idx)
        elif token[:1] == '-':
            arg_idx[1] = 0
            cur_idx = arg_idx[0]
            while cur_idx == arg_idx[0] and (len(token) - 1) > arg_idx[1]:
                arg_idx[1] += 1
                arg_char = arg_idx[1]
                if token[arg_char] == 'h':
                    self.help(args, arg_idx)
                elif token[arg_char] == 'v':
                    self.verbose += 1
                else:
                    print(f'{token=} {arg_char=}')
                    self.error(args, arg_idx)
        else:
            self.path.append(token)
        return self

    def check(self):
        super().check()
        self.check_narg('path', self.path, [0, -1])

@dataclass
class UpdateCmdParser(CmdParser):
    _name: ClassVar[str] = 'update'
    test: Optional[bool] = None
    path: list[str] = field(default_factory=list)
    help_nrs: ClassVar(list[int]) = [51, 3, 1, 8, 1, 15, 1, 8, 1, 22, 1, 4, 43, 44, 2, 5, 8, 1, 4, 23, 24, 52, 53, 25, 26, 27, 28, 29, 30, 31, 32, 2, 5]

    def parse(self, args: List[str], arg_idx : List[int]) -> CmdParser | GenCmdParser | ReplaceCmdParser | UpdateCmdParser | ConvertCmdParser | CommentCmdParser | SnippetCmdParser:
        token = args[arg_idx[0]]
        arg_idx[0] += 1
        if token[:2] == '--':
            token = self.long_token(token, args, arg_idx)
            if token == 'help':
                self.help(args, arg_idx)
            elif token == 'verbose':
                self.verbose += 1
            elif token == 'comment':
                self.comment = True
            elif token == 'debug':
                self.debug = True
            elif token == 'timeit':
                self.timeit = True
            elif token == 'test':
                self.test = True
            else:
                self.error(args, arg_idx)
        elif token[:1] == '-':
            arg_idx[1] = 0
            cur_idx = arg_idx[0]
            while cur_idx == arg_idx[0] and (len(token) - 1) > arg_idx[1]:
                arg_idx[1] += 1
                arg_char = arg_idx[1]
                if token[arg_char] == 'h':
                    self.help(args, arg_idx)
                elif token[arg_char] == 'v':
                    self.verbose += 1
                else:
                    print(f'{token=} {arg_char=}')
                    self.error(args, arg_idx)
        else:
            self.path.append(token)
        return self

    def check(self):
        super().check()
        self.check_narg('path', self.path, [0, -1])

@dataclass
class ConvertCmdParser(CmdParser):
    _name: ClassVar[str] = 'convert'
    append: Optional[bool] = None
    path: str = None
    help_nrs: ClassVar(list[int]) = [54, 3, 1, 8, 1, 17, 1, 8, 1, 22, 1, 4, 43, 8, 2, 5, 8, 1, 4, 23, 24, 55, 56, 25, 26, 27, 28, 29, 30, 31, 32, 2, 5]

    def parse(self, args: List[str], arg_idx : List[int]) -> CmdParser | GenCmdParser | ReplaceCmdParser | UpdateCmdParser | ConvertCmdParser | CommentCmdParser | SnippetCmdParser:
        token = args[arg_idx[0]]
        arg_idx[0] += 1
        if token[:2] == '--':
            token = self.long_token(token, args, arg_idx)
            if token == 'help':
                self.help(args, arg_idx)
            elif token == 'verbose':
                self.verbose += 1
            elif token == 'comment':
                self.comment = True
            elif token == 'debug':
                self.debug = True
            elif token == 'timeit':
                self.timeit = True
            elif token == 'append':
                self.append = True
            else:
                self.error(args, arg_idx)
        elif token[:1] == '-':
            arg_idx[1] = 0
            cur_idx = arg_idx[0]
            while cur_idx == arg_idx[0] and (len(token) - 1) > arg_idx[1]:
                arg_idx[1] += 1
                arg_char = arg_idx[1]
                if token[arg_char] == 'h':
                    self.help(args, arg_idx)
                elif token[arg_char] == 'v':
                    self.verbose += 1
                else:
                    print(f'{token=} {arg_char=}')
                    self.error(args, arg_idx)
        else:
            self.path.append(token)
        return self


@dataclass
class CommentCmdParser(CmdParser):
    _name: ClassVar[str] = 'comment'
    update: str = None
    help_nrs: ClassVar(list[int]) = [57, 3, 1, 8, 1, 19, 1, 8, 1, 22, 1, 4, 4, 23, 24, 58, 59, 25, 26, 27, 28, 29, 30, 31, 32, 2, 5]

    def parse(self, args: List[str], arg_idx : List[int]) -> CmdParser | GenCmdParser | ReplaceCmdParser | UpdateCmdParser | ConvertCmdParser | CommentCmdParser | SnippetCmdParser:
        token = args[arg_idx[0]]
        arg_idx[0] += 1
        if token[:2] == '--':
            token = self.long_token(token, args, arg_idx)
            if token == 'help':
                self.help(args, arg_idx)
            elif token == 'verbose':
                self.verbose += 1
            elif token == 'comment':
                self.comment = True
            elif token == 'debug':
                self.debug = True
            elif token == 'timeit':
                self.timeit = True
            elif token == 'update':
                self.update = self.optarg(token, args, arg_idx)
            else:
                self.error(args, arg_idx)
        elif token[:1] == '-':
            arg_idx[1] = 0
            cur_idx = arg_idx[0]
            while cur_idx == arg_idx[0] and (len(token) - 1) > arg_idx[1]:
                arg_idx[1] += 1
                arg_char = arg_idx[1]
                if token[arg_char] == 'h':
                    self.help(args, arg_idx)
                elif token[arg_char] == 'v':
                    self.verbose += 1
                else:
                    print(f'{token=} {arg_char=}')
                    self.error(args, arg_idx)
        else:
            self.error(args, arg_idx)
        return self


@dataclass
class SnippetCmdParser(CmdParser):
    _name: ClassVar[str] = 'snippet'
    list: Optional[bool] = None
    log: str = '/var/tmp/snippet.log'
    arg: list[str] = field(default_factory=list)
    help_nrs: ClassVar(list[int]) = [60, 3, 1, 8, 1, 21, 1, 8, 1, 22, 1, 4, 61, 8, 2, 5, 8, 1, 4, 23, 24, 62, 63, 64, 65, 25, 26, 27, 28, 29, 30, 31, 32, 2, 5]

    def parse(self, args: List[str], arg_idx : List[int]) -> CmdParser | GenCmdParser | ReplaceCmdParser | UpdateCmdParser | ConvertCmdParser | CommentCmdParser | SnippetCmdParser:
        token = args[arg_idx[0]]
        arg_idx[0] += 1
        if token[:2] == '--':
            token = self.long_token(token, args, arg_idx)
            if token == 'help':
                self.help(args, arg_idx)
            elif token == 'verbose':
                self.verbose += 1
            elif token == 'comment':
                self.comment = True
            elif token == 'debug':
                self.debug = True
            elif token == 'timeit':
                self.timeit = True
            elif token == 'list':
                self.list = True
            elif token == 'log':
                self.log = self.optarg(token, args, arg_idx)
            else:
                self.error(args, arg_idx)
        elif token[:1] == '-':
            arg_idx[1] = 0
            cur_idx = arg_idx[0]
            while cur_idx == arg_idx[0] and (len(token) - 1) > arg_idx[1]:
                arg_idx[1] += 1
                arg_char = arg_idx[1]
                if token[arg_char] == 'h':
                    self.help(args, arg_idx)
                elif token[arg_char] == 'v':
                    self.verbose += 1
                else:
                    print(f'{token=} {arg_char=}')
                    self.error(args, arg_idx)
        else:
            self.arg.append(token)
        return self

    def check(self):
        super().check()
        self.check_narg('arg', self.arg, [0, -1])

def parse(cmdarg: typing.List[str]) -> CmdParser | GenCmdParser | ReplaceCmdParser | UpdateCmdParser | ConvertCmdParser | CommentCmdParser | SnippetCmdParser:
    if '--version' in cmdarg:
        if '-v' in cmdarg or '--verbose' in cmdarg:
            return list_versions(pkg_name='cligen', version=None, pkgs=['ruamel.yaml'])
        print(__version__)
        return 0
    arg_idx = [0, 0]
    result = CmdParser()
    if len(cmdarg) == 0:
        cmdarg.append('gen')
    while arg_idx[0] < len(cmdarg):
        result = result.parse(cmdarg, arg_idx)
    result.check()
    return result


def main(cmdarg: typing.Optional[typing.List[str]]=None) -> int:
    cmdarg = sys.argv[1:] if cmdarg is None else cmdarg
    args = parse(cmdarg)
    if isinstance(args, int):
        return args
    config = ConfigYAML(path='cligen')
    cls = getattr(importlib.import_module('cligen.cligen'), 'CligenLoader')
    obj = cls(args, config=config)
    funcname = getattr(args, '_name', None)
    if funcname is None:
        funcname = 'run'
    fun = getattr(obj, funcname + '_subcommand', None)  # type: ignore
    if fun is None:
        fun = getattr(obj, funcname)  # type: ignore
    ret_val = fun()
    if ret_val is None:
        return 0
    if isinstance(ret_val, int):
        return ret_val
    return -1

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


if __name__ == '__main__':
    sys.exit(main())
