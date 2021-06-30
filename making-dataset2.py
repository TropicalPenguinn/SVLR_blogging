dataset_gen =Data_generator(1,n_sample=1000)
dataset_gen.set_coefficient([0,4])
dataset_gen.set_noise(0.5)
dataset=dataset_gen.make_dataset(init_noise=True)

x_data=dataset[:,1]
y_data=dataset[:,2]
fig,ax=plt.subplots(1,1,figsize=(10,10))
ax.scatter(x_data,y_data)
