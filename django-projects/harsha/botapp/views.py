from django.shortcuts import render
context={'first':'Welcome 👋 to Lead Chatbot!','second':'''Lead chatbot helps you 24/7 to connect with customers, generate leads and convert more sales. How may we help you?''','data':[]}
# Create your views here.
def message(request):
    global context
    context['data1']=['I want to start','I want to learn more','Is it free','I am an existing user']
    content={'I want to learn more':['Sure. Lead Chatbot makes it possible to build high converting chatbots without knowing how to code. In the chatbot control panel, you can add and remove steps to your conversation and create the right script to collect quality leads.','There are many ways to use and share your Lead Chatbot. You can add your chatbot as a chat widget to your website, embed it as a frame within your pages, use it as a conversational page or use a dedicated link to share it by SMS, WhatsApp, Emails, Facebook and so on.'],'I want to start':['With a simple and friendly platform, Lead Chatbot allows you to design the conversation you want. Within few minutes your lead generation chatbot can be up and running on your website.','Start Now Free'], 'Is it free':['Yes. You can enjoy our Free plans with unlimited chatbots, unlimited domains and unlimited leads for up to 200 conversations per month.',' You can always choose to upgrade to one of our paid plans for additional traffic and extra features.',],'I am an existing user':['Happy to see you here! 😀','How may I help you?'],'data':['I want to learn more','I want to start','Is it free','I am an existing user'],}

    if request.method=="POST":
        msg=request.POST['msg']
        if msg=='I want to learn more':

            context['data'].append(content['I want to learn more'][0])
            context['data'].append(content['I want to learn more'][1])
           
     
        
            
        elif msg == 'I want to start':

            context['data'].append(content['I want to start'][0])
            context['data'].append(content['I want to start'][1])
            
        
           
        elif msg == 'Is it free':

            context['data'].append(content['Is it free'][0])
            context['data'].append(content['Is it free'][1])
           
        
           
        elif msg == 'I am an existing user':
   
            context['data'].append(content['I am an existing user'][0])
            context['data'].append(content['I am an existing user'][1])
            
            
        elif msg == 'Start Now Free':
          
            context['data'].append(" Yes , your in the tutorial")
            
            
        else:
            pass
        



    return render(request,'message.html',context=context)