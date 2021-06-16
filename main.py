

import pywinmacro as pw
import time

location1 = (203, 57)  # addr
location2 = (487, 159)  # news button
location3 = (43, 653)  #new search
location4 = (423,305)   #검색창
#location5 = (589,305)   #검색버튼

#조회 대상 티커코드
stocks = ["삼성전자", "카카오", "네이버"]

# 역대 주가 정보를 다운받는 함수
def news_search(ticker):
    # 티커코드 입력

    pw.click(location3)
    time.sleep(3)
    # 종목창 클릭
    pw.click(location4)
    time.sleep(3)
    pw.type_in(ticker)
    time.sleep(3)
    # 엔터
    pw.key_press_once("enter")
    time.sleep(3)

#stock 리스트
def get_financenews_data(stocks):
    for stock in stocks:
        #개별 종목 news 조회
        news_search(stock)
        time.sleep(3)

#네이버 접속
def go_to_naverfinance():
    # 주소창 클릭
    pw.click(location1)
    time.sleep(1)
    # 네이버 파이낸스 주소 입력
    pw.type_in("https://finance.naver.com")
    time.sleep(1)
    # 엔터키 입력
    pw.key_press_once("enter")
    time.sleep(1)
    pw.click(location2)  #뉴스 버튼
    time.sleep(3)

#야후 파이낸스 접속
go_to_naverfinance()

#뉴스 검색 작업
get_financenews_data(stocks)



