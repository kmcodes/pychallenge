string = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc" \
        " dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr" \
        " gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml" \
        " rfc spj."
url = '/pc/def/'
mapped = 'map'


def trans(c):
    if c >= 'a' and c <= 'z':
        result = ord(c) + 2

        if result > ord('z'):
            result -= ord('z') - ord('a') + 1

        return chr(result)
    else:
        return c

print ''.join(map(trans, string))
print url + ''.join(map(trans, mapped)) + '.html'