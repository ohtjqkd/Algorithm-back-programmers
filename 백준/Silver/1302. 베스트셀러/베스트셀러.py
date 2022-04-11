##bestseller

kind = int(input())
titles = list()
for _ in range(kind):
    titles.append(input())
titles.sort()
booksales = list()
num = 1
for i in range(len(titles)):
    if i == len(titles)-1:
        if titles[i] == titles[i-1]:
            booksales.append((num, titles[i]))
        break
    if titles[i] != titles[i+1]:
        booksales.append((num,titles[i]))
        num = 1
    else:
        num += 1
        
# while titles:
#     title = titles.pop()
#     num = 1
    
#     while titles:
        
#         if titles[-1] == title:
#             titles.pop()
#             num += 1
#         else:
#             break
#     booksales.append((num, title))
    
    
booksales = sorted(booksales, key=lambda x: x[1])
booksales = sorted(booksales, key=lambda x: x[0],reverse = True)
print(booksales[0][1])