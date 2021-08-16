
{'date': 'Mon Aug 16 2021 17:32:32.10 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
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
  module <module> line 108
    teste()
  module <module> line 43
    bonequinha = Persona_control( fundo) 
  module <module> line 80
    self.persona1 = Elemento(PERSONAGEM1, h=170 , w=190, x=self.x, y=self.y) # cria Elemento
NameError: name 'PERSONAGEM1' is not defined
'''},