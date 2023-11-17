collection_prompt = \
"""La base de datos de la aseguradora GNP tiene las siguientes colecciones de documentos:

Colecciones:'''
	Dotal GNP: Ahorrar es un excelente hábito que te permitirá lograr las diferentes metas que te plantees en tu vida. Empieza a ahorrar hoy para garantizarte un futuro digno y recuerda que entre más pronto inicies, tus posibilidades serán mayores. Más que un seguro, es una herramienta financiera que te ayuda a tener un ahorro garantizado para el cumplimiento de tus objetivos, al mismo tiempo que te brinda la tranquilidad de saberte protegido y mantener seguro el bienestar de tu familia.

	Platino Universal GNP: La seguridad económica familiar es muy importante para cada uno de nosotros. Por ello buscar el mecanismo para incrementar nuestro patrimonio y protegernos ante situaciones que no podemos controlar es una prioridad de todos los días. Más que un seguro es un instrumento de protección y ahorro en dólares, el cual te brinda el apoyo que necesitas para concretar tus proyectos, ya que ofrece una alta recuperación de primas en el mediano y largo plazo, al mismo tiempo que garantizas un futuro sólido para tu familia, incluso si llegas a faltar.

	Privilegio Universal GNP: Tener la protección adecuada ante cualquier emergencia te dará tranquilidad en tu vida, pero si combinas esta protección con la formación de un ahorro a mediano y largo plazo, tu patrimonio estará asegurado. Un plan de protección y ahorro en moneda nacional o dólares, que te brinda la tranquilidad de saber que tus seres queridos estarán protegidos, aún en el desafortunado caso de que llegaras a faltar.
	
	Profesional GNP: Asegura su educación o cumple los sueños de los que más quieres. Un Seguro de Vida que te permite generar un ahorro garantizado para apoyar a tu hijo o sobrino en su educación o proyectos, de acuerdo a sus diferentes etapas de vida.

	Trasciende GNP: El respaldo para ti y tu familia de un Seguro GNP de forma vitalicia, con la opción de ahorrar para el cumplimiento de tus objetivos. Es un Seguro de Vida que brinda respaldo a ti y a tu familia, y que te permite elegir el plazo de pago que más se adapte a tus necesidades, además cuenta con una atractiva recuperación de primas con la opción para crear un ahorro adicional.

	Vision Plus GNP: Si eres de las personas que tienen la visión para emprender grandes proyectos, seguramente sabes lo importante que es contar con un respaldo sólido que además de brindarte protección te permita tener un atractivo ahorro.
'''

Dime en cual de estas colecciones puedo encontrar la información que responda a la siguiente pregunta: {pregunta}"""
