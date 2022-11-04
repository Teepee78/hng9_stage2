from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http import JsonResponse
import openai
from os import getenv

# Create your views here.
@api_view(['POST', ])
def Calc(request):
	# send request to openai
	data = request.data
	prompt = data['operation_type'] + ", return just the result"
	engine = 'text-davinci-002'
	openai.api_key = getenv('API_KEY')
	response = openai.Completion.create(engine=engine, prompt=prompt, temperature=1)
	print(data)

	try:
		result = int(response['choices'][0]['text'].strip('\n'))
	except Exception:
		prompt = f"perform {data['operation_type']} on {data['x']} and {data['y']}, return just the result as a number"
		response = openai.Completion.create(engine=engine, prompt=prompt, temperature=1)
		try:
			result = int(response['choices'][0]['text'].strip('\n'))
		except Exception:
			prompt = f"{data['operation_type']} {data['x']} and {data['y']}, return just the result as a number"
			response = openai.Completion.create(engine=engine, prompt=prompt, temperature=1)
			result = int(response['choices'][0]['text'].strip('\n'))


	return JsonResponse({
		'slackUsername': 'Lase',
		'result': result,
		'operation_type': data['operation_type'],
	})
