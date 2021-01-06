import struct
import numpy as np





def load(file_url):     
    f = open(file_url,'rb')
    f.read(64)
    data = f.read(104857600)
    raw = struct.unpack('52428800h',data)
    raw = np.array(raw)
    raw = raw.reshape(6400,8192)#, dtype=np.uint8
    img=np.ones((6400,4096))
    for i in range(6400):
        img[i,0:4096] = raw[i,0:4096] + raw[i,4096:8192]
    return raw

def normal(raw):
    min_row = np.min(raw, axis=0)#每行
    img=np.ones((raw.shape[0],raw.shape[1]))
    for i in range(6400):
        img[i,:] = raw[i,:] - min_row
    return img

def compress(img_in, mode, rate):
    if(mode=='t'):
        img_out = np.zeros((int(img_in.shape[0]/rate), img_in.shape[1]))
        for i in range(int(img_in.shape[0]/rate)):
            for j in range(rate):
                img_out[i,:] = img_out[i,:] + img_in[rate*i+j,:]
            img_out[i,:] = img_out[i,:]/rate
        return img_out
    if(mode=='f'):
        img_out = np.zeros((img_in.shape[0], int(img_in.shape[1]/rate)))
        for i in range(int(img_in.shape[1]/rate)):
            for j in range(rate):
                img_out[:,i] = img_out[:,i] + img_in[:,rate*i+j]
            img_out[:,i] = img_out[:,i]/rate
        return img_out

        
'''
f = open('D:\\Develop\\SRB\\20120309113756656WHF200T10.0D415data.dat','rb')
#f = open('D:\\Develop\\20120309112923906WHF200T10.0D415data.dat','rb')
#f = open('D:\\Develop\\20120309114629421WHF200T10.0D415data.dat','rb')
f.read(64)
data = f.read(104857600)
raw = struct.unpack('52428800h',data)
raw = np.array(raw)
raw = raw.reshape(6400,8192)
min_row = np.min(raw, axis=0)#每行
img=np.ones((6400,8192))
for i in range(6400):
    img[i,:] = raw[i,:] - min_row
#img = np.delete(img, list(range(0,38))+list(range(189,501))+list(range(876+1064))+list(range(1501,1575))+list(range(2013,2088))+list(range(2525,2599))+list(range(3037,3112))+list(range(3549,3623))+list(range(4061,4096))+list(range(0,38))+list(range(4096,4134))+list(range(4284,4597))+list(range(4972,5160))+list(range(5597,5671))+list(range(6109,6184))+list(range(6621,6695))+list(range(7133,7208))+list(range(7645,7719))+list(range(8157,8192)),axis=1 )

plt.imshow(img,cmap='gray')
plt.show()
'''