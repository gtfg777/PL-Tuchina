s = 'Герой книги, молодой парижанин, в котором так своеобразно сочетались романтичность и трезвый ум ученого'.lower().split(' ')
print(s)
for i in range(len(s)):
   s[i] = ''.join(sorted(s[i]))
print(' '.join(s))
