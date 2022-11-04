from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http import JsonResponse
import openai
from os import getenv

# Create your views here.
@api_view(['POST', ])
def Calc(request):
	data = request.data
	print(data)
	prompt = data['operation_type'] + ", return just the result"
	engine = 'text-davinci-002'
	openai.api_key = getenv('API_KEY')
	response = openai.Completion.create(engine=engine, prompt=prompt, temperature=1)
	print(response)
	print(data)
	return JsonResponse({
		'slackUsername': 'Lase',
		'result': int(response['choices'][0]['text'].strip('\n')),
		'operation_type': data['operation_type'],
	})
