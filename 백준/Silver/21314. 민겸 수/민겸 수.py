s = input()
m = 0
mnr = ['' for i in range(len(s))]
mxr = ['' for i in range(len(s))]
for i in range(len(s)):
  if s[i] == 'K':
    for j in range(i, i-m-1, -1):
      if j == i:
        mnr[j] = '5'
        mxr[j-m] = '5'
      elif j == i-m:
        mnr[j] = '1'
        mxr[j+m] = '0'
      else:
        mnr[j] = '0'
        mxr[j] = '0'
    m = 0
  elif i == len(s) - 1:
    for j in range(i, i-m-1, -1):
      if j == i-m:
        mnr[j] = '1'
        mxr[j] = '1'
      else:
        mnr[j] = '0'
        mxr[j] = '1'
  else:
    m+=1
print(''.join(mxr))
print(''.join(mnr))