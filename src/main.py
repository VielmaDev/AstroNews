import flet as ft
from flet import TextField, ElevatedButton, Column, Row, Text, Container, alignment, Dropdown, dropdown, Colors, Image, DataRow, DataCell, DataTable, DataColumn
import dbapi
from datetime import datetime
from time import strftime

# ---CONFIGURACIÓN DE FORMATOS ---
ORIGINAL_API_FORMAT = "%Y-%m-%d" #Formato ISO 
API_DATE_FORMAT = "%d-%m-%Y" #Nuevo formato fecha a convertir.

class myapp:
    def __init__(self, page: ft.Page):
        page.title = "Agenda NASA"
        page.bgcolor = Colors.BLACK26
        page.theme_mode = "dark"
        page.scroll = ft.ScrollMode.ADAPTIVE

        # Conexión con módulo dbapi 
        Apod= dbapi.apod()
        Neows= dbapi.neows() 

        # Método selector de pestaña
        def tab_chance(e):
            print("Selected tab:", e.control.selected_index)

            if page.navigation_bar.selected_index == 0:
                page.remove(asteroid_container)
                page.add(news_container)
            elif page.navigation_bar.selected_index == 1:
                page.remove(news_container)
                page.add(asteroid_container)

        # Menú de la app
        page.navigation_bar = ft.CupertinoNavigationBar(
            bgcolor=ft.Colors.BLUE_600,
            inactive_color=ft.Colors.WHITE,
            active_color=ft.Colors.BLACK,
            on_change = tab_chance, # Selector de pestaña
            destinations=[
                ft.NavigationBarDestination(icon=ft.Icons.HOME,
                                            selected_icon=ft.Icons.HOME, label="News"),
                ft.NavigationBarDestination(icon=ft.Icons.SEARCH, label="Asteroids"),
            ],
            selected_index = 0,
        )

        # Widgets News         
        label = ft.Text(f"{Apod['title']}", size=25,
                         color=ft.Colors.BLUE,
                         text_align=ft.TextAlign.CENTER)
        apod_label = Row(
                        controls=[label],
                        alignment="center", # Alineación horizontal
                    )
        
        date_objeto = datetime.strptime(Apod['date'], ORIGINAL_API_FORMAT) #Convierte la cadena de la API en un objeto 'datetime'.
        date_format = date_objeto.strftime(API_DATE_FORMAT) # Formatea el objeto `datetime` al nuevo formato de cadena.

        dates = ft.Text(
                        date_format,
                        size=17,
                        color=ft.Colors.WHITE,
                        text_align=ft.TextAlign.CENTER)
        apod_date = Row(
                        controls=[dates],
                        alignment="center", # Alineación horizontal
                    )
       
        imagen = ft.Image(src=f"{Apod['url']}", width=380, height=380)
        apod_imagen = Row(
                        controls=[imagen],
                        alignment="center", # Alineación horizontal
                        vertical_alignment="center"  # Alineación vertical
                    )
        apod_content = ft.Container(
                content=ft.Column([
                        ft.Text(f"{Apod['explanation']}",size=16,
                                color=ft.Colors.WHITE,
                                text_align=ft.TextAlign.JUSTIFY),
                    ]),
                padding=20)

        # Widget Asteroids
        #Etiqueta encabezado widget Asteroid
        label = ft.Text("Asteroides cercanos a la Tierra", size=23,
                            color=ft.Colors.BLUE, 
                            text_align=ft.TextAlign.CENTER)
        neows_label = Row(
                        controls=[label],
                        alignment="center", # Alineación horizontal
                    )
        #Contador de elementos widget Ateroid
        count = ft.Text(f"Cantidad de objetos:  {Neows['element_count']}", size=16,
                            color=ft.Colors.WHITE,
                            text_align=ft.TextAlign.CENTER)
        neows_count = Row(
                        controls=[count],
                        alignment="center", # Alineación horizontal
        )

        # Fecha clave de busqueda
        #date_key = list(Neows['near_earth_objects'].keys())[0]
            
        # ---Definición de las Columnas de la DataTable ---
        columns=[
                DataColumn(ft.Text("Neo id"), 
                              heading_row_alignment=ft.MainAxisAlignment.CENTER), #Centra las celdas de datos
                DataColumn(ft.Text("Nombre"), 
                              heading_row_alignment=ft.MainAxisAlignment.CENTER), #Centra las celdas de datos
                DataColumn(ft.Text("Magnitud"), 
                              heading_row_alignment=ft.MainAxisAlignment.CENTER), #Centra las celdas de datos
                DataColumn(ft.Text("Diámetro Km-Max"), 
                              heading_row_alignment=ft.MainAxisAlignment.CENTER), #Centra las celdas de datos
                DataColumn(ft.Text("Velocidad"), 
                              heading_row_alignment=ft.MainAxisAlignment.CENTER), #Centra las celdas de datos
                DataColumn(ft.Text("Dist. Astronómica"), 
                              heading_row_alignment=ft.MainAxisAlignment.CENTER), #Centra las celdas de datos
                DataColumn(ft.Text("Orbita"), 
                              heading_row_alignment=ft.MainAxisAlignment.CENTER), #Centra las celdas de datos
                DataColumn(ft.Text("Fecha aproximación"), 
                              heading_row_alignment=ft.MainAxisAlignment.CENTER), #Centra las celdas de datos
                DataColumn(ft.Text("Peligro"), 
                              heading_row_alignment=ft.MainAxisAlignment.CENTER), #Centra las celdas de datos
        ]

        #Generador de Filas (Rows) usando un bucle for
        neows_table= []
        
        #--- El bucle for itera sobre cada diccionario 'Neows' ---
        for date_key, neos_list in Neows['near_earth_objects'].items():
            for neo_data in neos_list:
                approach_data = neo_data['close_approach_data'][0]
                   
            # ---Definición de las Filas (Rows) de la DataTable ---
                rows=[
                    DataRow(
                    cells=[

                    #ft.DataCell(ft.Text(f"{Neows['near_earth_objects'][date_key][0]['neo_reference_id']}")),
                    #ft.DataCell(ft.Text(f"{Neows['near_earth_objects'][date_key][0]['close_approach_data'][0]['relative_velocity']['kilometers_per_hour']}")),
                    #ft.DataCell(ft.Text(f"{Neows['near_earth_objects'][date_key][0]['is_potentially_hazardous_asteroid']}")),

                    # El id de referncia
                    DataCell(ft.Text(f"{neo_data['neo_reference_id']}")),
                    # El nombre del asteroide
                    DataCell(ft.Text(f"{neo_data['name']}")),
                    # La magnitud absoluta
                    DataCell(ft.Text(f"{neo_data['absolute_magnitude_h']}")),
                    # E diámetro máximo
                    DataCell(ft.Text(f"{neo_data['estimated_diameter']['kilometers']['estimated_diameter_max']}")),
                    # La velocidad
                    DataCell(ft.Text(f"{approach_data['relative_velocity']['kilometers_per_hour']}")),
                    # La distancia astronómica
                    DataCell(ft.Text(f"{approach_data['miss_distance']['astronomical']}")),
                    # El cuerpo orbitante
                    DataCell(ft.Text(f"{approach_data['orbiting_body']}")),
                    # La fecha cerrada de aproximación
                    DataCell(ft.Text(f"{approach_data['close_approach_date_full']}")),
                    # Potencial peligro
                    DataCell(ft.Text(f"{neo_data['is_potentially_hazardous_asteroid']}")),
                ],
            ),
        ]
                #Agrega la fila (Row) con sus celdas a la lista neows_table
                neows_table.append(rows) # Revisar porque no guarda los datos

        # Tabla de widget Asteroids
        table= DataTable(
            #--- Configuración DataTable ---
            columns=columns, 
            rows=neows_table,
            width=1300,
            border=ft.border.all(1, ft.Colors.BLUE_500),
            border_radius=10,
            vertical_lines=ft.border.BorderSide(2, ft.Colors.BLUE_500),
            horizontal_lines=ft.border.BorderSide(2, ft.Colors.BLUE_500),
            heading_text_style=ft.TextStyle(weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_500),
            data_text_style=ft.TextStyle(color=ft.Colors.WHITE),
            column_spacing=10,
        )

        neows_table= Row(
                        controls=[table],
                        alignment="center", # Alineación horizontal
                    )
        
        # Contenedor de widgets news
        news_container = Container(
                    content=ft.Column(
                        controls=[
                            apod_label,
                            apod_date,
                            apod_imagen,
                            apod_content
                        ],
                    ),padding=20 
                )
        
        # Contenedor de widgets neows
        asteroid_container = Container(
                        content=ft.Column(
                                controls=[
                                    neows_label,
                                    neows_count,
                                    neows_table,
                            ],
                    ),padding=10 
                )

        page.add(news_container)
        page.update()

if __name__ == "__main__":
    ft.app(target = myapp)


