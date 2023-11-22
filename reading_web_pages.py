import urllib.request, urllib.parse, urllib.error
hand=urllib.request.urlopen('https://www.freecodecamp.org/learn/responsive-web-design/basic-html-and-html5/nest-an-anchor-element-within-a-paragraph')
for line in hand:
    print(line.decode().strip())
    
