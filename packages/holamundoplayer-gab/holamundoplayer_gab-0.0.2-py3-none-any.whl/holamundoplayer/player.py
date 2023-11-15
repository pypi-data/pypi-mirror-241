""""
Esta es el modulo que incluye la clase 
de reproductor de música
"""


class Player:
    """
      Esta clase crea un reproductor de música
    """

    def play(self, song):
        """
        reproduce la canción que recibió como parámetro

        Parameters:
        song(str): Este es un string con el path de la canción

        Returns:
        int: devuelve 1 si reproduce con éxito, en caso de fracaso devuelve 0
        """
        print("reproduciendo canción")

    def stop(self):
        print("stopping")
