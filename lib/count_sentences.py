#!/usr/bin/env python3
import re

class MyString:
  def __init__(self, value=''):
    self._value = value

  def get_value(self):
    return self._value
  
  def set_value(self, value):
    if isinstance(value, str):
      self._value = value
    else:
      print("The value must be a string.")

  value = property(get_value, set_value)

  def is_sentence(self):
    return self._value.endswith(".")
  
  def is_question(self):
    return self._value.endswith("?")
  
  def is_exclamation(self):
    return self._value.endswith("!")
  
  def count_sentences(self):
    if self._value:
      mod_value = re.split("[.]|[?]|[!]", self._value)
      while "" in mod_value:
        mod_value.remove("")
      return len(mod_value)
    else:
      return 0

simple_string = MyString("one. two. three?")
print(simple_string.count_sentences())