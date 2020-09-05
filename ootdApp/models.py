from django.db import models

# Create your models here.
class Member_info(models.Model) :
    # 좋아요 수
    like = models.IntegerField(default=0)
    # 팔로워 수
    follower = models.IntegerField(default=0)

    class Meta:
        db_table = 'member_info'
        unique_together = (("like", "follower"),)

    def __str__(self):
        return self.like

class Member(models.Model) :
    # 아이디
    user_id = models.TextField(primary_key=True, null=False)
    # 이름
    name = models.CharField(max_length=20, null=False)
    # 비밀번호
    password = models.CharField(max_length=20, null=False)
    # 이메일
    email = models.EmailField(max_length=200, unique=True, null=False)
    # 사용자 타입
    m_type = models.CharField(max_length=30, null=False)
    # 성별
    gender = models.CharField(max_length=10, null=False)
    # 생년월일
    birthdate = models.DateField(null=False)
    # 닉네임
    nickname = models.CharField(max_length=30, null=False, unique=True)
    # 좋아요 수
    like = models.ForeignKey(Member_info, on_delete=models.CASCADE, null=True, related_name="Member_like")
    # 팔로워 수
    follower = models.ForeignKey(Member_info, on_delete=models.CASCADE, null=True, related_name="Member_follower")

    class Meta:
        db_table = 'member'

    def __str__(self):
        return self.user_id

class Feedback(models.Model) :
    # 아이디
    f_id = models.ForeignKey(Member, on_delete=models.CASCADE, primary_key=True, null=False)

    # 내용
    f_content = models.TextField(null=False)

    # 이미지
    f_image = models.ImageField(null=False)

    # 카테고리
    Category = (
        ('A','All'),
        ('O','Outer'),
        ('T','Top'),
        ('B','Bottom'),
        ('S','Shoes'),
        ('Ac','Acc'),
        ('S','Similar'),
    )
    f_category = models.CharField(max_length=2, choices=Category, null=False)

    # 댓글
    f_comment = models.TextField(null=True)

    class Meta:
        db_table = 'feedback'

    def __str__(self):
        return self.f_id

class Market(models.Model) :
    # 아이디
    m_id = models.ForeignKey(Member, on_delete=models.CASCADE, primary_key=True, null=False)
    
    # 게시물 내용
    f_content = models.TextField(null=False)

    # 이미지
    m_image = models.ImageField(null=False)

    # 카테고리
    Category = (
        ('A','All'),
        ('O','Outer'),
        ('T','Top'),
        ('B','Bottom'),
        ('S','Shoes'),
        ('Ac','Acc'),
        ('S','Similar'),
    )
    m_category = models.CharField(max_length=2, choices=Category, null=False)

    # 댓글
    m_comment = models.TextField(null=True)

    # 가격
    price = models.IntegerField(null=False)

    class Meta:
        db_table = 'market'

    def __str__(self):
        return self.m_id

# class Chatting(models.Model) :
#     # 구매자 아이디
#     buyer_id = models.ForeignKey(Member, on_delete=models.CASCADE, primary_key=True, null=False)

#     # 판매자 아이디
#     seller_id = models.ForeignKey(Member, on_delete=models.CASCADE, primary_key=True, null=False)

#     # 채팅 내용
#     c_content = models.TextField(null=False)

#     def __str__(self):
#         return self.buyer_id










