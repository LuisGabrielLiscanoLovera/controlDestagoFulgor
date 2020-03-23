class Menu():
    def menuS():
        MenuScreen="""
<MenuScreen>:
	BoxLayout:
		orientation: "vertical"
		Button:
			text: '1) + Agregar nueva tarea'
			on_press: root.manager.current = 'NuevaTarea'		
			on_press: lamdap=print("1")
		Button:
			text: '2) +Agragar Nuevo Lote  '
			on_press: root.manager.current = 'NuevoLote'
			on_press: lamdap=print("2")
		Button:
			text: '3) +Agregar Integrante  '
			on_press: root.manager.current = 'NuevoIntegrante'
			on_press: lamdap=print("3")   		
		Button:
			text: '4) +Consultas            '
			on_press: root.manager.current = 'Consultas'
			on_press: lamdap=print("4")
		Button:
			text: '5) +Config              '
			on_press: root.manager.current = 'Config'
			on_press: lamdap=print("5")

"""