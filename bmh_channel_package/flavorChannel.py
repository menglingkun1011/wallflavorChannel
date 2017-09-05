# -*- coding:utf-8 -*-
import os
import subprocess

print ("开始多渠道打包中。。。\n\n")

android_home = os.environ["ANDROID_HOME"]

print ("zipalign 对齐中")
zipalign = android_home+"/build-tools/25.0.2/zipalign "+" -v 4 app-release.encrypted.apk app-release.apk"
output=subprocess.call(zipalign, shell=True)
print (output)

print ("\n\n zipalign对齐完成 签名中。。。\n\n")

signApk = android_home+"/build-tools/25.0.2/apksigner "+" sign --ks keys/signtest.jks app-release.apk"
signApkoutput=subprocess.call(signApk, shell=True)

if 0 != signApkoutput :
    print("签名失败")
assert 0 == signApkoutput


print (signApkoutput)

print ("签名完成\n\n")

print ("多渠道打包中。。。\n\n\n")
channel = "java -jar jar/walle-cli-all.jar batch -f jar/channel.txt app-release.apk channel/  "
channelOut = subprocess.call(channel,shell=True)
print (channelOut)
print ("\n\n打包完成！改名中")


path ="channel/"
for file in os.listdir(path):
    if file.startswith("app-release"):
        spFile = file.split("app-release_")
        newName = file.replace(file, spFile[1])
        print(file,"----------->",spFile[1])
        os.rename(os.path.join(path,file), os.path.join(path,spFile[1]))

print ("\n\n改名完成")
