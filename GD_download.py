import requests
def Download_from_GD(file_id, des_path):
	URL = "https://docs.google.com/uc?export=download"
	session = requests.Session()
	res = session.get(URL, params = { 'id' : file_id }, stream = True)	
	get_content(res, des_path) 
	
def get_content(rescont, path):
	with open(destination, "wb") as f:
		for i in rescont.iter_content():
			if i: 
				f.write(i)
if __name__ == "__main__":
    file_id = input("Enter File ID")
    destination = input("Enter the path to download")
    Download_from_GD(file_id, destination)