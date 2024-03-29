from django.shortcuts import render, get_object_or_404, redirect
from django.core.files.storage import FileSystemStorage
from rest_framework.decorators import api_view
import os
import cv2
from PIL import Image
import hashlib
import datetime as dt
from pixel_converter.pixel import make_dot
from .models import ImageModel

# Create your views here.


@api_view(['GET', 'POST'])
def index(request) :
    if request.method == 'GET' :
        return render(request,'pixel.html')

    elif request.method == 'POST' :
        img = request.FILES['image']
        img_obj = ImageModel()
        img_obj.org_image = img
        img_obj.save()
        if not img:
            error='파일을 선택하십시오.'
            return render('pixel.html', error=error)

        k = int(request.POST['k'])
        scale = int(request.POST['scale'])
        blur = int(request.POST['blur'])
        erode = int(request.POST['erode'])

        try:
            alpha = bool(int(request.POST['alpha']))
        except:
            alpha = False

        try:
            to_tw = bool(int(request.POST['to_tw']))
        except:
            to_tw = False

        img_name = hashlib.md5(str(dt.datetime.now()).encode('utf-8')).hexdigest()
        img_path = os.path.join('pixel_converter\\img', img_name + os.path.splitext(img.name)[-1])
        result_path = os.path.join('pixel_converter\\results', img_name + '.png')

        # 파일시스템으로 저장
        fs = FileSystemStorage()
        fs.save(img_path, img)

        img_path_for_open = 'media\\'+ img_path
        result_path_for_open = 'media\\' + result_path

        # with Image.open(img_path_for_open) as img_pl:
        #     if max(img_pl.size) > 1024:
        #         img_pl.thumbnail((1024, 1024), Image.ANTIALIAS)
                # img_pl.save(img_path)
                # 모델로 저장
                # img_obj.org_image = img_pl

        img_res, colors = make_dot(img_path_for_open, k=k, scale=scale, blur=blur, erode=erode, alpha=alpha, to_tw=to_tw)
        # img_obj.result = cv2.imwrite(result_path_for_open, img_res)
        # img_obj.result = cv2.imwrite(result_path_for_open, img_res)
        # img_obj.result = img_res
        # img_obj.save()

        show_obj = ImageModel.objects.first()
        # 'result' : img,'colors' : colors
        print(show_obj)
        return render(request,'pixel.html', {'img_obj' : show_obj})


# def post(request):
#     img = request.files['image']
#     if not img:
#         error='파일을 선택하십시오.'
#         return render('pixel.html', error=error)
#     k = int(request.form['k'])
#     scale = int(request.form['scale'])
#     blur = int(request.form['blur'])
#     erode = int(request.form['erode'])
#     try:
#         alpha = bool(int(request.form['alpha']))
#     except:
#         alpha = False
#     try:
#         to_tw = bool(int(request.form['to_tw']))
#     except:
#         to_tw = False
#     img_name = hashlib.md5(str(dt.datetime.now()).encode('utf-8')).hexdigest()
#     img_path = os.path.join('static/img', img_name + os.path.splitext(img.filename)[-1])
#     result_path = os.path.join('static/results', img_name + '.png')
#     img.save(img_path)
#     with Image.open(img_path) as img_pl:
#         if max(img_pl.size) > 1024:
#             img_pl.thumbnail((1024, 1024), Image.ANTIALIAS)
#             img_pl.save(img_path)
#     img_res, colors = make_dot(img_path, k=k, scale=scale, blur=blur, erode=erode, alpha=alpha, to_tw=to_tw)
#     cv2.imwrite(result_path, img_res)
#     return render('pixel.html', org_img=img_path, result=result_path, colors=colors)
#
#
# @app.errorhandler(413)
# def error_file_size(e):
#     error = '파일 크기가 너무 큽니다. 업로드 가능한 크기는 2MB까지입니다.'
#     return render('pixel.html', error=error), 413
#
#
# @app.errorhandler(404)
# def not_found(e):
#     error = '페이지를 찾을 수 없습니다.'
#     return render('pixel.html', error=error), 404
#
#
# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000, debug=True)