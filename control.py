"""
Created by PLSE

control.py      将对应文件进行编译，裁减生成需要对比的AST树
delete.py       裁减算法

"""
import json
import solcx
import os
import solcast
import json_tools
import delete

#调整到当前工作目录，在此之前，需要将比对的文件放入src文件夹和dst文件夹。
workingDir = "/home/yantong/Code/GumTree/test"
os.chdir(workingDir)
#获取子目录
dirNames = os.listdir(workingDir)
#创建对应的Ast目录
if not os.path.exists("srcAst"):
    os.mkdir("srcAst")
if not os.path.exists("dstAst"):
    os.mkdir("dstAst")
if not os.path.exists("srcAst/AstFiles"):
    os.mkdir("srcAst/AstFiles")
if not os.path.exists("srcAst/ModifiedAstFiles"):
    os.mkdir("srcAst/ModifiedAstFiles")
if not os.path.exists("dstAst/AstFiles"):
    os.mkdir("dstAst/AstFiles")
if not os.path.exists("dstAst/ModifiedAstFiles"):
    os.mkdir("dstAst/ModifiedAstFiles")

#需要编译的工程的目录
srcPath = "/src/src/contracts"
dstPath = "/dst/src/contracts"
abstractPath = workingDir+srcPath
srcName = "tokens/erc721-token-receiver.sol"
solcVersion = '0.8.0'
outputRelaDir = "/srcAst/AstFiles"
outputDir = workingDir + outputRelaDir
modifiedRelaDir = "/srcAst/ModifiedAstFiles"
modifiedDir = workingDir + modifiedRelaDir
allowPaths = abstractPath
#更换对应版本
os.system("solc-select use "+solcVersion)

#进行联编
os.chdir(abstractPath)
os.system("solc -o "+outputDir+" --ast-compact-json "+srcName+" --allow-paths "+allowPaths)
#在当前目录下寻找对应的AST文件
AstNames=os.listdir(outputDir)
print(AstNames)
#对每一个文件进行读取，并修剪，存放到ModifiedAstFiles新文件夹
for i in range(0,len(AstNames)):
    with open(outputDir+"/"+AstNames[i],'r') as file:
        data = json.load(file)
        delete.delete_id(data)
    with open(modifiedDir+"/"+AstNames[i][0:len(AstNames[i])-12]+"json",'w') as file:
        file.write(json.dumps(data))

abstractPath = workingDir + dstPath
outputRelaDir = "/dstAst/AstFiles"
outputDir = workingDir + outputRelaDir
modifiedRelaDir = "/dstAst/ModifiedAstFiles"
modifiedDir = workingDir + modifiedRelaDir
allowPaths = abstractPath
#进行联编
os.chdir(abstractPath)
os.system("solc -o "+outputDir+" --ast-compact-json "+srcName+" --allow-paths "+allowPaths)
#在当前目录下寻找对应的AST文件
AstNames=os.listdir(outputDir)
print(AstNames)
#对每一个文件进行读取，并修剪，存放到ModifiedAstFiles新文件夹
for i in range(0,len(AstNames)):
    with open(outputDir+"/"+AstNames[i],'r') as file:
        data = json.load(file)
        delete.delete_id(data)
    with open(modifiedDir+"/"+AstNames[i][0:len(AstNames[i])-12]+"json",'w') as file:
        file.write(json.dumps(data))
