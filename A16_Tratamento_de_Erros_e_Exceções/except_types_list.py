import builtins

# Lista de todos os tipos integrados, excluindo a classe Exception
built_in_types = [t for t in dir(builtins) if isinstance(getattr(builtins, t), type) and t != 'Exception']

print(built_in_types)
