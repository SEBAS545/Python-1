'''
import datetime
import time
Age = 0
while True :
  print(Age)
  Age += 1

  date_actuelle = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
  hour = int(date_actuelle[11:13])
  if hour < 12:
    print("Good morning")
  elif hour >= 12:
    print("Good afternoon")

  print(date_actuelle)
  time.sleep(60)
'''
'''Exo 1.1
def factorielle_1(n):
  p = 1
  for k in range(1,n+1):
    p = p * k
  return p
resultat = factorielle_1(40)
resultat_1 = factorielle_1(100)
print(resultat)
print(resultat_1)
'''

'''Exo 1.2
def newfactorielle(n):
  p = 1
  Liste = []
  for k in range(1,n+1):
    p = p * k
    Liste = Liste + [p]
  return Liste
resultat = newfactorielle(7)
print(resultat)
'''

'''Exo 1.3
def successeur(n):
  n = n+1
  return n
resultat = successeur(3)
resultat_1 = successeur(successeur(3))
print(resultat)
print(resultat_1)
'''

'''Exo 1.4
def mystere(a,b):
  a = a + b
  b = a - b
  a = a - b
  return a,b
resultat = mystere(7,5)
resultat_1 = mystere(3,9)
print(resultat)
print(resultat_1)
'''

'''Exo 1.5
L1 = [-3, -2, -1, 0, 1, 2, 3]
L2 = [-2**2, -1**2, 0**2, 1**2, 2**2, 3**2, 4**2]
L3 = L1 + L2
L3.sort()
L4 = []
for i in range(len(L1)):
  L4.append(L1[i] + L2[i])
print(L1)
print(L2)
print(L3)
print(L4)
'''

'''Exo 1.6
Mult7 = []
k = 1
while 7*k < 100:
  Mult7.append(7*k)
  k += 1
print(Mult7)
'''

'''Exo 1.7
def mystere(n):
  p = 1
  k = 1
  while k < n + 1:
    p = p * k
    k += 1
  return p  
resultat = mystere(3)  
resultat_1 = mystere(11)
print(resultat)
print(resultat_1)
'''

'''Exo 1.8
def divmod(n,p):
  j = 0
  while n >= p:
    n = n - p
    j += 1
  return j,n  
resultat = divmod(17,6)
resultat_1 = divmod(20,5)
resultat_2 = divmod(142,6)

print(resultat)
print(resultat_1)
print(resultat_2)
'''

'''Exo 1.9
def f(x):
  return x**3 - x**2 + 3
x_value = range(-5, 5)
T = [(x, f(x)) for x in x_value]
print(T)
'''

'''Exo 1.10
def factorielle(n):
  p = 1
  for k in range(1,n+1):
    p = p * k
  return p
resultat = factorielle(5)
print(resultat)

def sommefacto(n):
  somme = 0
  for k in range(0,n+1):
    somme = somme + 1/factorielle(k)
  return somme
resultat = sommefacto(500)
print(resultat)
'''

