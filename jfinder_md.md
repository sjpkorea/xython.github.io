### Jfinder
#### 개요
이름을 **Jfinder**라고 지었으며, 아래와 같은 특성을 가지고 있다

1. 건수는 ~를 사용하여 4~5라는 식으로 표현을 하였고
2. 한글, 영어와 같은 것은 대괄호를 사용하여 적용하였다 [한글]
3. 처음과 끝은 [처음], [끝]처럼 나타냈다
4. 그리고 이것은 누가 보아도 아~~ 무엇을 찾을려고 했는지를 알수있도록 하기위한것이며
5. 찾기기능중에 전부 찾아서 보기쉽도록 돌려주는 것과 같은 몇가지 메소드들을 만들어 넣었읍니다
제일 중요한 코드를 만드는 기능은 아래와 같읍니다
대략적으로 위의것을 읽은후에 보시면 이해가 되실부분이 많읍니다

* 아래의 코드들은 정규표현식을 사용하면서, 내가 만든 표현식조차도 다시 읽기가 어려워서, 나름 다른 형태로 만들어 본것인데. 생각보다 가독성이 좋아서 같이 공유해보는것이다
또한 만든김에 결과로 돌려주는것도 하나만 받으면 전부 가능하도록 만들어 보았다
위에서 언급한 이메일 형식이 맞느지를 보는 것은 상당히 반복적이기 때문에 크게 혼돈은 없다
하지만, 실제 코드를 사용하다 보면, 외계어를 해석하는 상태까지 와야할 경우가 있다


    ([a-zA-Z0-9_.+-]+)@[a-zA-Z0-9_.+-]+\.[a-zA-Z0-9_.+-]+

* 이정도만해도 간단한 축에 속한다. 맨처음 만들때는 그나마 이해를 하지만, 다른사람이 만든 것을 이해하는데 상당한 시간이 걸린다는 것이고, 또한 일반적인 사용자들이 이것을 공부하고 이해하는데 어려움이 잇을 것 같으면서 동시에, 정규표현식의 강력함을 사용할수 있도록 생각해 보는 것이다
그래서 좀더 간단하게 사용법을 만들고,


    [영어&숫자.+-:1~]@[영어&숫자.+-:1~]\.[영어&숫자.+-:1~]
이렇게 바꾸면 좀더 읽기가 쉬워진다

**jfinder**에는 자주사용하는 언어를 등록할수도 있읍니다. 예를 들어 일본어나 한자를 등록한것처럼 하면 사용이 가능하다.
간단하게 다시 사용하는 방법을 알려주면, 너무 줄여놓은 정규표현식을 좀더 늘이는 것이라고 생각하면 됩니다. 여기에서 느낀 부분은 전문가가 사용하기에는 좋지만, 비전문가가 사용하기 쉽게, 예전에는 단어1개가 아주 중요한 속도까지 영향을 주지만, 지금은너무 줄이지 않아도 된다는 것이다. 기계에 가까운 언어에서 좀더 사용자에 가까운 언어로 만들어도 된다는 것이지요
파이선이 사용하기에 좀더 편한방법이 되는 것이지요

    - 대괄호로 묶는다
    - 반복갯수는 대괄호안에 사용하며 ~로 나타낸다
    - 맨처음 맨마지막등의 용어는 [처음], [끝]등의 이유로 나타낸다 
    - 특수문자(re모듈내에 의미가있는 문자)는 \를 붙여서 사용한다
    - 어떤문자의 앞과뒤에있을때는 (앞에있음:abc)이라고 사용하면 abc가 앞에있는 문자열을 찾는것이다
#### 메타문자의 사용법
메타문자들 : . ^ $ * + ? { } [ ] \ | ( )
메타문자를 사용하기 위해서는 앞에 \를 하나더 붙이면, 메타기능을 없애는 것이다

#### 단어자체로 찾기를 하고 싶을때
    xython이라는 단어자체로 찾기를 하고싶다면
    (xython|자이썬)[1~1]처럼 사용하면 된다
    |는 or를 나타내는 메타문자이다

#### 메타문자와 다른 용어들을 사용하고 싶을때
[한글\.:1~3]처럼 사용하면 된다

    #-*- coding: utf-8 -*-
    import jfinder
    ezre = jfinder.jfinder()
    
    jf_sql = "[한글\.:1~2]"
    print("[한글\.:1~2]  ==> ", ezre.change_jf_sql_to_re_sql(jf_sql))
    jf_sql = "[\.한글:1~2]"
    print("[\.한글:1~2]  ==> ", ezre.change_jf_sql_to_re_sql(jf_sql))
    jf_sql = "[\.&한글:1~2]"
    print("[\.&한글:1~2]  ==> ", ezre.change_jf_sql_to_re_sql(jf_sql))

결과는 

    [한글\.:1~2]  ==>  [ㄱ-ㅎ|ㅏ-ㅣ|가-힣\.]{1,2}
    [\.한글:1~2]  ==>  [\.ㄱ-ㅎ|ㅏ-ㅣ|가-힣]{1,2}
    [\.&한글:1~2]  ==>  [\.ㄱ-ㅎ|ㅏ-ㅣ|가-힣]{1,2}

#### 결과의 형태

    결과가 여러개 일때는 2차원의 결과가 나타난다
    그룹은 괄호를 친것이 나타나는 것이다
    [[찾은글자, 찾은글자의 처음 위치 번호, 끝위치 번호, [그룹1, 그룹2], .........] 

#### jfinder의 사용법

``` python
# -*- coding: utf-8 -*-
import jfinder

myre = jfinder.jfinder()
input_text = "가나다라1234abc오육칠"
myre.search_all_by_resql("[숫자:1~2][영어:1~2]", input_text)


input_text = """님은 갔습니다. 아아, 사랑하는 나의 님은 갔습니다.
푸른 산빛을 깨치고 단풍나무 숲을 향하여 난 작은 길을 걸어서, 차마 떨치고 갔습니다.
황금의 꽃같이 굳고 빛나던 옛 맹세는 차디찬 티끌이 되어서 한숨의 미풍에 날아갔습니다.
날카로운 첫 키스의 추억은 나의 운명의 지침을 돌려놓고, 뒷걸음쳐서 사라졌습니다.
나는 향기로운 님의 말소리에 귀먹고, 꽃다운 님의 얼굴에 눈멀었습니다."""

result = ezre.match("(님)[1~1](은|이|의)[0~1]", input_text)
print(result)





```

