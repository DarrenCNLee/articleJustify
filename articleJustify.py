text = "Hi! How should this article look? Please format it properly."


def articleJustify(text, width: int) -> list[str]:
    punct = []
    punctuationMarks = set("!.?")

    for c in text:
        if c in punctuationMarks:
            punct.append(c)

    sentences = text.split(".")
    sentences = " ".join(sentences).split("?")
    sentences = " ".join(sentences).split("!")
    sentences = " ".join(sentences).split("  ")

    res = ["*" * (width + 2)]
    curLine = ""

    i = 0
    while i < len(sentences):
        curLine = "*   "

        if len(sentences[i]) < width:
            res.append(curLine + sentences[i] + punct[i] + " " *
                       (width - len(sentences[i] + curLine)) + "*")
        else:
            sentenceParts = sentences[i].split(" ")

            j = 0
            while j < len(sentenceParts):
                curLine += sentenceParts[j] + " "
                j += 1

                if j == len(sentenceParts) or len(curLine + sentenceParts[j]) > width:
                    if j == len(sentenceParts):
                        curLine = curLine.rstrip() + punct[i]
                        
                    res.append(curLine + " " *
                               (width - len(curLine) + 1) + "*")
                    curLine = "* "
        i += 1

    res.append("*" * (width + 2))
    return res


res = (articleJustify(text, 16))
for line in res:
    print(line)
