from config.Database import Database

class ArticleSchema:

	def __init__(self):
		pass


	def set_data(self,collection_name, data):	

		articles = {"title":data['title'], 
			        "content":data['content'], 
					"status":data['status']}
		
		return articles

	def save(self,collection_name,data):

		data = self.set_data(collection_name,data)

		db = Database()

		db.create_collection(collection_name,data)




