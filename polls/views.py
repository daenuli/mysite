# from django.shortcuts import render

# Create your views here.
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize, PunktSentenceTokenizer
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from nltk.corpus import state_union
from nltk.tag import CRFTagger
# nltk.download('stopwords')
# nltk.download('state_union')

def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
# from nltk.tokenize import sent_tokenize, word_tokenize
    sentence = "At 18:00 on Thursday morning Arthur didn't feel very good."
    tokens = nltk.word_tokenize(sentence)
    tagged = nltk.pos_tag(tokens)
    stop_word = set(stopwords.words("english"))
    filtered_sentence = []
    steming = []
    for w in tokens:
        if w not in stop_word:
            filtered_sentence.append(w)

    ps = PorterStemmer()
    for e in tokens:
        steming.append(ps.stem(e))

    template = loader.get_template('polls/index.html')
    context = {
        'sentence' : sentence,
        'steming' : steming,
        'tokens' : tokens,
        'tagged' : tagged,
        'words' : word_tokenize(sentence),
        'stop' : stop_word,
        'filtered_sentence' : filtered_sentence,
    }
    return HttpResponse(template.render(context, request))
def tagpos(request):
    ct = CRFTagger()
    ct.set_model_file('all_indo_man_tag_corpus_model.crf.tagger')
    tokenize = word_tokenize("Saya bekerja di Bandung")
    hasil = ct.tag_sents([tokenize])
    postag = nltk.pos_tag(tokenize)
    context = {
        'tokenize' : tokenize,
        'postag' : postag,
        'hasil' : hasil,
    }
    template = loader.get_template('polls/tagged.html')
    # train_text = state_union.raw('2005-GWBush.txt')
    # sample_text = state_union.raw('2006-GWBush.txt')
    # custom_sent_tokenizer = PunktSentenceTokenizer(train_text)
    # tokenized = custom_sent_tokenizer.tokenize(sample_text)
    # tagged = []
    # for i in tokenized[:5]:
    #     words = nltk.word_tokenize(i)
    #     tagged.append(nltk.pos_tag(words))
    #
    # template = loader.get_template('polls/tagged.html')
    # context = {
    #     'tagged' : tagged
    # }
    return HttpResponse(template.render(context, request))
