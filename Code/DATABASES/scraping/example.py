from bs4 import BeautifulSoup

with open("index.html", "r") as f:
    data = f.read()

#print(data)

soup = BeautifulSoup(data, 'html.parser')

#print(soup)

divs = list(soup.select("div"))

#print(len(divs), "divs found")

#for d in divs:
#    print("\n --> ")
#    print(d)

#print(divs[0].get_text())
#print(divs[1].get_text())


pps = divs[1].select("p")

#print(len(pps), "ps found")
#for p in pps:
#    print(p.get_text())


dailies = soup.select(".daily")
#for p in dailies:
#    print("daily:", p)

ourp = dailies[1]

print(ourp)
print(ourp.get_text())
print(ourp.attrs['data-value'])


