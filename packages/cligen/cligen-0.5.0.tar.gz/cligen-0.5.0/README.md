
# cligen

[![image](https://sourceforge.net/p/ruamel-cligen/code/ci/default/tree/_doc/_static/license.svg?format=raw)](https://opensource.org/licenses/MIT)
[![image](https://sourceforge.net/p/ruamel-cligen/code/ci/default/tree/_doc/_static/pypi.svg?format=raw)](https://pypi.org/project/cligen)
[![image](https://sourceforge.net/p/oitnb/code/ci/default/tree/_doc/_static/oitnb.svg?format=raw)](https://bitbucket.org/ruamel/oitnb/)

cligen is is a utility to generate command-line parsing code, writing
your `__main__.py` from a specification in YAML. The generated
code requires Python 3.8+.

For a commandline utility `direction` that needs the subcommands `left`
and `right`, and where the subcommand `left` can have the option
`--u-turn` (assuming you drive on the right side of the road), and both
subcommands could have a `--verbose` option would look like:

    !Cli 0:
    - !Instance driving.Direction
    - !Option [verbose, v, !Help increase verbosity level, !Action count]
    - left:
      - !Help turning to the left
      - !Option [u-turn, U, !Action store_true, !Help make a U-turn]
    - right:
      - !H turning to the right

with the result that `direction left -h` will generate:

    usage: direction left [-h] [--u-turn] [--verbose]

    optional arguments:
      -h, --help     show this help message and exit
      --u-turn, -U   make a U-turn
      --verbose, -v  increase verbosity level

When `direction left` is called from the command-line, the code in `__main__.py` 
will create an instance of the class `Direction` imported from `driving.py`, providing
the result of the parsing as argument to the intialisation,
and then call the method `left_subcommand` or method `left` (trying in that order) of that class. 
`cligen` can alternatively generate code that calls functions
imported from a Python file, or call code inserted from the
YAML specification in `__main__.py` itself (in this case the `..._subcommand` 
is not tried, and the results of parsing passed in to the function).

The YAML document can either be in a file `cli.yaml` on its own, or, if you
want to diminish file clutter in your project root, it can be stored in
the variable `_cligen_data` in `__init__.py`, this means between the
following two lines in that file:
```
_cligen_data = """\
"""
```
The YAML document uses
various tags, many of which have a short version (e.g. `!H` is equivalent
to using `!Help`).

Having the commandline options and argument data in a programmatically
modifiable format like YAML, makes it more easy to check or manipulate all
your utilities. E.g. if you want to make sure that all utilities that
have a `--verbose` option also have a `--quiet` option that
decreases the verbosity level.

## Feature list
-   multiple long (`--date`) and short options (`-D`) can be associated with
    one target. 

-   additional smart types/actions. E.g. an option with type 'date' defaults to `datetime.date.today()`
    and you can specify an argument like `yesterday` or `-w-2` (two weeks ago)

-   allows defaults, with optionally some defaults updated from a configuration 
    file

-   nested parsers for subcommands, and subcommands inherit options of the parent,
    unless explicitly indicated that they schouldn't. This allows you to
    insert such options before or after the subcommand.

-   no dependencies on anything but the Python standard library, 
    unless your config file is in a format that requires some installed
    library ( YAML -\> ruamel.yaml )

-   allow YAML aliases for tagged scalars to be used by other tags:

        - !Help &xhelp text1 text2 text3  # this is the same as: "&xhelp !Help text1 text2 text3"
        - !Prolog [*xhelp]                # xhelp is a tagged scalar, "!Prolog *xhelp" would error

## Using !Config

In its most explicit form the tag `!Config` can takes a two element
sequence as value. The first element indicates the *type* (`pon`,
`yaml`, `ini`, TBI: `json`), the second the *path* to the file. A path
starting with a tilde (`~`) will be expanded. A path not starting with
tilde, or (forward-)slash (`/`), will be appended to your users config
directory.

If `!Config` is followed by a scalar that looks like a path (i.e. the
value starts with `~` or includes a `/`) the extension of the path is
taken to be the *type*. In other cases `!Config` is assumed to be
followed by a *type* and the basename is derived from the package name
(`_package_data['full_package_name']`) in your users config directory.

A user config directory is based on XDG config locations (on Windows,
the config information is expected under `%APPDATA%`)

When `!Config` is specified the inserted code will check for
`--config some_explicit_path` on the commandline and load the config
data from the path specified.

### config file format

Config files are assumed to contain a dictionary at the root level (for
formats like `.ini` the data is converted to a dictionary during
loading). This dictionary contains keys that correspond to the various
subparsers. A section `global` (or optionally `glbl` in PON to prevent
use of a reserved keyword, renamed to `global` after loading), is used
for defaults for options that come before the subparser as well as for
global options. Each section consists of key-value pairs, where the key
corresponds to a long option (`--verbose`) or if that is not available
the short option (`-v`), either without the leading dashes.

Assuming you have the following configuration:

    !Cli 0:
    - !Opt [verbose, v, !H increase verbosity, !Action count]
    - !Config [pon, /usr/local/etc/myutil.pon]
    - subp1: []

your `myutil.pon` can use:

    dict(glbl=dict(verbose=2))

to set the verbosity (you might want to format your PON somewhat nicer.

The same with a YAML file:

    !Cli 0:
    - !Opt [verbose, v, !H increase verbosity, !Action count]
    - !Config YAML
    - subp1: []

your `~/.config/your_util_name/your_util_name.yaml` would be:

    global:
      verbose: 2

## argparse

An earlier version of cligen generated `argparse` commmands
in the `__main__.py` file. The current python output doesn't 
use `argparse` anymore, resulting in code that is about twice as 
big, but also twice as fast.

The old, unmaintained, code generator can be invoked by providing
`--type argparse`
