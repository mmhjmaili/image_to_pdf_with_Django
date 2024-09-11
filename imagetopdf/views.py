
from reportlab.pdfgen import canvas
import os
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ImageUploadForm
from .models import ImageUpload
from PIL import Image
from django.conf import settings
import urllib.parse

def convert_image_to_pdf(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image_instance = form.save()

            # الحصول على المسار الكامل للصورة
            image_path = os.path.join(settings.MEDIA_ROOT, image_instance.image.name)

            # إنشاء ملف PDF
            pdf_filename = f"{image_instance.image.name.split('.')[0]}.pdf"
            pdf_path = os.path.join(settings.MEDIA_ROOT, pdf_filename)
            c = canvas.Canvas(pdf_path)

            # فتح الصورة باستخدام Pillow
            img = Image.open(image_path)

            # تعديل حجم الصفحة ليطابق حجم الصورة
            width, height = img.size
            c.setPageSize((width, height))

            # إضافة الصورة إلى ملف PDF
            c.drawImage(image_path, 0, 0, width, height)

            # حفظ ملف PDF
            c.save()

            # إنشاء رابط لتحميل ملف PDF
            pdf_url = request.build_absolute_uri(os.path.join(settings.MEDIA_URL, pdf_filename))

            # تجهيز رابط WhatsApp
            message = f"لقد تم تحويل الصورة إلى PDF. يمكنك تحميله من الرابط التالي: {pdf_url}"
            encoded_message = urllib.parse.quote(message)
            whatsapp_url = f"https://wa.me/?text={encoded_message}"

            # عرض صفحة تحتوي على رابط لتحميل PDF ورابط WhatsApp
            return render(request, 'imagetopdf/convert_image_to_pdf.html', {
                'pdf_url': pdf_url,
                'whatsapp_url': whatsapp_url
            })

    else:
        form = ImageUploadForm()

    return render(request, 'imagetopdf/convert_image_to_pdf.html', {'form': form})
