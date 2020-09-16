import pickle
#Make the pickle file
# example_dic = {1: "6", 2: "5", 3: "f"}
# pickle_out = open("dict.pickle", "wb")
# pickle.dump(example_dic, pickle_out)
# pickle_out.close()
#Load the Pikle file 
pickle_in=open("dict.pickle","rb")
example_dic=pickle.load(pickle_in)
print(example_dic)