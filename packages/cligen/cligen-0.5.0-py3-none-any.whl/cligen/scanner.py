import datetime
from pathlib import Path

import ruamel.yaml

RYTS = ruamel.yaml.comments.TaggedScalar


class Scanner:
    """scans for files to update"""

    def __init__(self, patterns):
        self._patterns = patterns

    def __call__(self):
        base_path = Path('.')
        for pattern in self._patterns:
            for fn in base_path.glob(pattern):
                if fn.is_dir():
                    continue
                if '/new/templates' in str(fn.parent):
                    continue
                upd = Updater(fn)
                if upd.todo:
                    yield upd


class Updater:
    var_name = '_cligen_data'

    def __init__(self, path):
        self._todo = True
        self._path = path
        text = path.read_text()
        if self.init_file:
            if self.var_name not in text:
                self._todo = False
                return
        self._text = text.splitlines()
        self._start_line = 0
        self._end_line = len(self._text)

    @property
    def init_file(self) -> bool:
        return self._path.name == '__init__.py'

    @property
    def todo(self):
        return self._todo

    def replace(self, frm, to, backup=None):
        changed = False
        for idx, line in enumerate(self._text):
            if idx < self._start_line:
                continue
            if idx > self._end_line:
                break
            if frm in line:
                if not changed:
                    changed = True
                    print('fn', self._path)
                print(' <', line)
                newline = line.replace(frm, to)
                print(' >', newline)
                self._text[idx] = newline
        if not changed:
            return
        backup_path = (
            self._path.parent / f'{self._path.name}.{datetime.datetime.now():%Y%m%d-%H%M%S}'
        )
        self._path.rename(backup_path)
        self._path.write_text('\n'.join(self._text) + '\n')

    def set_range(self):
        """ set start and end line"""
        if not self.init_file:
            return
        start_found = False
        for idx, line in enumerate(self._text):
            if line.startswith(self.var_name):
                if line[len(self.var_name) :] != ' = """\\':
                    print(f'>>> check {self._path}, line {idx}: {line}')
                    return
                start_found = True
                self._start_line = idx + 1
                continue
            if not start_found:
                continue
            try:
                if line and line.split()[0] == '"""':
                    self._end_line = idx - 1
                    return
            except IndexError:
                print('indexerror in set_range', repr(line))

    def update(self, args) -> None:
        def update_values(data, **kw):
            """
            expand this to do other on individual values
            kw used to have a static argument to the recursive call
            """
            if kw.get('add_defaults') is None:
                return
            if isinstance(data, dict):
                for k, v in data.items():
                    if (res := update_values(v, **kw)) is not None:
                        data[k] = res
            elif isinstance(data, list):
                for idx, elem in enumerate(data):
                    if (res := update_values(elem, **kw)) is not None:
                        data[idx] = res
            elif isinstance(data, RYTS):
                if str(data.tag) in ['!H', '!Help']:
                    if (
                        ad := kw.get('add_defaults')
                    ) is not None and '%(default)s' in data.value:
                        if ad in data.value:
                            # copy attributes refers to YAML attributes and doesn't copy value
                            return data.copy_attributes(
                                RYTS(data.value.replace(ad, '').strip()),
                            )
                            # could also just update the value, without returning, as that
                            # would make this a string
                            # data.value = data.value.replace(ad, '').strip()
                        else:
                            print(
                                '>>> %(default)s found but not matching !AddDefault',
                                repr(data.value),
                            )
            else:
                pass

        changed = False
        self.set_range()
        if self._path.suffix == '.py' and self._start_line == 0:
            # library without generated __main__.py
            return
        try:
            data = self.yaml.load('\n'.join(self._text[self._start_line : self._end_line + 1]))
        except Exception:
            print('file:', self._path, 'lines', self._start_line, self._end_line)
            raise
        if data is None:
            print('no data in', self._path)
            return
        for x in data.values():
            break
            for elem in x:
                if isinstance(elem, dict):
                    for k, v in elem.items():
                        if k == 'show':
                            print(type(elem))
                            print(elem.ca)
                            print(type(v))
                            print(v.ca)
                            print(f'{v=}', type(v))
                            print(f'{v.ca=}')
                            print(f'{v[0].ca=}')
        ##
        assert len(data) == 1
        tl_key = list(data.keys())[0]
        assert str(tl_key.tag) == '!Cli'
        add_defaults = None
        for cli_setting in list(data.values())[0]:
            # print(str(cli_setting.tag))
            if str(cli_setting.tag) == '!AddDefaults':
                # print('AddDefaults', cli_setting)
                add_defaults = str(cli_setting)
        # print(data, data.tag)
        update_values(data, add_defaults=add_defaults)
        for idx, _line in enumerate(self._text):
            if idx < self._start_line:
                continue
            if idx > self._end_line:
                break
            # print(line)
        # print('range', self._start_line, self._end_line, self._path)
        changed, upd = self.compare_yaml(data)
        if not changed or args.test:
            print('up-to-date:', self._path)
            return
        backup_path = (
            self._path.parent / f'{self._path.name}.{datetime.datetime.now():%Y%m%d-%H%M%S}'
        )
        self._path.rename(backup_path)
        all_lines = self._text[: self._start_line] + upd + self._text[self._end_line :]
        self._path.write_text('\n'.join(all_lines) + '\n')

    def compare_yaml(self, data):
        """compare with the original lines"""
        import ruamel.yaml.string
        import difflib

        yaml = ruamel.yaml.YAML(typ=['rt', 'string'])
        yaml.preserve_quotes
        yaml.width = 2048
        upd = yaml.dump_to_string(data).splitlines()
        # print(upd)
        changed = False
        for line in difflib.unified_diff(
            self._text[self._start_line : self._end_line + 1], upd, str(self._path), 'updated',
        ):
            changed = True
            print(line)
        return changed, upd

    @property
    def yaml(self):
        try:
            return self._yaml
        except AttributeError:
            pass
        self._yaml = res = ruamel.yaml.YAML()
        return res
