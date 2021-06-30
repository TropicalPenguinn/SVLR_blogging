class Data_generator:
    def __init__(self, feature_dim, n_sample = 100, noise = 0):
        self._feature_dim = feature_dim  #몇개의 변수가 들어가는 polynomial 인지 저장 변수 이번 강의는 일차 함수이기 때문에 1
        self._n_sample = n_sample #데이터 샘플 갯수
        self._noise = noise #noise를 넣을 것인가? 흔히 말하는 퍼져있는 데이터를 만들고 싶은가
        
        self._coefficient_list = None #변수 앞에 계수를 저장하는 리스트 
        self._distribution_params = None #데이터를 정규 분포로 뿌릴 것이기 때문에 "평균","표준 편차" 정보를 저장한다.
        
        self._dataset = None #데이터셋 정보 저장
        
        self._init_coefficient() #계수 리스트 생성 메소드 실행
        self._init_distribution_params() #정규 분포 정보를 저장하는 딕셔너리 생성 메소드 실행
        
    def _init_coefficient(self):
        self._coefficient_list = [0] + [1 for _ in range(self._feature_dim)] #bias가 0이기 때문에 맨 앞에 0을 추가한다.
        
    def _init_distribution_params(self):
        self._distribution_params = {f:{'mean':0, 'std':1}
                                     for f in range(1, self._feature_dim+1)}  """ 계수 리스트 0번째가 bias이기 때문에 인덱스를
                                                                               맞추기 위해서 key를 1부터 배분"""    
    def make_dataset(self,init_noise=false): #dataset을 만들어 봅시다.
        x_data = np.zeros(shape = (self._n_sample, 1))
        y_data = np.zeros(shape = (self._n_sample, 1)) #데이터 샘플에 맞게 numpy로 행렬을 만든다 nX1 matrix다.
        
        for f_idx in range(1, self._feature_dim + 1):
            feature_data = np.random.normal(loc = self._distribution_params[f_idx]['mean'],
                                            scale = self._distribution_params[f_idx]['std'],
                                            size = (self._n_sample, 1)) 
            x_data = np.hstack((x_data, feature_data)) #모두 0인 부분(bias) 와 임의로 뿌린 데이터 값을 합친다
            
            y_data += self._coefficient_list[f_idx]*feature_data #임의로 뿌린 값에 계수를 곱해 y_data를 만든다
        y_data += self._coefficient_list[0]
        
        if init_noise=True: """만약 잡음을 넣는다고 하면 잡음 역시 정규분포로 뿌린 값을 사용한다. 정확한 통계 증명은 
                                대학 통계학에서 multi-variable 의 covariance 부분 참고"""
            
            y_data+=noise*np.random.normal(loc = self._distribution_params[f_idx]['mean'],
                                            scale = self._distribution_params[f_idx]['std'],
                                            size = (self._n_sample, 1)) 
        
        self._dataset = np.hstack((x_data, y_data)) """0인 부분 임의로 뿌린 값과 거기에 계수를 곱한 곱까지 하나로 묶어 dataset
                                                        을 만든다"""
        return self._dataset
    
    def set_n_sample(self, n_sample):
        self._n_sample = n_sample
    
    def set_noise(self, noise):
        self._noise = noise
    
    def set_distribution_params(self, distribution_params):
        for param_key, param_value in distribution_params.items():
            self._distribution_params[param_key] = param_value
    
    def set_coefficient(self, coefficient_list):
        self._coefficient_list = coefficient_list
