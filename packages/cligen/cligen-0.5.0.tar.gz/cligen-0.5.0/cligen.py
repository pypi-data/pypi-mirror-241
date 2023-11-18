# coding: utf-8

from __future__ import annotations

"""
the input is versioned based on key for the root mapping
the ouput is determined by --output python/argparse
"""

import sys
import os
import io
import datetime
from pathlib import Path
from _ast import *  # NOQA
from ast import parse
import warnings

from . import __version__  # NOQA

import ruamel.yaml

warnings.simplefilter('ignore', ruamel.yaml.error.ReusedAnchorWarning)


# the imports are dynamically generated, primarily from imports needed for included actions
# verimp, normally gets __version__ and _package_data from the __init__.py file (import . )
# but this can be changed to some other file

VERSION = '__version__'
PKG_DATA = '_package_data'


class CligenLoader(object):
    """
    This class is separate from CliGenBase, so it can properly instantiate
    the CliGenBase subclass based on version ( CliGen0, etc. )
    """

    def __init__(self, args, config=None):
        self._args = args
        self._config = config
        self.verimp_file = None
        self._extend_main = None
        self._pd = None

    @property
    def verbose(self):
        try:
            return self._verbose
        except AttributeError:
            pass
        self._verbose = res = getattr(self._args, 'verbose', 0)
        return res

    def gen_subcommand(self):
        # self._args often not available when called from import
        verbose = getattr(self._args, 'verbose', 0)
        if verbose > 1:
            print('cwd:', os.getcwd())
        yaml = ruamel.yaml.YAML()
        yaml.width = 132
        # parse data sources (cli.yaml, __init__.py), only one
        # is allowed to be present (checked)
        datas_found = []
        cli_yaml_file = Path('cli.yaml')
        if cli_yaml_file.exists():
            if verbose > 0:
                print('found:', cli_yaml_file)
            datas_found.append(yaml.load(cli_yaml_file))
        init_file = Path('__init__.py')
        if init_file.exists():
            # extract both package data and YAML in one go
            _end = None
            pds = None  # package data
            ys = None  # yaml string
            for line in init_file.open():
                if pds is None and PKG_DATA in line:
                    _end = ')' if 'dict(' in line else '}'
                    pds = collect = [line.split('=')[1].lstrip()]
                    continue
                if ys is None and '_cligen_data' in line:
                    ys = collect = []
                    _end = line.split('=')[1].lstrip()[:3]
                    if verbose > 0:
                        print('found: _cligen_data in', init_file)
                    continue
                if _end is None:
                    continue
                # if line.strip().startswith(_end):  # not working on develop
                if line.startswith(_end):
                    if pds is collect:
                        pds.append(line)
                    _end = None
                    continue
                if collect is not None:
                    collect.append(line)
            if pds is not None:
                try:
                    self._pd = literal_eval(''.join(pds))
                except SyntaxError as e:
                    print(f'{e=}')
                    for idx, line in enumerate(pds):
                        print(f'{idx:2}: {line}', end='')
                    raise

            if ys is not None:
                datas_found.append(yaml.load(''.join(ys)))
        # make sure only one data source exists
        if len(datas_found) == 0:
            print('no input found ( __init__.py with _cligen_data / cli.yaml )')
            return
        elif len(datas_found) == 2:
            print('multiple input found ( __init__.py with _cligen_data / cli.yaml )')
            return
        # update and/or check some cligen syntax changes
        # in principle can have multiple versions in one document
        if isinstance(datas_found[0], dict):
            for k, v in datas_found[0].items():
                try:
                    if k.tag.value == '!Cli':
                        version = int(k.value)
                        data = v
                except (KeyError, AttributeError):
                    continue
                try:
                    # this is used _test/test_data.py
                    if k.tag.value in ['!File', '!ImportFile']:
                        assert isinstance(k.value, str)
                        assert isinstance(v, str)
                        path = Path(k.value)
                        if path.name == '__main__.py':
                            self._extend_main = '\n\n' + v + '\n'
                            continue
                        if k.tag.value == '!ImportFile':
                            # sets the name of the from x import __version__, defaults to .
                            self.verimp_file = path
                            if self._pd is None:
                                _end = None
                                pds = None  # package data
                                for line in v.splitlines():
                                    if pds is None and PKG_DATA in line:
                                        _end = ')' if 'dict(' in line else '}'
                                        pds = [line.split('=')[1].lstrip()]
                                        continue
                                    if _end is None:
                                        continue
                                    if line.startswith(_end):
                                        pds.append(line)
                                        _end = None
                                        continue
                                    pds.append(line)
                                if pds is not None:
                                    try:
                                        self._pd = literal_eval(''.join(pds))
                                    except SyntaxError as e:
                                        print(f'{e=}')
                                        for idx, line in enumerate(pds):
                                            print(f'{idx:2}: {line}', end='')
                                        raise
                        if path.parent != '.':
                            path.parent.mkdir(parents=True, exist_ok=True)
                        path.write_text(v)
                except KeyError:
                    pass
            if verbose > 0:
                print('data from dict version:', version)
        elif isinstance(datas_found[0], list):
            data = datas_found[0]
            assert data.tag.value == '!Cli'
            data = list(data)
            version = 0
        else:
            print('data typ unknown', type(data))
            return

        if version == 0:
            dbg = getattr(self._args, 'debug', None)
            comment = getattr(self._args, 'comment', False)
            cligen_type = os.environ.get('CLIGEN_TYPE', self._args.type)
            if cligen_type == 'python':
                from .cligen0python import CliGen0Python

                cligen = CliGen0Python(
                    data,
                    verimp_file=self.verimp_file,
                    extend_main=self._extend_main,
                    pkg_data=self._pd,
                    debug=dbg,
                    comment=comment,
                    loader=self,
                )
            elif cligen_type == 'argparse':
                from .cligen0argparse import CliGen0Argparse

                cligen = CliGen0Argparse(
                    data,
                    verimp_file=self.verimp_file,
                    extend_main=self._extend_main,
                    pkg_data=self._pd,
                    debug=dbg,
                    comment=comment,
                    loader=self,
                )
            else:
                print('unknown type', cligen_type)
                sys.exit(1)
        else:
            print('unknown !Cli version', version)
            return
        # cligen.walk()
        buf = io.StringIO()
        cligen.gen_parser(fp=buf)  # have to run gen_parser first to set lists for gen_pre
        # print(buf.getvalue())

        test_py = Path('__main__.py')
        if test_py.exists() and self._args.meld:
            import tempfile

            with tempfile.NamedTemporaryFile('w', prefix='oitnb_') as fp:
                cligen.gen_pre(fp=fp)
                fp.write(buf.getvalue())
                cligen.gen_post(fp=fp)
                fp.flush()
                os.system(f'meld -n "{fp.name}" "{test_py!s}"')
            return
        if verbose > 0:
            print('writing __main__.py')
        with test_py.open('w') as fp:
            cligen.gen_pre(fp=fp)
            fp.write(buf.getvalue())
            cligen.gen_post(fp=fp)

    def replace(self):
        from .scanner import Scanner

        scanner = Scanner(self._args.path)
        for found in scanner():
            found.replace(self._args.frm, self._args.to, backup=self._args.backup)

    def update(self):
        from .scanner import Scanner

        scanner = Scanner(self._args.path)
        for found in scanner():
            found.update(self._args)

    def convert(self):
        import subprocess

        mdl = 'eppa.ooo'
        if self._args.path == '.':
            try:
                mdl = os.getcwd().split('/py/')[1].replace('/', '.')
            except Exception:
                mdl = os.getcwd().split('/site-packages/')[1].replace('/', '.')
            initpy = Path(os.getcwd()) / '__init__.py'
        else:
            mdl = self._args.path
            initpy = Path(self._args.path).resolve() / '__init__.py'
        os.chdir('/')
        os.environ['CLIGENCONVERT'] = '1'
        print('setting env.: CLIGENCONVERT=1')
        cmd = [sys.executable, '-m', mdl, '--cligen']
        print('cmd:', ' '.join(cmd), end='\n\n')
        try:
            res = subprocess.check_output(cmd, stderr=subprocess.STDOUT).decode('utf-8')
        except Exception as e:
            print('exception res:\n', e.output.decode('utf-8'), '\n', e, sep='')
        else:
            print('res:\n', sep='')

        lines = []
        for line in res.splitlines():
            print(line)
            if line.startswith('_cligen_data'):
                if self._args.append:
                    lines.append(line)
                self.insert_comments_from_cligen_init(
                    lines if self._args.append else None, verbose=1,
                )
                continue
            if self._args.append and lines:
                lines.append(line)
            if line.startswith('"""'):
                break

        if self._args.append:
            if lines:
                assert initpy.exists()
                with initpy.open('a') as fp:
                    fp.write('\n')
                    fp.write('\n'.join(lines))
                    fp.write('\n')
        return

    def comment(self, update=None):
        update = self._args.update if update is None else update
        if update is None:
            self.insert_comments_from_cligen_init(None, verbose=1)
            return
        path = Path(update)
        if path.is_dir():
            path /= '__init__.py'
        pos = -1
        lines = []
        doit = False
        for idx, line in enumerate(path.read_text().splitlines()):
            if doit and line.lstrip().startswith('#'):
                continue
            elif line.startswith('_cligen_data'):
                pos = idx + 1
                doit = True
            elif doit:
                doit = False
            lines.append(line)
        assert pos != -1

        add_lines = []
        self.insert_comments_from_cligen_init(add_lines, verbose=0)
        lines[pos:pos] = add_lines
        path.write_text('\n'.join(lines) + '\n')

    def insert_comments_from_cligen_init(self, lines, verbose=0):
        """show and append commentlines at top of cligen_data in cligen's __init__.py"""
        ununinit = Path(__file__).parent / '__init__.py'
        doit = False
        for line in ununinit.open():
            if doit and line.lstrip().startswith('#'):
                if verbose > 0:
                    print(line, end='')
                if lines is not None:
                    lines.append(line.rstrip())
                continue
            elif line.startswith('_cligen_data'):
                doit = True
                continue
            doit = False

    def snippet_subcommand(self):
        with Path(self._args.log).expanduser().open('a') as out:
            # typ = os.environ['kak_opt_filetype']
            try:
                typ = Path(os.environ['kak_buffile']).suffix
            except Exception:
                typ = '.py'
            return self.snippet(out, typ)

    def snippet(self, out, typ=''):
        """
        test with "echo '' | cligen snippet arg1 arg2 "
        """
        debug = False
        print(datetime.datetime.now(), '\nsnippet', self._args.arg, typ, file=out)
        if debug:
            print(datetime.datetime.now(), '\nsnippet', self._args.arg, file=sys.stderr)
        if self._args.list:
            print('list', file=out)
            for k in self.find_dir('snippet', typ=typ):
                print(' ', k, file=out)
                print(' ', k, file=sys.stderr)
            return
        kakoune_selected = sys.stdin.read()
        start_matches = []
        matches = []
        if debug:
            print('args', self._args.arg)
        if self._args.arg:
            arg0 = self._args.arg[0]
            for k, v in self.find_dir('snippet', typ=typ).items():
                if k == arg0:
                    matches = [v]
                    break
                if k.startswith(arg0):
                    start_matches.append(v)
                if arg0 in k:
                    matches.append(v)
        if len(matches) > 1 and len(start_matches) == 1:
            matches = start_matches
        print('snip matches', matches, file=out)
        print('snip matches', matches, file=sys.stderr)
        res = ''
        if len(matches) == 1:
            try:
                res = matches[0].read_text().format(*self._args.arg[1:])
            except IndexError as e:
                print(f'error expanding snippet {matches[0]}, {e}', file=out)
                print(f'error expanding snippet {matches[0]}, {e}', file=sys.stderr)

        print('snip', self._args.arg, repr(kakoune_selected), os.getcwd(), file=out)
        for k, v in sorted(os.environ.items()):
            if k.startswith('kak_'):
                print('env', k, '->', v, file=out)
        sys.stdout.write(kakoune_selected + res)
        out.flush()

    def find_dir(self, dname, typ='', dbg=None):
        # if dname == 'action', search ~/.config/cligen/action and `_action` in current dir
        if dbg is None:
            dbg = getattr(self._args, 'debug', None)
        res = {}
        if self._config:
            ddir = self._config._path.parent / dname
            if dbg:
                print(f'trying to find {dname} under', ddir)
            for fn in ddir.glob('*' + typ):
                name = fn.name
                if name == '__init__.py':
                    continue
                res[name] = fn
        ddir = Path(__file__).parent / ('_' + dname)
        if dbg:
            print(f'trying to find _{dname} under', ddir)
        for fn in ddir.glob('*' + typ):
            name = fn.name
            if name not in res:  # config/_action is preferred:
                res[name] = fn
        if dbg:
            for k, v in sorted(res.items()):
                print(f'>>> {k:9s} ->', v)
        return res


class CliGenBase:
    def __init__(
        self,
        data,
        verimp_file=None,  # if not None, replace the dot in "from . import __version__"
        extend_main=None,  # text from document to insert in __main__.py
        pkg_data=None,   # mapping read and eval-ed from __info__
        debug=False,  # insert debug statements in generated code
        comment=False,  # strip comments from included code (_actions/_config)
        loader=None,   # only used for find_dir, to find data under config dir and parent of __file__  # NOQA
    ):
        self._data = data
        self.extend_main = extend_main
        self._pkg_data = pkg_data
        self._debug = debug
        self._comment = comment
        assert loader is not None
        self._loader = loader
        self._import_line = self.scan_import_file(
            verimp_file,
        )  # to check for generating --version handling
        self._global_options = []  # inherited options from main to subparsers
        self.sub_parsers = None  # list of single key-value pairs
        self._default_subparser = None
        self._global_default_options = []
        self._import_from_module = self._instantiate = self._no_sub_parser = None
        self.smart_formatter = False
        self._help_all = True
        self._pre_subparser_option_tags = {'!PreSubparserOption', '!PSO'}
        self._option_tags = {'!Option', '!Opt', '!O', '!ReqOption', '!ReqOpt'}
        self._arg_tags = {'!Argument', '!Arg', '!A'}
        self._all_option_tags = self._pre_subparser_option_tags | self._option_tags
        self._tag_map = {}
        self.add_tag('Help H')
        self.add_tag('AddDefaults')
        self.add_tag('Prolog', 'description')
        self.add_tag('Epilog')
        self.add_tag('Action')
        self.add_tag('Nargs N')
        self._no_quotes = {'some_action', 'float', 'int'}
        self._add_defaults = None
        self._max_help_position = 40
        self._shorthands = {}

    @property
    def debug(self):
        return self._debug

    def add_tag(self, tags, key=None):
        # if key not given use first tag -> lowercase
        if not isinstance(tags, list):
            tags = tags.split()
        if key is None:
            key = tags[0].lower()
        for t in tags:
            self._tag_map[t] = key

    def scan_import_file(self, fn):
        """
        return the string used for importing version and data
        """
        imp_fn = '.' if fn is None else str(fn.with_suffix(''))
        imports = []
        try:
            for line in open('__init__.py' if fn is None else fn):
                if line.startswith(VERSION):
                    imports.append(VERSION)
                if not self._pkg_data and line.startswith(PKG_DATA):
                    imports.append(PKG_DATA)
            if imports:
                return f'\n\nfrom {imp_fn} import {", ".join(imports)}\n'
        except FileNotFoundError:
            pass
        return ''

    def clean_name(self, s):
        """cannot have dash in name -> underscore"""
        for k, v in {'-': '_'}.items():
            s = s.replace(k, v)
        return s

    def load_configs(self, dir, comment=False):
        # returns a mapping of file_name_stem name to imports/class_name/class_body
        # might be better off using the stem as the lookup
        # - import lines should come before the class statement
        # - any comments before the class statement are dropped
        # - comments after the class statement are dropped unless comment is True
        # this cannot handle # as the first non-blank line within a multiline python string!
        res = {}
        for _fn, config_file in sorted(self._loader.find_dir(dir).items()):
            if config_file.name == '__init__.py':
                continue
            import_lines, body = config_file.read_text().split('class ')
            imports = set()
            for line in import_lines.splitlines():
                # handle YAML that specifies default parameters for config
                if line.startswith('import '):
                    for x in line.split(' ', 1)[1].split(','):
                        imports.add(x)
            name = body.split('(', 1)[0]
            if ':' in name:
                name = body.split(':')[0]
            if not comment:
                body = ''.join(
                    [m for m in body.splitlines(True) if not m.lstrip().startswith('#')],
                )
            body = body.rstrip() + '\n'
            res[config_file.stem] = dict(imports=imports, name=name, body='class ' + body)
        return res

    def load_actions(self, dir, clsdef='def ', comment=False):
        # returns a mapping of class name to
        # imports/class_body/filename_stem/default_parameters
        # using the stem of the directory as the lookup
        # - import lines and parameters should come before the class statement
        # - any comments before the class statement are dropped
        # - comments after the class statement are dropped unless comment is True
        # this cannot handle # as the first non-blank line within a multiline python string!
        res = {}
        for fn, action_file in sorted(self._loader.find_dir(dir).items()):
            params = {}
            in_params = []
            import_lines, body = action_file.read_text().split(clsdef, 1)
            body = body.rstrip() + '\n'
            imports = set()
            for line in import_lines.splitlines():
                # handle YAML that specifies default parameters for action
                if line.startswith('_parameters = '):
                    in_params.append(line)
                    # print('xxx', line[15])
                    continue
                if in_params:
                    if line.startswith(in_params[0][15] * 3):
                        params = ruamel.yaml.YAML(typ='safe').load('\n'.join(in_params[1:]))
                        in_params = None
                    else:
                        in_params.append(line)
                    continue
                if line.startswith('import '):
                    for x in line.split(' ', 1)[1].split(','):
                        imports.add(x)
            if not comment:
                body = ''.join(
                    [m for m in body.splitlines(True) if not m.lstrip().startswith('#')],
                )
            res[os.path.basename(fn).split('.')[0]] = dict(
                imports=imports, body=clsdef + body, stem=action_file.stem, params=params,
            )
        return res


def quoted(s, q="'"):
    s = str(s)  # could be Path or integer
    if s and (s[0] not in '"\'' or s[0] != s[-1]):
        s = q + s + q
    return s


if sys.version_info >= (3, 8):
    from ast import Str, Num, Bytes, NameConstant  # NOQA


def literal_eval(node_or_string):
    """
    Safely evaluate an expression node or a string containing a Python
    expression.  The string or node provided may only consist of the following
    Python literal structures: strings, bytes, numbers, tuples, lists, dicts,
    sets, booleans, and None.

    Even when passing in Unicode, the resulting Str types parsed are 'str' in Python 2.
    I don't now how to set 'unicode_literals' on parse -> Str is explicitly converted.
    """
    _safe_names = {'None': None, 'True': True, 'False': False}
    if isinstance(node_or_string, str):
        node_or_string = parse(node_or_string, mode='eval')
    if isinstance(node_or_string, Expression):
        node_or_string = node_or_string.body
    else:
        raise TypeError('only string or AST nodes supported')

    def _convert(node):
        if isinstance(node, Str):
            if sys.version_info < (3,) and not isinstance(node.s, unicode):
                return node.s.decode('utf-8')
            return node.s
        elif isinstance(node, Bytes):
            return node.s
        elif isinstance(node, Num):
            return node.n
        elif isinstance(node, Tuple):
            return tuple(map(_convert, node.elts))
        elif isinstance(node, List):
            return list(map(_convert, node.elts))
        elif isinstance(node, Set):
            return set(map(_convert, node.elts))
        elif isinstance(node, Dict):
            return {_convert(k): _convert(v) for k, v in zip(node.keys, node.values)}
        elif isinstance(node, NameConstant):
            return node.value
        elif sys.version_info < (3, 4) and isinstance(node, Name):
            if node.id in _safe_names:
                return _safe_names[node.id]
        elif (
            isinstance(node, UnaryOp)
            and isinstance(node.op, (UAdd, USub))
            and isinstance(node.operand, (Num, UnaryOp, BinOp))
        ):  # NOQA
            operand = _convert(node.operand)
            if isinstance(node.op, UAdd):
                return +operand
            else:
                return -operand
        elif (
            isinstance(node, BinOp)
            and isinstance(node.op, (Add, Sub))
            and isinstance(node.right, (Num, UnaryOp, BinOp))
            and isinstance(node.left, (Num, UnaryOp, BinOp))
        ):  # NOQA
            left = _convert(node.left)
            right = _convert(node.right)
            if isinstance(node.op, Add):
                return left + right
            else:
                return left - right
        elif isinstance(node, Call):
            func_id = getattr(node.func, 'id', None)
            if func_id == 'dict':
                return {k.arg: _convert(k.value) for k in node.keywords}
            elif func_id == 'set':
                return set(_convert(node.args[0]))
            elif func_id == 'date':
                return datetime.date(*[_convert(k) for k in node.args])
            elif func_id == 'datetime':
                return datetime.datetime(*[_convert(k) for k in node.args])
        err = SyntaxError('malformed node or string: ' + repr(node))
        err.filename = '<string>'
        err.lineno = node.lineno
        err.offset = node.col_offset
        err.text = repr(node)
        err.node = node
        raise err

    return _convert(node_or_string)
