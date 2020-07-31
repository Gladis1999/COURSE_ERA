punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for line in pos_f:
        if line[0] != ';' and line[0] != '\n':
            positive_words.append(line.strip())


negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())
            

def strip_punctuation(string):
    for i in string:
        if i in punctuation_chars:
            string=string.replace(i,"")
    return string
def get_neg(string):
        pos=0
        string=strip_punctuation(string)
        x=string.split(" ")
        for i in x:
            if i.lower() in negative_words:
                  pos+=1
        return pos            
def get_pos(string):
        pos=0
        string=strip_punctuation(string)
        x=string.split(" ")
        for i in x:
            if i.lower() in positive_words:
                  pos+=1
        return pos
f=open("project_twitter_data.csv",'r')
g=open("resulting_data.csv","w")
g.write('Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score')
g.write("\n")
line=f.readlines()
pos=0
for i in line:
   
       if pos>0:
          x=i.split(",")
          a=x[0]
          p=x[1]
          q=x[2]
          b=get_pos(x[0])
          c=-(get_neg(x[0]))
          net=b+c
          s='{},{},{},{},{}'.format(int(p),int(q),b,c,net)
          g.write(s)
          g.write("\n")
       else:
            pos+=1
          
                
g.close()
        
