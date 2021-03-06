import requests
from bs4 import BeautifulSoup

# vo

class Product:
    def __init__(self, goodId=None, goodName=None, goodUnitDivCode=None,
                 goodBaseCnt=None, goodSmlclsCode=None, detailMean=None, goodTotalCnt=None, goodTotalDivCode=None):

        self.goodId = goodId
        self.goodName = goodName
        self.goodUnitDivCode = goodUnitDivCode
        self.goodBaseCnt = goodBaseCnt
        self.goodSmlclsCode = goodSmlclsCode
        self.detailMean = detailMean
        self.goodTotalCnt = goodTotalCnt
        self.goodTotalDivCode = goodTotalDivCode

class Service:
    def __init__(self):
        self.base_url = 'http://openapi.price.go.kr/openApiImpl/ProductPriceInfoService/getProductInfoSvc.do'
        self.api_key = 'maOhzLUdWh%2B71An2U%2F5nloeLuy%2F2dJSnnTbxJx8sw4RkZapqOELDIIEJIZps6T6XuEv3Gz1NwlHby%2BLQE2L%2F1A%3D%3D'


    # 상품 목록 전체
    def getProductInfoAll(self):
        url = self.base_url + '?ServiceKey=' + self.api_key
        html = requests.get(url).text
        root = BeautifulSoup(html, 'lxml-xml')
        code = root.find('resultCode').text
        resultMsg = root.find('resultMsg').text
        goods = []

        if code == '00':
            items = root.select('item')
            for item in items:
                goodId = int(item.find('goodId').text)
                goodName = item.find('goodName').text
                goodUnitDivCode = item.find('goodUnitDivCode').text
                goodBaseCnt = item.find('goodBaseCnt').text
                goodSmlclsCode = item.find('goodSmlclsCode').text
                if item.find('detailMean'):
                    detailMean = item.find('detailMean').text
                else:
                    detailMean = None
                goodTotalCnt = item.find('goodTotalCnt').text
                goodTotalDivCode = item.find('goodTotalDivCode').text

                goods.append(Product(goodId=goodId, goodName=goodName, goodUnitDivCode=goodUnitDivCode,
                                     goodBaseCnt=goodBaseCnt, goodSmlclsCode=goodSmlclsCode, detailMean=detailMean,
                                     goodTotalCnt=goodTotalCnt, goodTotalDivCode=goodTotalDivCode))
            goods.sort(key=lambda Product:Product.goodId)
            return goods

        else:
            print('오류 발생 code', code)
            print('오류 발생 메세지', resultMsg)

    # 상품 아이디로 검색
    def getProductInfoOne(self, goodId):
        cmd = '?goodId='
        url = self.base_url + cmd + goodId + '&ServiceKey=' + self.api_key
        html = requests.get(url).text
        root = BeautifulSoup(html, 'lxml-xml')
        code = root.find('resultCode').text
        resultMsg = root.find('resultMsg').text
        goods = []

        if code == '00':
            goodId = root.find('goodId').text
            goodName = root.find('goodName').text
            goodUnitDivCode = root.find('goodUnitDivCode').text
            goodBaseCnt = root.find('goodBaseCnt').text
            goodSmlclsCode = root.find('goodSmlclsCode').text
            if root.find('detailMean'):
                detailMean = root.find('detailMean').text
            else:
                detailMean = None

            goodTotalCnt = root.find('goodTotalCnt').text
            goodTotalDivCode = root.find('goodTotalDivCode').text

            goods.append(Product(goodId=goodId, goodName=goodName, goodUnitDivCode=goodUnitDivCode,
                                 goodBaseCnt=goodBaseCnt, goodSmlclsCode=goodSmlclsCode, detailMean=detailMean,
                                 goodTotalCnt=goodTotalCnt, goodTotalDivCode=goodTotalDivCode))
            return goods

        else:
            print('오류 발생 code', code)
            print('오류 발생 메세지', resultMsg)


    # 상품 이름으로 검색
    def getProductInfoByName(self, productName):
        url = self.base_url + '?ServiceKey=' + self.api_key
        html = requests.get(url).text
        root = BeautifulSoup(html, 'lxml-xml')
        code = root.find('resultCode').text
        resultMsg = root.find('resultMsg').text
        goods = []

        if code == '00':
            items = root.select('item')
            for item in items:
                if productName in item.find('goodName').text:
                    goodId = item.find('goodId').text
                    goodName = item.find('goodName').text
                    goodUnitDivCode = item.find('goodUnitDivCode').text
                    goodBaseCnt = item.find('goodBaseCnt').text
                    goodSmlclsCode = item.find('goodSmlclsCode').text
                    if item.find('detailMean'):
                        detailMean = item.find('detailMean').text
                    else:
                        detailMean = None
                    goodTotalCnt = item.find('goodTotalCnt').text
                    goodTotalDivCode = item.find('goodTotalDivCode').text

                    goods.append(Product(goodId=goodId, goodName=goodName, goodUnitDivCode=goodUnitDivCode,
                                         goodBaseCnt=goodBaseCnt, goodSmlclsCode=goodSmlclsCode, detailMean=detailMean,
                                         goodTotalCnt=goodTotalCnt, goodTotalDivCode=goodTotalDivCode))

            return goods

        else:
            print('오류 발생 code', code)
            print('오류 발생 메세지', resultMsg)

    # 상품 아이디, 이름 가져오기
    def getProductNameList(self):
        url = self.base_url + '?ServiceKey=' + self.api_key
        html = requests.get(url).text
        root = BeautifulSoup(html, 'lxml-xml')
        code = root.find('resultCode').text
        resultMsg = root.find('resultMsg').text
        goods = []

        if code == '00':
            items = root.select('item')
            for item in items:
                goodId = item.find('goodId').text
                goodName = item.find('goodName').text

                goods.append(Product(goodId=goodId, goodName=goodName))

            return goods

        else:
            print('오류 발생 code', code)
            print('오류 발생 메세지', resultMsg)

