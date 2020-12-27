vetOrInvert = str(input())
tipoAnimal = str(input())
tipoAlimentacao = str(input())

if vetOrInvert == 'vertebrado' and tipoAnimal == 'ave' and tipoAlimentacao == 'carnivoro':
    a = 'aguia'

if vetOrInvert == 'vertebrado' and tipoAnimal == 'ave' and tipoAlimentacao == 'onivoro':
    a = 'pomba'

if vetOrInvert == 'vertebrado' and tipoAnimal == 'mamifero' and tipoAlimentacao == 'onivoro':
    a = 'homem'

if vetOrInvert == 'vertebrado' and tipoAnimal == 'mamifero' and tipoAlimentacao == 'herbivoro':
    a = 'vaca'

if vetOrInvert == 'invertebrado' and tipoAnimal == 'inseto' and tipoAlimentacao == 'hematofago':
    a = 'pulga'

if vetOrInvert == 'invertebrado' and tipoAnimal == 'inseto' and tipoAlimentacao == 'herbivoro':
    a = 'lagarta'

if vetOrInvert == 'invertebrado' and tipoAnimal == 'anelideo' and tipoAlimentacao == 'hematofago':
    a = 'sanguessuga'

if vetOrInvert == 'invertebrado' and tipoAnimal == 'anelideo' and tipoAlimentacao == 'onivoro':
    a = 'minhoca'

print(a)
