"""Implemenation for Jac's command line interface."""
from __future__ import annotations

def o_Command_a___init__(self, func: callable):
    self.func = func
    self.sig = inspect.signature(func)

def o_Command_a_call(self, *args: list, **kwargs: dict):
    return self.func(*args, **kwargs)

def o_CommandRegistry_a___init__(self):
    self.registry = {}
    self.parser = argparse.ArgumentParser(prog='CLI')
    self.sub_parsers = self.parser.add_subparsers(title='commands', dest='command')

def o_CommandRegistry_a_register(self, func: callable):
    name = func.__name__
    cmd = Command(func)
    self.registry[name] = cmd
    cmd_parser = self.sub_parsers.add_parser(name)
    param_items = cmd.sig.parameters.items
    first = True
    for param_name, param in cmd.sig.parameters.items():
        if param_name == 'args':
            cmd_parser.add_argument('args', nargs=argparse.REMAINDER)
        elif param.default is param.empty:
            if first:
                first = True
                cmd_parser.add_argument(f'{param_name}', type=eval(param.annotation))
            else:
                cmd_parser.add_argument(f'-{param_name[:1]}', f'--{param_name}', required=True, type=eval(param.annotation))
        elif first:
            first = True
            cmd_parser.add_argument(f'{param_name}', default=param.default, type=eval(param.annotation))
        else:
            cmd_parser.add_argument(f'-{param_name[:1]}', f'--{param_name}', default=param.default, type=eval(param.annotation))
    return func

def o_CommandRegistry_a_get(self, name: str):
    return self.registry.get(name)

def o_CommandRegistry_a_items(self):
    return self.registry.items()

def o_CommandShell_a___init__(self, cmd_reg: CommandRegistry):
    self.cmd_reg = cmd_reg
    cmd.Cmd.__init__(self)

def o_CommandShell_a_do_exit(self, arg: list):
    return True

def o_CommandShell_a_default(self, line: str):
    try:
        args = vars(self.cmd_reg.parser.parse_args(line.split()))
        command = self.cmd_reg.get(args['command'])
        if command:
            args.pop('command')
            ret = command.call(**args)
            if ret:
                print(ret)
    except Exception as e:
        print(e)

def a_start_cli():
    parser = cmd_registry.parser
    args = parser.parse_args()
    command = cmd_registry.get(args.command)
    if command:
        args = vars(args)
        args.pop('command')
        ret = command.call(**args)
        if ret:
            print(ret)
    else:
        shell = CommandShell(cmd_registry).cmdloop()