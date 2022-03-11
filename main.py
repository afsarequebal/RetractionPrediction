from bs4 import BeautifulSoup
import numpy as np
import csv

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
            #print(reason)

            # original doi
            #print(tdx[4].find('span', class_='rNature').text)
            retractedDoiArr.append(tdx[4].find('span', class_='rNature').text)
            originalDate.append(tdx[4].contents[0])
            retractedDate.append(tdx[5].contents[0])
            articleType.append(tdx[6].contents[0])
        # retracted doi
        #print(tdx[5].find('span', class_='rNature').text)


        #print('')
   # np1 = np.array(retractedDoiArr)
   # np2 = np.array(reasonArr)
    #np.reshape(retractedDoiArr, -1)
    #np.reshape(reasonArr, -1)
   # print(np1.shape)
   # print(np2.shape)
    #a = np.array([retractedDoiArr, reasonArr])
   # a = np.array(np1, np2)

    with open('retractedPapers.csv', 'w', newline='') as file:
        mywriter = csv.writer(file, delimiter=',')
        mywriter.writerows(zip(retractedDoiArr, reasonArr,
                               originalDate, retractedDate, articleType))


scrape()
