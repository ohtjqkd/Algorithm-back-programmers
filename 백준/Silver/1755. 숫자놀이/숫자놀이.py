s, e = input().split(" ")
alph = {'0':'zero', '1':'one', '2':'two', '3':'three', '4':'four', '5':'five', '6':'six', '7':'seven', '8':'eight', '9':'nine'}
ret = [str(i) for i in range(int(s), int(e)+1)]
ret.sort(key=lambda x: ' '.join([alph[xx] for xx in x]))
for i in range(len(ret)//10+1):
    print(' '.join(ret[10*i:min(len(ret), 10*(i+1))]))