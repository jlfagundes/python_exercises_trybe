class Stack():
  def __init__(self):
    self.data = list()

  def size(self):
    return len(self._data)

  def is_empty(self):
    return not bool(self.size())