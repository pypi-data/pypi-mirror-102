# SchoolInfo

`Neis API` 기반으로 학교 정보, 급식 정보, 반 정보, 시간표 정보 등 제공 비동기 서비스  
이슈와 풀리퀘스트 환영합니다 :D

## 설치하기
```sh
pip install schoolInfo 
```

## 시작하기

[다음은 예시코드입니다.](./tests/test.py)
```python
import asyncio

import schoolInfo


async def main():
    print_end : str = "\n\n\n\n\n"
    school_data: dict = await schoolInfo.search("광주소프트웨어마이스터고등학교")
    print(school_data, end=print_end)
    # 학교를 검색하는 구문입니다.

    meal_data: dict = await schoolInfo.meal(
        ATPT_OFCDC_SC_CODE=school_data["ATPT_OFCDC_SC_CODE"],
        SD_SCHUL_CODE=school_data["SD_SCHUL_CODE"],
    )
    print(meal_data, end=print_end)
    # 급식을 가져오는 구문입니다.

    schedule_data: dict = await schoolInfo.schedule(
        ATPT_OFCDC_SC_CODE=school_data["ATPT_OFCDC_SC_CODE"],
        SD_SCHUL_CODE=school_data["SD_SCHUL_CODE"],
    )
    print(schedule_data, end=print_end)
    # 스케쥴을 가져오는 구문입니다.

    major_data: dict = await schoolInfo.major(
        ATPT_OFCDC_SC_CODE=school_data["ATPT_OFCDC_SC_CODE"],
        SD_SCHUL_CODE=school_data["SD_SCHUL_CODE"],
    )
    print(major_data, end=print_end)
    # 학교 학과 정보를 가져오는 구문입니다.

    class_data: dict = await schoolInfo.classes(
        ATPT_OFCDC_SC_CODE=school_data["ATPT_OFCDC_SC_CODE"],
        SD_SCHUL_CODE=school_data["SD_SCHUL_CODE"],
    )
    print(class_data, end=print_end)
    # 반정보를 가져오는 구문입니다.

    timetable_data : dict = await schoolInfo.timetable(
        ATPT_OFCDC_SC_CODE=school_data["ATPT_OFCDC_SC_CODE"],
        SD_SCHUL_CODE=school_data["SD_SCHUL_CODE"],
        SCHUL_KND_SC_NM=school_data["SCHUL_KND_SC_NM"]
    )
    print(timetable_data, end=print_end)
    # 시간표를 가져오는 구문입니다.

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
```
## 기능명세

### 공통 인자값

|Name|Type|Description|
|:-:|:-:|:-:|
|`ATPT_OFCDC_SC_CODE`|string|시도교육청코드|
|`SD_SCHUL_CODE`|string|표준학교코드|

### 학교 검색 및 기본정보 가져오기
```python
school_data : dict = await schoolInfo.search("광주소프트웨어마이스터고등학교", auth_key={your auth key})
print(school_data)
```

1. First args : 검색값
2. auth_key : [https://open.neis.go.kr/portal/guide/actKeyPage.do](https://open.neis.go.kr/portal/guide/actKeyPage.do)
    - Neis API의 인증키값입니다.

```js
{
   "ATPT_OFCDC_SC_CODE":"F10", // 시도 교육청 코드
   "ATPT_OFCDC_SC_NM":"광주광역시교육청", // 시도교육청 명
   "SD_SCHUL_CODE":"7380292", // 표준학교코드
   "SCHUL_NM":"광주소프트웨어마이스터고등학교", // 학교명
   "ENG_SCHUL_NM":"Gwangju Software Meister High School", // 영문학교명
   "SCHUL_KND_SC_NM":"고등학교", // 학교 구분
   "LCTN_SC_NM":"광주광역시", // 소재지명
   "JU_ORG_NM":"광주광역시교육청", // 관할조직명
   "FOND_SC_NM":"공립", // 설립명
   "ORG_RDNZC":"62423 ", // 도로명 우편번호
   "ORG_RDNMA":"광주광역시 광산구 상무대로 312", // 도로명 주소
   "ORG_RDNDA":"(송정동)", // 도로명 상세주소
   "ORG_TELNO":"062-949-6800", // 전화번호
   "HMPG_ADRES":"http://gsm.gen.hs.kr/", // 홈페이지 주소
   "COEDU_SC_NM":"남여공학", // 남녀공학구분
   "ORG_FAXNO":"062-944-8019", // 팩스번호
   "HS_SC_NM":"특목고", // 고등학교 구분명
   "INDST_SPECL_CCCCL_EXST_YN":"N", // 산업체특별학급존재여부
   "HS_GNRL_BUSNS_SC_NM":"전문계", // 고등학교 계열 구분
   "SPCLY_PURPS_HS_ORD_NM":"None", // 특수목적고등학교 계열명
   "ENE_BFE_SEHF_SC_NM":"전기", // 입시전후기 구분명
   "DGHT_SC_NM":"주간", // 주야구분명
   "FOND_YMD":"19540529", // 설립일자
   "FOAS_MEMRD":"19540601", // 개교기념일
   "LOAD_DTM":"20210319141311" //적재일시
}
```

### 급식식단정보

```python
school_data : dict = await schoolInfo.search("광주소프트웨어마이스터고등학교")
meal_data: dict = await schoolInfo.meal(
    ATPT_OFCDC_SC_CODE=school_data["ATPT_OFCDC_SC_CODE"],
    SD_SCHUL_CODE=school_data["SD_SCHUL_CODE"],
    MLSV_YMD=datetime.datetime(2021,10,10)
)
print(meal_data)
```

1. MLSV_YMD : 급식을 구할 해당 날짜입니다.

**결과값**

```js
[
   {
      "ATPT_OFCDC_SC_CODE":"F10", // 시도교육청 코드
      "ATPT_OFCDC_SC_NM":"광주광역시교육청", // 시도교육청 명
      "SD_SCHUL_CODE":"7380292", // 표준학교코드
      "SCHUL_NM":"광주소프트웨어마이스터고등학교", // 학교명
      "MMEAL_SC_CODE":"1", // 식사코드
      "MMEAL_SC_NM":"조식", //식사명
      "MLSV_YMD":"20211010", // 급식일자
      "MLSV_FGR":"228", // 급식인원 수
      "DDISH_NM":"백미밥..바지락무국/우유계란찜...1.9.13.*돼지불고기5.6.10.13.깍두기9.13.우리밀촉촉마들렌..1.2.5.6.13.", // 요리 명
      "ORPLC_INFO":"쌀 : 국내산김치류 : 국내산고춧가루(김치류) : 국내산쇠고기(종류) : 국내산(한우)돼지고기 : 국내산닭고기 : 국내산오리고기 : 국내산쇠고기 식육가공품 : 국내산돼지고기 식육가공품 : 국내산닭고기 식육가공품 : 국내산오리고기 가공품 : 국내산낙지 : 국내산고등어 : 국내산갈치 : 국내산오징어 : 국내산꽃게 : 국내산참조기 : 국내산콩 : 국내산", // 원산지 정보
      "CAL_INFO":"740.4 Kcal", // 칼로리 정보
      "NTR_INFO":"탄수화물(g) : 88.6단백질(g) : 52.2지방(g) : 20.1비타민A(R.E) : 211.0티아민(mg) : 0.9리보플라빈(mg) : 0.7비타민C(mg) : 7.2칼슘(mg) : 221.3철분(mg) : 6.5", // 영양분 정보
      "MLSV_FROM_YMD":"20211010", // 급식시작일자
      "MLSV_TO_YMD":"20211010" // 급식 종료 일자
   },
   .
   .
   .
   {
      "ATPT_OFCDC_SC_CODE":"F10",
      "ATPT_OFCDC_SC_NM":"광주광역시교육청",
      "SD_SCHUL_CODE":"7380292",
      "SCHUL_NM":"광주소프트웨어마이스터고등학교",
      "MMEAL_SC_CODE":"3",
      "MMEAL_SC_NM":"석식",
      "MLSV_YMD":"20211010",
      "MLSV_FGR":"238",
      "DDISH_NM":"오므라이스*1.2.5.6.10.12.13.15.16.18.근대된장국...5.6.13.삼색나물무침..수제오징어상추튀김/양념장..1.5.6.17.깍두기...9.13.",
      "ORPLC_INFO":"쌀 : 국내산김치류 : 국내산고춧가루(김치류) : 국내산쇠고기(종류) : 국내산(한우)돼지고기 : 국내산닭고기 : 국내산오리고기 : 국내산쇠고기 식육가공품 : 국내산돼지고기 식육가공품 : 국내산닭고기 식육가공품 : 국내산오리고기 가 공품 : 국내산낙지 : 국내산고등어 : 국내산갈치 : 국내산오징어 : 국내산꽃게 : 국내산참조기 : 국내산콩 : 국내산",
      "CAL_INFO":"777.0 Kcal",
      "NTR_INFO":"탄수화물(g) : 116.0단백질(g) : 42.4지방(g) : 16.8비타민A(R.E) : 446.3티아민(mg) : 0.4리보 플라빈(mg) : 0.8비타민C(mg) : 23.8칼슘(mg) : 203.3철분(mg) : 4.8",
      "MLSV_FROM_YMD":"20211010",
      "MLSV_TO_YMD":"20211010"
   }
]
```

### 일정 관련 정보

```python
school_data : dict = await schoolInfo.search("광주소프트웨어마이스터고등학교")
schedule_data : dict = await schoolInfo.schedule(
    ATPT_OFCDC_SC_CODE=school_data["ATPT_OFCDC_SC_CODE"],
    SD_SCHUL_CODE=school_data["SD_SCHUL_CODE"]
)
print(schedule_data)
```

**결과값**

```js
[
   {
      "ATPT_OFCDC_SC_CODE":"F10",
      "ATPT_OFCDC_SC_NM":"광주광역시교육청",
      "SD_SCHUL_CODE":"7380292",
      "SCHUL_NM":"광주소프트웨어마이스터고등학교",
      "AY":"2020",
      "DGHT_CRSE_SC_NM":"주간",
      "SCHUL_CRSE_SC_NM":"고등학교",
      "SBTR_DD_SC_NM":"공휴일",
      "AA_YMD":"20200301",
      "EVENT_NM":"3・1절",
      "EVENT_CNTNT":"None",
      "ONE_GRADE_EVENT_YN":"Y",
      "TW_GRADE_EVENT_YN":"Y",
      "THREE_GRADE_EVENT_YN":"Y",
      "FR_GRADE_EVENT_YN":"*",
      "FIV_GRADE_EVENT_YN":"*",
      "SIX_GRADE_EVENT_YN":"*",
      "LOAD_DTM":"20210414004454"
   },
   .
   .
   .
   {
      "ATPT_OFCDC_SC_CODE":"F10",
      "ATPT_OFCDC_SC_NM":"광주광역시교육청",
      "SD_SCHUL_CODE":"7380292",
      "SCHUL_NM":"광주소프트웨어마이스터고등학교",
      "AY":"2020",
      "DGHT_CRSE_SC_NM":"주간",
      "SCHUL_CRSE_SC_NM":"고등학교",
      "SBTR_DD_SC_NM":"휴업일",
      "AA_YMD":"20200305",
      "EVENT_NM":"코로나-19 휴업일",
      "EVENT_CNTNT":"None",
      "ONE_GRADE_EVENT_YN":"Y",
      "TW_GRADE_EVENT_YN":"Y",
      "THREE_GRADE_EVENT_YN":"Y",
      "FR_GRADE_EVENT_YN":"*",
      "FIV_GRADE_EVENT_YN":"*",
      "SIX_GRADE_EVENT_YN":"*",
      "LOAD_DTM":"20210414004454"
   }
]
```

### 학교 학과 정보

```python
school_data : dict = await schoolInfo.search("광주소프트웨어마이스터고등학교")
major_data : dict = await schoolInfo.major(
    ATPT_OFCDC_SC_CODE=school_data["ATPT_OFCDC_SC_CODE"],
    SD_SCHUL_CODE=school_data["SD_SCHUL_CODE"]
)
print(major_data)
```

**결과값**

```js
[
    {'ATPT_OFCDC_SC_CODE': 'F10',
    'ATPT_OFCDC_SC_NM': '광주광역시교육청',
    'SD_SCHUL_CODE': '7380292',
    'SCHUL_NM': '광주소프트웨어마이스터고등학교',
    'DGHT_CRSE_SC_NM': '주간',
    'ORD_SC_NM': '공업계',
    'DDDEP_NM': 'SW개발과',
    'LOAD_DTM': '20210401004927'
    },
    {'ATPT_OFCDC_SC_CODE': 'F10',
    'ATPT_OFCDC_SC_NM': '광주광역시교육청',
    'SD_SCHUL_CODE': '7380292',
    'SCHUL_NM': '광주소프트웨어마이스터고등학교',
    'DGHT_CRSE_SC_NM': '주간',
    'ORD_SC_NM': '공업계',
    'DDDEP_NM': '소프트웨어공통과정',
    'LOAD_DTM': '20210401004927'
    }
    .
    .
    .
]
```

### 시간표 정보

```python
school_data : dict = await schoolInfo.search("광주소프트웨어마이스터고등학교")
timetable_data : dict = await schoolInfo.timetable(
    ATPT_OFCDC_SC_CODE=school_data["ATPT_OFCDC_SC_CODE"],
    SD_SCHUL_CODE=school_data["SD_SCHUL_CODE"]
)
print(timetable_data)
```

**결과값**

```js
[
    {
        'ATPT_OFCDC_SC_CODE': 'F10',
        'ATPT_OFCDC_SC_NM': '광주광역시교육청',
        'SD_SCHUL_CODE': '7380292',
        'SCHUL_NM': '광주소프트웨어마이스터고등학교',
        'AY': '2020',
        'SEM': '1',
        'ALL_TI_YMD': '20200302',
        'DGHT_CRSE_SC_NM': '주간',
        'ORD_SC_NM': '공업계',
        'DDDEP_NM': 'SW개발과',
        'GRADE': '2',
        'CLRM_NM': '1',
        'CLASS_NM': '1',
        'PERIO': '1',
        'ITRT_CNTNT': '코로나-19 휴업일',
        'LOAD_DTM': '20200827165627'
    }, {
        'ATPT_OFCDC_SC_CODE': 'F10',
        'ATPT_OFCDC_SC_NM': '광주광역시교육청',
        'SD_SCHUL_CODE': '7380292',
        'SCHUL_NM': '광주소프트웨어마이스터고등학교',
        'AY': '2020',
        'SEM': '1',
        'ALL_TI_YMD': '20200302',
        'DGHT_CRSE_SC_NM': '주간',
        'ORD_SC_NM': '공업계',
        'DDDEP_NM': 'SW개발과',
        'GRADE': '2',
        'CLRM_NM': '1',
        'CLASS_NM': '1',
        'PERIO': '2',
        'ITRT_CNTNT': '코로나-19 휴업일',
        'LOAD_DTM': '20200827165627'
    } ...
]
```

### 반 정보 출력

```python
school_data : dict = await schoolInfo.search("광주소프트웨어마이스터고등학교")
class_data : dict = await schoolInfo.classes(
    ATPT_OFCDC_SC_CODE=school_data["ATPT_OFCDC_SC_CODE"],
    SD_SCHUL_CODE=school_data["SD_SCHUL_CODE"]
)
print(class_data)
```

**결과값**

```js
[
    {
        'ATPT_OFCDC_SC_CODE': 'F10',
        'ATPT_OFCDC_SC_NM': '광주광역시교육청',
        'SD_SCHUL_CODE': '7380292',
        'SCHUL_NM': '광주소프트웨어마이스터고등학교',
        'AY': '2020',
        'GRADE': '1',
        'DGHT_CRSE_SC_NM': '주간',
        'SCHUL_CRSE_SC_NM': '고등학교',
        'ORD_SC_NM': '공업계',
        'DDDEP_NM': '소프트웨어공통과정',
        'CLASS_NM': '1',
        'LOAD_DTM': '20210401002948'
    }, {
        'ATPT_OFCDC_SC_CODE': 'F10',
        'ATPT_OFCDC_SC_NM': '광주광역시교육청',
        'SD_SCHUL_CODE': '7380292',
        'SCHUL_NM': '광주소프트웨어마이스터고등학교',
        'AY': '2020',
        'GRADE': '1',
        'DGHT_CRSE_SC_NM': '주간',
        'SCHUL_CRSE_SC_NM': '고등학교',
        'ORD_SC_NM': '공업계',
        'DDDEP_NM': '소프트웨어공통과정',
        'CLASS_NM': '2',
        'LOAD_DTM': '20210401002948'
    }, etc ... 
```
