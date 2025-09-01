# pydantic 2 badi problem ko solved karna h

# let suppose mujhe data ko add karna h database meto hum kar karege
from pydoc import describe
from fastapi import FastAPI, HTTPException


def insertdata_batabase(name: str, age : int ):
    # ye karne se bas bta rha h mujhe guide kar satke h ye str type ka h ya int type kabut validaton nahi kar satke so 
    if type(name) == str and type(age)==int:
        # also need to add data validation on age to 
        if age <= 0:
            raise HTTPException(status_code=400)
        print(name)
        print(age)
        print("data inserted in database")
    else:
        raise HTTPException(status_code=400, )
  

insertdata_batabase('10' , 10)