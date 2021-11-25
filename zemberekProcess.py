import jpype as jp

def zemberek_baslat():
    ZEMBEREK_PATH = r'D:\Projects\TurkishTextNormalization\bin\zemberek-full.jar'
    jp.startJVM(jp.getDefaultJVMPath(), '-ea', '-Djava.class.path=%s' % (ZEMBEREK_PATH))

def zemberek_duzeltme_islemleri(girdi):
    TurkishMorphology = jp.JClass('zemberek.morphology.TurkishMorphology')
    TurkishSpellChecker = jp.JClass('zemberek.normalization.TurkishSpellChecker')
    TurkishSentenceNormalizer = jp.JClass('zemberek.normalization.TurkishSentenceNormalizer')
    Paths = jp.JClass('java.nio.file.Paths')

    lookupRoot = Paths.get(r'D:\Projects\TurkishTextNormalization\data\normalization')
    lmPath = Paths.get(r'D:\Projects\TurkishTextNormalization\data\lm\lm.2gram.slm')
    morphology = TurkishMorphology.createWithDefaults()

    morph = TurkishMorphology.createWithDefaults()
    spell = TurkishSpellChecker(morph)
    sentenceNormalizer = TurkishSentenceNormalizer(morphology, lookupRoot, lmPath)

    duzeltilmisGirdi = sentenceNormalizer.normalize(girdi)
    return duzeltilmisGirdi

def zemberek_kapat():
    jp.shutdownJVM()