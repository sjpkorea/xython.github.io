### anydb
매번 엑셀에 저장하는 것은 실시간의 자료와 같이, 어쩔수없이 database를 사용해야 하는 경우들이 생긴다<br>
이럴때, 우리가 자주사용하는 자료의 형태들을 쉽게 변경을 할수있도록 만들면 어떨까라고 생각을 했다<br>
그렇게 만든 것이 anydb모듈입니다<br>
파이썬에서 자료를 저장하고 불러오는 기능은 여러가지가 가능하다. 그중에서 실시간으로 자료를 저장하고 분석을 하여야 하는 경우에는 어떤 방법을 할것인지에 대해서 생각을 해 보아야 한다
에를들어 주식을 분석하는 자료를 만든다고 가정을 하면, 1초에 2~3번의 자료가 들어오고, 이것을 분리후에 database나 다른 형태로 한 것을 저장하고, 앞위로 100개의 자료를 분석을 다시 갖고와서 그 자료를 실시간으로 분석을 해서 올라가는 것인지 내려가는 것인지, 예전의 상태랑 비교를 해서 그결과에 따라서 무엇인가를 해야 한다. 이러때를 보면 자료를 저장하는 속도또한 중요한 요소가 된다.

이모듈은 엑셀, list, dic, sqlite, pandas등의 자료를 서로 변경이 쉽게 되도록 만드는 기능을 넣은 것이다<br>
또는 쉽게 database를 사용해서 저장하고 관리할수있도록 만든 것이다

	database를 사용하기 쉽게 만든것
	table, df의 자료는 [제일 첫컬럼에 컬럼이름을 넣는다]

	개인적으로 만든 이용형태를 것으로,
	check로 시작하는 메소드는 자료형태의 변경이나 맞는지를 확인하는 것이다
	dataframe의 영역을 나타내는 방법을 dataframe에 맞도록 변경하는 것이다
	x=["1:2", "1~2"] ===> 1, 2열
	x=["1,2,3,4"] ===> 1,2,3,4열
	x=[1,2,3,4]  ===> 1,2,3,4열
	x=""또는 "all" ===> 전부

#### 전반적인 설명
		databse가 있는 화일의 위치를 알려주면 시작이 된다
		pandas의 장점
		1. 대용량 데이터(GB 단위 이상)를 다룰 수 있습니다. 엑셀은 데이터 용량이 100MB을 넘어가거나, 데이터가 100만 행이 넘어가면 정상적으로 작동하지 않는 현상을 겪기도 합니다.
		2. 복잡한 처리 작업들을 비교적 손쉽게 할 수 있습니다. 소위 말하는 엑셀 노가다를 할 필요가 없습니다.
		3. 손쉽게 데이터를 결합하고 분리할 수 있습니다. SQL처럼 데이터를 합치고 관계 연산을 수행할 수 있습니다.

		df.index, df.columns, df.values
		df["col1"], df[1:3]

		index는 숫자만 가능하지 않고, String(문자열) 일 수도 있다.
		index가 숫자여도 순서대로 정렬될 필요가 없다. 그리고 index는 중복될 수 있다.
		print(df.loc[:3, ['Surv', 'N']])

		df[val]	Select single column or sequence of columns from the DataFrame
		df.loc[val]	Selects single row or subset of rows from the DataFrame by label
		df.loc[:, val]	Selects single column or subset of columns by label
		df.loc[val1, val2]	Select both rows and columns by label
		df.iloc[where]	Selects single row or subset of rows from the DataFrame by integer position
		df.iloc[:, where]	Selects single column or subset of columns by integer position
		df.iloc[where_i, whe	re_j] Select both rows and columns by integer position
		df.at[label_i, label	_j] Select a single scalar value by row and column label
		df.iat[i, j]	Select a single scalar value by row and column position (integers)
		get_value(), set_val	ue() Select single value by row and column label

#### 용어

|       용어        | 설명                                                                              |
|:---------------:|---------------------------------------------------------------------------------|
|       df        | dataframe 개개체                                                                   |                       
|       df        | dataframe                                                                       |
|       con       | Connection, 외부환경과 Database를 연결하는 것. 즉 db가 위치한 곳들을 연결하는 것이지요                     |
|     cursor      | DB에 어떤 일을 시키면, Db에서 Item이라는 객체가 만들어진다. 그 만들어진곳을 가리키는 객체                         |
|     의미적인 분류     | active_document(화일) > paragraph(문단) > line(줄) > word(한 단어) > character(한글자)     |              
| active_document | 현재 선택된 워드문서, word라는 단어가 두가지 이름으로 사용되기때문에, file로 통일시킴                            |
|    paragraph    | 줄바꿈이 이루어지기 전까지의 자료                                                              |                   
|      line       | 한줄                                                                              |            
|      word       | 공백으로 구분된 단어 (다른의미 : 프로그램이름과 혼동을 피하기위해 file이라는 이름으로 사용)                          |
|    character    | 글자 1개                                                                           |            
|     content     | 라인, 문단, 단어들을 총괄적으로 뜻하는것, 항목이라고 설명하는것이 좋을듯...                                    |
|    bookmark     | 책갈피                                                                             |            
|      range      | 임의적으로 설정할수가 있으며,word밑에 range가 설정이 되고, select를 하면 selection밑에 자동으로 range객체가 설정된다 |
|    sentence     | 표현이 완결된 단위, 그 자체로 하나의 서술된 문장이 되는 것                                              |         
|    paragraph    | 줄바꿈이 이루어지기 전까지의 자료                                                              |         
|                 | MS워드를 사용하기 쉽게하기위해 만든 모듈입니다,                                                     |            
|                 | 차후에는 다른 Libero및 한글의 연동또한 만들 예정입니다                                               |              
|                 | 기본적으로 적용되는 selection은 제외한다                                                      |         

#### dataframe자료를 사전형식들
		dataframe자료를 사전형식으로 변경하는것
		dic의 형태중에서 여러가지중에 하나를 선택해야 한다

		입력형태 : data = {"calory": [123, 456, 789], "기간": [10, 40, 20]}
		출력형태 : dataframe
		dict :    {'제목1': {'가로제목1': 1, '가로제목2': 3}, '제목2': {'가로제목1': 2, '가로제목2': 4}}
		list :    {'제목1': [1, 2], '제목2': [3, 4]}
		series :  {열 : Series, 열 : Series}
		split :   {'index': ['가로제목1', '가로제목2'], 'columns': ['제목1', '제목2'], 'data': [[1, 2], [3, 4]]}
		records : [{'제목1': 1, '제목2': 2}, {'제목1': 3, '제목2': 4}]
		index :   {'가로제목1': {'제목1': 1, '제목2': 2}, '가로제목2': {'제목1': 3, '제목2': 4}}