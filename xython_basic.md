<img src="D:\my_code\icons\xython.png" width="10%" height="10%" title="px(픽셀) 크기 설정" alt="RubberDuck"></img>

## About xython module / 개요
Functional Programming for Excel, Word, Outlook, Color, Etc by Python

### Manual / 사용법
oficial document : https://sjpkorea.github.io/xython.github.io/   <br>
oficial website : www.xython.co.kr  (Korean base)  <br>

### Components / 구성은 

| 모듈이름| 개요                            | 설명                         |
|-------------|-------------------------------|--------------------------------------|
| anydb       | for Database                  | sqlite와 pandas 를 좀더 쉽게 사용할수있도록 만든것   |
| ganada      | for Word                      | 워드를 다루기위해 만든 것                       |
| jfinder     | for Regex                     | 정규표현식을 좀더 편하게 사용하도록 만든 것             |
| mailmail    | for outlook                   | outlook을 다루는것                        |
| pcell       | for Excel                     | 엑셀을 다루는 것 |
| pcell_event | for Excel Event               | 엑셀의 이벤트를 다루는것         |               
| pyclick     | for Keyboard & Mouse control | 키보드와 마우스를 다루는 모듈                     |
| pynal       | for Date & Time               | 시간과 날짜를 다루는것                         |
| scolor      | for Color                     | 색의 RGB값을 편하게 사용가능하도록 만든 것            |
| youtil      | utilities                     | 이러저런 문장이나 시간등을 변환하는데 도움이되는 것         |
| basic_data  | general enum                  | xython패키지에서 사용되는 전반적인 공유 자료들을 저장하는 곳 |
| etc         | 기타                            | 나머지들은 추가적인 내용들을 위하여 사용하는 것임          |

### Brief / 개괄적인 설명
this is target for easy RPA system of office work<br>
It composed of several python files, and basic concept is function style total over the 1500 functions in this package<br>
please see how to use for this package in xython.co.kr<br>
now under making GUI toolkit for easy & no installing for python for this package<br>    

이모듈은 업무용으로 많이 사용하는 엑셀 , 색, 정규표현식, 등에 대하여 Python과 win32com을 기본으로 사용하여 각기 새롭게 모듈을 만들어서 좀더 쉽고 편하게 사용하고 만들자는 것입니다
자동화는 각자의 사용에 대한<br>
만든 이유는 우리가 업무등을 하는 입장에서, 손으로 작업하기에는 양이 많고, 그렇다고
계속 반복적으로 일어나는 일은 아니며, VBA등을 만들어서 사용하기에는 어렵고 힘든 부분에 대해서<br>
파이썬이라는 훌룡한 언어를 위용하여, 좀더 쉽고 간결하게 몇가지 기능만 배워도 20줄안으로 자신만의 코드를
만들어 사용할수있는 기준을 만들기 위한 것입니다<br>
또한 보통 많이 사용하는 코드들은 첨부된 sample코드를 보시거나 저의 사이트에 와서 비슷한것을 다운 받은후
변경해서 사용하시기를 추천 드립니다<br>
좀더 편한 업무의 일을 하기위한 것입니다<br>

### Version History / 버전 변화
    - 1.15.0 : word를 위한 ganada모듈을 전반적으로 많이 Update함
    - 1.16.0 : applied docstring style for all files
    - 1.17.0 : connected with github document system
    - 2023-03-02 : 전반적으로 이름을 수정함

## xython패키지의 전반적인 사용법 및 용어 설명
### 함수들의 이름을 만드는 기준

나름대로 편하고 쉽게 이름을 만들려고 하였습니다. <br>
기본적인 틀을 만들어 놓으니, 분명억지로 지어진 이름또한 있음을 시인합니다. 
나름대로 생각하고 고심한끝에 만들어진 이름이오니 맘에 들지 않는 부분이 있이더라도 양해를 부탁드립니다<br>
물론, 지금의 이름이 최종이라고는 생각하지 않고 있습니다. 좋은 이름이라는것은 어떤 메소드가 들어가 있는지 잘 몰라도 거의 사용하는데 사람의 생각에서 쉽게 사용을 할수 있도록 만드는 것이라고 생각을 합니다<br>
아마 한 4~5번정오는 크게 이름을 변경한 것 같습니다. 만들어놓고 조금지나면 저스스로가 도데체 이것의 이름은 왜 이렇게 만들어놓은거야???라는 질문을 하는경우가 가끔있습니다. 이리바꾸고 저리바꾸어도 맘에 안드는구석이 아직 많습니다<br>
한사람의 이름이 인생에서 차지하는부분이 많듯이 제가만든것또한 그러하지만, 만약 맘에 안드시는 것이 있으시면 본인스스로가 바꾼어서 사용하셔도 됩니다
단, 기존의것은 그대로 두시고 아래부분에 새로운 메소드를 추가하셔서 위의것을 그대로 사용하시면 될것입니다
그래서 다음과 같은 원리를 이용해서 만들었으나, 조금은 틀린부분도 있지만…

	1. 이름은 기본적으로 3부분으로 만들었으며 각부분은 언더바(_)로 연결했습니다
	2. 읽을때는 read, 쓸때는 write, 삭제는 delete, 추가는insert등을 사용하였습니다
	3. 두번째의 이름의 규칙은
		관련된 부분에 따라 다른것을 사용하며 다음과 같은 것이 사용이 됩니다
		거진 영역을 나타내는 부분으로 사용하였습니다
		range, workbook, cell, line, column
	4. 세번째 부분이 어떤 일을 할것인지를 알아보는 것입니다
	5. 일반사항은 다음과 같습니다

-	모든함수에는 sheet가 명시되어야 합니다
-	값을 읽는것은 read로 시작하며
-	값을 쓰는 것은 write로 시작합니다
-	선을 긋는등의 그림은 dwg로 시작합니다
-	하나의 자료가 아닌, 자료의 묶음은 Range를 사용한다
-	두개의 문구사이에는 '_' 로 연결을 하였다 예) read_cell
-	메소드는 모두 소문자를 사용함

예를 들어, 어떤셀에 값을 입력하는 것은 write_value_in_cell라는 이름으로 구성하였습니다
그리고 부가적으로 함수의 변수로 사용되는부분은 큰 것->작은것으로 만들었으며, 영역을 표시하는 부분은 모두 리스트를 기준으로 하나로 만들었습니다.

그저, 그렇다는것을 이해바라며, 실질적으로 코드를 보시면 더 쉽게 이해가 가실것으로 생각됩니다.
보지않고 찾지않아도 함수의 이름을 생각해낼수있도록 만든다고 나름대로 정의한 것입니다.

### 전체적인 패키지안의 단어들에 대한 설명

| 맨앞의 동사  | 두번째      | 마지막          | 설명                                        |
|:-------:|----------|--------------|-------------------------------------------|
|   add   |          |              | 기존에 있는것의 일반적인 끝에 넣는 것 <-> insert          |                        
|   New   |          |              | 새로운것을 만드는 개념                              |                                                
| Insert  |          |              | 내가 원하는위치에 넣는 것                            |                                            
|  make   |          |              | 만들기                                       |                                                 
| append  |          |              | 맨끝에 추가할 때                                 |                        
| change  |          |              | 입력값을 바꾸는 목적, 전체를 변경                       |
| Replace |          |              | 바꾸기, 전체또는 일부를 변경 전체내용중에서 일부를 변경           |                                           
|  check  |          |              | 내부적인 자료들을 확인할때 사용                         |                                                          
| control |          |              | 어느 영역안에서 조정을 할 때                          |                                            
|  data   |          |              | 어떤 종류의 자료형태로 결과값을 돌려줄 때, 보통 내부적인 자료를 돌려줄때 |                                       
|  pick   |          |              | 여러개중에서 하나를 갖고올 때                          |                                         
|   Get   |          |              | read를 제외한 모든 자료를 갖고올 때                    |           
|  Read   |          |              | 눈에보이는 현상의 자료를 갖고올 때                       |                
|  input  |          |              | 내부적으로 어떤 값을 넣을 때                          |                                             
|  Write  |          |              | 눈에 보이는 것을 변경할때                            |                             
|   set   |          |              | 입력값이 특별한것없이 자료를 설정하는 것, 설정값을 변경할 때        |                      
| delete  |          |              | 삭제하기, 어느 영역안에서 조정을 할 때                    |                               
| remove  |          |              | 값이외의 객체등의것을 제거하는것 사용 X                    |                               
|  split  |          |              | 분리하기                                      |                                 
|  Move   |          |              | 이동하기                                      |                                                  
|  fill   |          |              | 넣기                                        |                                               
|  Find   |          |              | 찾기, 우연히 발견된다는 의미로, 이것은 search로 바꾼다 사용 X   |                                                 
| search  |          |              | 찾기, 조금더 상세하게 찾을때, 찾고자하는것을 찾는것             |                                              
| select  |          |              | 어떤 영역을 선택할 때                              |                                             
|  draw   |          |              | 선을 그을 때 사용, 라인에 대한 색과 형태등을 설정할때                              |                                             
|  paint  |          |              | 어떤 영역에, 색을 칠하는것                                |                                             
|   is    |          |              | 어떤것이 맞고 틀린지를 확인하는것                        | 
|         | current  |              | 어떤 객체 든지 현재에 활성화된 것을 뜻함                   |                                       
|         | obj      |              | 객체를 뜻함                                    |                                             
|         | color    |              | 색넣기                                       |                                                         
|         | lisr_1d  |              | 1차원 리스트가 입력값일 때                           |                                              
|         | list_2d  |              | 2차원 리스트가 입력값일 때                           |                                             
|         | pwh      |              | 넓이, 높이의 길이를 픽셀단위로 나타낸것 (단위 : pixel)       |                                  
|         | dtx      |              | 두 셀간의 차이, d : differancial                |                                                  
|         | dx       |              | 두지점간의 차이                                  |                                                  
|         | cpx      |              | 셀의 좌표번호, c : cell, p : pixel              |                                               
|         | curr_x   |              | 키보드등으로 움직이는 현재의 셀                         |                                          
|         | mx, mpx  |              | 마우스의 좌표                                   |                                                  
|         | space_px |              | 기준이되는 것,  (단위 : pixel)                    |                                
|         | win_x    |              | 윈도우의 x                                    |                        
|         | px       |              | 그림을 그리고 싶은 좌표, 커서의 픽셀 좌표 (단위 : pixel)     |                                   
|         | sel_x    |              | 셀렉션된 영역                                   |                                                 
|         | tbl_x    |              | 테이블의 x                                    |                                 
|         | tx       |              | cell의 번호에 대한것, table에서 몇번째 셀이라는 쯧         |                         
|         | x, y     |              | cell의 기본좌표, X: 가로줄번호, Y: 세로줄 번호           |                             
|         | xx       |              | 가로줄의 영역, [3,6]                            |                                
|         | xy       |              | 하나의 셀에대한 좌표, [3,6]                        |                                     
|         | xyxy     |              | 셀의 영역에 대한 좌표, [3,6, 7,8]                  |                                    
|         | yy       |              | 세로줄의 영역, [3,6]                            |                                  
|         |          | index        | 몇번째의 순서대로 어떤 것을 하는 것                      |                                    
|         |          | num, no      | 1부터시작되는 번호                                |                                    
|         |          | By_limit     | 번호가 들어가 그때까지 적용                           |
|         |          | By_step      | 번호가 들어가 그 간격으로 실행될 때                      |                                   
|         |          | nstep        | n번째마다 실행하는것                               |                                   
|         |          | nth          | n번째 자료 (index를 기준으로 하는것)                  |                                   
|         |          | dic          | 자료의 형태가 dic형태로 줄때는 맨뒤에 dic을 붙임            |                              
|         |          | obj          | 객체를 뜻함, object            |                              
|         |          | input_value  | 기본적인 입력값                                  
|         |          | input_list1d | 1차원 리스트가 입력값일 때                           
|         |          | input_list2d | 2차원 리스트가 입력값일 때                           
|         |          | input_dic    | 사전형식일 때                                   


### 용어 설명
|          약어          | 기준                         | 설명                                           |
|:--------------------:|----------------------------|----------------------------------------------|
|       cx, cy         | 셀의 좌표번호, x,y대신 시용          | C : Cell의 약어                                 |
|         x, y         | cell의 기본좌표                 | X: 가로줄번호, Y: 세로줄 번호                          |    
|         xyxy         | 셀의 영역에 대한 좌표               | [x,y,x2,y2]                                  |
|          xy          | 하나의 셀에대한 좌표                | [x,y]                                        |
|          xx          | 가로줄의 영역                    | [x, x2]                                      |
|          yy          | 세로줄의 영역                    | [y, y2]                                      |
|          px          | 커서의 픽셀 좌표                  | P : pixel의 약어                                | 
|         pwh          | 넓이, 높이의 길이를 픽셀단위로 나타낸것     | P : pixel의 약어                                |
|        dx, dy        | 포인트간의 길이, 두지점간의 차이         | D : Difference 또는 Delta                      |
|         dtx          | 두 셀간의 차이                   |                                              |
|        mx, my        | 마우스의 위치                    |  M : mouse의 약어                                            |
|        tx, ty        | 테이블의 셀좌표 (table_x)         | T : table의 약어 , txy로 사용도가능                   |
|   tx, ty, tx2, ty2   | 그리드안의 영역 (table_x)         | T : table의 약어 , txyxy로 사용도가능                 |
|        win_x         | 윈도우의 x                     |                                              |
|        sel_x         | 셀렉션된 영역                    |                                              |
|        curr_x        | 키보드등으로 움직이는 현재의 셀          |                                              |
|     x, y, x2, y2     | 컴퓨터안에서의 영역                 |                                              |
|        gx, gy        | graphic기준의 x, y 좌표         | (graphic_x) pixel의 px와 혼돈이 될수있어서 px를 사용하지 않음 |
| stx, sty, stx2, sty2 | 현재 선택된 table의 셀번호 (select) | 워드에서 여러테이블 자료를 다룰 때                          |

             
### 용어의 뜻
|   용어   | 설명                                              |
|:------:|-------------------------------------------------|
| x_char | 첫문자에서부터 번호째                                     |
| x_word | 처음에서부터의 단어순번째                                   |
| x_para | 처음에서부터의 문단의 순번째                                 |
| x_line | 처음에서부터의 줄의 순번째                                  |
| x_sel  | 선택된 첫                                           |
|  xy_s  | selection의 처음과 끝위치                              |
| x_len  | x는 시작위치, l은 길이                                  |
| x_sel  | selection의 시작점                                  |
| y_sel  | selection의 끝점                                   |
|  nth   | 맨처음부터 몇번째의 의미|
