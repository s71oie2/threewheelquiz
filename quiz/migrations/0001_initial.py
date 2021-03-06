# Generated by Django 2.1.5 on 2019-05-15 04:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyQuiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True, verbose_name='퀴즈 푼 날짜')),
                ('myAnswer', models.CharField(max_length=1, verbose_name='회원 답')),
            ],
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='퀴즈내용')),
                ('answer', models.CharField(max_length=1, verbose_name='답')),
            ],
        ),
        migrations.CreateModel(
            name='QuizSub',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='퀴즈주제')),
            ],
        ),
        migrations.AddField(
            model_name='quiz',
            name='quizSub',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quizSubs', to='quiz.QuizSub', verbose_name='퀴즈주제'),
        ),
        migrations.AddField(
            model_name='myquiz',
            name='quiz',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quizs', to='quiz.Quiz', verbose_name='퀴즈'),
        ),
    ]
