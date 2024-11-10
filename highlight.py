def highlight(text,hlwords):
    #notDone = True
    output = text
    for word in hlwords:
        subtext = output
        peices = []
        while word in subtext:
            startIndex = subtext.index(word)
            peices.append(subtext[:startIndex] + '<b style="color:yellow;">' + word + '</b>')
            subtext = subtext[startIndex+len(word):]
        peices.append(subtext)
        output = ""
        for p in peices:
            output = output + p
    return output
            
            