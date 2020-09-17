저번까지 선형리스트
리스트 길이가 제한되어있다고 가정,
불편

링크드 리스트
쓸데없이 사용되는 메모리 공간을 줄인다.

메모리를 선형적으로만 집어넣게 되면
중간에 삭제했을때 문제..
조각 모음:속도를 빠르게 하려고
HDD하드디스크 메모리에서 이짓을 함 한번에 모아서 쭉
오버헤드는 실제로 컴퓨터에 별 영향X

물리 주소를 유지하기위해...등등

주소:RAM의 주소
64bit컴퓨터: 메모리의 주소 공간.2^64개
CPU operation의 과정
HDD에서 저장된 코드들에서 램에서 CPU, 계산 후
다시 메모리 주소로 쏴서 바꿈.

논리적인 순서와 물리적 순서가 일치하지 않음.

연결리스트의 노드

ㅣ1= [] 이면 데이터밖에 없다.

연결리스트는 [1] -> [2] 일때 ->를 의미하는 링크가 필요.

파이썬 형변환 필요x
C는? header? tile def?
C에서는 pointer를 쓰지만(주소)
python은 변수자체가 주소
a=1이면 a가 1이라는 걸 가리키는것
a=2입력하면 a->2로 가리킴.

함수는 메인프로그램이 아님.
def func~ 따로 영역이 존재함.
이름을 불렸을때 메모리에,,

head(처음 시작)는 항상존재 -> 다음주소 가리킴
가리킬 주소가 없다면 None

data&link

class!
data:명사
method:행위

ADT:abstract data program

Node.link, Node.data

데이터형식은 class

head.next=node1

insertion, deletion
linked list가 하는것.가 같고 잇다.

linked list
    head
    insert
    delete

1.head 뒤에 2
2.뒤에
3.사이에

linkedlistprint(아무거나)

head를 처음에 받아서
head.data==None이면 head
ishead 함수

ifhead.next==None이면 print해줌
elseprint(head.next.data)
    
head=head.next
print(head.data)
a=head.next
while문써서
a.data=None이면 종료

헤드일때 아닐때

next가 none일때까지 head를 print함












































