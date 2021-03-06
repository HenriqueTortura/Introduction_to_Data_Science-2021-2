import numpy as np
import matplotlib.pyplot as plt

#%%
def Rho_x(i, x):
    return (-1)**(i-1)/np.math.factorial(i-1) * (np.log(1-x))**(i-1)

def Rho_delta(n, i, delta):
    if i == n:
        i = i-1
    return (-1)**(i-1)/np.math.factorial(i-1) * (np.log(delta))**(i-1)

def Plot_Histogram(data, i, n, label, bins = 50):
        
        plt.figure(figsize=(8,4.5))
        
        hist = plt.hist(data, bins, label='Simulação', color='#3971cc', edgecolor='#303030',
                  linewidth=1.5, density=True, zorder=1)
        
        x = np.linspace(0, 0.9999, num=1000)
        
        if label == 'x':
            analitical = Rho_x(i, x)
        elif label == 'delta':
            analitical = Rho_delta(n, i, x)
        
        plt.plot(x, analitical, color='#ff7f0e',
                    label='Analítico', zorder=2)
        
        plt.legend(loc='best', fontsize=18)
        plt.xticks(fontsize = 14)
        plt.yticks(fontsize = 14)
        plt.xlim(0, 1)
        plt.ylim(0, 1.1*np.max(hist[0]))
        # plt.xlabel('Degree', fontsize=18)
        plt.ylabel('Frequência', fontsize=18)
        plt.grid(axis='y')
        
        plt.savefig('img/'+label+'_'+str(i)+'of'+str(n)+'.png',
                    dpi=200, bbox_inches='tight')

#%%
m = 10**6 # Número de execuções
n = 5 # Número de partições

x = np.zeros((n,m)) # Vetor de pontos (que guarda x_0=0)
delta = np.zeros((n,m)) # Vetor de partições

for j in range(m): # Percorre execuções
    for i in range(1,n): # Percorre cada sorteio de pontos
    
        # Sorteio dada a distribuição condicional uniforme
        x[i,j] = np.random.uniform(low=x[i-1,j]+np.nextafter(0.0, 1.0), high=1.0)
        
        # Cáclulo do tamanho das partições intermediárias
        delta[i-1,j] = x[i,j] - x[i-1,j]
    
    # Cálculo da partição final
    delta[i,j] = 1 - x[i,j]
        
        
#%%
for i in range(n):
    if i != 0:
        Plot_Histogram(x[i,:], i,
                       n, 'x')
    Plot_Histogram(delta[i,:], i+1,# "Corrige" indexação do Python
                   n, 'delta')
