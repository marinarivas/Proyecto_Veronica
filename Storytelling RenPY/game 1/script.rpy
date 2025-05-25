# Script de la historia (en modo txt)
# nombre: VERONICA 

# Definicion de imágenes

image fondo_1 = "Exterior castillo.png"
image fondo_2 = "Pasadizos.png"
image Veronica_1 = "Veronica normal.png"
image Veronica_2 = "Veronica enfadada.png"
image Martin_El_Cuervo = "Martin normal.png"
image Martin_El_Cuervo_2= "Martin enfadado.png"
image El_Oso = "El Oso normal.png"
image Sombra_42 = "Sombra 42.png"
image La_Espectro = "La Espectro.png"
image La_Devota = "La Devota.png"

# Definicion de personajes

define v = Character('Veronica', color="#56070c")
define m = Character('Martin_El_Cuervo', color="#195439")
define o = Character('El_Oso', color="#DC4A00")
define s = Character('Sombra_42', color="#581845")
define e = Character('La_Espectro', color="#34495E")
define d = Character('La_Devota', color="#BA4A00")

#################################
# - El juego comienza aquí.
#################################


label start:

   scene fondo_1

   play music "audio/Fondo_musical.mp3" loop
    
   show Veronica_1 at left
   
   v "Ya he llegado, me colaré y buscaré los documentos corruptos del Maldito Cuervo."

   show Martin_El_Cuervo at right

   m "¡Verónica! Te estaba esperando. Bienvenida a mi hogar."
   m "Si logras superar mis pruebas, tal vez salgas de aquí con vida."
   m "Cada habitación contiene una persona que te hará una pregunta. Solo respondiendo correctamente podrás avanzar."

   hide Veronica_1
   show Veronica_2 at left

   v "Maldito... ¡lo pagarás!"

   hide Martin_El_Cuervo
   hide Veronica_2
   scene fondo_2
   with fade
   play music "fondo musical.mp3"

   show Veronica_1 at right   
   show La_Espectro at left

   e "No lo conseguirás Verónica, aquí va el primer acertijo."
   e "¿Cuál es el único mamífero capaz de volar por sí solo?"

   hide Veronica_1   
   hide La_Espectro

label pregunta_uno:

    menu:
        "El murcielago":
            "Dices el murciélago."
            jump El_murcielago

        "El pelicano":
            "Dices el pelícano."
            jump El_pelicano

label El_murcielago:

    e "La Espectro ríe malévolamente y te deja pasar."
    jump pregunta_dos
    
label El_pelícano:
    
     e "Veronica no regresa."
     jump pregunta_uno

label pregunta_dos:
   
    show Veronica_1 at right   
    show Sombra_42 at left

    s "Me sorprende que una delincuente como tú haya superado a La Espectro. Te lo pondré difícil."
    s "Si en un estanque hay 10 peces y 3 se ahogan, ¿cuántos quedan vivos?"

    hide Veronica_1  
    hide Sombra_42

    menu:
        "Siete peces":
            "Dices siete peces."
            jump siete_peces

        "Diez peces":
            "Dices diez peces."
            jump diez_peces

label diez_peces:

    d "Sombra 42 te maldice en voz baja. Pasas."
    jump pregunta_tres
    
label siete_peces:
    
     d "¿Tú has leído bien? Veronica no regresa."
     jump pregunta_dos

label pregunta_tres:

    show Veronica_1 at right   
    show El_Oso at left

    o "A mi no me vas a ganar. Tu pequeño cerebro no podrá con mi inteligencia."
    o "¿Qué se hace más grande cuanto más se le quita?"

    hide Veronica_1  
    hide El_Oso

    menu:
        "El hambre.":
            "Dices el hambre."
            jump El_hambre

        "Un agujero.":
            "Dices un agujero."
            jump Un_agujero

label El_hambre:

    o "El_Oso se tira al suelo y ríe a carcajadas. Le gusta el juego, es un cachondo. Verónica no pasa."
    jump pregunta_tres
    
label Un_agujero:
    
     o "El Oso gruñe y patalea. En realidad es un niño disfrazado de adulto funcional. Adelantas."
     jump pregunta_cuatro

label pregunta_cuatro:

    show Veronica_1 at right   
    show La_Devota at left

    d "Vaya desgraciada, ¿todavía sigues aquí? Anda responde y pasa."
    d "¿Qué alimento puedes comer pero nunca cocinar ni congelar?"

    hide Veronica_1  
    hide La_Devota

    menu:
        "Un huevo crudo.":
            "Dices un huevo crudo."
            jump El_huevo_crudo

        "La lechuga.":
            "Dices la lechuga."
            jump La_lechuga

label El_huevo_crudo:

    d "La Devota simplemente se va con un cigarillo en la mano negando con la cabeza. Te deja sola con la puerta abierta."
    jump pregunta_cinco
    
label La_lechuga:
    
     d "La Devota te mira raro. Parpadea. Te vuelve a mirar raro. Verónica se queda donde está."
     jump pregunta_cuatro

label pregunta_cinco:

    show Veronica_1 at right   
    show Martin_El_Cuervo_2 at left

    m "¿¡Cómo has llegado?! ¡Me pones de los nervios! ¡Para salir deberás usar la lógica, morena de bote!"
    m "Tengo ciudades, pero no casas. Tengo montañas, pero no árboles. Tengo agua, pero no peces. ¿Qué soy?"

    hide Veronica_1  
    hide Martin_El_Cuervo_2

    menu:
        "Qué fácil, vaya tonto, pues un mapa.":
            "Dices un mapa."
            jump El_mapa

        "El juego del Catán.":
            "Dices El Catán."
            jump El_Catán

label El_mapa:

    m "Martin El Cuervo se sorprende y cae al suelo. Más pálido de lo que estaba."
    jump pregunta_seis
    
label El_Catán:
    
     m "Martin El Cuervo se enfada más, luego hace una mueca. Al menos podrás jugar al juego, juegazo por cierto. Ah sí, te encierran y no sales jamás."
     jump pregunta_cinco

label pregunta_seis:

v "¡Bien! He recuperado los documentos, es hora de volver con el equipo y seguir desentrañando el mal."

v "Recoges los documentos y sales de la mansión en cuanto antes."

# Finaliza el juego: