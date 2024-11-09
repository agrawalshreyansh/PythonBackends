from django.http import JsonResponse
from django.core.mail import send_mail
import json
from django.views.decorators.csrf import csrf_exempt
import smtplib
import ssl
from email.message import EmailMessage



@csrf_exempt
def sendmail(request):
    try:
        data = json.loads(request.body)
        my_email = data['my_email']
        my_password = data['my_password']
        user_email = data['user_email']

        
        email_sender = my_email
        email_pwd = my_password
        email_receiver = user_email

        subject = "Thanks !"
        body = "Thank you for contacting me ! I will get back to you as soon as possible !"
        em = EmailMessage()
        em['From'] = email_sender
        em['To'] = email_receiver
        em['Subject'] = subject
        em.set_content(body)

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context = context) as smtp:
            smtp.login(email_sender, email_pwd)
            smtp.sendmail(email_sender, email_receiver, em.as_string())


        print(user_email,my_email,my_password)
        return JsonResponse({'message': 'Thank you email sent successfully'}, status=200)
    except Exception as e:
            print("Error:", e)
            return JsonResponse({'error': 'Failed to send email', 'details': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid request method'}, status=405)




