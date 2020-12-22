def comer(comida, saudavel):

    if saudavel:
        final = 'quero manter a forma.'

    else:
        final = 'a gente só vive uma vez.'

    return f'Estou comendo {comida} porque {final}'


def dormir(num_horas):

    if num_horas > 8:
        return 'Ah não, dormi muito! Agora estou atrasada para o trabalho!'

    elif num_horas < 6:
        return f'Continuo cansado após dormir {num_horas} horas. =('
