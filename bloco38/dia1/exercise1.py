#1 - Primeiro método de executar o clear
def clear(self):
  self.head.value = None
  self.__length = 0

#2 - Segundo método e mais indicado
def clear(self):
  while not self.is_empty():
    self.remove_first()
