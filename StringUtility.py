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

  def asciiSum(self):
    sum_ascii = 0
    for i in self.string:
      sum_ascii += ord(i)
    return sum_ascii

  def cipher(self):
    #thing = self.string[0:len(self.string)] #for replace attempt
    thing = []
    index = 0
    ORDa = ord("a")
    ORDz = ord("z")
    ORDA = ord("A")
    ORDZ = ord("Z")
    for i in self.string:
      cipher_ascii = ord(i)+len(self.string)
      if ord(i) >= ORDa: #lowercase
        if cipher_ascii > ORDz: #past z
          difference = cipher_ascii-ORDz
          cipher_ascii = ORDa+difference-1 #wraps back around
      if ord(i) < ORDa: #uppercase
        if ord(i) == ord(" "):
          cipher_ascii = ord(" ")
        elif cipher_ascii > ORDZ: #past Z
          difference = cipher_ascii-ORDZ
          cipher_ascii = ORDA+difference-1 #wraps 
      index+=1 ##same
      thing[index:index] = chr(cipher_ascii)
    return "".join(thing)
    