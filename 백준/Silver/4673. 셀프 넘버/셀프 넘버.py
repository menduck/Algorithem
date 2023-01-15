def self_number() :
  not_self_number_list = []
  for num in range(1,10001):
    not_self_number_list.append(num+sum(list(map(int,str(num)))))
  
  set_not_selfnumber = set(not_self_number_list)
  number_list = set(range(1,10001))

  print(*sorted(number_list - set_not_selfnumber), sep='\n')

self_number()