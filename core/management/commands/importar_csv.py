import csv
from django.core.management.base import BaseCommand
from core.models import Projeto

def to_none(value):
    if value in ('', 'NULL', 'null', None):
        return None
    return value

class Command(BaseCommand):
    help = 'Importa dados de um CSV'

    def handle(self, *args, **kwargs):
        with open('./tabelas/projeto_tecnologias.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                projeto_id = int(row['projeto_id'])
                tecnologia_id = int(row['tecnologia_id'])

                if projeto_id and tecnologia_id:
                    projeto = Projeto.objects.get(id=projeto_id)
                    projeto.tecnologias.add(tecnologia_id)

        self.stdout.write(self.style.SUCCESS('Importação concluída!'))