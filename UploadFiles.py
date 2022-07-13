import dropbox
import os
from dropbox.files import WriteMode

class TransferData:
    def __init__(self, access_token):
      self.access_token = access_token

    def upload_file(self , file_from , file_to):
      dbx = dropbox.Dropbox(self.access_token)


      for root, dirs, files in os.walk(file_from):
      
        for filename in files:
        

          local_path = os.path.join(root, filename)
        
          relative_path = os.path.relpath(local_path ,file_from)
        
          dropbox_path = os.path.join(file_to , relative_path)

      with open(local_path, 'rb') as f:
        dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))

def main():
    access_token = "sl.BLP2lIIuejK4DdnRNO29ZQppdhSHu-SmQkebos4t5Ia00LELP0dm-jm4wJ6XKrDKLtqY1R9OK5RaGi82tERyxEGOPowQwA40pJCI5e8XB-fVO-yTTEpz2nlmFC1ECkXuRbicOBw"
    transferData = TransferData(access_token)

    file_from = input("Enter the folder path to transfer: ")
    file_to =  input("Enter the entire path to upload to dropbox: ")
     
    transferData.upload_file(file_from , file_to)
    print("File has been moved")

main()