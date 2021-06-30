import numpy as np

class plus_node:
  def __init__(self):
    self._x,self._y=None,None    #입력 정보를 저장하는 변수를 정의한다.
    self._z=None  #출력 정보를 저장하는 변수를 정의한다.
   
  def forward(self,x,y): #forward를 수행하는 내부 메소드를 정의한다.
    self._x,self._y=x,y #입력 정보를 받아 저장한다.
    self._z=self_x+self._y #출력값을 계산한다.
    return self._z #출력한다.
  
  def backward(self,dz):
    return dz,dz  #"전체의 변화를 알려면 부분 변화의 곱을 구하면 됩니다."여기서 자기 단계의 변화와 자기 앞의 변화를 곱해 vector-chain을 누적해 나갑니다.
  
 
class minus_node:
  def __init__(self):
    self._x,self._y=None,None #입력 정보를 저장하는 변수를 정의한다
    self._z=None
    
  def forward(self,x,y):  #forward를 수행하는 내부 메소드를 정의한다.
    self._x,self._y=x,y
    self._z=self._x-self_y
    return self._z
  
  def backward(self,dz):  #"전체의 변화를 알려면 부분 변화의 곱을 구하면 됩니다."여기서 자기 단계의 변화와 자기 앞의 변화를 곱해 vector-chain을 누적해 나갑니다.
    return dz,-dz
  
class mul_node:
  def __init__(self): #입력 정보를 저장하는 변수를 정의한다
    self._x,self._y=None,None
    self._z=None
   
  def forward(self,x,y):  #forward를 수행하는 내부 메소드를 정의한다.
    self._x,self._y=x,y
    self._z=self._x*self._y
    return self._z
  
  def backward(self,dz):  #"전체의 변화를 알려면 부분 변화의 곱을 구하면 됩니다."여기서 자기 단계의 변화와 자기 앞의 변화를 곱해 vector-chain을 누적해 나갑니다.
    return dz*self._y,dz*self._x
  
class square: #입력 정보를 저장하는 변수를 정의한다
  def __init__(self):
    self._x=None
    self._z=None
   
  def forward(self,x):  #forward를 수행하는 내부 메소드를 정의한다.
    self._x=x
    self._z=self._x*self._x
    return self_z
  
  def backward(self,dz):  #"전체의 변화를 알려면 부분 변화의 곱을 구하면 됩니다."여기서 자기 단계의 변화와 자기 앞의 변화를 곱해 vector-chain을 누적해 나갑니다.
    return 2*dz*self._x
  
class mean:
  def __init__(self): #입력 정보를 저장하는 변수를 정의한다
    self._x=None
    self._z=None
    
   def forward(self,x):  #forward를 수행하는 내부 메소드를 정의한다.
    self._x=x
    self._z=np.mean(self._x)
    
   def backward(self,dz):  #"전체의 변화를 알려면 부분 변화의 곱을 구하면 됩니다."여기서 자기 단계의 변화와 자기 앞의 변화를 곱해 vector-chain을 누적해 나갑니다.
    return dz*1/len(self._x)*np.ones_like(self._x)
  #어이쿠 여기는 좀 뭔가 복잡하죠? 평균을 구하는 노드에서는 입력이 많기 때문에 numpy로 받아서 처리합니다. 위 그림을 보시면 알겠지만 평균의 미분 결과는 스칼라가 모두 1/n인 row-vector에요
  #그래서 np.ones_like 를 사용해서 이것을 표현합니다.
