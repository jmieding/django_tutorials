from django.contrib import admin

from .models import Post, Category, Comment

class ArticleAdmin(admin.ModelAdmin):
  prepopulated_fields = {"slug": ('title',)}
  search_fields = ['text']
  filter_horizontal = ['categories']

class CategoryAdmin(admin.ModelAdmin):
  model = Category

class CommentAdmin(admin.ModelAdmin):
  model = Comment

# Syntax for importing from the blog_app:
#from .models import ModelName
#from .forms import ModelNameForm

# Syntax for importing from another app:
#from anotherapp.models import ModelName

# Syntax for changing the Admin Layout:
#class ModelNameAdmin(admin.ModelAdmin):
# 	list_display = ["__unicode__", "timestamp", "updated"]
# 	form = SignUpForm
#	class Meta:
# 		model = ModelName

# ModelAdmin objects/fields are located here:
#https://docs.djangoproject.com/en/1.8/ref/contrib/admin/

# Syntax for registering models for the admin section of the project
# (This line goes last.)
admin.site.register(Post, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)