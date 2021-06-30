import matplotlib.cm as cm

N_lines=100

cmap=cm.get_cmap("rainbow",lut=N_lines)

fig,ax=plt.subplots(1,1,figsize=(10,10))
ax.scatter(x_data,y_data)

test_th=th_list[:N_lines]
x_range=np.array([np.min(x_data),np.max(x_data)])

for line_idx in range(N_lines):
  pred_line=np.array([x_range[0]*test_th[line_idx],x_range[1]*test_th[line_idx]])

  ax.plot(x_range,pred_line,color=cmap(line_idx),alpha=0.1)
