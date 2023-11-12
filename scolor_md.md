### scolor
이것은 모든 외부로 들어오고 나가는 것은 전부 RGB형태로 이루어지도록 만든다

    - 색을 변경하고 관리하는 모듈이며
    - 색의 변화를 잘 사용이 가능하도록 하기위한 것이다
    - 기본 입력 예 : "빨강", "빨강55", "red55", "0155"
    - 기본색 ==> 12색 + (하양, 검정, 회색),
    - 큰변화 ==> 1~9단계, 작은변화 ==> 1~9단계
    - 기본함수 : get_color_rgb("red55"), get_rgb_3input(색, 큰변화, 작은변화)
    - 모든 색의 표현이나 결과는 rgb로 돌려준다

``` python
# -*- coding: utf-8 -*-
import scolor

color = scolor.scolor()
#기본 빨간색을 2단계 밝은 rgb값을 갖고온다 
color.change_scolor_to_rgb("red++")
```
