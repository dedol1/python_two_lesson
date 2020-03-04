data = {'name': 'sam', 'age': 34, 'date': 'get'}

#key = str(raw_input('enter the key: ').split())

#if key in data:
 #   print(data[key])
#else:
 #   print("invalid key")

#for key in data:
 #   print data.get(key)


def myDict(**kwargs):
  # add all of your keys here
  keys = str(raw_input('enter the key: ').split())
      
  # iterate through keys
  # return the key element if it's in kwargs
  list_comp = ''.join([val for val in keys if val in kwargs ])
  results = kwargs.get(list_comp,data)

  print(results)

myDict()
