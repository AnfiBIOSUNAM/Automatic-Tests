Feature: Buscar un producto en la página

  Scenario Outline: Buscar producto con diferentes opciones
    Given estoy logueado en la pagina
    When busco el producto "<producto>"
    Then se muestran los resultados de búsqueda para "<producto>"

    Examples:
      | producto            |
      | PIN DE GATOS        |
      | FRESAS              |
      | ZAPATOS             |