__author__ = 'dongpei'


1 == 1 and \
2 == 2

b = 1+2+3\
    +4

class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

def put(self,key,data):
  hashvalue = self.hashfunction(key,len(self.slots))


  """ put hash value into slots and data list if they are empty """
  if self.slots[hashvalue] == None:
    self.slots[hashvalue] = key
    self.data[hashvalue] = data

  else:
  """ if key  in the table"""
    if self.slots[hashvalue] == key:
      self.data[hashvalue] = data  #replace
    else:
      nextslot = self.rehash(hashvalue,len(self.slots))
      """ Tell if slot is occupied or not, if occupied, then keep rehash
       If not occupied, then put key and values into slots.
       iterates the rehash function until an empty slot occurs."""
      while self.slots[nextslot] != None and self.slots[nextslot] != key:
        nextslot = self.rehash(nextslot,len(self.slots))

      """ Put values into slots """
      if self.slots[nextslot] == None:
        self.slots[nextslot]=key
        self.data[nextslot]=data
      else:
        self.data[nextslot] = data #replace data value with new value when old key=new key.

def hashfunction(self,key,size):
     return key%size

"""get rehash value by add one and get remener"""
def rehash(self,oldhash,size):
    return (oldhash+1)%size



def get(self,key):
  startslot = self.hashfunction(key,len(self.slots))

  data = None
  stop = False
  found = False
  position = startslot
  while self.slots[position] != None and not found and not stop:
     if self.slots[position] == key:
       found = True
       data = self.data[position]
     else:
       position=self.rehash(position,len(self.slots))
       if position == startslot:
           stop = True
  return data

def __getitem__(self,key):
    return self.get(key)

def __setitem__(self,key,data):
    self.put(key,data)