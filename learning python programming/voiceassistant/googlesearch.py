while True:
    try: 
        from googlesearch import search 
    except ImportError:  
        print("No module named 'google' found") 
  
# to search 
    query = input("Enter what you want to search:-")
  
    for j in search(query, tld="co.in",lang="en",num=10,stop=10,pause=2.0): 
        print(j) 
