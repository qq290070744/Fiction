# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-01-02 10:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appannie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device', models.CharField(default='', max_length=255, verbose_name='设备')),
                ('country_region', models.CharField(default='', max_length=255, verbose_name='国家/地区')),
                ('category', models.CharField(default='', max_length=255, verbose_name='类别')),
                ('ranking_type', models.CharField(default='', max_length=255, verbose_name='排行 类型')),
                ('index', models.IntegerField(default=0, verbose_name='排名')),
                ('app_id', models.CharField(default='', max_length=255, verbose_name='APP ID')),
                ('app_name', models.CharField(default='', max_length=255, verbose_name='APP NAME')),
                ('app_img', models.CharField(default='', max_length=255, verbose_name='APP 图片')),
                ('app_description', models.TextField(default='', verbose_name='APP 说明')),
                ('app_company_website', models.CharField(default='', max_length=255, verbose_name='APP 公司网站')),
                ('compatibility', models.CharField(default='', max_length=255, verbose_name='兼容性')),
                ('updated', models.CharField(default='', max_length=255, verbose_name='更新')),
                ('version', models.CharField(default='', max_length=255, verbose_name='版本')),
                ('size', models.CharField(default='', max_length=255, verbose_name='大小')),
                ('only_32_bit', models.CharField(default='', max_length=255, verbose_name='仅限32位')),
                ('language', models.TextField(default='', verbose_name='语言')),
                ('seller', models.CharField(default='', max_length=255, verbose_name='出版商')),
                ('headquarter_country_region', models.CharField(default='', max_length=255, verbose_name='总部所在国家/地区')),
                ('rating', models.CharField(default='', max_length=255, verbose_name='评级')),
                ('family_sharing', models.CharField(default='', max_length=255, verbose_name='家庭共享')),
                ('requirements', models.CharField(default='', max_length=255, verbose_name='要求')),
                ('bundle_ID', models.CharField(default='', max_length=255, verbose_name='套餐 ID')),
                ('game_center', models.CharField(default='', max_length=255, verbose_name='游戏中心')),
                ('supports_apple_watch', models.CharField(default='', max_length=255, verbose_name='支持Apple Watch')),
                ('supports_iMessage', models.CharField(default='', max_length=255, verbose_name='支持iMessage')),
                ('update_time', models.CharField(default='', max_length=255, verbose_name='本条数据更新时间')),
            ],
        ),
        migrations.CreateModel(
            name='Classification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(default='', max_length=255, verbose_name='小说来源')),
                ('name', models.CharField(max_length=255, verbose_name='小说分类')),
            ],
            options={
                'verbose_name': '小说分类',
                'verbose_name_plural': '小说分类',
            },
        ),
        migrations.CreateModel(
            name='Comics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True)),
                ('cover_image', models.CharField(max_length=255, unique=True, verbose_name='封面图片')),
            ],
        ),
        migrations.CreateModel(
            name='Comics_img',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.CharField(max_length=255, unique=True, verbose_name='图片')),
                ('sort', models.IntegerField(verbose_name='排序')),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.Comics')),
            ],
        ),
        migrations.CreateModel(
            name='Fiction_chapter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chapter_name', models.CharField(max_length=255, verbose_name='章节名称')),
                ('chapter_content', models.TextField(verbose_name='章节内容')),
                ('is_vip', models.BooleanField(default=False, verbose_name='是否是VIP章节')),
                ('update_time', models.CharField(default='', max_length=255, verbose_name='章节更新时间')),
                ('order_by', models.IntegerField(default=0, verbose_name='排序')),
            ],
            options={
                'verbose_name': '章节',
                'verbose_name_plural': '章节',
            },
        ),
        migrations.CreateModel(
            name='Fiction_list',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fiction_name', models.CharField(max_length=255, verbose_name='小说名称')),
                ('author', models.CharField(max_length=255, verbose_name='作者')),
                ('viewing_count', models.CharField(default='', max_length=255, verbose_name='浏览数/点击数')),
                ('update_time', models.CharField(default='', max_length=255, verbose_name='小说更新时间')),
                ('status', models.CharField(default='连载', max_length=255, verbose_name='小说状态')),
                ('image', models.CharField(default='', max_length=255, verbose_name='小说封面图片')),
                ('cassificationc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.Classification', verbose_name='小说分类')),
            ],
            options={
                'verbose_name': '小说',
                'verbose_name_plural': '小说',
            },
        ),
        migrations.CreateModel(
            name='Hentai',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=255, verbose_name='名称')),
                ('author', models.CharField(max_length=255, verbose_name='作者')),
                ('posted', models.CharField(default='', max_length=255, verbose_name='更新时间')),
                ('parent', models.CharField(default='', max_length=255)),
                ('language', models.CharField(default='', max_length=255, verbose_name='语言')),
                ('file_size', models.CharField(default='', max_length=255, verbose_name='文件大小')),
                ('length', models.CharField(default='', max_length=255, verbose_name='长度')),
                ('classification', models.CharField(default='', max_length=255, verbose_name='分类')),
            ],
        ),
        migrations.CreateModel(
            name='Hentai2read',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='名称')),
                ('cover_image', models.CharField(default='', max_length=255, verbose_name='封面')),
                ('Parody', models.CharField(default='', max_length=255)),
                ('Ranking', models.CharField(default='', max_length=255)),
                ('Status', models.CharField(default='', max_length=255)),
                ('Release_Year', models.CharField(default='', max_length=255)),
                ('View', models.CharField(default='', max_length=255)),
                ('Author', models.CharField(default='', max_length=255)),
                ('Artist', models.CharField(default='', max_length=255)),
                ('Category', models.CharField(default='', max_length=255)),
                ('Content', models.CharField(default='', max_length=255)),
                ('Character', models.CharField(default='', max_length=255)),
                ('Language', models.CharField(default='', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Hentai2read_chapter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chapter_name', models.CharField(max_length=255, verbose_name='章节名')),
                ('chapter_index', models.FloatField(verbose_name='章节索引')),
                ('page_num', models.IntegerField(null=True, verbose_name='图片数量')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.Hentai2read', verbose_name='名称')),
            ],
        ),
        migrations.CreateModel(
            name='Hentai2read_chapter_flag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chapter_name', models.CharField(max_length=255, unique=True, verbose_name='名称')),
            ],
        ),
        migrations.CreateModel(
            name='Hentai2read_flag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='名称')),
            ],
        ),
        migrations.CreateModel(
            name='Hentai2read_img',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_index', models.IntegerField(verbose_name='图片索引')),
                ('image', models.CharField(max_length=255, verbose_name='图片')),
                ('chapter_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.Hentai2read_chapter', verbose_name='章节名')),
            ],
        ),
        migrations.CreateModel(
            name='Hentai_chapter_flag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chapter_name', models.CharField(max_length=255, unique=True, verbose_name='名称')),
            ],
        ),
        migrations.CreateModel(
            name='Hentai_flag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='名称')),
            ],
        ),
        migrations.CreateModel(
            name='Hentai_img',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.CharField(max_length=255, unique=True, verbose_name='图片')),
                ('sort', models.IntegerField(verbose_name='排序')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.Hentai', verbose_name='名称')),
            ],
        ),
        migrations.CreateModel(
            name='Xiangqing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(max_length=255, verbose_name='来源网站')),
                ('name', models.CharField(max_length=255, verbose_name='姓名')),
                ('age', models.CharField(default='', max_length=255, verbose_name='年龄')),
                ('photo', models.CharField(default='', max_length=255, verbose_name='头像')),
                ('country_address', models.CharField(default='', max_length=255, verbose_name='国家地区')),
                ('instructions', models.TextField(default='', verbose_name='交友说明')),
                ('relationship', models.CharField(default='', max_length=255, verbose_name='状态：是否单身')),
                ('education', models.CharField(default='', max_length=255, verbose_name='学历')),
                ('faith', models.CharField(default='', max_length=255, verbose_name='宗教信仰')),
                ('have_kids', models.CharField(default='', max_length=255, verbose_name='是否有小孩')),
                ('body_type', models.CharField(default='', max_length=255, verbose_name='体型')),
                ('smoke', models.CharField(default='', max_length=255, verbose_name='是否抽烟')),
                ('want_kids', models.CharField(default='', max_length=255, verbose_name='打不打算要小孩')),
                ('height', models.CharField(default='', max_length=255, verbose_name='身高')),
                ('drink', models.CharField(default='', max_length=255, verbose_name='喝不喝酒')),
                ('ethnicity', models.CharField(default='', max_length=255, verbose_name='种族')),
                ('more', models.TextField(default='', verbose_name='更多信息')),
                ('photo_gallery', models.TextField(default='', verbose_name='照片库')),
                ('sex', models.CharField(default='', max_length=255, verbose_name='性别')),
                ('INTERESTS_and_PORTS', models.TextField(default='', verbose_name='兴趣爱好')),
                ('What_She_is_Looking_For', models.TextField(default='', verbose_name='她在寻找什么')),
            ],
            options={
                'verbose_name': '交友网站信息',
                'verbose_name_plural': '交友网站信息',
            },
        ),
        migrations.AlterUniqueTogether(
            name='xiangqing',
            unique_together=set([('source', 'name')]),
        ),
        migrations.AlterUniqueTogether(
            name='hentai',
            unique_together=set([('name', 'author')]),
        ),
        migrations.AddField(
            model_name='fiction_chapter',
            name='fiction_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.Fiction_list', verbose_name='小说名称'),
        ),
        migrations.AlterUniqueTogether(
            name='classification',
            unique_together=set([('source', 'name')]),
        ),
        migrations.AlterUniqueTogether(
            name='hentai_img',
            unique_together=set([('name', 'sort')]),
        ),
        migrations.AlterUniqueTogether(
            name='hentai2read_img',
            unique_together=set([('chapter_name', 'img_index')]),
        ),
        migrations.AlterUniqueTogether(
            name='hentai2read_chapter',
            unique_together=set([('name', 'chapter_index')]),
        ),
        migrations.AlterUniqueTogether(
            name='fiction_list',
            unique_together=set([('fiction_name', 'author', 'cassificationc')]),
        ),
        migrations.AlterUniqueTogether(
            name='fiction_chapter',
            unique_together=set([('chapter_name', 'fiction_name')]),
        ),
        migrations.AlterUniqueTogether(
            name='comics_img',
            unique_together=set([('title', 'sort')]),
        ),
    ]