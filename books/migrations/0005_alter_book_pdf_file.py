# Generated by Django 5.0.6 on 2024-08-05 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_book_pdf_file_comment_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='pdf_file',
            field=models.FileField(blank=True, null=True, upload_to='books/pdfs/'),
        ),
    ]