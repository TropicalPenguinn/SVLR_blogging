fig, ax = plt.subplots(2, 1, figsize = (50,10)) 
ax[0].plot(th_list)
title_font = {'size':30, 'alpha':0.8, 'color':'navy'} 
label_font = {'size':20, 'alpha':0.8} 
plt.style.use('seaborn') 
ax[0].set_title(r'$\theta$', fontdict = title_font)
ax[1].set_title("Loss", fontdict = title_font)
ax[1].set_xlabel("Iteration", fontdict = label_font)
ax[1].plot(loss_list)
