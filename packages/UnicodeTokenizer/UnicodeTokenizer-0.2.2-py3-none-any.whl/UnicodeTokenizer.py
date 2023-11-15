# -*- coding: utf-8 -*-

from icu import BreakIterator, Locale

from tokenizers import pre_tokenizers


class UnicodeTokenizer:
    def __init__(self, lang="zh"):
        self.lang = lang
        self.word_breaker = BreakIterator.createWordInstance(Locale(lang))
        self.sentence_breaker = BreakIterator.createSentenceInstance(Locale(lang))
        self.pre_tokenizer = pre_tokenizers.Sequence([
            # pre_tokenizers.Whitespace(),  # \w+|[^\w\s]+
            # pre_tokenizers.UnicodeScripts(),
            pre_tokenizers.Punctuation("contiguous"),
            #  pre_tokenizers.Split(" ?[^(\\s|[.,!?…。，、।۔،])]+", "isolated"),
             pre_tokenizers.Split("\s+", "contiguous"),
              ])
        # self.pre_tokenizer = pre_tokenizers.Sequence([pre_tokenizers.UnicodeScripts()])

    def split_lines(self, text):
        self.sentence_breaker.setText(text)
        parts = []
        p0 = 0
        for p1 in self.sentence_breaker:
            part = text[p0:p1]
            parts.append(part)
            p0 = p1
        return parts

    def tokenize(self, text):
        tokens = []
        lines = self.split_lines(text)
        for line in lines:
            spans = self.pre_tokenizer.pre_tokenize_str(line)
            for span, bound in spans:
                tokens += self.tokenize_line(span)
        return tokens

    def tokenize_line(self, line):
        self.word_breaker.setText(line)
        parts = []
        p0 = 0
        for p1 in self.word_breaker:
            part = line[p0:p1]
            parts.append(part)
            p0 = p1
        return parts


def demo_token(line):
    tokenizer = UnicodeTokenizer()
    print(tokenizer.split_lines(line))
    print([word for word,(start,end) in tokenizer.pre_tokenizer.pre_tokenize_str(line)])
    print(tokenizer.tokenize_line(line))
    print(tokenizer.tokenize(line))


if __name__ == "__main__":
    line = """                  
            首先8.88设置 st。art_new_word=True 和 output=[açaí]，output 就是最终 no such name"
            的输出คุณจะจัดพิธีแต่งงานเมื่อไรคะ탑승 수속해야pneumonoultramicroscopicsilicovolcanoconiosis"
            하는데 카운터가 어디에 있어요ꆃꎭꆈꌠꊨꏦꏲꅉꆅꉚꅉꋍꂷꂶꌠلأحياء تمارين تتطلب من [MASK] [PAD] [CLS][SEP]
            est 𗴂𗹭𘜶𗴲𗂧, ou "phiow-bjij-lhjij-lhjij", ce que l'on peut traduire par « pays-grand-blanc-élevé » (白高大夏國). 
        """.strip()
    # demo_token(line)
    l=line.splitlines()[0]
    demo_token(l)
        



"""
pre_tokenizers.Split(" ?[^(\\s|[.,!?…。，、।۔،])]+", "isolated").pre_tokenize_str(l)
"""