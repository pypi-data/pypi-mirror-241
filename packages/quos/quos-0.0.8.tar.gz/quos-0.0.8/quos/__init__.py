import os
import matplotlib.pyplot as plt
from matplotlib.image import imread
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import webbrowser

def qdoc():
    """
    Output: Html list of various gates
    """
    webbrowser.open("qdoc.html", new=2)

def qplt(ssgqt):
    """
    Output: Matplotlib plot
    ssgqt : String of sgqt strings concatenated by pipe ('|')
    sgqt  : String of g q t strings concatenated by comma
    g     : String of item-name and applicable arguments strings concatenated by space
    q     : Positive integer denoting qudit sequence number
    t     : Positive integer denoting opertation time sequence number
    """
    asgqt = ssgqt.split('|')
    qmx, tmx = 0, 0
    for sgqt in asgqt:
        agqt = sgqt.split(",")
        q, t = int(agqt[1]), int(agqt[2])
        if (q > qmx): qmx = q
        if (t > tmx): tmx = t
        if len(agqt) > 3:
            q, t = int(agqt[4]), int(agqt[5])
            if (q > qmx): qmx = q
            if (t > tmx): tmx = t
    fig = plt.figure()
    ax=fig.add_subplot(1,1,1)
    ax.set_xlim(0, tmx+1)
    ax.set_ylim(-qmx-1, 0)
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    idir = 'icons/'
    if os.path.isfile('icons/0.jpg'):
        idir = (__file__).replace('__init__.py','') + idir
    for q in range(1, qmx+1):
        ax.axhline(-q, color='red', lw=1)
        ax.add_artist(AnnotationBbox(
            OffsetImage(imread(idir +'0.jpg')),
            (0, -q), frameon=False))
    for sgqt in asgqt:
        agqt = sgqt.split(",")
        g = agqt[0].split(" ")[0]
        q, t = int(agqt[1]), int(agqt[2])
        if (t==0) and (q>0) and (g=="1"):
            ax.add_artist(AnnotationBbox(
                OffsetImage(imread(idir + '1.jpg')),
                (0, -q), frameon=False))
        if (t>0) and (q>0) and (g in ['0','1','C','Cd','H','I','iSw','Ph','Pp','R','Rx','Ry','Rz','S','Sw','T','V','X','Y','Z']):
            ax.add_artist(AnnotationBbox(
                OffsetImage(imread(idir + g + '.jpg')),
                (t, -q), frameon=False))
            if len(agqt) > 3:
                g, q1, t1 = agqt[3].split(" ")[0], int(agqt[4]), int(agqt[5])
                if q > 0 and t> 0:
                    ax.add_artist(AnnotationBbox(
                        OffsetImage(imread(idir + g + '.jpg')),
                        (t1, -q1), frameon=False))
                    plt.plot([t,t1], [-q,-q1], 'b')
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
qplt('1,3,0|H,1,1|X,2,1|Z,3,2|Y,4,2|C,1,3,X,3,3|Rx 30,2,4|R 30 30 60,3,4|Cd,4,5,H,3,6|Ph 15,1,5|Pp 45,2,5|Ry 45,4,6|Sw,1,6,Sw,2,6|S,4,4|Rz 15,1,7|T,3,7|V,4,7|iSw,1,8,iSw,4,8')
'''