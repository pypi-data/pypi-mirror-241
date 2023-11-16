from simhash import Simhash,SimhashIndex
import re

class FuzzyMatching():
    def __init__(self, feature_len = 3, ):
        self.feature_len = feature_len

    def get_features(self, text):
        width = self.feature_len
        text = text.lower()
        text = re.sub(r'[^\w]+', '', text)
        return [text[i:i + width] for i in range(max(len(text) - width + 1, 1))]


a=FuzzyMatching(feature_len=6)

print(a.get_features('这是一段测试文本，用于计算Simhash值'))

        

def get_features(s):
    width = 3
    s = s.lower()
    s = re.sub(r'[^\w]+', '', s)
    return [s[i:i + width] for i in range(max(len(s) - width + 1, 1))]

text = '这是一段测试文本，用于计算Simhash值'
hashfunc = lambda x: hash(x) & 0xffffffffffffffff



# simhash = Simhash(text.split(), hashfunc=hashfunc)

simhash0 = Simhash(text)

print(simhash0.value)

text1 = '这是一段测试文本，用于计算Simhash值'

text2 = '这是一段用于计算Simhash值的测试文本'

simhash1 = Simhash(get_features(text1), hashfunc=hashfunc)

simhash2 = Simhash(get_features(text2), hashfunc=hashfunc)

distance = simhash1.distance(simhash2)

print(distance)


#文本去重
texts = ['这是一段测试文本，用于计算Simhash值',

'这是一段用于计算Simhash值的测试文本',

'这是一段测试文本，用于计算Simhash的应用',

'这是一段测试文本，用于计算Simhash的原理',

'这是一段测试文本，用于计算Simhash的算法']


objs = [(i, Simhash(text.split(), hashfunc=hashfunc)) for i, text in enumerate(texts)]

index = SimhashIndex(objs, k=3)

duplicates = index.get_near_dups(Simhash('这是一段用于计算Simhash值的测试文本', hashfunc=hashfunc))

print(duplicates)

#index demo
import re
from simhash import Simhash, SimhashIndex
def get_features(s):
    width = 3
    s = s.lower()
    s = re.sub(r'[^\w]+', '', s)
    return [s[i:i + width] for i in range(max(len(s) - width + 1, 1))]

data = {
    1: u'How are you? I Am fine. blar blar blar blar blar Thanks.',
    2: u'How are you i am fine. blar blar blar blar blar than',
    3: u'This is simhash test.',
}
objs = [(str(k), Simhash(get_features(v))) for k, v in data.items()]
index = SimhashIndex(objs, k=3)

print (index.bucket_size())

s1 = Simhash(get_features(u'How are you i am fine. blar blar blar blar blar thank'))
print (index.get_near_dups(s1))

index.add('4', s1)
print (index.get_near_dups(s1))