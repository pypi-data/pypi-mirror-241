import webbrowser

url = 'file:///path/to/your/file/testdata.html'
webbrowser.open(url, new=2)  # open in new tab

def qdoc(s):
    """
    Output: Html list of various gates
    s : Option string 'q' or 'w'
    """
    print(s)
    zurl=r'Quos.html'
    if s=='w':
        zurl=r'Wiki.html'
    webbrowser.open(zurl, new=2)

qdoc('w')
