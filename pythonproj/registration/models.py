from django.db import models

class UserDetails(models.Model):
    name=models.CharField(max_length=50,unique=True)
    emailID=models.EmailField()
    password=models.CharField(max_length=15)

class categories(models.Model):
    categoryname=models.CharField(max_length=50,primary_key=True)
    course_count=models.IntegerField()
    img_file=models.ImageField(upload_to='images/cat/',null=True,verbose_name="")
    def __str__(self):
        return self.categoryname

class courses(models.Model):
    cname=models.CharField(max_length=100,primary_key=True)
    categoryname=models.ForeignKey('categories',on_delete=models.CASCADE)
    img_file=models.ImageField(upload_to='images/course/',null=True,verbose_name="")
    user_count=models.IntegerField()
    def __str__(self):
        return self.cname

class coursecontent(models.Model):
    cname=models.ForeignKey('courses',on_delete=models.CASCADE)
    text_file=models.FileField(upload_to='files/',null=False,verbose_name="")
    def __str__(self):
        return self.cname
        
class coursevideocontent(models.Model):
    cname=models.ForeignKey('courses',on_delete=models.CASCADE)
    video_file=models.FileField(upload_to='videos/',null=False,verbose_name="")
    def __str__(self):
        return self.cname+":"+str(self.video_file)

class enrollDetails(models.Model):
    name=models.ForeignKey('UserDetails',to_field='name',on_delete=models.CASCADE)
    cname=models.ForeignKey('courses',on_delete=models.CASCADE)
    status=models.CharField(max_length=100,default='in progress')