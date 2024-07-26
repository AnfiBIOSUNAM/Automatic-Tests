Feature: Cambiar el nombre del perfil
    Scenario: El usuario cambia el nombre del perfil
    Given Estamos en la página de inicio
    When Navegar a la sección del perfil
    And Edito el nombre a "Anonimo"
    And Guardo el nombre
    Then Verificar el nombre "Anonimo" en la pagina