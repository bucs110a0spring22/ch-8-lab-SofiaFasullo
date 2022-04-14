class StringUtility:
  
  def __init__(self, string):
    self.string = string
  
  def __str__(self):
    return(self.string)
  
  def vowels(self):
    num_vowels = 0
    for i in self.string:
      if i == "a":
        num_vowels += 1
      elif i == "e":
        num_vowels += 1
      elif i == "i":
        num_vowels += 1
      elif i == "o":
        num_vowels += 1
      elif i == "u":
        num_vowels += 1
      else:
        num_vowels = num_vowels
    if num_vowels > 4:
      return("many")
    else:
      num_vowels = str(num_vowels)
      return(num_vowels)
  
  def bothEnds(self):
    if len(self.string) > 2:
      return self.string[0] + self.string[1] + self.string[-2] + self.string[-1]
    else:
      return ""

  def fixStart(self):
    if len(self.string) > 1:
      first = self.string[0]
      manipulate = self.string[1:len(self.string)]
      replaced = manipulate.replace(first,"*")
      final_list = first.join([first,replaced]) 
      end = len(self.string) + 1
      return final_list[1:end]
    return self.string

  