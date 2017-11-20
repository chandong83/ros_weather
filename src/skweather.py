#-*- coding:utf-8 -*-
import sys
import requests

# SK Planet에서 키 요청 받아야 함.
# https://developers.skplanetx.com/develop/
# 앱 등록 및 키 발급
appKey = "00000000-0000-0000-0000-000000000000"
#appKey = "0b3c7d46-d4fb-3545-ac1f-ab3d51e4c07a"


# 현재 날씨(시간별)
url_hourly = "http://apis.skplanetx.com/weather/current/hourly"
# 현재 날씨(분별)
url_minutely = "http://apis.skplanetx.com/weather/current/minutely"

headers = {'Content-Type': 'application/json; charset=utf-8',
           'appKey': appKey}

#현재 날씨(시간별)
def hourly(weather):
    # print(weather)
    # 상대 습도
    humidity     = weather['humidity']

    # 발표 시간
    timeRelease  = weather['timeRelease']

    # 격자정보
    # 위도
    grid_latitude  = weather['grid']['latitude']
    # 경도
    grid_longitude = weather['grid']['longitude']
    # 시, 도
    grid_city      = weather['grid']['city']
    # 시, 군, 구
    grid_county    = weather['grid']['county']
    # 읍, 면, 동
    grid_village   = weather['grid']['village']

    # 기온 정보
    # 오늘의 최고기온
    temperature_tmax = weather['temperature']['tmax']
    # 1시간 현재기온
    temperature_tc = weather['temperature']['tc']
    # 오늘의 최저기온
    temperature_tmin = weather['temperature']['tmin']

    # 낙뢰유무(해당 격자 내)
    # - 0: 없음
    # - 1: 있음
    lightning = weather['lightning']

    # 강수량
    # 강수형태코드
    # - 0: 현상없음 → rain(sinceOntime) 사용
    # - 1: 비       → rain(sinceOntime) 사용
    # - 2: 비/눈 → precipitation(sinceOntime) 사용
    # - 3: 눈    → precipitation(sinceOntime) 사용
    precipitation_type = weather['precipitation']['type']

    # 1시간 누적 강수량
    # - if type=0/1/2 → 강우량 (mm)
    # - if type=3     → 적설량 (cm)
    precipitation_sinceOntime = weather['precipitation']['sinceOntime']

    # 바람정보
    # 풍향 (dgree)
    wind_wdir = weather['wind']['wdir']
    # 풍속 (m/s)
    wind_wspd = weather['wind']['wspd']

    # 하늘 상태 정보
    # 하늘상태코드명
    # - SKY_A01: 맑음
    # - SKY_A02: 구름조금
    # - SKY_A03: 구름많음
    # - SKY_A04: 구름많고 비
    # - SKY_A05: 구름많고 눈
    # - SKY_A06: 구름많고 비 또는 눈
    # - SKY_A07: 흐림
    # - SKY_A08: 흐리고 비
    # - SKY_A09: 흐리고 눈
    # - SKY_A10:  흐리고 비 또는 눈
    # - SKY_A11: 흐리고 낙뢰
    # - SKY_A12: 뇌우, 비
    # - SKY_A13: 뇌우, 눈
    # - SKY_A14: 뇌우, 비 또는 눈
    sky_name = weather['sky']['name']
    # 하늘상태코드
    sky_code = weather['sky']['code']

    #현재 기온 + 날씨 + 풍속
    str = temperature_tc + ',' + sky_name +  ',' + wind_wspd
    #print(str)
    return str


#현재 날씨(분별)
def minutely(weather):
    #print(weather)

    # 상대 습도
    humidity     = weather['humidity']
    # 기압정보
    # 현지기압(Ps)
    pressure_surface  = weather['pressure']['surface']
    # 해면기압(SLP)
    pressure_seaLevel  = weather['pressure']['seaLevel']
    # 관측소
    # 관측소명
    station_name      = weather['station']['name']
    # 관측소 지점번호(stnid)
    station_id      = weather['station']['id']
    # 관측소 유형
    #- KMA: 기상청 관측소
    #- BTN: SKP 관측소
    station_type  = weather['station']['type']
    # 위도
    station_latitude  = weather['station']['latitude']
    # 경도
    station_longitude = weather['station']['longitude']

    # 기온 정보
    # 오늘의 최고기온
    temperature_tmax = weather['temperature']['tmax']
    # 1시간 현재기온
    temperature_tc = weather['temperature']['tc']
    # 오늘의 최저기온
    temperature_tmin = weather['temperature']['tmin']

    # 낙뢰유무(해당 격자 내)
    # - 0: 없음
    # - 1: 있음
    lightning = weather['lightning']

    # 강수량
    # 강수형태코드
    # - 0: 현상없음 → rain(sinceOntime) 사용
    # - 1: 비       → rain(sinceOntime) 사용
    # - 2: 비/눈 → precipitation(sinceOntime) 사용
    # - 3: 눈    → precipitation(sinceOntime) 사용
    precipitation_type = weather['precipitation']['type']
    # 1시간 누적 강수량
    # - if type=0/1/2 → 강우량 (mm)
    # - if type=3     → 적설량 (cm)
    precipitation_sinceOntime = weather['precipitation']['sinceOntime']

    # 바람정보
    # 풍향 (dgree)
    wind_wdir = weather['wind']['wdir']
    # 풍속 (m/s)
    wind_wspd = weather['wind']['wspd']

    # 하늘 상태 정보
    # 하늘상태코드명
    # - SKY_A01: 맑음
    # - SKY_A02: 구름조금
    # - SKY_A03: 구름많음
    # - SKY_A04: 구름많고 비
    # - SKY_A05: 구름많고 눈
    # - SKY_A06: 구름많고 비 또는 눈
    # - SKY_A07: 흐림
    # - SKY_A08: 흐리고 비
    # - SKY_A09: 흐리고 눈
    # - SKY_A10:  흐리고 비 또는 눈
    # - SKY_A11: 흐리고 낙뢰
    # - SKY_A12: 뇌우, 비
    # - SKY_A13: 뇌우, 눈
    # - SKY_A14: 뇌우, 비 또는 눈
    sky_name = weather['sky']['name']
    # 하늘상태코드
    sky_code = weather['sky']['code']

    # 강우정보
    # 1시간 누적 강우량
    rain_sinceOntime   = weather['rain']['sinceOntime']
    # 일 누적 강우량
    rain_sinceMidnight = weather['rain']['sinceMidnight']
    # 10분 이동누적 강우량
    rain_last10min     = weather['rain']['last10min']
    # 15분 이동누적 강우량
    rain_last15min     = weather['rain']['last15min']
    # 30분 이동누적 강우량
    rain_last30min     = weather['rain']['last30min']
    # 1시간 이동누적 강우량
    rain_last1hour     = weather['rain']['last1hour']
    # 6시간 이동누적 강우량
    rain_last6hour     = weather['rain']['last6hour']
    # 12시간 이동누적 강우량
    rain_last12hour    = weather['rain']['last12hour']
    # 24시간 이동누적 강우량
    rain_last24hour    = weather['rain']['last24hour']

    #현재 기온 + 날씨 + 풍속
    str = temperature_tc + ',' + sky_name +  ',' + wind_wspd
    #print(str)
    return str


def requestCurrentWeather(city, county, village, isHourly = True):
    params = { "version": "1",
                "city": city,
                "county": county,
                "village": village }
    print(city + ' ' + county + ' ' + village + ' ' + str(isHourly))
    if isHourly:
        response = requests.get(url_hourly, params=params, headers=headers)
    else:
        response = requests.get(url_minutely, params=params, headers=headers)

    if response.status_code == 200:
        response_body = response.json()
        #print(response.json())
        #날씨 정보
        try:
            if isHourly:
                weather_data = response_body['weather']['hourly'][0]
            else:
                weather_data = response_body['weather']['minutely'][0]

            if isHourly:
                ret = hourly(weather_data)
            else:
                ret = minutely(weather_data)

            return ret
        except:
            pass
            print(response_body)
            return 'failed'
    else:
        pass
        print(response.status_code)
        return response.status_code
        #에러


if __name__ == '__main__':
    #city = '경기'  #'도' 나 '시'는 빼고 넣는다.
    #county = '김포시' #시 or 구
    #village = '장기동' #동
    # 시간별 (기본)
    requestCurrentWeather('경기','김포시','장기동')
    requestCurrentWeather('경기','김포시','장기동', False)
