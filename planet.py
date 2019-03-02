import ephem

__all__ = ['planet_constellation', ]



def planet_constellation(bot, update) -> 'Planet Constellation':
    # update.message.reply_text('Введите имя планеты на английском в нижнем регистре:')
    planet_name = update.message.text.split()[1].capitalize()
    planets = [name for _0, _1, name in ephem._libastro.builtin_planets()]
    if planet_name not in planets:
        update.message.reply_text('Нет такой планеты')
    if planet_name in planets:
        planet = getattr(ephem, planet_name)()
        planet.compute()
        answer = f"Планета {planet_name} находиться в созвездии {ephem.constellation(planet)[1]}"
        update.message.reply_text(answer)
