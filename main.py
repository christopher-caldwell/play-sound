from playsound import playsound  # imports method from object package
import click  # imports object that contains methods
from sound_list import sound_list  # contains the dict of songs available


@click.command()
@click.option("--song-number", 'song',
              prompt="Number of audio file",
              type=click.IntRange(0, 20, clamp=True),
              help="The number that matches the audio file you want to play")
def play_selected_sound(song):
    """Press a button, hear the beep"""

    while song != 0:
# cast the song int to a string, use it as the key to a hash map dictionary to grab the file path
        playsound(sound_list[(str(song))])
        play_selected_sound()
    exit


if __name__ == '__main__':
    play_selected_sound()
