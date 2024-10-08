# Q1. 클래스와 인스턴스에 대해 설명해주세요.

클래스(class)와 객체(object)는 설계도와 그 설계도의 대상이라는 관계입니다.
그렇다면 인스턴스는 클래스라는 설계도를 사용하여 객체를 생성하는 것입니다.  

영어로 들으면 이들의 관계가 조금 쉬워지는데요, "instantiate a class object"라고 합니다. 한국어로는 "클래스 객체를 생성한다"라는 의미로 볼 수 있겠죠.

클래스는 객체지향프로그래밍의 핵심입니다. 그런데 왜 핵심일까요? 사실 프로그래밍의 장점중 하나는 반복적인 작업을 대신 해준다는 것인데요, 클래스는 효율을 매우 높여줍니다.  

예를 들어, 건물을 지어야하는데 매번:  
`building_201_floor = 20`  
`building_201_location = Seoul`  
`building_201_year = 2001`  
`building_202_floor = 24`  
`building_202_location = Seoul`  
`building_202_year = 2003`  

층수, 위치, 건설연도를 변수에 저장하면 보기도 불편하고 비효율적이죠?

그래서 클래스는 이것을 하나의 묶음으로,  
``` Python
    class Building:
        def __init__(self, floor, location, year):
            self.floor = floor
            self.location = location
            self.year = year
```
간단하게는 코드를 이렇게만 적어도,
``` Python
    building_201 = Building(20, 'Seoul', '2001')
    building_202 = Building(24, 'Seoul', '2003')
```
201동, 202동 건물의 객체를 인스턴스화 할 수 있습니다.

이 말고도 클래스의 함수인 메소드도 만들 수 있고 이 외에도 활용성은 많습니다.

결론적으로, 예제를 사용해서 마무리를 짓는다면, 클래스는 빌딩이라는 객체를 생성하기 위해 필요한 내용을 포함한 설계도이며, 인스턴스는 공사하는 단계 (프로그램에서 클래스 객체를 생성하는 단계)이며, 객체는 생성된 클래스의 대상인 건물이 되겠습니다.


# Q2. 정적 메소드는 무엇이고, 어떻게 호출하나요?
메소드(method)는 클래스 안에서 속성과 마찬가지로 생성할 수 있는 함수입니다. 그렇다면 정적 메소드는 어떤 메소드일까요? 

일단 일반 메소드는 클래스 인스턴스의 속성을 사용하여 특정 액션을 취할 수 있다고 보면 편합니다. 예를 들어, 한 축구 선수의 클래스가 있고 그 선수의 속성이: 나이, 키, 몸무게, 국적이 있다면, 축구 선수 클래스의 메소드는: 패스, 슛, 헤딩 등이 있겠죠.  

정적 메소드는 일반 메소드 또는 클래스 메소드와 다르게, 클래스 인스턴스의 속성과 다른 메소드의 영향을 안받는다는 것입니다. 예를 들어, 일반 메소드는 클래스를 인스턴스화 해서 그 선수가 패스를 하든 슛을 하든 시킬 수 있습니다. 하지만 정적 메소드는 굳이 인스턴스를 할 필요 없이 바로 호출을 할 수 있습니다.  

``` Python
Player.today_match()
```
그렇다면 정적 메소드는 왜 사용할까요? 클래스의 영향을 직접적으로 받지는 않지만 관련은 있을 때 편의성으로 만들면 좋습니다.

예를 들어, 저희가 축구 선수 클래스를 사용한다면 축구와 관련된 프로그램을 만들고 있다고 볼 수 있겠죠? 그런데 저희가 이 클래스를 모듈화해서 재사용하고 싶다면 어떤 축구 프로그램에서 이 모듈을 사용하더라도 쉽게 `Player.today_match()` 라는 코드만 적어도 오늘 어느 팀사이에 매치가 있는지 확인할 수 있으면 편하겠죠? 선수의 속성과는 상관 없지만 클래스의 추상적인 내용과는 관련이 있으니까요. 

결론적으로 정적 메소드는 클래스 하나의 객체와는 상관 또는 영향이 없지만 추상적인 개념과 관련되었을 때 편의성을 위해 사용한다고 생각하면 이해하기 쉬울 것 같습니다.