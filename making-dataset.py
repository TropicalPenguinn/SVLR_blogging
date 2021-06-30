dataset_gen =Data_generator(1,n_sample=1000)
dataset_gen.set_coefficient([0,4])
dataset_gen.set_noise(0.5)
dataset=dataset_gen.make_dataset(init_noise=True)
