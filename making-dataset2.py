dataset_gen =Data_generator(1,n_sample=1000)
dataset_gen.set_coefficient([0,4])  #y=4x 관계를 이루는 데이터를 만들기 위해 계수 설정
dataset_gen.set_noise(0.5) #노이즈의 정규 분포의 "표준 편차"설정 정확한 증명은 하지 않지만 간단히 말해 노이즈의 표준편차가 클수록 데이터 상관관계가 옅어집니다.
dataset=dataset_gen.make_dataset(init_noise=True) #노이즈를 적용합니다.

x_data=dataset[:,1] #1열 데이터만을 추출
y_data=dataset[:,2] #2열 데이터만을 추출
fig,ax=plt.subplots(1,1,figsize=(10,10)) #시각적으로 확인
ax.scatter(x_data,y_data)
