
{'date': 'Mon Aug 24 2020 19:54:59.502 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 40
  def vai(self):
  ^
IndentationError: unexpected indent
'''},
{'date': 'Mon Aug 24 2020 20:24:27.557 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 177
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 306
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 278
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 295
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 57
    Estrutura().vai()
  module <module> line 42
    self.ik.onmouseenter(self.mostra)
AttributeError: 'Elemento' object has no attribute 'onmouseenter'
'''},
{'date': 'Mon Aug 24 2020 20:24:42.500 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 177
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 306
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 278
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 295
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 57
    Estrutura().vai()
  module <module> line 42
    self.ik.elt.onmouseenter(self.mostra)
TypeError: 'NoneType' object is not callable
'''},