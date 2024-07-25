Feature: Validar la entrada a la pagina y hacer login


	Scenario: Validar entrada a la pagina
		Given quiero entrar a la pagina
		When accedo a la pagina del proyecto
		Then validar entrada
		
	Scenario: Hacer login
		Given quiero inlciar sesion
		When estoy en la pagina de inicio
		Then dar click al boton
		And llenar los datos y enviarlos
	

	
