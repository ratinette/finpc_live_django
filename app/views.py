from django.shortcuts import render, redirect

from app.models import Quiz, QuizOptions
import random

# Create your views here.
"""
1. 퀴즈를 보여주는 페이지를 렌더링
2. 퀴즈의 정답을 확인하고 맞으면 다음 퀴즈로
3. 다음퀴즈가 없으면 끝! 하는 페이지로
"""

def get_quiz(request, quiz_id):
    try:
        quiz = Quiz.objects.get(id=quiz_id)
        quiz_option = QuizOptions.objects.filter(quiz_id=quiz_id).all()
    except Quiz.DoesNotExist:
        return redirect("get_404_page")
    
    return render(request, "quiz.html", {"quiz": quiz, "quiz_option": quiz_option})

def check_quiz_answer(request, quiz_id, option_id):
    try:
        quiz_option = QuizOptions.objects.get(id=option_id, quiz_id=quiz_id)
    except QuizOptions.DoesNotExist:
        return redirect("get_404_page")
    is_correct = quiz_option.is_answer
    return render(request, "check_answer.html",{"is_correct":is_correct})

def get_404_page(request):
    return render(request, "404.html", {})