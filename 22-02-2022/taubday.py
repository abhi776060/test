
def taumBdawc(b, w, bc, wc, z):
    if bc + z < wc:
        print(b*bc+w*(bc+z))
    elif wc + z < bc:
        print(w*wc+b*(wc+z))
    else:
        print(b*bc+w*wc)
taumBdawc(10,10,1,1,1)