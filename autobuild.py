#coding:utf-8
import os
import subprocess
import urllib, httplib
import json

def exeCommand(cmd, needResult=False):
    try:
        if needResult:
            process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
            process.wait()
            return process.stdout.read().strip()
        else:
            process = subprocess.Popen(cmd, shell=True)
            process.wait()
    except Exception, e:
        print(e)

def cleanLastBuild():

    print("clean last compile")
    exeCommands("rm -rf build")

def beginNewBuild():
    
    print("start this compile")
    exeCommands('xcodebuild archive -workspace yourprojectWorkspace.xcworkspace -scheme yourProjectScheme -configuration  DailyBuild -derivedDataPath build -archivePath ./build/Products/yourproject.xcarchive')

def exportIpa():

    print("finish compile，making ipa")
    exeCommands('xcodebuild -exportArchive -archivePath ./build/Products/yourproject.xcarchive -exportOptionsPlist ./adhoc.plist -exportPath ./build/Products')
    print("finish making ipa: ./build/Products/yourproject.ipa" )


#Pgyer key
uKey          = "xxxxxxxxxxxxxxxxxxx"
aKey          = "xxxxxxxxxxxxxxxxxxx"

def uploadIpa():

    cmdstr = u'curl  -F "file=@./build/Products/yourproject.ipa"  -F "uKey=%s" -F "_api_key=%s"  http://www.pgyer.com/apiv1/app/upload' % (uKey, aKey)
    exeCommands(cmdstr)

#autobuild extrance
if __name__ == '__main__':

    os.chdir(os.path.abspath(os.path.dirname(__file__)))

    cleanLastBuild()
    beginNewBuild()

    exportIpa()
    uploadIpa()
