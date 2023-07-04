from django.shortcuts import render, redirect
from .forms import UploadFileForm
from .models import UploadedBook


def upload_books(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('uploaded_files')
    else:
        form = UploadFileForm()
    return render(request, 'book/upload_books.html', {'form': form})


def uploaded_files(request):
    files = UploadedBook.objects.all()
    return render(request, 'book/uploaded_files.html', {'files': files})
