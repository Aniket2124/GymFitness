from django.contrib import admin
from accounts.models import Contact, Enrollment, Trainer, Membership_Plan, Gallery, Attendance
# Register your models here.

@admin.register(Contact)

class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phonenumber', 'description']


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ['fullname','email','gender','phonenumber']



@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
    list_display = ['trainer_name','gender']




@admin.register(Membership_Plan)
class Membership_PlanAdmin(admin.ModelAdmin):
    list_display = ['plan','price']

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ['title','image']


admin.site.register(Attendance)