
{'date': 'Sun Jun 20 2021 20:04:19.910 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
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
  module <module> line 70
    Quadro().vai()
  module <module> line 21
    self.bonequinha = Persona_control(self.fundo)        
TypeError: __init__() missing 1 positional argument: movi
'''},
{'date': 'Sun Jun 20 2021 20:04:34.58 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 32
  def __init__(self, nome_do_fundo, self.movi):
                                    ^
SyntaxError: duplicate argument 'self' in function definition
'''},
{'date': 'Sun Jun 20 2021 20:06:47.258 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
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
  module <module> line 70
    Quadro().vai()
  module <module> line 21
    self.bonequinha = Persona_control(self.fundo,30)        
  module <module> line 35
    movi = self.movi 
AttributeError: 'Persona_control' object has no attribute 'movi'
'''},
{'date': 'Sun Jun 20 2021 20:11:01.174 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
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
  module <module> line 77
    Quadro().vai()
  module <module> line 21
    self.bonequinha = Persona_control(self.fundo,300)        
  module <module> line 44
    self.persona = Elemento(PERSONAGEM, h=100 , w=100, x=self.x, y=self.y)
NameError: name 'PERSONAGEM' is not defined
'''},
{'date': 'Sun Jun 20 2021 20:22:23.523 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
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
  module <module> line 76
    Quadro().vai()
  module <module> line 21
    self.bonequinha = Persona_control(PERSONAGEM, self.fundo)        
TypeError: __init__ missing 2 positional arguments: 'h' and 'w'
'''},
{'date': 'Sun Jun 20 2021 21:22:25.668 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 36
  def __init__(self, variavel_personagem, nome_do_fundo, h =100, w=100, x=10, y=430 movi= 10):
                                                                                     ^
SyntaxError: invalid syntax
'''},
{'date': 'Sun Jun 20 2021 21:28:36.569 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
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
  module <module> line 84
    Quadro().vai()
  module <module> line 21
    self.bonequinha = Persona_control(PERSONAGEM, self.fundo)        
  module <module> line 50
    self.persona = Elemento(self.variavel_personagem, h=self.h , w=self.w, x=self.x, y=self.y)
AttributeError: 'Persona_control' object has no attribute 'x'
'''},
{'date': 'Sun Jun 20 2021 21:42:24.383 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
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
  module <module> line 30
    bonequinha = Persona_control(PERSONAGEM, fundo) 
NameError: name 'Persona_control' is not defined
'''},
{'date': 'Sun Jun 20 2021 21:42:29.83 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
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
  module <module> line 30
    bonequinha = Persona_control(PERSONAGEM, fundo) 
NameError: name 'Persona_control' is not defined
'''},
{'date': 'Sun Jun 20 2021 21:42:31.286 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
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
  module <module> line 30
    bonequinha = Persona_control(PERSONAGEM, fundo) 
NameError: name 'Persona_control' is not defined
'''},
{'date': 'Sun Jun 20 2021 21:42:44.654 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
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
  module <module> line 30
    bonequinha = Persona_control(PERSONAGEM, fundo) 
NameError: name 'Persona_control' is not defined
'''},