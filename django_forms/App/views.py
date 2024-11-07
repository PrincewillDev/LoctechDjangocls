# from django.shortcuts import render, redirect
# from .models import Student
# from .forms import CreateStudentForm
# from django.http import HttpResponse

# def createStudent(request):
#     if request.method == 'POST':
#         form = CreateStudentForm(request.POST)
#         if form.is_valid():
#             student_name = form.cleaned_data['name']
#             student = Student.objects.create(name=student_name)
#             student.save()
#             print('It was saved')
#             # Redirect to prevent form resubmission on refresh
#             return redirect('createStudent')  # Redirect to a 'success' page or the same form page
#     else:
#         form = CreateStudentForm()
#     return render(request, 'form.html', {'form': form})


from django.shortcuts import render, redirect
from .models import Student
from .forms import CreateStudentForm
from django.http import HttpResponse

def createStudent(request):
    if request.method == 'POST':
        form = CreateStudentForm(request.POST)
        if form.is_valid():
            # Check if the student already exists before creating it
            student_name = form.cleaned_data['name']
            # Ensure that a student with this name doesn't already exist to avoid duplicate entries
            if not Student.objects.filter(name=student_name).exists():
                student = Student.objects.create(name=student_name)
                student.save()
                print('It was saved')
                # Redirect after successful submission to avoid resubmission on refresh
                return redirect('success')
            else:
                return HttpResponse('Student with this name already exists!')
    else:
        form = CreateStudentForm()

    return render(request, 'form.html', {'form': form})

def success(request):
    return HttpResponse('Success Whooray')