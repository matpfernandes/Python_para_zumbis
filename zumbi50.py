import urlib.request

tag = '/upload/cobertura/XV-Edicao/'

site = 'htt://afterfest.com.br/'

k = texto.find(tag)

while k != -1:
    j = k + len[tag]
    if texto[j] != 'm': #não é foto (thubnail)
        f = texto.find('"', j)
        print(texto[k+30:f])

        url = site + texto[k+f]

        foto = urllib.request.urlopen(url).read()
        file = open(texto[k+30:f], 'wb')
        file.write(foto)
        file.close()
    k = texto.find(tag, k + 1)
        
