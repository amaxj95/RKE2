# Rancher Kubernetes Engine (RKE2)[[RKE](https://docs.rke2.io/install/quickstart)]

Let's set up the master node. The master node in Kubernetes is essentially the brain of the system. To set up a master node using RKE2 you can clone this repo and run the python script called 'rke2.py' <br><br>  
In your terminal on your master node server type: <br>

>> git clone git@github.com:amaxj95/RKE2.git<br>
>> cd RKE2 <br>
>> python3 rke2.py <br> 

Once the script completes, you'll need to manually exit the log trace (ctrl + c). Then in your terminal type: <br>

>> sudo cp /etc/rancher/rke2/rke2.yaml ~/.kube/config <br> 
>> sudo chown $USER:$USER ~/.kube/config <br> 
>> export KUBECONFIG=~/.kube/config <br> 
>> kubectl get nodes <br> 


