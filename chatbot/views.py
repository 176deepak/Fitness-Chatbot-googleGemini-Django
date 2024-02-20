from django.shortcuts import render
from .models import *
from .utils import *

# chatbot 
def chatbot(request):
    # check, user asks anything to fitness bot
    if request.method == "POST":
        # extract the users query or problem
        userquery = request.POST
        if len(userquery) == 2:
            prompt = userquery.get('user-query')
            chat = ask_to_bot(query=prompt)        
            return render(request, 'index.html', context={"response": chat})
        elif len(userquery) > 2:
            # save the image to folder
            UserImage.objects.create(image=request.FILES['image'])
            # user details 
            user_age = userquery.get('age')
            user_btype = userquery.get("body_type")
            user_goal = userquery.get("goal")
            image_name = str(request.FILES['image'])
            # make prompt using details
            prompt = f"I am {user_age} years old. My body type is {user_btype} and i want {user_goal}. Now suggest me diet plan, workout plan."

            chat = ask_to_bot(query=prompt, image=image_name)
            return render(request, 'index.html', context={"chat": chat})

    return render(request, 'index.html')







            