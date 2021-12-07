from fastapi import FastAPI

app = FastAPI()

list_of_usernames = dict()

@app.get("/home/{user_name}")
def w_home(user_name:str,query):
    return{
        "Name":user_name,
        "Age":25,
        "query":query
    }

@app.put("/username/{user_name}")
def put_data(user_name:str):
    print(user_name)
    list_of_usernames.append(user_name)
    return{
        "username":user_name
    }

@app.post("/postdata")
def post_data(user_name: str):
    list_of_usernames.append(user_name)
    return{
        "username":list_of_usernames
    }


@app.delete("/deleteData/{user_name}")
def delete_data(user_name: str):
    list_of_usernames.remove(user_name)
    return{
        "username":list_of_usernames
    }

#for duplication using at a time get,post,put,delete methods
@app.api_route("/homedata",methods=['GET','POST','PUT','DELETE'])
def handle_homedata(username: str):
    print(username)
    return{
        "username":username
    }