def main(data:str):
    """
    The data is from the file. Find the smallest of the numeric characters.
    Args:
        data: str
    Returns:
        int: return answer
    """
    f=open(data,'r')
    a=f.read()
    m=1000
    for i in a:
        if i.isdigit():
            if int(i)<m:
                m=int(i)
    return m
print(main('data/data09.txt'))   
# Read data from file