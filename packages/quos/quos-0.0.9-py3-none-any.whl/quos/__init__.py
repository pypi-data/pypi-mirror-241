import os
import matplotlib.pyplot as plt
from matplotlib.image import imread
from matplotlib.offsetbox import OffsetImage, AnnotationBbox


def qdoc():
    """
    Output: Html list of various gates
    """
    import webbrowser
    try:
        webbrowser.open((__file__).replace('__init__.py','') + "qdoc.html")
    except:
        webbrowser.open("qdoc.html") #  new=2)

def qplt(ssgqt):
    """
    Output: Matplotlib plot
    ssgqt : String of sgqt strings concatenated by pipe ('|')
    sgqt  : String of g q t strings concatenated by comma
    g     : String of item-name and applicable arguments strings concatenated by space
    q     : a (for all) or Positive integer denoting qudit sequence number
    t     : Positive integer denoting opertation time sequence number
    """
    asgqt = ssgqt.split('|')
    qmx, tmx = 0, 0
    for sgqt in asgqt:
        agqt = sgqt.split(",")
        q, t = agqt[1], int(agqt[2])
        if not (q=="a"):
            if (int(q) > qmx): qmx = int(q)
        if (t > tmx): tmx = t
        if len(agqt) > 3:
            q, t = agqt[4], int(agqt[5])
            if not (q=="a"):
                if (int(q) > qmx): qmx = int(q)
            if (t > tmx): tmx = t
    fig = plt.figure()
    ax=fig.add_subplot(1,1,1)
    ax.set_xlim(0, tmx+1)
    ax.set_ylim(-qmx-1, 0)
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    try:
        idir = (__file__).replace('__init__.py','') + 'icons/'
    except:
        idir = 'icons/'
    for q in range(1, qmx+1):
        ax.axhline(-q, color='red', lw=1)
        ax.add_artist(AnnotationBbox(
            OffsetImage(imread(idir +'0.jpg')),
            (0, -q), frameon=False))
    for sgqt in asgqt:
        agqt = sgqt.split(",")
        g, q, t = agqt[0].split(" ")[0], agqt[1], int(agqt[2])
        if q=="a":
            r = range(1,qmx+1)
        else:
            r = [int(q)]
        if (t==0) and (g=="1"):
            for p in r:
                ax.add_artist(AnnotationBbox(
                    OffsetImage(imread(idir + '1.jpg')),
                    (0, -p), frameon=False))
        if (t>0) and (g in ['0','1','C','Cd','H','I','iSw','K','M','O','Ph','Pp','R','Rx','Ry','Rz','S','Sw','T','V','X','Y','Z']):
            for p in r:
                ax.add_artist(AnnotationBbox(
                    OffsetImage(imread(idir + g + '.jpg')),
                    (t, -p), frameon=False))
                if len(agqt) > 3:
                    g1, q1, t1 = agqt[3].split(" ")[0], agqt[4], int(agqt[5])
                    if q1=="a":
                        r1 = range(1,qmx)
                    else:
                        r1 = [int(q1)]
                    for p1 in r1:
                        ax.add_artist(AnnotationBbox(
                            OffsetImage(imread(idir + g1 + '.jpg')),
                            (t1, -p1), frameon=False))
                        plt.plot([t,t1], [-p,-p1], 'b')
    plt.show()

def qsim(ssgqt):
    """
    Output: Matplotlib plot
    ssgqt : String of sgqt strings concatenated by pipe ('|')
    sgqt  : String of g q t strings concatenated by comma
    g     : String of item-name and applicable arguments strings concatenated by space
    q     : Positive integer denoting qudit sequence number
    t     : Positive integer denoting opertation time sequence number
    """
    print(ssgqt)

'''
qsim("This is to test qsim.")
qdoc()
qplt('1,3,0|H,1,1|X,2,1|Z,3,2|Y,4,2|C,1,3,X,3,3|K,4,3|Rx 30,2,4|R 30 30 60,3,4|Cd,4,5,H,3,6|Ph 15,1,5|Pp 45,2,5|Ry 45,4,6|Sw,1,6,Sw,2,6|S,4,4|Rz 15,1,7|T,3,7|V,4,7|O,a,8|iSw,1,9,iSw,4,9|M,a,10')
'''