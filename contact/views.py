#coding:utf8
from django.shortcuts import render_to_response
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.template import RequestContext
from django.http import Http404,HttpResponse
from django.core.mail import EmailMultiAlternatives
import datetime
# Create your views here.

def home(request):
	return render_to_response('index.html',context_instance=RequestContext(request))

def en_home(request):
	return render_to_response('en_index.html',context_instance=RequestContext(request))

def sendmail(request):

	if request.method=='POST':
		s = datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')
		subject = '新订单产生:'+s
		name = request.POST['name']
		tel = request.POST['tel']
		address = request.POST['address']
		html_content = render_to_string('email_template.html', {'s':s,'name':name,'tel':tel,'address':address},context_instance=RequestContext(request))
		text_content = strip_tags(html_content)
		from_email = 'i@lushizhao.me'
		msg = EmailMultiAlternatives(subject, text_content, from_email, ['lushizhao@qq.com'])
		msg.attach_alternative(html_content, "text/html")
		msg.send()
		return HttpResponse('thanks')
	else:
		return HttpResponse('error')

