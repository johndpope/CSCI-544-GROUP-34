from nltk.corpus import brown

sentences = []

fileWriter = open("brownCorpusSentences.txt", 'w')

brown_sentences = brown.sents()
print(len(brown_sentences))
for b_s in brown_sentences[56000:56100]:
    str1 = ' '.join(b_s)
    fileWriter.write(str1+"\n")

fileWriter.close()

