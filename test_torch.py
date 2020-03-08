import torch
a=str(torch.cuda.is_available())
with open('test_read.json','r') as f:
    b=f.read()
with open('test_write.json','w') as f:
    f.write(a)
    f.write(b)