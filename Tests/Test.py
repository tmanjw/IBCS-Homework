
def rgbtohex(red=127,green=0,blue=255):
    rgb=[red,green,blue]
    colours=["R:","G:","B:"]
    printout=""
    for x in range(0,3):
        printout+=colours[x]
        printout+=str(hex(rgb[x]))[2:].upper()
        printout+=" "
    print(printout)

def hextorgb(red="7F",green="0",blue="FF"):
    rgb = [red, green, blue]
    colours = ["R:", "G:", "B:"]
    printout=""
    for x in range(0,3):
        printout+=colours[x]
        printout+=str(int(rgb[x],16))
        printout+=" "
    print(printout)

rgbtohex()
hextorgb()
