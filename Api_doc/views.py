from django.shortcuts import render

def handler404(tequest,exception):
    return render( tequest, '404.html')


def handler500(tequest,):
    return render( tequest, '500.html')