import uvicorn

from fastapi import FastAPI, File, UploadFile,Form
#from Image_read import read_imagefile,base
from io import BytesIO
from typing import List
import shutil
import aiofiles
import os
import logging
import base64
app = FastAPI()
logging.basicConfig(filename='test.log', level=logging.DEBUG,
                    format = '%(asctime)s:%(levelname)s:%(name)s:%(message)s')
                  
parent_dir = "D:/AttendanceSupportSystem/"


@app.post("/")
async def getData(base: str = Form(),entityID: str = Form(), schoolID: str = Form()):
    i=0
    
    destination_file_path = "{}/".format(schoolID)
    sub_path="{}".format(entityID)
    path = os.path.join(parent_dir, destination_file_path)
    isdir = os.path.isdir(path)
    if not isdir:
        os.mkdir(path)
    final_path=os.path.join(path,sub_path)
    isfinal=os.path.isdir(final_path)
    if not isfinal:
        os.mkdir(final_path)
     
    decoded_data=base64.b64decode(base)
    file_path = "{}/".format(final_path)  
    #write the decoded data back to original format in  file
    img_file = open(file_path+'image{}.jpeg'.format(i), 'wb')
    i+=1
    img_file.write(decoded_data)
    img_file.close()
        
       
    logging.info("File saved successfully")
    return {'message': 'DONE '}
if __name__ == "__main__":
     uvicorn.run(app, host='127.0.0.1', port=8000)