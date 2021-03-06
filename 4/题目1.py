# -*- coding:utf-8 -*-
import re 
text1 = \
    """美国贸易代表戴琪4日表示，美计划与中方就中美第一阶段经贸协议落实情况、产业政策等问题展开坦率对话。她称，美方无意“激化”与中国的贸易紧张局势。

戴琪当天在美国智库战略与国际研究中心发表演讲，首次阐述拜登政府对华贸易政策愿景。她说，美中经贸关系影响深远，作为全球最大的两个经济体，美中两国如何相处不仅影响两国本身，也影响全世界。

戴琪说，美国政府以前处理对华经贸问题的手段未能解决美方根本关切，拜登政府将寻求以“全新、全面和务实”的方式处理对华经贸关系。她同时称，美国将联合盟友制定“公平”的国际贸易规则，并利用所有政策工具保护美国经济不受“不公平”竞争行为的伤害。

戴琪表示，美方将启动针对性的关税豁免程序，允许美国企业申请豁免某些中国输美商品的加征关税。她还提出美中两国“长久共存”的概念，寻求开辟改变美中双边贸易格局的新路径。

在随后问答环节被问及对美中经济“脱钩”的看法时，戴琪说，全球两大经济体停止贸易并不现实。美方可能要思考的问题是，“我们寻求某种‘再挂钩’的目标是什么”。

美国智库彼得森国际经济研究所高级研究员加里·赫夫鲍尔告诉新华社记者，戴琪讲话内容有积极因素，比如谈到“再挂钩”而非“脱钩”，美中两国必须共存，以及为中国输美商品给予加征关税豁免。

一些美国商界团体对戴琪未明确提到取消对华加征关税感到失望。美国消费技术协会主席加里·夏皮罗当天发表声明说，拜登政府应当结束这些伤害美国企业和消费者的关税。自贸易争端爆发以来，美国民众已额外承担900多亿美元的关税成本。此前，约30个有影响力的美国商业团体曾于8月写信敦促拜登政府削减对华商品加征的关税，称关税增加美国民众和企业负担，拖累美国经济增长。

中国外交部发言人华春莹近日表示，中美经贸关系的本质是互利共赢，打贸易战只会带来双输。中方一贯坚定维护以世贸组织为核心的多边贸易体系，坚定按照国际贸易规则办事。希望美方切实尊重市场经济原则和国际经贸规则，同中方一道努力，推动中美经贸关系健康稳定发展。
    """
text2=\
    """
    据新华社华盛顿消息，美国贸易代表戴琪4日表示，美计划与中方就中美第一阶段经贸协议落实情况、产业政策等问题展开坦率对话。她称，美方无意“激化”与中国的贸易紧张局势。

戴琪当天在美国智库战略与国际研究中心发表演讲，首次阐述拜登政府对华贸易政策愿景。她说，美中经贸关系影响深远，作为全球最大的两个经济体，美中两国如何相处不仅影响两国本身，也影响全世界。

戴琪说，美国政府以前处理对华经贸问题的手段未能解决美方根本关切，拜登政府将寻求以“全新、全面和务实”的方式处理对华经贸关系。她同时称，美国将联合盟友制定“公平”的国际贸易规则，并利用所有政策工具保护美国经济不受“不公平”竞争行为的伤害。

戴琪表示，美方将启动针对性的关税豁免程序，允许美国企业申请豁免某些中国输美商品的加征关税。她还提出美中两国“长久共存”的概念，寻求开辟改变美中双边贸易格局的新路径。

在随后问答环节被问及对美中经济“脱钩”的看法时，戴琪说，全球两大经济体停止贸易并不现实。美方可能要思考的问题是，“我们寻求某种‘再挂钩’的目标是什么”。

美国智库彼得森国际经济研究所高级研究员加里·赫夫鲍尔告诉新华社记者，戴琪讲话内容有积极因素，比如谈到“再挂钩”而非“脱钩”，美中两国必须共存，以及为中国输美商品给予加征关税豁免。

一些美国商界团体对戴琪未明确提到取消对华加征关税感到失望。美国消费技术协会主席加里·夏皮罗当天发表声明说，拜登政府应当结束这些伤害美国企业和消费者的关税。自贸易争端爆发以来，美国民众已额外承担900多亿美元的关税成本。此前，约30个有影响力的美国商业团体曾于8月写信敦促拜登政府削减对华商品加征的关税，称关税增加美国民众和企业负担，拖累美国经济增长。

中国外交部发言人华春莹近日表示，中美经贸关系的本质是互利共赢，打贸易战只会带来双输。中方一贯坚定维护以世贸组织为核心的多边贸易体系，坚定按照国际贸易规则办事。希望美方切实尊重市场经济原则和国际经贸规则，同中方一道努力，推动中美经贸关系健康稳定发展。
    """

# n-gram-list
# 输入是多个句子组成的列表
# 为每一个句子单独使用n-gram后，全部加入ngram_list
def create_ngram_list(input_list, ngram_num):
    ngram_list = []
    for sentence in input_list:
        if len(sentence) <= ngram_num:
            ngram_list.append(sentence)
        else:
            for tmp in zip(*[sentence[i:] for i in range(ngram_num)]):
                tmp = "".join(tmp)
                ngram_list.append(tmp)
    return ngram_list

# 划分出句子
pat=r"[。；]\s*"
text1_sentences_list = [i for i in re.split(pat, text1)]
text2_sentences_list = [i for i in re.split(pat, text2)]
# print(text1_sentences_list)
# print(text2_sentences_list)
text1_words_list = create_ngram_list(text1_sentences_list, 5)
text2_words_list = create_ngram_list(text2_sentences_list, 5)

words1_set = set(text1_words_list)  # 得到n-gram词语的集合
words2_set = set(text2_words_list)

print("words1_set = ", text1_words_list)
print("words2_set = ", text2_words_list)


print("集合交：", (words1_set & words2_set))
print("集合并：", (words1_set | words2_set))

similar12 = len(words1_set & words2_set) / len(words1_set | words2_set)
print("两篇文章文本相似度为：%f"%(similar12))
