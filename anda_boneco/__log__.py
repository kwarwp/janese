
{'date': 'Sun Jun 20 2021 16:50:44.225 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 35
  self.cf = dict(A = "(2,3)"
                                  ^
SyntaxError: invalid syntax
'''},
{'date': 'Sun Jun 20 2021 16:50:47.672 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 35
  self.cf = dict(A = "(2,3)"
                                  ^
SyntaxError: invalid syntax
'''},
{'date': 'Sun Jun 20 2021 16:51:05.238 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 180
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 310
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 282
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 299
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 61
    	inicialesquerda().vai()
  module <module> line 17
    self.fundo = Cena(FUNDO)
NameError: name 'FUNDO' is not defined
'''},
{'date': 'Sun Jun 20 2021 16:54:02.100 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 180
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 310
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 282
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 299
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 62
    	inicialesquerda().vai()
  module <module> line 23
    self.bonequinha = bonequinha(self.fundo)
TypeError: __init__() missing 1 positional argument: opcao
'''},