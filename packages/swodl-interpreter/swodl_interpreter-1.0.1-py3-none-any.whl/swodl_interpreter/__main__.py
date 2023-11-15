from functools import reduce
import re
import json
import logging
import time
import click

from swodl_interpreter.doc import Doc
from swodl_interpreter.repl import repl as relp_func
from swodl_interpreter.mock import Mock
from swodl_interpreter.runner import Runner
from swodl_interpreter.convertor import Converter

traceback = False

@click.group(help='Interpret SWoDL script.')
def main():
    pass

opts = [
    click.argument('file', type=click.File('r')),
    click.option('-h', '--host', help='MAM System host'),
    click.option('-m', '--mock', type=click.Path(exists=True),
        help='Path to mock configuration file.'),
    click.option('-i', '--include_folder', type=click.Path(exists=True, dir_okay=True),
        help='Path to include folder where wf to import stored.'),
    click.option('-in', '--input', multiple=True,
        help='Input parameters. Example "name=value"'),
    click.option('--traceback', is_flag=True,
        help='Show exception trace back.'),
    click.option('--from_line', default=0, help='Use script from line number.',
        show_default=True),
    click.option('--to_line', default=float('inf'), help='Use script to line number.',
        show_default=True),
]

def compose_decorators(*decs):
    return reduce(lambda a, b: b(a), decs)

def executor(f):
    return compose_decorators(f, *opts)

@main.command(help='Run SWoDL script.')
@executor
def run(file, host, mock, include_folder, input, traceback, from_line, to_line):
    execute(False, file, host, mock, include_folder, input, traceback, from_line, to_line, (), False, False)

@main.command(help='Debug SWoDL script.')
@executor
@click.option('-bp', '--brake_point', type=int, multiple=True,
    help='Brake point line numbers')
@click.option('--code', is_flag=True,
    help='Show line where debuger stop')
@click.option('--args', is_flag=True,
    help='Show args on each step')
def debug(file, host, mock, include_folder, input, traceback, from_line, to_line, brake_point, code, args):
    execute(True, file, host, mock, include_folder, input, traceback, from_line, to_line, brake_point, code, args)

def execute(is_debug, file, _host, _mock, _include_folder, _input, traceback, from_line, to_line, _brake_point, _code, _args):
    class Args:
        debug = is_debug
        check_syntax = False
        host = _host
        include_folder = _include_folder
        brake_point = _brake_point
        show_args = _args
        show_code = _code
        mock = _mock
    if _mock:
        Mock.config['mock'] = _mock
    runner = Runner.from_file(file, Args)
    try:
        inputs = [x.split('=') for x in _input or []]
        runner.run({v[0]: json.loads(v[1].replace("'", '"'))
                for v in inputs}, from_line, to_line)
        scope = runner.scope
        if (
            '_ExceptionMessage' in scope.Global
            and scope.Global['_ExceptionMessage']
        ):
            raise Exception(scope.Global['_ExceptionMessage'])
    except Exception as e:
        print(f'\033[91m')
        if traceback:
            logging.exception(e)
        else:
            #logging.error(e)
            click.secho(e, fg='red')
        print(f'\033[0m')
    finally:
        try:
            print(json.dumps(runner.scope.Global, indent=4))
        except:
            pass

@main.command(help='Validate SWoDL script syntax.')
@click.argument('file', type=click.File('r'))
@click.option('-c', '--const', is_flag=True, help='Show all constants')
def validate(file, const):
    class Args:
        check_syntax = True
    runner = Runner.from_file(file, Args)
    for err in runner.validate():
        print(f'Line: {err.line}. Error: {err.msg}')
    if const:
        print(json.dumps(runner.scope.const))

@main.command(help='Lint SWoDL script.')
@click.argument('file', type=click.File('r'))
def lint(file):
    class Args:
        check_syntax = True
    Runner.from_file(file, Args).lint()

@main.command(help='Return SWoDL documentation for keyword.')
@click.argument('keyword', required=False)
def doc(keyword):
    if keyword:
        print(Doc.get(keyword)['doc'])
    else:
        print(json.dumps(Doc.get_all()))

@main.command(help='Generate and update description block in SWoDL script.')
@click.argument('input', type=click.File('r'))
@click.argument('output', type=click.File('w'))
def gen_desc(input, output):
    import re
    new_doc = '/'*110+'\n// Description: (automatically generated from block descriptions - do not edit!)\n//\n'
    wf_text = input.read()
    r = re.findall(r'\/\/(\*)+\n?((\s*\/\/\/.*)+)\s*\[\[([^\]]+)\]\]', wf_text)
    for i, s in enumerate(r):
        new_doc += f'// {i+1}. [[{s[3]}]]\n'
        for d in re.findall(r'\/\/\/\s*([^\n]+)', s[1]):
            new_doc += f'// {d}\n'
        new_doc += '//\n'
    new_doc += '\n\n'
    new_wf = re.sub(r'\/\/\/.*\n// Description: \(automatically generated from block descriptions - do not edit!\)\n(\/\/[^\/]*\n)*',
        new_doc,
        wf_text)
    output.write(new_wf)

@main.command(help='Run SWoDL REPL')
def repl():
    relp_func()


@main.command(help='Get line number of label or function.')
@click.argument('file', type=click.File('r'))
def get_line_for(file):
    class Args:
        check_syntax = True
    runner = Runner.from_file(file, Args)
    n = runner.get_exec_lines()
    print(json.dumps(n))

@main.command(help='Convert to Python file.')
@click.argument('input', type=click.File('r'))
@click.argument('output', type=click.File('w'))
def convert(input, output):
    Converter(input.readlines()).convert(output)

@main.command(help='Run BPM process.')
@executor
@click.option('--wf_folder', type=click.Path(exists=True, dir_okay=True),
    help='Path to workflow folder where  process wf is stored.')
def bpm(file, host, mock, include_folder, input, traceback, wf_folder):
    from swodl_interpreter.bpm import parse
    class Args:
        _host = host
        _mock = mock
        _include_folder = include_folder
        _wf_folder = wf_folder
    p = parse(file, {x.split('=')[0]: x.split('=')[1] for x in input}, args=Args)
    p.run()

if __name__ == '__main__':
    main()
