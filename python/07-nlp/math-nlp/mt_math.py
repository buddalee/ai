from math_dict import tagMap, mtMap

words="小明 有 5 個 蘋果 ， 給 了 小華 3 個 蘋果 ， 請問 他 還 剩 幾 個 蘋果 ？".split(" ")
print('中文:', words)
wi = 0
mtWords=[]

def mt(w):
    if mtMap.get(w) == None:
        return w
    else:
        return mtMap[w]

def isTag(tag):
    tagWords=tagMap[tag]
    if tagWords == None: 
        return False
    else:
        return words[wi] in tagWords

def next(tag):
    global wi
    print("tag="+tag+" word="+words[wi])
    if isTag(tag):
        word = words[wi]
        mtWords.append(mt(word))
        wi += 1
        return word
    
    raise Error("Error !")

def T():
    while wi < len(words):
        S()

# S=Q? NP? v? V v? NP* .
def S():
    if isTag("Q"):
        next("Q")
    while not isTag("V") and not isTag("v"):
        NP()
    if isTag("v"):
        next("v")
    next("V")
    if isTag("v"):
        next("v")
    while not isTag("."):
        NP()  
    next(".")

# NP = (D d)? N
def NP():
    if (isTag("D")):
        next("D")
        next("d")
    
    next("N")

T()
print("英文：", mtWords)
