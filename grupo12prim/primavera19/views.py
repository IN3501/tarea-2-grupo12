from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'home.html')

def inputs(request):
	return render(request, 'inputs.html')

def inicio(request):
	return render(request, 'inicio.html')

def contacto(request):
	return render(request, 'contacto.html')

def recuperar(request):
	usuario=request.POST["inputText"]
	contraseña=request.POST["inputPassword"]
	correo=request.POST["inputEmail"]


	diccionario={}
	diccionario["comentario1"]=usuario
	diccionario["comentario2"]=contraseña
	diccionario["comentario3"]=correo



	return render(request, "mostrar_resultado.html", diccionario)

def recuperar2(request):
	usuario2=request.POST["inputText"]
	contraseña2=request.POST["inputPassword"]

	diccionario2={}
	diccionario2["comentario4"]=usuario2
	diccionario2["comentario5"]=contraseña2

	return render(request, "mostrar_resultado2.html", diccionario2)


def recuperar3(request):
	usuario3=request.POST["inputText"]
	contraseña3=request.POST["inputPassword"]
	comentario=request.POST["inputTextArea"]

	diccionario3={}
	diccionario3["comentario6"]=usuario3
	diccionario3["comentario7"]=contraseña3
	diccionario3["comentario8"]=comentario
	

	return render(request, "mostrar_resultado3.html", diccionario3)



def recuperar4(request):
	carro=request.POST.getlist('inputCheck1')

	diccionario4={}
	diccionario4["comentario9"]=carro
	
	

	return render(request, "mostrar_resultado4.html", diccionario4)



	