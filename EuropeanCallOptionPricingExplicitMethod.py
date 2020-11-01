import numpy as np
import matplotlib.pyplot as plt

def EuropeanCall(interest_rate,volatility,exercise_price,\
                 expiry_time,time_steps,price_steps,max_price):
    """Calculates the price of a European Call option for a range of \
        underlying asset prices"""
    
    #assigning variables
        
    r = interest_rate
    sigma = volatility
    E = exercise_price
    T = expiry_time
    Nt = time_steps
    Ns = price_steps
    Smax = max_price
    Smin = 0 #noted but never used
    
    dt = T/Nt #size of time step
    ds = Smax/Ns #size of price step
    
    #initialise time-space vector with values set to zero

    V=np.zeros((Ns+1,Nt+1))
    
    #initialise asset price
    
    S = np.array([np.arange(Ns+1)*ds]) #from 0 to Ns
    
    #initilise time-to-expiry
    
    tau = np.array([np.arange(Nt+1)*dt])
    
    #boundary conditions
    
    for i in range(Ns+1): #option price upon expiry
        option_value = S[:,i] - E
        if option_value > 0:
            V[i][0] = option_value #was index -1
        else:
            V[i][0] = 0 #was index -1
            
    V[0][:] = 0 #option price when asset price is zero
    
    V[-1][:] = Smax - E*np.exp(-r*tau) #option price when asset price is max
    
    #begin iterative method
    
    for i in range(Nt):
        for n in range(1,Ns):
            V[n][i+1] = 0.5*dt*(sigma*sigma*n*n-r*n)*V[n-1][i]\
                +(1-dt*(sigma*sigma*n*n+r))*V[n][i]\
                    +0.5*dt*(sigma*sigma*n*n+r*n)*V[n+1][i]
    
    #plot results
    
    fig = plt.figure()
    ax = fig.gca(projection = '3d')
    X, Y = np.meshgrid(tau, S)
    Z = V
    surf = ax.plot_surface(X, Y, Z)
    
    return V, surf
    
Ans = EuropeanCall(0.05,0.05,10,1,12,10,100)







