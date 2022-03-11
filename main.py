from bs4 import BeautifulSoup
import requests


def scrape():
    with open('retraction.html') as html_file:
        soup = BeautifulSoup(html_file, 'lxml')

    retractionTable = soup.find('table', id='grdRetraction')
    for paper in retractionTable.find_all('tr', class_='mainrow'):
        tdx = paper.find_all('td')
        reason = ", ".join([str(item.text) for item in tdx[2].find_all('div', class_='rReason')])
        print(reason)
        #for r in reason:
         #   print(r.text)
        print(tdx[4].find('span', class_='rNature').text)
        print(tdx[5].find('span', class_='rNature').text)
        # for i in range(1, len(tdx)):
        #   print(tdx[i])
        print('')


scrape()
