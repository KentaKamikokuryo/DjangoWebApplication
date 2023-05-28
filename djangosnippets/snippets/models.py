from django.db import models
from django.conf import settings


# Create your models here.
class Snippet(models.Model):

    title = models.CharField("Title", max_length=128)                  # スニペットのタイトルを格納するフィールド．models.CharFieldで定義し，最大128文字とした．
    code = models.TextField("Code", blank=True)                        # スニペットを誰が投稿したのかわかるように，このフィールドではユーザーモデルの主キーへの参照を持っている．
    description = models.TextField("Description", blank=True)          # ソースコードを格納するフィールド
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   verbose_name="Contributor",
                                   on_delete=models.CASCADE)
    created_at = models.DateTimeField("Posted day", auto_now_add=True)
    updated_at = models.DateTimeField("Updated day", auto_now=True)

    def __str__(self):
        return self.title

