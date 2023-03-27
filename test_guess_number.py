import guess_number as game
import re
import random


def test_game_lost():
    input_values = ['2', '3', '4', '5', '6', '7']
    game.input = lambda _: input_values.pop(0)

    result = game.play_game(1)

    assert result == game.GAME_LOST


def test_game_won_on_last_guesss():
    input_values = ['2', '3', '4', '5', '6', '1']
    game.input = lambda _: input_values.pop(0)

    result = game.play_game(1)

    assert result == game.GAME_WON


def test_game_won_on_first_guess():
    input_values = ['50']
    game.input = lambda _: input_values.pop(0)

    result = game.play_game(50)

    assert result == game.GAME_WON


def test_game_won_when_bad_input_ignored():
    input_values = ['1', 'a', '5e', '2', '!', '#', '$', '3', '4', '5', '6']
    game.input = lambda _: input_values.pop(0)

    result = game.play_game(6)

    assert result == game.GAME_WON


def test_game_lost_when_bad_input_ignored():
    input_values = ['1', 'a', '5e', '2', '!', '#', '$', '3', '4', '5', '7']
    game.input = lambda _: input_values.pop(0)

    result = game.play_game(6)

    assert result == game.GAME_LOST


def test_game_congratulations_after_six_guesses(capsys):
    input_values = ['2', '3', '4', '5', '6', '7']
    game.input = lambda _: input_values.pop(0)

    game.play_game(7)
    out, err = capsys.readouterr()

    match = re.search('Congratulations, you guessed the number after 6 guesses!', out)
    assert match, '"Congratulations, you guessed the number after 6 guesses!" was not found in the output.'
    assert err == ''


def test_game_congratulations_after_one_guess(capsys):
    input_values = ['7', 'n']
    game.input = lambda _: input_values.pop(0)
    random.randint = lambda a, b: 7

    game.main()
    out, err = capsys.readouterr()

    match = re.search(r'Congratulations, you guessed the number after 1 guess[es]*!', out)
    assert match, '"Congratulations, you guessed the number after 1 guesses!" was not found in the output.'
    assert err == ''


def test_game_sorry_you_lost(capsys):
    input_values = ['1', '3', '4', '5', '6', '2', 'n']
    game.input = lambda _: input_values.pop(0)
    random.randint = lambda a, b: 7

    game.main()
    out, err = capsys.readouterr()

    match = re.search(r'Sorry, you ran out of guesses.\s+The number was 7.', out)
    assert match, '"Sorry, you ran out of guesses. The number was 7." was not found in the output.'
    assert err == ''
