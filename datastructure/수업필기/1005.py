연결자료구조
리스트가 시작되는 점을 항상 알아야하고, 이것을 head라고 지정을 해놓았다.
숫자를 입력받으면 노드가 생성되고 노드가 삽입되어야한다.
노드를 만들었으면 우리가 실제로 만들려고 하는것은 단순 연결 리스트를 만드는것.
이 리스트가 클래스가 되어야한다.
이 리스트가 하는 것:function 속성 atrribution

클래스 Node를 만들고
클래스 단순연결리스트를 만듦.
SLL의 한 원소가 Node클래스
SLL에서 Node를 선언한다.
Node는 디자인 해놨으니 insert만 만들면 된다.

SLL:head를 지정해놔야한다. 생성자에서, head에는 값이 없고, 값은 None
Node 클래스를 만들때 타입을 안만들어서 SLL에서도 관계 X
SLLprint도 있어야한다

insert delete search 원소의 개수 정렬 값바꾸기 몇번째원소지우기
몇번째원소인지
class의 함수로 디자인하면 쉽게 할 수 있다.

search:어떤 것인지 찾은 다음 node자체를 반환시켜줌
현재노드 currentnode를 만들어서 head값은 항상 유지

첫번째 원소추가: head 뒤에 넣기
두번째 원소추가: 마지막node뒤에 넣기

쉽게하는 방법: classSLL tail node추가, tail뒤에 붙이기 head 뒤에 있는지 없는지만
판단하고
tail안쓴다면 search 함수 만들기 어떤 값이든..
insert는 head가 새로운 노드를 가리키고 head - a이면 b를 추가하면
head가 b를 가리킥 b는 a를 가리킨다.

총 3가지 방법,,

그런데 만약, 정렬이 되있는 경우는 어떡할까.
3 - 6 - 7
5를 집어넣으면 3-6-7-5
그렇지만 이렇게하면 정렬이 안됨. 다시 정렬시켜야하니까 귀찮, 집어넣을때 정렬하자
위치를 찾은 다음 3이 5를 가리키고 5가 6을 가리키게 들어가자.

방법을 원래 하나만 배웠지만 다 가르켜줄거야 ㅋㅋㅋ;
세가지 방법을 다 사용할 줄 알아야합니다.

class node 선언,
node.py로 만들고
SLL.py를 따로 만들고 import node

insertion같은 거를 정의해주면 linked list를 계속 사용가능.
overide?polymorphism?  capsulation?

뒤에 next는 알수있지만 그 앞에 어떤 값이 올지는 모른다.
따라서 previous와 current를 만들어야한다.

linkedlist를 디자인,,의 __init__

생성자를 만들, tail쓸거면 init에 head, tail
반환하는 거 할려면 init에 tail없어도 됨

insert : new node를 만들면 head.next에 newnode를 붙이고 newnode.next=~
head의 next가 new node로 가고~

insert : Head가 있으면 아무것도 없는 상태, next가 none이기 때문
1.newnode를 생성
2.만약 head.next=none이면 head.next가 newnode
3.none이 아니면 head가 가리키는 원소가 존재한다. 즉 newnode가 들어갈 자리를
찾는다 search를 이용(맨 마지막 노드를 찾아서, next가 none인 경우)
위치를 찾아서 findnode 값 찾고 findnode.next=newnode
search: print해서 마지막 부분을 찾아서 그 노드를 source,
findnode=source


insert : tail 붙이기 무조건 tail 뒤에 붙일거.
tail뒤에 붙이기는 newnode 생성하고 tail.next=newnode
head

단순연결리스트만들기
중간에 추가시키는건 아직 안함
search해서 위치를 찾으면 그 위치의 previous와 current를 반환받아서 쉬움

삭제1. 맨 마지막거만 삭제
h-1-2 삭제 하려면 search해서 맨마지막 노드를 찾거나 tail을 없앰.
또는 head가 가리키는거 삭제는 hea.next를 그 뒤로
1.next=None으로 한다. node를 만들때 생성자말고 소멸자를 만들면 데이터 안먹는다

tail을 쓰지 않는 경우 제일 마지막의 바로 앞녀석을 반환받음. 근데 search하면
제일 마지막을 찾아버리니까 previous의 next를 noen으로 만들어버림.
맨 끝에있는

head뒤에걸 삭제해야할때 a뭐라는건지모르겠다

세번째 삭제: 중간에 걸 삭제할때 , 그 녀석의 next를 앞의 녀석으로가고 

current의 위치를 찾는것이 search함수

삽입 삭제를 구현하기
정렬되어있는 곳에서 100 200 300 400 500
100 200 400 500 4개연결리스트
node를 몇개만들래? (겹치지 않게)
1~100까지 5개 숫자 생성
정렬된 상태로 값이 들어간 연결리스트만들기
data 넣을거 있니? 1~100
자동적으로 정렬되어서 연결리스트에 들어가고 프린트
뺄래? 현재 프린트
고르면 빼서 프린트

다음번엔 이중연결리스트할것
2주후에 이 숙제 할것 단순연결리스트로






















