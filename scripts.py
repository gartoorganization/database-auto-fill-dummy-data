import uuid
import random
from random import randint
from django.utils import timezone
from django.db import connection
from django.apps import apps


def fillDummyData():
	i=0
	table_info = []
	tables = connection.introspection.table_names()
	seen_models = connection.introspection.installed_models(tables)
	for p in range(500000):
		for counter, model in enumerate(apps.get_models()):
			if len(str(model._meta.__dict__['db_table']).split('django')) == 1:
				if str(model._meta.__dict__['db_table']) != "auth_permission":
					model_create =  model._meta.__dict__['model']()
					for field in model._meta.fields:
						#field type of model
						field_type = "{}".format(field.get_internal_type())
						value = None
						if field_type == "AutoField":
							pass
						elif field_type == "BooleanField":
							value = random.choice([True, False])
						elif field_type == "DateTimeField":
							value = timezone.now()
						elif field_type == "CharField":
							if len(field.__dict__['choices']) != 0:
								value = random.choice(field.__dict__['choices'])
								value = str(value).split('\'')
								value = value[1]
							else:
								if field.__dict__['name'] == "module":
									print(field.__dict__)
								value = str(uuid.uuid1())
								value = value[0: int(field.__dict__['max_length'])]
						elif field_type == "foreignTableKey":
							value = foreignTable(field.rel.to)
						elif field_type == "FloatField":
							value = random.uniform(1, 100000000)
						elif field_type == "IntegerField":
							value = randint(0, 2147483647)
						elif field_type == "FileField":
							value = None
						elif field_type == "TextField":
							value = "Lorem ipsum dolor sit amet, vix cu consulatu consequat. Soluta indoctum et usu. Vim te sanctus laboramus conceptam, in eros populo oblique mea, his et persius explicari definitionem. Ut cum stet legere delectus, eu percipit suavitate mea. In etiam iudico patrioque cum, vel timeam urbanitas cu. Porro fuisset vivendum ne nec, nec ea perpetua constituam. Diam nobis ei mel, has tale blandit reprehendunt an. Quem essent erroribus id duo, ea vide ferri affert duo. Tibique eloquentiam at est, duis placerat nam ne, vel atqui scripta id. Eam ponderum verterem deterruisset ut, vel at etiam munere sensibus. Porro munere aliquando vix ad. Elitr albucius percipitur cu eam. Eu ius putant utroque. Omnis nostro bonorum nam id. No pri tale forensibus dissentiet, in doctus recteque dignissim usu. Lobortis partiendo accommodare nec at, propriae invidunt vituperatoribus ad vim. His placerat dignissim te, in minimum similique efficiantur sit. Elitr theophrastus est ne, ius suas denique prodesset ei. Facilis assentior quaerendum id eam. Pri ei homero elaboraret. Probatus scribentur eam at, movet primis sit ei. Id sit maluisset vituperatoribus, choro graeco ne cum. Ei mea voluptaria intellegebat, vim alia saepe detracto cu. Hinc copiosae gloriatur at vim."
						elif field_type == "SlugField":
							value = str(uuid.uuid1())
						elif field_type == "JSONField":
							value = {str(uuid.uuid1()):str(uuid.uuid1())}
						elif field_type == "PositiveSmallIntegerField":
							value = randint(0, 2147483647)
						else:
							print(field_type)
						if value != None:
							setattr(model_create,field.__dict__['name'],value)
					model_create.save()
					i = i + 1
					print("Se agrego {} campo".format(i))
		print("se agregaron {} registros en la base de datos".format(i))

def foreignTable(model):
	model_foreignTable = model()
	for foreig_field in model_foreignTable._meta.fields:
		field_type_foreignTable = "{}".format(foreig_field.get_internal_type())
		value_foreignTable = None
		if field_type_foreignTable == "AutoField":
			pass
		elif field_type_foreignTable == "BooleanField":
			value_foreignTable = random.choice([True, False])
		elif field_type_foreignTable == "DateTimeField":
			value_foreignTable = timezone.now()
		elif field_type_foreignTable == "CharField":
			if len(foreig_field.__dict__['choices']) != 0:
				value_foreignTable = random.choice(foreig_field.__dict__['choices'])
				value_foreignTable = str(value_foreignTable).split('\'')
				value_foreignTable = value_foreignTable[1]
			else:
				if foreig_field.__dict__['name'] == "module":
					print(foreig_field.__dict__)
				value_foreignTable = str(uuid.uuid1())
				value_foreignTable = value_foreignTable[0: int(foreig_field.__dict__['max_length'])]

		elif field_type_foreignTable == "FloatField":
			value_foreignTable = random.uniform(1, 100000000)
		elif field_type_foreignTable == "IntegerField":
			value_foreignTable = randint(0, 2147483647)
		elif field_type_foreignTable == "FileField":
			value_foreignTable = None
		elif field_type_foreignTable == "TextField":
			value_foreignTable = "Lorem ipsum dolor sit amet, vix cu consulatu consequat. Soluta indoctum et usu. Vim te sanctus laboramus conceptam, in eros populo oblique mea, his et persius explicari definitionem. Ut cum stet legere delectus, eu percipit suavitate mea. In etiam iudico patrioque cum, vel timeam urbanitas cu. Porro fuisset vivendum ne nec, nec ea perpetua constituam. Diam nobis ei mel, has tale blandit reprehendunt an. Quem essent erroribus id duo, ea vide ferri affert duo. Tibique eloquentiam at est, duis placerat nam ne, vel atqui scripta id. Eam ponderum verterem deterruisset ut, vel at etiam munere sensibus. Porro munere aliquando vix ad. Elitr albucius percipitur cu eam. Eu ius putant utroque. Omnis nostro bonorum nam id. No pri tale forensibus dissentiet, in doctus recteque dignissim usu. Lobortis partiendo accommodare nec at, propriae invidunt vituperatoribus ad vim. His placerat dignissim te, in minimum similique efficiantur sit. Elitr theophrastus est ne, ius suas denique prodesset ei. Facilis assentior quaerendum id eam. Pri ei homero elaboraret. Probatus scribentur eam at, movet primis sit ei. Id sit maluisset vituperatoribus, choro graeco ne cum. Ei mea voluptaria intellegebat, vim alia saepe detracto cu. Hinc copiosae gloriatur at vim."
		elif field_type_foreignTable == "SlugField":
			value_foreignTable = str(uuid.uuid1())
		elif field_type_foreignTable == "JSONField":
			value_foreignTable = {str(uuid.uuid1()):str(uuid.uuid1())}
		elif field_type_foreignTable == "PositiveSmallIntegerField":
			value_foreignTable = randint(0, 2147483647)
		elif field_type_foreignTable == "foreignTableKey":
			value_foreignTable = foreignTable(foreig_field.rel.to)
		else:
			print(field_type_foreignTable)
		if value_foreignTable != None:
			setattr(model_foreignTable,foreig_field.__dict__['name'],value_foreignTable)
	model_foreignTable.save()
	return model_foreignTable