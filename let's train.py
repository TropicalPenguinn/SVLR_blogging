for epoch in range(epochs):
    for data_idx in range(len(x_data)):
        x,y=x_data[data_idx],y_data[data_idx]
        
        z1=node1.forward(th,x)
        z2=node2.forward(y,z1)
        l=node3.forward(z2)
        
        dz2=node3.backward(1)
        dy,dz1=node2.backward(dz2)
        dth,dx=node1.backward(dz1)
        
        th=th-lr*dth
    
        th_list.append(th)
        loss_list.append(l)
        
