import imageio
import numpy as np
import matplotlib.pyplot as plt

key1=imageio.imread('key1.png')
key2=imageio.imread('key2.png')
imgI=imageio.imread('I.png')
imgE=imageio.imread('E.png')
Eprime=imageio.imread('Eprime.png')

epoch=1			 #Set Epoch=1
weight=np.random.rand(3) #隨機生成初始值
a=0.00001 		 #LearningRate
maxil=10		 #MaxIterLimit

while (epoch==1 or epoch<maxil):
	for h in range(300):		#設定範圍
		for w in range(400):
			ak=weight[0]*key1[h][w]+weight[1]*key2[h][w]+weight[2]*imgI[h][w]
			ek=imgE[h][w]-ak
			weight[0]+=a*ek*key1[h][w]
			weight[1]+=a*ek*key2[h][w]
			weight[2]+=a*ek*imgI[h][w]
	epoch+=1
	if epoch>=0:
		print("Output w:",weight)
		ans=(Eprime-(weight[0]*key1)-(weight[1]*key2))/weight[2]
		plt.imshow(ans,cmap='gray')
		plt.savefig('ans.png')
		plt.show()
		break




