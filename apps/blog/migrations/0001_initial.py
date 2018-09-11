# Generated by Django 2.0 on 2018-05-26 06:33

import DjangoUeditor.models
import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogActicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acticle_sn', models.CharField(default='', max_length=50, verbose_name='文章唯一标识')),
                ('acticle_name', models.CharField(max_length=100, verbose_name='文章标题')),
                ('acticle_content', DjangoUeditor.models.UEditorField(default='', verbose_name='内容')),
                ('comment_num', models.IntegerField(default=0, verbose_name='评价数')),
                ('fav_num', models.IntegerField(default=0, verbose_name='收藏数')),
                ('click_num', models.IntegerField(default=0, verbose_name='点击数')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '博客文章',
                'verbose_name_plural': '博客文章',
            },
        ),
        migrations.CreateModel(
            name='BlogActicleBanner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='blog/images/', verbose_name='轮播图片')),
                ('index', models.IntegerField(default=0, verbose_name='轮播顺序')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.BlogActicle', verbose_name='博客文章')),
            ],
            options={
                'verbose_name': '轮播文章',
                'verbose_name_plural': '轮播文章',
            },
        ),
        migrations.CreateModel(
            name='BlogCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', help_text='类别名', max_length=30, verbose_name='类别名')),
                ('code', models.CharField(default='', help_text='类别code', max_length=30, verbose_name='类别code')),
                ('desc', models.TextField(default='', help_text='类别描述', verbose_name='类别描述')),
                ('category_type', models.IntegerField(choices=[(1, '一级类目'), (2, '二级类目')], help_text='类目级别', verbose_name='类目级别')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('parent_category', models.ForeignKey(blank=True, help_text='父目录', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub_cat', to='blog.BlogCategory', verbose_name='父类目级别')),
            ],
            options={
                'verbose_name': '博客文章类别',
                'verbose_name_plural': '博客文章类别',
            },
        ),
        migrations.CreateModel(
            name='HotSearchWords',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keywords', models.CharField(default='', max_length=20, verbose_name='热搜词')),
                ('index', models.IntegerField(default=0, verbose_name='排序')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '热搜词',
                'verbose_name_plural': '热搜词',
            },
        ),
    ]
