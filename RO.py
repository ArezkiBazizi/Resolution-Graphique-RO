import numpy as np
import matplotlib.pyplot as plt
from numpy import zeros,array
xmax = int(input('Donnez la taille maximale des abscisses et des ordonnées à afficher: '))
ymax = xmax
bord  = 1000
x=np.arange(-bord,bord,0.02)
n = int(input('quel est le nombre de contrainte ? '))
Y = []
T = []
A = []
B = []
C = []
S = []
SOL = []
Max = []
Min = []
plt.fill_between(x, -bord, bord, color='green')
def V(s,a,b): 
 if s == "<=":
    if b<0 : 
      return 1 #atekset iwksar
    if b>0 :
      return 0 #atekset iwsawen  
  
 if s == ">=" :
    if b > 0: 
       return 1 #atekset iwksar
    if b < 0:
       return 0 #atekset iwsawen

for i in range (0,n):
  s=input('donnez le signe de la contrainte n°' +str(i+1) +' <= ou >=')
  print('donnez a,b,c tel que ax+by'+str(s)+' c ')
  a = float( input('donnez a ' +str(i+1) + ' : '))
  b= float (input('donnez b ' +str(i+1) + ' : '))
  c= float (input('donnez c ' +str(i+1) + ' : ')) #recuperation des contraintes
  A.append(a)
  B.append(b)
  C.append(c)
  S.append(s)

  if b != 0: 
    T.append(V(s,a,b))
    y = (c-a*x)/b
    Y.append(y) 
    plt.plot(x,Y[i],color='red') #dessin des droites
  else:
     T.append(2)
     Y.append(0)
     plt.axvline(x=c,color='red') #dessine des droites verticals
     if s == "<=":                              
      plt.fill_between(x, bord, where = (x > c), 
                 color = 'gray')              
     if s == ">=":
      plt.fill_between(x, bord, where = (x < c),
                 color = 'gray')

for i in range(0 , n-1):
        for j in range(i+1 ,n):
            try :
                X1 = ((C[j]*B[i])-(B[j]*C[i]))/((A[j]*B[i])-(A[i]*B[j])) 
                Y1 = ((C[j]*A[i])-(C[i]*A[j]))/((B[j]*A[i])-(B[i]*A[j]))     
            except ZeroDivisionError:
                X1 = X1
                Y1 = Y1
            l = 0
            for k in range(0, n):            #verifier les points d'intersection 
                    r = A[k]*X1+B[k]*Y1                                 
                    if (S[k] == ">=") and (r<C[k]) :
                        continue
                    elif (S[k] == "<=") and (r>C[k]) :
                        continue
                    else :
                       l+=1
            if l == n :
               cordonnées = (X1,Y1)
               SOL.append(cordonnées)       #Ajouter les points qui appartienent a l'espace

for w in range(len(SOL)) :
    plt.plot(SOL[w][0],SOL[w][1], 'ro')  #Dessiner les points

plt.grid()
plt.axis([-xmax,xmax,-ymax,ymax])
plt.plot([0, 0], [-bord, bord], color='black')
plt.plot([-bord, bord], [0, 0], color='black')     #desiner la grille

for i in range (0,n):  
    if T[i]==0 :
     plt.fill_between(x, Y[i], bord, color='gray') #effacer en haut horizontal
    if T[i]==1 :
     plt.fill_between(x, Y[i], -bord, color='gray') #effacer en bas horizontal

ss = input ('La contrainte peincipale est-elle une max ou une min ?')
print('donner lequation avec la forme '+str(ss)+'(z)=Ax1+Bx2')
A = int(input ('donner A :'))
B = int (input('donner B :'))

if ss =='max':
   max=(A*SOL[0][0]+B*SOL[0][1])   #supposer que le premier point est la solution optimale
   ptmax = (SOL[0][0],SOL[0][1])
   for w in range(1,len(SOL)):     #la comparer avec le reste des points
    M = A*SOL[w][0]+B*SOL[w][1]
    point = (SOL[w][0],SOL[w][1])
    if M > max :
      max = M
      Max.clear  
      Max.append(point)               #Prendre la solution optiale
      ptmax = point 
    if (M == max) and (point != ptmax):
      Max.append(point) 

   if (len(Max) == 0):
       print('la solution optimale est le point '+str(ptmax))
       plt.plot(SOL[0][0], SOL[0][1], 'bo')                                       #Dessiner la solution optimale en bleu
       plt.text(SOL[0][0], SOL[0][1], ' ({}, {}) '.format(SOL[0][0],SOL[0][1])      )#ecrire les cordonnées de la solution optimale
   elif (len(Max) == 1):
       print('la solution optimale est le point '+str(Max[0])) 
       plt.plot(Max[0][0], Max[0][1],'bo')                                         #Dessiner la solution optimale en bleu
       plt.text(Max[0][0], Max[0][1], ' ({}, {}) '.format(Max[0][0],Max[0][1]))      #ecrire les cordonnées de la solution optimale

   else :
      print('il existe une infinité de solution optimale, sur le segment que compose les deux point'+str(Max[0]) + str(Max[1]))
      plt.plot(Max[0][0], Max[0][1],'bo')                                          #Dessiner la solution optimale en bleu
      plt.plot(Max[1][0], Max[1][1],'bo')                                          #Dessiner la solution optimale en bleu
      plt.text(Max[0][0], Max[0][1], ' ({}, {}) '.format(Max[0][0],Max[0][1]))      #ecrire les cordonnées de la solution optimale
      plt.text(Max[1][0], Max[1][1], ' ({}, {}) '.format(Max[1][0],Max[1][1]))      #ecrire les cordonnées de la solution optimale

if ss =='min':  
  min=(A*SOL[0][0]+B*SOL[0][1])     #supposer que le premier point est la solution optimale
  ptmin = (SOL[0][0],SOL[0][1])  
  for w in range(1,len(SOL)):        #la comparer avec le reste des points
    M = A*SOL[w][0]+B*SOL[w][1]
    point = (SOL[w][0],SOL[w][1])
    if M < min :
      min = M
      Min.clear  
      Min.append(point)               #Prendre la solution optiale
      ptmin = point 
    if (M == min) and (point != ptmin):
      Min.append(point) 

  if (len(Min) == 0):
    print('la solution optimale est le point '+str(ptmin))
    plt.plot(SOL[0][0], SOL[0][1],'bo')                                        #Dessiner la solution optimale en bleu
    plt.text(SOL[0][0], SOL[0][1], '({}, {})'.format(SOL[0][0],SOL[0][1]))     #ecrire les cordonnées de la solution optimale
  elif (len(Min) == 1):
       print('la solution optimale est le point '+str(Min[0])) 
       plt.plot(Min[0][0], Min[0][1],'bo')                                      #Dessiner la solution optimale en bleu
       plt.text(Min[0][0], Min[0][1], '({}, {})'.format(Min[0][0],Min[0][1]))   #ecrire les cordonnées de la solution optimale
  else :
      print('il existe une infinité de solution optimale, sur le segment que compose les deux point'+str(Min[0]) + str(Min[1]))  
      plt.plot(Min[0][0], Min[0][1],'bo')                                      #Dessiner la solution optimale en bleu
      plt.plot(Min[1][0], Min[1][1],'bo')                                       #Dessiner la solution optimale en bleu
      plt.text(Min[0][0], Min[0][1], '({}, {})'.format(Min[0][0],Min[0][1]))    #ecrire les cordonnées de la solution optimale
      plt.text(Min[1][0], Min[1][1], '({}, {})'.format(Min[1][0],Min[1][1]))    #ecrire les cordonnées de la solution optimale


plt.show()   #affichage des graphes