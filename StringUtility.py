class StringUtility:
  def __init__(self, string):
    self.string = string
  def __str__(self):
    return(self.string)
  def vowels(self):
    count = 0
    for i in self.string:
      if i == "a" or "e" or "i" or "o" or "u":
        count += 1
      else:
        count = count
    if count >= 5:
      return("many")
    else:
      count = str(count)
      return(count)
    
    