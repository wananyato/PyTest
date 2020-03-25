# 序列化和反序列化
import pickle

a1 = "左航伟"
a2 = 18
a3 = [1,2,3,4,5,6,7]

with open(r"d:\ax.txt","wb") as f:
    pickle.dump(a1, f)
    pickle.dump(a2, f)
    pickle.dump(a3, f)

with open(r"d:\ax.txt","rb") as f:
    b1 = pickle.load(f)
    b2 = pickle.load(f)
    b3 = pickle.load(f)
    print(b1);print(b2);print(b3);
    print(id(a1));print(id(b1))
