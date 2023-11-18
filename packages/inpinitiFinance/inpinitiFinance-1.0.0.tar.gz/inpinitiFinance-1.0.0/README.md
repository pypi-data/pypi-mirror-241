# inpiniti finance

본 모듈은 Dart 전자공시시스템에서 재무정보와
KRX 정보데이터시스템에서 개별종목 시세 추이 그리고
Daum 에서 섹터정보 및 종목정보를 조회하는 라이브러리입니다.

API 사용에 대한 책임은 사용자 본인에게 있으며, 도의적으로 무분별한 호출을 자제해 주시기 부탁드립니다. 또한 결과물은 참고용으로만 사용하셔야 하며, 투자에 대한 책임은 사용자에게 있습니다.

## 환경설정

### dart api key

dart 를 이용하시려면 dart에서 생성한 api_key 를 지정해주셔야 합니다.

```
api_key = 'your_api_key_here'

dt.set_api_key(api_key)
```

### 예시

```
import ifinance as dt

api_key = 'your_api_key_here'

dt.set_api_key(api_key)

df = dt.get_financial_dataframe('005930')
print(df)

df = dt.get_sector_dataframe()
print(df)

df = dt.get_stock_dataframe('G101010')
print(df)

df = dt.get_monthly_stock_dataframe('KR7005930003')
print(df)
```
