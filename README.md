<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    Image to PDF Converter
</head>
<body>

<h1>Image to PDF Converter</h1>

<p>This Django web application allows users to upload images and convert them into PDF files. It leverages the powerful <strong>Pillow</strong> library for image handling and <strong>ReportLab</strong> for generating PDF files. The application is designed for simplicity, allowing users to upload an image, convert it to PDF, and download the resulting file.</p>

<h2>Features</h2>
<ul>
    <li><strong>Image Upload</strong>: Supports uploading of images in formats such as PNG, JPEG, etc.</li>
    <li><strong>PDF Conversion</strong>: Converts uploaded images to PDF format with the same dimensions as the original image.</li>
    <li><strong>Downloadable PDF</strong>: Provides the user with a downloadable PDF file directly from the browser.</li>
</ul>

<h2>Requirements</h2>
<ul>
    <li>Python 3.x</li>
    <li>Django 4.x</li>
    <li>Pillow</li>
    <li>ReportLab</li>
</ul>

<h2>Installation</h2>
<ol>
    <li>Clone the repository:
        <pre><code>git clone https://github.com/mmhjmaili/image_to_pdf_with_Django.git</code></pre>
    </li>
    <li>Navigate to the project directory:
        <pre><code>cd image_to_pdf_with_Django</code></pre>
    </li>
    <li>Create the Django app:
        <pre><code>django-admin startapp imagetopdf</code></pre>
    </li>
    <li>Install the dependencies:
        <pre><code>pip install -r requirements.txt</code></pre>
    </li>
    <li>Apply migrations:
        <pre><code>python manage.py migrate</code></pre>
    </li>
    <li>Run the server:
        <pre><code>python manage.py runserver</code></pre>
    </li>
    <li>Visit <code>http://127.0.0.1:8000/convert/</code> in your browser to upload an image and convert it to PDF.</li>
</ol>

<h2>Configuration</h2>
<p>Before running the application, make sure to update the following files:</p>

1. **Add the app to <code>INSTALLED_APPS</code> in <code>project/settings.py</code>:**
   <pre><code>'imagetopdf',</code></pre>

2. **Add the app's URLs to <code>project/urls.py</code>:**
   <pre><code>path('', include('imagetopdf.urls', namespace='imagetopdf'))</code></pre>

<h2>Usage</h2>
<ol>
    <li>Navigate to the image upload page.</li>
    <li>Select an image from your local machine.</li>
    <li>Click the "Convert to PDF" button.</li>
    <li>The generated PDF will be available for download immediately.</li>
</ol>

<h2>Project Structure</h2>
<pre><code>.
├── imagetopdf
│   ├── migrations
│   ├── forms.py                           # Django forms for image upload
│   ├── models.py                          # Image model definition
│   ├── views.py                           # Logic for converting images to PDF
│   ├── urls.py                            # URL routing for the app
├── templates
│   └── imagetopdf
│       └── convert_image_to_pdf.html      # HTML template for image upload
├── media                                  # Uploaded images and generated PDFs
├── requirements.txt                       # Project dependencies
├── manage.py
└── README.md
</code></pre>

<h2>Contributing</h2>
<p>Contributions are welcome! If you have any suggestions or improvements, feel free to open an issue or submit a pull request.</p>

<h2>Need Help?</h2>
<p>If you need assistance, you can reach out to the developer community on Telegram:</p>
<p><a href="https://t.me/Web_Developer_DevOps">https://t.me/Web_Developer_DevOps</a></p>

</body>
</html>

=======================================================================================================================================================================

<!DOCTYPE html>
<html lang="ar">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    محول الصور إلى PDF
</head>
<body>

<h1>محول الصور إلى PDF</h1>

<p>يتيح لك هذا التطبيق المبني على Django رفع الصور وتحويلها إلى ملفات PDF. يعتمد على مكتبة <strong>Pillow</strong> للتعامل مع الصور و<strong>ReportLab</strong> لتوليد ملفات PDF. تم تصميم التطبيق ليكون بسيطًا، مما يسمح للمستخدمين برفع صورة، تحويلها إلى PDF، وتنزيل الملف الناتج.</p>

<h2>الميزات</h2>
<ul>
    <li><strong>رفع الصور</strong>: يدعم رفع الصور بصيغ مثل PNG وJPEG وغيرها.</li>
    <li><strong>تحويل إلى PDF</strong>: يحول الصور المرفوعة إلى صيغة PDF بنفس أبعاد الصورة الأصلية.</li>
    <li><strong>تنزيل ملف PDF</strong>: يوفر للمستخدم ملف PDF جاهزًا للتنزيل مباشرةً من المتصفح.</li>
</ul>

<h2>المتطلبات</h2>
<ul>
    <li>Python 3.x</li>
    <li>Django 4.x</li>
    <li>Pillow</li>
    <li>ReportLab</li>
</ul>

<h2>التثبيت</h2>
<ol>
    <li>استنساخ المستودع:
        <pre><code>git clone https://github.com/mmhjmaili/image_to_pdf_with_Django.git</code></pre>
    </li>
    <li>الانتقال إلى مجلد المشروع:
        <pre><code>cd image_to_pdf_with_Django</code></pre>
    </li>
    <li>إنشاء التطبيق:
        <pre><code>django-admin startapp imagetopdf</code></pre>
    </li>
    <li>تثبيت المتطلبات:
        <pre><code>pip install -r requirements.txt</code></pre>
    </li>
    <li>تطبيق الترقيات:
        <pre><code>python manage.py migrate</code></pre>
    </li>
    <li>تشغيل الخادم:
        <pre><code>python manage.py runserver</code></pre>
    </li>
    <li>زيارة الرابط التالي في المتصفح لتحويل الصور إلى PDF:
        <pre><code>http://127.0.0.1:8000/convert/</code></pre>
    </li>
</ol>

<h2>الإعدادات</h2>
<p>قبل تشغيل التطبيق، تأكد من تحديث الملفات التالية:</p>

1. **إضافة التطبيق إلى <code>INSTALLED_APPS</code> في <code>project/settings.py</code>:**
   <pre><code>'imagetopdf',</code></pre>

2. **إضافة روابط التطبيق إلى <code>project/urls.py</code>:**
   <pre><code>path('', include('imagetopdf.urls', namespace='imagetopdf'))</code></pre>

<h2>الاستخدام</h2>
<ol>
    <li>انتقل إلى صفحة رفع الصور.</li>
    <li>اختر صورة من جهازك.</li>
    <li>اضغط على زر "تحويل إلى PDF".</li>
    <li>سيكون ملف PDF الناتج جاهزًا للتنزيل فورًا.</li>
</ol>

<h2>هيكل المشروع</h2>
<pre><code>.
├── imagetopdf
│   ├── migrations
│   ├── forms.py                           # استمارات Django لرفع الصور
│   ├── models.py                          # تعريف نموذج الصور
│   ├── views.py                           # المنطق لتحويل الصور إلى PDF
│   ├── urls.py                            # توجيه روابط التطبيق
├── templates
│   └── imagetopdf
│       └── convert_image_to_pdf.html      # قالب HTML لرفع الصور
├── media                                  # الصور المرفوعة وملفات PDF الناتجة
├── requirements.txt                       # الاعتماديات الخاصة بالمشروع
├── manage.py
└── README.md
</code></pre>

<h2>المساهمة</h2>
<p>المساهمات مرحب بها! إذا كانت لديك اقتراحات أو تحسينات، لا تتردد في فتح قضية أو إرسال طلب سحب.</p>

<h2>تحتاج إلى مساعدة؟</h2>
<p>إذا كنت بحاجة إلى مساعدة، يمكنك التواصل مع مجتمع المطورين عبر تيليجرام:</p>
<p><a href="https://t.me/Web_Developer_DevOps">https://t.me
