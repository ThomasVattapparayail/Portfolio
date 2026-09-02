from django.shortcuts import render,redirect
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings

# Create your views here.
def index(request):
    return render(request,'index.html')

def contact(request):

    if request.method == "POST":

        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        email_subject = f"Portfolio Contact: {subject}"

        email_message = f"""
                            You received a new message from your portfolio.

                            Name: {name}
                            Visitor Email: {email}
                            Subject: {subject}

                            Message:
                            {message}
                            """

        send_mail(
            email_subject,
            email_message,       
            email,
            ["midhunchackoxyz@gmail.com"],
            fail_silently=False,
        )

        messages.success(
            request,
            "Your message has been sent successfully!"
        )

        return redirect("index")
    return redirect("index")

