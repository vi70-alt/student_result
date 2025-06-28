from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout as auth_logout
from .models import Student, Result

# Redirect root to login page
def welcome_redirect(request):
    return redirect('login')

# Handle post-login redirect based on user type

@login_required
def after_login(request):
    if request.user.is_superuser or request.user.is_staff:
        return redirect('home') 
    else:
        return redirect('my_results') 
# Home page (for admin/staff only)
@login_required
def home(request):
    return render(request, 'main/home.html')

# Admin-only check
def is_admin(user):
    return user.is_superuser

# Add student view (only admin allowed)
@user_passes_test(is_admin)
def add_student(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        roll_no = request.POST['roll_no']
        department = request.POST['department']

        user = User.objects.create_user(username=username, password=password)
        Student.objects.create(user=user, roll_no=roll_no, department=department)
        return redirect('add_student')

    return render(request, 'main/add_student.html')

# Admin enters student result
@user_passes_test(is_admin)
def enter_result(request):
    if request.method == "POST":
        username = request.POST['username']
        subject = request.POST['subject']
        marks = int(request.POST['marks'])

        try:
            student = Student.objects.get(user__username=username)
            Result.objects.create(student=student, subject=subject, marks=marks)
            return redirect('enter_result')
        except Student.DoesNotExist:
            return render(request, 'main/enter_result.html', {'error': 'Student not found'})

    return render(request, 'main/enter_result.html')

# Student views their own result
@login_required
def student_results(request):
    if request.user.is_superuser or request.user.is_staff:
        return redirect('home')  # Prevent admin access

    try:
        student = Student.objects.get(user=request.user)
        results = Result.objects.filter(student=student)
        return render(request, 'main/view_results.html', {'results': results})
    except Student.DoesNotExist:
        return redirect('home')

# Optional logout view
def logout_view(request):
    auth_logout(request)
    return redirect('login')
