import re, sys
import nltk, os

print("hello world")


def POS(term):  # term is a string var
    text = nltk.word_tokenize(term)
    pos = nltk.pos_tag(text)
    return pos  # list



    '''
    example
    model["rehabilitation"]
    array([ 1.6414467e-01,  4.4121653e-01, -2.8913401e-02,  1.0129289e-01,
        1.6282564e-01,  1.1306662e-01,  1.5452161e-01,  7.5199974e-01,
       -1.4735998e-01, -1.1530967e-01, -7.5835139e-01, -3.4401456e-01,
        3.0404374e-01,  1.3833216e-01, -3.6553386e-01,  2.0026161e-01,
        4.9306461e-01,  6.5304376e-02, -1.4981459e-01,  2.9404959e-01,
        8.8873178e-02,  2.4156427e-01, -7.7626295e-02,  8.3764620e-02,
       -6.1509404e-02,  1.1974657e-01,  5.2886903e-02,  1.6408244e-01,
       -1.1823344e-05,  1.3502230e-01, -6.0520232e-02, -2.1051948e-01,
        7.9011339e-01,  1.5732346e-01,  3.2846194e-02, -3.1719619e-01,
        6.2882417e-01,  3.0638477e-01,  2.7526679e-02,  3.0634990e-01,
        2.5534379e-01, -2.5403795e-01,  2.5541601e-01, -8.1370361e-03,
       -1.2304571e-01, -1.5843496e-01,  5.5351205e-02, -1.6279392e-01,
       -6.3115799e-01, -4.2328852e-01,  9.0211809e-02, -1.4318320e-01,
       -1.4251815e-02, -2.1460125e-01,  6.4320165e-01, -5.3128654e-01,
        2.6446244e-01,  4.9587634e-01, -2.7171206e-01, -8.3484188e-02,
       -1.9495094e-01, -5.4937024e-02, -6.5427542e-01,  3.0726850e-02,
        3.5758510e-01, -6.3109338e-01,  1.7434639e-01, -5.0865752e-01,
        1.4672601e-01,  3.2686856e-01, -1.7438327e-01, -6.0765755e-01,
        3.4864226e-01,  7.0890814e-01,  3.7233850e-01,  5.0420977e-02,
       -8.0349308e-01, -3.2940325e-01,  1.5491892e-01,  1.2358645e-01,
       -8.9757122e-02, -8.9040473e-03,  2.5326538e-01, -4.3965644e-01,
       -7.6811910e-02,  8.5545279e-02, -2.5291875e-01, -1.8338847e-01,
        2.9879898e-01,  2.8823546e-01, -2.0901331e-01, -1.6261689e-01,
       -1.9261570e-01,  4.7923699e-01, -1.1424187e-01,  7.3239845e-01,
       -4.3270564e-01, -7.0422196e-01,  2.8523457e-01, -2.8920728e-01],
      dtype=float32)
      '''
    return vec


def get_term_dist(term1, term2, model):  # get term distance from pretrained embeddings
    dist = model.wmdistance(term1.lower().split(), term2.lower().split())
    return dist


def get_umls_tagging(text, matcher):
    info = matcher.match(text, best_match=True, ignore_syntax=False)
    taggings = []
    if len(info) == 0:
        return None
    for one_c in info:
        one_c = one_c[0]
        print(one_c)
        result = {"cui": one_c["cui"], "term": one_c["term"]}
        taggings.append(result)
    return taggings


from QuickUMLS.quickumls import QuickUMLS

matcher = QuickUMLS("/home/tk2624/tools/QuickUMLS", threshold=0.8)

text = "tension-free hernioplasty"
print(get_umls_tagging(text, matcher))

# def main():
#     print("hrmmo world")
#
#
# if __name__== "__main__":
#     main()


