deleteList = ['id','src','scope','absolutePath','exportedSymbols','linearizedBaseContracts','referencedDeclaration','functionReturnParameters']

def delete_id(source):
    # 首先判断是否为dict
    if isinstance(source, dict):
        # 如果是的话，先删除该字典下面的deleteList
        for var in list(source):
            if var in deleteList:
                source.pop(var)

        # 将剩下的元素进行下一轮遍历
        for var in list(source):
            if isinstance(source[var], (dict,list)):
                delete_id(source[var])

    #再判断是否为list
    if isinstance(source,list):
        for var in source:
            if isinstance(var,(dict,list)):
                delete_id(var)

    return source







