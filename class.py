import getpass


class Member:
    def __init__(self, name, username, password):
        print(f'회원명 : {name}')
        print(f'아이디 : {username}')
        print(f'비밀번호 : {password}')

        self.name = name
        self.username = username
        self.password = password


class Post:
    def __init__(pself, title, content, author):
        print(f'제목 : {title}')
        print(f'내용 : {content}')
        print(f'작성자 : {author}')

        pself.title = title
        pself.content = content
        pself.author = author


student1 = Member('둘리', 'dul2', '123')
student2 = Member('도우너', 'dounut', '456')
student3 = Member('또치', 'chichi', '789')
student = (student1, student2, student3)

members = []
for a in student:
    members.append(a)

print(members)

member1 = Post(input('제목을 입력하세요 : '),
               input('내용을 입력하세요 : '),
               input('작성자명을 입력하세요 : '))
