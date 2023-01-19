import sys
T = int(sys.stdin.readline().strip())
inout_dict = {}
for _ in range(T):
  name, inout = sys.stdin.readline().strip().split()
  inout_dict[name] = inout

in_user = {key : value for key, value in inout_dict.items() if value == 'enter'}
print(*sorted(in_user.keys(), reverse=True), sep = '\n')