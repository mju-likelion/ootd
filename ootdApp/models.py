from django.db import models

class Member(models.Model):
    # 아이디
    user_id = models.AutoField(primary_key=True)
    # 이름
    name = models.CharField(max_length=20)
    # 비밀번호
    password = models.CharField(max_length=20)
    # 이메일
    email = models.EmailField(unique=True)
    # 사용자 타입
    member_type = models.CharField(max_length=30)
    # 성별
    gender = models.BooleanField()
    # 생년월일
    birthdate = models.DateField()
    # 닉네임
    nickname = models.CharField(max_length=30, unique=True)


class Like(models.Model):
    # 누가 좋아요를 눌렀는지
    like_from = models.ForeignKey(
        'Member', on_delete=models.CASCADE, related_name='like_from')
    # 누구한테 좋아요를 눌렀는지
    like_to = models.ForeignKey(
        'Member', on_delete=models.CASCADE, related_name='like_to')


class Feedback(models.Model):
    # 아이디
    f_id = models.AutoField(primary_key=True)
    # 글쓴이 (유저가 삭제되면 Feedback도 삭제되야 하므로 on_delete는 CASCADE)
    f_writer = models.ForeignKey('Member', on_delete=models.CASCADE)
    # 이미지
    f_image = models.ImageField()
    # 카테고리

    #class Category(models.TextChoices):
    #    ALL = 'A'
    #    OUTER = 'O'
    #    TOP = 'T'
    #    BOTTOM = 'B'
    #    SHOES = 'S'
    #    ACC = 'AC'
    #    SIMILAR = 'SI'
    #f_category = models.CharField(
    #    max_length=2, choices=Category.choices, default=Category.ALL)


class Comment(models.Model):
    # 아이디
    c_id = models.AutoField(primary_key=True)
    # 글쓴이
    c_writer = models.ForeignKey('Member', on_delete=models.CASCADE)
    # 어느 글인지
    c_feedback = models.ForeignKey('Feedback', on_delete=models.CASCADE)
    # 내용
    c_content = models.CharField(max_length=256)


class Image(models.Model):
    objects = models.Manager()
    title = models.CharField(max_length=30)
    description = models.TextField()
    date = models.DateTimeField(auto_now=True)
    src = models.ImageField(blank=True)