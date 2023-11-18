# coding: utf-8
# flake8: noqa


_package_data = dict(
    full_package_name='cligen',
    version_info=(0, 5, 1),
    __version__='0.5.1',
    version_timestamp='2023-11-17 23:33:08',
    author='Anthon van der Neut',
    author_email='a.van.der.neut@ruamel.eu',
    description='generate __main__.py with argparse setup generated from YAML',
    url='https://sourceforge.net/p/ruamel-cligen',
    keywords='generate cli yaml',
    data_files=["_action/*", "_config/*"],
    entry_points='cligen=cligen.__main__:main',
    # entry_points=None,
    license='MIT',
    since=2021,
    # status="α|β|stable",  # the package status on PyPI
    # data_files="",
    # universal=True,  # py2 + py3
    install_requires=['ruamel.yaml'],
    tox=dict(env='3', ),  # *->all p->pypy
    read_the_docs='cligen',
    python_requires='>=3.8',
    print_allowed=True,
)


version_info = _package_data['version_info']
__version__ = _package_data['__version__']


_cligen_data = """\
# all tags start with an uppercase char and can often be shortened to three and/or one
# characters. If a tag has multiple uppercase letter, only using the uppercase letters is a
# valid shortening
# Tags used:
# !Commandlineinterface, !Cli,
# !Option, !Opt, !O
  # - !Option [all, !Action store_true, !Help build sdist and wheels for all platforms]
# !PreSubparserOption, !PSO
# !Alias for a subparser
# - !DefaultSubparser  # make this (one) subparser default
# !Help, !H
# !HelpWidth 40    # width of the left side column width option details 
# !Argument, !Arg
  # - !Arg [files, !Nargs '*', !H files to process]
# !Module   # make subparser function calls imported from module
# !Instance # module.Class: assume subparser method calls on instance of Class imported from module
# !Main     # function to call/class to instantiate, no subparsers
# !Action # either one of the actions in cligen subdir _action (by stem of the file) or e.g. "store_action"
# !Nargs, !N
#    provide a number, '?', '*', or +. Special code is inserted to allow for defaults when +
# !Config YAML/INI/PON  read defaults from config file
# !AddDefaults ' (default: %(default)s)'
# !Prolog (sub-)parser prolog/description text (for multiline use | ), used as subparser !Help if not set
# !Epilog (sub-)parser epilog text (for multiline use | )
# !NQS used on arguments, makes sure the scalar is non-quoted e.g for instance/method/function
#      call arguments, when cligen knows about what argument a keyword takes, this is not needed
!Cli 0:
- !Instance cligen.cligen.CligenLoader
- !Config YAML
- !AddDefaults ' (default: %(default)s)'
- !Option [verbose, v, !Help increase verbosity level, !Action count]
- !Option [comment, !Type bool, !H "don't strip comments from included code (config)"]
- !Option [debug, !Action store_true, !H insert debug statements in generated code]
- !Option [timeit, !Type bool, !H insert code to time from startup to calling method/function']
# - !PSO [config, !Help directory to store, !Default '~/.config/test42/']
- gen:
  - !DefaultSubparser
  - !Option [type, !Default python, !H select python/argparse]
  - !Option [output, !Default __main__.py, !H output to file]
  - !Option [meld, !Type bool, !Help present output as diff for inspection]
  - !Prolog generate __main__.py
- replace:
  - !Prolog replace a string in the _cligen_data/cli.yaml
  - !ReqOption [from, !Dest frm, !H original string to match]
  - !ReqOption [to, !H replacement string]
  - !Option [backup, !Action store_true, !H make a timestamped backup of the file (.YYYYMMDD-HHMMSS)]
  - !Argument
    - path
    - !Nargs '*'
    - !Default ['**/__init__.py', '**/cli.yaml']
    - !H path pattern to scan for replacement
- update:
  - !Prolog |-
    common updates to _cligen_data/cli.yaml
    - remove explicit default adding on !Help if !AddDefaults is set
  - !Option [test, !Action store_true, !Help don't save]
  - !Argument
    - path
    - !Nargs '*'
    - !Default ['**/__init__.py', '**/cli.yaml']
    - !H path pattern to scan for replacement
- convert:
  - !Prolog |-
    analyse argument file that uses ruamel.std.argparse and generate cligen data
    - commands currently cannot have a different name (using set first @subparser argument)
  - !Option [append, !Action store_true, !H append _cligen_data to __init__.py]
  - !Argument [path]
- comment:
  - !Prolog show cligen_data comments (from cligen.__init__.py)
  - !Option [update, !H update cligen_data comments in __init__.py (argument can be directory or file)]
- snippet:
  - !Prolog |-
    work on snippets (site-packages/cligen/_snippet, ~/.config/cligen/snippet), by default insert
    based on matching arguments
  - !Option [list, !Action store_true, !Help list available snippets for current environment]
  - !Option [log, !Default /var/tmp/snippet.log, !Help file to log output to]
  - !Arg [arg, !Nargs '*']
"""
