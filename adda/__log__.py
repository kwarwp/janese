
{'date': 'Sun Jul 04 2021 22:26:02.577 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 9
  PERSONAGEM ANDANDO= "https://i.imgur.com/Jo5Ho94.png"
              ^
SyntaxError: invalid syntax
'''},
{'date': 'Mon Jul 05 2021 18:00:16.806 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 25
  self.personagem = Elemento (img = FOLHA, cena = self.fundo, x= self.x2, y= self.y2, h=80, w= 80
                                                                                                                ^
SyntaxError: invalid syntax
'''},
{'date': 'Mon Jul 05 2021 18:01:25.572 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
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
  module <module> line 44
    inicial().vai()
  module <module> line 25
    self.personagem = Elemento(img = FOLHA, cena = self.fundo, x=self.x1, y=self.y1, h=100, w=100)
NameError: name 'FOLHA' is not defined
'''},
{'date': 'Mon Jul 05 2021 18:09:40.659 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 23
  self.personagem = Elemento(img = FOLHA, cena = self.fundo, x=self.x1, y=self.y1, h=80, w=80)
  ^
IndentationError: unexpected indent
'''},
{'date': 'Mon Jul 05 2021 18:10:00.315 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 23
  self.personagem = Elemento(img = FOLHA, cena = self.fundo, x=self.x1, y=self.y1, h=80, w=80)
  ^
IndentationError: unexpected indent
'''},
{'date': 'Mon Jul 05 2021 18:14:29.293 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
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
  module <module> line 50
    inicial().vai()
  module <module> line 22
    self.personagem = Elemento(img = PERSONAGEM, cena = self.fundo, x=self.x1, y=self.y1, h=100, w=100)
AttributeError: 'inicial' object has no attribute 'x1'
'''},