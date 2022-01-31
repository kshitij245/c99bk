import dropbox

class TransferData:
    def __init__(self,access_token):
        self.access_token= access_token

    def upload_files(self,folder_from,folder_to):
        dbx = dropbox.Dropbox(self.access_token)

        f=open(folder_from,'rb')
        dbx.files_upload(f.read(),folder_to)

def main():
    access_token='sl.BBLN6lGizEYnpAx72BJiXpw0yA-vzjk72_wBOqk0iZ-F65vGkgXk-pPxGWxLAyp3Raf4C0Z5DUlzYkKErDjkFBZMVm9dyr9c9CYfp-JUK3SdpEQ-JRhc2_RpBMlmftRh-mUmrgA'
    transferData=TransferData(access_token)
    folder_from=input("enter the  path folder to transfer: ")
    folder_to=input("enter the full path to upload to dropbox: ")
    transferData.upload_files(folder_from,folder_to)
    print("folder has been moved")

main()
        
        
        