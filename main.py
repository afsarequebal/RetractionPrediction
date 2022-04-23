from bs4 import BeautifulSoup
import numpy as np
import csv

# This script is used to read html documents(taken from retractionWatchDatabase and reading doi number, retraction reason, authors etc.
def scrape():
    with open('retraction.html') as html_file:
        soup = BeautifulSoup(html_file, 'lxml')
    reasonArr = []
    filteredReasonArr=[]
    retractedDoiArr = []
    filteredRetractedDoiArr = []
    originalDate = []
    filteredOriginalDate = []
    retractedDate = []
    filteredRetractedDate = []
    articleType = []
    filteredarticleType = []
    retractionTable = soup.find('table', id='grdRetraction')
    for paper in retractionTable.find_all('tr', class_='mainrow'):
        tdx = paper.find_all('td')
        if tdx[4].find('span', class_='rNature').text != 'unavailable':

            reason = ", ".join([str(item.text) for item in tdx[2].find_all('div', class_='rReason')])
            reasonArr.append(reason)
            retractedDoiArr.append(tdx[4].find('span', class_='rNature').text)
            originalDate.append(tdx[4].contents[0])
            retractedDate.append(tdx[5].contents[0])
            articleType.append(tdx[6].contents[0])

    with open('retractedPapers.csv', 'w', newline='') as file:
        mywriter = csv.writer(file, delimiter=',')
        mywriter.writerows(zip(retractedDoiArr, reasonArr,
                               originalDate, retractedDate, articleType))


scrape()
