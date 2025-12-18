def main(data:str):
    """
    The data is from the file. Find the number of digital and str(non-digital) data and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    f=open(data,'r')
    a=f.read()
    dc=0
    sc=0
    for i in a:
        if i.isdigit():
            dc+=1
        else:
            sc+=1
    return [dc,sc]
print(main('data/data05.txt')) 
# Read data from file