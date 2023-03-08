from operator import itemgetter
#1//cmax,la somme,c bare
def task(n, p):
# Rangement des tâches dans l’ordre croissant de leurs dates de leurs dureés SPT
    tasks = list(zip(p))
    # Trie de la liste en utilisant p[i] comme clé de tri
    tasks = sorted(tasks, key=lambda x: x[0])
   
    # Initialisation des variables
    t = 0.0
    c=[]
    a=t+tasks[0][0]
    c.append(a)
    cmax = 0.0
    # Calcul de t1 et C1
   
    # Calcul de ti et Ci pour i de 2 à n
    for i in range(1, n):
        t=a
        a=t+tasks[i][0]
        c.append(a)
    # Calcul du Cmax
    cmax = c[-1]
    some_c=0.0
    cbare=0.0
    for i in range(n):
        some_c+=c[i]
        
    cbare=some_c/n
        
    return  c,cmax,cbare,some_c






#1/ri/Cmax , la somme , c bare

def task_scheduling(n, r, p):
# Rangement des tâches dans l’ordre croissant de leurs dates de disponibilité
    tasks = sorted(zip(r, p), key=lambda x: x[0])
    # Initialisation des variables
    t = []
    c = []
    cmax = 0.0
    # Calcul de t1 et C1
    t.append(tasks[0][0])
    c.append(tasks[0][0] + tasks[0][1])
    # Calcul de ti et Ci pour i de 2 à n
    for i in range(1, n):
        t.append(max(c[i-1], tasks[i][0]))
        c.append(t[i] + tasks[i][1])
    # Calcul du Cmax
    cmax = c[-1]
    some_c=0.0
    cbare=0.0
    for i in range(n):
        some_c+=c[i]
        
    cbare=some_c/n
        
    return  c, cmax,cbare,some_c
    
    
    
    
    
 #1/di/Cmax  , la somme , c bare,Lmax,lbare,somme des li  Tmax EDD

def task_scheduling_echue(n, d, p):
# Rangement des tâches dans l’ordre croissant de leurs dates Echues
    tasks = sorted(zip(d, p), key=lambda x: x[0])
    # Initialisation des variables
    t = 0.0
    c=[]
    a=t+tasks[0][1]
    c.append(a)
    cmax = 0.0
   
    for i in range(1, n):
        t=a
        a=t+tasks[i][1]
        c.append(a)
    # Calcul du Cmax
    cmax = c[-1]
    some_c=0.0
    cbare=0.0
    for i in range(n):
        some_c+=c[i]
        
    cbare=some_c/n
    lmax = max(c[i] - d[i] for i in range(n))
    some_li=0.0
    for i in range(n):
       some_li=c[i] - d[i]
    l_bare=some_li/n
    tmax=max(0,lmax)
        
    return  c, cmax,cbare,some_c,lmax,l_bare,some_li,tmax
    








#1/w/cmax,la somme,c bare,cw_bare
def task_scheduling_with_weights(n, p, w):
    # Création d'une liste de tuples (w[i], p[i], r[i]) pour chaque tâche i
    tasks = sorted(zip(w, p), key=lambda x: x[0])
    # Trie de la liste en utilisant w[i]/p[i] comme clé de tri
    tasks = sorted(tasks, key=lambda x: x[0]/x[1])
    t = 0.0
    c=[]
    a=t+tasks[0][1]
    c.append(a)
    cmax = 0.0
    # Calcul du t1 et C1
   
    # Calcul du ti et Ci pour i de 2 à n
    for i in range(1, n):
        t=a
        a=t+tasks[i][1]
        c.append(a)
    # Calcul du Cmax
    cmax = c[-1]
    some_c=0.0
    cbare=0.0
    for i in range(n):
        some_c+=c[i]
        
    cbare=some_c/n
    
    s=0.0
    sw=0.0
    for i in range(n):
        sw+=w[i]
        s+=c[i]*w[i]
    cw_bare=s/sw
    return  c,cmax,cbare,some_c,cw_bare


def display_menu():
    print("\nMenu:")
    print("1.le problème <1/ /(cmax,la somme des ci,c bare)> SPT ")
    print("2.le problème <1/ri/ (Cmax , la somme des ci , c_bare)>range selon ri")
    print("3.le problème <1/di/(Cmax , la somme des ci , c_bare,Lmax,l_bare,somme des li,Tmax)>EDD")
    print("4.le problème<1/w/(cmax,la somme des ci,c_bare,cw_bare)> W/P  ")
    print("5. Quitter")
def option_1():
    # code pour exécuter l'option 1
    print("Option 1 sélectionnée")
    list_p=[]
    n=int(input("donner le nombre de tâches :"))
    for i in range(n):
   
        p=float(input ("donner la durée de la tâche "+str(i+1)+': '))
        #d=float(input ("donner la date échue de la tâche "+str(i+1)+': '))
        list_p.append(p)
    c,cmax,cbare,some_c=task(n, list_p)
    print(f"la liste des dates de fin de chaque tâche avec la règles SPT est :\n {c}")
    print(f"La longueur de l’ordonnancement :\n {cmax}")
    print(f"Le temps de fin de traitement moyen \n:{cbare}")
    print(f"La somme de fin de traitement des tâches \n:{some_c}")
    
    
    
    
def option_2():
# code pour exécuter l'option 2
   
    print("Option 2 sélectionnée")
    list_p=[]
    list_r=[]
    n=int(input("donner le nombre de tâches :"))
    for i in range(n):
   
        p=float(input ("donner la durée de la tâche "+str(i+1)+': '))
        r=float(input ("donner la date de disponibilité de la tâche "+str(i+1)+': '))
        list_p.append(p)
        list_r.append(r)
    c,cmax,cbare,some_c=task_scheduling(n, list_r, list_p)
    print(f"la liste des dates de fin de chaque tâche est :\n {c}")
    print(f"La longueur de l’ordonnancement :\n {cmax}")
    print(f"Le temps de fin de traitement moyen \n:{cbare}")
    print(f"La somme de fin de traitement des tâches \n:{some_c}")
    
def option_3():
# code pour exécuter l'option 3
    print("Option 3 sélectionnée")
    list_p=[]
    list_d=[]
    n=int(input("donner le nombre de tâches :"))
    for i in range(n):
   
        p=float(input ("donner la durée de la tâche "+str(i+1)+': '))
        d=float(input ("donner la date échue de la tâche "+str(i+1)+': '))
        list_p.append(p)
        list_d.append(d)
    c, cmax,cbare,some_c,lmax,l_bare,some_li,tmax=task_scheduling_echue(n, list_d, list_p)
    print(f"la liste des dates de fin de chaque tâche est :\n {c}")
    print(f"La longueur de l’ordonnancement :\n {cmax}")
    print(f"Le temps de fin de traitement moyen \n:{cbare}")
    print(f"La somme de fin de traitement des tâches \n:{some_c}")
    print(f"La grande tardivete \n:{lmax}")
    print(f"La tardivete moyenne \n :{l_bare}")
    print(f"La somme de tardivete des tâches \n :{some_li}")
    print(f"Le grand retard \n:{tmax}")
def option_4():
# code pour exécuter l'option 2
   
    print("Option 2 sélectionnée")
    list_p=[]
    list_w=[]
    n=int(input("donner le nombre de tâches :"))
    for i in range(n):
   
        p=float(input ("donner la durée de la tâche "+str(i+1)+': '))
        w=float(input ("donner le poid de la tâche "+str(i+1)+': '))
        list_p.append(p)
        list_w.append(w)
    c,cmax,cbare,some_c,cw_bare=task_scheduling_with_weights(n, list_p, list_w)
    print(f"la liste des dates de fin de chaque tâche est :\n {c}")
    print(f"La longueur de l’ordonnancement :\n {cmax}")
    print(f"Le temps de fin de traitement moyen \n:{cbare}")
    print(f"La somme de fin de traitement des tâches \n:{some_c}")  
    print(f"Le temps de fin de traitement moyen ponderé \n :{cw_bare}")     
    
    
def quit():
# code pour quitter le programme
    print("Au revoir!")
    exit()
while True:
    display_menu()
    selection = input("\nSélectionnez une option (1-5): ")
    # Exécution de l'option sélectionnée
    options = {
    "1": option_1,
    "2": option_2,
    "3": option_3,
    "4": option_4,
    "5": quit
    }
    options.get(selection, lambda: print("Sélection non valide"))()